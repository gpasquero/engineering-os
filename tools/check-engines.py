#!/usr/bin/env python3
"""Verify that the two query engines agree — on everything, not on identifiers.

`ADR-0086` accepts one query language with two implementations. `ADR-0088` §7
makes **semantic parity a public invariant**, and requires comparing:

    result nodes · result edges · full paths · ordering · diagnostics · status

Comparing only final identifiers would have missed the defect this check found on
its first full-fidelity run: JavaScript's `localeCompare` is locale-aware and does
not order like Python's codepoint comparison, so the two engines returned the
same set of rows **in a different order**.

Requires `node`. Skips loudly if absent, because a check that cannot run must say
so rather than pass.

Usage:  python3 tools/check-engines.py <project>...

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import shutil
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.query import Model, run, load_queries  # noqa: E402

HARNESS = """
const fs = require('fs');
const h = fs.readFileSync(process.argv[2], 'utf8');
const s = h.slice(h.indexOf('<script>') + 8, h.lastIndexOf('</script>'));
const stub = () => ({classList:{toggle(){},add(){},remove(){}}, dataset:{}, style:{},
  appendChild(){}, set textContent(v){this._t=v}, get textContent(){return this._t||''},
  set innerHTML(v){this._h=v}, get innerHTML(){return this._h||''}, scrollTop:0});
global.document = {getElementById: stub, createElement: stub, querySelectorAll: () => []};
eval(s + ';global.__r = runQuery; global.__q = QUERIES; global.__n = CKM.nodes;');
const out = {};
for (const [id, q] of Object.entries(global.__q)) {
  const subjects = q.subject === 'required' ? global.__n.map(n => n.id) : [null];
  for (const subj of subjects) out[id + '|' + (subj || '')] = global.__r(q, subj);
}
process.stdout.write(JSON.stringify(out));
"""

# Comparable projection of a result: everything that is semantically load-bearing.
def canonical(result):
    return {
        "status": result["status"],
        "rows": [{"id": r["id"], "type": r["type"], "hops": r.get("hops"),
                  "origin": r.get("origin"), "via": r.get("via"),
                  "path": [{k: h[k] for k in ("from", "predicate", "to", "direction", "matched")}
                           for h in r.get("path", [])],
                  "extra": {k: v for k, v in sorted(r.items())
                            if k not in ("id", "type", "label", "hops", "origin", "via", "path")}}
                 for r in result["rows"]],          # ORDER PRESERVED, not sorted
        "edges": [{k: e[k] for k in ("from", "predicate", "to") if k in e}
                  for e in result["edges"]],
        "diagnostics": [{"message": d["message"], "rule": d.get("rule")}
                        for d in result["diagnostics"]],
    }


def python_results(ckm, queries):
    model = Model(ckm)
    out = {}
    for qid, query in queries.items():
        subjects = ([n["id"] for n in ckm["nodes"]]
                    if query.get("subject") == "required" else [None])
        for subject in subjects:
            out[f"{qid}|{subject or ''}"] = canonical(run(model, query, subject))
    return out


def first_difference(a, b, path="result"):
    if type(a) is not type(b):
        return f"{path}: {type(a).__name__} vs {type(b).__name__}"
    if isinstance(a, dict):
        for key in sorted(set(a) | set(b)):
            if key not in a:
                return f"{path}.{key}: missing in python"
            if key not in b:
                return f"{path}.{key}: missing in js"
            d = first_difference(a[key], b[key], f"{path}.{key}")
            if d:
                return d
    elif isinstance(a, list):
        if len(a) != len(b):
            return f"{path}: {len(a)} vs {len(b)} items"
        for i, (x, y) in enumerate(zip(a, b)):
            d = first_difference(x, y, f"{path}[{i}]")
            if d:
                return d
    elif a != b:
        return f"{path}: {a!r} vs {b!r}"
    return None


def main(argv):
    if not shutil.which("node"):
        print("SKIPPED: node is not available, so engine parity is UNVERIFIED")
        return 0
    projects = argv[1:] or ["examples/vertical-slice", "examples/tiny"]
    queries = load_queries()
    harness = ROOT / ".engine-harness.js"
    harness.write_text(HARNESS)
    failures = 0
    try:
        for name in projects:
            project = ROOT / name
            ckm_path, page = (project / "build/canonical-knowledge-model.json",
                              project / "build/explorer.html")
            if not ckm_path.exists() or not page.exists():
                print(f"  SKIP  {name} — not compiled")
                continue
            js_raw = json.loads(subprocess.run(["node", str(harness), str(page)],
                                               capture_output=True, text=True,
                                               check=True).stdout)
            js = {k: canonical(v) for k, v in js_raw.items()}
            py = python_results(json.loads(ckm_path.read_text()), queries)

            keys = sorted(set(py) | set(js))
            bad = [(k, first_difference(py.get(k), js.get(k))) for k in keys
                   if py.get(k) != js.get(k)]
            if bad:
                failures += len(bad)
                print(f"  FAIL  {name} — {len(bad)} of {len(keys)} disagree")
                for k, why in bad[:5]:
                    print(f"        {k}\n          {why}")
            else:
                print(f"  OK    {name} — {len(keys)} pairs agree on "
                      f"status, rows, paths, ordering, edges and diagnostics")
    finally:
        harness.unlink(missing_ok=True)

    print()
    if failures:
        print(f"ENGINES DIVERGE on {failures} pair(s)")
        return 1
    print("both engines agree on every declared query")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
