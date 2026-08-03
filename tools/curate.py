#!/usr/bin/env python3
"""Human Curation — the only stage where a person decides anything.

    python3 tools/curate.py <project>          curate, interactively
    python3 tools/curate.py <project> --report read a finished session

Sessions resume automatically: run the same command again and only undecided
and deferred proposals return.

**Human Curation is a first-class product, not a governance requirement**
(`ADR-0145`). It has existed in this repository since `SESSION-0039` as a filter
function inside a script. **No human has ever used it.**

## What this is

A curation session over a Candidate Engineering Model. Each proposal is shown
with its evidence and, when the Onboarding Skill produced one, its **Engineering
Review** — the argument for and against admitting it (`ADR-0142`).

    a  authorize    it becomes authoritative
    r  reject       it does not, and the reason is recorded
    c  correct      it is admitted with the reviewer's own statement
    d  defer        undecided; it returns in the next session
    ?  evidence     open the cited source and locator
    q  save and stop

## What is measured

Six figures, recorded per proposal, because **the objective of onboarding is not
discovering more — it is letting a reviewer authorize better understanding
faster** (`ADR-0144`):

    proposals generated · accepted · review time · evidence quality
    reviewer corrections · reviewer confidence

**Nothing here is simulated.** A session with no human produces no measurement,
which is the point: `ADR-0144` forbids inventing these numbers.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import os
import sys
import json
import time
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from _cli import help_requested, project as project_arg  # noqa: E402

from compiler.apply import authorize, apply       # noqa: E402

GREEN, RED, YELLOW, BLUE, DIM, BOLD, OFF = (
    "\033[32m", "\033[31m", "\033[33m", "\033[34m", "\033[2m", "\033[1m", "\033[0m")

DECISIONS = {"a": "authorized", "r": "rejected", "c": "corrected", "d": "deferred"}
CONFIDENCE = {"1": "low", "2": "medium", "3": "high"}


def load(project):
    source = project / "candidate-initial.json"
    if not source.exists():
        raise SystemExit(
            f"no Candidate Engineering Model in {project}.\n"
            f"  There is nothing to curate yet. Produce proposals first:\n"
            f"    python discovery/run.py <repository> {project}      "
            f"# deterministic\n"
            f"    python tools/onboard.py brief <repository> {project}  "
            f"# with Claude or Codex")
    candidate = json.loads(source.read_text())
    reviews = {}
    review_file = project / "engineering-review.json"
    if review_file.exists():
        reviews = {r["subject"]: r for r in json.loads(review_file.read_text())["items"]}
    session_file = project / "curation-session.json"
    session = (json.loads(session_file.read_text()) if session_file.exists()
               else {"decisions": {}, "reviewer": None, "seconds": 0.0})
    return candidate, reviews, session, session_file


def show(entity, review, n, total, rels):
    print(f"\n{DIM}{'─' * 74}{OFF}")
    print(f"{DIM}{n}/{total}{OFF}  {BOLD}{entity['type']}{OFF}  {entity['label']}")
    print(f"      {DIM}{entity['id']}{OFF}")
    p = entity["provenance"]
    print(f"\n  evidence   {p['source']}")
    if p.get("locator"):
        print(f"             {DIM}{p['locator']}{OFF}")
    print(f"  support    {entity['support']}"
          f"   {DIM}{(entity.get('attributes') or {}).get('rule', '')}{OFF}")
    origin = entity.get("origin") or {}
    if origin.get("nondeterministic"):
        print(f"  producer   {YELLOW}non-deterministic{OFF} "
              f"{DIM}{origin.get('worker', '')} — would not repeat itself{OFF}")
    for r in rels[:4]:
        print(f"  relation   {r['predicate']} → {r['to']}   {DIM}{r['support']}{OFF}")

    if review:
        print(f"\n  {BLUE}engineering review{OFF}")
        for line in (review.get("for") or []):
            print(f"    {GREEN}+{OFF} {line}")
        for line in (review.get("against") or []):
            print(f"    {RED}−{OFF} {line}")
        if review.get("uncertainty"):
            print(f"    {DIM}uncertainty: {review['uncertainty']}{OFF}")
        if review.get("recommendation"):
            print(f"    {DIM}skill recommends: {review['recommendation']}{OFF}")


def report(project, session, candidate):
    d = session["decisions"]
    total = len(candidate["proposals"]["entities"])
    counts = {k: sum(1 for v in d.values() if v["decision"] == k)
              for k in set(DECISIONS.values())}
    seen = len(d)
    seconds = session.get("seconds", 0.0)
    print(f"\n{DIM}{'─' * 74}{OFF}\n{BOLD}CURATION SESSION{OFF}   "
          f"{session.get('reviewer') or 'unattributed'}\n{DIM}{'─' * 74}{OFF}")
    print(f"  proposals generated   {total}")
    print(f"  reviewed              {seen}")
    for k in ("authorized", "corrected", "rejected", "deferred"):
        print(f"  {k:<21} {counts.get(k, 0)}")
    if seen:
        print(f"  review time           {seconds / 60:.1f} min"
              f"   {DIM}{seconds / seen:.1f}s per proposal{OFF}")
        accepted = counts.get("authorized", 0) + counts.get("corrected", 0)
        print(f"  {BOLD}accepted per minute   {accepted / (seconds / 60):.1f}{OFF}"
              f"   {DIM}the figure onboarding is optimized for (ADR-0144){OFF}")
        print(f"  reviewer corrections  {counts.get('corrected', 0)}"
              f"   {DIM}a proposal right enough to keep and wrong as stated{OFF}")
        conf = [v["confidence"] for v in d.values() if v.get("confidence")]
        if conf:
            dist = {c: conf.count(c) for c in ("high", "medium", "low")}
            print(f"  reviewer confidence   "
                  + "  ".join(f"{k} {v}" for k, v in dist.items() if v))
        ev = [v["evidence"] for v in d.values() if v.get("evidence")]
        if ev:
            dist = {c: ev.count(c) for c in ("high", "medium", "low")}
            print(f"  evidence quality      "
                  + "  ".join(f"{k} {v}" for k, v in dist.items() if v))
    print(f"\n{DIM}  Nothing above is simulated. A session with no human produces\n"
          f"  no measurement, which is the point (ADR-0144).{OFF}")


def main(argv):
    if help_requested(argv):
        print(__doc__)
        return 0
    if len(argv) < 2:
        print(__doc__)
        return 2
    project = project_arg(argv[1], must_have_model=False)
    candidate, reviews, session, session_file = load(project)
    entities = candidate["proposals"]["entities"]
    rels = {}
    for r in candidate["proposals"]["relationships"]:
        rels.setdefault(r["from"], []).append(r)

    if "--report" in argv:
        report(project, session, candidate)
        return 0

    if not sys.stdin.isatty():
        print(f"{YELLOW}Human Curation requires a human.{OFF}\n"
              f"{DIM}  This tool refuses to run without a terminal. A curation\n"
              f"  session produced by a script would generate exactly the\n"
              f"  reviewer-efficiency numbers ADR-0144 forbids inventing.{OFF}")
        return 1

    if not session.get("reviewer"):
        session["reviewer"] = input("reviewer: ").strip() or os.environ.get("USER", "?")

    pending = [e for e in entities
               if session["decisions"].get(e["id"], {}).get("decision")
               in (None, "deferred")]
    print(f"\n{len(pending)} proposal(s) to review. "
          f"{DIM}a authorize · r reject · c correct · d defer · ? evidence · q stop{OFF}")

    try:
        for i, entity in enumerate(pending, start=1):
            show(entity, reviews.get(entity["id"]), i, len(pending),
                 rels.get(entity["id"], []))
            started = time.monotonic()
            while True:
                choice = input(f"\n  {BOLD}decision{OFF} [a/r/c/d/?/q] ").strip().lower()
                if choice == "?":
                    print(f"    {DIM}{entity['provenance']['source']}"
                          f"  {entity['provenance'].get('locator') or ''}{OFF}")
                    continue
                if choice == "q":
                    raise KeyboardInterrupt
                if choice in DECISIONS:
                    break
            record = {"decision": DECISIONS[choice]}
            if choice == "c":
                record["statement"] = input("  corrected statement: ").strip()
            if choice == "r":
                record["reason"] = input("  reason: ").strip()
            if choice in ("a", "c"):
                record["confidence"] = CONFIDENCE.get(
                    input("  your confidence [1 low / 2 medium / 3 high] ").strip(),
                    "medium")
                record["evidence"] = CONFIDENCE.get(
                    input("  evidence quality [1 low / 2 medium / 3 high] ").strip(),
                    "medium")
            session["seconds"] += time.monotonic() - started
            session["decisions"][entity["id"]] = record
            session_file.write_text(json.dumps(session, indent=2) + "\n")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{DIM}  saved{OFF}")

    session_file.write_text(json.dumps(session, indent=2) + "\n")
    report(project, session, candidate)

    accepted = {k for k, v in session["decisions"].items()
                if v["decision"] in ("authorized", "corrected")}
    if accepted and input("\n  apply to the authoritative model? [y/N] ").strip().lower() == "y":
        auth, rejected, diags = authorize(
            candidate, accept_ids=accepted,
            accept_support={"S-inferred", "S-specified", "S-tested",
                            "S-implemented", "S-confirmed-deterministic"},
            reviewer=session["reviewer"])
        apply(auth, project)
        print(f"  {GREEN}{len(auth['entities'])} entities applied{OFF}, "
              f"{len(rejected)} rejected by coherence")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
