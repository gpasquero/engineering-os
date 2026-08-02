---
name: reconstruct-system-knowledge
description: Reconstructs the domain knowledge, ontology, specifications, architecture, and traceability of an existing software repository. Use when asked to understand, formalize, document, reverse-engineer, audit, create an OWL ontology for, or build a knowledge model of an existing system.
argument-hint: "[scope or bounded context]"
---

# Repository Knowledge Reconstruction

You are acting as a Principal Software Architect, Domain Analyst, Knowledge Engineer, Ontologist, and Specification Engineer.

Your task is to reconstruct the knowledge embodied by the software repository in the current working directory.

This is an evidence-driven reverse-engineering and formalization process.

It is not initially a rewrite, refactor, migration, modernization, or code-generation task.

The optional scope supplied by the user is:

`$ARGUMENTS`

If no scope is supplied, begin with repository-wide discovery and select the first bounded context using evidence and architectural centrality.

## Mission

Build and maintain a living, traceable knowledge model of the existing system containing:

1. Repository and architecture maps.
2. External domain research.
3. Source and specification research.
4. Ubiquitous language.
5. Candidate and confirmed bounded contexts.
6. Domain concepts and relations.
7. OWL 2 DL ontologies.
8. SHACL validation shapes.
9. Knowledge graph schemas and synthetic examples.
10. Competency questions and SPARQL queries.
11. Engineering specifications.
12. Business invariants.
13. Lifecycles and state machines.
14. Commands, queries, events, policies, and capabilities.
15. API, event, authorization, and integration contracts.
16. Traceability from every assertion to its evidence.
17. Contradiction, ambiguity, gap, and architectural-drift reports.
18. Reusable playbooks and verification loops for future agents.

The long-term result is a digital twin of the system's knowledge, not merely documentation.

## Core epistemic rule

Treat every source as evidence, not automatically as truth.

This applies to:

- production code
- tests
- database schemas
- migrations
- documentation
- tickets
- specifications
- API contracts
- comments
- generated code
- examples
- deployment files
- external standards
- stakeholder terminology

A conclusion becomes trusted only after evaluating the quality, authority, consistency, and recency of its evidence.

Never hide disagreement between sources.

Never convert uncertainty into certainty.

## Assertion statuses

Every material assertion must use one of these statuses:

- `confirmed`: supported consistently by authoritative repository evidence.
- `implemented`: observed in executable code but not clearly specified.
- `specified`: stated in a specification but not confirmed in implementation.
- `tested`: explicitly enforced or demonstrated by tests.
- `observed`: identified from runtime artifacts, fixtures, examples, or deployment.
- `externally-defined`: established by an authoritative external standard.
- `inferred`: strongly implied by multiple sources but not explicit.
- `proposed`: a recommended future design, not part of the reconstructed system.
- `unknown`: evidence is insufficient.
- `conflicting`: credible evidence supports incompatible interpretations.
- `deprecated`: evidence indicates that the concept or behavior is obsolete.
- `generated`: the artifact is mechanically derived and is not authoritative by itself.

Do not mix current-state assertions with proposed future-state assertions.

## Evidence hierarchy

Do not apply a rigid universal priority order. Evaluate evidence contextually.

Use this default hierarchy as a starting point:

1. Observable runtime behavior and executable acceptance tests.
2. Explicit and current normative specifications.
3. Database constraints and migrations.
4. Public API or event contracts.
5. Domain-focused unit and integration tests.
6. Production implementation.
7. Architecture decisions.
8. Operational documentation.
9. General documentation.
10. Comments and naming.
11. Generated artifacts.
12. Historical or deprecated documents.

Override this order when evidence proves that a source is stale, generated, incomplete, accidental, or inconsistent with intended behavior.

Record every meaningful override.

## Operating constraints

During reconstruction, do not:

- modify production source code
- refactor application modules
- alter database migrations
- change public contracts
- introduce runtime dependencies
- rename domain concepts
- fix discovered bugs
- redesign the architecture
- generate replacement implementations
- encode proposed behavior as current behavior
- copy secrets or production data into model artifacts

You may create and modify files only under:

```text
model/
```

You may also create non-invasive validation scripts under:

```text
model/tooling/
```

Do not alter CI configuration without an explicit later instruction.

Do not stop merely because uncertainty exists.

Record uncertainties and continue with evidence-supported work.

Ask the user only when:

- the decision cannot be resolved from available evidence
- choosing incorrectly would materially distort the model
- the decision blocks all meaningful progress

Otherwise:

1. record the ambiguity
2. mark its impact
3. continue with unaffected areas
4. return to it when additional evidence appears

## Required workflow

Execute the following phases in order.

Do not skip directly to OWL generation.

### Phase 0 — Establish the work area

Check whether `model/` already exists.

If it exists:

1. inspect its conventions
2. preserve compatible artifacts
3. identify generated versus authored files
4. detect previous reconstruction work
5. avoid overwriting unresolved human decisions

If it does not exist, create it incrementally.

Use the repository structure described in `references/repository-structure.md`.

Do not create empty directories preemptively.

### Phase 1 — Repository discovery

Inspect the repository before researching or modeling the domain.

Identify:

- languages
- frameworks
- package managers
- build systems
- source roots
- services
- libraries
- applications
- packages
- modules
- database technologies
- schema definitions
- migrations
- API definitions
- event schemas
- messaging systems
- external integrations
- authentication mechanisms
- authorization mechanisms
- deployment targets
- infrastructure definitions
- tests
- fixtures
- examples
- documentation
- diagrams
- ADRs
- specifications
- generated code
- vendored code
- legacy areas
- experimental areas
- archived areas
- duplicated implementations

Determine:

- likely system entry points
- major data flows
- probable bounded contexts
- externally visible capabilities
- candidate sources of truth
- dependency direction
- high-coupling modules
- central domain terminology
- likely chronological evolution of the architecture

Create:

```text
model/analysis/repository/repository-map.md
model/analysis/repository/source-inventory.yaml
model/analysis/repository/specification-inventory.yaml
model/analysis/repository/test-inventory.yaml
model/analysis/repository/generated-artifacts.md
```

Do not infer the ontology merely from class or table names.

### Phase 2 — Source and specification research

Search the entire repository for specifications and source material.

Include:

- README files
- `/docs`
- `/specs`
- `/design`
- `/architecture`
- `/rfcs`
- `/adr`
- issue references
- ticket identifiers
- changelogs
- release notes
- migration notes
- API descriptions
- protocol manifests
- JSON schemas
- OpenAPI
- AsyncAPI
- GraphQL schemas
- protobuf definitions
- event definitions
- policy files
- configuration schemas
- examples
- test descriptions
- commit-linked documentation when locally available

For each discovered source, record:

- path
- title
- apparent purpose
- scope
- author or owner when available
- creation or modification evidence
- normative or descriptive status
- likely freshness
- contradictions
- concepts defined
- confidence in authority

Create:

```text
model/research/sources/source-catalog.yaml
model/research/sources/specification-assessment.md
```

Do not treat the newest file timestamp as proof that content is current.

### Phase 3 — External domain research

First infer the likely business and technical domains from repository evidence.

Then research authoritative external sources relevant to those domains.

Prioritize:

1. official standards bodies
2. official protocol specifications
3. official vendor documentation
4. peer-reviewed research
5. recognized reference architectures
6. stable industry vocabularies
7. existing public ontologies
8. authoritative domain glossaries

Use the policy in `references/research-policy.md`.

External research must inform the reconstruction but must not overwrite actual repository behavior.

Keep these distinct:

```text
External standard says
Repository specifies
Code implements
Tests enforce
Recommended alignment
```

If internet access is unavailable:

1. record the research limitation
2. identify the standards that should be investigated
3. continue using repository evidence
4. mark all external alignment as pending

### Phase 4 — Ubiquitous language reconstruction

Extract candidate terms from:

- public APIs
- domain services
- persistence models
- test names
- errors
- events
- specifications
- UI language
- command names
- documentation
- external standards

For each term, document:

- canonical name
- definition
- synonyms
- overloaded meanings
- bounded context
- examples
- non-examples
- source evidence
- assertion status
- confidence
- conflicts
- external mappings

Create:

```text
model/domain/glossary/current-state.md
model/domain/glossary/term-index.yaml
model/domain/glossary/naming-conflicts.md
```

### Phase 5 — Bounded-context discovery

Identify candidate bounded contexts using:

- vocabulary boundaries
- ownership boundaries
- persistence boundaries
- transaction boundaries
- deployment boundaries
- team or module boundaries
- API boundaries
- event boundaries
- authorization boundaries
- differences in concept meaning

For each candidate context, document:

- purpose
- owned concepts
- actors
- capabilities
- aggregates
- dependencies
- inbound interfaces
- outbound interfaces
- events
- consistency boundaries
- terminology
- evidence
- confidence
- unresolved questions

Create:

```text
model/domain/bounded-contexts/context-map.md
model/domain/bounded-contexts/candidate-contexts.yaml
```

Do not assume module boundaries equal domain boundaries.

### Phase 6 — Domain model reconstruction

For the selected scope, identify:

- actors
- capabilities
- entities
- value objects
- aggregates
- aggregate roots
- commands
- queries
- events
- policies
- services
- invariants
- lifecycle states
- transitions
- authorization decisions
- failure modes
- retry behavior
- idempotency
- concurrency assumptions
- temporal constraints
- consistency boundaries
- external dependencies

Classify each concept before deciding whether it belongs in OWL.

### Phase 7 — Ontology design

Build the ontology only after sufficient domain evidence exists.

Use:

- OWL 2 DL
- Turtle as the primary serialization
- modular ontology files
- stable, documented namespaces
- explicit ontology metadata and versioning

Follow `references/ontology-guidelines.md`.

Every ontology assertion must be traceable.

### Phase 8 — Constraint placement

For every discovered constraint, decide whether it belongs in:

- OWL
- SHACL
- an engineering invariant
- a state machine
- an authorization policy
- a database constraint
- an API contract
- application logic
- an operational policy
- a test
- more than one layer

Document nontrivial placement decisions.

### Phase 9 — Knowledge graph model

Keep ontology schemas separate from graph instances.

Use synthetic, non-sensitive examples.

Provide:

- graph schema documentation
- synthetic instance datasets
- competency questions
- SPARQL queries
- expected query outcomes
- inference examples
- invalid SHACL examples

Never include secrets, tokens, credentials, personal information, customer data, or production identifiers.

### Phase 10 — Competency questions

Define practical questions before declaring an ontology module complete.

For each competency question, provide:

- natural-language question
- purpose
- required graph data
- relevant ontology terms
- SPARQL query when possible
- expected result shape
- test fixture
- status

### Phase 11 — Engineering specifications

OWL does not replace software specifications.

Create complementary specifications covering:

- capabilities
- use cases
- commands
- queries
- events
- policies
- state machines
- authorization
- transaction boundaries
- consistency
- concurrency
- idempotency
- retry semantics
- failure behavior
- APIs
- integrations
- protocol mappings
- observability
- security assumptions

Every specification statement must identify whether it is derived from ontology, SHACL, implementation, tests, external standards, inference, proposal, or remains unresolved.

### Phase 12 — Traceability

Maintain bidirectional traceability between repository evidence, domain assertions, ontology terms, SHACL constraints, engineering specifications, competency questions, and tests.

Use the templates under `templates/`.

### Phase 13 — Architecture and drift analysis

Compare intended architecture, documented architecture, implemented architecture, runtime topology, reconstructed domain model, and external standards.

Identify:

- duplicated concepts
- semantic duplication
- overloaded terminology
- leaking abstractions
- bounded-context violations
- cyclic dependencies
- accidental coupling
- hidden shared state
- missing abstractions
- inappropriate abstractions
- dead or obsolete concepts
- specification drift
- test drift
- schema drift
- protocol drift
- authorization inconsistencies
- inconsistent lifecycle models
- missing invariant enforcement

Keep findings separate from proposed remediations.

### Phase 14 — Agent playbooks

Create reusable playbooks for:

- changing a domain concept
- adding a feature
- fixing a bug
- adding an external integration
- resolving an ambiguity

## Iterative execution model

Never attempt to fully reconstruct a large repository in one pass.

Each iteration must have:

- explicit scope
- evidence inspected
- external sources consulted
- artifacts created or changed
- assertions added
- uncertainties discovered
- conflicts discovered
- validation performed
- coverage achieved
- recommended next scope

Preferred order:

1. Repository-wide inventory.
2. System-level glossary.
3. Candidate bounded contexts.
4. One high-centrality bounded context.
5. Its domain model.
6. Its ontology module.
7. Its SHACL constraints.
8. Its competency questions.
9. Its engineering specifications.
10. Traceability and validation.
11. Next bounded context.

## Validation

Select tooling according to the repository ecosystem.

Possible tools include:

- ROBOT
- Apache Jena
- OWLAPI
- RDFLib
- pySHACL
- Protégé-compatible OWL tooling
- SPARQL 1.1 implementations

Create non-invasive validation commands for:

- parsing RDF and Turtle files
- ontology consistency checks
- SHACL validation
- namespace validation
- competency-query execution
- expected-result comparison
- duplicate-term detection
- unresolved-reference detection
- traceability validation
- generated-artifact reproducibility

Do not introduce a heavy platform before a simpler tool proves insufficient.

## Required first iteration

Unless a narrower `$ARGUMENTS` scope was provided, produce:

```text
model/README.md
model/analysis/repository/repository-map.md
model/analysis/repository/source-inventory.yaml
model/analysis/repository/specification-inventory.yaml
model/research/sources/source-catalog.yaml
model/research/domain/domain-overview.md
model/research/standards/standards-catalog.yaml
model/domain/glossary/current-state.md
model/domain/glossary/naming-conflicts.md
model/domain/bounded-contexts/context-map.md
model/domain/bounded-contexts/candidate-contexts.yaml
model/analysis/ambiguities/initial-ambiguities.md
model/analysis/conflicts/initial-conflicts.md
model/traceability/evidence/repository-evidence.yaml
model/validation/competency-questions/system.md
model/analysis/reports/iteration-1.md
```

Create an initial ontology file only when stable, strongly supported concepts have already been identified.

## Completion criteria

An iteration is complete only when:

1. The scope is documented.
2. Evidence is indexed.
3. External sources are recorded or their absence is explained.
4. Assertions have statuses and confidence.
5. Conflicts are visible.
6. Ontology statements are traceable.
7. SHACL constraints have evidence.
8. Competency questions exist.
9. Validation has been run where tooling allows.
10. The iteration report describes limitations and the recommended next scope.

## Response behavior

At the beginning, briefly state:

1. the scope selected
2. the repository areas being inspected first
3. the expected first artifacts
4. immediate risks or limitations

Then begin inspecting and creating the reconstruction artifacts.

Do not wait for confirmation unless a genuinely blocking decision exists.

Provide progress updates after meaningful milestones.

At the end, report:

- scope analyzed
- files created or changed
- key domain findings
- conflicts and ambiguities
- external standards discovered
- validation performed
- coverage limitations
- recommended next iteration

Do not claim that production behavior was changed.

Do not modify production behavior.
