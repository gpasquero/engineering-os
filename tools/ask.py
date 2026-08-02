#!/usr/bin/env python3
"""Ask the Canonical Knowledge Model an engineering question.

**Implements no question.** Every question is a declared semantic query
(`model/queries.md`) executed by the engine in `compiler/query/` — the semantic
API of Engineering OS (ADR-0086).

    python3 tools/ask.py <project> questions
    python3 tools/ask.py <project> Q-impact Concept.Order
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

from compiler.query import Model, run, load_queries  # noqa: E402


def render(query, subject, rows):
    lines = [query["question"]]
    if subject:
        lines.append(f"  subject: {subject}")
    lines.append("")
    if not rows:
        lines.append("  (no results)")
    for row in rows:
        parts = []
        for key, value in row.items():
            if value in (None, [], ""):
                continue
            if key == "label":
                continue
            parts.append(f"{key}={value}" if not isinstance(value, list)
                         else f"{key}={','.join(value)}")
        lines.append("  " + "  ".join(parts))
    lines += ["", f"  {len(rows)} row(s) · {query['id']}"]
    return "\n".join(lines)


def main(argv):
    as_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = ROOT / argv[1]
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
            need = "" if q.get("subject") == "required" else "   (no subject)"
            print(f"  {qid:<{width}}  {q['question']}{need}")
        return 0

    if name not in queries:
        print(f"unknown query {name!r}. Try: questions")
        return 2

    query = queries[name]
    subject = argv[3] if len(argv) > 3 else None
    if query.get("subject") == "required" and not subject:
        print(f"{name} requires a subject node id")
        return 2
    if subject and subject not in model.by_id:
        print(f"unknown node {subject!r}")
        return 1

    rows = run(model, query, subject)
    if as_json:
        print(json.dumps({"query": query["id"], "question": query["question"],
                          "subject": subject, "rows": rows}, indent=2))
    else:
        print(render(query, subject, rows))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
