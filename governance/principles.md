---
id: PRINCIPLES
title: Principles
status: accepted
created: 2026-08-02
updated: 2026-08-02
source: [AGENTS.md, sources/handoff/DECISIONS.md]
---

# Principles

Non-negotiable rules. A change that violates one of these is wrong even if it
otherwise works. Changing a principle requires an ADR.

## Knowledge

1. **Knowledge is a first-class artifact.** It is produced, reviewed and
   versioned like code.
2. **Code is one output of engineering**, not the goal of it.
3. **Knowledge update is part of Done.** A change is incomplete until the model
   reflects it.
4. **The repository is the memory.** Knowledge that lives only in a
   conversation is lost knowledge.

## Epistemics

5. **Every source is evidence, not truth.** Authority, consistency, recency and
   quality are evaluated before a source is trusted.
6. **Every important assertion must be traceable to evidence.**
7. **Never convert uncertainty into certainty.** Record the unknown and continue
   with what is supported.
8. **Never hide disagreement between sources.** Conflicts are recorded, not
   resolved by preference.
9. **Keep current state and proposed state separate.** Always, in every
   document.
10. **When information is missing, create an issue — do not assume.**

## Method

11. **Research before design.**
12. **Ontology before implementation when semantics change.**
13. **Mandatory impact analysis before implementation.**
14. **The smallest coherent change** that satisfies the model and the acceptance
    criteria.
15. **Never weaken a test to make an implementation pass.**

## Structure

16. **Skills are composable.** Every unit declares its inputs, outputs,
    preconditions and postconditions.
17. **Workflows orchestrate skills.** Workflows sequence; they do not contain
    methodology of their own.
18. **Shared policies instead of duplicated text.** Policy is referenced by
    path, never inlined into a skill.
19. **Everything is modular, versioned and reviewable.**
20. **Frozen inputs stay frozen.** `imports/` and `sources/` are never edited.

## Safety

21. **Never place secrets, credentials, personal data or production identifiers**
    into any artifact, including examples, fixtures and synthetic data.
22. **Never work directly on `main`.** Use `feat/*`, `fix/*` or `chore/*`.

## Process

23. **Never generate everything in one pass.** Work proceeds milestone by
    milestone, with the repository updated at the end of each session.
24. **Update the build state after every delivery.**
