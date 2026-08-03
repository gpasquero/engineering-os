#!/usr/bin/env python3
"""Verify an Engineering OS installation. Run this first.

    python tools/check.py
    python tools/check.py --quick     dependencies and compiler health only

Checks, in order:

    1. Python version and required dependencies
    2. Git, and the optional dependency
    3. Registry consistency          — 20 declared registries load
    4. Governance consistency        — the decision corpus is internally sound
    5. Fixtures                      — every test project behaves as declared
    6. Query-engine parity           — both engines agree on every question
    7. Deterministic generation      — the same sources produce the same model
    8. Compiler health               — the bundled example compiles and emits

Exit code 0 means the installation is usable. Anything else prints what failed
and what to do about it.
"""
import sys
import shutil
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

GREEN, RED, YELLOW, DIM, BOLD, OFF = (
    "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[1m", "\033[0m")
OK, BAD, WARN = f"{GREEN}ok  {OFF}", f"{RED}FAIL{OFF}", f"{YELLOW}warn{OFF}"

MIN_PYTHON = (3, 9)


class Check:
    def __init__(self):
        self.failed = 0

    def line(self, mark, name, detail="", fix=""):
        print(f"  {mark}  {name:<34} {DIM}{detail}{OFF}")
        if fix:
            print(f"        {DIM}→ {fix}{OFF}")

    def ok(self, name, detail=""):
        self.line(OK, name, detail)

    def warn(self, name, detail="", fix=""):
        self.line(WARN, name, detail, fix)

    def fail(self, name, detail="", fix=""):
        self.failed += 1
        self.line(BAD, name, detail, fix)


def run(script, *args):
    proc = subprocess.run([sys.executable, str(ROOT / script), *args],
                          capture_output=True, text=True, cwd=ROOT)
    tail = [ln for ln in proc.stdout.strip().splitlines() if ln.strip()]
    return proc.returncode, (tail[-1] if tail else ""), proc.stdout + proc.stderr


def strip(text):
    out, i = [], 0
    while i < len(text):
        if text[i] == "\033":
            while i < len(text) and text[i] != "m":
                i += 1
        else:
            out.append(text[i])
        i += 1
    return "".join(out)


def main(argv):
    quick = "--quick" in argv
    if "--help" in argv or "-h" in argv:
        print(__doc__)
        return 0

    c = Check()
    print(f"\n{BOLD}Engineering OS — installation check{OFF}")
    print(f"{DIM}{ROOT}{OFF}\n")

    # 1 · environment
    v = sys.version_info
    if v[:2] >= MIN_PYTHON:
        c.ok("python", f"{v.major}.{v.minor}.{v.micro}")
    else:
        c.fail("python", f"{v.major}.{v.minor}, need >= "
                         f"{MIN_PYTHON[0]}.{MIN_PYTHON[1]}",
               "install a newer Python and recreate the virtual environment")

    try:
        import yaml                                          # noqa: F401
        where = ("vendored — nothing to install"
                 if "vendor" in str(getattr(yaml, "__file__", ""))
                 else f"installed, {getattr(yaml, '__version__', '?')}")
        c.ok("YAML", where)
    except ImportError:
        c.fail("PyYAML", "not installed",
               "python -m pip install -r requirements.txt")
        print(f"\n{RED}Cannot continue without PyYAML.{OFF}")
        return 1

    if shutil.which("git"):
        c.ok("git", "found on PATH")
    else:
        c.warn("git", "not found",
               "needed only for Continuous Acquisition against a real history")

    try:
        import rdflib                                        # noqa: F401
        c.ok("rdflib (optional)", "installed")
    except ImportError:
        c.warn("rdflib (optional)", "not installed",
               "only needed to regenerate metamodel diagrams; skip it")

    # 2 · the model itself
    try:
        from compiler.registry import load_all
        registries = load_all()
        c.ok("registries", f"{len(registries)} declared, all load")
    except Exception as e:                                   # noqa: BLE001
        c.fail("registries", f"{type(e).__name__}: {e}",
               "a registry source is malformed; see docs/troubleshooting.md")

    try:
        from compiler import compile_project, emit_all, EMITTERS
        ckm, problems = compile_project(ROOT / "examples/tiny")
        if problems:
            c.fail("compiler", f"{len(problems)} diagnostic(s)",
                   f"first: {problems[0]}")
        else:
            s = ckm["statistics"]
            c.ok("compiler", f"examples/tiny → {s['nodes']} nodes, "
                             f"{s['edges']} edges")
            again, _ = compile_project(ROOT / "examples/tiny")
            if again == ckm:
                c.ok("deterministic generation", "two compilations are identical")
            else:
                c.fail("deterministic generation",
                       "the same sources produced different models",
                       "clear stale bytecode: find . -name __pycache__ -exec rm -rf {} +")
            _, written = emit_all(ROOT / "examples/tiny", ckm)
            missing = sorted(set(EMITTERS) - set(written))
            if missing:
                c.fail("emitters", f"missing {', '.join(missing)}")
            else:
                c.ok("emitters", f"{len(written)}: {', '.join(sorted(written))}")
    except Exception as e:                                   # noqa: BLE001
        c.fail("compiler", f"{type(e).__name__}: {e}")

    if quick:
        return report(c, quick=True)

    # 3 · the corpus and the suite
    #
    # Governance consistency and the fixtures are CONTRIBUTOR checks: they
    # verify this project's own decision corpus and regression suite. An
    # installed copy may not ship them, and their absence says nothing about
    # whether the installation works. Skipped, never failed.
    for label, script, fix in (
        ("governance consistency", "tools/check-governance.py",
         "a decision record is inconsistent; see docs/troubleshooting.md"),
        ("engineering questions", "tools/check-questions.py",
         "the question set is malformed"),
        ("Agent Skills standard", "tools/check-agentskills.py",
         "a SKILL.md does not meet agentskills.io/specification"),
        ("discovery skills", "tools/check-skills.py",
         "a skill contract is incomplete"),
        ("plans and recommendations", "tools/check-plans.py",
         "a plan phase can never act"),
    ):
        if not (ROOT / script).exists():
            c.warn(label, "not shipped in this installation",
                   "a contributor check; its absence is not a problem")
            continue
        code, last, _ = run(script)
        if code == 0:
            c.ok(label, strip(last)[:60])
        else:
            c.fail(label, strip(last)[:60], fix)

    if not (ROOT / "tests/projects").is_dir():
        c.warn("fixtures and query parity", "no fixtures in this installation",
               "a contributor check; the compiler was already exercised above")
        return report(c)
    code, last, out = run("tools/test.py")
    if code == 0:
        c.ok("fixtures and query parity", strip(last)[:60])
    else:
        c.fail("fixtures and query parity", "see output below",
               "python tools/test.py")
        print(strip(out)[-1200:])

    return report(c)


def report(c, quick=False):
    print()
    if c.failed:
        print(f"{RED}{c.failed} check(s) failed.{OFF} "
              f"{DIM}Engineering OS is not ready to use.{OFF}")
        print(f"{DIM}See docs/troubleshooting.md{OFF}\n")
        return 1
    scope = "quick check" if quick else "all checks"
    print(f"{GREEN}{BOLD}Engineering OS is installed and healthy{OFF} "
          f"{DIM}({scope} passed){OFF}")
    print(f"{DIM}Next: eos compile examples/tiny  "
          f"— or read the Quick Start in README.md{OFF}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
