---
id: ADR-0144
title: Onboarding is optimized for reviewer efficiency, and the benchmark that matters requires humans
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0023, ADR-0120, ADR-0132, ADR-0138, ADR-0140, ADR-0142, ADR-0145]
---

# ADR-0144 — Reviewer efficiency, and the limit of simulation

## Context

The reviewer set the objective of onboarding and, separately, the limit of what
this project may measure alone.

> **Do not optimize for proposal count. Optimize for reviewer efficiency.** For
> every onboarding session measure: proposals generated · proposals accepted ·
> review time · evidence quality · reviewer corrections · reviewer confidence.
>
> **The objective is not discovering more. The objective is allowing a human
> reviewer to authorize better engineering understanding faster.**

and:

> Not *"did Guidance remain stable?"* Instead: **"did Guidance help engineers
> make better decisions?"** That benchmark will require humans. **Do not attempt
> to simulate it.** Real engineering teams should eventually become part of the
> validation.

## Decision

**The objective of Brownfield Onboarding is reviewer efficiency. Six figures are
recorded per curation session, and none of them may be produced without a
human.**

```text
proposals generated · proposals accepted · review time
evidence quality · reviewer corrections · reviewer confidence
```

**The headline figure is `accepted per minute of review`.** It is the only one
that moves in the right direction for the right reason: raising it by proposing
more fails, because unreviewed proposals cost time and accept nothing.

**Simulation is prohibited.** `tools/curate.py` **refuses to run without a
terminal**. A scripted session would generate precisely these numbers, and they
would be indistinguishable in the record from measurements of a real reviewer.

## Rationale

**Proposal count is the metric this project would otherwise reach for**, and it
fails `ADR-0132` outright: 453 proposals was the largest model ever built and
the least useful. **500 confident proposals a team cannot review is a worse
partner than 40 it can.**

Reviewer efficiency passes the same test. It cannot rise while understanding
deteriorates, because it counts what a human *authorized* — and a human
authorizes fewer things, more slowly, when the evidence is worse.

The prohibition on simulation is the same principle as `ADR-0023` and
`ADR-0138`. **The oracle is outside the system.** Every measurement this project
has is the model checking itself; a simulated reviewer would be the model
checking itself while wearing a person's name, and it would score well.

## Consequences

**Some measurements will stay empty for a long time, and empty is the honest
value.** No human has curated a model in this system. The instrument exists; the
reading does not, and it will not be filled in by a script.

**The onboarding skill's success criterion is not comparable to Discovery's.**
Deterministic Discovery is measured by what it proposes; onboarding is measured
by **what survives a human**. A skill that proposes half as much and gets twice
as much authorized has won.

**`did Guidance help engineers make better decisions?` is out of reach and
stays named.** It requires real engineering teams (`ADR-0138`). Recording it as
unreachable is more useful than a proxy that would be reported as if it were
the thing.

**Reviewer corrections are the most informative of the six.** A correction is a
proposal *right enough to keep and wrong as stated* — the signal that separates a
partner from a generator, and one no volume metric can express.

## Compliance

- `tools/curate.py` refuses non-interactive execution.
- Onboarding results report accepted-per-minute before any count.
- No reviewer-efficiency figure is generated without a human session.
- The human benchmark is named as unreached, never approximated.
