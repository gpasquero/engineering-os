"""Diagnostics. A diagnostic names its phase, so a structural error is never
reported as a semantic one (ADR-0078)."""


class Diagnostic:
    __slots__ = ("phase", "source", "message", "rule")

    def __init__(self, phase, source, message, rule=None):
        self.phase, self.source, self.message, self.rule = phase, source, message, rule

    def __str__(self):
        where = f"{self.source}: " if self.source else ""
        tag = f" [{self.rule}]" if self.rule else ""
        return f"{where}{self.message}{tag}"

    def key(self):
        return (self.phase, self.source or "", self.message)

    def as_dict(self):
        return {"phase": self.phase, "source": self.source,
                "message": self.message, "rule": self.rule}


def sort(diagnostics):
    """Determinism: a failing project fails identically every run (ADR-0073)."""
    return sorted(diagnostics, key=lambda d: d.key())
