"""Execute the discovery workers and serialize a Candidate Engineering Model.

    python3 discovery/run.py <repository> <bootstrap-project>

The Director declares HOW discovery is directed (ADR-0105). This performs it.
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from discovery.candidate import Candidate                       # noqa: E402
from discovery.workers import extractors as X                   # noqa: E402
from discovery.workers import interpreters as I                 # noqa: E402


def discover(repo, bootstrap):
    cand = Candidate(str(repo), bootstrap)

    # ── extract: deterministic, reproducible ──────────────────────────────
    pkgs = X.repository_structure(repo, cand, "T01-extract")
    fw = X.stack(repo, cand, "T01-extract")
    mods = X.modules(repo, cand, "T01-extract")
    eps = X.apis(repo, cand, "T01-extract")
    tables = X.persistence(repo, cand, "T01-extract")
    suites = X.tests(repo, cand, "T01-extract")
    envs = X.configuration(repo, cand, "T01-extract")
    integ = X.integrations(repo, cand, "T01-extract")
    decs = X.decisions(repo, cand, "T01-extract")

    # ── interpret: bounded rules over what was extracted ──────────────────
    inv = I.invariants_from_tests(suites, cand, "T02-interpret")
    scoped = I.tenancy_from_schema(tables, decs, cand, "T02-interpret")
    amb = I.ambiguities(decs, cand, "T02-interpret")

    # ── identify gaps: propose no knowledge ───────────────────────────────
    I.gaps(cand, "T03-identify-gaps", modules=mods, suites=suites,
           tables=tables, decisions=decs)

    return cand, {
        "packages": len(pkgs), "frameworks": len(fw), "modules": len(mods),
        "endpoints": len(eps), "tables": len(tables), "suites": len(suites),
        "env-vars": len(envs), "integrations": len(integ), "decisions": len(decs),
        "invariants-inferred": inv, "tenant-scoped-tables": scoped,
        "ambiguities": amb,
    }


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    repo = pathlib.Path(argv[1]).expanduser().resolve()
    bootstrap = argv[2]
    cand, extracted = discover(repo, bootstrap)
    model = cand.serialize()

    out = ROOT / bootstrap / "candidate-engineering-model.json"
    out.write_text(json.dumps(model, indent=2) + "\n")

    s = model["statistics"]
    print(f"[discovery]  {repo}")
    for k, v in extracted.items():
        print(f"    {k:<22} {v}")
    print(f"[candidate]  {s['entities']} entities · {s['relationships']} relationships")
    print(f"             {s['ambiguities']} ambiguities · {s['conflicts']} conflicts "
          f"· {s['gaps']} gaps")
    print(f"[support]    {s['bySupport']}")
    print(f"[digest]     {model['digest']}")
    print(f"[written]    {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
