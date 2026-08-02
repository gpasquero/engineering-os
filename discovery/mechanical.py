"""Mechanical Discovery — a reproducible Mechanical Engineering Model.

**Facts, not engineering vocabulary** (`ADR-0108`). This stage records what a
repository *contains*: packages, dependencies, module directories, routes, table
declarations, test suites and their cases, configuration references, documents.

**It names nothing as a Concept, Capability or Invariant.** That is
interpretation, and it belongs to the second stage.

**Where those facts live is declared, not coded** (`ADR-0117`). This module holds
seven extraction kinds; `discovery/stacks.yaml` holds the Stack Profiles that say
where each stack keeps them. Adding a stack costs a declaration.

Every fact carries its file and locator. Re-running reproduces the model exactly,
which is what makes it a fair fixed input for comparing interpreters.
"""
import re
import json
import hashlib
import pathlib

import yaml

ORIGIN = "O-mechanical-extraction"
VOCABULARY = "2.0.0"      # 1.x was produced by a hard-coded layout (ADR-0110)

HEADING = re.compile(r"^#\s*(.+)$", re.M)
TABLEROW = re.compile(r"\|\s*([A-Za-z ]+?)\s*\|\s*([^|]+?)\s*\|")
SKIP_DIRS = {"node_modules", ".git", "target", "build", "dist", ".gradle", ".claude",
             "venv", ".venv", "site-packages", "__pycache__", ".mypy_cache"}

VOCABULARY_KEYS = ("packages", "dependencies", "moduleDirs", "routes", "tables",
                   "testSuites", "envRefs", "documents")


def load_profiles(path=None):
    path = pathlib.Path(path or pathlib.Path(__file__).parent / "stacks.yaml")
    return {p["id"]: p for p in yaml.safe_load(path.read_text())["profiles"]}


def detect(root, profiles=None):
    """Which profile does this repository match? Returns an id or None.

    Detection is a fact about the repository, so it is recorded in the model
    rather than passed in by whoever ran the tool.
    """
    root = pathlib.Path(root)
    for pid, prof in sorted((profiles or load_profiles()).items()):
        if any((root / marker).exists() for marker in prof.get("detect") or []):
            return pid
    return None


def _rel(root, p):
    return str(pathlib.Path(p).relative_to(root))


def _flat(s):
    return " ".join(s.split())


def _walk(root, pattern, exclude=()):
    """Glob, minus vendor and build directories. Braces expand; rglob does not."""
    patterns = [pattern]
    brace = re.search(r"\{([^}]*)\}", pattern)
    if brace:
        patterns = [pattern[:brace.start()] + alt + pattern[brace.end():]
                    for alt in brace.group(1).split(",")]
    seen = []
    for pat in patterns:
        for p in root.glob(pat):
            if set(p.parts) & (SKIP_DIRS | set(exclude)):
                continue
            if p.name in (exclude or ()):
                continue
            seen.append(p)
    return sorted(set(seen))


def _read(p):
    return p.read_text(errors="ignore")


# ─────────────────────────────────────────────────────── the seven kinds

def k_manifest_json(root, spec, m):
    for manifest in _walk(root, spec["glob"]):
        name = manifest.parent.name
        data = json.loads(_read(manifest))
        m["packages"].append({"name": name, "path": _rel(root, manifest.parent),
                              "source": _rel(root, manifest)})
        for dep in sorted((data.get(spec["dependencies"]) or {}).keys()):
            m["dependencies"].append({"package": name, "name": dep,
                                      "source": _rel(root, manifest),
                                      "locator": spec["dependencies"]})


def k_manifest_xml(root, spec, m):
    name_re, dep_re = re.compile(spec["name"]), re.compile(spec["dependencies"], re.S)
    for manifest in _walk(root, spec["glob"]):
        text = _read(manifest)
        # A Maven module inherits from a parent, and the parent's coordinates
        # appear FIRST. Reading the first artifactId named every repository
        # after its framework's BOM — the first repository tried reported one
        # package called `spring-boot-starter-parent`.
        body = re.sub(r"<parent>.*?</parent>", "", text, flags=re.S)
        found = name_re.search(body)
        name = found.group(1) if found else manifest.parent.name
        m["packages"].append({"name": name, "path": _rel(root, manifest.parent),
                              "source": _rel(root, manifest)})
        block = re.search(r"<dependencies>(.*?)</dependencies>", body, re.S)
        for dep in sorted(set(dep_re.findall(block.group(1) if block else ""))):
            m["dependencies"].append({"package": name, "name": dep,
                                      "source": _rel(root, manifest),
                                      "locator": "dependencies"})


def k_dirs_under(root, spec, m):
    if spec.get("root"):
        roots = [root / spec["root"]]
    elif spec.get("root-marker"):
        # The root is wherever a marker file sits. In Spring the base package is
        # the directory holding the application class — a mechanical fact, and a
        # more honest locator than guessing at directory NAMES, which was the
        # first attempt and found nothing in the first repository tried.
        roots = sorted({f.parent for f in _walk(root, spec["root-marker"])})
    else:
        roots = _walk(root, spec["root-glob"])
    for base in roots:
        if not base.is_dir():
            continue
        for d in sorted(x for x in base.iterdir() if x.is_dir()):
            m["moduleDirs"].append({
                "name": d.name, "path": _rel(root, d),
                "files": len([f for f in d.rglob(f"*{spec['count-suffix']}")
                              if not set(f.parts) & SKIP_DIRS])})


def k_routes(root, spec, m):
    prefix_re = re.compile(spec["prefix"])
    verb_re = re.compile(spec["verb-path"])
    for f in _walk(root, spec["glob"]):
        text = _read(f)
        if spec.get("require") and spec["require"] not in text:
            continue
        base = prefix_re.search(text)
        for verb, path in verb_re.findall(text):
            m["routes"].append({"verb": verb.upper(), "path": path,
                                "prefix": base.group(1) if base else "",
                                "moduleDir": f.parent.name,
                                "source": _rel(root, f)})


def k_declaration_blocks(root, spec, m):
    """Members belong to the declaration they FOLLOW.

    Attributing every member in a file to every declaration in it produced two
    tables with byte-identical column sets — a defect found by a blind discovery
    worker reading only this extractor's output (SESSION-0042).
    """
    decl_re = re.compile(spec["declaration"])
    fallback = spec.get("declaration-fallback")
    fallback_re = re.compile(fallback) if fallback else None
    member_re = re.compile(spec["member"], re.M)
    for f in _walk(root, spec["glob"], exclude=spec.get("exclude") or ()):
        text = _read(f)
        if spec.get("require") and spec["require"] not in text:
            continue
        decls = [(x.start(), x.group(1)) for x in decl_re.finditer(text)]
        if not decls and fallback_re:
            decls = [(x.start(), x.group(1)) for x in fallback_re.finditer(text)][:1]
        for i, (start, name) in enumerate(decls):
            end = decls[i + 1][0] if i + 1 < len(decls) else len(text)
            m["tables"].append({
                "name": name, "source": _rel(root, f),
                "columns": sorted(set(member_re.findall(text[start:end])))[:40]})


def _module_of(f, how):
    if how == "parent-dir-skipping-tests":
        return f.parent.parent.name if f.parent.name == "__tests__" else f.parent.name
    return f.parent.name


def k_test_suites(root, spec, m):
    describe_re = re.compile(spec["describe"], re.S)
    d_fallback = spec.get("describe-fallback")
    d_fallback_re = re.compile(d_fallback) if d_fallback else None
    case_re = re.compile(spec["case"], re.S)
    c_fallback = spec.get("case-fallback")
    c_fallback_re = re.compile(c_fallback) if c_fallback else None
    for f in _walk(root, spec["glob"]):
        text = _read(f)
        if spec.get("require") and spec["require"] not in text:
            continue
        cases = [_flat(c) for c in case_re.findall(text)]
        if not cases and c_fallback_re:
            cases = [_flat(c) for c in c_fallback_re.findall(text)]
        if not cases:
            continue
        describes = [_flat(d) for d in describe_re.findall(text)]
        if not describes and d_fallback_re:
            describes = [_flat(d) for d in d_fallback_re.findall(text)]
        m["testSuites"].append({
            "file": _rel(root, f), "name": f.stem,
            "moduleDir": _module_of(f, spec.get("module-from")),
            "describes": describes, "cases": cases})


def k_regex_set(root, spec, m):
    pattern, seen = re.compile(spec["pattern"]), {}
    for f in _walk(root, spec["glob"]):
        for var in pattern.findall(_read(f)):
            seen.setdefault(var, _rel(root, f))
    m["envRefs"] = [{"name": v, "source": s} for v, s in sorted(seen.items())]


def k_documents(root, spec, m):
    for f in _walk(root, spec["glob"], exclude=spec.get("exclude-dirs") or ()):
        text = _read(f)
        heading = HEADING.search(text)
        fields = {k.strip().lower(): v.strip()
                  for k, v in TABLEROW.findall(text[:1500])
                  if k.strip().lower() in ("status", "date", "decision")}
        m["documents"].append({
            "file": _rel(root, f),
            "heading": _flat(heading.group(1)) if heading else None,
            "fields": fields,
            "kind": "adr" if "/adr/" in _rel(root, f).lower() else "doc"})


KINDS = {"manifest-json": k_manifest_json, "manifest-xml": k_manifest_xml,
         "dirs-under": k_dirs_under, "routes": k_routes,
         "declaration-blocks": k_declaration_blocks, "test-suites": k_test_suites,
         "regex-set": k_regex_set, "documents": k_documents}


def extract(root, profile=None):
    """Returns the Mechanical Engineering Model. Reads files; interprets nothing."""
    root = pathlib.Path(root)
    profiles = load_profiles()
    pid = profile or detect(root, profiles)
    if pid is None:
        raise SystemExit(
            f"no Stack Profile matches {root}.\n"
            "  Mechanical Acquisition refuses rather than returning an empty\n"
            "  model: an empty model and an unrecognised stack are opposite\n"
            "  findings, and only one of them is about the repository.")
    prof = profiles[pid]

    m = {k: [] for k in VOCABULARY_KEYS}
    m["fileCounts"] = {}

    files = [p for p in root.rglob("*") if p.is_file() and not set(p.parts) & SKIP_DIRS]
    counts = {}
    for f in files:
        if f.suffix:
            counts[f.suffix] = counts.get(f.suffix, 0) + 1
    m["fileCounts"] = dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:12])
    m["fileTotal"] = len(files)

    for key in VOCABULARY_KEYS:
        spec = prof.get(key)
        if not spec:
            continue
        KINDS[spec["kind"]](root, spec, m)

    m["statistics"] = {k: len(v) for k, v in m.items() if isinstance(v, list)}
    m["repository"] = str(root)
    m["stackProfile"] = pid
    m["vocabularyVersion"] = VOCABULARY
    m["origin"] = ORIGIN
    m["note"] = ("Mechanical Engineering Model. Facts about what the repository "
                 "contains. Nothing here is named as engineering knowledge — that "
                 "is Interpretive Discovery (ADR-0108). Where the facts live is "
                 "declared by a Stack Profile (ADR-0117).")
    m["digest"] = hashlib.sha256(
        json.dumps(m, sort_keys=True).encode()).hexdigest()[:16]
    return m
