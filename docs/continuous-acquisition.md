# Continuous acquisition

**Purpose.** After a commit lands, *maintain* the engineering model instead of
rebuilding it — proposing only what changed, and proposing it with the same
meaning the onboarding established.

Initial onboarding is expensive on purpose. Continuous acquisition is what makes
that expense pay: on the ten-commit benchmark, maintaining the model cost
**13–15 %** of re-deriving it each time.

---

## The five stages, end to end

**Command**

```bash
python tools/lifecycle.py <before-repo> <after-repo> <project>
```

`<before-repo>` and `<after-repo>` are two checkouts of the same system —
typically a detached `git worktree` at the previous commit and your working
tree. **Neither is modified.** Everything is written into `<project>`.

**What happens**

| Stage | What it does |
|---|---|
| 1 · Initial Acquisition | Mechanical extraction over `<before-repo>`, interpretation with `both-levels`, authorization, and application into `<project>/model/` |
| 2 · Engineering change | Mechanical extraction over `<after-repo>` and a delta: suites, tables, modules, routes, dependencies added, removed and changed |
| 3 · Continuous Acquisition | **only what changed** is proposed, authorized and applied. Retractions are computed and **never applied** |
| 4 · Periodic Reacquisition | full discovery again over `<after-repo>`, written to `candidate-reacquisition.json` and **not applied** |
| 5 · Knowledge Drift Report | the maintained model is compared against that fresh candidate |

**Expected result**

```text
2  ENGINEERING CHANGE  (real, from git history)
   9b80ba2e41c0cd65 → 9d0a7ec1b2c0c82b
   suites     +1 -0 ~0
   modules    +1 -0 ~0
   routes     +1 -0 ~0

3  CONTINUOUS ACQUISITION
   proposed incrementally  3 entities
   retractions (governed)  0
   authorized and applied  3 entities
   maintained model        5 sources

4  PERIODIC REACQUISITION
   full discovery again    18 entities
   NOT applied — reacquisition challenges, it does not replace

5  KNOWLEDGE DRIFT REPORT
   maintained model        5 nodes
   fresh candidate         18 proposals
   D-implementation-without-knowledge     8
   D-invariant-without-enforcement        1
   D-new-knowledge                        5
```

**Output location**, all in `<project>/`:

| File | What it is |
|---|---|
| `model/*.md` | the maintained authoritative model, extended in place |
| `candidate-initial.json` | what initial acquisition proposed |
| `candidate-continuous.json` | what the change proposed incrementally |
| `candidate-reacquisition.json` | what a fresh full discovery proposed — never applied |
| `knowledge-drift-report.json` | the challenge, itemised by drift class |

---

## Two things you must know before running it

**Stage 5 needs a compiled model.** The drift report compares the *compiled*
maintained model against the fresh candidate, so on a brand-new project the
first run stops after stage 4:

```text
5  KNOWLEDGE DRIFT REPORT
   compile the project first: python3 tools/compile.py <project>
```

Exit code 1. Compile, then run `lifecycle.py` again:

```bash
python tools/compile.py <project>
python tools/lifecycle.py <before-repo> <after-repo> <project>
```

**The authorization filter is hard-coded.** `tools/lifecycle.py` simulates a
curation policy with a fixed list of id fragments — `Auth`, `Jwt`,
`RefreshToken`, `Lockout`, `Password`, `Sla`, `BusinessHours`,
`TenantIsolation`, `Rls`, `Ticket`, plus `ADR.0001` and `BoundedContext.Backend`.
On a repository whose vocabulary does not overlap that list, stage 1 will
authorize very few entities or none. This tool is a demonstration of the
lifecycle, not a curation front end. **Real authorization is
[curation](curation.md)**, and `tools/lifecycle.py` does not replace it.

---

## Did understanding survive?

```bash
python tools/measure.py <project>
```

Coverage against the nine Engineering Questions, recomputed from the current
sources.

```bash
python tools/guidance.py <project-before> <project-after>
```

Guidance Preservation — whether the same work is still recommended. See
[engineering guidance](engineering-guidance.md).

---

## The frozen longitudinal benchmark

**Purpose.** Acquire a model once, then force it to survive a real sequence of
commits, and measure what it can still answer at the end.

```bash
python tools/longitudinal.py <repo> <project> <commit> [<commit> ...]
```

`<repo>` must be a git repository. Each commit is materialised as a **detached
worktree at `/tmp/eos-longitudinal`**; the repository is never modified. The
first commit is the initial acquisition; every later commit is a mechanical
delta followed by continuous acquisition. Every four steps, and always on the
last, it runs a periodic reacquisition and a drift report.

**Expected result**

```text
   step  kind          cost  rerun      %  answered
   t0    initial         15      —      —  1/9
   t1    continuous       2     17  11.8%  1/9
   t2    continuous       1     18   5.6%  1/9

   Knowledge Growth         1 → 2 curated sources
   Understanding Growth     1/9 → 1/9 questions answered
   Understanding Retention  100%   of 1 answered at t0: 1 retained, 0 degraded, 0 lost; 0 gained
   Guidance Preservation    —      0 pairs over 1 untouched subjects
   acquired once at 15 proposals; maintained across 2 changes at 3 more (20% of one acquisition)
   engineering questions: 1/9 → 1/9   understanding held
```

**Output location** `<project>/longitudinal.json` — the timeline, retention and
guidance figures. `<project>/model/` is **deleted and rebuilt on every run**;
nothing else in the project directory is removed.

Two cautions, both real:

- **The curation policy is hard-coded** here too (`Auth`, `Jwt`,
  `RefreshToken`, `Lockout`, `Password`, `Sla`, `BusinessHours`,
  `TenantIsolation`, `Rls`, `Ticket`, `Inbox`, `Contact`, `Company`,
  `Attachment`, `Email`, `Csat`). It is applied identically at every step so
  that the measurement is about the tool and not about a drifting reviewer — but
  on an unrelated repository it will accept almost nothing.
- **The verdict is not read off coverage alone.** Coverage can stay flat while
  every question that was answered at `t0` is lost and a different one gained,
  so retention is reported separately and dominates the verdict.

---

## Failure modes

| Symptom | Exit | Cause and fix |
|---|---|---|
| `compile the project first: python3 tools/compile.py <project>` | 1 | stages 1–4 completed; compile and re-run to get the drift report |
| `no Stack Profile matches …` | 1 | one of the two checkouts is not a supported stack |
| `worktree <commit>: …` | 1 | `<repo>` is not a git repository, or the commit does not exist |
| stage 1 authorizes 0 entities | 0 | the hard-coded acceptance filter matched nothing in your repository. Use [curation](curation.md) instead |
| `python tools/lifecycle.py --help` prints usage | 2 | the tool takes exactly three positional arguments and has no flags |
