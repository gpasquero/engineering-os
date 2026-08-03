"""The Engineering OS Knowledge Compiler.

    Authoring -> Discovery -> Parsing -> Resolution -> Canonical Knowledge Model -> Projection

**The Canonical Knowledge Model is the product** (ADR-0072, ADR-0076). Every
emitter produces a projection of it.

Module layout mirrors the phases (ADR-0073). `tools/compile.py` is orchestration
only and holds no compiler logic.
"""
# Zero-install: fall back to the vendored pure-Python PyYAML when none is
# installed. Appended to sys.path, so a real installation always wins.
import sys as _sys, pathlib as _pathlib
_sys.path.append(str(_pathlib.Path(__file__).resolve().parent.parent / "vendor"))
from .runtime import phases, diagnostics
from .registry import load_all as load_registries
from .discovery import discover
from .parser import parse
from .resolver import resolve, load_metamodel
from .validator import validate, load_rules
from .ckm import build
from .emitters import json as json_emitter, owl, mermaid, explorer, shacl, indexes

EMITTERS = {
    "canonical-knowledge-model.json": json_emitter.emit,
    "model.ttl": owl.emit,
    "graph.md": mermaid.emit,
    "explorer.html": explorer.emit,
    "shapes.ttl": shacl.emit,
    "indexes.json": indexes.emit,
}


def compile_project(project, log=lambda m: None):
    """Returns (ckm, diagnostics). Diagnostics are non-empty iff compilation failed."""
    registries = load_registries()
    log(f"[registries] {len(registries)} registries: "
        + ", ".join(f"{k.replace('REG-', '')} {len(v)}" for k, v in sorted(registries.items())))

    entities, predicates, core_types = load_metamodel()

    paths = discover(project)
    log(f"[discovery]  {len(paths)} authoring sources")

    nodes, parse_diagnostics = parse(paths)
    log(f"[parsing]    {len(nodes)} nodes, {len(parse_diagnostics)} structural diagnostic(s)")
    if parse_diagnostics:
        return None, diagnostics.sort(parse_diagnostics)

    rules = load_rules()
    ctx = {"entities": entities, "predicates": predicates,
           "ids": {n["id"] for n in nodes}}
    problems = validate(nodes, ctx, rules)
    log(f"[resolution] {len(rules)} rules executed, {len(problems)} violation(s)")
    if problems:
        return None, diagnostics.sort(problems)

    edges = resolve(nodes, entities, predicates)
    ckm = build(nodes, edges, entities, core_types, project.name)
    log(f"[ckm]        {ckm['statistics']['nodes']} nodes, {ckm['statistics']['edges']} edges")
    return ckm, []


def emit_all(project, ckm):
    out = project / "build"
    out.mkdir(parents=True, exist_ok=True)
    written = {}
    for filename, emitter in EMITTERS.items():
        text = emitter(ckm)
        (out / filename).write_text(text)
        written[filename] = text
    return out, written
