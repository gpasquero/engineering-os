# Installation

**Purpose.** Get a working Engineering OS checkout and prove it is healthy
before you trust anything it tells you.

Engineering OS is a set of Python programs run from a checkout. There is no
package on PyPI, no installer, no daemon and no service. You clone it, create a
virtual environment, install one dependency, and run a verifier.

---

## Requirements

| | |
|---|---|
| Operating system | macOS and Linux. Windows is untested; WSL should work. |
| Python | 3.9 or newer |
| Python dependencies | **PyYAML** only (`requirements.txt`) |
| Optional dependency | `rdflib` (`requirements-optional.txt`) |
| Git | needed only by `tools/longitudinal.py`, which materialises commits as detached worktrees |
| API keys | **none.** Engineering OS makes no network calls |

`rdflib` is used by exactly one program, `tools/generate-metamodel-views.py`,
which regenerates the metamodel's own diagrams from the OWL ontology. Nothing in
the normal workflow needs it. `tools/check.py` reports it as `optional` and does
not fail when it is absent.

---

## Install

```bash
git clone https://github.com/gpasquero/engineering-os.git
cd engineering-os
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python tools/check.py
```

Optional, only if you intend to edit the metamodel:

```bash
python -m pip install -r requirements-optional.txt
```

---

## Verify the installation

`tools/check.py` is the single verification command. Run it after installing and
after any change you make to the repository.

```bash
python tools/check.py            # everything
python tools/check.py --quick    # dependencies and compiler health only
python tools/check.py --help     # what it checks, in order
```

**What it checks**, in the order it prints them: Python version and required
dependencies; Git and the optional dependency; that all 20 declared registries
load; governance consistency across the decision corpus; that every test fixture
behaves as declared; that both query engines agree on every declared question;
that two compilations of the same sources are byte-identical; and that the
bundled example compiles and emits every product.

**Healthy output** ends with:

```text
Engineering OS is installed and healthy (all checks passed)
Next: python tools/compile.py examples/tiny  — or read the Quick Start in README.md
```

**Exit code 0 means the installation is usable.** Any other exit code is a real
failure, and the tool prints which check failed and what to do about it. A
failing check looks like this:

```text
  FAIL  governance consistency             15 governance finding(s)
        → a decision record is inconsistent; see docs/troubleshooting.md
```

---

## Verify the whole documented path

`tools/check.py` verifies the installation. `tools/smoke.py` verifies that a
person who did not build Engineering OS can actually complete the documented
journey — installation check, compiling the bundled example, every knowledge
product, one question, one guidance result, a brownfield briefing, deterministic
discovery, and that curation correctly refuses to run unattended.

```bash
python tools/smoke.py                      # the whole path, in a temp directory
python tools/smoke.py --repo /path/to/repo # use your repository for the onboarding steps
python tools/smoke.py --keep               # leave the temporary workspace behind
python tools/smoke.py --help
```

It works in a fresh temporary directory so that pre-existing generated state
cannot make a broken path look healthy. Exit code 0 means a third-party engineer
can complete the documented path.

---

## What gets written where

Engineering OS never writes to the system you analyse. It writes only inside its
own checkout and inside the project directory you name.

| Location | Contents |
|---|---|
| `<project>/model/*.md` | authoring sources — **yours**, hand-editable |
| `<project>/build/` | generated products — **always overwritten**, never edit |
| `<project>/*.json` | discovery, candidate, curation and drift artifacts |

`.gitignore` excludes Python bytecode and `/tmp-worktrees/`. Generated `build/`
directories for the bundled examples *are* committed, because compilation is
deterministic and a diff in them is a real regression.

---

## Failure modes

| Symptom | Cause and fix |
|---|---|
| `ModuleNotFoundError: No module named 'yaml'` | the virtual environment is not active, or `requirements.txt` was not installed |
| `check.py` reports a Python version failure | you are on an interpreter older than 3.9; `python3 --version` to confirm which one you are running |
| `deterministic generation` fails | stale Python bytecode. See [troubleshooting](troubleshooting.md) — on macOS the cache is outside the repository |
| `governance consistency` fails | a document in `governance/` references something that does not exist, or a Markdown link is broken. Run `python tools/check-governance.py` for the list |
| `fixtures and query parity` fails | run `python tools/test.py` for per-fixture detail |
