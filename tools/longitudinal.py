#!/usr/bin/env python3
"""Longitudinal validation — does engineering understanding survive time?

    python3 tools/longitudinal.py <repo> <project> <commit> [<commit> ...]

**The central promise of Engineering OS, and the one no benchmark can test**
(`ADR-0122`). A benchmark measures a single moment. This measures a model that
was acquired once and then had to survive real engineering changes.

    t0    Initial Acquisition, then curation
    t1..  a real commit → mechanical delta → Continuous Acquisition
    every REACQUIRE_EVERY steps, Periodic Reacquisition and a Knowledge Drift
    Report — which challenges the maintained model and never replaces it

At every step the model is measured by the **engineering questions it can
answer** (`ADR-0120`), not by how large it became.

The repository is never modified: each commit is materialised as a detached
`git worktree` (`SESSION-0043`).

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import io
import sys
import json
import shutil
import pathlib
import contextlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from discovery.mechanical import extract                    # noqa: E402
from discovery.interpretive import interpret                # noqa: E402
from discovery.candidate import Candidate                   # noqa: E402
from discovery.continuous import acquire, delta, _index      # noqa: E402
from discovery import drift                                 # noqa: E402
from compiler.apply import authorize, apply                 # noqa: E402
from compiler import compile_project                        # noqa: E402
from compiler.registry import load_all                      # noqa: E402
from compiler.query import load_queries                     # noqa: E402
sys.path.insert(0, str(ROOT / "tools"))
from measure import score_all, retention
from guidance import guidance                               # noqa: E402

REACQUIRE_EVERY = 4
BAR = "─" * 74
GREEN, RED, YELLOW, DIM, OFF = ("\033[32m", "\033[31m", "\033[33m",
                                "\033[2m", "\033[0m")

# The curation a team would plausibly maintain: the subsystems it owns. Applied
# identically at every step, because a team whose curation policy drifts is
# measuring its own inconsistency rather than the tool's.
KEEP = ("Auth", "Jwt", "RefreshToken", "Lockout", "Password", "Sla",
        "BusinessHours", "TenantIsolation", "Rls", "Ticket", "Inbox",
        "Contact", "Company", "Attachment", "Email", "Csat")


def keep(node_id):
    return any(k in node_id for k in KEEP)


def worktree(repo, commit, at):
    if at.exists():
        shutil.rmtree(at, ignore_errors=True)
    subprocess.run(["git", "-C", str(repo), "worktree", "prune"],
                   capture_output=True)
    r = subprocess.run(["git", "-C", str(repo), "worktree", "add", "--detach",
                        str(at), commit], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"worktree {commit}: {r.stderr.strip()}")
    return at


def measure(project, questions, queries):
    ckm, problems = compile_project(project)
    if problems:
        return None, f"{len(problems)} diagnostic(s)"
    return score_all(ckm, questions, queries), None


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    repo = pathlib.Path(argv[1]).resolve()
    project = ROOT / argv[2]
    commits = argv[3:]

    # Reset the MODEL, never the project. The first version removed the whole
    # directory and deleted `LONGITUDINAL.md` — the report the suite exists to
    # produce — on its second run. A permanent benchmark may not destroy its own
    # record (ADR-0129).
    shutil.rmtree(project / "model", ignore_errors=True)
    (project / "model").mkdir(parents=True, exist_ok=True)
    questions = load_all()["REG-engineering-questions"]
    queries = load_queries()
    at = pathlib.Path("/tmp/eos-longitudinal")
    timeline = []

    # ── t0 ────────────────────────────────────────────────────────────────
    print(f"{BAR}\nt0  INITIAL ACQUISITION  {commits[0]}\n{BAR}")
    worktree(repo, commits[0], at)
    mech = extract(at)
    cand = Candidate(str(at), project)
    interpret(mech, cand, "both-levels")
    model = cand.serialize()
    proposed = len(model["proposals"]["entities"])
    ids = {e["id"] for e in model["proposals"]["entities"] if keep(e["id"])}
    auth, _, _ = authorize(model, accept_ids=ids,
                           accept_support={"S-inferred", "S-specified"},
                           reviewer="Project Owner (gpasquero)")
    apply(auth, project)
    scores, err = measure(project, questions, queries)
    ckm_t0, _ = compile_project(project)
    touched = set()          # every source the repository changed after t0
    print(f"   proposed {proposed}   curated {len(auth['entities'])}   "
          f"answered {scores['answered']}/{scores['total']}")
    timeline.append({"step": "t0", "commit": commits[0], "kind": "initial",
                     "proposed": proposed, "accepted": len(auth["entities"]),
                     "cost": proposed, "answered": scores["answered"],
                     "total": scores["total"], "states": scores["states"]})

    prev_mech = mech
    # ── t1.. ──────────────────────────────────────────────────────────────
    for i, commit in enumerate(commits[1:], start=1):
        worktree(repo, commit, at)
        mech = extract(at)
        ckm_before, _ = compile_project(project)
        auth_ids = {n["id"] for n in ckm_before["nodes"]}
        inc, inc_report = acquire(prev_mech, mech, auth_ids)
        # Resolve each delta key to the SOURCE PATH it concerns. The keys are
        # heterogeneous — a suite is a path, a table is a name, a route is a
        # verb and a path — and substring-matching them against provenance
        # over-matched badly enough to leave two untouched subjects out of ten.
        d = delta(prev_mech, mech)
        idx_a, idx_b = _index(mech), _index(prev_mech)
        for kind, key in (("suites", "file"), ("tables", "source"),
                          ("modules", "path"), ("routes", "source"),
                          ("docs", "file")):
            for bucket in ("added", "removed", "changed"):
                for k in d[kind].get(bucket) or []:
                    item = idx_a[kind].get(k) or idx_b[kind].get(k) or {}
                    if item.get(key):
                        touched.add(item[key])
        ents = inc["proposals"]["entities"]
        ids = {e["id"] for e in ents if keep(e["id"])}
        auth, _, _ = authorize(inc, accept_ids=ids,
                               accept_support={"S-inferred", "S-specified"},
                               reviewer="Project Owner (gpasquero)")
        apply(auth, project)
        scores, err = measure(project, questions, queries)
        full = len(interpret_count(mech))
        pct = 100 * len(ents) / full if full else 0
        print(f"{BAR}\nt{i}  CONTINUOUS  {commit}\n{BAR}")
        print(f"   incremental {len(ents):3}   would be {full:3} on a full rerun"
              f"   {pct:.1f}%   curated {len(auth['entities'])}   "
              f"retractions {len(inc_report['retractions'])}   "
              f"answered {scores['answered']}/{scores['total']}")
        timeline.append({"step": f"t{i}", "commit": commit, "kind": "continuous",
                         "proposed": len(ents), "accepted": len(auth["entities"]),
                         "cost": len(ents), "fullRerun": full,
                         "retractions": len(inc_report["retractions"]),
                         "answered": scores["answered"], "total": scores["total"],
                         "states": scores["states"]})

        if i % REACQUIRE_EVERY == 0 or commit == commits[-1]:
            fresh = Candidate(str(at), project)
            interpret(mech, fresh, "both-levels")
            fresh_model = fresh.serialize()
            ckm, _ = compile_project(project)
            report = drift.report(ckm["nodes"], ckm["edges"], fresh_model,
                                  {e["id"] for e in ents})
            counts = {k: len(v) for k, v in (report.get("items") or {}).items() if v}
            print(f"   {YELLOW}periodic reacquisition{OFF}  "
                  f"{len(fresh_model['proposals']['entities'])} fresh proposals, "
                  f"NOT applied")
            for k, v in sorted(counts.items()):
                print(f"      {k:42} {v}")
            timeline[-1]["drift"] = counts
            timeline[-1]["reacquired"] = len(fresh_model["proposals"]["entities"])

        prev_mech = mech

    # ── verdict ───────────────────────────────────────────────────────────
    print(f"\n{BAR}\nLONGITUDINAL RESULT\n{BAR}")
    print(f"   {'step':5} {'kind':11} {'cost':>6} {'rerun':>6} {'%':>6}  answered")
    for row in timeline:
        full = row.get("fullRerun")
        pct = f"{100 * row['cost'] / full:.1f}%" if full else "—"
        print(f"   {row['step']:5} {row['kind']:11} {row['cost']:6} "
              f"{full if full else '—':>6} {pct:>6}  "
              f"{row['answered']}/{row['total']}")
    # Knowledge Growth and Understanding Growth are different things and are
    # never again reported as one (ADR-0127).
    r = retention(timeline[0]["states"], timeline[-1]["states"])
    print(f"\n   {'Knowledge Growth':<24} "
          f"{timeline[0]['accepted']} → {len(list((project / 'model').glob('*.md')))} "
          f"curated sources   {DIM}implementation telemetry{OFF}")
    print(f"   {'Understanding Growth':<24} "
          f"{timeline[0]['answered']}/{timeline[0]['total']} → "
          f"{timeline[-1]['answered']}/{timeline[-1]['total']} questions answered")
    rate = "—" if r["rate"] is None else f"{100 * r['rate']:.0f}%"
    print(f"   {'Understanding Retention':<24} {rate}   "
          f"{DIM}of {r['previouslyAnswered']} answered at t0: "
          f"{r['retained']} retained, {r['degraded']} degraded, "
          f"{r['lost']} lost; {r['gained']} gained{OFF}")
    for qid, move in sorted(r["moves"].items()):
        if move in ("retained", "degraded", "lost", "gained"):
            colour = {"retained": GREEN, "gained": GREEN,
                      "degraded": YELLOW, "lost": RED}[move]
            print(f"      {colour}{move:9}{OFF} {qid}")

    # Guidance Preservation, over subjects whose evidence nobody touched. A
    # subject the repository changed SHOULD get different advice; only an
    # untouched one makes drift meaningful (ADR-0139).
    ckm_t9, _ = compile_project(project)
    untouched = {n["id"] for n in ckm_t0["nodes"]
                 if (n.get("attributes") or {}).get("source") not in touched}
    g = guidance(ckm_t0, ckm_t9, untouched)
    grate = "—" if g["rate"] is None else f"{100 * g['rate']:.0f}%"
    print(f"   {'Guidance Preservation':<24} {grate}   "
          f"{DIM}{g['judged']} pairs over {g['subjects']} untouched subjects: "
          f"{g['counts']['stable']} stable, {g['counts']['changed']} changed, "
          f"{g['counts']['lost']} lost{OFF}")
    for row in g["rows"]:
        if row["state"] in ("changed", "lost"):
            print(f"      {YELLOW if row['state'] == 'changed' else RED}"
                  f"{row['state']:9}{OFF} {row['subject']}  {row['recommendation']}")

    first, last = timeline[0], timeline[-1]
    maint = [r for r in timeline if r["kind"] == "continuous"]
    total_maint = sum(r["cost"] for r in maint)
    print(f"\n   acquired once at {first['cost']} proposals; "
          f"maintained across {len(maint)} changes at {total_maint} more "
          f"({100 * total_maint / first['cost']:.0f}% of one acquisition)")
    # The verdict may NOT be read off coverage alone. Coverage was flat at 1/9
    # for ten steps while retention was 0% — the one question answered at t0 was
    # lost and a different one gained. "Understanding held" would have been a
    # true sentence about a false thing (ADR-0128).
    delta_q = last["answered"] - first["answered"]
    if r["rate"] is not None and r["rate"] < 1:
        verdict = (f"{RED}understanding did not survive{OFF} — coverage moved "
                   f"{delta_q:+d} and retention is {100 * r['rate']:.0f}%")
    else:
        verdict = (f"{GREEN}understanding grew{OFF}" if delta_q > 0 else
                   f"{YELLOW}understanding held{OFF}" if delta_q == 0 else
                   f"{RED}understanding decayed{OFF}")
    print(f"   engineering questions: {first['answered']}/{first['total']} → "
          f"{last['answered']}/{last['total']}   {verdict}")

    (project / "longitudinal.json").write_text(json.dumps(
        {"repository": str(repo), "timeline": timeline, "retention": r,
         "guidance": {k: v for k, v in g.items() if k != "rows"}},
        indent=2) + "\n")
    return 0


def interpret_count(mech):
    """What a full rerun would propose — the denominator for maintenance cost."""
    c = Candidate("/dev/null", pathlib.Path("/tmp"))
    interpret(mech, c, "both-levels")
    return c.serialize()["proposals"]["entities"]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
