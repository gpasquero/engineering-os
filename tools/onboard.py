#!/usr/bin/env python3
"""Run the Brownfield Onboarding Skill with Claude, Codex or any frontier model.

    python tools/onboard.py brief  <repository> <project>
    python tools/onboard.py ingest <project> <worker-output.json>
    python tools/onboard.py status <project>

Engineering OS does **not** call a model for you. There is no API key, no
vendor SDK and no network access anywhere in this repository — deliberately.
The worker runs in whatever tool you already use, and this command is the
contract at both ends of it:

    brief    →  writes everything the worker is allowed to see, and the exact
                schema it must return
    ingest   →  validates what came back and turns it into a Candidate
                Engineering Model plus an Engineering Review

**The worker investigates and proposes. It never authorizes, and nothing it
returns reaches the Authoritative Engineering Model without a human curating
it** (`tools/curate.py`).

Typical use, from a clean checkout:

    python tools/onboard.py brief /path/to/your/repo external/yourrepo
    # open external/yourrepo/onboarding-brief.md in Claude Code or Codex,
    # follow it, and save the model's JSON reply as worker-output.json
    python tools/onboard.py ingest external/yourrepo external/yourrepo/worker-output.json
    python tools/curate.py external/yourrepo
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from discovery.mechanical import extract              # noqa: E402
from compiler.registry import load_all                # noqa: E402

GREEN, RED, YELLOW, DIM, BOLD, OFF = (
    "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[1m", "\033[0m")

SKILL = "DS-brownfield-onboarding"
UNCERTAINTY = {"high", "medium", "low"}
TYPES = {"Concept", "Capability", "Invariant", "ADR", "Actor", "Evidence",
         "BoundedContext", "Artifact", "Policy", "Workflow"}


def skill():
    skills = load_all()["REG-discovery-skills"]
    if SKILL not in skills:
        raise SystemExit(f"{SKILL} is not declared in discovery/skills/skills.yaml")
    return skills[SKILL]


# ─────────────────────────────────────────────────────────────── brief

def brief(repository, project):
    project.mkdir(parents=True, exist_ok=True)
    mech = extract(repository)
    (project / "mechanical-engineering-model.json").write_text(
        json.dumps(mech, indent=2) + "\n")

    s = skill()
    try:
        rel = str(project.relative_to(ROOT))
    except ValueError:
        rel = str(project)
    questions = "\n".join(f"{i}. {q}" for i, q in enumerate(s["questions"], 1))
    types = ", ".join(f"`{t}`" for t in s["proposal-types"])

    text = f"""# Brownfield Onboarding — worker briefing

**Repository:** `{mech['repository']}`
**Stack Profile:** `{mech['stackProfile']}`
**Mechanical Model digest:** `{mech['digest']}`
**Skill:** `{SKILL}` (level {s['level']}, non-deterministic)

You are acting as an **expert engineering partner** helping a human team build an
engineering model of a system nobody fully understands any more.

## Your objective

{s['objective'].strip()}

**You are not producing the model.** You are producing proposals and arguments
that let a human reviewer authorize good engineering understanding *faster*.
Five hundred confident proposals nobody can review is a worse result than forty
they can.

## What you may read

`mechanical-engineering-model.json`, in this directory. It contains
{mech['statistics']['documents']} documents, {mech['statistics']['testSuites']} test suites,
{mech['statistics']['routes']} routes, {mech['statistics']['tables']} tables and
{mech['statistics']['moduleDirs']} module directories, each with its file and locator.

You may also open any file it references, to read it. **Do not explore the
repository beyond what the model references** — the model is the agreed evidence
boundary, and a proposal citing something outside it cannot be checked.

## The questions to answer

{questions}

## What you must return

A single JSON document, matching this shape exactly:

```json
{{
  "skill": "{SKILL}",
  "mechanicalModelDigest": "{mech['digest']}",
  "worker": "claude-code",
  "proposals": [
    {{
      "id": "Invariant.RefundWindowIsThirtyDays",
      "type": "Invariant",
      "label": "A refund may not be issued more than 30 days after delivery",
      "source": "docs/policies/refunds.md",
      "locator": "## Refund window",
      "uncertainty": "medium",
      "for": ["The policy document states the limit explicitly.",
              "`refund.service.ts` compares against a 30-day constant."],
      "against": ["No test asserts it, so nothing enforces it mechanically."],
      "recommendation": "authorize"
    }}
  ],
  "relationships": [
    {{"from": "Invariant.RefundWindowIsThirtyDays",
      "predicate": "constrains", "to": "Capability.Refunds",
      "source": "docs/policies/refunds.md", "uncertainty": "medium"}}
  ]
}}
```

**Allowed `type` values:** {types}.

## Rules you must not break

1. **Every proposal cites a `source` a human can open**, and a `locator` inside
   it. A proposal whose evidence is your own judgement is rejected at intake.
2. **`uncertainty` is `high`, `medium` or `low`.** Never a number, never a
   percentage, never a confidence score.
3. **`for` and `against` are both required.** An argument that only makes the
   case *for* is not a review — the reviewer's job would become finding what
   you left out, which is slower than having no review at all.
4. **`recommendation` is advice, not a verdict.** A human decides.
5. **You never write to the model.** Return JSON; that is all.
6. **Say so when you cannot tell.** *"The documents and the code disagree here"*
   is a more valuable proposal than a confident guess.

## Stopping

{s['stopping'].strip()}

Save your reply as `worker-output.json`, then hand it back:

```bash
python tools/onboard.py ingest PROJECT <path-to-worker-output.json>
```
""".replace("PROJECT", rel)

    out = project / "onboarding-brief.md"
    out.write_text(text)
    print(f"  {GREEN}briefing written{OFF}  {out}")
    print(f"  {DIM}mechanical model  {project / 'mechanical-engineering-model.json'}"
          f"  ({mech['statistics']['documents']} documents, "
          f"{mech['statistics']['testSuites']} suites){OFF}")
    print(f"\n  Open the briefing in Claude Code or Codex, follow it, and save the")
    print(f"  JSON reply. Then run:\n")
    print(f"    python tools/onboard.py ingest {project} <worker-output.json>\n")
    return 0


# ────────────────────────────────────────────────────────────── ingest

def ingest(project, reply_path):
    mech_file = project / "mechanical-engineering-model.json"
    if not mech_file.exists():
        raise SystemExit(f"no mechanical model in {project}. Run `brief` first.")
    mech = json.loads(mech_file.read_text())
    try:
        reply = json.loads(pathlib.Path(reply_path).read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"{reply_path} is not valid JSON: {e}\n"
                         f"  Models often wrap JSON in prose or a code fence. "
                         f"Save only the JSON document.")

    problems, proposals = [], reply.get("proposals") or []
    if reply.get("mechanicalModelDigest") != mech["digest"]:
        problems.append(
            f"digest mismatch: the worker saw {reply.get('mechanicalModelDigest')!r}, "
            f"this project has {mech['digest']!r}. The repository changed after the "
            f"briefing was written — re-run `brief` and re-run the worker.")
    if not proposals:
        problems.append("no proposals returned")

    known_sources = set()
    for key, field in (("documents", "file"), ("testSuites", "file"),
                       ("routes", "source"), ("tables", "source"),
                       ("moduleDirs", "path"), ("envRefs", "source"),
                       ("packages", "source")):
        known_sources.update(x[field] for x in mech.get(key, []) if x.get(field))

    entities, reviews, seen = [], [], set()
    for i, p in enumerate(proposals):
        where = f"proposals[{i}] {p.get('id', '?')}"
        for field in ("id", "type", "label", "source", "uncertainty", "for", "against"):
            if not p.get(field):
                problems.append(f"{where}: missing {field!r}")
        if p.get("type") not in TYPES:
            problems.append(f"{where}: type {p.get('type')!r} is not a metamodel entity")
        if p.get("uncertainty") not in UNCERTAINTY:
            problems.append(f"{where}: uncertainty must be high, medium or low")
        for numeric in ("confidence", "score", "probability"):
            if numeric in p:
                problems.append(f"{where}: {numeric!r} is not permitted — "
                                f"Engineering OS has no confidence scores")
        if p.get("id") in seen:
            problems.append(f"{where}: duplicate id")
        seen.add(p.get("id"))
        if p.get("source") and p["source"] not in known_sources:
            problems.append(f"{where}: source {p['source']!r} is not in the "
                            f"Mechanical Model — the worker went outside the "
                            f"evidence boundary")
        if problems:
            continue
        entities.append({
            "id": p["id"], "type": p["type"], "label": p["label"],
            "support": "S-inferred",
            "provenance": {"source": p["source"], "locator": p.get("locator")},
            "origin": {"worker": reply.get("worker", "unnamed"),
                       "task": "T-onboarding", "nondeterministic": True},
            "attributes": {"origin": "O-onboarding-skill", "skill": SKILL,
                           "uncertainty": p["uncertainty"]},
        })
        reviews.append({"subject": p["id"], "for": p["for"], "against": p["against"],
                        "uncertainty": p["uncertainty"],
                        "recommendation": p.get("recommendation", "review")})

    relationships = []
    for i, r in enumerate(reply.get("relationships") or []):
        where = f"relationships[{i}]"
        for field in ("from", "predicate", "to", "source"):
            if not r.get(field):
                problems.append(f"{where}: missing {field!r}")
        if problems:
            continue
        relationships.append({
            "from": r["from"], "predicate": r["predicate"], "to": r["to"],
            "support": "S-inferred",
            "provenance": {"source": r["source"], "locator": r.get("locator")},
            "origin": {"worker": reply.get("worker", "unnamed"),
                       "task": "T-onboarding", "nondeterministic": True},
        })

    if problems:
        print(f"  {RED}rejected — {len(problems)} problem(s){OFF}\n")
        for p in problems[:20]:
            print(f"    {p}")
        if len(problems) > 20:
            print(f"    {DIM}… and {len(problems) - 20} more{OFF}")
        print(f"\n  {DIM}Nothing was written. Fix the worker's output and run "
              f"ingest again.{OFF}\n")
        return 1

    candidate = {
        "candidateModelVersion": "1.0.0",
        "repository": mech["repository"],
        "mechanicalModelDigest": mech["digest"],
        "note": ("Candidate Engineering Model from a NON-DETERMINISTIC worker. "
                 "Nothing here is authoritative. Every proposal requires human "
                 "curation."),
        "proposals": {"entities": entities, "relationships": relationships},
        "statistics": {"entities": len(entities),
                       "relationships": len(relationships)},
    }
    existing = project / "candidate-initial.json"
    if existing.exists():
        backup = project / "candidate-initial.deterministic.json"
        if not backup.exists():
            backup.write_text(existing.read_text())
            print(f"  {DIM}kept the previous candidate model as {backup.name}{OFF}")
    existing.write_text(json.dumps(candidate, indent=2) + "\n")
    (project / "engineering-review.json").write_text(
        json.dumps({"skill": SKILL, "worker": reply.get("worker", "unnamed"),
                    "items": reviews}, indent=2) + "\n")

    print(f"  {GREEN}accepted{OFF}  {len(entities)} proposal(s), "
          f"{len(relationships)} relationship(s)")
    dist = {u: sum(1 for e in entities
                   if e["attributes"]["uncertainty"] == u) for u in
            ("low", "medium", "high")}
    print(f"  {DIM}uncertainty  " + "  ".join(f"{k} {v}" for k, v in dist.items()
                                              if v) + OFF)
    print(f"  {DIM}candidate    {existing}{OFF}")
    print(f"  {DIM}review       {project / 'engineering-review.json'}{OFF}")
    print(f"\n  {YELLOW}Nothing is authoritative yet.{OFF} Next:\n")
    print(f"    python tools/curate.py {project}\n")
    return 0


def status(project):
    print(f"\n  {BOLD}{project}{OFF}")
    for name, label in (("mechanical-engineering-model.json", "mechanical model"),
                        ("onboarding-brief.md", "worker briefing"),
                        ("candidate-initial.json", "candidate model"),
                        ("engineering-review.json", "engineering review"),
                        ("curation-session.json", "curation session"),
                        ("model", "authoritative model")):
        path = project / name
        if not path.exists():
            print(f"    {DIM}—    {label}{OFF}")
            continue
        detail = (f"{len(list(path.glob('*.md')))} sources" if path.is_dir()
                  else f"{path.stat().st_size // 1024 or 1} KB")
        print(f"    {GREEN}✓{OFF}    {label:<22} {DIM}{detail}{OFF}")
    print()
    return 0


def main(argv):
    if len(argv) < 2 or argv[1] in ("--help", "-h"):
        print(__doc__)
        return 0 if len(argv) > 1 else 2
    cmd = argv[1]
    if cmd == "brief" and len(argv) == 4:
        return brief(pathlib.Path(argv[2]).resolve(), ROOT / argv[3])
    if cmd == "ingest" and len(argv) == 4:
        return ingest(ROOT / argv[2], argv[3])
    if cmd == "status" and len(argv) == 3:
        return status(ROOT / argv[2])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
