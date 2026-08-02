#!/usr/bin/env python3
"""Ask the Canonical Knowledge Model an engineering question.

A **consumer** of the CKM (ADR-0081). It parses no authoring source and rebuilds
no semantic understanding — it reads the model the compiler produced.

    python3 tools/ask.py <project> impact Concept.Order
    python3 tools/ask.py <project> questions            # what can be asked
    python3 tools/ask.py <project> impact Concept.Order --json

`--json` makes every answer machine-consumable, because an agent is a
first-class consumer and not an eventual one (ADR-0080).

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib
import collections

ROOT = pathlib.Path(__file__).resolve().parent.parent

DERIVES = {"derives-from", "derived-into", "implements", "implemented-by", "represents"}
QUESTIONS = {}


def question(name, prompt):
    def wrap(fn):
        QUESTIONS[name] = {"prompt": prompt, "fn": fn}
        return fn
    return wrap


class Model:
    """A read-only view over the Canonical Knowledge Model."""

    def __init__(self, ckm):
        self.ckm = ckm
        self.by_id = {n["id"]: n for n in ckm["nodes"]}
        self.out = collections.defaultdict(list)
        self.inc = collections.defaultdict(list)
        for e in ckm["edges"]:
            self.out[e["from"]].append(e)
            self.inc[e["to"]].append(e)

    def label(self, node_id):
        n = self.by_id.get(node_id)
        return f"{n['label']} ({n['type']})" if n else node_id

    def closure(self, start, step):
        """Breadth-first transitive closure. Returns [{id, hops, via}]."""
        seen, queue = {}, [(start, 0, None)]
        while queue:
            node_id, hops, via = queue.pop(0)
            for e in step(node_id):
                nxt = e["to"] if e["from"] == node_id else e["from"]
                if nxt == start or nxt in seen:
                    continue
                seen[nxt] = {"id": nxt, "hops": hops + 1, "via": via or e["predicate"]}
                queue.append((nxt, hops + 1, via or e["predicate"]))
        return sorted(seen.values(), key=lambda r: (r["hops"], r["id"]))


# ---------------------------------------------------------------- questions
@question("impact", "What breaks if I change this?")
def _impact(m, target):
    found = m.closure(target, lambda i: m.inc[i])
    return {"affected": found,
            "direct": sum(1 for f in found if f["hops"] == 1),
            "transitive": sum(1 for f in found if f["hops"] > 1)}


@question("why", "Why does this relationship exist?")
def _why(m, target):
    rows = []
    for e in m.out[target] + m.inc[target]:
        voc = m.ckm.get("vocabulary", {}).get(e["core"], {})
        rows.append({"from": e["from"], "predicate": e["predicate"], "to": e["to"],
                     "core": e["core"], "category": e["category"],
                     "means": voc.get("means")})
    return {"relationships": rows}


@question("rationale", "Which ADR established this?")
def _rationale(m, target):
    adrs = [{"adr": e["from"], "label": m.by_id[e["from"]]["label"], "via": e["predicate"]}
            for e in m.inc[target]
            if m.by_id.get(e["from"], {}).get("type") == "ADR" and e["core"] == "establishes"]
    superseded = [{"adr": a["adr"], "superseded_by": e["to"]}
                  for a in adrs for e in m.out[a["adr"]] if e["predicate"] == "superseded-by"]
    return {"established_by": adrs, "superseded": superseded}


@question("provenance", "Where did this come from?")
def _provenance(m, target):
    n = m.by_id[target]
    return {"source": (n.get("provenance") or {}).get("source"),
            "project": m.ckm.get("project"),
            "metamodelVersion": m.ckm.get("metamodelVersion"),
            "note": "Source revision is not recorded; ADR-0064 wants (artifact-id, revision-id)."}


@question("dependents", "Which Capabilities depend on this?")
def _dependents(m, target):
    reach = {f["id"] for f in m.closure(target, lambda i: m.out[i] + m.inc[i])}
    caps = [c for c in reach if m.by_id[c]["type"] == "Capability"]
    return {"capabilities": sorted(caps)}


@question("tests", "Which Tests must change?")
def _tests(m, target):
    reach = {target} | {f["id"] for f in m.closure(target, lambda i: m.inc[i])}
    tests = [n["id"] for n in m.ckm["nodes"]
             if any(e["core"] == "validates" for e in m.out[n["id"]])
             and (set(e["to"] for e in m.out[n["id"]]) & reach or n["id"] in reach)]
    return {"tests": sorted(tests),
            "note": "A test is an Artifact that `validates` another. There is no Test entity."}


@question("specifications", "Which Specifications become inconsistent?")
def _specifications(m, target):
    specs = [e["from"] for e in m.inc[target] if e["core"] == "represents"]
    return {"specifications": sorted(specs),
            "note": "A specification is an Artifact that `represents` a Concept."}


@question("status", "What is the implementation status?")
def _status(m, target):
    revs = [e["to"] for e in m.out[target] if e["predicate"] == "has-active-revision"] or [target]
    out = []
    for r in revs:
        accepted = [e["from"] for e in m.inc[r]
                    if m.by_id.get(e["from"], {}).get("type") == "AcceptanceRecord"]
        out.append({"revision": r, "accepted_by": accepted,
                    "active": bool(accepted)})
    return {"revisions": out,
            "note": "Acceptance confers Active status; commits do not (ADR-0018)."}


@question("unenforced", "Which Invariants have no enforcement point?")
def _unenforced(m, _target):
    rows = [{"invariant": n["id"], "label": n["label"]}
            for n in m.ckm["nodes"] if n["type"] == "Invariant"
            and not any(e["predicate"] == "enforced-at" for e in m.out[n["id"]])]
    return {"unenforced": rows,
            "note": "The gap is the finding. `enforced-at` is zero-or-more by decision."}


# -------------------------------------------------------------------- main
def render(name, target, answer):
    lines = [f"{QUESTIONS[name]['prompt']}", f"  subject: {target}" if target else "", ""]
    def walk(value, indent="  "):
        if isinstance(value, dict):
            for k, v in value.items():
                if isinstance(v, (dict, list)) and v:
                    lines.append(f"{indent}{k}:")
                    walk(v, indent + "  ")
                elif not isinstance(v, (dict, list)):
                    lines.append(f"{indent}{k}: {v}")
                else:
                    lines.append(f"{indent}{k}: (none)")
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    lines.append(indent + "  ".join(f"{k}={v}" for k, v in item.items()))
                else:
                    lines.append(f"{indent}{item}")
    walk(answer)
    return "\n".join(l for l in lines if l is not None)


def main(argv):
    as_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = ROOT / argv[1]
    ckm_path = project / "build/canonical-knowledge-model.json"
    if not ckm_path.exists():
        print(f"no compiled model at {ckm_path}\nrun: python3 tools/compile.py {argv[1]}")
        return 1
    m = Model(json.loads(ckm_path.read_text()))

    name = argv[2]
    if name == "questions":
        for key, q in QUESTIONS.items():
            print(f"  {key:<15} {q['prompt']}")
        return 0
    if name not in QUESTIONS:
        print(f"unknown question {name!r}. Try: questions")
        return 2

    target = argv[3] if len(argv) > 3 else None
    if target and target not in m.by_id:
        print(f"unknown node {target!r}")
        return 1

    answer = QUESTIONS[name]["fn"](m, target)
    if as_json:
        print(json.dumps({"question": name, "subject": target, "answer": answer}, indent=2))
    else:
        print(render(name, target, answer))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
