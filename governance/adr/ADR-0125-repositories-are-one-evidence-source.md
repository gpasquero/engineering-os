---
id: ADR-0125
title: The Engineering Model is the stable representation; a repository is one evidence source
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0072, ADR-0081, ADR-0108, ADR-0117, ADR-0118, ADR-0123]
---

# ADR-0125 — Repositories are one evidence source

## Context

Every piece of evidence Engineering OS has ever consumed came from a Git
repository. Nothing else has been tried, and the architecture has quietly grown
around that fact: Mechanical Acquisition globs files, Stack Profiles describe
directory layouts, and Continuous Acquisition is driven by a commit.

The reviewer named the risk before it hardened:

> **The Engineering Model should eventually become the stable engineering
> representation. Repositories are simply one evidence source.** Future evidence
> sources may include runtime observations, production incidents, architecture
> diagrams, API gateways, issue trackers, ADR repositories, operational metrics,
> human engineering reviews.
>
> **Repositories should not become the center of the architecture. They are
> simply the richest current source.**

## Decision

**The Authoritative Engineering Model is the stable representation. Every input
is an evidence source, and a repository is one of them.**

Three rules follow.

**1. No component below the Engineering Model may assume its evidence came from
a repository.** The CKM, the query engine, Plans, Recommendations, the Director
and the Drift Report already satisfy this and it is now binding.

**2. A new evidence source supplies facts in the mechanical vocabulary; it does
not extend the metamodel.** A production incident is `Evidence`; a runtime
observation is `Evidence`; an issue is an `Artifact` or `Evidence`; a
person's review is `Evidence` with an `Actor`. **A source that appeared to
require a twenty-fourth entity would be evidence the source is being modelled
wrongly** (`ADR-0085`).

**3. Provenance names the source, not only the file.** Today every assertion
carries a path. When a second source exists, a path is ambiguous — an assertion
must say *which kind of evidence* produced it, or two sources disagreeing cannot
be told apart from one source being read twice.

## Rationale

The three acquisition modes were written for repositories and **describe
something more general than repositories** (`ADR-0118`):

| Mode | Repository | Runtime | Incidents |
|---|---|---|---|
| Initial | clone and read | observe a period | read the history |
| Continuous | a commit | a new trace | a new incident |
| Periodic | full rediscovery | a fresh observation window | re-read with today's model |

**The lifecycle survives the generalization unchanged**, which is the strongest
available evidence that the abstraction was drawn in the right place.

The vocabulary is where the leak is. Its eight keys — packages, dependencies,
module directories, routes, tables, test suites, configuration references,
documents — are **all repository nouns**. A runtime source would have nowhere to
put a latency distribution and no honest way to invent one.

## Consequences

**This decision builds nothing**, by `ADR-0116` and `ADR-0119`. No customer has
asked for a second source and none is available to test against. What it does is
forbid a class of decision that would be expensive to undo:

- extending the mechanical vocabulary with more repository-shaped keys without
  asking whether the key is a *repository* fact or an *engineering* fact;
- letting a Stack Profile concept leak upward into Discovery Skills, which
  `ADR-0121` already forbids for exactly this reason;
- treating "the repository" as a synonym for "the system" in documentation,
  which is how architectures acquire assumptions nobody chose.

**The most valuable near-term second source is the one already sitting unread in
the repositories measured so far**: `wa-b2b` has 135 markdown documents and 369
migrations, and `EQ-01` — *why does this system work this way?* — scores
`no-data` on both benchmarked systems. **A decision-record source would be a
second evidence source without needing anything new to exist.**

## Compliance

- No component consuming the Engineering Model refers to files, commits or
  repositories.
- A new evidence source is added by declaration, and proposes only the
  twenty-three entities.
- Provenance identifies the evidence source kind, not only a path.
