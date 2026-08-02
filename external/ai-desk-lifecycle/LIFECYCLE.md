---
id: EXTERNAL-AIDESK-LIFECYCLE
title: The first complete Brownfield Acquisition lifecycle
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0110, ADR-0111, ADR-0112, ADR-0113]
---

# The first complete acquisition lifecycle

```sh
python3 tools/lifecycle.py /tmp/ai-desk-before /Users/willy/Localsources/ai-desk \
    external/ai-desk-lifecycle
```

```text
Initial Acquisition → review → Authoritative Model → CKM
   → [real engineering change] → Continuous Acquisition
   → Periodic Reacquisition → Knowledge Drift Report
```

## The change is real, not simulated

**`97ca033 feat: Etapa 3 — SLA business-hours + column chooser + merge primary`**,
from `ai-desk`'s own history. The "before" state is a detached `git worktree` at
`97ca033^`, so the working tree was never touched.

| | digest | test suites |
|---|---|---|
| before | `01087455d80543f2` | 69 |
| after | `30a9a7207f45cc16` | 70 |

The change added `business-hours-calc.ts` and its spec — **261 lines, one new
test suite, 11 cases.**

## The run

| Stage | Result |
|---|---|
| **1 Initial Acquisition** | 299 proposals → **72 authorized** → 72 authoring sources |
| **2 Engineering change** | `suites +1`, detected mechanically |
| **3 Continuous Acquisition** | **4 incremental proposals**, 0 retractions → maintained model 76 sources |
| **4 Periodic Reacquisition** | 302 proposals, **not applied** |
| **5 Knowledge Drift Report** | 76 maintained nodes against 302 fresh proposals |

**Continuous Acquisition proposed 4 entities where a full rerun proposes 302.**
That is the point of the mode: *do not rerun the complete onboarding workflow
after every change.*

## What incremental maintenance captured

**The change, correctly.**

```text
Artifact.BusinessHoursCalcSpec
Invariant.Calculatebusinessminutes
Invariant.Addbusinessminutes
Invariant.ReturnsTheSameDateFor0Minutes
```

**`D-missed-incremental-update: 0`** — nothing the reacquisition found in the
changed evidence was absent from the maintained model.

## What it misrepresented — and the drift report caught it

**`D-unsupported-assertion: 1`**

> `Invariant.Addbusinessminutes` — a maintained assertion the fresh
> reacquisition does not support.

**The cause is a real defect, and it is in this repository, not in `ai-desk`.**

The suite declares **two** `describe` blocks — `calculateBusinessMinutes` and
`addBusinessMinutes`. The two acquisition modes read them differently:

| Mode | Rule | Proposes |
|---|---|---|
| Initial and Reacquisition | `R4` | `describes[0]` only → **one** invariant |
| Continuous | `C1` | **every** describe → **two** invariants |

**Continuous Acquisition and full reacquisition disagreed about the same
evidence**, and the maintained model carried an assertion a full rerun would
never produce.

> **This is exactly what a Knowledge Drift Report is for, found on its first
> real run.** Not drift between the model and the repository — **drift between
> two acquisition modes that were supposed to agree.**

**It is recorded and not silently fixed.** Fixing `R4` to iterate all `describe`
blocks would remove the finding and the evidence that the mechanism works.
Whichever rule is corrected, the correction is a proposal like any other, and the
divergence is now a documented question rather than an invisible inconsistency.

## What the maintained model does not contain

| | |
|---|---|
| `D-implementation-without-knowledge` | **123** |
| `D-new-knowledge` | **104** |
| `D-invariant-without-enforcement` | 10 |

**72 of 299 proposals were authorized**, so 227 things the repository contains
are absent from the model by choice. **The drift report states the size of that
choice** — which nothing previously did.

## What this demonstrates, and what it does not

**Demonstrated:**

- The lifecycle runs end to end against a real repository and a real commit.
- Continuous Acquisition maintains the model at **1.3% of the cost** of a rerun —
  4 proposals against 302.
- Periodic Reacquisition **challenges without replacing**: 302 fresh proposals
  changed nothing, and produced a report.
- **The drift report found a defect no other mechanism would have.**

**Not demonstrated:**

- **A change that removes evidence.** The retraction path exists and never fired;
  `Etapa 3` only added.
- **A change to a curated assertion.** Nothing a human corrected was later
  contradicted by the repository, which is the hardest case.
- **Runtime evidence.** No mode consumes it.
- **That the model stayed useful.** Synchronized is not the same as useful, and
  only running the Director against both states would show it.

## Cost

Initial Acquisition over a 469-file repository: **seconds**, because both
interpreters here are deterministic. The directive accepts that onboarding may
take hours; **that budget is unspent**, and is where probabilistic Discovery
Skills would go.
