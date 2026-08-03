#!/usr/bin/env python3
"""Validate every SKILL.md against the Agent Skills open standard.

    python tools/check-agentskills.py

The standard (https://agentskills.io/specification) is a *format*, not a
registry: a skill is a folder with a `SKILL.md` whose YAML frontmatter is the
manifest. Two fields are required and four are optional. Getting them wrong is
silent — the skill is simply never discovered — so it is checked here.

  name           required · 1-64 chars · [a-z0-9-] · no leading, trailing or
                 doubled hyphen · MUST match the parent directory name
  description    required · 1-1024 chars · what it does AND when to use it
  license        optional
  compatibility  optional · <= 500 chars
  metadata       optional · string -> string
  allowed-tools  optional · space-separated, experimental

The body should stay under 500 lines: agents load the whole file on activation.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.append(str(ROOT / "vendor"))

import yaml                                                  # noqa: E402

GREEN, RED, YELLOW, DIM, OFF = ("\033[32m", "\033[31m", "\033[33m",
                                "\033[2m", "\033[0m")
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
KNOWN = {"name", "description", "license", "compatibility", "metadata",
         "allowed-tools"}


def check(path, bad, warn):
    where = path.relative_to(ROOT)
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        bad.append(f"{where}: no YAML frontmatter")
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        bad.append(f"{where}: unparseable frontmatter — "
                   f"{str(e).splitlines()[-1].strip()}")
        return None

    name = fm.get("name")
    if not name:
        bad.append(f"{where}: `name` is required")
    else:
        if len(name) > 64:
            bad.append(f"{where}: `name` is {len(name)} chars, max 64")
        if not NAME.match(str(name)):
            bad.append(f"{where}: `name` must be lowercase a-z0-9 and single "
                       f"hyphens, got {name!r}")
        # The spec requires the name to match the parent directory. For a skill
        # at a repository root the parent is whatever the user cloned it into,
        # so that case is a warning rather than a failure.
        parent = path.parent.name
        if parent != name:
            (warn if path.parent == ROOT else bad).append(
                f"{where}: `name` is {name!r} but the directory is {parent!r}"
                + (" — install it under a directory of that name"
                   if path.parent == ROOT else ""))

    desc = fm.get("description")
    if not desc:
        bad.append(f"{where}: `description` is required")
    elif len(desc) > 1024:
        bad.append(f"{where}: `description` is {len(desc)} chars, max 1024")
    elif len(desc) < 40:
        warn.append(f"{where}: `description` is {len(desc)} chars — it should "
                    f"say what the skill does AND when to use it")

    if fm.get("compatibility") and len(fm["compatibility"]) > 500:
        bad.append(f"{where}: `compatibility` exceeds 500 chars")
    if fm.get("metadata") and not all(
            isinstance(v, str) for v in fm["metadata"].values()):
        bad.append(f"{where}: `metadata` values must be strings")
    for key in set(fm) - KNOWN:
        warn.append(f"{where}: `{key}` is not in the standard — clients may "
                    f"ignore it")

    lines = len(text.splitlines())
    if lines > 500:
        warn.append(f"{where}: {lines} lines — the whole file loads on "
                    f"activation; move detail into references/")
    return name, len(desc), lines


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return 0
    # `imports/` holds third-party skills kept for reference. They are not ours
    # to fix, and failing on someone else's frontmatter would make this check
    # unrunnable rather than useful.
    paths = sorted(p for p in (set(ROOT.glob("SKILL.md")) |
                               set(ROOT.glob("*/*/SKILL.md")))
                   if "imports" not in p.parts)
    if not paths:
        print("no SKILL.md found")
        return 1
    bad, warn, rows = [], [], []
    for p in paths:
        r = check(p, bad, warn)
        if r:
            rows.append((p.relative_to(ROOT), *r))

    for rel, name, dlen, lines in rows:
        print(f"  {GREEN}ok  {OFF}  {str(name):24} {DIM}{lines:>4} lines · "
              f"description {dlen} chars · {rel}{OFF}")
    for w in warn:
        print(f"  {YELLOW}warn{OFF}  {w}")
    for b in bad:
        print(f"  {RED}FAIL{OFF}  {b}")

    print()
    if bad:
        print(f"{RED}{len(bad)} skill(s) do not meet the Agent Skills "
              f"standard{OFF}")
        return 1
    print(f"{GREEN}{len(rows)} skill(s) meet the Agent Skills standard{OFF} "
          f"{DIM}(agentskills.io/specification){OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
