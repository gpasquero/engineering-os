"""JSON emitter — a serialization of the model, not the model (ADR-0076)."""
import json

from ...runtime.phases import feature


@feature("JSON projection",
         input_phase="ckm", output_phase="projection",
         invariants=["round-trips: json.loads(emit(m)) == m",
                     "keys are emitted in model order, not sorted, so diffs stay readable"],
         determinism="a pure function of the canonical model")
def emit(ckm):
    return json.dumps(ckm, indent=2) + "\n"
