# reconstruct-system-knowledge

Claude Code skill for reconstructing the domain model, ontology, knowledge graph, specifications, architecture, and traceability of an existing software repository.

## Install globally

Copy this directory to:

```text
~/.claude/skills/reconstruct-system-knowledge/
```

## Install in one repository

Copy it to:

```text
.claude/skills/reconstruct-system-knowledge/
```

## Run

From the repository root:

```text
/reconstruct-system-knowledge
```

Optional scoped execution:

```text
/reconstruct-system-knowledge authentication and authorization
```

or:

```text
/reconstruct-system-knowledge repository-wide discovery only
```

The skill is intentionally read-only for production code during reconstruction. It creates artifacts under `model/`.
