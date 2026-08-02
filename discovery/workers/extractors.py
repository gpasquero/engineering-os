"""Deterministic discovery extractors.

Each reads files and reports what they say. **Re-running reproduces the result
exactly**, which is why their output is classified `S-confirmed-deterministic`,
`S-implemented`, `S-tested` or `S-specified` — never `S-inferred`.

Written for the ai-desk stack: a TypeScript monorepo with a NestJS backend, Next
frontend and Drizzle schema. **No universal language support** (`ADR-0107`).
"""
import re
import json
import pathlib

WORKER = "W-structure-extractor"


def _rel(root, path):
    return str(pathlib.Path(path).relative_to(root))


def _slug(text):
    return re.sub(r"[^A-Za-z0-9]", "", text.title())


# ---------------------------------------------------------------- structure
def repository_structure(root, cand, task):
    """Packages, file counts, languages."""
    pkgs = sorted(p.name for p in (root / "packages").iterdir()
                  if p.is_dir()) if (root / "packages").exists() else []
    files = [p for p in root.rglob("*") if p.is_file()
             and "node_modules" not in p.parts and ".git" not in p.parts]
    langs = {}
    for f in files:
        if f.suffix:
            langs[f.suffix] = langs.get(f.suffix, 0) + 1

    for pkg in pkgs:
        cand.entity(f"BoundedContext.{_slug(pkg)}", "BoundedContext",
                    f"{pkg} package",
                    support="S-confirmed-deterministic",
                    source=f"packages/{pkg}", locator="workspace package",
                    worker=WORKER, task=task,
                    attributes={"package": pkg})
    cand.entity("Evidence.RepositoryLayout", "Evidence", "Repository layout",
                support="S-confirmed-deterministic", source=".",
                locator=f"{len(files)} files, {len(pkgs)} packages",
                worker=WORKER, task=task,
                attributes={"kind": "source-reference",
                            "packages": ",".join(pkgs),
                            "top-languages": ",".join(
                                f"{k}:{v}" for k, v in
                                sorted(langs.items(), key=lambda x: -x[1])[:5])})
    return pkgs


# -------------------------------------------------------------------- stack
def stack(root, cand, task):
    """Frameworks and dependencies, from package manifests."""
    found = []
    for manifest in sorted(root.glob("packages/*/package.json")):
        pkg = manifest.parent.name
        data = json.loads(manifest.read_text())
        deps = sorted((data.get("dependencies") or {}).keys())
        frameworks = [d for d in deps if any(
            d.startswith(f) for f in ("@nestjs/", "next", "react", "drizzle",
                                      "socket.io", "passport"))]
        for fw in frameworks:
            fid = f"Concept.{_slug(fw)}"
            cand.entity(fid, "Concept", fw,
                        support="S-confirmed-deterministic",
                        source=_rel(root, manifest), locator="dependencies",
                        worker=WORKER, task=task,
                        attributes={"framework": fw, "package": pkg})
            cand.relation(fid, "scoped-to", f"BoundedContext.{_slug(pkg)}",
                          support="S-confirmed-deterministic",
                          source=_rel(root, manifest), worker=WORKER, task=task)
            found.append((pkg, fw))
    return found


# ------------------------------------------------------------------ modules
def modules(root, cand, task):
    """NestJS modules are the architectural boundaries the code itself declares."""
    base = root / "packages/backend/src/modules"
    if not base.exists():
        return []
    names = sorted(d.name for d in base.iterdir() if d.is_dir())
    for name in names:
        mid = f"Capability.{_slug(name)}"
        cand.entity(mid, "Capability", f"{name} module",
                    support="S-implemented",
                    source=f"packages/backend/src/modules/{name}",
                    locator="NestJS module directory",
                    worker=WORKER, task=task, attributes={"module": name})
        cand.relation(mid, "scoped-to", "BoundedContext.Backend",
                      support="S-confirmed-deterministic",
                      source=f"packages/backend/src/modules/{name}",
                      worker=WORKER, task=task)
    return names


# --------------------------------------------------------------------- APIs
ROUTE = re.compile(r"@(Get|Post|Put|Patch|Delete)\(\s*['\"]?([^'\")]*)")
CONTROLLER = re.compile(r"@Controller\(\s*['\"]([^'\"]*)")


def apis(root, cand, task):
    """Public API surface, from NestJS decorators."""
    endpoints = []
    for f in sorted(root.glob("packages/backend/src/**/*.controller.ts")):
        text = f.read_text(errors="ignore")
        base = CONTROLLER.search(text)
        prefix = base.group(1) if base else ""
        verbs = ROUTE.findall(text)
        if not verbs:
            continue
        module = f.parent.name
        aid = f"Artifact.{_slug(f.stem)}"
        cand.entity(aid, "Artifact", f.name,
                    support="S-implemented", source=_rel(root, f),
                    locator=f"@Controller('{prefix}'), {len(verbs)} routes",
                    worker=WORKER, task=task,
                    attributes={"routes": str(len(verbs)), "prefix": prefix})
        cand.relation(aid, "implements", f"Capability.{_slug(module)}",
                      support="S-implemented", source=_rel(root, f),
                      worker=WORKER, task=task)
        endpoints += [(prefix, v, p) for v, p in verbs]
    return endpoints


# -------------------------------------------------------------- persistence
def persistence(root, cand, task):
    """Tables, from Drizzle schema declarations."""
    base = root / "packages/backend/src/common/database/schema"
    tables = []
    if not base.exists():
        return tables
    for f in sorted(base.glob("*.ts")):
        if f.name == "index.ts":
            continue
        text = f.read_text(errors="ignore")
        for name in re.findall(r"pgTable\(\s*['\"]([^'\"]+)", text):
            cid = f"Concept.Table{_slug(name)}"
            cand.entity(cid, "Concept", f"{name} table",
                        support="S-implemented", source=_rel(root, f),
                        locator=f"pgTable('{name}')",
                        worker=WORKER, task=task,
                        attributes={"table": name,
                                    "tenant-scoped": str("tenantId" in text).lower()})
            tables.append((name, "tenantId" in text))
    return tables


# -------------------------------------------------------------------- tests
IT = re.compile(r"\bit\(\s*['\"](.+?)['\"]", re.S)


def tests(root, cand, task):
    """Test suites and what each case asserts."""
    suites = []
    for f in sorted(root.glob("packages/backend/src/**/*.spec.ts")):
        cases = IT.findall(f.read_text(errors="ignore"))
        if not cases:
            continue
        sid = f"Artifact.{_slug(f.stem)}"
        cand.entity(sid, "Artifact", f.name,
                    support="S-tested", source=_rel(root, f),
                    locator=f"{len(cases)} it() cases",
                    worker=WORKER, task=task,
                    attributes={"cases": str(len(cases))})
        module = f.parent.parent.name if f.parent.name == "__tests__" else f.parent.name
        cand.relation(sid, "validates", f"Capability.{_slug(module)}",
                      support="S-tested", source=_rel(root, f),
                      worker=WORKER, task=task)
        suites.append((_rel(root, f), sid, cases, module))
    return suites


# ------------------------------------------------------------- config & env
ENVVAR = re.compile(r"process\.env\.([A-Z][A-Z0-9_]+)")


def configuration(root, cand, task):
    """Environment dependencies, from process.env references."""
    seen = {}
    for f in sorted(root.glob("packages/*/src/**/*.ts")):
        for var in ENVVAR.findall(f.read_text(errors="ignore")):
            seen.setdefault(var, _rel(root, f))
    for var, where in sorted(seen.items()):
        cand.entity(f"Concept.Env{_slug(var)}", "Concept", f"${var}",
                    support="S-confirmed-deterministic", source=where,
                    locator=f"process.env.{var}", worker=WORKER, task=task,
                    attributes={"env-var": var})
    return sorted(seen)


# ------------------------------------------------------------ integrations
INTEGRATION_HINTS = ("@aws-sdk", "socket.io", "redis", "nodemailer", "stripe",
                     "twilio", "@sendgrid", "openai", "@anthropic")


def integrations(root, cand, task):
    """External integrations, from dependency names."""
    found = []
    for manifest in sorted(root.glob("packages/*/package.json")):
        data = json.loads(manifest.read_text())
        for dep in sorted((data.get("dependencies") or {}).keys()):
            if any(dep.startswith(h) for h in INTEGRATION_HINTS):
                cand.entity(f"Concept.Integration{_slug(dep)}", "Concept", dep,
                            support="S-confirmed-deterministic",
                            source=_rel(root, manifest), locator="dependencies",
                            worker=WORKER, task=task,
                            attributes={"integration": dep})
                found.append(dep)
    return found


# ---------------------------------------------------------------- decisions
def decisions(root, cand, task):
    """Existing ADRs, and their declared status."""
    found = []
    for f in sorted(root.glob("docs/adr/*.md")):
        text = f.read_text(errors="ignore")
        title = re.search(r"^#\s*(.+)$", text, re.M)
        status = re.search(r"\|\s*Status\s*\|\s*([^|]+?)\s*\|", text)
        decision = re.search(r"\|\s*Decision\s*\|\s*([^|]+?)\s*\|", text)
        num = re.search(r"ADR-(\d+)", f.name)
        if not num:
            continue
        aid = f"ADR.{num.group(1)}"
        cand.entity(aid, "ADR", (title.group(1) if title else f.stem).strip(),
                    support="S-specified", source=_rel(root, f), locator="header",
                    worker=WORKER, task=task,
                    attributes={"status": (status.group(1).strip() if status else "unstated"),
                                "decision": (decision.group(1).strip() if decision else "")})
        found.append((aid, status.group(1).strip() if status else None,
                      _rel(root, f)))
    return found
