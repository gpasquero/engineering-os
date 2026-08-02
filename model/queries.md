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
| `with` | attach a named sub-traversal to every row, reporting **the edge in hand** |

`direction` is `out`, `in` or `both`. `transitive` follows edges to a bounded
fixpoint.

## The result contract (`ADR-0088`)

Every execution returns a **status**, and an empty result never hides an
applicability error:

| Status | Means |
|---|---|
| `ok` | valid query, results |
| `empty` | valid query, no results — **often the finding** |
| `not-applicable` | the query does not apply to this subject type |
| `invalid` | the declaration or subject is malformed |

**Every row carries its complete ordered path** — every traversed edge with its
direction and the reason it matched — plus `hops` and `origin`. `via` remains as
the first predicate of that path and is a convenience, never the explanation.

Output modes: `nodes` (default) · `edges`, which returns **the edges the
traversal actually walked** · `induced-subgraph`, which returns every edge
between result nodes and is **never the default** because it includes
relationships the query never followed.

Bounded by default: **depth 16, results 1000**, both overridable per query, and
**truncation emits a diagnostic**.

`applies-to` declares which subject types a question supports. Omitting it means
any type.

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
    applies-to: [Invariant, Policy, Concept, Capability]
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
    applies-to: [Workflow, Skill, Artifact, Concept]
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
    applies-to: [Concept, Capability, Invariant]
    rationale: >
      A specification is an Artifact that `represents` a Concept. No
      Specification entity exists, for the same reason.
    steps:
      - traverse: {direction: in, core: represents}

  - id: Q-status
    question: What is the implementation status?
    subject: required
    applies-to: [Artifact, ArtifactRevision]
    rationale: >
      Acceptance confers Active status; commits do not (ADR-0018). A revision
      with no AcceptanceRecord is not Active, whatever the repository says.
    steps:
      - traverse: {direction: out, predicate: has-active-revision, or-self: true}
      - with:
          accepted-by: {direction: in, node-type: AcceptanceRecord}

  - id: Q-constraints
    question: Which invariants or guarantees constrain this?
    subject: required
    rationale: >
      A capability is bounded by what must remain true of it. Answering this
      requires the constraint to be modelled separately from the thing it
      constrains, which is why Invariant is its own entity.
    steps:
      - traverse: {direction: in, core: governs, node-type: Invariant}

  - id: Q-evidence
    question: What evidence supports this, and where does it come from?
    subject: required
    rationale: >
      An assertion without a citation is a claim. This is the query that makes
      "insufficient evidence" a visible answer rather than an empty one, and it
      is how an answer whose support spans several source classes is recognised.
    steps:
      - traverse: {direction: out, core: evidenced-by, node-type: Evidence}

  - id: Q-unsupported
    question: Which assertions carry no evidence at all?
    subject: none
    rationale: >
      A confident fabricated connection is worse than an incomplete result.
      This lists every Concept, Capability and Invariant that nothing cites —
      the model's own honesty check.
    steps:
      - select: {type: Invariant}
      - reject: {has-edge: {direction: out, core: evidenced-by}}

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

**`applies-to` is declared on four queries and omitted on the rest.** Omission
means *any type*, which is right for `Q-impact` and lazy for `Q-tests` — nothing
yet forces the question.

**Paths are larger than the rows carrying them.** A five-hop result carries five
edge records per row and nothing prunes them.
