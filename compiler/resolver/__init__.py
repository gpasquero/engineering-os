"""Resolution — assertions to a resolved assertion set.

Resolution builds edges. It does NOT decide whether the model is valid; that is
the validator executing declarative rules (ADR-0077).
"""
import re
import pathlib

from ..runtime.phases import feature

METAMODEL = pathlib.Path(__file__).resolve().parents[2] / "model/metamodel"


def load_metamodel():
    """The compiler's rulebook, read from the metamodel rather than hard-coded."""
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

    # Core-type definitions, so the model can answer "why does this edge exist?"
    core_types = {}
    for category in ("Structural", "Behavioral", "Semantic", "Traceability"):
        block = re.search(rf"^### {category} — .*?\n(.*?)(?=^###|^## )", voc, re.M | re.S)
        if not block:
            continue
        for core, means, inverse in re.findall(
                r"^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \|", block.group(1), re.M):
            core_types[core] = {"category": category.lower(),
                                "means": means.strip(), "inverse": inverse}
            core_types.setdefault(inverse, {"category": category.lower(),
                                            "means": f"inverse of {core}", "inverse": core})
    return entities, predicates, core_types


@feature("edge resolution",
         input_phase="parsing", output_phase="resolution",
         invariants=["no edge is created that was not asserted (ADR-0044)",
                     "an edge is created only when its target resolves",
                     "every edge carries its core type and category"],
         determinism="edges are sorted by (from, predicate, to)")
def resolve(nodes, entities, predicates):
    ids = {n["id"] for n in nodes}
    edges = []
    for n in nodes:
        for predicate, target in n["relationships"]:
            if target in ids and predicate in predicates:
                core, category = predicates[predicate]
                edges.append({"from": n["id"], "predicate": predicate, "to": target,
                              "core": core, "category": category})
    edges.sort(key=lambda e: (e["from"], e["predicate"], e["to"]))
    return edges
