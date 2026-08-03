# Periodic reacquisition and knowledge drift

**Purpose.** Periodically re-derive understanding at onboarding quality, in
order to **challenge** what the maintained model claims — and turn the
disagreement into a work queue.

> **Nothing a reacquisition produces is applied.** Its purpose is not to rebuild
> the model. A fresh candidate that silently replaced the curated model would
> throw away every decision a reviewer made.

---

## Producing a drift report

Reacquisition and drift are the last two stages of the lifecycle tool:

```bash
python tools/compile.py <project>                         # stage 5 needs a compiled model
python tools/lifecycle.py <before-repo> <after-repo> <project>
```

**Output location** — two files in `<project>/`:

- `candidate-reacquisition.json` — the fresh, full discovery. Never applied.
- `knowledge-drift-report.json` — the comparison.

The report is a JSON document with `mode`, `candidateDigest`,
`authoritativeNodes`, `candidateProposals`, per-class `statistics`, and `items`
keyed by drift class. Every item names a `subject` and its `evidence` or the
reason it was flagged:

```json
{
  "subject": "Artifact.AccountsController",
  "type": "Artifact",
  "evidence": "packages/backend/src/modules/accounts/accounts.controller.ts"
}
```

Its own note states the rule: *reacquisition validates and challenges the
maintained model. It does not replace it. Every item is a proposal requiring
review.*

---

## The fifteen drift classes

Each class declares where its work belongs. **Three route nowhere, and each says
why** — routing to a plan that cannot help would be worse than admitting there
is no route.

| Drift class | What it detects | Routes to |
|---|---|---|
| `D-new-knowledge` | the repository grew, or extraction improved | *not routed — additive; curation alone suffices* |
| `D-unsupported-assertion` | the model claims something the repository no longer shows | `P-review-unsupported` |
| `D-implementation-without-knowledge` | code nobody described | `P-discover` |
| `D-knowledge-without-implementation` | a description nothing implements | `P-verify-capability` |
| `D-invariant-without-enforcement` | a rule nothing checks | `P-establish-enforcement` |
| `D-dependency-change` | the boundary moved | *not routed* |
| `D-boundary-change` | modules, packages or contexts were restructured | `P-change-capability` |
| `D-conflicting-interpretation` | two readings of one fact | `P-resolve-conflict` |
| `D-missed-incremental-update` | continuous acquisition did not keep up | `P-review-unsupported` |
| `D-stale-provenance` | provenance that no longer resolves | `P-discover` |
| `D-obsolete-rationale` | knowledge whose reason expired while the knowledge remained | `P-change-concept` |
| `D-missing-evidence` | claims that entered the model without provenance | `P-discover` |
| `D-architectural-drift` | erosion, which no single added or removed fact reveals | `P-change-capability` |
| `D-business-rule-drift` | a rule that changed rather than disappeared | `P-change-concept` |
| `D-unexplained-divergence` | everything the taxonomy did not anticipate | *not routed* |

The registry lives in `model/drift-categories.md`.

---

## Turning the report into work

**Command**

```bash
python tools/drift-queue.py <project>
python tools/drift-queue.py <project> --plan=P-discover
```

**Input** `<project>/knowledge-drift-report.json`.
**Output** printed to stdout; nothing is written.

**Expected result**

```text
KNOWLEDGE DRIFT WORK QUEUE
  5 maintained nodes · 18 fresh proposals

  P-discover   8 item(s)
      Build a Candidate Engineering Model of …
      from D-implementation-without-knowledge  (8)
           extend the model over what exists
        e.g. Artifact.AccountsController
        e.g. Artifact.AccountsSpec

  P-establish-enforcement   1 item(s)
      Find where … is enforced, or record that nothing enforces it
      from D-invariant-without-enforcement  (1)
           find the enforcement point or record that none exists
        e.g. Invariant.MustRecordWhoAuthorisedTheRefund

  NOT ROUTED — curation alone, or unroutable by definition
      D-new-knowledge  (5)  additive; curation alone suffices
```

Items are grouped by the plan they route to, largest group first, with each
group's drift classes and the rationale for the routing. **The routing says what
*kind* of work this is, not what to do.**

**Nothing is instantiated automatically.** A report with 238 items would produce
238 plans, which is a queue nobody can face. Instantiating a plan is a curation
decision, and `--plan=` makes exactly one:

```bash
python tools/drift-queue.py <project> --plan=P-establish-enforcement
```

```text
INSTANTIATED  P-establish-enforcement  for  Invariant.MustRecordWhoAuthorisedTheRefund
  from drift class D-invariant-without-enforcement
  ── UNDERSTAND: …
```

It instantiates the plan for the **first** item in that group, against the
compiled model at `<project>/build/canonical-knowledge-model.json`.

> **A real limitation.** `--plan=P-discover` will usually fail with
> `NOT APPLICABLE — no node 'X' in this model`, because
> `D-implementation-without-knowledge` names subjects that are by definition
> *absent* from the maintained model, while plan instantiation requires the
> subject to be present in it. Exit code 1. The grouped queue above is still
> the useful output for that class; treat `--plan=` as working for classes whose
> subjects are already in the model.

---

## How this fits the loop

```text
maintained model ── periodic reacquisition ──▶ fresh candidate
        ▲                                             │
        └──────── curation ◀── drift work queue ◀──────┘
```

Reacquisition challenges; drift analysis routes; **curation decides**. Every
item in the queue is a proposal, and it enters the model through
[curation](curation.md) or not at all.

---

## Failure modes

| Symptom | Exit | Cause and fix |
|---|---|---|
| `no drift report at <project>/knowledge-drift-report.json` | 1 | run `tools/lifecycle.py` first; the message says so |
| `no drift items route to 'P-review-unsupported'` | 1 | that plan has no items in this report. The unflagged queue above lists which plans do |
| `NOT APPLICABLE — no node 'X' in this model` | 1 | the drift subject is not in the maintained model — see the limitation above |
| every class reports 0 | 0 | the fresh candidate and the maintained model agree, or reacquisition found nothing because the stack profile matched nothing |
