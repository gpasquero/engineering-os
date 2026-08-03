"""Shared entry-point guards for every documented command.

Three failures found by writing the third-party documentation, all of the same
family: **a tool treating an argument as a project directory without ever
checking that it was one.**

    python tools/compile.py --help        created a directory called `--help`
    python tools/test.py --help           crashed with a traceback
    python tools/compile.py exmaples/tny  exited 0 and emitted an empty model

The third is the worst. A new user who mistypes a path is told the compilation
succeeded, is handed a model with nothing in it, and has no reason to suspect
the path.

Two guards, used by every command a user is told to run:

    help_requested(argv)   → True when the user asked for help
    project(argv[1])       → an existing project directory, or a clear refusal

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

RED, YELLOW, DIM, OFF = "\033[31m", "\033[33m", "\033[2m", "\033[0m"


def help_requested(argv):
    """`--help` and `-h` are never a project name."""
    return any(a in ("--help", "-h") for a in argv[1:])


def project(arg, *, must_have_model=True, hint=None):
    """Resolve a project directory, refusing rather than inventing one.

    Relative paths resolve against the repository root so the documented
    commands work from a clean clone; absolute paths are used as given, so a
    third-party project may live anywhere.
    """
    path = pathlib.Path(arg).expanduser()
    if not path.is_absolute():
        # Resolve against the USER's working directory first. When Engineering
        # OS is installed as a plugin its own root is a cache directory that is
        # replaced on every update — a project kept there would be destroyed.
        # The repository root is the fallback, so `examples/tiny` still works
        # from a clone.
        here = pathlib.Path.cwd() / path
        path = here if here.exists() else ROOT / path

    if not path.exists():
        _refuse(f"no such project directory: {arg}",
                "Check the path. Engineering OS will not create a project "
                "directory\n  for you — an empty model and a mistyped path "
                "are opposite findings.", hint)
    if not path.is_dir():
        _refuse(f"{arg} is a file, not a project directory", "", hint)
    if must_have_model and not (path / "model").is_dir():
        _refuse(f"{arg} has no `model/` directory",
                "A project keeps its authoring sources in `<project>/model/*.md`.\n"
                "  If you meant to start one:  mkdir -p "
                f"{arg}/model", hint)
    return path


def _refuse(what, why, hint):
    print(f"{RED}{what}{OFF}")
    if why:
        print(f"{DIM}  {why}{OFF}")
    if hint:
        print(f"{DIM}  {hint}{OFF}")
    sys.exit(2)


def new_project(arg):
    """A project directory being CREATED. Relative paths are the user's.

    Creation is the opposite case to `project()`: nothing exists yet, so there
    is nothing to look for. A relative path here always means "where I am",
    never "inside Engineering OS" — a plugin's own directory is a cache that is
    replaced on update.
    """
    path = pathlib.Path(arg).expanduser()
    if not path.is_absolute():
        path = pathlib.Path.cwd() / path
    return path
