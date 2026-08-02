"""The Proposal Applier — accepted proposals become authoring sources.

> **Not a model write.** An approved assertion is authored into the repository
> and recompiled like everything else (`ADR-0106`), so the compiler remains the
> only writer of the Canonical Knowledge Model and `ADR-0072` survives untouched.

One mechanism serves two purposes: discovery intake and the loop's knowledge
update. They are the same artifact at different scales.
"""
import re
import pathlib

import yaml

from ..runtime.phases import feature
from ..registry import load_all

BATCHABLE = None  # loaded from the registry


def _review_mode():
    """Which support classifications may be accepted in batch, per the registry."""
    reg = load_all()["REG-support-classification"]
    return {sid: ("batch" if s["review"].strip().lower().startswith("may be accepted in batch")
                  or "batch-acceptable" in s["review"].lower() else "individual")
            for sid, s in reg.items()}


def _slug(node_id):
    return re.sub(r"[^A-Za-z0-9]+", "-", node_id).strip("-").lower()


@feature("proposal authorization",
         input_phase="projection", output_phase="projection",
         invariants=["a proposal is never applied unauthorized (ADR-0100)",
                     "individual-review classifications are never batch-accepted",
                     "an authorization names what it accepted and what it left"],
         determinism="selection is by declared predicate; order is by node id")
def authorize(candidate, *, accept_types=None, accept_ids=None, accept_support=None,
              reviewer=None):
    """Select a coherent subset. Returns (authorized, rejected, diagnostics)."""
    modes = _review_mode()
    entities = candidate["proposals"]["entities"]
    relationships = candidate["proposals"]["relationships"]

    def wanted(e):
        if accept_ids is not None and e["id"] in accept_ids:
            return True
        if accept_types and e["type"] in accept_types:
            return True
        return False

    picked = sorted((e for e in entities if wanted(e)), key=lambda e: e["id"])
    diagnostics = []
    if accept_support:
        kept = []
        for e in picked:
            if modes.get(e["support"]) == "individual" and e["support"] not in accept_support:
                diagnostics.append(
                    f"{e['id']}: support {e['support']} requires individual review "
                    f"and was not individually accepted")
            else:
                kept.append(e)
        picked = kept

    ids = {e["id"] for e in picked}
    # A relationship is authorized only when BOTH endpoints are: an edge to an
    # unaccepted node would compile to a dangling reference.
    edges, dropped = [], []
    for r in relationships:
        (edges if r["from"] in ids and r["to"] in ids else dropped).append(r)
    if dropped:
        diagnostics.append(
            f"{len(dropped)} relationship(s) not authorized: an endpoint was not accepted")

    return ({"reviewer": reviewer, "entities": picked, "relationships": edges},
            {"entities": [e for e in entities if e["id"] not in ids],
             "relationships": dropped},
            diagnostics)


@feature("proposal application",
         input_phase="projection", output_phase="authoring",
         invariants=["an accepted proposal becomes an AUTHORING SOURCE, never a "
                     "model write (ADR-0106)",
                     "every written source carries the provenance the proposal carried",
                     "every written source records the worker and task that "
                     "proposed it",
                     "generated sources are emitted by a YAML writer, never by "
                     "hand-rolled quoting",
                     "no language model participates"],
         determinism="a pure function of the authorization; filenames derive from node ids")
def apply(authorized, target):
    """Write authorized proposals as authoring sources. Returns the paths written."""
    model_dir = pathlib.Path(target) / "model"
    model_dir.mkdir(parents=True, exist_ok=True)

    by_subject = {}
    for r in authorized["relationships"]:
        by_subject.setdefault(r["from"], []).append(r)

    written = []
    for e in authorized["entities"]:
        attrs = dict(e.get("attributes") or {})
        attrs.setdefault("source", e["provenance"]["source"])
        if e["provenance"].get("locator"):
            attrs.setdefault("locator", e["provenance"]["locator"])
        attrs["support"] = e["support"]
        attrs["proposed-by"] = e["origin"]["worker"]
        attrs["proposed-in"] = e["origin"]["task"]

        # A generated source is compiler input. Emit YAML with a YAML writer:
        # hand-rolled quoting was wrong for labels containing ':' and for values
        # beginning with a YAML indicator such as '@'.
        head = {"id": e["id"], "type": e["type"], "label": e["label"],
                "attributes": {k: str(v) for k, v in sorted(attrs.items())}}
        lines = ["---"]
        lines.append(yaml.safe_dump(head, sort_keys=False,
                                    default_flow_style=False,
                                    allow_unicode=True).rstrip())
        rels = by_subject.get(e["id"], [])
        rel_list = [{r["predicate"]: r["to"]}
                    for r in sorted(rels, key=lambda x: (x["predicate"], x["to"]))]
        lines.append(yaml.safe_dump({"relationships": rel_list}, sort_keys=False,
                                    default_flow_style=False,
                                    allow_unicode=True).rstrip())
        lines += ["---", ""]

        origin = e["origin"]
        rule = next((r["origin"].get("rule") for r in rels
                     if r["origin"].get("rule")), None)
        lines.append(
            f"Proposed by `{origin['worker']}` in task `{origin['task']}` and "
            f"accepted through review. Support: `{e['support']}`.")
        if rule:
            lines.append(f"\nInferred by rule `{rule}`.")
        lines.append(
            "\n**Authored from a discovery proposal** (`ADR-0106`). This is an "
            "authoring source, not a model write: the compiler reads it exactly "
            "as it reads a hand-written one.")

        path = model_dir / f"{_slug(e['id'])}.md"
        path.write_text("\n".join(lines) + "\n")
        written.append(path)
    return written
