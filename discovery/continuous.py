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
                              source=path, worker=W, task=task, rule="C1-new-suite")
            for case in rule_cases:
                iid = f"Invariant.{_slug(case, 44)}"
                if cand.entity(iid, "Invariant", case, support="S-inferred",
                               source=path, locator=f"it('{case[:70]}')",
                               worker=W, task=task,
                               attributes={"origin": ORIGIN, "rule": "C1-new-suite",
                                           "granularity": "guarantee"}) is None:
                    continue
                cand.relation(iid, "specializes", gid, support="S-inferred",
                              source=path, worker=W, task=task, rule="C1-new-suite")

    for name in d["tables"]["added"]:
        t = a["tables"][name]
        cand.entity(f"Concept.Table{_slug(name)}", "Concept", f"{name} table",
                    support="S-implemented", source=t["source"],
                    locator=f"pgTable('{name}')", worker="W-domain-interpreter",
                    task=task, attributes={"origin": ORIGIN, "rule": "C2-new-table"})

    for name in d["modules"]["added"]:
        m = a["modules"][name]
        cand.entity(f"Capability.{_slug(name)}", "Capability", f"{name} module",
                    support="S-implemented", source=m["path"],
                    locator="module directory", worker="W-domain-interpreter",
                    task=task, attributes={"origin": ORIGIN, "rule": "C3-new-module"})

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
