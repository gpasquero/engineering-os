#!/usr/bin/env python3
"""Ask the Canonical Knowledge Model an engineering question.

**Implements no question.** Every question is a declared semantic query
(`model/queries.md`) executed by the engine in `compiler/query/` — the semantic
API of Engineering OS (ADR-0086).

    python3 tools/ask.py <project> questions
    python3 tools/ask.py <project> Q-impact Concept.Order
    python3 tools/ask.py <project> Q-impact Concept.Order --paths
    python3 tools/ask.py <project> Q-impact Concept.Order --json

`--json` on every question, because an agent is a first-class consumer and not
an eventual one (ADR-0080).

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from _cli import help_requested, project as project_arg  # noqa: E402

from compiler.query import Model, run, load_queries  # noqa: E402


STATUS_NOTE = {
    "ok": "",
    "empty": "no results — which is often the finding",
    "not-applicable": "this question does not apply to that subject",
    "invalid": "the query or subject is malformed",
}


def render(result, paths=False):
    lines = [result["question"]]
    if result["subject"]:
        lines.append(f"  subject: {result['subject']}")
    lines.append("")

    if result["status"] == "not-applicable":
        for d in result["diagnostics"]:
            lines.append(f"  NOT APPLICABLE — {d['message']}")
        lines += ["", f"  status: {result['status']} · {result['query']}"]
        return "\n".join(lines)

    for row in result["rows"]:
        head = f"  {row['id']}"
        if row.get("type"):
            head += f"  ({row['type']})"
        if row.get("hops"):
            head += f"  {row['hops']} hop(s)"
        lines.append(head)
        if paths and row.get("path"):
            for hop in row["path"]:
                arrow = "<-" if hop["direction"] == "in" else "->"
                lines.append(f"      {hop['from']} {arrow}{hop['predicate']}{arrow} "
                             f"{hop['to']}   [{', '.join(hop['matched'])}]")
        for key, value in row.items():
            if key in ("id", "type", "label", "hops", "origin", "via", "path"):
                continue
            if isinstance(value, list) and value:
                rendered = ", ".join(f"{v['id']} via {v['predicate']}"
                                     if isinstance(v, dict) else str(v) for v in value)
                lines.append(f"      {key}: {rendered}")

    for edge in result["edges"]:
        lines.append(f"  {edge['from']} --{edge['predicate']}--> {edge['to']}"
                     f"   [{edge.get('direction', '')}]")

    for d in result["diagnostics"]:
        lines.append(f"  ! {d['message']}")
    if result["status"] == "empty":
        lines.append(f"  ({STATUS_NOTE['empty']})")

    lines += ["", f"  status: {result['status']} · {len(result['rows'])} row(s), "
                  f"{len(result['edges'])} edge(s) · {result['query']}"]
    return "\n".join(lines)


def main(argv):
    if help_requested(argv):
        print(__doc__)
        return 0
    as_json, paths = "--json" in argv, "--paths" in argv
    argv = [a for a in argv if a not in ("--json", "--paths")]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = project_arg(argv[1])
    ckm_path = project / "build/canonical-knowledge-model.json"
    if not ckm_path.exists():
        print(f"no compiled model at {ckm_path}\nrun: python3 tools/compile.py {argv[1]}")
        return 1

    model = Model(json.loads(ckm_path.read_text()))
    queries = load_queries()
    name = argv[2]

    if name == "questions":
        width = max(len(q) for q in queries)
        for qid, q in queries.items():
            applies = q.get("applies-to")
            note = ("   (no subject)" if q.get("subject") != "required"
                    else f"   [{', '.join(applies)}]" if applies else "")
            print(f"  {qid:<{width}}  {q['question']}{note}")
        return 0

    if name not in queries:
        print(f"unknown query {name!r}. Try: questions")
        return 2

    query = queries[name]
    subject = argv[3] if len(argv) > 3 else None
    result = run(model, query, subject)
    print(json.dumps(result, indent=2) if as_json else render(result, paths))
    return 0 if result["status"] in ("ok", "empty") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
