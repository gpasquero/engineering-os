"""The Canonical Knowledge Model — the product (ADR-0072).

A Layer A concept, not a compiler artifact (ADR-0076). This module materialises
it; it does not invent it.
"""
import collections

from ..runtime.phases import feature

FORMAT_VERSION = "1.0.0"
METAMODEL_VERSION = "0.4.0-skeleton"


@feature("canonical knowledge model",
         input_phase="resolution", output_phase="ckm",
         invariants=["the model is the product; every other output derives from it (ADR-0072)",
                     "node and edge order is stable",
                     "no statistic is stored that cannot be recomputed from nodes and edges",
                     "provenance names the source of every node",
                     "the model carries the vocabulary needed to explain its own edges",
                     "field order is normalised; extraction order never reaches the product"],
         determinism="fully determined by the resolved assertion set; carries no timestamp")
def build(nodes, edges, entities, core_types, project_name):
    nodes = sorted(nodes, key=lambda n: n["id"])
    by_type = collections.Counter(n["type"] for n in nodes)
    by_family = collections.Counter(entities.get(n["type"], "unassigned") for n in nodes)
    return {
        "formatVersion": FORMAT_VERSION,
        "metamodelVersion": METAMODEL_VERSION,
        "project": project_name,
        "note": "Canonical Knowledge Model. Every edge was asserted; none inferred "
                "(ADR-0044, ADR-0061). Serializations are projections of this model, "
                "not the model (ADR-0076).",
        "nodes": [{"id": n["id"], "type": n["type"], "label": n["label"],
                   "family": entities.get(n["type"], "unassigned"),
                   "position": n["position"], "description": n["body"],
                   "provenance": {"source": n["source"]}} for n in nodes],
        "edges": edges,
        # Key order is normalised: how a registry happened to extract a field must
        # not leak into the product.
        "vocabulary": {c: {"category": core_types[c].get("category"),
                           "means": core_types[c].get("means"),
                           "inverse": core_types[c].get("inverse")}
                       for c in sorted({e["core"] for e in edges}) if c in core_types},
        "statistics": {
            "nodes": len(nodes), "edges": len(edges),
            "byType": dict(sorted(by_type.items())),
            "byFamily": dict(sorted(by_family.items())),
            "byCategory": dict(sorted(collections.Counter(
                e["category"] for e in edges).items())),
            "byCoreType": dict(sorted(collections.Counter(
                e["core"] for e in edges).items())),
        },
    }
