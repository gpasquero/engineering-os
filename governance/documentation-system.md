---
id: DOC-SYSTEM
title: Documentation System
status: accepted
created: 2026-08-02
updated: 2026-08-02
related: [ADR-0001, ADR-0002, ADR-0003]
---

# Documentation System

This document defines how knowledge is recorded in this repository.

It is normative. Every document in this repository must conform to it.

## Governing rule

The repository is the persistent memory of this project.

Conversation history is not memory. It is not durable, not reviewable, and not
available to a future session or a different agent. Any knowledge that exists
only in a conversation is considered lost.

Therefore:

- Every decision must produce an ADR.
- Every unknown must produce an issue.
- Every session must produce a session log.
- Every delivery must update the build state.

If a fact cannot be traced to a file in this repository, it does not exist.

## Document types

| Type | ID prefix | Location | Mutability | Purpose |
|---|---|---|---|---|
| Architecture Decision Record | `ADR-` | `governance/adr/` | Immutable once `accepted` | Records a decision, its context, alternatives and consequences |
| Issue | `ISSUE-` | `governance/issues/` | Mutable until `closed` | Records an open question, inconsistency, gap or risk |
| Session log | `SESSION-` | `governance/sessions/` | Immutable once written | Append-only journal of what a session did |
| Acceptance Record | `ACCEPT-` | `governance/acceptance/` | Immutable once written | The act that confers `Active` status on a revision (`ADR-0021`) |
| Governance document | none | `governance/` | Mutable | Vision, principles, glossary, roadmap, architecture, protocol |
| Build state | none | `governance/build-state.md` | Overwritten | The single current-status document |
| Design note | none | `governance/design/` | Mutable | Working proposals not yet promoted to a decision |
| Specification | `SPEC-` | `shared/`, `skills/`, `workflows/` | Versioned | Normative contracts and policies (from M2 onward) |
| Provenance | none | `imports/`, `sources/` | **Frozen** | Original inputs, never edited |

No other document types exist. Introducing one requires an ADR.

## Front matter

Every Markdown document under `governance/` begins with YAML front matter.
Documents outside `governance/` adopt it from M2 onward.

### ADR

```yaml
---
id: ADR-0001
title: Short imperative statement of the decision
status: proposed | accepted | superseded | rejected
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0004]
related: []
---
```

### Issue

```yaml
---
id: ISSUE-0001
title: Short statement of the unknown
type: question | inconsistency | gap | risk
status: open | resolved | deferred | closed
severity: blocking | high | medium | low
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence: [path/to/file.md]
resolved-by: null
---
```

### Session log

```yaml
---
id: SESSION-0001
date: 2026-08-02
milestone: M1
branch: feat/repository-bootstrap
---
```

## Status vocabularies

**Each of these is a distinct state machine** (`ADR-0025`). There is no global
concept of "state" in this project. `ADRLifecycle.Accepted` and
`ArtifactLifecycle.Accepted` are different states that happen to share an
English word; the label implies no equivalence.

In front matter the machine is determined by document type, so the bare value is
used. Explicit qualification is required wherever context does not fix the
machine — in prose, vocabularies, contracts and any cross-machine comparison.

These are closed sets. Adding a value requires an ADR.

**ADR status** — `proposed`, `accepted`, `superseded`, `rejected`.
An accepted ADR is never edited. It is superseded by a new ADR.

**Issue status** — `open`, `resolved`, `deferred`, `closed`.

- `open` — unresolved, and work that depends on it must not assume an answer.
- `resolved` — answered; `resolved-by` names the ADR or document that answers it.
- `deferred` — deliberately postponed; must name the milestone it defers to.
- `closed` — no longer relevant; must state why.

**Issue severity** — `blocking`, `high`, `medium`, `low`.
`blocking` means a named milestone cannot start until it is resolved.

**Issue type** — `question` (unknown), `inconsistency` (two sources disagree),
`gap` (something required is absent), `risk` (a known future hazard).

**Governance-document status** — `accepted` (normative), `current` (a living
index or status document), `proposal` (a design note, not binding),
`superseded` (replaced; must name `superseded-by`).

These three predate the revision lifecycle defined in `ADR-0020` (`Draft`,
`Under Review`, `Accepted`, `Active`, `Superseded`, `Archived`) and appeared to
overlap it. Under `ADR-0025` they do not: each is its own state machine, and
`ADRLifecycle.Accepted` never meant `ArtifactLifecycle.Active`.

The naming of the artifact/revision machine is still open (`ISSUE-0044`), as is
the full inventory of machines this repository owns (`ISSUE-0045`).

## ID allocation

IDs are zero-padded to four digits, allocated sequentially, and never reused.

A deleted or closed issue keeps its ID permanently. Renumbering is forbidden,
because IDs are referenced from ADRs, session logs and commit messages.

The highest allocated ID of each type is recorded in `governance/issues/index.md`
and `governance/adr/README.md`.

## File naming

```text
governance/adr/ADR-0001-repository-is-persistent-memory.md
governance/issues/ISSUE-0001-runtime-target-undefined.md
governance/sessions/SESSION-0001-2026-08-02.md
```

Lowercase, hyphen-separated slug after the ID. The slug is descriptive and may
differ from the title.

## Cross-referencing

Reference documents by ID in prose (`ISSUE-0004`), and by relative path in
front matter and link targets. Every ADR that answers an issue must list it in
`resolves`, and that issue must name the ADR in `resolved-by`. This
bidirectional link is mandatory — a one-sided link is a defect.

## Where knowledge must not live

- Not in commit messages alone.
- Not in code comments alone.
- Not in conversation history.
- Not in a chat summary handed to the next session.
- Not in `imports/` or `sources/`, which are frozen inputs and must never be
  edited to reflect current thinking.

## Separation of current and proposed state

Current state and proposed state are never mixed in the same document. This
mirrors the epistemic rule the Engineering OS itself imposes on target systems.

- `governance/build-state.md` describes only what exists.
- `governance/roadmap.md` describes only what is planned.
- `governance/design/` holds proposals that are not yet decisions.
- `governance/adr/` holds decisions that are not yet necessarily implemented.

## Known limitations

- `governance/issues/index.md` is maintained by hand and will drift. Tracked as
  `ISSUE-0028`; a generator is planned for M9.
- Front matter is not yet machine-validated. Schemas arrive in M9.
