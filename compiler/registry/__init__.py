"""Registries — one mechanism instead of three ad-hoc readers (ADR-0032, ADR-0083).

The compiler does not know the shape of any particular registry file. It knows
three EXTRACTION kinds, and reads `model/metamodel/registries.md` to learn which
registries exist, where they live and how each is extracted.

Adding a registry is a data change. Adding an extraction kind is a compiler
change and should be rare.
"""
import re
import pathlib

import yaml

from ..runtime.phases import feature

METAMODEL = pathlib.Path(__file__).resolve().parents[2] / "model/metamodel"
DECLARATION = METAMODEL / "registries.md"

EXTRACTORS = {}


def extractor(name):
    def wrap(fn):
        EXTRACTORS[name] = fn
        return fn
    return wrap


@extractor("front-matter")
def _front_matter(spec, base):
    """One entry per file, keyed by a front-matter field."""
    out = {}
    for path in sorted(base.glob(spec["source"])):
        text = path.read_text()
        key = re.search(rf"^{spec['key']}:\s*(\S+)", text, re.M)
        if not key:
            continue
        entry = {}
        for field in spec.get("fields", []):
            found = re.search(rf"^{field}:\s*(\S+)", text, re.M)
            entry[field] = found.group(1) if found else None
        out[key.group(1)] = entry
    return out


@extractor("markdown-table")
def _markdown_table(spec, base):
    """Entries from one or more pipe tables, keyed by the first column."""
    text = (base / spec["source"]).read_text()
    if "section" in spec:
        blocks = [(None, re.search(rf"^## {re.escape(spec['section'])}\n(.*?)(?=^## )",
                                   text, re.M | re.S).group(1))]
    else:
        # A capturing group in the section pattern labels every row it contains,
        # so a value that is a property of the SECTION is not lost.
        blocks = [(m.group(1) if m.lastindex else None, m.group(m.lastindex or 0 + 1))
                  for m in re.finditer(
                      spec["section-pattern"] + r".*?\n(.*?)(?=^###|^## )", text, re.M | re.S)]
        blocks = [(m.group(1) if m.re.groups > 1 else None, m.group(m.re.groups))
                  for m in re.finditer(
                      spec["section-pattern"] + r".*?\n(.*?)(?=^###|^## )", text, re.M | re.S)]

    columns = spec["columns"]
    cells = r"^\|\s*`([^`]+)`\s*\|" + r"".join(
        [r"\s*`?([^|`]+?)`?\s*\|"] * (len(columns) - 1))
    label_as = spec.get("section-label")
    out = {}
    for label, block in blocks:
        for row in re.findall(cells, block, re.M):
            entry = dict(zip(columns[1:], (c.strip() for c in row[1:])))
            if label_as and label:
                entry[label_as] = label.lower()
            out[row[0]] = entry
    return out


@extractor("yaml-file")
def _yaml_file(spec, base):
    """Entries from a whole YAML file, keyed by `id`."""
    data = yaml.safe_load((base / spec["source"]).read_text())
    return {item["id"]: item for item in data[spec["collection"]]}


@extractor("yaml-block")
def _yaml_block(spec, base):
    """Entries from a fenced YAML block, keyed by `id`."""
    text = (base / spec["source"]).read_text()
    block = re.search(r"```yaml\n(.*?)```", text, re.S)
    if not block:
        raise SystemExit(f"{spec['source']}: no yaml block")
    items = yaml.safe_load(block.group(1))[spec["collection"]]
    return {item["id"]: item for item in items}


@feature("registry loading",
         input_phase="authoring", output_phase="discovery",
         invariants=["the compiler knows extraction kinds, never registry shapes",
                     "every declared registry names an implemented extraction kind",
                     "a registry is read exactly once per compilation"],
         determinism="registries are keyed and sorted; extraction is a pure function of the source")
def load_all(base=METAMODEL):
    """Returns {registry-id: {entry-key: entry}}."""
    block = re.search(r"```yaml\n(.*?)```", DECLARATION.read_text(), re.S)
    if not block:
        raise SystemExit(f"{DECLARATION}: no registries block")
    declared = yaml.safe_load(block.group(1))["registries"]

    unknown = [r["id"] for r in declared if r["extraction"] not in EXTRACTORS]
    if unknown:
        raise SystemExit(f"registries naming unimplemented extraction kinds: {unknown}")

    return {spec["id"]: EXTRACTORS[spec["extraction"]](spec, base)
            for spec in sorted(declared, key=lambda r: r["id"])}
