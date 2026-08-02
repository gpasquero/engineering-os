"""Parsing — a source set to structurally valid assertions (ADR-0078).

Front matter is parsed with a real YAML parser and validated against a schema
BEFORE semantic resolution. A structural error is never reported as a semantic
one.
"""
import re
import pathlib

import yaml

from ..runtime.phases import feature
from ..runtime.diagnostics import Diagnostic

SCHEMA_DIR = pathlib.Path(__file__).parent / "schemas"
_FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

_CHECKERS = {
    "string": lambda v: isinstance(v, str),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "list": lambda v: isinstance(v, list),
    "mapping": lambda v: isinstance(v, dict),
}


def load_schema(name):
    return yaml.safe_load((SCHEMA_DIR / f"{name}.yaml").read_text())


def validate_against(schema, data, source):
    """Structural validation only. Says nothing about whether assertions are true."""
    out = []
    for key in schema.get("required", []):
        if data.get(key) in (None, ""):
            out.append(Diagnostic("parsing", source, f"missing required key '{key}'"))
    for key, value in data.items():
        spec = schema.get("properties", {}).get(key)
        if spec is None:
            out.append(Diagnostic("parsing", source, f"unknown key '{key}'"))
            continue
        if value is None:
            continue
        if not _CHECKERS[spec["type"]](value):
            out.append(Diagnostic("parsing", source,
                                  f"key '{key}' must be {spec['type']}, got "
                                  f"{type(value).__name__}"))
            continue
        if spec.get("pattern") and not re.match(spec["pattern"], value):
            out.append(Diagnostic("parsing", source,
                                  f"key '{key}' value {value!r} does not match "
                                  f"{spec['pattern']}"))
        if spec.get("items") and isinstance(value, list):
            for i, item in enumerate(value):
                if not _CHECKERS[spec["items"]](item):
                    out.append(Diagnostic("parsing", source,
                                          f"'{key}[{i}]' must be {spec['items']}, got "
                                          f"{type(item).__name__}"))
    return out


@feature("front-matter parsing",
         input_phase="discovery", output_phase="parsing",
         invariants=["front matter is parsed as YAML, never by pattern matching",
                     "every source is validated against its schema before Resolution",
                     "a structural error is reported at Parsing, never at Resolution",
                     "attribute values are scalar and carried verbatim",
                     "parsing never consults another source"],
         determinism="parsing is a pure function of one file's bytes and one schema")
def parse(paths):
    schema = load_schema("node")
    nodes, diagnostics = [], []

    for path in paths:
        source = path.name
        m = _FRONT_MATTER.match(path.read_text())
        if not m:
            diagnostics.append(Diagnostic("parsing", source, "no front matter"))
            continue
        try:
            data = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as exc:
            first = str(exc).splitlines()[0]
            diagnostics.append(Diagnostic("parsing", source, f"invalid YAML: {first}"))
            continue
        if not isinstance(data, dict):
            diagnostics.append(Diagnostic("parsing", source, "front matter is not a mapping"))
            continue

        problems = validate_against(schema, data, source)
        diagnostics.extend(problems)
        if problems:
            continue

        rels = []
        for i, item in enumerate(data.get("relationships") or []):
            if len(item) != 1:
                diagnostics.append(Diagnostic(
                    "parsing", source,
                    f"'relationships[{i}]' must have exactly one predicate, has {len(item)}"))
                continue
            (predicate, target), = item.items()
            rels.append((str(predicate), str(target)))

        attributes = data.get("attributes") or {}
        bad_attr = [k for k, v in attributes.items()
                    if not isinstance(v, (str, int, float, bool))]
        if bad_attr:
            diagnostics.append(Diagnostic(
                "parsing", source,
                f"attributes must be scalar; {sorted(bad_attr)} are not"))
            continue

        nodes.append({"id": data["id"], "type": data["type"],
                      "label": data.get("label") or data["id"],
                      "position": data.get("position"),
                      "attributes": {k: str(v) for k, v in sorted(attributes.items())},
                      "relationships": rels,
                      "body": m.group(2).strip(),
                      "source": source})
    return nodes, diagnostics
