"""Discovery — authoring sources to a source set."""
from ..runtime.phases import feature


@feature("source discovery",
         input_phase="authoring", output_phase="discovery",
         invariants=["every *.md under model/ is a source",
                     "no source is read twice",
                     "discovery reads no file content"],
         determinism="sources are sorted by path, so the source set is order-stable")
def discover(project):
    return sorted((project / "model").glob("*.md"))
