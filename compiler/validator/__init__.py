"""Validation — the compiler executes rules, it does not contain them (ADR-0077).

Rule KINDS are mechanisms and live here. RULES are instances of a kind bound to
model elements, and live in model/metamodel/validation-rules.md.
"""
import collections

from ..runtime.phases import feature
from ..runtime.diagnostics import Diagnostic
from ..registry import load_all

KINDS = {}


def kind(name):
    def wrap(fn):
        KINDS[name] = fn
        return fn
    return wrap


def load_rules():
    """Rules are authored data, not code. They arrive through a registry."""
    rules = sorted(load_all()["REG-validation-rules"].values(), key=lambda r: r["id"])
    unknown = [r["id"] for r in rules if r["kind"] not in KINDS]
    if unknown:
        raise SystemExit(f"rules naming unimplemented kinds: {unknown}")
    return rules


# ------------------------------------------------------------------- kinds
@kind("declared-entity-type")
def _declared_entity_type(rule, nodes, ctx):
    for n in nodes:
        if n["type"] not in ctx["entities"]:
            yield Diagnostic("resolution", n["source"],
                             rule["message"].format(value=n["type"]), rule["id"])


@kind("registered-predicate")
def _registered_predicate(rule, nodes, ctx):
    for n in nodes:
        for predicate, _ in n["relationships"]:
            if predicate not in ctx["predicates"]:
                yield Diagnostic("resolution", n["source"],
                                 rule["message"].format(value=predicate), rule["id"])


@kind("resolvable-target")
def _resolvable_target(rule, nodes, ctx):
    for n in nodes:
        for predicate, target in n["relationships"]:
            if target not in ctx["ids"]:
                yield Diagnostic("resolution", n["source"],
                                 rule["message"].format(predicate=predicate, value=target),
                                 rule["id"])


@kind("unique-identity")
def _unique_identity(rule, nodes, ctx):
    for node_id, count in sorted(collections.Counter(n["id"] for n in nodes).items()):
        if count > 1:
            yield Diagnostic("resolution", None,
                             rule["message"].format(value=node_id, count=count), rule["id"])


@kind("forbidden-self-reference")
def _forbidden_self_reference(rule, nodes, ctx):
    watched = set(rule.get("applies-to-predicates", []))
    for n in nodes:
        for predicate, target in n["relationships"]:
            if predicate in watched and target == n["id"]:
                yield Diagnostic("resolution", n["source"],
                                 rule["message"].format(predicate=predicate, subject=n["id"]),
                                 rule["id"])


@kind("required-relationship")
def _required_relationship(rule, nodes, ctx):
    for n in nodes:
        if n["type"] != rule["applies-to-type"]:
            continue
        if not any(p == rule["requires-predicate"] for p, _ in n["relationships"]):
            yield Diagnostic("resolution", n["source"], rule["message"], rule["id"])


@feature("declarative rule execution",
         input_phase="parsing", output_phase="resolution",
         invariants=["every rule names an implemented kind, or compilation aborts",
                     "no check is authored in Python; kinds are mechanisms, rules are data",
                     "a rule reports the rule id that produced it"],
         determinism="rules run in id order and diagnostics are sorted")
def validate(nodes, ctx, rules=None):
    rules = rules if rules is not None else load_rules()
    out = []
    for rule in rules:
        out.extend(KINDS[rule["kind"]](rule, nodes, ctx))
    return out
