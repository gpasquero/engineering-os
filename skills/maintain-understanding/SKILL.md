---
name: maintain-understanding
description: Keep an engineering model current after code changes, and periodically challenge what it claims. Use after a commit or a feature lands in a repository that has an Engineering OS model, or when the user asks whether the model is still accurate, what has drifted, or what the model no longer reflects.
---

# Maintaining understanding

A model that is not maintained becomes folklore. Maintenance is incremental and
cheap — roughly **13–15 %** of the cost of re-deriving understanding each time.

```bash
eos maintain <before-repo> <after-repo> <project>
```

`<before-repo>` and `<after-repo>` are two checkouts — typically a detached
`git worktree` at the previous commit and the working tree. **Neither is
modified.**

Create the "before" state safely:

```bash
git -C <repo> worktree add --detach /tmp/before <commit>
```

## Locating the engine

Run this once per session, before anything else:

```bash
EOS="$(command -v eos 2>/dev/null || echo "${CLAUDE_SKILL_DIR}/../../bin/eos")"
"$EOS" --version
```

`eos` is on `PATH` whenever Engineering OS is loaded as a plugin. Otherwise it
ships beside this skill, and `${CLAUDE_SKILL_DIR}` points at this skill's own
directory. **Use `"$EOS"` wherever the commands below say `eos`** if the bare
name was not found.

## What it runs

1. **Continuous Acquisition** — only what changed is proposed, carrying the
   meaning the onboarding established.
2. **Periodic Reacquisition** — full discovery again, **to challenge the model,
   never to replace it. Nothing it produces is applied.**
3. **Knowledge Drift Report** — where the maintained model and a fresh look
   disagree.

Then:

```bash
eos drift <project>                              # the report as a work queue
eos drift <project> --plan=P-review-unsupported  # instantiate one plan
```

Fifteen drift classes, each routed to an engineering plan. Classes that route
nowhere say why.

## Two things it will not do

**Retractions are never applied.** An assertion whose evidence disappeared is a
*proposal* to remove it — the evidence may have moved. A human decides.

**Reacquisition never overwrites.** Its entire value is challenging the
maintained understanding; applying it would destroy the curation that makes the
model authoritative.

## Check that understanding survived

```bash
eos measure <project>
```

Compare against the previous reading. **A model that grew while answering fewer
questions has got worse**, however many assertions it gained — say so plainly
rather than reporting the growth.
