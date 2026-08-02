"""Run Discovery: Mechanical extraction, then Interpretation over its output.

    python3 discovery/run.py <repository> <project> [--strategy=suite-level|case-level]

Two stages (`ADR-0108`). Mechanical Discovery reads source and produces a
reproducible Mechanical Engineering Model. Interpretive Discovery reads **only
that model** and proposes engineering knowledge.
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from discovery.candidate import Candidate        # noqa: E402
from discovery.mechanical import extract         # noqa: E402
from discovery.interpretive import interpret, STRATEGIES  # noqa: E402


def main(argv):
    opts = {a.split("=", 1)[0]: a.split("=", 1)[1]
            for a in argv if a.startswith("--") and "=" in a}
    argv = [a for a in argv if not a.startswith("--")]
    if len(argv) != 3:
        print(__doc__)
        return 2
    repo, project = pathlib.Path(argv[1]).expanduser().resolve(), argv[2]
    strategy = opts.get("--strategy", "suite-level")
    if strategy not in STRATEGIES:
        print(f"unknown strategy {strategy!r}; try {sorted(STRATEGIES)}")
        return 2

    # ── stage 1: mechanical ───────────────────────────────────────────────
    mech = extract(repo)
    mech_path = ROOT / project / "mechanical-engineering-model.json"
    mech_path.write_text(json.dumps(mech, indent=2) + "\n")
    print(f"[mechanical]  {repo}")
    for k, v in mech["statistics"].items():
        print(f"    {k:<16} {v}")
    print(f"    digest           {mech['digest']}")

    # ── stage 2: interpretive — reads ONLY the mechanical model ───────────
    cand = Candidate(str(repo), project)
    cand.mechanical_digest = mech["digest"]
    invariants = interpret(mech, cand, strategy)
    model = cand.serialize()
    model["mechanicalModelDigest"] = mech["digest"]
    model["interpretationStrategy"] = strategy

    out = ROOT / project / "candidate-engineering-model.json"
    out.write_text(json.dumps(model, indent=2) + "\n")

    s = model["statistics"]
    print(f"[interpretive] strategy '{strategy}', reading only the mechanical model")
    print(f"    invariants       {invariants}")
    print(f"[candidate]   {s['entities']} entities · {s['relationships']} relationships")
    print(f"              {s['ambiguities']} ambiguities · {s['gaps']} gaps")
    print(f"[origin]      {s.get('byOrigin', {})}")
    print(f"[written]     {mech_path.relative_to(ROOT)}")
    print(f"              {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
