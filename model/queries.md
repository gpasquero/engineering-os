---
id: MODEL-QUERIES
title: Semantic Queries
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0081, ADR-0084, ADR-0085, ADR-0086]
---

# Semantic Queries

**Every engineering question Engineering OS can answer, declared as data.**

> **The query engine — not individual commands — is the semantic API**
> (`ADR-0086`). The Explorer, the CLI, agents and automation execute these same
> declarations.

## Operators

The engine implements operators. This file declares questions. Adding a question
is a data change; adding an operator is an engine change and should be rare.

| Operator | Does |
|---|---|
| `select` | start a result set — `{type}`, `{id}`, `{subject}`, or `{all: true}` |
| `traverse` | follow edges — `{direction, predicate, core, category, node-type, transitive, max-hops}` |
| `keep` | retain rows matching `{type}` or `{has-edge}` |
| `reject` | drop rows matching `{type}` or `{has-edge}` |
| `with` | attach a named sub-traversal to every row |

`direction` is `out`, `in` or `both`. `transitive` follows edges to fixpoint and
records `hops` and `via` — the first predicate on the path.

Output is `nodes` (default) or `edges`.

## The questions

```yaml
queries:
  - id: Q-impact
    question: What breaks if I change this?
    subject: required
    rationale: >
      Anything reachable by an incoming edge depends on this node, directly or
      transitively. This is the question ADR-0082 names first.
    steps:
      - traverse: {direction: in, transitive: true}

  - id: Q-why
    question: Why does this relationship exist?
    subject: required
    output: edges
    rationale: >
      Every edge carries its core type and category, and the model carries the
      vocabulary that defines them. The answer needs no access to the metamodel.
    steps:
      - traverse: {direction: both, max-hops: 1}

  - id: Q-rationale
    question: Which ADR established this, and does that decision still stand?
    subject: required
    rationale: >
      An invariant whose establishing decision has been superseded is a finding
      that no document states.
    steps:
      - traverse: {direction: in, core: establishes, node-type: ADR}
      - with:
          superseded-by: {direction: out, predicate: superseded-by}

  - id: Q-provenance
    question: Where did this come from?
    subject: required
    rationale: >
      Provenance is carried by the model, not remembered. Source revision is not
      yet recorded; ADR-0064 wants (artifact-id, revision-id).
    steps:
      - select: {subject: true}

  - id: Q-dependents
    question: Which Capabilities depend on this?
    subject: required
    rationale: >
      A Workflow's dependents are not all direct — a Capability may reach it only
      through a shared Skill.
    steps:
      - traverse: {direction: both, transitive: true}
      - keep: {type: Capability}

  - id: Q-tests
    question: Which Tests must change?
    subject: required
    rationale: >
      A test is an Artifact that `validates` another. No Test entity exists, and
      none is needed — it would introduce no relationship `validates` lacks.
    steps:
      - traverse: {direction: in, transitive: true}
      - keep: {has-edge: {direction: out, core: validates}}

  - id: Q-specifications
    question: Which Specifications become inconsistent?
    subject: required
    rationale: >
      A specification is an Artifact that `represents` a Concept. No
      Specification entity exists, for the same reason.
    steps:
      - traverse: {direction: in, core: represents}

  - id: Q-status
    question: What is the implementation status?
    subject: required
    rationale: >
      Acceptance confers Active status; commits do not (ADR-0018). A revision
      with no AcceptanceRecord is not Active, whatever the repository says.
    steps:
      - traverse: {direction: out, predicate: has-active-revision, or-self: true}
      - with:
          accepted-by: {direction: in, node-type: AcceptanceRecord}

  - id: Q-unenforced
    question: Which Invariants have no enforcement point?
    subject: none
    rationale: >
      `enforced-at` is zero-or-more by decision. The empty case is the finding —
      a rule the domain asserts and nothing checks.
    steps:
      - select: {type: Invariant}
      - reject: {has-edge: {direction: out, predicate: enforced-at}}

  - id: Q-unaccepted
    question: Which revisions are not Active?
    subject: none
    rationale: >
      The inverse of Q-status across the whole model. Answers "what is in this
      repository that nobody has accepted?" without reading any document.
    steps:
      - select: {type: ArtifactRevision}
      - reject: {has-edge: {direction: in, node-type: AcceptanceRecord}}

  - id: Q-orphan-concepts
    question: Which Concepts does nothing realise or reference?
    subject: none
    rationale: >
      A Concept nothing points at is either dead vocabulary or an undocumented
      dependency. Both are worth surfacing; neither is visible by reading.
    steps:
      - select: {type: Concept}
      - reject: {has-edge: {direction: in}}
```

## What declaring these exposed

**`Q-unaccepted` and `Q-orphan-concepts` did not exist before this file.** Both
were written because a table of questions invites *what else can be asked?* —
the same effect `validation-rules.md` produced, and the second time the format
has generated content the code form did not.

**Two questions needed no traversal at all.** `Q-unenforced` and
`Q-orphan-concepts` are `select` plus `reject`, which is evidence that the
useful questions are not all about reachability.

## Debt

**No query is parameterised beyond `subject`.** *Impact limited to two hops* or
*tests for this capability only* require an operator the language lacks.

**Two engines execute these declarations** — Python and the Explorer's
JavaScript — and **nothing checks that they agree** (`ADR-0086`).

**Every query scans.** There is no index; `Q-orphan-concepts` walks every edge
for every Concept. At 28 nodes this is irrelevant and it will not stay so.

**`subject: none` queries ignore any subject given.** That is silent rather than
an error.
