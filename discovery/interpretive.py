"""Interpretive Discovery — proposes engineering knowledge.

> **Its only input is the Mechanical Engineering Model** (`ADR-0108`). It never
> opens a source file. That constraint is what makes extraction quality and
> interpretation quality separately measurable, and what makes two interpreters
> comparable over identical input.

Rules are **named**, and every proposal records the rule that produced it and its
origin kind (`ADR-0109`).

Two rule sets are provided so that interpretation strategies can be compared over
the same mechanical facts:

  * **case-level** — one invariant per rule-stating test case
  * **suite-level** — one invariant per `describe` block, with its cases as
    evidence

Neither is probabilistic. `ADR-0103` permits a probabilistic interpreter; none is
built, so both are exactly reproducible.
"""
import re

ORIGIN = "O-deterministic-rule"

RULE_VERBS = ("rejects", "must", "never", "always", "cannot", "locks",
              "prevents", "requires", "returns the same", "does not", "fails",
              "isolation", "enforce")


def _slug(text, limit=48):
    return re.sub(r"[^A-Za-z0-9]", "", text.title())[:limit]


def _states_a_rule(text):
    return any(v in text.lower() for v in RULE_VERBS)


# ============================================================== structural
def structure(mech, cand, task):
    """S1 — a workspace package is a bounded context; a module directory a capability."""
    W = "W-domain-interpreter"
    for pkg in mech["packages"]:
        cand.entity(f"BoundedContext.{_slug(pkg['name'])}", "BoundedContext",
                    f"{pkg['name']} package", support="S-confirmed-deterministic",
                    source=pkg["source"], locator="workspace package",
                    worker=W, task=task,
                    attributes={"origin": ORIGIN, "rule": "S1-package-is-a-context"})
    for mod in mech["moduleDirs"]:
        mid = f"Capability.{_slug(mod['name'])}"
        cand.entity(mid, "Capability", f"{mod['name']} module",
                    support="S-implemented", source=mod["path"],
                    locator="module directory", worker=W, task=task,
                    attributes={"origin": ORIGIN, "rule": "S1-module-is-a-capability",
                                "ts-files": str(mod["files"])})
        cand.relation(mid, "scoped-to", "BoundedContext.Backend",
                      support="S-inferred", source=mod["path"], worker=W, task=task,
                      rule="S1-module-is-a-capability")
    for t in mech["tables"]:
        cand.entity(f"Concept.Table{_slug(t['name'])}", "Concept", f"{t['name']} table",
                    support="S-implemented", source=t["source"],
                    locator=f"pgTable('{t['name']}')", worker=W, task=task,
                    attributes={"origin": ORIGIN, "rule": "S1-pgtable-is-a-concept",
                                "tenant-scoped": str("tenantId" in t["columns"]).lower()})


def routes(mech, cand, task):
    """S2 — a controller file with routes is an artifact implementing its module."""
    W = "W-domain-interpreter"
    by_source = {}
    for r in mech["routes"]:
        by_source.setdefault((r["source"], r["moduleDir"]), []).append(r)
    for (source, module), rs in sorted(by_source.items()):
        aid = f"Artifact.{_slug(source.split('/')[-1].replace('.ts', ''))}"
        cand.entity(aid, "Artifact", source.split("/")[-1], support="S-implemented",
                    source=source, locator=f"{len(rs)} routes", worker=W, task=task,
                    attributes={"origin": ORIGIN, "rule": "S2-controller-implements-module",
                                "routes": str(len(rs))})
        cand.relation(aid, "implements", f"Capability.{_slug(module)}",
                      support="S-inferred", source=source, worker=W, task=task,
                      rule="S2-controller-implements-module")


def decisions(mech, cand, task):
    """S3 — a document under docs/adr is a decision; its status may be ambiguous."""
    W = "W-decision-archaeologist"
    for doc in mech["documents"]:
        if doc["kind"] != "adr":
            continue
        num = re.search(r"ADR-(\d+)", doc["file"])
        if not num:
            continue
        aid = f"ADR.{num.group(1)}"
        status = doc["fields"].get("status")
        cand.entity(aid, "ADR", doc["heading"] or doc["file"], support="S-specified",
                    source=doc["file"], locator="header", worker=W, task=task,
                    attributes={"origin": ORIGIN, "rule": "S3-adr-directory-is-a-decision",
                                "status": status or "unstated"})
        if status and status.lower() not in ("accepted", "active"):
            cand.ambiguity(aid,
                           [f"status is '{status}': the decision is not in force",
                            "the repository implements it, so it is in force in practice"],
                           source=doc["file"], worker=W, task=task)


# ================================================ invariants: two strategies
def invariants_case_level(mech, cand, task):
    """R1 — one invariant per rule-stating test CASE.

    The rule SESSION-0039 used. High volume, low abstraction: eight lockout
    cases become eight invariants.
    """
    W = "W-constraint-interpreter"
    n = 0
    for suite in mech["testSuites"]:
        sid = f"Artifact.{_slug(suite['name'])}"
        for case in suite["cases"]:
            if not _states_a_rule(case):
                continue
            iid = f"Invariant.{_slug(case, 44)}"
            if cand.entity(iid, "Invariant", case, support="S-inferred",
                           source=suite["file"], locator=f"it('{case[:70]}')",
                           worker=W, task=task,
                           attributes={"origin": ORIGIN,
                                       "rule": "R1-case-states-a-rule"}) is None:
                continue
            cand.relation(iid, "enforced-at", sid, support="S-tested",
                          source=suite["file"], worker=W, task=task,
                          rule="R1-case-states-a-rule")
            n += 1
    return n


def invariants_suite_level(mech, cand, task):
    """R3 — one invariant per DESCRIBE block, with its cases as evidence.

    The abstraction a human produces is already in the file: a suite declaring
    `describe('account lockout & brute-force protection')` names the concept its
    cases assert. Lower volume, higher abstraction, same input.
    """
    W = "W-constraint-interpreter"
    n = 0
    for suite in mech["testSuites"]:
        sid = f"Artifact.{_slug(suite['name'])}"
        # The outermost describe names the subject; fall back to the file stem.
        subject = suite["describes"][0] if suite["describes"] else suite["name"]
        rule_cases = [c for c in suite["cases"] if _states_a_rule(c)]
        if not rule_cases:
            continue
        iid = f"Invariant.{_slug(subject, 40)}"
        if cand.entity(iid, "Invariant", subject, support="S-inferred",
                       source=suite["file"], locator=f"describe('{subject}')",
                       worker=W, task=task,
                       attributes={"origin": ORIGIN,
                                   "rule": "R3-describe-names-the-invariant",
                                   "asserted-by-cases": str(len(rule_cases))}) is None:
            continue
        cand.relation(iid, "enforced-at", sid, support="S-tested",
                      source=suite["file"], worker=W, task=task,
                      rule="R3-describe-names-the-invariant")
        cand.relation(iid, "constrains", f"Capability.{_slug(suite['moduleDir'])}",
                      support="S-inferred", source=suite["file"], worker=W, task=task,
                      rule="R3-describe-names-the-invariant")
        n += 1
    return n


def test_suites(mech, cand, task):
    """S4 — a test suite is an artifact validating its module."""
    W = "W-domain-interpreter"
    for suite in mech["testSuites"]:
        sid = f"Artifact.{_slug(suite['name'])}"
        cand.entity(sid, "Artifact", f"{suite['name']}.spec.ts", support="S-tested",
                    source=suite["file"], locator=f"{len(suite['cases'])} cases",
                    worker=W, task=task,
                    attributes={"origin": ORIGIN, "rule": "S4-spec-validates-module",
                                "cases": str(len(suite["cases"])),
                                "describes": " | ".join(suite["describes"][:3])})
        cand.relation(sid, "validates", f"Capability.{_slug(suite['moduleDir'])}",
                      support="S-inferred", source=suite["file"], worker=W, task=task,
                      rule="S4-spec-validates-module")


def gaps(mech, cand, task):
    """Reports absence. Proposes no knowledge."""
    W = "W-gap-identifier"
    tested = {s["moduleDir"] for s in mech["testSuites"]}
    for mod in mech["moduleDirs"]:
        if mod["name"] not in tested:
            cand.gap(f"Capability.{_slug(mod['name'])}",
                     "no test suite in the mechanical model validates this module",
                     worker=W, task=task, source=mod["path"])
    for t in mech["tables"]:
        if "tenantId" not in t["columns"]:
            cand.gap(f"Concept.Table{_slug(t['name'])}",
                     "table has no tenant column; whether that is correct is unrecorded",
                     worker=W, task=task, source=t["source"])
    for label, why in [
        ("workflows", "no rule proposes workflows from the mechanical model"),
        ("runtime behaviour", "the mechanical model contains no runtime observation"),
        ("prose invariants", "no rule reads document prose; a guarantee stated only "
                             "in a document is invisible to interpretation"),
    ]:
        cand.gap(label, why, worker=W, task=task)


def invariants_both_levels(mech, cand, task):
    """R4 — both levels, related by `specializes` (`ADR-0111`).

    `R3` reaches the concept and loses the specific guarantee; `R1` keeps the
    guarantee and never states the concept. Neither dominates, and the resolution
    is not to choose.

    The `describe` block becomes the general Invariant; each rule-stating case
    becomes a specific Invariant that `specializes` it. **No new entity** — a
    specific guarantee is a narrower Invariant, and `specializes` is a registered
    core relationship type.
    """
    W = "W-constraint-interpreter"
    general = specific = 0
    for suite in mech["testSuites"]:
        sid = f"Artifact.{_slug(suite['name'])}"
        subject = suite["describes"][0] if suite["describes"] else suite["name"]
        rule_cases = [c for c in suite["cases"] if _states_a_rule(c)]
        if not rule_cases:
            continue

        gid = f"Invariant.{_slug(subject, 40)}"
        if cand.entity(gid, "Invariant", subject, support="S-inferred",
                       source=suite["file"], locator=f"describe('{subject}')",
                       worker=W, task=task,
                       attributes={"origin": ORIGIN,
                                   "rule": "R4-both-levels",
                                   "granularity": "concept",
                                   "established-by-cases": str(len(rule_cases))}) is not None:
            cand.relation(gid, "enforced-at", sid, support="S-tested",
                          source=suite["file"], worker=W, task=task,
                          rule="R4-both-levels")
            cand.relation(gid, "constrains", f"Capability.{_slug(suite['moduleDir'])}",
                          support="S-inferred", source=suite["file"], worker=W,
                          task=task, rule="R4-both-levels")
            general += 1

        for case in rule_cases:
            iid = f"Invariant.{_slug(case, 44)}"
            if cand.entity(iid, "Invariant", case, support="S-inferred",
                           source=suite["file"], locator=f"it('{case[:70]}')",
                           worker=W, task=task,
                           attributes={"origin": ORIGIN,
                                       "rule": "R4-both-levels",
                                       "granularity": "guarantee"}) is None:
                continue
            # A specific guarantee is a NARROWER invariant, not a different kind.
            cand.relation(iid, "specializes", gid, support="S-inferred",
                          source=suite["file"], worker=W, task=task,
                          rule="R4-both-levels")
            cand.relation(iid, "enforced-at", sid, support="S-tested",
                          source=suite["file"], worker=W, task=task,
                          rule="R4-both-levels")
            specific += 1
    return {"concepts": general, "guarantees": specific}


STRATEGIES = {
    "case-level": invariants_case_level,
    "suite-level": invariants_suite_level,
    "both-levels": invariants_both_levels,
}


def interpret(mech, cand, strategy="suite-level"):
    """Run interpretation over the Mechanical Model with a named strategy."""
    structure(mech, cand, "T02-interpret")
    routes(mech, cand, "T02-interpret")
    test_suites(mech, cand, "T02-interpret")
    decisions(mech, cand, "T02-interpret")
    n = STRATEGIES[strategy](mech, cand, "T02-interpret")
    gaps(mech, cand, "T03-identify-gaps")
    return n
