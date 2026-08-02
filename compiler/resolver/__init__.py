"""Resolution — assertions to a resolved assertion set.

Resolution builds edges. It does NOT decide whether the model is valid; that is
the validator executing declarative rules (ADR-0077). It reads nothing from disk:
the metamodel reaches it through registries (ADR-0083).
"""
from ..runtime.phases import feature
from ..registry import load_all


def load_metamodel():
    """The compiler's rulebook, via registries rather than ad-hoc readers."""
    reg = load_all()
    entities = {name: entry.get("entity-family") or "unassigned"
                for name, entry in reg["REG-entity-types"].items()}
    predicates = {name: (entry["core"], entry["category"])
                  for name, entry in reg["REG-relationship-predicates"].items()}
    core_types = {}
    for name, entry in reg["REG-core-relationship-types"].items():
        core_types[name] = dict(entry)
        # An inverse IS a core type. The vocabulary tables declare the pair on one
        # row; the registry reads the row, and the pair is unfolded here because
        # that is interpretation, not extraction.
        inverse = entry.get("inverse")
        if inverse and inverse not in core_types:
            core_types[inverse] = {"category": core_types[name]["category"],
                                   "means": f"inverse of {name}", "inverse": name}
    return entities, predicates, core_types


@feature("edge resolution",
         input_phase="parsing", output_phase="resolution",
         invariants=["no edge is created that was not asserted (ADR-0044)",
                     "an edge is created only when its target resolves",
                     "every edge carries its core type and category",
                     "resolution reads no file; the metamodel arrives via registries"],
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
