"""The semantic query engine — the semantic API of Engineering OS (ADR-0086).

A **consumer** of the Canonical Knowledge Model (ADR-0081). It parses no
authoring source.

The engine implements OPERATORS. Questions are declared in `model/queries.md`
and arrive through a registry. Adding a question is a data change; adding an
operator is an engine change and should be rare.
"""
from ..runtime.phases import feature
from ..registry import load_all

OPERATORS = {}


def operator(name):
    def wrap(fn):
        OPERATORS[name] = fn
        return fn
    return wrap


def load_queries():
    queries = load_all()["REG-queries"]
    unknown = sorted({op for q in queries.values() for step in q["steps"] for op in step
                      if op not in OPERATORS})
    if unknown:
        raise SystemExit(f"queries naming unimplemented operators: {unknown}")
    return queries


class Model:
    """A read-only view over the Canonical Knowledge Model."""

    def __init__(self, ckm):
        self.ckm = ckm
        self.by_id = {n["id"]: n for n in ckm["nodes"]}
        self.out, self.inc = {}, {}
        for e in ckm["edges"]:
            self.out.setdefault(e["from"], []).append(e)
            self.inc.setdefault(e["to"], []).append(e)

    def edges(self, node_id, direction):
        if direction == "out":
            return [(e, e["to"]) for e in self.out.get(node_id, [])]
        if direction == "in":
            return [(e, e["from"]) for e in self.inc.get(node_id, [])]
        return ([(e, e["to"]) for e in self.out.get(node_id, [])]
                + [(e, e["from"]) for e in self.inc.get(node_id, [])])

    def matches(self, edge, other, spec):
        if spec.get("predicate") and edge["predicate"] != spec["predicate"]:
            return False
        if spec.get("core") and edge["core"] != spec["core"]:
            return False
        if spec.get("category") and edge["category"] != spec["category"]:
            return False
        if spec.get("node-type") and self.by_id.get(other, {}).get("type") != spec["node-type"]:
            return False
        return True

    def row(self, node_id, **extra):
        n = self.by_id.get(node_id, {})
        return {"id": node_id, "type": n.get("type"), "label": n.get("label"), **extra}


# ------------------------------------------------------------- operators
@operator("select")
def _select(m, rows, spec, subject):
    if spec.get("all"):
        return [m.row(n["id"]) for n in m.ckm["nodes"]]
    if spec.get("subject"):
        return [m.row(subject)] if subject in m.by_id else []
    if spec.get("id"):
        return [m.row(spec["id"])] if spec["id"] in m.by_id else []
    if spec.get("type"):
        return [m.row(n["id"]) for n in m.ckm["nodes"] if n["type"] == spec["type"]]
    return rows


@operator("traverse")
def _traverse(m, rows, spec, subject):
    starts = [r["id"] for r in rows] or ([subject] if subject in m.by_id else [])
    direction = spec.get("direction", "out")
    origin = set(starts)
    seen, queue = {}, [(s, 0, None) for s in starts]

    while queue:
        node_id, hops, via = queue.pop(0)
        if not spec.get("transitive") and hops >= spec.get("max-hops", 1):
            continue
        for edge, other in m.edges(node_id, direction):
            if not m.matches(edge, other, spec) or other in origin or other in seen:
                continue
            seen[other] = m.row(other, hops=hops + 1, via=via or edge["predicate"])
            queue.append((other, hops + 1, via or edge["predicate"]))

    out = sorted(seen.values(), key=lambda r: (r["hops"], r["id"]))
    if not out and spec.get("or-self"):
        return [m.row(s, hops=0, via=None) for s in starts]
    return out


def _has_edge(m, node_id, spec):
    return any(m.matches(e, o, spec) for e, o in m.edges(node_id, spec.get("direction", "out")))


def _row_matches(m, row, spec):
    if spec.get("type"):
        return row["type"] == spec["type"]
    if spec.get("has-edge"):
        return _has_edge(m, row["id"], spec["has-edge"])
    return False


@operator("keep")
def _keep(m, rows, spec, subject):
    return [r for r in rows if _row_matches(m, r, spec)]


@operator("reject")
def _reject(m, rows, spec, subject):
    return [r for r in rows if not _row_matches(m, r, spec)]


@operator("with")
def _with(m, rows, spec, subject):
    for row in rows:
        for name, sub in spec.items():
            row[name] = [other for _, other in m.edges(row["id"], sub.get("direction", "out"))
                         if m.matches(_edge_of(m, row["id"], other, sub), other, sub)]
    return rows


def _edge_of(m, node_id, other, sub):
    for edge, o in m.edges(node_id, sub.get("direction", "out")):
        if o == other:
            return edge
    return {}


# ------------------------------------------------------------------- run
@feature("semantic query execution",
         input_phase="ckm", output_phase="projection",
         invariants=["a query reads the model and never an authoring source (ADR-0081)",
                     "every declared operator is implemented, or loading aborts",
                     "the engine holds operators; questions are data (ADR-0086)"],
         determinism="rows are sorted by (hops, id); a query is a pure function of model and subject")
def run(model, query, subject=None):
    rows = []
    for step in query["steps"]:
        for name, spec in step.items():
            rows = OPERATORS[name](model, rows, spec, subject)
    if query.get("output") == "edges":
        ids = {r["id"] for r in rows} | ({subject} if subject else set())
        return [e for e in model.ckm["edges"] if e["from"] in ids and e["to"] in ids]
    return rows
