---
id: ADR-0124
title: Discovery Skills have three maturity levels and only two are catalog assets
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0113, ADR-0115, ADR-0119, ADR-0121, ADR-0123]
---

# ADR-0124 — Discovery Skill maturity levels

## Context

`ADR-0121` gave Discovery Skills three **kinds** — general, technology, domain —
which say *what a skill knows*. It says nothing about *whether a skill should
outlive the experiment that produced it*.

That gap has a cost this project has already paid. `DS-multitenant-saas` was
written in one session, catalogued immediately, and reclassified in the next.
It was catalogued before anyone knew whether it generalized.

The reviewer supplied the missing axis:

> **Level 1** — repository-specific Discovery Skills. Useful for experiments.
> **Level 2** — reusable Technology Discovery Skills.
> **Level 3** — reusable Domain Discovery Skills.
>
> **Only Level 2 and Level 3 should become long-lived catalog assets. Level 1
> exists only to discover what should generalize.**

## Decision

**Every Discovery Skill declares a `level`.**

| Level | Scope | Lifetime |
|---|---|---|
| **1** | one repository | **disposable.** Exists to find out what should generalize, and is deleted without ceremony |
| **2** | a technology — Spring Security, Hibernate, Kafka, PostgreSQL, GeneXus, Kubernetes | long-lived |
| **3** | a business — Banking, Insurance, ERP, Healthcare, Manufacturing | long-lived |

**Only levels 2 and 3 are catalog assets.** A level 1 skill is an experiment
that happens to be written down.

**Promotion requires the evidence `ADR-0119` already demands**: the same need in
two or more repositories. Level is therefore not a quality judgement — a level 1
skill may be excellent and still not have earned a second sighting.

## Rationale

The levels give `ADR-0119` a place to put work it previously had to refuse
outright.

Before this decision the choice on finding a gap was binary: build a catalog
skill on one repository's evidence, or build nothing. **The first overfits and
the second wastes the observation.** Level 1 is the third option — write the
skill, run it, learn what it needs, and do not pretend it generalizes.

It also removes the incentive that produced the misclassification. Cataloguing
was previously the only way to record that a skill existed, so everything got
catalogued.

## Consequences

**The current catalog is ten skills at level 2 and none at level 1 or 3.** Nine
general skills and `DS-multitenant-saas`.

**`DS-authorization-discovery` may now be written as level 1** — against one
repository, disposable, to find out what a real authorization skill needs. The
reviewer's bar for promoting it to level 2 is unchanged and unmet: the same
missing understanding in Spring Security, ASP.NET Identity, NestJS Guards or
Django Permissions.

**A level 1 skill is not evidence.** Running one on a second repository is what
produces evidence; writing one produces a hypothesis.

## Compliance

- `discovery/skills/skills.yaml` declares `level: 1 | 2 | 3` on every skill.
- `tools/check-skills.py` rejects any other value and requires level 3 to be a
  domain skill.
- A promotion from level 1 cites two or more benchmark reports naming the same
  need.
