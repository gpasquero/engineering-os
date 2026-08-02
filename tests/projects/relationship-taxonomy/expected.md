---
id: TEST-relationship-taxonomy
exercises: Relationship taxonomy — all four categories in one project
outcome: pass
expected-nodes: 11
expected-edges: 9
expected-categories: [structural, behavioral, semantic, traceability]
---
Every core relationship category must appear, so a change to the vocabulary that
drops a category fails here rather than silently.

**This project failed on its first run.** It claimed all four categories and had
no `semantic` edge — `has-position` is a datatype property, not an edge. The
suite caught it immediately, which is the argument for negative and positive
expectations being declared rather than inferred from whatever the compiler
happens to produce.
