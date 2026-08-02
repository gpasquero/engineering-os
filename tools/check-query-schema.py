#!/usr/bin/env python3
"""Verify that invalid query declarations are rejected (ADR-0088 §4).

A schema that accepts a malformed declaration is worse than no schema: the query
still runs and returns something plausible. Each case in
`tests/query-schema/invalid-declarations.md` must produce its expected message.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import re
import sys
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.query import validate_query  # noqa: E402
from compiler.registry import load_all     # noqa: E402

CASES = ROOT / "tests/query-schema/invalid-declarations.md"
GREEN, RED, OFF = "\033[32m", "\033[31m", "\033[0m"


def main():
    registries = load_all()
    vocab = {"node-types": set(registries["REG-entity-types"]),
             "predicates": set(registries["REG-relationship-predicates"]),
             "core-types": set(registries["REG-core-relationship-types"])
                           | {e["core"] for e in
                              registries["REG-relationship-predicates"].values()}}
    cases = yaml.safe_load(re.search(r"```yaml\n(.*?)```", CASES.read_text(),
                                     re.S).group(1))["cases"]
    width = max(len(c["name"]) for c in cases)
    failures = 0
    print(f"Query declaration schema — {len(cases)} invalid declarations\n")
    for case in cases:
        messages = validate_query(case["query"], vocab)
        hit = any(case["expect"] in m for m in messages)
        print(f"  {GREEN + 'REJECTED' + OFF if hit else RED + 'ACCEPTED' + OFF}  "
              f"{case['name']:<{width}}  {case['expect']}")
        if not hit:
            failures += 1
            print(f"          {RED}got: {messages or 'no diagnostics at all'}{OFF}")
    print()
    if failures:
        print(f"{RED}{failures} malformed declaration(s) were not rejected{OFF}")
        return 1
    print(f"{GREEN}every malformed declaration was rejected{OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
