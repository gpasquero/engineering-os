"""Explorer emitter — the primary interface to the model (ADR-0079).

Question-driven, not node-driven (ADR-0084). It executes the SAME declared
queries `tools/ask.py` executes (ADR-0086); the language is shared and the engine
has two implementations.
"""
import json
import pathlib

from ...runtime.phases import feature
from ...query import load_queries

PAGE = pathlib.Path(__file__).parent / "page.html"


@feature("knowledge explorer projection",
         input_phase="ckm", output_phase="projection",
         invariants=["self-contained: no external request (ADR-0017)",
                     "every screen answers one declared engineering question",
                     "it implements no question; it executes declarations (ADR-0086)",
                     "a projection, never a source of truth (ADR-0072)"],
         determinism="model and queries are embedded verbatim; the page adds no state")
def emit(ckm):
    queries = load_queries()
    return (PAGE.read_text()
            .replace("__QUERIES__", json.dumps(queries).replace("</", "<\\/"))
            .replace("__DATA__", json.dumps(ckm).replace("</", "<\\/")))
