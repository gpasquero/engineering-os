# Impact analysis checklist

Before implementation:

- [ ] Request classified.
- [ ] Governing bounded context identified.
- [ ] Affected concepts identified.
- [ ] Current and intended behavior documented.
- [ ] Ontology impact reviewed.
- [ ] Invariant impact reviewed.
- [ ] API and event consumers identified.
- [ ] Data migration impact reviewed.
- [ ] Direct and transitive dependencies reviewed.
- [ ] Authorization and security impact reviewed.
- [ ] Operational impact reviewed.
- [ ] Test impact reviewed.
- [ ] Compatibility reviewed.
- [ ] Rollout and rollback defined.
- [ ] Risks assessed.
- [ ] Gate decision recorded.

After implementation:

- [ ] Focused tests pass.
- [ ] Regression tests pass.
- [ ] Contract tests pass.
- [ ] Ontology remains consistent.
- [ ] SHACL validation passes.
- [ ] No unexpected data migration occurred.
- [ ] No authorization scope was unintentionally broadened.
- [ ] Observability covers new behavior.
- [ ] Impact analysis was re-run.
- [ ] Traceability was updated.
