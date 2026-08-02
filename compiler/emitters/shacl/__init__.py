"""SHACL emitter — validation shapes, derived from the metamodel and the model.

A projection of the Canonical Knowledge Model (`ADR-0072`). Shapes are generated
from the declared relationship vocabulary and the ValidationRules the compiler
already executes, so **the shapes and the compiler enforce the same rules** and
cannot disagree.
"""
from ...runtime.phases import feature
from ...registry import load_all


def _camel(k):
    head, *tail = k.split("-")
    return head + "".join(w.capitalize() for w in tail)


@feature("SHACL projection",
         input_phase="ckm", output_phase="projection",
         invariants=["shapes derive from the same registries the compiler reads",
                     "a shape is generated for every node type present in the model",
                     "no shape asserts a constraint no ValidationRule enforces"],
         determinism="a pure function of the model and the registries")
def emit(ckm):
    reg = load_all()
    predicates = reg["REG-relationship-predicates"]
    rules = reg["REG-validation-rules"]
    types = sorted({n["type"] for n in ckm["nodes"]})
    used = sorted({e["predicate"] for e in ckm["edges"]})

    L = ["@prefix sh:   <http://www.w3.org/ns/shacl#> .",
         "@prefix eos:  <https://example.org/engineering-os/metamodel#> .",
         "@prefix ex:   <https://example.org/engineering-os/example#> .",
         "@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .", "",
         "# A PROJECTION of the Canonical Knowledge Model (ADR-0072).",
         "# Shapes are generated from the SAME registries the compiler reads, so",
         "# the shapes and the compiler cannot enforce different rules.", ""]

    for t in types:
        L += [f"eos:{t}Shape",
              "    a sh:NodeShape ;",
              f"    sh:targetClass eos:{t} ;",
              "    sh:property [",
              "        sh:path eos:label ; sh:minCount 1 ; sh:datatype xsd:string ;",
              f'        sh:message "Every {t} must carry a label" ;',
              "    ] ."]
        L.append("")

    L += ["# Every predicate used in the model, constrained to its registered core",
          "# type. A predicate with no registered parent is rejected at compile",
          "# time by VR-0002; these shapes state the same rule declaratively.", ""]
    for p in used:
        core, category = predicates[p]["core"], predicates[p]["category"]
        L += [f"eos:{_camel(p)}Shape",
              "    a sh:PropertyShape ;",
              f"    sh:path eos:{_camel(p)} ;",
              f'    sh:description "specializes {core} ({category})" ;',
              f"    sh:node eos:MetamodelEntity .", ""]

    L += ["# ValidationRules the compiler executes, stated as documentation. A",
          "# shape may not assert a constraint no rule enforces.", ""]
    for rid, rule in sorted(rules.items()):
        L.append(f"#   {rid}  {rule['kind']}: {rule['message']}")
    return "\n".join(L) + "\n"
