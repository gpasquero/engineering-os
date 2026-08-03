#!/usr/bin/env python3
"""Ask the Canonical Knowledge Model what to do.

Recommendations are declared in `model/recommendations.md` and composed entirely
of semantic queries (`ADR-0091`). This tool implements none of them.

    python3 tools/advise.py <project> recommendations
    python3 tools/advise.py <project> R-change-implementation Artifact.ConflictGo
    python3 tools/advise.py <project> R-audit-model --json

`--json` on every recommendation: an AI agent and a developer consume the same
output, and neither is the privileged consumer.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from _cli import help_requested, project as project_arg  # noqa: E402

from compiler.query import Model                       # noqa: E402
from compiler.recommend import advise, load_recommendations  # noqa: E402


def render(result):
    lines = [result["intent"]]
    if result["subject"]:
        lines.append(f"  subject: {result['subject']}")
    lines.append("")

    if result["status"] == "not-applicable":
        for d in result["diagnostics"]:
            lines.append(f"  NOT APPLICABLE — {d['message']}")
        lines += ["", f"  status: {result['status']} · {result['recommendation']}"]
        return "\n".join(lines)

    for step in result["steps"]:
        head = f"  {step['action'].upper()}"
        if step["status"] == "not-applicable":
            lines.append(f"{head}  — skipped, {step['diagnostics'][0]['message']}")
            lines.append(f"      ({step['query']})")
            continue
        if not step["rows"]:
            lines.append(f"{head}  — nothing")
            lines.append(f"      {step['because']}   ({step['query']})")
            continue
        lines.append(f"{head}  {step['because']}")
        for row in step["rows"]:
            detail = f" via {row['path'][0]['predicate']}" if row.get("path") else ""
            lines.append(f"      {row['id']}  ({row['type']}){detail}")
        lines.append(f"      ({step['query']})")

    lines += ["", f"  status: {result['status']} · "
                  f"{sum(len(s['rows']) for s in result['steps'])} item(s) across "
                  f"{len(result['steps'])} step(s) · {result['recommendation']}"]
    return "\n".join(lines)


def main(argv):
    if help_requested(argv):
        print(__doc__)
        return 0
    as_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = project_arg(argv[1])
    ckm_path = project / "build/canonical-knowledge-model.json"
    if not ckm_path.exists():
        print(f"no compiled model at {ckm_path}\nrun: python3 tools/compile.py {argv[1]}")
        return 1

    model = Model(json.loads(ckm_path.read_text()))
    recommendations = load_recommendations()
    name = argv[2]

    if name == "recommendations":
        width = max(len(r) for r in recommendations)
        for rid, rec in recommendations.items():
            applies = rec.get("applies-to") or []
            note = f"   [{', '.join(applies)}]" if applies else "   (no subject)"
            print(f"  {rid:<{width}}  {rec['intent']}{note}")
        return 0

    if name not in recommendations:
        print(f"unknown recommendation {name!r}. Try: recommendations")
        return 2

    subject = argv[3] if len(argv) > 3 else None
    result = advise(model, recommendations[name], subject)
    print(json.dumps(result, indent=2) if as_json else render(result))
    return 0 if result["status"] in ("ok", "empty") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
