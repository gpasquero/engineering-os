---
id: ADR-0148
title: Engineering OS is installed as a Claude Code plugin and depends on nothing
status: accepted
date: 2026-08-03
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0135, ADR-0140, ADR-0141, ADR-0143, ADR-0145, ADR-0147]
---

# ADR-0148 — Installed as a plugin, depending on nothing

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

**Engineering OS is a Claude Code plugin, and it depends on nothing.**

```
/plugin marketplace add gpasquero/engineering-os
/plugin install engineering-os@engineering-os
```

Three properties make that the whole installation.

**1. Zero dependencies.** A pure-Python PyYAML is vendored in `vendor/`. The
plugin system has **no dependency-installation step**, so a product that needed
one could not be a plugin at all. **An installed PyYAML always wins** — `vendor/`
is only reached when nothing else provides it.

**2. One entry point.** `bin/eos` — and `bin/` is added to `PATH` when the
plugin is enabled, so every documented command runs verbatim. It dispatches to
the existing tools and redesigns none of them.

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

**Codex has no plugin mechanism**, and the README says so rather than implying
parity. `eos` is a dependency-free script, so the honest instruction is a clone
onto `PATH` plus pasting a skill into `AGENTS.md`. **The skills name no vendor**
(`ADR-0113`), so the contract is identical whichever model reads it.

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
