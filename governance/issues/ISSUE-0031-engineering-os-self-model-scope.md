---
id: ISSUE-0031
title: The scope of Engineering OS's own model/ is undefined
type: gap
status: open
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M2, M11]
evidence:
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
resolved-by: null
---

# ISSUE-0031 — The scope of Engineering OS's own `model/` is undefined

## Statement

`ADR-0010` establishes that Engineering OS has its own `model/` describing the
framework. What "describes the framework" means is not defined.

## Why it matters

This is the strongest available test of the methodology: if Engineering OS
cannot produce a coherent knowledge model of itself, the methodology does not
work. `governance/roadmap.md` now places this at M11, before the v1 release,
for exactly that reason.

It also raises a question the methodology has not yet faced. The prototypes
reconstruct knowledge from an *implementation* — code, tests, schemas,
migrations. Engineering OS is largely prose. What counts as evidence when the
system under analysis is a methodology rather than a program?

## Open sub-questions

- What is the domain? Software engineering as a practice, or Engineering OS as
  an artifact? These produce very different ontologies.
- What are the bounded contexts of a methodology?
- What is evidence here? Prose is not executable, so the inherited evidence
  hierarchy — which ranks observable runtime behavior first — does not apply as
  written.
- Does `governance/` become part of `model/`, or stay separate? They overlap:
  the glossary is already a Layer B artifact by any reasonable reading, yet it
  lives in `governance/` because it existed before `model/` did.

That last question is the one most likely to force a structural change, and it
should be answered before `model/` is created rather than after.

## Compounded by ADR-0013

`ADR-0013` defines `KNOWLEDGE-MANIFEST.yaml` as declaring, among other things,
**glossary modules**, bounded contexts, capabilities, invariants and state
machines.

This repository's glossary lives at `governance/glossary.md`, not in a knowledge
model. So the overlap is no longer hypothetical: a manifest of the knowledge
model will need to point at a glossary that currently sits in the memory layer.

Either the glossary moves into the knowledge model, or `governance/` is declared
part of the model, or the two are explicitly different glossaries — one for the
project's own vocabulary, one for the modelled domain. The third reading is
defensible, because the domain being modelled (`ISSUE-0034` notwithstanding) may
legitimately be software engineering rather than Engineering OS the artifact.

This must be settled before `KNOWLEDGE-MANIFEST.yaml` is written, not at M11.

## Resolution criteria

An ADR defining the scope of the self-model and its relationship to
`governance/`, followed by the model itself in M11.
