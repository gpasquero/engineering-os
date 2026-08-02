"""Bounded interpreters and gap identifiers.

An interpreter applies a **named rule** to already-extracted assertions. It reads
no new source: everything it produces is derived from what an extractor reported,
and is classified `S-inferred` — **the rule may be sound and the instance
wrong.**

> **Every proposal names the rule that produced it.** An inference whose rule is
> unnamed is indistinguishable from a guess (`ADR-0107`).

**No language model participates.** `ADR-0105` permits probabilistic
interpreters; none is built here, so the first candidate model is reproducible.
"""
import re

INTERPRETER = "W-constraint-interpreter"
ARCHAEOLOGIST = "W-decision-archaeologist"
GAPS = "W-gap-identifier"


def _slug(text):
    return re.sub(r"[^A-Za-z0-9]", "", text.title())


# ------------------------------------------------------- invariant proposals
#
# Rule R1: a test case whose name states a rule proposes an invariant.
# Bounded by a vocabulary of rule-stating verbs; a name that merely describes
# a scenario is NOT an invariant, and the rule declines rather than guesses.
RULE_VERBS = ("rejects", "must", "never", "always", "cannot", "locks",
              "prevents", "requires", "returns the same", "does not")


def invariants_from_tests(suites, cand, task):
    """R1 — a rule-stating test case proposes an invariant it asserts."""
    proposed = 0
    for source, suite_id, cases, module in suites:
        for case in cases:
            flat = " ".join(case.split())
            if not any(v in flat.lower() for v in RULE_VERBS):
                continue
            iid = f"Invariant.{_slug(flat[:44])}"
            if cand.entity(iid, "Invariant", flat,
                           support="S-inferred", source=source,
                           locator=f"it('{flat[:70]}')",
                           worker=INTERPRETER, task=task,
                           attributes={"rule": "R1-test-name-states-a-rule",
                                       "asserted-by": suite_id}) is None:
                continue
            cand.relation(iid, "enforced-at", suite_id, support="S-tested",
                          source=source, worker=INTERPRETER, task=task,
                          rule="R1-test-name-states-a-rule")
            cand.relation(iid, "constrains", f"Capability.{_slug(module)}",
                          support="S-inferred", source=source,
                          worker=INTERPRETER, task=task,
                          rule="R1-test-name-states-a-rule")
            proposed += 1
    return proposed


# Rule R2: a table carrying a tenant column is tenant-scoped, and a tenancy
# decision that exists constrains it.
def tenancy_from_schema(tables, decisions, cand, task):
    """R2 — a tenant-scoped table is constrained by the tenancy decision."""
    tenancy = [a for a, _, _ in decisions if "0001" in a]
    if not tenancy:
        return 0
    scoped = [t for t, is_scoped in tables if is_scoped]
    for name, _ in [(t, s) for t, s in tables if s]:
        cand.relation(f"Concept.Table{_slug(name)}", "governed-by", tenancy[0],
                      support="S-inferred",
                      source="packages/backend/src/common/database/schema",
                      worker=INTERPRETER, task=task,
                      rule="R2-tenant-column-implies-tenancy-decision")
    return len(scoped)


# ------------------------------------------------------------- ambiguities
def ambiguities(decisions, cand, task):
    """A decision whose status is not Accepted is ambiguous in force."""
    n = 0
    for aid, status, source in decisions:
        if status and status.lower() not in ("accepted", "active"):
            cand.ambiguity(
                aid,
                [f"status is '{status}': the decision is not in force",
                 "the codebase implements it, so it is in force in practice"],
                source=source, worker=ARCHAEOLOGIST, task=task)
            n += 1
    return n


# -------------------------------------------------------------- gap finding
def gaps(cand, task, *, modules, suites, tables, decisions):
    """Report what the candidate model does NOT contain. Proposes no knowledge."""
    tested = {m for _, _, _, m in suites}
    for module in modules:
        if module not in tested:
            cand.gap(f"Capability.{_slug(module)}",
                     "no test suite in the modelled scope validates this module",
                     worker=GAPS, task=task,
                     source=f"packages/backend/src/modules/{module}")
    decided = {a for a, _, _ in decisions}
    if not decided:
        cand.gap("decisions", "no ADR was found", worker=GAPS, task=task)
    for name, is_scoped in tables:
        if not is_scoped:
            cand.gap(f"Concept.Table{_slug(name)}",
                     "table has no tenant column; whether that is correct is unrecorded",
                     worker=GAPS, task=task,
                     source="packages/backend/src/common/database/schema")
    cand.gap("workflows",
             "no engineering workflow was discovered; no worker extracts them",
             worker=GAPS, task=task)
    cand.gap("runtime behaviour",
             "nothing was observed at runtime; discovery read files only",
             worker=GAPS, task=task)
