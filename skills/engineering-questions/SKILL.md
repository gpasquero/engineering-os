---
name: engineering-questions
description: Answer questions about a system from its engineering model with provenance — what breaks if this changes, what depends on it, which invariant protects this behaviour, which decision established it, what is unsupported. Use when the user asks about impact, dependencies, business rules, rationale or risk in a repository that has an Engineering OS model.
---

# Asking engineering questions

Every answer comes from the compiled model and **carries its provenance**, so
the follow-up — *how do you know?* — is always answerable.

```bash
eos ask <project> questions                    # what can be asked
eos ask <project> Q-impact Concept.Order       # ask one
eos ask <project> Q-impact Concept.Order --paths --json
```

## Choosing the question

| The user asks | Query |
|---|---|
| what breaks if I change this? | `Q-impact` |
| what depends on this? | `Q-dependents` |
| which invariant protects this? | `Q-constraints` |
| which decision established this, and does it still stand? | `Q-rationale` |
| where did this come from? | `Q-provenance` |
| which tests must change? | `Q-tests` |
| what does this model claim with no evidence? | `Q-unsupported` |
| which rules are enforced nowhere? | `Q-unenforced` |

`eos ask <project> questions` lists all of them with the subject types each
accepts.

## Read the status, not just the rows

| Status | It means | Say |
|---|---|---|
| `ok` | answered | give the rows **and their paths** |
| `empty` | the question applies and nothing matched | *"nothing does"* — a real answer |
| `not-applicable` | wrong subject type for this question | pick a different question or subject |

**`empty` and `not-applicable` are different findings and must not be blurred
together.** One is about the system; the other is about the question.

## When the model cannot answer

```bash
eos measure <project>
```

This reports how many of the registered engineering questions the model can
answer at all. A low score is a fact about the model's coverage — usually that
too little was curated, or that the knowledge exists in prose nobody has
onboarded yet.

**Say that, rather than filling the gap from the source code yourself.** An
answer you inferred by reading the repository is not in the model, has no
provenance, and will not be there next time. If it matters, propose it — use the
`brownfield-onboarding` skill.
