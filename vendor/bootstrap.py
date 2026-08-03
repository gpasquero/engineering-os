"""Make Engineering OS importable with nothing installed.

`vendor/` is **appended** to `sys.path`, never prepended: a PyYAML the user
already has always wins, and the vendored copy is only a fallback. That way
installing the dependency properly is never worse than not installing it.
"""
import sys
import pathlib

VENDOR = pathlib.Path(__file__).resolve().parent


def ensure():
    path = str(VENDOR)
    if path not in sys.path:
        sys.path.append(path)
