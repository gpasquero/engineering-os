#!/usr/bin/env python3
"""The Knowledge Compiler — first end-to-end pipeline.

    authoring sources -> Canonical Knowledge Model -> projections

Crude by intent. The objective is to validate the complete pipeline as early as
possible, not to be the implementation (ADR-0017: reference architecture, not
reference implementation).

Phases:
    1. discover   find authoring sources
    2. parse      front matter and body
    3. resolve    check every assertion against the METAMODEL
    4. emit       Canonical Knowledge Model, OWL, graph, HTML explorer

What makes this a compiler rather than a converter is phase 3. It reads
model/metamodel/ to learn which entity types exist and which predicates are
registered, then rejects a model that violates them. Nothing is inferred:
every edge in the output was asserted in the input (ADR-0061).

Usage:  python3 tools/compile.py examples/tiny

Semantic Layer: None — cross-cutting infrastructure (ADR-0039).
"""
import re
import sys
import json
import html
import pathlib
import collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
METAMODEL = ROOT / "model/metamodel"


# ---------------------------------------------------------------- metamodel
def load_metamodel():
    """The compiler's rulebook, read from the metamodel itself."""
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


# ------------------------------------------------------------------- phases
def discover(source):
    return sorted((source / "model").glob("*.md"))


def parse(paths):
    nodes = []
    for path in paths:
        text = path.read_text()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            raise SystemExit(f"parse: {path.name} has no front matter")
        fm, body = m.group(1), m.group(2).strip()

        def field(k):
            got = re.search(rf"^{k}:\s*(.+)$", fm, re.M)
            return got.group(1).strip() if got else None

        rels = []
        block = re.search(r"^relationships:\s*(.*?)(?=^\w|\Z)", fm, re.M | re.S)
        if block:
            for pred, target in re.findall(r"^\s*-\s*([\w-]+):\s*(\S+)", block.group(1), re.M):
                rels.append((pred, target))
        nodes.append({
            "id": field("id"), "type": field("type"),
            "label": field("label") or field("id"),
            "position": field("position"),
            "relationships": rels, "body": body, "source": path.name,
        })
    return nodes


def resolve(nodes, entities, predicates):
    """Validate every assertion against the metamodel. Returns (edges, errors)."""
    errors, edges = [], []
    ids = {n["id"] for n in nodes}

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
            else:
                core, cat = predicates.get(pred, ("?", "?"))
                edges.append({"from": n["id"], "predicate": pred,
                              "to": target, "core": core, "category": cat})
    return edges, errors


# -------------------------------------------------------------- projections
def canonical_model(nodes, edges, entities):
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
            "byCategory": dict(sorted(collections.Counter(e["category"] for e in edges).items())),
        },
    }


def to_owl(ckm):
    EOS = "https://example.org/engineering-os/metamodel#"
    NS = "https://example.org/engineering-os/example/tiny#"

    def camel(k):
        parts = k.split("-")
        return parts[0] + "".join(w.capitalize() for w in parts[1:])

    def iri(i):
        return "ex:" + re.sub(r"[^A-Za-z0-9_]", "_", i)

    L = [f"@prefix ex:   <{NS}> .", f"@prefix eos:  <{EOS}> .",
         "@prefix owl:  <http://www.w3.org/2002/07/owl#> .",
         "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
         "@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .", "",
         "# Generated by tools/compile.py. A derived artifact (ADR-0012).", "",
         f"<{NS.rstrip('#')}> a owl:Ontology ;",
         f'    rdfs:comment "Layer B model expressed in the Layer A metamodel." ;',
         f"    owl:imports <{EOS.rstrip('#')}> .", ""]
    for n in ckm["nodes"]:
        L.append(f"{iri(n['id'])} a eos:{n['type']} ;")
        L.append(f'    rdfs:label "{n["label"]}" ;')
        if n["position"]:
            L.append(f'    eos:hasPosition {n["position"]} ;')
        first = n["description"].split("\n")[0].replace('"', "'")
        L.append(f'    rdfs:comment "{first}" .')
        L.append("")
    for e in ckm["edges"]:
        L.append(f"{iri(e['from'])} eos:{camel(e['predicate'])} {iri(e['to'])} .")
    return "\n".join(L) + "\n"


def to_graph(ckm):
    L = ["# Generated graph — tiny example\n",
         "> **Generated by `tools/compile.py`. Do not edit.**\n",
         f"\n**{ckm['statistics']['nodes']} nodes, {ckm['statistics']['edges']} edges.**\n",
         "\n```mermaid\ngraph LR"]
    for n in ckm["nodes"]:
        nid = re.sub(r"[^A-Za-z0-9_]", "_", n["id"])
        L.append(f'  {nid}["{n["label"]}<br/><i>{n["type"]}</i>"]')
    for e in ckm["edges"]:
        a = re.sub(r"[^A-Za-z0-9_]", "_", e["from"])
        b = re.sub(r"[^A-Za-z0-9_]", "_", e["to"])
        L.append(f"  {a} -->|{e['predicate']}| {b}")
    desc = [n for n in ckm["nodes"] if n["family"] == "descriptive"]
    oper = [n for n in ckm["nodes"] if n["family"] == "operational"]
    for cls, group in (("descriptive", desc), ("operational", oper)):
        if group:
            ids = ",".join(re.sub(r"[^A-Za-z0-9_]", "_", n["id"]) for n in group)
            L.append(f"  class {ids} {cls};")
    L.append("  classDef descriptive fill:#e8f0fe,stroke:#4285f4;")
    L.append("  classDef operational fill:#fce8e6,stroke:#ea4335;")
    L.append("```\n")
    return "\n".join(L)


def to_explorer(ckm):
    data = json.dumps(ckm).replace("</", "<\\/")
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Knowledge Explorer — tiny example</title>
<style>
:root{--bg:#fff;--fg:#1f1f1f;--mut:#5f6368;--line:#dadce0;--d:#4285f4;--o:#ea4335}
@media(prefers-color-scheme:dark){:root{--bg:#17181a;--fg:#e8eaed;--mut:#9aa0a6;--line:#3c4043}}
*{box-sizing:border-box}
body{margin:0;font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
background:var(--bg);color:var(--fg)}
header{padding:1.25rem 1.5rem;border-bottom:1px solid var(--line)}
h1{margin:0;font-size:1.1rem}
.sub{color:var(--mut);font-size:.85rem;margin-top:.25rem}
.wrap{display:grid;grid-template-columns:minmax(240px,320px) 1fr;min-height:calc(100vh - 90px)}
@media(max-width:720px){.wrap{grid-template-columns:1fr}}
nav{border-right:1px solid var(--line);padding:1rem;overflow-y:auto}
main{padding:1.5rem;overflow-x:auto}
.grp{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);
margin:1rem 0 .35rem}
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
<div class="sub">Generated by <code>tools/compile.py</code> from the Canonical Knowledge Model.
Nothing here was written by hand.</div></header>
<div class="wrap"><nav id="nav"></nav><main id="main"></main></div>
<script>
const CKM = __DATA__;
const byId = Object.fromEntries(CKM.nodes.map(n => [n.id, n]));
const nav = document.getElementById('nav'), main = document.getElementById('main');
const groups = {};
CKM.nodes.forEach(n => (groups[n.type] ||= []).push(n));
Object.keys(groups).sort().forEach(type => {
  const h = document.createElement('div'); h.className = 'grp'; h.textContent = type;
  nav.appendChild(h);
  groups[type].forEach(n => {
    const b = document.createElement('button');
    b.className = 'node ' + n.family; b.textContent = n.label; b.dataset.id = n.id;
    b.onclick = () => show(n.id); nav.appendChild(b);
  });
});
function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
function rows(list, dir){
  if(!list.length) return '<p class="empty">None.</p>';
  return '<div class="tbl-wrap"><table><tr><th>Predicate</th><th>Core type</th>'
    + '<th>Category</th><th>' + dir + '</th></tr>'
    + list.map(e => {
        const other = dir === 'Target' ? e.to : e.from;
        const o = byId[other];
        return `<tr><td><code>${esc(e.predicate)}</code></td><td><code>${esc(e.core)}</code></td>`
          + `<td><span class="pill">${esc(e.category)}</span></td>`
          + `<td><a class="link" onclick="show('${other}')">${esc(o ? o.label : other)}</a>`
          + ` <span class="type">${esc(o ? o.type : '')}</span></td></tr>`;
      }).join('') + '</table></div>';
}
function show(id){
  const n = byId[id]; if(!n) return;
  document.querySelectorAll('button.node').forEach(b =>
    b.classList.toggle('sel', b.dataset.id === id));
  main.innerHTML = `<h2>${esc(n.label)}</h2>
    <p><code>${esc(n.id)}</code> &middot; <span class="pill">${esc(n.type)}</span>
       <span class="pill">${esc(n.family)}</span></p>
    <p>${esc(n.description)}</p>
    <h3>Outgoing</h3>${rows(CKM.edges.filter(e => e.from === id), 'Target')}
    <h3>Incoming</h3>${rows(CKM.edges.filter(e => e.to === id), 'Source')}`;
}
main.innerHTML = `<h2>Tiny example</h2>
  <p>${CKM.statistics.nodes} nodes, ${CKM.statistics.edges} edges.
  Every edge was asserted in the sources; none was inferred.</p>
  <h3>Nodes by metamodel type</h3><div class="tbl-wrap"><table>
  ${Object.entries(CKM.statistics.byType).map(([k,v]) =>
     `<tr><td><code>${k}</code></td><td>${v}</td></tr>`).join('')}</table></div>
  <h3>Edges by relationship category</h3><div class="tbl-wrap"><table>
  ${Object.entries(CKM.statistics.byCategory).map(([k,v]) =>
     `<tr><td><span class="pill">${k}</span></td><td>${v}</td></tr>`).join('')}</table></div>
  <p class="empty">Select a node to explore.</p>`;
</script></body></html>
""".replace("__DATA__", data)


# --------------------------------------------------------------------- main
def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    source = ROOT / argv[1]
    out = source / "build"
    out.mkdir(parents=True, exist_ok=True)

    entities, predicates = load_metamodel()
    print(f"[metamodel] {len(entities)} entity types, {len(predicates)} registered predicates")

    paths = discover(source)
    print(f"[discover]  {len(paths)} authoring sources")

    nodes = parse(paths)
    print(f"[parse]     {len(nodes)} nodes")

    edges, errors = resolve(nodes, entities, predicates)
    if errors:
        print(f"[resolve]   FAILED — {len(errors)} error(s):")
        for e in errors:
            print("   ", e)
        return 1
    print(f"[resolve]   OK — {len(edges)} edges, all types and predicates valid")

    ckm = canonical_model(nodes, edges, entities)
    (out / "canonical-knowledge-model.json").write_text(json.dumps(ckm, indent=2) + "\n")
    (out / "model.ttl").write_text(to_owl(ckm))
    (out / "graph.md").write_text(to_graph(ckm))
    (out / "explorer.html").write_text(to_explorer(ckm))
    print("[emit]      canonical-knowledge-model.json, model.ttl, graph.md, explorer.html")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
