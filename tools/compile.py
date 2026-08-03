#!/usr/bin/env python3
"""Orchestration only. The compiler lives in `compiler/` (ADR-0073).

Usage:
    python3 tools/compile.py <project-dir>
    python3 tools/compile.py --phases

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from _cli import help_requested, project as project_arg  # noqa: E402

from compiler import compile_project, emit_all           # noqa: E402
from compiler.runtime.phases import describe             # noqa: E402


def main(argv):
    if len(argv) == 2 and argv[1] == "--phases":
        print(describe())
        return 0
    if help_requested(argv) or len(argv) != 2:
        print(__doc__)
        return 0 if help_requested(argv) else 2

    project = project_arg(argv[1])
    ckm, problems = compile_project(project, log=print)
    if problems:
        print(f"[FAILED]     {len(problems)} diagnostic(s):")
        for d in problems:
            print(f"    ({d.phase}) {d}")
        return 1

    out, written = emit_all(project, ckm)
    print(f"[projection] {', '.join(sorted(written))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
