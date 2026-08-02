"""The Candidate Engineering Model — the substantive output of discovery.

Not a collection of arbitrary observations (ADR-0107). A serialized model
carrying proposed entities, relationships, invariants, capabilities, workflows,
evidence and traceability, **plus what discovery could not settle**: ambiguities,
conflicts and gaps.

Every proposal carries provenance, support classification, and its origin.
"""
import json
import hashlib


class Candidate:
    """Accumulates proposals. Never writes authoritative knowledge."""

    def __init__(self, repository, bootstrap):
        # Coerced: a candidate model is serialized, and a path object is not.
        self.repository = str(repository)
        self.bootstrap = str(bootstrap)
        self.entities, self.relationships = [], []
        self.classifications, self.invariants = [], []
        self.capabilities, self.workflows = [], []
        self.evidence, self.traceability = [], []
        self.ambiguities, self.conflicts, self.gaps = [], [], []
        self._ids = set()

    # -- proposals ---------------------------------------------------------
    def entity(self, node_id, node_type, label, *, support, source, locator=None,
               worker, task, attributes=None):
        if node_id in self._ids:
            return None
        self._ids.add(node_id)
        self.entities.append({
            "id": node_id, "type": node_type, "label": label,
            "support": support,
            "provenance": {"source": source, "locator": locator},
            "origin": {"worker": worker, "task": task},
            "attributes": attributes or {},
        })
        return node_id

    def relation(self, subject, predicate, obj, *, support, source, worker, task,
                 rule=None, locator=None):
        self.relationships.append({
            "from": subject, "predicate": predicate, "to": obj,
            "support": support,
            "provenance": {"source": source, "locator": locator},
            "origin": {"worker": worker, "task": task, "rule": rule},
        })

    def classification(self, node_id, dimension, value, *, support, source,
                       worker, task):
        self.classifications.append({
            "node": node_id, "dimension": dimension, "value": value,
            "support": support, "provenance": {"source": source},
            "origin": {"worker": worker, "task": task}})

    def ambiguity(self, about, readings, *, source, worker, task):
        self.ambiguities.append({
            "about": about, "readings": readings, "support": "S-ambiguous",
            "provenance": {"source": source}, "origin": {"worker": worker, "task": task}})

    def conflict(self, about, positions, *, worker, task):
        self.conflicts.append({
            "about": about, "positions": positions, "support": "S-conflicting",
            "origin": {"worker": worker, "task": task}})

    def gap(self, what, why, *, worker, task, source=None):
        self.gaps.append({
            "what": what, "why": why, "support": "S-unknown",
            "provenance": {"source": source}, "origin": {"worker": worker, "task": task}})

    # -- serialization -----------------------------------------------------
    def serialize(self):
        body = {
            "candidateModelVersion": "1.0.0",
            "repository": self.repository,
            "bootstrap": self.bootstrap,
            "note": "A PROPOSAL. Nothing here is authoritative until reviewed and "
                    "applied (ADR-0105, ADR-0106).",
            "proposals": {
                "entities": sorted(self.entities, key=lambda e: e["id"]),
                "relationships": sorted(
                    self.relationships, key=lambda r: (r["from"], r["predicate"], r["to"])),
                "classifications": sorted(
                    self.classifications, key=lambda c: (c["node"], c["dimension"])),
            },
            "unsettled": {
                "ambiguities": sorted(self.ambiguities, key=lambda a: a["about"]),
                "conflicts": sorted(self.conflicts, key=lambda c: c["about"]),
                "gaps": sorted(self.gaps, key=lambda g: g["what"]),
            },
            "statistics": self.statistics(),
        }
        # A digest over content only, so the same repository yields the same model.
        body["digest"] = hashlib.sha256(
            json.dumps(body, sort_keys=True).encode()).hexdigest()[:16]
        return body

    def statistics(self):
        by_support, by_type, by_worker, by_origin, by_rule = {}, {}, {}, {}, {}
        for e in self.entities:
            by_support[e["support"]] = by_support.get(e["support"], 0) + 1
            by_type[e["type"]] = by_type.get(e["type"], 0) + 1
            w = e["origin"]["worker"]
            by_worker[w] = by_worker.get(w, 0) + 1
            # Origin kind (ADR-0109) — what KIND of process produced it.
            o = (e.get("attributes") or {}).get("origin", "O-mechanical-extraction")
            by_origin[o] = by_origin.get(o, 0) + 1
            r_ = (e.get("attributes") or {}).get("rule")
            if r_:
                by_rule[r_] = by_rule.get(r_, 0) + 1
        for r in self.relationships:
            by_support[r["support"]] = by_support.get(r["support"], 0) + 1
            w = r["origin"]["worker"]
            by_worker[w] = by_worker.get(w, 0) + 1
            o = "O-deterministic-rule" if r["origin"].get("rule") else "O-mechanical-extraction"
            by_origin[o] = by_origin.get(o, 0) + 1
        return {
            "entities": len(self.entities),
            "relationships": len(self.relationships),
            "classifications": len(self.classifications),
            "ambiguities": len(self.ambiguities),
            "conflicts": len(self.conflicts),
            "gaps": len(self.gaps),
            "bySupport": dict(sorted(by_support.items())),
            "byType": dict(sorted(by_type.items())),
            "byWorker": dict(sorted(by_worker.items())),
            "byOrigin": dict(sorted(by_origin.items())),
            "byRule": dict(sorted(by_rule.items())),
        }
