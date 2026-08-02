#!/usr/bin/env python3
"""Derive a deterministic Task Graph from an Engineering Plan.

    python3 tools/taskgraph.py <project> P-change-implementation Artifact.ConflictGo
    python3 tools/taskgraph.py <project> P-change-concept Concept.ManagedFields --json
    python3 tools/taskgraph.py <project> P-change-implementation Artifact.ConflictGo --mermaid

**No language model participates** (`ADR-0092`). A task declares the capabilities
it requires, never which worker performs it (`ADR-0097`).

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.query import Model               # noqa: E402
from compiler.plan import plan, load_plans     # noqa: E402
from compiler.taskgraph import derive          # noqa: E402

BAR = "─" * 72
MARK = {"mechanical": "auto", "reasoning": "LLM ", "human": "HUMAN"}


def render(g):
    L = [BAR, f"TASK GRAPH   {g['taskGraph']}", BAR, "", "OBJECTIVE",
         f"  {g['objective']}", ""]
    if g["status"] == "not-applicable":
        L += [f"  NOT APPLICABLE — {g['diagnostics'][0]['message']}", ""]
        return "\n".join(L)

    by_id = {t["id"]: t for t in g["tasks"]}
    L.append(f"EXECUTION   {g['execution']['mechanical']} mechanical · "
             f"{g['execution']['reasoning']} reasoning · {g['execution']['human']} human"
             f"   ·   max parallelism {g['parallelism']}")
    L.append("")
    for i, level in enumerate(g["levels"], 1):
        parallel = "  (parallel)" if len(level) > 1 else ""
        L.append(f"  LEVEL {i}{parallel}")
        for tid in level:
            t = by_id[tid]
            cls = "/".join(MARK[c] for c in t["execution"])
            L.append(f"    [{cls:^5}]  {t['id']}")
            L.append(f"              {t['objective']}")
            if t["dependsOn"]:
                L.append(f"              depends on: {', '.join(t['dependsOn'])}")
            for c in t["completion"]:
                L.append(f"              done when:  {c}")
            L.append(f"              evidence:   {t['evidence']}")
            L.append(f"              needs:      {', '.join(t['capabilities'])}")
            src = t["derivedFrom"]
            trace = (f"{src['taskKind']} (terminal)" if src.get("terminal")
                     else f"{src['taskKind']} ← {src['query']} · {src['recommendation']}")
            L.append(f"              from:       {trace}")
            for r in t["requiresReviewAt"]:
                L.append(f"              review:     {r}")
            L.append("")
    for d in g["diagnostics"]:
        L.append(f"  ! {d['message']}")
    j = g.get("judgment") or {}
    if j:
        L += [f"JUDGMENT   {len(j.get('derived', []))} derived · "
              f"{len(j.get('deferred', []))} deferred", ""]
        for d in j.get("deferred", []):
            L.append(f"  deferred: {d}")
        L.append("")
    L += [BAR, "Every task was derived from a plan action and a declared task kind.",
          "No language model participated. No task names a worker.", BAR]
    return "\n".join(L)


def mermaid(g):
    L = ["```mermaid", "graph TD"]
    for t in g["tasks"]:
        cls = t["execution"][0]
        L.append(f'  {t["id"].replace("-", "_")}["{t["id"]}<br/><i>{cls}</i>"]')
    for t in g["tasks"]:
        for dep in t["dependsOn"]:
            L.append(f'  {dep.replace("-", "_")} --> {t["id"].replace("-", "_")}')
    for cls in ("mechanical", "reasoning", "human"):
        ids = [t["id"].replace("-", "_") for t in g["tasks"] if t["execution"][0] == cls]
        if ids:
            L.append(f"  class {','.join(ids)} {cls};")
    L += ["  classDef mechanical fill:#e6f4ea,stroke:#0f9d58;",
          "  classDef reasoning fill:#e8f0fe,stroke:#4285f4;",
          "  classDef human fill:#fce8e6,stroke:#ea4335;", "```"]
    return "\n".join(L)


def main(argv):
    modes = {a for a in argv if a.startswith("--")}
    argv = [a for a in argv if not a.startswith("--")]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = ROOT / argv[1]
    ckm_path = project / "build/canonical-knowledge-model.json"
    if not ckm_path.exists():
        print(f"no compiled model at {ckm_path}\nrun: python3 tools/compile.py {argv[1]}")
        return 1

    model = Model(json.loads(ckm_path.read_text()))
    plans = load_plans()
    if argv[2] not in plans:
        print(f"unknown plan {argv[2]!r}")
        return 2

    result = plan(model, plans[argv[2]], argv[3] if len(argv) > 3 else None)
    graph = derive(result)
    print(json.dumps(graph, indent=2) if "--json" in modes
          else mermaid(graph) if "--mermaid" in modes else render(graph))
    return 0 if graph["status"] in ("ok", "empty") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
