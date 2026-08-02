---
id: Evidence.TestInventory
type: Evidence
label: auth test suite inventory
attributes:
  source: packages/backend/src/modules/auth/__tests__/
  locator: "5 suites, 50 cases"
  kind: source-reference
  extracted: "2026-08-02"
  support: confirmed
relationships: []
---
grep -c 'it(' across the directory: 8 + 12 + 12 + 11 + 7 = 50 cases in 5 suites.
