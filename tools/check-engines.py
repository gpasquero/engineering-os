#!/usr/bin/env python3
"""Verify that the two query engines agree.

`ADR-0086` accepts one query language with two implementations — Python for the
CLI and agents, JavaScript for the Explorer — and records the cost: **two engines
can diverge and nothing detects it.**

This is the detector. It runs every declared query through both engines against
the same Canonical Knowledge Model, for every node, and compares the results.

Requires `node`. Skips with a warning if absent, because a check that cannot run
must say so rather than pass.

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
  if (q.subject === 'required') {
    for (const n of global.__n)
      out[id + '|' + n.id] = global.__r(q, n.id).map(r => r.id || (r.from + '>' + r.to)).sort();
  } else {
    out[id + '|'] = global.__r(q, null).map(r => r.id || (r.from + '>' + r.to)).sort();
  }
}
process.stdout.write(JSON.stringify(out));
"""


def python_results(ckm, queries):
    model = Model(ckm)
    out = {}
    for qid, query in queries.items():
        subjects = [n["id"] for n in ckm["nodes"]] if query.get("subject") == "required" else [None]
        for subject in subjects:
            rows = run(model, query, subject)
            out[f"{qid}|{subject or ''}"] = sorted(
                r.get("id") or f"{r['from']}>{r['to']}" for r in rows)
    return out


def main(argv):
    if not shutil.which("node"):
        print("SKIPPED: node is not available, so engine equivalence is UNVERIFIED")
        return 0
    projects = argv[1:] or ["examples/vertical-slice", "examples/tiny"]
    queries = load_queries()
    harness = ROOT / "build-harness.js"
    harness.write_text(HARNESS)
    failures = 0
    try:
        for name in projects:
            project = ROOT / name
            ckm_path = project / "build/canonical-knowledge-model.json"
            page = project / "build/explorer.html"
            if not ckm_path.exists() or not page.exists():
                print(f"  SKIP  {name} — not compiled")
                continue
            ckm = json.loads(ckm_path.read_text())
            js = json.loads(subprocess.run(
                ["node", str(harness), str(page)],
                capture_output=True, text=True, check=True).stdout)
            py = python_results(ckm, queries)

            keys = sorted(set(py) | set(js))
            bad = [k for k in keys if py.get(k) != js.get(k)]
            checked = len(keys)
            if bad:
                failures += len(bad)
                print(f"  FAIL  {name} — {len(bad)} of {checked} disagree")
                for k in bad[:5]:
                    print(f"        {k}\n          py: {py.get(k)}\n          js: {js.get(k)}")
            else:
                print(f"  OK    {name} — {checked} query/subject pairs agree")
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
