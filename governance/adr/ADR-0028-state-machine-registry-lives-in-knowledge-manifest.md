---
id: ADR-0028
title: The State Machine Registry is a section of KNOWLEDGE-MANIFEST.yaml
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0047]
related: [ADR-0013, ADR-0027, ISSUE-0049]
---

# ADR-0028 — The State Machine Registry lives in `KNOWLEDGE-MANIFEST.yaml`

## Context

`ADR-0027` made the State Machine Registry the source of truth for state
machines, without saying where it lives. `ISSUE-0047` recorded three candidate
homes and noted that `ADR-0013` had already assigned "state machines" to
`KNOWLEDGE-MANIFEST.yaml`, while `ADR-0025` had assigned vocabularies grouped by
state machine to `shared/vocabularies/`.

## Decision

**The State Machine Registry belongs in `KNOWLEDGE-MANIFEST.yaml`.**

A state machine is part of the **semantic model of the domain**. It is not
project metadata. It is not build metadata. **It is knowledge.**

This sharpens the three-manifest split from `ADR-0013` into a decision test:

| Manifest | Describes |
|---|---|
| `MANIFEST.yaml` | the repository **architecture** |
| `BUILD-STATE.yaml` | the implementation **status** |
| `KNOWLEDGE-MANIFEST.yaml` | the **semantic structure** of the repository |

The registry is therefore a **section of `KNOWLEDGE-MANIFEST.yaml`**, not an
independent top-level file.

**Individual state machine specifications remain separate artifacts.**
`KNOWLEDGE-MANIFEST.yaml` only **indexes and relates** them.

## Alternatives considered

**A separate registry file declared from `KNOWLEDGE-MANIFEST.yaml`.** This was
the option `ISSUE-0047` judged most likely, on the grounds that nine-field
registrations with transition rules would be too heavy for a manifest. Rejected:
the weight objection disappears once the manifest only indexes, and a separate
top-level file would add a fourth root artifact whose relationship to the
manifest would need explaining every time.

**The registry in `shared/vocabularies/`.** Rejected: `shared/` holds the
methodology, and a state machine is domain semantics. It would also mean an
adopting repository declared its domain's state machines inside the framework's
shared layer, which inverts the ownership rule in `ADR-0010`.

**A fourth manifest.** Rejected: the three-manifest split is defined by
responsibility, and semantics already has a manifest.

## Consequences

### Positive

- **`ADR-0013`'s split gains a usable decision test.** Architecture, status,
  semantics — a sharper criterion than "responsibility and lifecycle", and one
  that answers future placement questions without re-litigating them. State
  machines were the first real test and it resolved cleanly.
- Knowledge ownership holds across repositories: an adopter declares its domain
  state machines in its own knowledge manifest, exactly as it declares its
  ontology modules.
- The index/specification split keeps the manifest readable while letting each
  specification be as detailed as its machine requires.
- **Third instance of the same pattern.** `MANIFEST.yaml` indexes skills whose
  specifications live in `skills/`; `ADR-0027` made the registry an index; this
  puts the index in a manifest and the specifications outside it. Three
  independent arrivals at *registry indexes, specifications live separately* is
  no longer a coincidence worth watching — it is close to a principle, and
  should be named as one when the fourth appears.

### Negative

- **Where the specifications live is now the open question**, moved rather than
  answered. `shared/vocabularies/` was slated to hold vocabularies grouped by
  state machine, and the vocabulary is one of the nine registration fields —
  so the boundary between a state machine specification and a vocabulary file is
  undefined. `ISSUE-0049`.
- `KNOWLEDGE-MANIFEST.yaml` grows a section whose entries point outward, so
  reading it alone no longer tells you what a state machine does. That is the
  intended trade, but it makes the manifest less self-contained than the other
  two.

### Neutral

- No change to `ADR-0027`'s registration model. Only its location is fixed.

## Compliance

No state machine registry exists outside `KNOWLEDGE-MANIFEST.yaml`. The manifest
contains index entries and relationships only — never a full specification. No
state machine is declared in `MANIFEST.yaml` or `BUILD-STATE.yaml`.
