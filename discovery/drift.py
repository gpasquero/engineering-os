"""Knowledge Drift — compare a maintained model against a fresh candidate.

`ADR-0112`. **Periodic Reacquisition does not rebuild the model. It challenges
it.** Every item below is a proposal requiring review; nothing is applied.

The comparison is between:

  * the **Authoritative Engineering Model** — what was curated and maintained
  * a **fresh Candidate Engineering Model** — full onboarding-quality discovery
    against the current repository

Its value is entirely in what the two disagree about.
"""
import json
import pathlib

CATEGORIES = json.loads("{}")  # loaded from the registry at call time


def report(authoritative_nodes, authoritative_edges, candidate, incremental_ids=None):
    """Returns a Knowledge Drift Report. Every item is a proposal."""
    auth = {n["id"]: n for n in authoritative_nodes}
    cand = {e["id"]: e for e in candidate["proposals"]["entities"]}
    incremental = set(incremental_ids or [])

    items = {c: [] for c in (
        "D-new-knowledge", "D-unsupported-assertion",
        "D-implementation-without-knowledge", "D-knowledge-without-implementation",
        "D-invariant-without-enforcement", "D-dependency-change",
        "D-boundary-change", "D-conflicting-interpretation",
        "D-missed-incremental-update", "D-stale-provenance",
        "D-unexplained-divergence")}

    # Knowledge the fresh discovery has and the maintained model does not.
    for cid, c in sorted(cand.items()):
        if cid in auth:
            continue
        entry = {"subject": cid, "type": c["type"],
                 "evidence": c["provenance"]["source"]}
        # A change that continuous acquisition SHOULD have caught and did not is
        # the category the report exists for.
        if incremental and cid not in incremental and _is_recent(c, incremental):
            items["D-missed-incremental-update"].append(entry)
        elif c["type"] in ("Artifact", "Capability", "Concept"):
            items["D-implementation-without-knowledge"].append(entry)
        else:
            items["D-new-knowledge"].append(entry)

    # Maintained assertions the fresh discovery no longer supports.
    for aid, a in sorted(auth.items()):
        if aid in cand:
            continue
        src = (a.get("attributes") or {}).get("source")
        entry = {"subject": aid, "type": a["type"], "was-evidenced-by": src}
        if (a.get("attributes") or {}).get("proposed-by"):
            items["D-unsupported-assertion"].append(entry)
        else:
            items["D-stale-provenance"].append(entry)

    # Modelled capabilities with no realising artifact, and invariants with no
    # enforcement — computed over the MAINTAINED model, which is what is being
    # challenged.
    realised = {e["to"] for e in authoritative_edges
                if e["predicate"] in ("implements", "realised-by", "validates")}
    enforced = {e["from"] for e in authoritative_edges
                if e["predicate"] in ("enforced-at", "enforced-by")}
    for aid, a in sorted(auth.items()):
        if a["type"] == "Capability" and aid not in realised:
            items["D-knowledge-without-implementation"].append(
                {"subject": aid, "why": "no artifact implements or validates it"})
        if a["type"] == "Invariant" and aid not in enforced:
            items["D-invariant-without-enforcement"].append(
                {"subject": aid, "why": "nothing is recorded as enforcing it"})

    # Same subject, different label — two readings of one fact.
    for cid, c in sorted(cand.items()):
        a = auth.get(cid)
        if a and a.get("label") and c.get("label") and a["label"] != c["label"]:
            items["D-conflicting-interpretation"].append(
                {"subject": cid, "maintained": a["label"], "rediscovered": c["label"]})

    return {
        "mode": "periodic-reacquisition",
        "note": "Reacquisition validates and challenges the maintained model. It "
                "does not replace it. EVERY ITEM IS A PROPOSAL REQUIRING REVIEW "
                "(ADR-0112).",
        "candidateDigest": candidate.get("mechanicalModelDigest"),
        "authoritativeNodes": len(auth),
        "candidateProposals": len(cand),
        "items": {k: v for k, v in items.items() if v},
        "statistics": {k: len(v) for k, v in sorted(items.items())},
    }


def _is_recent(entity, incremental_ids):
    """Was this in the same evidence neighbourhood continuous acquisition saw?"""
    src = entity["provenance"]["source"] or ""
    return any(src and src in i for i in incremental_ids)
