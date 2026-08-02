# Benchmark — a Spring Boot business application

**Repository:** `wa-b2b` · Java 21 · Spring Boot · JPA · Maven
**Mechanical Model digest:** `960437b1101a4366` · Stack Profile `S-java-spring-jpa`
**Run:** `SESSION-0045` · Initial Acquisition only

This is a **benchmark, not a backlog** (`ADR-0119`). Nothing below was fixed
because it appeared here, except the two items marked **`correctness`**.

## Why this repository

Chosen for **engineering characteristics**, not for its language. It is the
reviewer's first-priority profile and it exercises five things `ai-desk` never
did: **layered architecture, declarative security, 193 test classes, 369 SQL
migrations, and a rich business domain** spread over 21 feature packages.

**Nothing about its design was known to this project.** That is enforced
structurally rather than by promise: Interpretive Discovery reads the Mechanical
Engineering Model **exclusively** (`ADR-0108`), and the Mechanical Model contains
only what the declared Stack Profile extracted.

## The product metric

**2 of 9 engineering questions answered — 22 %** (`ADR-0120`). Measured after
this report was first written, and it leads now because counts do not.

```text
wa-b2b     2/9   22%      453 nodes, 324 edges
ai-desk    3/9   33%       76 nodes,  78 edges
```

**The six-times-larger model understands less.** Everything below is the detail
behind that sentence.

## What was observed

| | `ai-desk` | `wa-b2b` |
|---|---|---|
| Files | 780 | 1 913 |
| Packages | 4 | 1 |
| Module directories | 28 | 21 |
| Routes | 161 | **143** |
| Tables | 34 | **45** |
| Test suites | 69 | **193** |
| Config references | 27 | 38 |
| Documents | 62 | **135** |
| **Proposals** | **299** | **453** |

**The interpreter was not changed to read Java.** A Stack Profile was declared
(`ADR-0117`); the six Discovery rules ran unmodified. That was the architectural
claim under test and it held.

---

## 1. Which metamodel entities were actually exercised?

**Five of twenty-three.**

| Entity | Count | From |
|---|---|---|
| `Artifact` | 236 | controllers, test classes |
| `Invariant` | 150 | rule-stating test methods |
| `Concept` | 45 | JPA entities |
| `Capability` | 21 | feature packages |
| `BoundedContext` | 1 | the Maven module |

**Not exercised — eighteen**, including `Actor`, `Evidence`, `Policy`,
`Workflow`, `EngineeringGate`, `StateMachineSpecification`, `Dimension`, and
**`ADR`**.

`ai-desk` exercised **six**. The extra one was `ADR`, and its absence here is the
single most consequential finding in this report.

**This is now repeated evidence** (`ADR-0119` rule 1): two repositories, two
stacks, and the same five entities. The limitation is **in the interpreter, not
in the repositories** — nothing in the six deterministic rules can propose an
`Actor` or a `Policy`, whatever it is pointed at.

## 2. Which Discovery Skills produced valuable engineering knowledge?

| Rule | Output | Judgement |
|---|---|---|
| `S1-module-is-a-capability` | 21 capabilities | **Valuable.** The 21 feature packages *are* the system's capability map, and it is one no document in the repository states |
| `S1-pgtable-is-a-concept` | 45 concepts | **Valuable.** The JPA entities are the domain vocabulary |
| `S2-controller-implements-module` | 43 controllers | **Valuable.** 143 routes attributed to capabilities |
| `S4-spec-validates-module` | 193 suites | **Valuable as coverage.** Every capability has tests, and which ones is now queryable |
| `R4-both-levels` | 150 invariants | **Mixed — see below** |

The strongest single result is unglamorous: **`voice` (38 files), `whatsapp`
(97 files) and `mcp` (34 files) are the three largest capabilities**, and the
model says so from structure alone, with provenance, in seconds.

## 3. Which Discovery Skills produced mostly noise?

**`R4-both-levels`, and the noise was manufactured by Engineering OS, not found
in the repository.**

`R4` proposes a general Invariant from a suite's declared subject, and specific
ones from its cases. **No `wa-b2b` test class declares a subject** — JUnit has no
`describe` block and this repository does not use `@DisplayName`.

`R4` fell back to the **file name**. The result was 67 proposals of this shape:

```
Invariant.AgentServiceTest        "AgentServiceTest"
Invariant.AuditDeciderTest        "AuditDeciderTest"
```

**67 assertions that assert nothing** — 13 % of the entire proposal set —
carrying full provenance and `S-inferred` support, indistinguishable to a
reviewer from a real finding.

**`correctness` — fixed.** This is fabrication, not fitting: it converts absence
into content and misreports support. `R4` now emits only case-level invariants
when no subject is declared, and marks them `grouping: none-declared`.

> **A fallback that supplies an identifier where a statement is missing does not
> improve coverage. It manufactures evidence.**

`ai-desk` could never have exposed this. **Every one of its 69 suites declares a
`describe` block**, so the branch never ran in fourteen milestones.

The fix is verifiably not an optimization for Java: **`ai-desk` still produces
exactly 299 proposals, unchanged.**

**Residual noise, not fixed.** The surviving 150 invariants are stated as Java
method identifiers — `addAsync_failsTheFuture_onHttpException`. They state real
rules, and they are not sentences. Recorded, not solved: one repository.

## 4. Which engineering questions could not be answered?

The 453 proposals were compiled into a CKM (453 nodes, 324 edges) **without
curation** — this measures the ceiling, not the product — and all 17 declared
queries were run against every eligible subject.

**Nine of seventeen answer nothing at all.**

| Query | Answers | Why |
|---|---|---|
| `Q-why` | 361/453 | — |
| `Q-provenance`, `Q-status` | all | — |
| `Q-dependents` | 174/281 | — |
| `Q-impact` | 82/453 | — |
| `Q-tests` | 17/453 | only controllers link to suites |
| **`Q-rationale`** | **0/216** | **no decision record exists in the model** |
| `Q-constraints` | 0 | see below |
| `Q-evidence`, `Q-specifications` | 0 | no `Evidence`, no specification artifacts |
| `Q-unenforced`, `Q-unaccepted` | 0 | no acceptance, no enforcement points |
| `Q-obsolete-decisions`, `Q-stale-implementation` | 0 | both need decisions |

**`Q-rationale` — *which decision established this?* — is the question the
metamodel most needs to answer, and it returns nothing for all 216 subjects.**
The repository has **135 markdown documents and zero that the profile recognises
as a decision record**: no `status`/`date` header, no `adr/` directory. The
knowledge exists in the repository. The model cannot see it.

**`Q-constraints` returns nothing as a direct consequence of the fix in §3.** The
fabricated general invariants were also the only thing emitting `constrains`
edges from Invariant to Capability. Removing the fabrication removed the only
link between a guarantee and the capability it guards.

**This is worth stating plainly: the noise was load-bearing.** 13 % fabricated
content was purchasing one real relationship, and the honest model is a
*less connected* model. The remedy is not to restore the fallback.

## 5. Which gaps appeared?

| Gap | Evidence |
|---|---|
| **Decisions are invisible unless filed as ADRs** | 135 documents, 0 recognised |
| **Security is entirely absent from the vocabulary** | `@PreAuthorize`, JWT, OIDC, 24 security files — **143 routes and not one carries who may call it** |
| **A repository may host several stacks** | Java backend + TypeScript frontend + Python service; detection returns one profile |
| **Migrations are unread** | 369 `.sql` files — the system's history of schema decisions, entirely unobserved |
| **Layering is unobserved** | Controller / Service / Repository is the repository's central architectural fact and nothing records it |
| **Invariants no longer reach capabilities** | §4 |

## 6. Did the metamodel require changes?

**No.**

Twenty-three entities, unchanged for thirteen milestones, absorbed a Java Spring
application on the first attempt with **zero additions and zero amendments**. A
JPA entity is a `Concept`; a feature package is a `Capability`; a controller is
an `Artifact` that `implements`; a test class is an `Artifact` that `validates`.

Every gap in §5 is a gap in **observation**, not in **representation**. An
authorization rule is an `Invariant`; a layer is a `Capability` or a
`BoundedContext`; a migration is an `ArtifactRevision`. **Nothing was missing
from the metamodel. Things were missing from what the profile looked at.**

## 7. Repository-caused, or missing concepts in Engineering OS?

**Engineering OS, in every case.**

- *Decisions invisible* — **Engineering OS.** `wa-b2b` documents decisions in
  prose. The profile only recognises one filing convention.
- *Security absent* — **Engineering OS.** The vocabulary has eight keys and none
  of them is about authorization.
- *Polyglot* — **Engineering OS.** One-profile-per-repository is our assumption.
- *Migrations unread* — **Engineering OS.**
- *Identifier-shaped invariants* — **shared.** JUnit offers `@DisplayName` and
  this repository does not use it; a skill that reads only test *names* is also
  reading the weakest available source.

**The distinction matters because the remedies differ.** A repository-caused gap
is reported to the team as a finding about their system. An Engineering-OS-caused
gap is our defect and must never be reported as theirs.

## 8. Which new reusable Discovery Skill would now be justified?

**Candidate: `DS-authorization-discovery`** — *who may invoke what, and what
happens when they may not.*

It is the highest-value gap: a business application's authorization model is
among the first things a new engineer must learn and among the last things any
document states correctly.

**It is not built, and `ADR-0119` is the reason.** One repository. The evidence
still outstanding is a second repository — ideally the event-driven service, where
authorization crosses a message boundary rather than an HTTP one — exposing the
same need. `ai-desk` had authentication tests but was never examined for an
authorization *model*, so it does not count as a second observation.

**Also short of evidence, recorded here so the second sighting is recognisable:**

- `DS-decision-archaeology` — recover decisions from prose documents and commit
  history, for the majority of repositories that never adopted ADRs.
- `DS-layering-discovery` — name the layering convention a repository actually
  follows.
- `DS-schema-history` — read migrations as the record of schema decisions.

## Corrections made during this run

| Change | Class | Justification |
|---|---|---|
| `R4` no longer names an invariant after a file | **`correctness`** | Fabricates evidence; `ai-desk` output unchanged at 299 |
| Maven `<parent>` excluded before reading `artifactId` | **`correctness`** | Named the repository after its framework's BOM |
| Base package found by application-class marker | fitting, **first profile** | Part of authoring `S-java-spring-jpa` |
| `venv`, `site-packages`, `__pycache__` skipped | **`correctness`** | 9 504 vendored files counted as repository content |

**No Discovery Skill was generalized. No metamodel entity was added.**

## Verdict against the product criterion

> *Did Engineering OS acquire useful engineering understanding that would make
> future development measurably easier?*

**Partly, and the honest answer is "less than the numbers suggest."**

**Yes:** a new engineer receives, in seconds and with provenance, the capability
map of a system whose 21 feature packages are documented nowhere; which
capability each of 143 routes belongs to; the 45-concept domain vocabulary; and
which capabilities are tested.

**No:** they learn nothing about **why** anything is the way it is — the question
they will actually ask on day one — and nothing about **who is allowed to do
what**, in a product whose reason for existing is multi-tenant B2B messaging.

**453 proposals, and the two questions a new engineer asks first are both
unanswerable.** That gap, not the count, is what the next repository must test.
