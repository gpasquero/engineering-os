"""Continuous Acquisition — maintain the Authoritative Engineering Model
incrementally after an accepted engineering change (`ADR-0112`).

> **Do not rerun the complete onboarding workflow after every change.**

It consumes the change, not the repository: two Mechanical Models — before and
after — plus whatever the engineering process accepted. It proposes only what
changed, in the same proposed-assertion shape everything else uses
(`ADR-0106`), so the same applier and the same curation handle it.

**Nothing it produces is authoritative.** Incremental maintenance is not a
licence to write.
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from discovery.candidate import Candidate          # noqa: E402
from discovery.interpretive import _slug, _states_a_rule  # noqa: E402

ORIGIN = "O-deterministic-rule"


def _index(mech):
    return {
        "suites": {s["file"]: s for s in mech["testSuites"]},
        "tables": {t["name"]: t for t in mech["tables"]},
        "modules": {m["name"]: m for m in mech["moduleDirs"]},
        "routes": {f"{r['verb']} /{r['prefix']}/{r['path']}".replace("//", "/"): r
                   for r in mech["routes"]},
        "deps": {f"{d['package']}:{d['name']}" for d in mech["dependencies"]},
        "docs": {d["file"]: d for d in mech["documents"]},
    }


def delta(before, after):
    """What changed, mechanically. Facts only, no interpretation."""
    b, a = _index(before), _index(after)
    out = {}
    for kind in ("suites", "tables", "modules", "routes", "docs"):
        out[kind] = {"added": sorted(set(a[kind]) - set(b[kind])),
                     "removed": sorted(set(b[kind]) - set(a[kind])),
                     "changed": sorted(k for k in set(a[kind]) & set(b[kind])
                                       if a[kind][k] != b[kind][k])}
    out["deps"] = {"added": sorted(a["deps"] - b["deps"]),
                   "removed": sorted(b["deps"] - a["deps"]), "changed": []}
    out["summary"] = {k: {p: len(v[p]) for p in ("added", "removed", "changed")}
                      for k, v in out.items()}
    return out


def acquire(before, after, authoritative_ids, accepted=None):
    """Propose incremental updates. Returns (candidate, report)."""
    d = delta(before, after)
    a = _index(after)
    cand = Candidate(after.get("repository"), "continuous")
    cand.mechanical_digest = after["digest"]
    task = "T-continuous"
    W = "W-constraint-interpreter"

    # ── Semantic preservation (ADR-0130) ─────────────────────────────────
    #
    # Continuous Acquisition preserves the engineering meaning that Initial
    # Acquisition established. Each relationship below cites the initial rule
    # whose meaning it carries forward, and none of them is INFERRED — every one
    # is read from evidence the mechanical delta already carries.
    #
    # Before SESSION-0049 this function preserved `enforced-at` and
    # `specializes` and dropped `constrains`, `implements`, `validates` and
    # `scoped-to`. All four attach something to a Capability, so a model
    # maintained rather than rebuilt grew nodes and lost the ability to answer
    # `EQ-06` — measured at 0% Understanding Retention across ten commits.

    # New test suites propose invariants at both levels (ADR-0111), exactly as
    # Initial Acquisition does. The rule is the same rule; only the input is
    # narrower.
    for path in d["suites"]["added"]:
        suite = a["suites"][path]
        sid = f"Artifact.{_slug(suite['name'])}"
        cand.entity(sid, "Artifact", f"{suite['name']}.spec.ts", support="S-tested",
                    source=path, locator=f"{len(suite['cases'])} cases",
                    worker="W-domain-interpreter", task=task,
                    attributes={"origin": ORIGIN, "rule": "C1-new-suite",
                                "cases": str(len(suite["cases"]))})
        # preserves S4-spec-validates-module
        cand.relation(sid, "validates", f"Capability.{_slug(suite['moduleDir'])}",
                      support="S-inferred", source=path,
                      worker="W-domain-interpreter", task=task,
                      rule="C1-new-suite", preserves="S4-spec-validates-module")

        # A suite that declares no subject has no general invariant, and its
        # cases are still guarantees — the same degradation R4 makes (ADR-0130).
        if not suite["describes"]:
            for case in [c for c in suite["cases"] if _states_a_rule(c)]:
                iid = f"Invariant.{_slug(case, 44)}"
                if cand.entity(iid, "Invariant", case, support="S-inferred",
                               source=path, locator=f"case('{case[:70]}')",
                               worker=W, task=task,
                               attributes={"origin": ORIGIN, "rule": "C1-new-suite",
                                           "granularity": "guarantee",
                                           "grouping": "none-declared"}) is None:
                    continue
                cand.relation(iid, "enforced-at", sid, support="S-tested",
                              source=path, worker=W, task=task, rule="C1-new-suite",
                              preserves="R4-both-levels")

        for describe in suite["describes"]:
            rule_cases = [c for c in suite["cases"] if _states_a_rule(c)]
            if not rule_cases:
                continue
            gid = f"Invariant.{_slug(describe, 40)}"
            if cand.entity(gid, "Invariant", describe, support="S-inferred",
                           source=path, locator=f"describe('{describe}')",
                           worker=W, task=task,
                           attributes={"origin": ORIGIN, "rule": "C1-new-suite",
                                       "granularity": "concept"}) is not None:
                cand.relation(gid, "enforced-at", sid, support="S-tested",
                              source=path, worker=W, task=task, rule="C1-new-suite",
                              preserves="R4-both-levels")
                # preserves R4-both-levels: an invariant guards a capability
                cand.relation(gid, "constrains",
                              f"Capability.{_slug(suite['moduleDir'])}",
                              support="S-inferred", source=path, worker=W,
                              task=task, rule="C1-new-suite",
                              preserves="R4-both-levels")
            for case in rule_cases:
                iid = f"Invariant.{_slug(case, 44)}"
                if cand.entity(iid, "Invariant", case, support="S-inferred",
                               source=path, locator=f"it('{case[:70]}')",
                               worker=W, task=task,
                               attributes={"origin": ORIGIN, "rule": "C1-new-suite",
                                           "granularity": "guarantee"}) is None:
                    continue
                cand.relation(iid, "specializes", gid, support="S-inferred",
                              source=path, worker=W, task=task, rule="C1-new-suite",
                              preserves="R4-both-levels")
                cand.relation(iid, "enforced-at", sid, support="S-tested",
                              source=path, worker=W, task=task, rule="C1-new-suite",
                              preserves="R4-both-levels")

    for name in d["tables"]["added"]:
        t = a["tables"][name]
        cand.entity(f"Concept.Table{_slug(name)}", "Concept", f"{name} table",
                    support="S-implemented", source=t["source"],
                    locator=f"pgTable('{name}')", worker="W-domain-interpreter",
                    task=task, attributes={"origin": ORIGIN, "rule": "C2-new-table"})

    for name in d["modules"]["added"]:
        m = a["modules"][name]
        mid = f"Capability.{_slug(name)}"
        cand.entity(mid, "Capability", f"{name} module",
                    support="S-implemented", source=m["path"],
                    locator="module directory", worker="W-domain-interpreter",
                    task=task, attributes={"origin": ORIGIN, "rule": "C3-new-module"})
        # preserves S1-module-is-a-capability
        cand.relation(mid, "scoped-to", "BoundedContext.Backend",
                      support="S-inferred", source=m["path"],
                      worker="W-domain-interpreter", task=task,
                      rule="C3-new-module", preserves="S1-module-is-a-capability")

    # C4 — a controller that gained routes realises its capability. There was no
    # route rule at all: a controller added after onboarding never entered the
    # model, so its capability had nothing implementing it.
    by_source = {}
    for key in d["routes"]["added"]:
        r = a["routes"][key]
        by_source.setdefault((r["source"], r["moduleDir"]), []).append(r)
    for (source, module), rs in sorted(by_source.items()):
        aid = f"Artifact.{_slug(source.split('/')[-1].rsplit('.', 1)[0])}"
        cand.entity(aid, "Artifact", source.split("/")[-1], support="S-implemented",
                    source=source, locator=f"{len(rs)} routes",
                    worker="W-domain-interpreter", task=task,
                    attributes={"origin": ORIGIN, "rule": "C4-new-routes",
                                "routes": str(len(rs))})
        # preserves S2-controller-implements-module
        cand.relation(aid, "implements", f"Capability.{_slug(module)}",
                      support="S-inferred", source=source,
                      worker="W-domain-interpreter", task=task,
                      rule="C4-new-routes", preserves="S2-controller-implements-module")

    # Removals are never applied mechanically. An assertion whose evidence
    # disappeared is a GOVERNED proposal (ADR-0101): the evidence may have moved.
    retractions = []
    for kind, key in (("suites", "file"), ("tables", "name"), ("modules", "name")):
        for gone in d[kind]["removed"]:
            retractions.append({"kind": kind, "subject": gone,
                                "proposal": "retract",
                                "intake": "govern",
                                "why": "the evidence supporting it is no longer present"})

    for kind in ("suites", "tables", "modules", "routes", "docs"):
        for path in d[kind]["changed"]:
            cand.gap(f"{kind}:{path}",
                     "evidence changed; assertions resting on it may be stale",
                     worker="W-gap-identifier", task=task, source=path)

    model = cand.serialize()
    model["mechanicalModelDigest"] = after["digest"]
    model["previousMechanicalDigest"] = before["digest"]
    model["mode"] = "continuous"
    report = {"delta": d["summary"], "retractions": retractions,
              "proposed": model["statistics"]["entities"],
              "accepted-inputs": sorted(accepted or []),
              "authoritative-before": len(authoritative_ids)}
    return model, report
