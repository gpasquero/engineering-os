"""OWL emitter — a projection of the Canonical Knowledge Model."""
import re

from ...runtime.phases import feature

EOS = "https://example.org/engineering-os/metamodel#"
NS = "https://example.org/engineering-os/example#"


def _iri(i):
    return "ex:" + re.sub(r"[^A-Za-z0-9_]", "_", i)


def _camel(k):
    head, *tail = k.split("-")
    return head + "".join(w.capitalize() for w in tail)


@feature("OWL projection",
         input_phase="ckm", output_phase="projection",
         invariants=["every instance is typed by a metamodel class",
                     "every edge uses a metamodel object property",
                     "the result imports the metamodel ontology"],
         determinism="a pure function of the canonical model")
def emit(ckm):
    L = [f"@prefix ex:   <{NS}> .", f"@prefix eos:  <{EOS}> .",
         "@prefix owl:  <http://www.w3.org/2002/07/owl#> .",
         "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
         "@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .", "",
         "# A PROJECTION of the Canonical Knowledge Model (ADR-0072). Generated; do not edit.",
         "",
         f"<{NS.rstrip('#')}> a owl:Ontology ;",
         '    rdfs:comment "Layer B model expressed in the Layer A metamodel." ;',
         f"    owl:imports <{EOS.rstrip('#')}> .", ""]
    for n in ckm["nodes"]:
        L.append(f"{_iri(n['id'])} a eos:{n['type']} ;")
        L.append(f'    rdfs:label "{n["label"]}" ;')
        if n["position"] is not None:
            L.append(f'    eos:hasPosition {n["position"]} ;')
        first = (n["description"].splitlines() or [""])[0].replace('"', "'")
        L.append(f'    rdfs:comment "{first}" .')
        L.append("")
    for e in ckm["edges"]:
        L.append(f"{_iri(e['from'])} eos:{_camel(e['predicate'])} {_iri(e['to'])} .")
    return "\n".join(L) + "\n"
