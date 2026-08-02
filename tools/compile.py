#!/usr/bin/env python3
"""The Knowledge Compiler.

    Authoring -> Discovery -> Parsing -> Resolution -> Canonical Knowledge Model -> Projection

**The Canonical Knowledge Model is the product** (ADR-0072). OWL, the explorer
and the graphs are projections of it, not deliverables in their own right.

Phases are first-class (ADR-0073). Every feature declares its input phase,
output phase, invariants and determinism guarantee. Run with `--phases` to print
the contract without reading the implementation.

Nothing is inferred: every edge in the output was asserted in the input
(ADR-0044, ADR-0061).

Usage:
    python3 tools/compile.py <project-dir>
    python3 tools/compile.py --phases

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import re
import sys
import json
import pathlib
import collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
METAMODEL = ROOT / "model/metamodel"


# ============================================================== phase model
class Phase:
    """A first-class compiler phase (ADR-0073)."""

    def __init__(self, key, title, consumes, produces, executed=True):
        self.key, self.title = key, title
        self.consumes, self.produces, self.executed = consumes, produces, executed


PHASES = [
    Phase("authoring", "Authoring", "human intent", "authoring sources", executed=False),
    Phase("discovery", "Discovery", "authoring sources", "a source set"),
    Phase("parsing", "Parsing", "a source set", "assertions"),
    Phase("resolution", "Resolution", "assertions", "a resolved assertion set"),
    Phase("ckm", "Canonical Knowledge Model", "resolved assertions", "the semantic model"),
    Phase("projection", "Projection", "the semantic model", "derived artifacts"),
]
PHASE_KEYS = {p.key for p in PHASES}

FEATURES = []


def feature(name, *, input_phase, output_phase, invariants, determinism):
    """Register a compiler feature with its mandatory four-field contract."""
    assert input_phase in PHASE_KEYS and output_phase in PHASE_KEYS, name
    assert invariants and determinism, f"{name}: a feature with no stated determinism has none"

    def wrap(fn):
        FEATURES.append({"name": name, "input": input_phase, "output": output_phase,
                         "invariants": invariants, "determinism": determinism, "fn": fn})
        return fn
    return wrap


def print_phases():
    print("Compiler phases (ADR-0073)\n")
    for p in PHASES:
        mark = "" if p.executed else "   [not executed by the compiler]"
        print(f"  {p.title}{mark}\n    consumes: {p.consumes}\n    produces: {p.produces}")
    print("\nFeatures\n")
    for f in FEATURES:
        print(f"  {f['name']}:  {f['input']} -> {f['output']}")
        for inv in f["invariants"]:
            print(f"    invariant:   {inv}")
        print(f"    determinism: {f['determinism']}")
    return 0


# =========================================================== the metamodel
def load_metamodel():
    """The compiler's rulebook, read from model/metamodel/ rather than hard-coded."""
    entities = {}
    for path in METAMODEL.glob("entities/*.md"):
        text = path.read_text()
        name = re.search(r"^title:\s*(\S+)", text, re.M)
        family = re.search(r"^entity-family:\s*(\S+)", text, re.M)
        if name:
            entities[name.group(1)] = family.group(1) if family else "unassigned"

    voc = (METAMODEL / "relationship-vocabulary.md").read_text()
    section = re.search(r"^## The mapping\n(.*?)(?=^## )", voc, re.M | re.S).group(1)
    predicates = {p: (core, cat) for p, core, cat
                  in re.findall(r"^\| `([^`]+)` \| `([^`]+)` \| (\w+) \|", section, re.M)}
    return entities, predicates


# ================================================================== phases
@feature("source discovery",
         input_phase="authoring", output_phase="discovery",
         invariants=["every *.md under model/ is a source",
                     "no source is read twice"],
         determinism="sources are sorted by path, so the source set is order-stable")
def discover(project):
    return sorted((project / "model").glob("*.md"))


@feature("front-matter parsing",
         input_phase="discovery", output_phase="parsing",
         invariants=["every source has front matter",
                     "a node declares an id and a type",
                     "parsing never consults another source"],
         determinism="parsing is a pure function of one file's bytes")
def parse(paths):
    nodes, errors = [], []
    for path in paths:
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", path.read_text(), re.S)
        if not m:
            errors.append(f"{path.name}: no front matter")
            continue
        fm, body = m.group(1), m.group(2).strip()

        def field(k):
            got = re.search(rf"^{k}:\s*(.+)$", fm, re.M)
            return got.group(1).strip() if got else None

        rels = []
        block = re.search(r"^relationships:\s*(.*?)(?=^\w|\Z)", fm, re.M | re.S)
        if block:
            rels = re.findall(r"^\s*-\s*([\w-]+):\s*(\S+)", block.group(1), re.M)
        nodes.append({"id": field("id"), "type": field("type"),
                      "label": field("label") or field("id"),
                      "position": field("position"),
                      "relationships": rels, "body": body, "source": path.name})
    return nodes, errors


@feature("metamodel type checking",
         input_phase="parsing", output_phase="resolution",
         invariants=["every node type is a declared metamodel entity",
                     "every predicate has a registered parent (ADR-0071)",
                     "every relationship target resolves to a node in this project",
                     "no edge is created that was not asserted (ADR-0044)"],
         determinism="errors are sorted, so a failing project fails identically every run")
def resolve(nodes, entities, predicates):
    errors, edges = [], []
    ids = {n["id"] for n in nodes if n["id"]}
    seen = collections.Counter(n["id"] for n in nodes if n["id"])

    for dup, count in sorted(seen.items()):
        if count > 1:
            errors.append(f"duplicate node id '{dup}' declared {count} times")

    for n in nodes:
        where = n["source"]
        if not n["id"] or not n["type"]:
            errors.append(f"{where}: missing id or type")
            continue
        if n["type"] not in entities:
            errors.append(f"{where}: '{n['type']}' is not a metamodel entity")
        for pred, target in n["relationships"]:
            if pred not in predicates:
                errors.append(f"{where}: predicate '{pred}' has no registered parent (ADR-0071)")
            if target not in ids:
                errors.append(f"{where}: '{pred}' points at unknown node '{target}'")
            elif pred in predicates:
                core, cat = predicates[pred]
                edges.append({"from": n["id"], "predicate": pred,
                              "to": target, "core": core, "category": cat})
    edges.sort(key=lambda e: (e["from"], e["predicate"], e["to"]))
    return edges, sorted(errors)


@feature("canonical knowledge model",
         input_phase="resolution", output_phase="ckm",
         invariants=["the model is the product; every other output derives from it (ADR-0072)",
                     "node and edge order is stable",
                     "no statistic is stored that cannot be recomputed from nodes and edges"],
         determinism="fully determined by the resolved assertion set")
def canonical_model(nodes, edges, entities):
    nodes = sorted(nodes, key=lambda n: n["id"])
    return {
        "metamodelVersion": "0.4.0-skeleton",
        "note": "Canonical Knowledge Model. Every edge was asserted; none inferred (ADR-0061).",
        "nodes": [{"id": n["id"], "type": n["type"], "label": n["label"],
                   "family": entities.get(n["type"], "unassigned"),
                   "position": n["position"], "description": n["body"]} for n in nodes],
        "edges": edges,
        "statistics": {
            "nodes": len(nodes), "edges": len(edges),
            "byType": dict(sorted(collections.Counter(n["type"] for n in nodes).items())),
            "byFamily": dict(sorted(collections.Counter(
                entities.get(n["type"], "unassigned") for n in nodes).items())),
            "byCategory": dict(sorted(collections.Counter(e["category"] for e in edges).items())),
            "byCoreType": dict(sorted(collections.Counter(e["core"] for e in edges).items())),
        },
    }


# ============================================================= projections
def _iri(i):
    return "ex:" + re.sub(r"[^A-Za-z0-9_]", "_", i)


def _camel(k):
    parts = k.split("-")
    return parts[0] + "".join(w.capitalize() for w in parts[1:])


@feature("OWL projection",
         input_phase="ckm", output_phase="projection",
         invariants=["every instance is typed by a metamodel class",
                     "every edge uses a metamodel object property",
                     "the result imports the metamodel ontology"],
         determinism="a pure function of the canonical model")
def to_owl(ckm):
    EOS = "https://example.org/engineering-os/metamodel#"
    NS = "https://example.org/engineering-os/example#"
    L = [f"@prefix ex:   <{NS}> .", f"@prefix eos:  <{EOS}> .",
         "@prefix owl:  <http://www.w3.org/2002/07/owl#> .",
         "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
         "@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .", "",
         "# A PROJECTION of the Canonical Knowledge Model (ADR-0072). Generated; do not edit.", "",
         f"<{NS.rstrip('#')}> a owl:Ontology ;",
         '    rdfs:comment "Layer B model expressed in the Layer A metamodel." ;',
         f"    owl:imports <{EOS.rstrip('#')}> .", ""]
    for n in ckm["nodes"]:
        L.append(f"{_iri(n['id'])} a eos:{n['type']} ;")
        L.append(f'    rdfs:label "{n["label"]}" ;')
        if n["position"]:
            L.append(f'    eos:hasPosition {n["position"]} ;')
        L.append(f'    rdfs:comment "{n["description"].splitlines()[0].replace(chr(34), chr(39))}" .')
        L.append("")
    for e in ckm["edges"]:
        L.append(f"{_iri(e['from'])} eos:{_camel(e['predicate'])} {_iri(e['to'])} .")
    return "\n".join(L) + "\n"


@feature("graph projection",
         input_phase="ckm", output_phase="projection",
         invariants=["one node per model node, one edge per model edge",
                     "families are visually distinguished"],
         determinism="a pure function of the canonical model")
def to_graph(ckm):
    def nid(i):
        return re.sub(r"[^A-Za-z0-9_]", "_", i)
    s = ckm["statistics"]
    L = ["# Generated graph\n", "> **A projection of the Canonical Knowledge Model.**",
         "> Generated by `tools/compile.py`. Do not edit.\n",
         f"\n**{s['nodes']} nodes, {s['edges']} edges.**\n", "\n```mermaid\ngraph LR"]
    for n in ckm["nodes"]:
        L.append(f'  {nid(n["id"])}["{n["label"]}<br/><i>{n["type"]}</i>"]')
    for e in ckm["edges"]:
        L.append(f"  {nid(e['from'])} -->|{e['predicate']}| {nid(e['to'])}")
    for fam in ("descriptive", "operational"):
        ids = [nid(n["id"]) for n in ckm["nodes"] if n["family"] == fam]
        if ids:
            L.append(f"  class {','.join(ids)} {fam};")
    L += ["  classDef descriptive fill:#e8f0fe,stroke:#4285f4;",
          "  classDef operational fill:#fce8e6,stroke:#ea4335;", "```\n"]
    return "\n".join(L)


@feature("knowledge explorer projection",
         input_phase="ckm", output_phase="projection",
         invariants=["self-contained: no external request (ADR-0017)",
                     "every node reachable; every edge traversable in both directions"],
         determinism="the model is embedded verbatim; the page adds no state")
def to_explorer(ckm):
    return _EXPLORER.replace("__DATA__", json.dumps(ckm).replace("</", "<\\/"))


_EXPLORER = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Knowledge Explorer</title>
<style>
:root{--bg:#fff;--fg:#1f1f1f;--mut:#5f6368;--line:#dadce0;--d:#4285f4;--o:#ea4335}
@media(prefers-color-scheme:dark){:root{--bg:#17181a;--fg:#e8eaed;--mut:#9aa0a6;--line:#3c4043}}
*{box-sizing:border-box}
body{margin:0;font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
background:var(--bg);color:var(--fg)}
header{padding:1.25rem 1.5rem;border-bottom:1px solid var(--line)}
h1{margin:0;font-size:1.1rem}
.sub{color:var(--mut);font-size:.85rem;margin-top:.25rem}
.wrap{display:grid;grid-template-columns:minmax(230px,300px) 1fr;min-height:calc(100vh - 90px)}
@media(max-width:720px){.wrap{grid-template-columns:1fr}}
nav{border-right:1px solid var(--line);padding:1rem;overflow-y:auto}
main{padding:1.5rem;overflow-x:auto}
.grp{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);margin:1rem 0 .35rem}
button.node{display:block;width:100%;text-align:left;background:none;border:0;color:inherit;
font:inherit;padding:.3rem .5rem;border-radius:6px;cursor:pointer;border-left:3px solid transparent}
button.node:hover{background:color-mix(in srgb,var(--fg) 8%,transparent)}
button.node.sel{background:color-mix(in srgb,var(--fg) 12%,transparent);font-weight:600}
button.node.descriptive{border-left-color:var(--d)}
button.node.operational{border-left-color:var(--o)}
.type{color:var(--mut);font-size:.78rem}
table{border-collapse:collapse;margin:.5rem 0 1.5rem;font-size:.9rem;min-width:100%}
th,td{border-bottom:1px solid var(--line);padding:.45rem .7rem;text-align:left;vertical-align:top}
th{color:var(--mut);font-weight:500;font-size:.78rem;text-transform:uppercase;letter-spacing:.05em}
code{background:color-mix(in srgb,var(--fg) 8%,transparent);padding:.1rem .35rem;
border-radius:4px;font-size:.85em}
a.link{color:inherit;text-decoration:underline;text-underline-offset:2px;cursor:pointer}
.pill{display:inline-block;font-size:.7rem;padding:.1rem .5rem;border-radius:999px;
border:1px solid var(--line);color:var(--mut)}
.empty{color:var(--mut);font-style:italic}
.tbl-wrap{overflow-x:auto}
</style></head><body>
<header><h1>Knowledge Explorer</h1>
<div class="sub">A projection of the Canonical Knowledge Model, which is the product.
Generated by <code>tools/compile.py</code>; nothing here was written by hand.</div></header>
<div class="wrap"><nav id="nav"></nav><main id="main"></main></div>
<script>
const CKM = __DATA__;
const byId = Object.fromEntries(CKM.nodes.map(n => [n.id, n]));
const nav = document.getElementById('nav'), main = document.getElementById('main');
const groups = {};
CKM.nodes.forEach(n => (groups[n.type] ||= []).push(n));
Object.keys(groups).sort().forEach(type => {
  const h = document.createElement('div'); h.className='grp'; h.textContent=type; nav.appendChild(h);
  groups[type].forEach(n => {
    const b=document.createElement('button');
    b.className='node '+n.family; b.textContent=n.label; b.dataset.id=n.id;
    b.onclick=()=>show(n.id); nav.appendChild(b);
  });
});
function esc(s){const d=document.createElement('div');d.textContent=s==null?'':s;return d.innerHTML}
function rows(list,dir){
  if(!list.length) return '<p class="empty">None.</p>';
  return '<div class="tbl-wrap"><table><tr><th>Predicate</th><th>Core type</th>'
   +'<th>Category</th><th>'+dir+'</th></tr>'
   +list.map(e=>{const other=dir==='Target'?e.to:e.from,o=byId[other];
     return `<tr><td><code>${esc(e.predicate)}</code></td><td><code>${esc(e.core)}</code></td>`
      +`<td><span class="pill">${esc(e.category)}</span></td>`
      +`<td><a class="link" onclick="show('${other}')">${esc(o?o.label:other)}</a> `
      +`<span class="type">${esc(o?o.type:'')}</span></td></tr>`}).join('')+'</table></div>';
}
function show(id){
  const n=byId[id]; if(!n) return;
  document.querySelectorAll('button.node').forEach(b=>b.classList.toggle('sel',b.dataset.id===id));
  main.innerHTML=`<h2>${esc(n.label)}</h2>
    <p><code>${esc(n.id)}</code> &middot; <span class="pill">${esc(n.type)}</span>
       <span class="pill">${esc(n.family)}</span></p>
    <p>${esc(n.description)}</p>
    <h3>Outgoing</h3>${rows(CKM.edges.filter(e=>e.from===id),'Target')}
    <h3>Incoming</h3>${rows(CKM.edges.filter(e=>e.to===id),'Source')}`;
}
function tbl(o){return '<div class="tbl-wrap"><table>'+Object.entries(o).map(([k,v])=>
  `<tr><td><code>${esc(k)}</code></td><td>${v}</td></tr>`).join('')+'</table></div>'}
main.innerHTML=`<h2>Canonical Knowledge Model</h2>
  <p>${CKM.statistics.nodes} nodes, ${CKM.statistics.edges} edges.
  Every edge was asserted in the sources; none was inferred.</p>
  <h3>Nodes by metamodel type</h3>${tbl(CKM.statistics.byType)}
  <h3>Nodes by family</h3>${tbl(CKM.statistics.byFamily)}
  <h3>Edges by relationship category</h3>${tbl(CKM.statistics.byCategory)}
  <h3>Edges by core relationship type</h3>${tbl(CKM.statistics.byCoreType)}
  <p class="empty">Select a node to explore.</p>`;
</script></body></html>
"""


# ==================================================================== main
def compile_project(project, quiet=False):
    """Returns (ckm, errors). Errors are non-empty iff compilation failed."""
    def log(m):
        if not quiet:
            print(m)

    entities, predicates = load_metamodel()
    log(f"[metamodel]  {len(entities)} entity types, {len(predicates)} registered predicates")

    paths = discover(project)
    log(f"[discovery]  {len(paths)} authoring sources")

    nodes, parse_errors = parse(paths)
    log(f"[parsing]    {len(nodes)} nodes")

    edges, resolve_errors = resolve(nodes, entities, predicates)
    errors = sorted(parse_errors + resolve_errors)
    if errors:
        log(f"[resolution] FAILED — {len(errors)} error(s):")
        for e in errors:
            log(f"    {e}")
        return None, errors
    log(f"[resolution] OK — {len(edges)} edges, all types and predicates valid")

    ckm = canonical_model(nodes, edges, entities)
    log(f"[ckm]        {ckm['statistics']['nodes']} nodes, {ckm['statistics']['edges']} edges")
    return ckm, []


def emit(project, ckm):
    out = project / "build"
    out.mkdir(parents=True, exist_ok=True)
    (out / "canonical-knowledge-model.json").write_text(json.dumps(ckm, indent=2) + "\n")
    (out / "model.ttl").write_text(to_owl(ckm))
    (out / "graph.md").write_text(to_graph(ckm))
    (out / "explorer.html").write_text(to_explorer(ckm))
    return out


def main(argv):
    if len(argv) == 2 and argv[1] == "--phases":
        return print_phases()
    if len(argv) != 2:
        print(__doc__)
        return 2
    project = ROOT / argv[1]
    ckm, errors = compile_project(project)
    if errors:
        return 1
    emit(project, ckm)
    print("[projection] canonical-knowledge-model.json, model.ttl, graph.md, explorer.html")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
