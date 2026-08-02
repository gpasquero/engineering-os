"""First-class compiler phases and the feature contract (ADR-0073)."""


class Phase:
    def __init__(self, key, title, consumes, produces, executed=True):
        self.key, self.title = key, title
        self.consumes, self.produces, self.executed = consumes, produces, executed


PHASES = [
    Phase("authoring", "Authoring", "human intent", "authoring sources", executed=False),
    Phase("discovery", "Discovery", "authoring sources", "a source set"),
    Phase("parsing", "Parsing", "a source set", "structurally valid assertions"),
    Phase("resolution", "Resolution", "assertions", "a resolved assertion set"),
    Phase("ckm", "Canonical Knowledge Model", "resolved assertions", "the semantic model"),
    Phase("projection", "Projection", "the semantic model", "derived artifacts"),
]
PHASE_KEYS = {p.key for p in PHASES}
FEATURES = []


def feature(name, *, input_phase, output_phase, invariants, determinism):
    """Register a compiler feature with its mandatory four-field contract."""
    assert input_phase in PHASE_KEYS and output_phase in PHASE_KEYS, name
    assert invariants and determinism, f"{name}: a feature with no stated determinism has none"

    def wrap(fn):
        FEATURES.append({"name": name, "input": input_phase, "output": output_phase,
                         "invariants": invariants, "determinism": determinism})
        return fn
    return wrap


def describe():
    out = ["Compiler phases (ADR-0073)", ""]
    for p in PHASES:
        mark = "" if p.executed else "   [not executed by the compiler]"
        out += [f"  {p.title}{mark}",
                f"    consumes: {p.consumes}",
                f"    produces: {p.produces}"]
    out += ["", f"Features ({len(FEATURES)})", ""]
    for f in sorted(FEATURES, key=lambda f: ([p.key for p in PHASES].index(f["input"]), f["name"])):
        out.append(f"  {f['name']}:  {f['input']} -> {f['output']}")
        out += [f"    invariant:   {i}" for i in f["invariants"]]
        out.append(f"    determinism: {f['determinism']}")
    return "\n".join(out)
