#!/usr/bin/env python3
"""The Engineering OS regression suite.

**Knowledge repositories are executable regression assets.** Each project under
`tests/projects/` is a minimal repository exercising one architectural feature.

Every fixture verifies:

    CKM  ·  OWL  ·  Explorer  ·  Graph  ·  deterministic rebuild  ·  diagnostics
    ·  declared query results  ·  agreement between both query engines

Golden outputs live in `tests/projects/<name>/golden/`. A change to any emitter
that alters output shows up as a diff in every affected fixture.

Usage:
    python3 tools/test.py               run every project
    python3 tools/test.py <name>        run one
    python3 tools/test.py --accept      rewrite golden outputs from current behaviour

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import re
import sys
import difflib
import pathlib
import subprocess

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler import compile_project, emit_all, EMITTERS  # noqa: E402
from compiler.query import Model, run as run_query, load_queries  # noqa: E402

QUERIES = load_queries()

PROJECTS = ROOT / "tests/projects"
GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"


def expectation(project):
    fm = re.match(r"^---\n(.*?)\n---\n", (project / "expected.md").read_text(), re.S).group(1)
    return yaml.safe_load(fm)


def diff(name, want, got):
    lines = list(difflib.unified_diff(want.splitlines(), got.splitlines(),
                                      f"golden/{name}", f"built/{name}", lineterm="", n=1))
    return lines[:14]


def check(project, accept=False):
    exp = expectation(project)
    outcome = exp.get("outcome")
    ckm, problems = compile_project(project)
    bad = []

    if outcome == "fail":
        if not problems:
            return ["expected compilation to FAIL, it succeeded"], None
        for want in exp.get("expected-errors", []):
            if not any(want in str(d) for d in problems):
                bad.append(f"expected diagnostic containing {want!r}; got {[str(d) for d in problems]}")
        for want in exp.get("expected-phase", []) if isinstance(exp.get("expected-phase"), list) else []:
            if not any(d.phase == want for d in problems):
                bad.append(f"expected a diagnostic at phase {want!r}")
        if exp.get("expected-phase") and isinstance(exp["expected-phase"], str):
            if not any(d.phase == exp["expected-phase"] for d in problems):
                bad.append(f"expected a diagnostic at phase {exp['expected-phase']!r}; "
                           f"got {sorted({d.phase for d in problems})}")
        if exp.get("expected-rule"):
            if not any(d.rule == exp["expected-rule"] for d in problems):
                bad.append(f"expected rule {exp['expected-rule']} to fire; "
                           f"got {sorted({d.rule for d in problems if d.rule})}")
        return bad, None

    if problems:
        return [f"expected to compile, failed: ({d.phase}) {d}" for d in problems], None

    s = ckm["statistics"]
    for key, actual in (("expected-nodes", s["nodes"]), ("expected-edges", s["edges"])):
        if exp.get(key) is not None and exp[key] != actual:
            bad.append(f"{key}: expected {exp[key]}, got {actual}")
    for cat in exp.get("expected-categories") or []:
        if cat not in s["byCategory"]:
            bad.append(f"expected relationship category '{cat}', absent")

    # declared query results (ADR-0086): a question is answered only if a fixture says so
    for qid, want in (exp.get("expected-queries") or {}).items():
        query = QUERIES.get(qid)
        if not query:
            bad.append(f"expected-queries names unknown query {qid!r}")
            continue
        subject = want.get("subject")
        got = sorted(r.get("id") or f"{r['from']}>{r['to']}"
                     for r in run_query(Model(ckm), query, subject))
        if sorted(want.get("rows", [])) != got:
            bad.append(f"{qid}({subject}): expected {sorted(want.get('rows', []))}, got {got}")

    # deterministic rebuild
    again, _ = compile_project(project)
    if again != ckm:
        bad.append("NON-DETERMINISTIC: two compilations produced different models")

    # golden outputs for every emitter
    _, written = emit_all(project, ckm)
    golden = project / "golden"
    if accept:
        golden.mkdir(exist_ok=True)
        for name, text in written.items():
            (golden / name).write_text(text)
    else:
        for name in sorted(EMITTERS):
            path = golden / name
            if not path.exists():
                bad.append(f"golden/{name} missing — run --accept")
            elif path.read_text() != written[name]:
                bad.append(f"golden/{name} differs:\n" + "\n".join(
                    "          " + line for line in diff(name, path.read_text(), written[name])))
    return bad, ckm


def main(argv):
    accept = "--accept" in argv
    argv = [a for a in argv if a != "--accept"]
    names = [argv[1]] if len(argv) > 1 else sorted(p.name for p in PROJECTS.iterdir() if p.is_dir())
    width = max(len(n) for n in names)
    failures = 0

    mode = f" {YELLOW}[--accept: rewriting golden outputs]{OFF}" if accept else ""
    print(f"Engineering OS regression suite — {len(names)} project(s){mode}\n")
    for name in names:
        project = PROJECTS / name
        exp = expectation(project)
        bad, ckm = check(project, accept)
        tag = f"{GREEN}PASS{OFF}" if not bad else f"{RED}FAIL{OFF}"
        detail = (f"{ckm['statistics']['nodes']}n {ckm['statistics']['edges']}e"
                  if ckm else "rejected as expected" if exp.get("outcome") == "fail" else "")
        print(f"  {tag}  {name:<{width}}  {DIM}{exp.get('outcome',''):<4} {detail}{OFF}")
        print(f"        {DIM}{exp.get('exercises','')}{OFF}")
        for b in bad:
            print(f"        {RED}{b}{OFF}")
            failures += 1

    print()
    engines = subprocess.run([sys.executable, str(ROOT / "tools/check-engines.py")],
                             capture_output=True, text=True)
    for line in engines.stdout.strip().splitlines():
        print("  " + line)
    if engines.returncode:
        failures += 1

    print()
    if failures:
        print(f"{RED}{failures} failure(s){OFF}")
        return 1
    print(f"{GREEN}all {len(names)} project(s) behaved as declared{OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
