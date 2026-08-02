"""Explorer emitter — the primary interface to the model (ADR-0079).

Semantic navigation, not visualization: why an edge exists, provenance, what
derives from a node, impact of changing it, and its acceptance history.
"""
import json
import pathlib

from ...runtime.phases import feature

PAGE = pathlib.Path(__file__).parent / "page.html"


@feature("knowledge explorer projection",
         input_phase="ckm", output_phase="projection",
         invariants=["self-contained: no external request (ADR-0017)",
                     "every node reachable; every edge traversable in both directions",
                     "every edge explains itself from the vocabulary the model carries",
                     "a projection, never a source of truth (ADR-0072)"],
         determinism="the model is embedded verbatim; the page adds no state")
def emit(ckm):
    return PAGE.read_text().replace("__DATA__", json.dumps(ckm).replace("</", "<\\/"))
