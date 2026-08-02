"""The semantic query engine — the semantic API of Engineering OS (ADR-0086).

A **consumer** of the Canonical Knowledge Model (ADR-0081). It parses no
authoring source.

The engine implements OPERATORS. Questions are declared in `model/queries.md`.
The result contract is `ADR-0088`:

  * a row carries the **complete ordered path**, never one predicate;
  * `output: edges` returns edges actually traversed, not an induced subgraph;
  * `with` evaluates the edge in hand, so parallel edges are unambiguous;
  * declarations are validated — an unknown field fails;
  * applicability is distinguished from emptiness;
  * cycles, ties, ordering, depth and result count are defined and bounded.
"""
import pathlib

import yaml

from ..runtime.phases import feature
from ..runtime.diagnostics import Diagnostic
from ..registry import load_all

SCHEMA = yaml.safe_load((pathlib.Path(__file__).parent / "schema.yaml").read_text())

DEFAULT_MAX_DEPTH = 16
DEFAULT_MAX_RESULTS = 1000

OK, EMPTY, NOT_APPLICABLE, INVALID = "ok", "empty", "not-applicable", "invalid"

OPERATORS = {}


def operator(name):
    def wrap(fn):
        OPERATORS[name] = fn
        return fn
    return wrap


# ============================================================== validation
def _check_value(value, spec, where, vocab, out):
    kind = spec["type"]
    if kind == "bool" and not isinstance(value, bool):
        out.append(f"{where}: must be a boolean")
    elif kind == "str" and not isinstance(value, str):
        out.append(f"{where}: must be a string")
    elif kind == "posint" and not (isinstance(value, int) and not isinstance(value, bool)
                                   and value > 0):
        out.append(f"{where}: must be a positive integer")
    elif kind == "list" and not isinstance(value, list):
        out.append(f"{where}: must be a list")
    elif kind == "node-type" and value not in vocab["node-types"]:
        out.append(f"{where}: {value!r} is not a declared metamodel entity")
    elif kind == "predicate" and value not in vocab["predicates"]:
        out.append(f"{where}: {value!r} is not a registered predicate")
    elif kind == "core-type" and value not in vocab["core-types"]:
        out.append(f"{where}: {value!r} is not a registered core relationship type")
    if spec.get("enum") and value not in spec["enum"]:
        out.append(f"{where}: {value!r} must be one of {spec['enum']}")
    if spec.get("pattern"):
        import re
        if not isinstance(value, str) or not re.match(spec["pattern"], value):
            out.append(f"{where}: {value!r} must match {spec['pattern']}")


def _check_fields(mapping, definition, where, vocab, out):
    fields = definition.get("fields", {})
    for key, value in mapping.items():
        if key not in fields:
            out.append(f"{where}: unknown field {key!r} (permitted: {sorted(fields)})")
            continue
        if value is None:
            continue
        if fields[key]["type"] == "edge-spec":
            _check_fields(value, SCHEMA["edge-spec"], f"{where}.{key}", vocab, out)
        elif fields[key]["type"] == "edge-spec-list":
            if not isinstance(value, list) or not value:
                out.append(f"{where}.{key}: must be a non-empty list of edge specs")
            else:
                for i, step in enumerate(value):
                    if not isinstance(step, dict):
                        out.append(f"{where}.{key}[{i}]: must be a mapping")
                        continue
                    _check_fields(step, SCHEMA["edge-spec"], f"{where}.{key}[{i}]", vocab, out)
        elif fields[key]["type"] == "list" and fields[key].get("item"):
            for i, item in enumerate(value):
                _check_value(item, {"type": fields[key]["item"]},
                             f"{where}.{key}[{i}]", vocab, out)
        else:
            _check_value(value, fields[key], f"{where}.{key}", vocab, out)
    for key in definition.get("required", []):
        if mapping.get(key) in (None, ""):
            out.append(f"{where}: missing required field {key!r}")
    one_of = definition.get("exactly-one-of")
    if one_of:
        present = [k for k in one_of if mapping.get(k) not in (None, False)]
        if len(present) != 1:
            out.append(f"{where}: exactly one of {one_of} required, got {present}")


def validate_query(query, vocab):
    """Returns a list of message strings. Empty means the declaration is valid."""
    out = []
    where = f"query {query.get('id', '<no id>')!r}"
    _check_fields(query, SCHEMA["query"], where, vocab, out)
    if not isinstance(query.get("steps"), list) or not query.get("steps"):
        out.append(f"{where}: steps must be a non-empty list")
        return out
    for i, step in enumerate(query["steps"]):
        at = f"{where}.steps[{i}]"
        if not isinstance(step, dict):
            out.append(f"{at}: must be a mapping")
            continue
        if len(step) != 1:
            out.append(f"{at}: exactly one operator per step, got {sorted(step)}")
            continue
        (name, spec), = step.items()
        if name not in OPERATORS:
            out.append(f"{at}: unknown operator {name!r} (implemented: {sorted(OPERATORS)})")
            continue
        definition = SCHEMA["operators"][name]
        if definition.get("free-form"):
            for key, sub in (spec or {}).items():
                _check_fields(sub, SCHEMA["edge-spec"], f"{at}.{name}.{key}", vocab, out)
        else:
            _check_fields(spec or {}, definition, f"{at}.{name}", vocab, out)
    return out


def load_queries(strict=True):
    registries = load_all()
    vocab = {"node-types": set(registries["REG-entity-types"]),
             "predicates": set(registries["REG-relationship-predicates"]),
             "core-types": set(registries["REG-core-relationship-types"])
                           | {e["core"] for e in registries["REG-relationship-predicates"].values()}}
    queries = registries["REG-queries"]
    problems = {qid: validate_query(q, vocab) for qid, q in queries.items()}
    bad = {qid: msgs for qid, msgs in problems.items() if msgs}
    if bad and strict:
        lines = [f"  {m}" for msgs in bad.values() for m in msgs]
        raise SystemExit("invalid query declarations:\n" + "\n".join(lines))
    return queries


# ==================================================================== model
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
        """[(edge, other, direction)] — direction is per edge, so `both` is unambiguous."""
        out = [(e, e["to"], "out") for e in self.out.get(node_id, [])]
        inc = [(e, e["from"], "in") for e in self.inc.get(node_id, [])]
        return out if direction == "out" else inc if direction == "in" else out + inc

    def match(self, edge, other, spec):
        """Returns the list of reasons the edge matched, or None if it did not."""
        why = []
        for field, value in (("predicate", edge["predicate"]), ("core", edge["core"]),
                             ("category", edge["category"])):
            if spec.get(field) is not None:
                if value != spec[field]:
                    return None
                why.append(f"{field}={value}")
        if spec.get("node-type") is not None:
            actual = self.by_id.get(other, {}).get("type")
            if actual != spec["node-type"]:
                return None
            why.append(f"node-type={actual}")
        return why or ["any"]

    def row(self, node_id, **extra):
        n = self.by_id.get(node_id, {})
        return {"id": node_id, "type": n.get("type"), "label": n.get("label"), **extra}


def _hop(edge, other, direction, why):
    return {"from": edge["from"], "predicate": edge["predicate"], "to": edge["to"],
            "core": edge["core"], "category": edge["category"],
            "direction": direction, "matched": why, "reached": other}


def _path_key(path):
    """Deterministic tie-break between equal-length paths (ADR-0088 §6)."""
    return ([h["predicate"] for h in path], [h["reached"] for h in path])


# ------------------------------------------------------------- operators
@operator("select")
def _select(m, rows, spec, ctx):
    if spec.get("all"):
        return [m.row(n["id"], hops=0, origin=n["id"], path=[]) for n in m.ckm["nodes"]]
    if spec.get("subject"):
        s = ctx["subject"]
        return [m.row(s, hops=0, origin=s, path=[])] if s in m.by_id else []
    if spec.get("id"):
        i = spec["id"]
        return [m.row(i, hops=0, origin=i, path=[])] if i in m.by_id else []
    if spec.get("type"):
        return [m.row(n["id"], hops=0, origin=n["id"], path=[])
                for n in m.ckm["nodes"] if n["type"] == spec["type"]]
    return rows


@operator("traverse")
def _traverse(m, rows, spec, ctx):
    starts = [r["id"] for r in rows] or ([ctx["subject"]] if ctx["subject"] in m.by_id else [])
    direction = spec.get("direction", "out")
    depth_cap = ctx["max_depth"]
    limit = spec.get("max-hops") if not spec.get("transitive") else depth_cap
    limit = min(limit or 1, depth_cap)

    origin = set(starts)
    best, queue = {}, [(s, s, 0, []) for s in starts]
    truncated_depth = False

    while queue:
        node_id, start, hops, path = queue.pop(0)
        if hops >= limit:
            if spec.get("transitive") and m.edges(node_id, direction):
                truncated_depth = truncated_depth or hops >= depth_cap
            continue
        for edge, other, edge_dir in m.edges(node_id, direction):
            why = m.match(edge, other, spec)
            if why is None or other in origin:
                continue
            candidate = path + [_hop(edge, other, edge_dir, why)]
            prior = best.get(other)
            # cycles: first path wins; ties: lexicographically smallest path
            if prior is not None and (len(prior["path"]) < len(candidate)
                                      or (len(prior["path"]) == len(candidate)
                                          and _path_key(prior["path"]) <= _path_key(candidate))):
                continue
            best[other] = m.row(other, hops=len(candidate), origin=start,
                                path=candidate, via=candidate[0]["predicate"])
            queue.append((other, start, len(candidate), candidate))

    if truncated_depth:
        ctx["diagnostics"].append(Diagnostic(
            "projection", None,
            f"traversal truncated at max-depth {depth_cap}", ctx["query"]["id"]))

    result = sorted(best.values(), key=lambda r: (r["hops"], r["id"]))
    if not result and spec.get("or-self"):
        return [m.row(s, hops=0, origin=s, path=[], via=None) for s in starts]
    return result


def _has_edge(m, node_id, spec):
    return any(m.match(e, o, spec) is not None
               for e, o, _ in m.edges(node_id, spec.get("direction", "out")))


def _has_path(m, node_id, chain):
    """Does a path exist from node_id matching this ordered sequence of edge specs?

    Added because a real engineering question could not be expressed: *which
    implementation artifacts no longer match their original design rationale?*
    requires filtering a row on a property reached two hops away while still
    returning the row. `has-edge` is single-hop, and the pipeline cannot return
    to an earlier stage.
    """
    frontier = {node_id}
    for spec in chain:
        nxt = set()
        for current in frontier:
            for edge, other, _ in m.edges(current, spec.get("direction", "out")):
                if m.match(edge, other, spec) is not None:
                    nxt.add(other)
        if not nxt:
            return False
        frontier = nxt
    return True


def _row_matches(m, row, spec):
    if spec.get("type") is not None:
        return row["type"] == spec["type"]
    if spec.get("has-path") is not None:
        return _has_path(m, row["id"], spec["has-path"])
    return _has_edge(m, row["id"], spec["has-edge"])


@operator("keep")
def _keep(m, rows, spec, ctx):
    return [r for r in rows if _row_matches(m, r, spec)]


@operator("reject")
def _reject(m, rows, spec, ctx):
    return [r for r in rows if not _row_matches(m, r, spec)]


@operator("with")
def _with(m, rows, spec, ctx):
    """Evaluates the edge in hand. Parallel edges are never confused (ADR-0088 §3)."""
    for row in rows:
        for name, sub in spec.items():
            found = []
            for edge, other, edge_dir in m.edges(row["id"], sub.get("direction", "out")):
                why = m.match(edge, other, sub)
                if why is not None:
                    found.append({"id": other, "predicate": edge["predicate"],
                                  "direction": edge_dir, "matched": why})
            row[name] = sorted(found, key=lambda f: (f["id"], f["predicate"]))
    return rows


# ==================================================================== run
def applicable(m, query, subject):
    """Returns None if applicable, otherwise the reason it is not."""
    if query.get("subject") == "required":
        if not subject:
            return "this question requires a subject"
        if subject not in m.by_id:
            return f"no node {subject!r} in this model"
        allowed = query.get("applies-to")
        if allowed and m.by_id[subject]["type"] not in allowed:
            return (f"applies to {', '.join(allowed)}; "
                    f"{subject} is a {m.by_id[subject]['type']}")
    return None


@feature("semantic query execution",
         input_phase="ckm", output_phase="projection",
         invariants=["a query reads the model and never an authoring source (ADR-0081)",
                     "declarations are validated; an unknown field fails (ADR-0088)",
                     "a row carries its complete ordered path, never one predicate",
                     "edge output is what the traversal walked, not an induced subgraph",
                     "applicability is distinguished from emptiness",
                     "traversal is bounded, and truncation emits a diagnostic"],
         determinism="cycles visit once; equal-length paths break lexicographically; "
                     "rows sort by (hops, id)")
def run(model, query, subject=None):
    """Returns the ADR-0088 result contract."""
    result = {"query": query["id"], "question": query["question"], "subject": subject,
              "status": OK, "rows": [], "edges": [], "diagnostics": []}

    reason = applicable(model, query, subject)
    if reason:
        result["status"] = NOT_APPLICABLE
        result["diagnostics"] = [{"phase": "projection", "message": reason,
                                  "rule": query["id"]}]
        return result

    ctx = {"subject": subject, "query": query, "diagnostics": [],
           "max_depth": query.get("max-depth", DEFAULT_MAX_DEPTH)}
    rows = []
    for step in query["steps"]:
        (name, spec), = step.items()
        rows = OPERATORS[name](model, rows, spec or {}, ctx)

    limit = query.get("max-results", DEFAULT_MAX_RESULTS)
    if len(rows) > limit:
        ctx["diagnostics"].append(Diagnostic(
            "projection", None, f"result truncated at max-results {limit} "
                                f"({len(rows)} found)", query["id"]))
        rows = rows[:limit]

    mode = query.get("output", "nodes")
    if mode == "edges":
        seen, walked = set(), []
        for row in rows:
            for hop in row["path"]:
                key = (hop["from"], hop["predicate"], hop["to"])
                if key not in seen:
                    seen.add(key)
                    walked.append(hop)
        result["edges"] = walked
    elif mode == "induced-subgraph":
        ids = {r["id"] for r in rows} | ({subject} if subject else set())
        result["edges"] = [e for e in model.ckm["edges"]
                           if e["from"] in ids and e["to"] in ids]

    result["rows"] = rows
    result["diagnostics"] = [d.as_dict() for d in ctx["diagnostics"]]
    if not rows and not result["edges"]:
        result["status"] = EMPTY
    return result
