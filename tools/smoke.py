#!/usr/bin/env python3
"""Third-party smoke test — can someone who did not build this actually use it?

    python tools/smoke.py
    python tools/smoke.py --repo /path/to/a/brownfield/repo
    python tools/smoke.py --keep      leave the temporary workspace for inspection

Runs the documented MVP journey end to end, in a **fresh temporary directory**
with no pre-existing generated state, using only commands that appear in
`README.md`.

    1  install verified          tools/check.py
    2  compile the example       tools/compile.py examples/tiny
    3  knowledge products        CKM · OWL · SHACL · graph · indexes · Explorer
    4  ask an Engineering Question
    5  request Engineering Guidance
    6  begin Brownfield onboarding      (worker briefing for Claude or Codex)
    7  deterministic Interpretive Discovery → Candidate Engineering Model

**Human Curation is not automated and never will be** — a scripted curation
session would generate exactly the reviewer-efficiency numbers Engineering OS
refuses to invent. Step 8 verifies only that the tool launches and correctly
*refuses* to run without a terminal.

Exit code 0 means a third-party engineer can complete the documented path.
"""
import sys
import shutil
import pathlib
import tempfile
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
GREEN, RED, DIM, BOLD, OFF = ("\033[32m", "\033[31m", "\033[2m", "\033[1m",
                              "\033[0m")


def step(n, name):
    print(f"\n{BOLD}{n}{OFF}  {name}")


def run(*args, expect=0, cwd=None):
    cmd = [sys.executable, *[str(a) for a in args]]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd or ROOT)
    shown = " ".join(["python", *[str(a) for a in args]])
    if proc.returncode != expect:
        print(f"   {RED}FAIL{OFF}  {shown}")
        print(f"   {DIM}exit {proc.returncode}, expected {expect}{OFF}")
        print((proc.stdout + proc.stderr)[-800:])
        return None
    print(f"   {GREEN}ok{OFF}    {DIM}{shown}{OFF}")
    return proc.stdout


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__)
        return 0
    keep = "--keep" in argv
    repo = None
    for i, a in enumerate(argv):
        if a == "--repo" and i + 1 < len(argv):
            repo = pathlib.Path(argv[i + 1]).resolve()

    work = pathlib.Path(tempfile.mkdtemp(prefix="eos-smoke-"))
    print(f"\n{BOLD}Engineering OS — third-party smoke test{OFF}")
    print(f"{DIM}workspace {work}{OFF}")
    failures = 0

    step(1, "installation verified")
    if run("tools/check.py") is None:
        failures += 1

    step(2, "compile the bundled example")
    if run("tools/compile.py", "examples/tiny") is None:
        failures += 1

    step(3, "knowledge products generated")
    build = ROOT / "examples/tiny/build"
    expected = ["canonical-knowledge-model.json", "model.ttl", "shapes.ttl",
                "graph.md", "indexes.json", "explorer.html"]
    missing = [f for f in expected if not (build / f).exists()]
    if missing:
        print(f"   {RED}FAIL{OFF}  missing {', '.join(missing)}")
        failures += 1
    else:
        print(f"   {GREEN}ok{OFF}    {DIM}{', '.join(expected)}{OFF}")
        print(f"   {DIM}      Explorer: {build / 'explorer.html'}{OFF}")

    step(4, "ask an Engineering Question")
    out = run("tools/ask.py", "examples/tiny", "Q-impact", "Concept.Order")
    if out is None or "Invariant.PaymentBeforeShipping" not in out:
        print(f"   {RED}FAIL{OFF}  expected the invariant in the answer")
        failures += 1

    step(5, "request Engineering Guidance")
    out = run("tools/advise.py", "examples/tiny", "R-change-concept",
              "Concept.Order")
    if out is None:
        failures += 1
    if run("tools/direct.py", "examples/tiny", "intents") is None:
        failures += 1

    step(6, "begin Brownfield onboarding")
    target = repo or (ROOT / "examples/brownfield-demo")
    project = work / "onboarding"
    out = run("tools/onboard.py", "brief", target, project)
    if out is None or not (project / "onboarding-brief.md").exists():
        print(f"   {RED}FAIL{OFF}  no worker briefing produced")
        failures += 1
    elif not (project / "mechanical-engineering-model.json").exists():
        print(f"   {RED}FAIL{OFF}  no mechanical model produced")
        failures += 1

    step(7, "deterministic Interpretive Discovery")
    if run("discovery/run.py", target, project) is None:
        failures += 1
    elif not (project / "candidate-initial.json").exists():
        print(f"   {RED}FAIL{OFF}  no Candidate Engineering Model produced")
        failures += 1

    step(8, "Human Curation refuses to run unattended")
    proc = subprocess.run([sys.executable, str(ROOT / "tools/curate.py"),
                           str(project)], capture_output=True, text=True,
                          cwd=ROOT, stdin=subprocess.DEVNULL)
    if proc.returncode == 0 or "requires a human" not in proc.stdout:
        print(f"   {RED}FAIL{OFF}  curation did not refuse a non-interactive run")
        failures += 1
    else:
        print(f"   {GREEN}ok{OFF}    {DIM}refused, as designed{OFF}")

    if keep:
        print(f"\n{DIM}workspace kept at {work}{OFF}")
    else:
        shutil.rmtree(work, ignore_errors=True)

    print()
    if failures:
        print(f"{RED}{failures} step(s) failed.{OFF} "
              f"{DIM}The documented MVP path is broken.{OFF}\n")
        return 1
    print(f"{GREEN}{BOLD}The documented MVP path completes.{OFF} "
          f"{DIM}Human Curation still requires a human.{OFF}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
