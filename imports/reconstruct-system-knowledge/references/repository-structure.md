# Target repository structure

Create directories only when they receive meaningful content.

```text
model/
├── README.md
├── research/
│   ├── domain/
│   ├── standards/
│   ├── sources/
│   └── reports/
├── analysis/
│   ├── repository/
│   ├── ambiguities/
│   ├── conflicts/
│   ├── gaps/
│   ├── drift/
│   ├── technical-debt/
│   └── reports/
├── domain/
│   ├── glossary/
│   ├── bounded-contexts/
│   ├── capabilities/
│   ├── actors/
│   ├── aggregates/
│   ├── entities/
│   ├── value-objects/
│   ├── invariants/
│   ├── lifecycles/
│   └── state-machines/
├── ontology/
│   ├── core/
│   ├── modules/
│   ├── alignments/
│   ├── vocabularies/
│   ├── imports/
│   └── deprecated/
├── validation/
│   ├── shacl/
│   ├── competency-questions/
│   ├── sparql/
│   └── reports/
├── graph/
│   ├── schema/
│   ├── examples/
│   ├── fixtures/
│   └── inferred/
├── engineering/
│   ├── contexts/
│   ├── commands/
│   ├── queries/
│   ├── events/
│   ├── policies/
│   ├── consistency/
│   └── failure-models/
├── specs/
│   ├── capabilities/
│   ├── use-cases/
│   ├── api/
│   ├── events/
│   ├── authorization/
│   ├── workflows/
│   └── integrations/
├── traceability/
│   ├── evidence/
│   ├── assertions/
│   ├── coverage/
│   └── provenance/
├── architecture/
│   ├── adr/
│   ├── diagrams/
│   ├── dependencies/
│   └── decisions/
├── playbooks/
├── loops/
├── prompts/
├── tooling/
└── generated/
```
