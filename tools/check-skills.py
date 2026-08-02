#!/usr/bin/env python3
"""Verify the Discovery Skill contracts (ADR-0113).

A Skill is an engine-independent investigation contract. Three properties make it
one, and each is checked:

  * **eleven declared fields** — a contract missing a stopping condition or an
    output schema is a prompt;
  * **no model or vendor named** — the Skill belongs to Engineering OS and the
    model is only a worker implementation;
  * **independently runnable** — a skill that requires another skill's output
    cannot be tested alone. Only synthesis and gap discovery may.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.registry import load_all  # noqa: E402

VALID_TYPES = {"Concept", "Capability", "BoundedContext", "Invariant", "Actor",
               "ADR", "Workflow", "WorkflowStep", "Artifact", "Evidence",
               "relationship"}
REQUIRED = ["kind", "level", "objective", "required-inputs", "evidence", "questions",
            "permitted-tools", "proposal-types", "provenance", "uncertainty",
            "stopping", "output-schema", "review"]
VENDORS = ("claude", "codex", "gpt", "gemini", "anthropic", "openai", "llama",
           "mistral", "sonnet", "opus")
MAY_DEPEND = {"DS-gap-discovery", "DS-candidate-synthesis"}
GREEN, RED, OFF = "\033[32m", "\033[31m", "\033[0m"


def main():
    skills = load_all()["REG-discovery-skills"]
    failures = []
    width = max(len(s) for s in skills)
    print(f"Discovery Skill contracts — {len(skills)} skills, "
          f"{len(REQUIRED)} required fields\n")

    for sid, skill in skills.items():
        problems = []
        missing = [f for f in REQUIRED if f not in skill]
        if missing:
            problems.append(f"missing {missing}")
        blob = str(skill).lower()
        named = [v for v in VENDORS if v in blob]
        if named:
            problems.append(f"names a model or vendor: {named}")
        depends = any("candidate-proposals" in str(i)
                      for i in (skill.get("required-inputs") or []))
        if depends and sid not in MAY_DEPEND:
            problems.append("requires another skill's output; not independently runnable")
        level = skill.get("level")
        if level not in (1, 2, 3):
            problems.append(f"level must be 1, 2 or 3, got {level!r}")
        if level == 3 and skill.get("kind") != "domain":
            problems.append("level 3 is reserved for domain skills")
        kind = skill.get("kind")
        if kind not in ("general", "technology", "domain"):
            problems.append(f"kind must be general, technology or domain, "
                            f"got {kind!r}")
        if kind == "domain" and not skill.get("domain"):
            problems.append("a domain skill must name its business domain")
        if kind == "technology" and not skill.get("technology"):
            problems.append("a technology skill must name its technology")
        # A skill reads the Mechanical Engineering Model. One that reads the
        # repository is a Stack Profile wearing a skill's name (ADR-0121).
        for tool in skill.get("permitted-tools") or []:
            if "repositor" in tool or "file" in tool or "grep" in tool:
                problems.append(f"permitted-tool {tool!r} reads the repository; "
                                f"a skill reads the Mechanical Model (ADR-0121)")

        # proposal-types must name real metamodel entities. A blind worker
        # reported that nothing flagged a proposal typed outside the list; the
        # list itself was never checked either.
        bad_types = [p for p in (skill.get("proposal-types") or [])
                     if p not in VALID_TYPES]
        if bad_types:
            problems.append(f"proposal-types names unknown type(s) {bad_types}")

        # Evidence must name Mechanical Model parts, never files (ADR-0108).
        tools = [str(t) for t in (skill.get("permitted-tools") or [])]
        if any("source" in t and "read-source" in t for t in tools) and \
                "F-fact-absent" not in str(skill):
            problems.append("permits source reading without an F-fact-absent justification")

        mark = f"{GREEN}OK  {OFF}" if not problems else f"{RED}FAIL{OFF}"
        print(f"  {mark}  {sid:<{width}}  {skill['objective'].strip().splitlines()[0][:52]}")
        for p in problems:
            print(f"        {RED}{p}{OFF}")
            failures.append(f"{sid}: {p}")

    print()
    if failures:
        print(f"{RED}{len(failures)} contract defect(s){OFF}")
        return 1
    print(f"{GREEN}every skill declares a complete, engine-independent contract{OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
