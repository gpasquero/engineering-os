# Greenfield usage

**Purpose.** Build an Engineering OS model for a system that does not exist yet,
or one whose stack is not supported by Mechanical Discovery.

> **Only manual authoring is supported.** There is no greenfield automation in
> this repository — no scaffolder, no generator, no interactive model builder,
> and no command that turns a specification into authoring sources. None is
> claimed, and nothing below is a workaround for a feature that exists
> elsewhere. What you get is a compiler, a query engine and a guidance engine
> over Markdown files you write yourself.

---

## What an authoring source actually is

One Markdown file per entity, under `<project>/model/`. YAML front matter
declares the node; the prose below the front matter is for humans and the
compiler does not interpret it.

This is `examples/tiny/model/concept-order.md`, verbatim:

```markdown
---
id: Concept.Order
type: Concept
label: Order
relationships:
  - scoped-to: BoundedContext.Sales
---
A customer's request to purchase goods, from submission until fulfilment.
```

And `examples/tiny/model/invariant-payment-before-shipping.md`:

```markdown
---
id: Invariant.PaymentBeforeShipping
type: Invariant
label: An order cannot ship before payment clears
relationships:
  - scoped-to: BoundedContext.Sales
  - constrains: Concept.Order
---
Stated independently of whatever enforces it. Note that `enforced-at` is absent:
this invariant has no recorded enforcement point, which is a finding rather than
an omission.
```

Ordering lives on a reified association, not on the thing being ordered — this
is `examples/tiny/model/workflow-step-checkout-1.md`:

```markdown
---
id: WorkflowStep.Checkout.1
type: WorkflowStep
label: Checkout step 1
position: 1
relationships:
  - step-of: Workflow.Checkout
  - executes: Skill.ValidateOrder
---
The reified association. The position lives here, not on the Skill.
```

---

## The front-matter contract

Declared in `compiler/parser/schemas/node.yaml` and enforced at the Parsing
phase, before any semantic resolution.

| Key | Required | Type | Notes |
|---|---|---|---|
| `id` | yes | string | Stable and unique within the project. Must match `^[A-Za-z][A-Za-z0-9]*(\.[A-Za-z0-9_-]+)*$` |
| `type` | yes | string | A metamodel entity name. Checked at Resolution |
| `label` | no | string | Human-readable name; defaults to the id |
| `position` | no | integer | Extrinsic ordinal; only meaningful on reified associations such as `WorkflowStep` |
| `relationships` | no | list | A list of **single-key mappings**, predicate → target id |
| `attributes` | no | mapping | Flat key/value facts carried verbatim into the model. **Scalar values only** |

Two rules catch most authoring mistakes: `relationships` must be a *list* (a
string fails at Parsing), and `attributes` values must be *scalar* (a nested
structure fails at Parsing).

**The 23 entity types** are declared in `model/metamodel/entities/` — one
specification file each. Read the specification for the type you intend to use;
it states what the type means and which relationships it participates in.

| Family | Types |
|---|---|
| descriptive | `Actor`, `Artifact`, `ArtifactRevision`, `BoundedContext`, `CanonicalKnowledgeModel`, `Capability`, `Concept`, `Dimension`, `DimensionAssignment`, `Evidence`, `Invariant`, `RelationshipType`, `StateMachineSpecification` |
| operational | `ADR`, `AcceptanceRecord`, `EngineeringGate`, `Issue`, `Policy`, `Registry`, `Skill`, `ValidationRule`, `Workflow`, `WorkflowStep` |

Predicates are not free text either. All 74 are declared in
`model/metamodel/relationship-vocabulary.md`, each specialising one of 18 core
relationship types. An unregistered predicate is rejected at Resolution.

---

## Start a project

```bash
mkdir -p myproject/model
cp examples/tiny/model/*.md myproject/model/
# edit them to describe your system, then:
python tools/compile.py myproject
```

`examples/tiny/model/` uses thirteen of the entity types and is the smaller
starting point. `examples/vertical-slice/model/` is larger (28 nodes, 52 edges)
and shows workflows, gates, policies, evidence and acceptance records together —
copy from it when you want a fuller vocabulary.

Remember that project paths resolve against the **repository root**, so
`myproject` above means `<checkout>/myproject`. An absolute path works too.

---

## The loop this is meant to support

```bash
python tools/compile.py myproject
python tools/advise.py myproject recommendations
python tools/advise.py myproject R-change-concept Concept.YourConcept
python tools/measure.py myproject
```

Ask for guidance **before** implementing, and update the authoring sources as
work completes. `tools/measure.py` tells you which of the nine Engineering
Questions your model can already answer — it is the fastest signal that a model
is thin in a way that matters.

---

## What does not work in a greenfield project

- **Discovery is not available.** `discovery/run.py` and `tools/onboard.py`
  require a repository matching a Stack Profile. There is nothing to extract
  from a system that does not exist.
- **Continuous acquisition is not available** for the same reason. Keeping the
  model current is manual: edit `model/*.md` and recompile.
- **Nothing validates your model against reality.** In brownfield onboarding a
  proposal cites a file and a locator; a hand-authored assertion cites whatever
  you put in its `attributes`. `python tools/ask.py myproject Q-unsupported`
  lists assertions carrying no evidence at all, which is the closest available
  check.

---

## Failure modes

| Symptom | Cause and fix |
|---|---|
| `[discovery]  0 authoring sources` | wrong path, or files are not directly under `<project>/model/`. `compile.py` creates a missing directory rather than failing |
| `bad.md: key 'relationships' must be list, got str` | `relationships:` was written as a string; it must be a YAML list of single-key mappings |
| `a.md: attributes must be scalar; ['source'] are not` | an attribute value is a list or mapping |
| `w.md: 'Widget' is not a metamodel entity [VR-0001]` | `type` is not one of the 23 declared entity types |
| `a.md: predicate 'invented-link' has no registered parent (ADR-0071) [VR-0002]` | the predicate is not in the relationship vocabulary |
| `a.md: 'references' points at unknown node 'Concept.Missing' [VR-0003]` | the target id does not exist in this project |
| `duplicate node id 'Concept.Same' declared 2 times [VR-0004]` | two files declare the same id |
| `loop.md: 'scoped-to' on 'BC.Loop' points at itself [VR-0005]` | a containment or revision edge points at its own node |
| `step.md: a WorkflowStep must declare 'executes' [VR-0006]` | a `WorkflowStep` exists only to position a `Skill`; it must execute one |
