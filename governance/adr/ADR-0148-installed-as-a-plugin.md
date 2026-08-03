---
id: ADR-0148
title: Skills are the unit; the plugin manifest is a shipping label, and both ship
status: accepted
date: 2026-08-03
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0135, ADR-0140, ADR-0141, ADR-0143, ADR-0145, ADR-0147]
---

# ADR-0148 — Skills are the unit, and the manifest ships beside them

## Context

`SESSION-0052` produced a README whose installation section began with `git
clone`, `python3 -m venv`, `source .venv/bin/activate` and `pip install`. The
reviewer rejected it:

> **Queda muy incómodo la forma de instalar y ejecutar.** Debería ser todo un
> skill que pueda instalar en Claude o Codex y poder invocar para el brownfield
> y para el resto de las cosas. **No quiero que tengan que clonar el repo.**

The objection is not about convenience. **The product's own workers are Claude
and Codex** (`ADR-0140`), and asking a user to leave that environment, clone a
repository and manage a virtual environment before they can use it puts the
whole friction of a development setup in front of a tool whose value is
answering a question.

`ADR-0147` exempts exactly this: a change that **directly blocks third-party
installation** is permitted under Research Freeze.

## Decision

**The default installation requires no clone, no terminal and no package
manager.** Two lines, typed inside Claude Code:

```
/plugin marketplace add gpasquero/engineering-os
/plugin install engineering-os@engineering-os
```

Claude Code fetches and caches the product; the user never runs `git`.

**The manifest is what makes every other shape work too.** A folder under a
skills directory that carries one is loaded automatically on the next session,
with no marketplace and no install step — so the same repository also works
dropped into `~/.claude/skills/` or a project's `.claude/skills/`, yielding the
same five namespaced skills and the same `bin/` on `PATH`.

## Skills are the unit

The reviewer asked three times, with increasing force, why a plugin was involved
at all — and the third time named what settled it:

> **Otra vez, ¿por qué plugin si esto se resuelve con skills?**
> **Si quiero en Codex, ¿cómo hago?**

**Codex has skills too**, at `~/.agents/skills/` and `.agents/skills/`, with the
same `SKILL.md` carrying `name` and `description`, and scripts bundled beside
it. So the portable unit is a **skill folder**, and a plugin manifest does
nothing there.

**Both ship, because they are the same folder:**

| File | Read by |
|---|---|
| `SKILL.md` at the root | Codex, and Claude Code as a plain skill |
| `skills/*/SKILL.md` | Claude Code's plugin loader — five namespaced skills |
| `.claude-plugin/` | the Claude marketplace, so nothing has to be cloned |
| `bin/eos` | all of them, and any shell |

**The manifest is a shipping label, not architecture.** Its only job is letting
a Claude Code user install without leaving the chat. Deleting it would cost that
and buy nothing; treating it as the product's shape cost three rounds of
confusion.

## Two wrong turns, recorded rather than quietly fixed

**First:** answering *"does it need a plugin?"* by making `git clone` the
primary instruction — which **reintroduced the exact friction rejected one
message earlier**: *no quiero que tengan que clonar el repo*.

**Second:** answering *"why plugin if skills solve this?"* by starting to delete
the plugin path, until the reviewer stopped it:

> **No borres la posibilidad de tenerlo como plugin para Claude, pero Codex no
> tiene, así que tenemos que tener empaquetado para skill, downloadable o como
> sea.**

**Both corrections were subtractive when the answer was additive.** A question
about mechanism was twice answered by removing a capability, when the right
response was to add the missing one and stop leading with the wrong vocabulary.
*"Must they clone?"* is a question about experience, and the experience governs
(`ADR-0141`).

Three properties make the installation possible at all.

**1. Zero dependencies.** A pure-Python PyYAML is vendored in `vendor/`. The
plugin system has **no dependency-installation step**, so a product that needed
one could not be a plugin at all. **An installed PyYAML always wins** — `vendor/`
is only reached when nothing else provides it.

**2. One entry point.** `bin/eos` — and `bin/` is added to `PATH` when the
skill folder is loaded, so every documented command runs verbatim. It dispatches
to the existing tools and redesigns none of them. Skills locate it through
`${CLAUDE_SKILL_DIR}` rather than assuming `PATH`, so they work in every
installation shape.

**3. Five skills, invoked in plain language.** `brownfield-onboarding`,
`engineering-questions`, `engineering-guidance`, `curate-proposals`,
`maintain-understanding`. The user asks *"onboard this repository"*; Claude
selects the skill.

## The worker is now inside the product

Before this decision the onboarding flow was: generate a briefing, **the user
pastes it into Claude**, the user saves the reply, the user feeds it back.

With the skill installed, **Claude Code is the worker** — it runs the
extraction, reads its own briefing, investigates within the evidence boundary,
writes proposals and ingests them. The manual round trip disappears.

**Nothing about the trust model changes, and that is the point.** The skill
document states the same contract the briefing does, and the same validation
gate rejects the same things: a numeric confidence, a source outside the
Mechanical Model, a missing counter-argument. **The worker proposes; a human
authorizes** (`ADR-0143`). Being invoked more conveniently does not grant it
authority.

## A project may not live inside the plugin

A plugin's root is a **cache directory replaced on every update**. A project
kept there would be destroyed by an upgrade.

So a relative project path now resolves against **the user's working
directory**, with the repository root as a fallback so `examples/tiny` still
works from a clone. `eos` no longer changes directory before dispatching.

This was found by running the flow from `/tmp` rather than from the checkout,
and it would have silently written a customer's engineering model into a cache.

## Consequences

**Contributor checks may be absent, and their absence is not a failure.**
Governance consistency and the 17 fixtures verify **this project's own** corpus
and suite. A trimmed installation — 1.8 MB against 11 MB for the full checkout —
ships neither, and `eos check` now reports them as not shipped rather than
failing. **An installation check must check the installation, not the author's
repository.**

**Nothing is ever cloned by a user.** Every documented install is either two
slash commands or one `curl` of a release tarball into the tool's skills
directory. The clone survives only for contributors, behind a fold.

**`ADR-0113` paid off three milestones later.** It required Discovery Skills to
be engine-independent and to name no model vendor, when there was exactly one
consumer. That is the only reason the same `SKILL.md` files work unchanged in
Codex.

**Vendoring is a maintenance obligation**, accepted deliberately. Writing a
small YAML subset parser was considered and rejected: this repository has
already lost two sessions to YAML edge cases, and a hand-rolled parser would
reintroduce that defect class where a silent misparse is most expensive.

**The clone path remains, for contributors**, and `requirements.txt` becomes an
optimisation rather than a requirement.

## Compliance

- The plugin installs and runs with no `pip`, no virtual environment and no
  network access.
- `vendor/` is appended to `sys.path`, never prepended.
- No project directory is created inside the product's own root.
- Skills state the proposal contract and name no model vendor.
