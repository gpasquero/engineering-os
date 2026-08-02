"""Search, impact and traceability indexes — projections of the model.

Each is derived by the same query engine the Director uses (`ADR-0086`), so an
index and an answer cannot disagree.
"""
import json

from ...runtime.phases import feature
from ...query import Model, run, load_queries


@feature("index projection",
         input_phase="ckm", output_phase="projection",
         invariants=["indexes are derived by the declared query engine, not by "
                     "a second traversal",
                     "an index and a query answer cannot disagree",
                     "no index carries a score (ADR-0090)"],
         determinism="derived from deterministic queries; keys sorted")
def emit(ckm):
    model, queries = Model(ckm), load_queries()

    search = sorted(
        ({"id": n["id"], "type": n["type"], "label": n["label"],
          "family": n["family"],
          "text": " ".join(filter(None, [n["label"], n["type"],
                                         (n.get("description") or "")[:200]])).lower(),
          "attributes": n.get("attributes") or {}}
         for n in ckm["nodes"]), key=lambda r: r["id"])

    impact, traceability = {}, {}
    for n in ckm["nodes"]:
        answer = run(model, queries["Q-impact"], n["id"])
        if answer["rows"]:
            impact[n["id"]] = [{"id": r["id"], "hops": r["hops"], "via": r.get("via")}
                               for r in answer["rows"]]
        ev = run(model, queries["Q-evidence"], n["id"])
        rat = run(model, queries["Q-rationale"], n["id"])
        if ev["rows"] or rat["rows"]:
            traceability[n["id"]] = {
                "evidence": [r["id"] for r in ev["rows"]],
                "rationale": [r["id"] for r in rat["rows"]],
            }

    return json.dumps({
        "note": "Projections of the Canonical Knowledge Model, derived by the "
                "declared query engine (ADR-0086).",
        "search": search,
        "impact": dict(sorted(impact.items())),
        "traceability": dict(sorted(traceability.items())),
        "statistics": {"searchable": len(search), "withImpact": len(impact),
                       "withTraceability": len(traceability)},
    }, indent=2) + "\n"
