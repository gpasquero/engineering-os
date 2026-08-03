---
name: engineering-guidance
description: Get deterministic guidance before changing a system — what to read first, what constrains the change, which capabilities are affected, and what to verify. Use when the user is about to modify, extend, refactor or investigate something in a repository that has an Engineering OS model, or asks how to approach a change safely.
---

# Requesting engineering guidance

Guidance is **derived from the model, not generated**. No language model
participates in producing a plan — including you. Your job is to run it,
interpret it, and act on it.

```bash
eos advise <project> recommendations                    # what advice exists
eos advise <project> R-change-concept Concept.Order     # advice for a subject
eos direct <project> intents                            # the intents
eos direct <project> I-modify-behavior Concept.Order    # the full loop
```

`direct` runs **intent → plan → task graph → worker assignment → execution
context**. It tells you which decisions were made deterministically and which
are deliberately left to a worker.

## Use it before you change anything

When the user asks you to modify a system that has a model, run guidance
**first**. It answers what to read before deciding, what invariants constrain
the change, which capabilities are affected, and what to verify afterwards —
from recorded evidence rather than from your reading of the code.

## Read what it deliberately does not say

- A step reported as **not applicable** is named, with the reason. That is the
  system saying *this does not apply to your subject*, not an error.
- An intent with **no plan** says so. `I-investigate` is a real intent with no
  planning support, recorded as a gap rather than hidden.
- An **empty** result means the model has nothing on this subject.

**Do not fill these in from your own reading and present the result as
guidance.** If the model is thin, say so and offer to onboard what is missing.

## After the change

```bash
eos maintain <before-repo> <after-repo> <project>
```

Only what changed is proposed, carrying the meaning the onboarding established.
Removals are never applied automatically — they are proposals a human reviews.
