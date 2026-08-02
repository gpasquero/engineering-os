---
id: ADR-0136
title: The North Star is preserving an engineering team's ability to make correct decisions as software evolves
status: accepted
date: 2026-08-02
supersedes: ADR-0131
superseded-by: null
resolves: []
related: [ADR-0123, ADR-0127, ADR-0128, ADR-0131, ADR-0133, ADR-0134, ADR-0135]
---

# ADR-0136 — The North Star

## Context

`ADR-0131` set the North Star as *can Engineering OS preserve engineering
understanding as software evolves?* One session later the reviewer moved it
again, and the move is not a rewording:

> Originally the promise was *"we can acquire engineering knowledge."*
> Then *"we can maintain engineering understanding."*
>
> I think the promise is now becoming: **"We preserve an engineering team's
> ability to make correct decisions as software evolves."**
>
> That is stronger than maintaining a model. That is stronger than preserving a
> graph. That is ultimately what customers pay for.

## Decision

**The North Star is: *we preserve an engineering team's ability to make correct
decisions as software evolves.***

`ADR-0131` is superseded. Its instrument, its severity and its ordering all
survive; **its subject changes from the model to the team.**

| | `ADR-0131` | **`ADR-0136`** |
|---|---|---|
| Subject | Engineering OS | **an engineering team** |
| Preserved | understanding | **the ability to decide correctly** |
| Succeeds when | questions still answer | **decisions are still right** |
| Measured by | Understanding Retention | retention **and** Guidance Preservation |

**Three words carry it, and each rules something out.**

**A team** — not a model. A perfectly maintained model nobody can act on
preserves nothing. This is the first framing whose subject is outside the
software.

**Correct decisions** — not answers. An answer may be accurate and useless; a
decision is correct or it is not, and correctness is checkable after the fact.

**As software evolves** — unchanged from `ADR-0131`, and still the part only the
frozen suite can measure.

## Rationale

The escalation is exactly one level, and it lands on the property nothing
measures. `ADR-0133` names three preservation properties and only Understanding
is measured; **this North Star is Guidance Preservation stated as a promise.**

It also raises the standard on work that has already passed. This session
restored `EQ-06` and reached 100 % Understanding Retention — success under
`ADR-0131`, and under `ADR-0136` **an unfinished argument**: nothing yet shows
that a team makes a better decision because `EQ-06` answers.

**That gap is the point.** A North Star that the current work already satisfies
is a description, not a direction.

## Consequences

**Understanding Retention remains the primary measured KPI** (`ADR-0132`) and is
no longer the terminal one. It is necessary and not sufficient.

**Guidance Preservation becomes the next thing to measure**, and `ADR-0135`
already names who owns it. The question — *would this plan still be correct ten
commits later?* — runs on the same frozen suite, which is now the instrument for
both products.

**Correctness needs a definition before it can be measured**, and inventing one
alone would be self-certification (`ADR-0023`). What a *correct decision* means
is a reviewer question, and it is recorded as open rather than assumed.

**Acquisition is now two levels from the objective**: it produces understanding,
understanding enables guidance, guidance preserves the ability to decide. It
remains necessary and it is no longer close to the promise.

## Compliance

- Architectural proposals state how they help a team decide correctly, not only
  how they help the model answer.
- Where an admission test and the North Star conflict, the North Star governs.
- *Correct decision* is defined by the reviewer before Guidance Preservation is
  measured.
