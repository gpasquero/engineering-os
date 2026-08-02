# Ontology guidelines

Use OWL 2 DL and Turtle.

Model semantics, not source-code structure.

## Prefer OWL for

- taxonomy
- semantic classification
- equivalence
- disjointness
- inverse relationships
- logically inferable restrictions
- stable domain meaning

## Prefer SHACL for

- required properties
- exact validation cardinality
- datatype constraints
- allowed values
- closed shapes
- graph consistency reports
- validation of instance data

## Prefer engineering specifications for

- workflows
- state transitions
- retries
- idempotency
- authorization decisions
- side effects
- temporal behavior
- operational failure handling

## Modeling rules

- Do not turn every class or table into `owl:Class`.
- Do not turn every foreign key into `owl:ObjectProperty`.
- Do not encode uncertain business rules as axioms.
- Avoid broad global `rdfs:domain` and `rdfs:range` declarations when they create unintended inferences.
- Prefer modular ontologies.
- Use stable namespaces and ontology version metadata.
- Use external ontology terms only when semantics genuinely match.
- Use SKOS mappings for approximate correspondence.
- Maintain provenance and traceability for every material assertion.
