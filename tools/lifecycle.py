#!/usr/bin/env python3
"""Run the complete Brownfield Acquisition lifecycle.

    python3 tools/lifecycle.py <before-repo> <after-repo> <project>

    Initial Acquisition → review → Authoritative Model → CKM
        → [engineering change]
        → Continuous Acquisition → Periodic Reacquisition → Knowledge Drift

**Every stage produces proposals. Nothing is authoritative without curation**
(`ADR-0110`, `ADR-0112`).

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from discovery.mechanical import extract           # noqa: E402
from discovery.interpretive import interpret       # noqa: E402
from discovery.candidate import Candidate          # noqa: E402
from discovery.continuous import acquire, delta    # noqa: E402
from discovery import drift                        # noqa: E402
from compiler.apply import authorize, apply        # noqa: E402

BAR = "─" * 72


def initial(repo, project, accept_filter):
    mech = extract(repo)
    cand = Candidate(repo, project)
    interpret(mech, cand, "both-levels")
    model = cand.serialize()
    model["mechanicalModelDigest"] = mech["digest"]
    (project / "candidate-initial.json").write_text(json.dumps(model, indent=2) + "\n")

    ids = {e["id"] for e in model["proposals"]["entities"] if accept_filter(e["id"])}
    auth, rejected, diags = authorize(model, accept_ids=ids,
                                      accept_support={"S-inferred", "S-specified"},
                                      reviewer="Project Owner (gpasquero)")
    apply(auth, project)
    return mech, model, auth


def main(argv):
    if len(argv) != 4:
        print(__doc__)
        return 2
    before_repo, after_repo, project = argv[1], argv[2], ROOT / argv[3]
    (project / "model").mkdir(parents=True, exist_ok=True)

    def keep(node_id):
        return any(k in node_id for k in
                   ("Auth", "Jwt", "RefreshToken", "Lockout", "Password", "Sla",
                    "BusinessHours", "TenantIsolation", "Rls", "Ticket")) \
            or node_id in ("ADR.0001", "BoundedContext.Backend")

    print(BAR); print("1  INITIAL ACQUISITION"); print(BAR)
    mech_before, cand_initial, auth = initial(before_repo, project, keep)
    print(f"   mechanical digest   {mech_before['digest']}")
    print(f"   proposed            {cand_initial['statistics']['entities']} entities")
    print(f"   authorized          {len(auth['entities'])} entities, "
          f"{len(auth['relationships'])} relationships")
    print(f"   authoritative model {len(list((project / 'model').glob('*.md')))} sources\n")

    print(BAR); print("2  ENGINEERING CHANGE  (real, from git history)"); print(BAR)
    mech_after = extract(after_repo)
    d = delta(mech_before, mech_after)
    changed = {k: v for k, v in d["summary"].items() if any(v.values())}
    print(f"   {mech_before['digest']} → {mech_after['digest']}")
    for k, v in changed.items():
        print(f"   {k:<10} +{v['added']} -{v['removed']} ~{v['changed']}")
    for kind in ("suites", "tables", "modules"):
        for added in d[kind]["added"]:
            print(f"     added: {added}")
    print()

    print(BAR); print("3  CONTINUOUS ACQUISITION"); print(BAR)
    auth_ids = {e["id"] for e in auth["entities"]}
    inc_model, inc_report = acquire(mech_before, mech_after, auth_ids)
    (project / "candidate-continuous.json").write_text(json.dumps(inc_model, indent=2) + "\n")
    print(f"   proposed incrementally  {inc_report['proposed']} entities")
    print(f"   retractions (governed)  {len(inc_report['retractions'])}")
    inc_ids = {e["id"] for e in inc_model["proposals"]["entities"]}
    for i in sorted(inc_ids)[:6]:
        print(f"     {i}")
    inc_auth, _, _ = authorize(inc_model, accept_ids=inc_ids,
                               accept_support={"S-inferred", "S-specified"},
                               reviewer="Project Owner (gpasquero)")
    apply(inc_auth, project)
    print(f"   authorized and applied  {len(inc_auth['entities'])} entities")
    print(f"   maintained model        "
          f"{len(list((project / 'model').glob('*.md')))} sources\n")

    print(BAR); print("4  PERIODIC REACQUISITION"); print(BAR)
    fresh_cand = Candidate(after_repo, str(project))
    interpret(mech_after, fresh_cand, "both-levels")
    fresh = fresh_cand.serialize()
    fresh["mechanicalModelDigest"] = mech_after["digest"]
    (project / "candidate-reacquisition.json").write_text(json.dumps(fresh, indent=2) + "\n")
    print(f"   full discovery again    {fresh['statistics']['entities']} entities")
    print(f"   NOT applied — reacquisition challenges, it does not replace\n")

    print(BAR); print("5  KNOWLEDGE DRIFT REPORT"); print(BAR)
    maintained = json.loads(
        (project / "build/canonical-knowledge-model.json").read_text()) \
        if (project / "build/canonical-knowledge-model.json").exists() else None
    if not maintained:
        print("   compile the project first: python3 tools/compile.py " + argv[3])
        return 1
    rep = drift.report(maintained["nodes"], maintained["edges"], fresh,
                       incremental_ids=inc_ids)
    (project / "knowledge-drift-report.json").write_text(json.dumps(rep, indent=2) + "\n")
    print(f"   maintained model        {rep['authoritativeNodes']} nodes")
    print(f"   fresh candidate         {rep['candidateProposals']} proposals")
    for cat, count in rep["statistics"].items():
        if count:
            print(f"   {cat:<38} {count}")
    print(f"\n   Every item is a proposal requiring review (ADR-0112).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
