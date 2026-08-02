"""Mechanical Discovery — a reproducible Mechanical Engineering Model.

**Facts, not engineering vocabulary** (`ADR-0108`). This stage records what a
repository *contains*: files, packages, dependencies, module directories, route
decorators, table declarations, test suites and their cases, environment
references, documents and their headers.

**It names nothing as a Concept, Capability or Invariant.** That is
interpretation, and it belongs to the second stage.

Every fact carries its file and locator. Re-running reproduces the model exactly,
which is what makes it a fair fixed input for comparing interpreters.
"""
import re
import json
import hashlib
import pathlib

ORIGIN = "O-mechanical-extraction"

ROUTE = re.compile(r"@(Get|Post|Put|Patch|Delete)\(\s*['\"]?([^'\")]*)")
CONTROLLER = re.compile(r"@Controller\(\s*['\"]([^'\"]*)")
PGTABLE = re.compile(r"pgTable\(\s*['\"]([^'\"]+)")
ENVVAR = re.compile(r"process\.env\.([A-Z][A-Z0-9_]+)")
DESCRIBE = re.compile(r"describe\(\s*['\"](.+?)['\"]", re.S)
IT = re.compile(r"\bit\(\s*['\"](.+?)['\"]", re.S)
HEADING = re.compile(r"^#\s*(.+)$", re.M)
TABLEROW = re.compile(r"\|\s*([A-Za-z ]+?)\s*\|\s*([^|]+?)\s*\|")


def _rel(root, p):
    return str(pathlib.Path(p).relative_to(root))


def _flat(s):
    return " ".join(s.split())


def extract(root):
    """Returns the Mechanical Engineering Model. Reads files; interprets nothing."""
    root = pathlib.Path(root)
    m = {"packages": [], "dependencies": [], "moduleDirs": [], "routes": [],
         "tables": [], "testSuites": [], "envRefs": [], "documents": [],
         "fileCounts": {}}

    files = [p for p in root.rglob("*") if p.is_file()
             and "node_modules" not in p.parts and ".git" not in p.parts]
    counts = {}
    for f in files:
        if f.suffix:
            counts[f.suffix] = counts.get(f.suffix, 0) + 1
    m["fileCounts"] = dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:12])
    m["fileTotal"] = len(files)

    for manifest in sorted(root.glob("packages/*/package.json")):
        pkg = manifest.parent.name
        data = json.loads(manifest.read_text())
        m["packages"].append({"name": pkg, "path": f"packages/{pkg}",
                              "source": _rel(root, manifest)})
        for dep in sorted((data.get("dependencies") or {}).keys()):
            m["dependencies"].append({"package": pkg, "name": dep,
                                      "source": _rel(root, manifest),
                                      "locator": "dependencies"})

    base = root / "packages/backend/src/modules"
    if base.exists():
        for d in sorted(x for x in base.iterdir() if x.is_dir()):
            m["moduleDirs"].append({"name": d.name, "path": _rel(root, d),
                                    "files": len(list(d.rglob("*.ts")))})

    for f in sorted(root.glob("packages/backend/src/**/*.controller.ts")):
        text = f.read_text(errors="ignore")
        base_route = CONTROLLER.search(text)
        for verb, path in ROUTE.findall(text):
            m["routes"].append({"verb": verb.upper(), "path": path,
                                "prefix": base_route.group(1) if base_route else "",
                                "moduleDir": f.parent.name,
                                "source": _rel(root, f)})

    schema = root / "packages/backend/src/common/database/schema"
    if schema.exists():
        for f in sorted(schema.glob("*.ts")):
            if f.name == "index.ts":
                continue
            text = f.read_text(errors="ignore")
            # Columns belong to the table whose declaration they follow. Attributing
            # every column in a FILE to every table declared in it produced two
            # tables with byte-identical column sets — a defect found by a blind
            # discovery worker reading only this extractor's output.
            decls = [(m_.start(), m_.group(1)) for m_ in PGTABLE.finditer(text)]
            for i, (start, name) in enumerate(decls):
                end = decls[i + 1][0] if i + 1 < len(decls) else len(text)
                body = text[start:end]
                m["tables"].append({
                    "name": name, "source": _rel(root, f),
                    "columns": sorted(set(
                        re.findall(r"^\s*([a-zA-Z][A-Za-z0-9]*)\s*:", body, re.M)))[:40]})

    for f in sorted(root.glob("packages/backend/src/**/*.spec.ts")):
        text = f.read_text(errors="ignore")
        cases = [_flat(c) for c in IT.findall(text)]
        if not cases:
            continue
        m["testSuites"].append({
            "file": _rel(root, f),
            "name": f.stem,
            "moduleDir": (f.parent.parent.name if f.parent.name == "__tests__"
                          else f.parent.name),
            "describes": [_flat(d) for d in DESCRIBE.findall(text)],
            "cases": cases,
        })

    seen = {}
    for f in sorted(root.glob("packages/*/src/**/*.ts")):
        for var in ENVVAR.findall(f.read_text(errors="ignore")):
            seen.setdefault(var, _rel(root, f))
    m["envRefs"] = [{"name": v, "source": s} for v, s in sorted(seen.items())]

    for f in sorted(root.glob("docs/**/*.md")):
        text = f.read_text(errors="ignore")
        heading = HEADING.search(text)
        fields = {k.strip().lower(): v.strip()
                  for k, v in TABLEROW.findall(text[:1500])
                  if k.strip().lower() in ("status", "date", "decision")}
        m["documents"].append({
            "file": _rel(root, f),
            "heading": _flat(heading.group(1)) if heading else None,
            "fields": fields,
            "kind": "adr" if "/adr/" in _rel(root, f) else "doc",
        })

    m["statistics"] = {k: len(v) for k, v in m.items() if isinstance(v, list)}
    m["repository"] = str(root)
    m["vocabularyVersion"] = "1.1.0"   # a versioned contract (ADR-0110)
    m["origin"] = ORIGIN
    m["note"] = ("Mechanical Engineering Model. Facts about what the repository "
                 "contains. Nothing here is named as engineering knowledge — that "
                 "is Interpretive Discovery (ADR-0108).")
    m["digest"] = hashlib.sha256(
        json.dumps(m, sort_keys=True).encode()).hexdigest()[:16]
    return m
