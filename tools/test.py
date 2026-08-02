#!/usr/bin/env python3
"""The Engineering OS regression suite.

**Knowledge repositories are executable test fixtures.** Each project under
`tests/projects/` is a minimal repository exercising one architectural feature,
and declares its expected outcome in `expected.md`.

Every compiler change rebuilds every project. A project that should compile and
does not, or that should fail and compiles, is a regression.

Negative fixtures matter as much as positive ones: they are what proves the
metamodel is an executable contract rather than a description.

Usage:
    python3 tools/test.py            run every project
    python3 tools/test.py <name>     run one

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import re
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "tests/projects"
sys.path.insert(0, str(ROOT / "tools"))

from compile import compile_project, emit  # noqa: E402

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"


def read_expectation(project):
    text = (project / "expected.md").read_text()
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1)

    def scalar(k):
        m = re.search(rf"^{k}:\s*(.+)$", fm, re.M)
        return m.group(1).strip() if m else None

    def items(k):
        m = re.search(rf"^{k}:\s*\n((?:\s+-\s.*\n?)+)", fm, re.M)
        return [re.sub(r'^["\']|["\']$', "", v.strip())
                for v in re.findall(r"^\s+-\s*(.+)$", m.group(1), re.M)] if m else []

    inline = scalar("expected-categories")
    cats = ([c.strip() for c in inline.strip("[]").split(",")] if inline else []) or items("expected-categories")
    return {
        "id": scalar("id"), "exercises": scalar("exercises"),
        "outcome": scalar("outcome"),
        "nodes": int(scalar("expected-nodes")) if scalar("expected-nodes") else None,
        "edges": int(scalar("expected-edges")) if scalar("expected-edges") else None,
        "categories": [c for c in cats if c],
        "errors": items("expected-errors"),
    }


def check(project):
    """Returns (ok, [failure descriptions], ckm|None)."""
    exp = read_expectation(project)
    ckm, errors = compile_project(project, quiet=True)
    bad = []

    if exp["outcome"] == "pass":
        if errors:
            return False, [f"expected to compile, failed with: {e}" for e in errors], None
        s = ckm["statistics"]
        if exp["nodes"] is not None and s["nodes"] != exp["nodes"]:
            bad.append(f"expected {exp['nodes']} nodes, got {s['nodes']}")
        if exp["edges"] is not None and s["edges"] != exp["edges"]:
            bad.append(f"expected {exp['edges']} edges, got {s['edges']}")
        for cat in exp["categories"]:
            if cat not in s["byCategory"]:
                bad.append(f"expected relationship category '{cat}', absent")
        # determinism: the same input must produce a byte-identical model
        again, _ = compile_project(project, quiet=True)
        if json.dumps(again, sort_keys=False) != json.dumps(ckm, sort_keys=False):
            bad.append("NON-DETERMINISTIC: two compilations produced different models")
    elif exp["outcome"] == "fail":
        if not errors:
            bad.append("expected compilation to FAIL, it succeeded")
        for want in exp["errors"]:
            if not any(want in e for e in errors):
                bad.append(f"expected error containing {want!r}; got {errors}")
    else:
        bad.append(f"unknown expected outcome {exp['outcome']!r}")

    return not bad, bad, ckm


def main(argv):
    names = [argv[1]] if len(argv) > 1 else sorted(p.name for p in PROJECTS.iterdir() if p.is_dir())
    width = max(len(n) for n in names)
    failures = 0

    print(f"Engineering OS regression suite — {len(names)} project(s)\n")
    for name in names:
        project = PROJECTS / name
        exp = read_expectation(project)
        ok, bad, ckm = check(project)
        tag = f"{GREEN}PASS{OFF}" if ok else f"{RED}FAIL{OFF}"
        detail = (f"{ckm['statistics']['nodes']}n {ckm['statistics']['edges']}e"
                  if ckm else f"rejected as expected" if exp["outcome"] == "fail" else "")
        print(f"  {tag}  {name:<{width}}  {DIM}{exp['outcome']:<4} {detail}{OFF}")
        print(f"        {DIM}{exp['exercises']}{OFF}")
        for b in bad:
            print(f"        {RED}{b}{OFF}")
            failures += 1
        if ok and ckm:
            emit(project, ckm)

    print()
    if failures:
        print(f"{RED}{failures} failure(s){OFF}")
        return 1
    print(f"{GREEN}all {len(names)} project(s) behaved as declared{OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
