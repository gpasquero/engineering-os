#!/usr/bin/env python3
"""Verify the governance corpus (SESSION-0044).

This check existed for many sessions **as a script retyped from memory each
time**, which is why it never caught anything permanently. It is committed now
for the same reason every other rule was moved out of code and into data: a check
nobody can run twice is not a check.

Seven properties:

  * **parseable front matter** — a record whose YAML does not parse carries no
    `id`, no `status` and no `supersedes`, and every check below silently skips
    it. This is the only check whose failure hides the others;
  * **id matches filename** — the register is navigable by name;
  * **contiguous sequence, with documented gaps** — a missing ID is either an
    error or a decision. If it is a decision, the index says so, and **a
    reference to a documented gap is not dangling: it is the documentation**;
  * **no dangling references** — every `ADR-nnnn` cited resolves;
  * **supersession symmetry** — `supersedes` and `superseded-by` agree
    (`ADR-0021`);
  * **no broken relative links**;
  * **index row counts match file counts** — an index that omits a record is a
    register that lies.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import re
import sys
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

REGISTERS = (("governance/adr", "ADR"), ("governance/issues", "ISSUE"),
             ("governance/sessions", "SESSION"), ("governance/acceptance", "ACCEPT"))
INDEXED = ("governance/adr", "governance/acceptance", "governance/sessions")


def main():
    bad, docs = [], {}

    def front_matter(path):
        m = re.match(r"^---\n(.*?)\n---\n", path.read_text(), re.S)
        if not m:
            bad.append(f"{path}: no front matter")
            return {}
        try:
            return yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            line = str(e).splitlines()[-1].strip()
            bad.append(f"{path}: unparseable front matter — {line}")
            return {}

    for folder, prefix in REGISTERS:
        d = ROOT / folder
        ids = []
        for p in sorted(d.glob(f"{prefix}-*.md")):
            f = front_matter(p)
            if f.get("id") and not p.name.startswith(f["id"]):
                bad.append(f"{p}: front matter says {f['id']}")
            docs[f.get("id") or p.name] = (p, f)
            ids.append(int(re.match(rf"{prefix}-(\d+)", p.name).group(1)))
        index = (d / "README.md").read_text()
        for n in sorted(set(range(min(ids), max(ids) + 1)) - set(ids)):
            if f"{prefix}-{n:04d}" not in index:
                bad.append(f"{prefix}-{n:04d} is missing and the index does not say why")

    known = set(docs)
    for folder, _ in REGISTERS:
        known |= set(re.findall(r"(?:ADR|ISSUE|SESSION|ACCEPT)-\d{4}",
                                (ROOT / folder / "README.md").read_text()))

    for did, (p, f) in docs.items():
        for ref in sorted(set(re.findall(r"\b(?:ADR|ISSUE|SESSION|ACCEPT)-\d{4}\b",
                                         p.read_text()))):
            if ref not in known:
                bad.append(f"{did}: dangling reference {ref}")
        sup = f.get("supersedes")
        for s in (sup if isinstance(sup, list) else [sup] if sup else []):
            if s in docs and docs[s][1].get("superseded-by") != did:
                bad.append(f"{did} supersedes {s}; {s} does not say so")

    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        for link in re.findall(r"\]\(([^)#][^)]*?)\)", p.read_text()):
            if link.startswith(("http", "mailto:")):
                continue
            if not (p.parent / link.split("#")[0]).exists():
                bad.append(f"{p.relative_to(ROOT)}: broken link -> {link}")

    for folder in INDEXED:
        prefix = dict(REGISTERS)[folder]
        d = ROOT / folder
        rows = len(re.findall(rf"^\| \[{prefix}-\d{{4}}\]",
                              (d / "README.md").read_text(), re.M))
        files = len(list(d.glob(f"{prefix}-*.md")))
        if rows != files:
            bad.append(f"{folder}: {rows} index rows for {files} records")

    for b in bad:
        print(f"  {RED}{b}{OFF}")
    print()
    if bad:
        print(f"{RED}{len(bad)} governance finding(s){OFF}")
        return 1
    print(f"{GREEN}the governance corpus is internally consistent{OFF} "
          f"{DIM}({len(docs)} records){OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
