---
id: ADR-0121
title: Discovery Skills are general, technology or domain, and all three produce the same entities
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0085, ADR-0108, ADR-0113, ADR-0115, ADR-0117, ADR-0119]
---

# ADR-0121 — Three kinds of Discovery Skill

## Context

`ADR-0115` declared two kinds of Discovery Skill: `general` and `domain`. The
reviewer refined the taxonomy:

> **Technology Discovery Skills understand frameworks** — Spring Security,
> Hibernate, Kafka, Kubernetes, PostgreSQL.
>
> **Domain Discovery Skills understand businesses** — Banking, ERP, Healthcare,
> Insurance, E-commerce, Manufacturing.
>
> **Both should produce exactly the same metamodel entities. They differ only in
> how engineering understanding is acquired.**

The distinction `ADR-0115` was missing is not between *software* and *business*.
It is between **three different sources of prior knowledge**.

## Decision

**A Discovery Skill declares one of three kinds.**

| Kind | Knows about | Prior knowledge it carries |
|---|---|---|
| `general` | software, in any language and any business | how systems are shaped |
| `technology` | a framework, runtime or datastore | where that framework puts things, and what it implies |
| `domain` | a business | what such a business must be true of, whether or not the code says so |

**All three produce exactly the same metamodel entities.** A Spring Security
skill and a Banking skill both propose `Invariant`, `Concept`, `Capability`,
`Actor`. Neither may introduce a type, and a kind that seemed to require one
would be evidence the kind does not fit (`ADR-0085`).

**They differ only in how understanding is acquired**, and that difference is
entirely in the *questions* the skill asks, never in its output.

## Framework semantics may not leak into Discovery Skills

The reviewer was explicit, and it constrains this decision:

> **Keep Mechanical Acquisition stack-aware and repository-independent.
> Interpretive Discovery should continue consuming only the Mechanical
> Engineering Model. Do not let framework-specific semantics leak into Discovery
> Skills.**

This looks like a contradiction with a `technology` kind and is not. The
boundary is:

- **A Stack Profile knows where a framework puts things.** `@Entity`,
  `@GetMapping`, `pgTable(`. It is `stacks.yaml`, it is mechanical, and it
  produces facts in a stack-independent vocabulary (`ADR-0117`).
- **A Technology Discovery Skill knows what a framework's presence implies.**
  *If Spring Security is on the classpath, which endpoints are unprotected, and
  what happens to a request that presents no credential?*

The first is a parser. **The second is a question.** A technology skill that
started matching annotations would have become a parser plugin, which
`ADR-0115` already forbids, and the test is simple:

> **Does the skill read the repository, or does it read the Mechanical
> Engineering Model?** If the former, it is a Stack Profile wearing a skill's
> name.

## Rationale

The taxonomy immediately corrected a misclassification this project had already
made.

`DS-multitenant-saas` was written in `SESSION-0044` as the worked example of a
**domain** skill. Multi-tenancy is not a business. Banking is a business;
multi-tenancy is an **architectural pattern**, and the skill's questions —
*which tables carry a tenant discriminator, how does a request acquire its
tenant* — are structural, not commercial.

**It is easy to believe you are encoding business knowledge when you are
encoding structure**, and a taxonomy with only two boxes made that mistake
invisible. It is reclassified as `technology`, and the domain category is empty
again — honestly this time.

## Consequences

**`DS-authorization-discovery` is a `technology` skill, and the evidence bar is
now precise.** The reviewer set it:

> Build it only if the same missing engineering understanding appears again in a
> fundamentally different repository — Spring Security, ASP.NET Identity, NestJS
> Guards, Django Permissions. **If all produce the same engineering question,
> then the Discovery Skill is justified.**

`ADR-0120` makes this measurable rather than a judgement: `EQ-08` currently
scores `no-query`, which is a **constant** and cannot accumulate. **The bar
cannot be met by measuring more repositories.** Something must first be declared
that attempts the question at all.

**The domain category stays empty until a real business is in front of us.** A
domain skill invented without a customer would encode our guesses about banking,
and `ADR-0119` exists precisely to stop that.

## Compliance

- `discovery/skills/skills.yaml` declares `kind: general | technology | domain`;
  `technology` skills name their `technology` and `domain` skills their
  `domain`.
- `tools/check-skills.py` rejects any other value and any skill whose
  `permitted-tools` include reading the repository directly.
- No skill of any kind proposes a type outside the twenty-three.
