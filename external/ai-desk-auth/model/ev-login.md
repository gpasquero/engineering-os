---
id: Evidence.LoginSignature
type: Evidence
label: auth.service.ts login signature
attributes:
  source: packages/backend/src/modules/auth/auth.service.ts
  locator: "line 31"
  kind: source-reference
  extracted: "2026-08-02"
  support: confirmed
relationships: []
---
grep -nE 'async login'. Signature (email, password, workspaceSlug) shows the
tenant is resolved by slug, not carried.
