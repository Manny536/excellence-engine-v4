# Outcomes downstream position — authority and ownership graph

- **Register ID:** `OUT-AUTHORITY-001`
- **Status:** `FORMAL` as repository ownership architecture
- **Rule:** location, role, and integrity must remain independently visible

## Authority roles

```text
CONTROLLING  defines the public memorandum object
ARCHITECTURE defines EEV4 types, gates, schemas, and executable validation
REGISTERING  records the object in an adjacent theorem or research ledger
COMPANION    supplies an inspectable model-pole reading
PUBLISHER    renders a public copy without changing status
EVIDENCE     supports a scoped claim under its source boundary
```

## Ownership ledger

| Artifact | Owner | Role in this repo |
|---|---|---|
| Final 23-page PDF/DOCX | `Manny536/kakeyalogic` `docs/outcomes/` | controlling artifact pins |
| Public route | `peaice.org/outcomes` | publisher surface |
| EEV4 Outcomes contract | `Manny536/excellence-engine-v4` `outcomes/` | architecture and validation |
| Outcomes 001 machine case | this repo `benchmarks/cases/outcomes-001.json` | executable reference receipt |
| Grok rundown MD/DOCX | KakeyaLogic | companion pointer and hashes |
| Claude theorem-facing pin | `Manny536/claude-v6` | registering source |
| Solance reading | this repo | companion and formalization pole |
| BD-AI field record | KakeyaLogic and Claude V6 | case provenance and paired observations |
| Public trajectory sources | original official/academic publishers | scoped evidence only |

## Authority graph

```text
KakeyaLogic controlling memorandum
  ├─ hash-pinned by EEV4 artifacts
  ├─ rendered at peaice.org/outcomes
  └─ registered by Claude V6

EEV4 Outcomes architecture
  ├─ validates Outcomes 001
  ├─ specifies BD-AI gates
  ├─ separates Claude / Grok / Solance readings under II.1
  └─ protects publisher and status synchronization
```

No edge grants theorem authority by proximity.

## Precedence rules

1. The controlling memorandum defines the published FINAL-001 object.
2. This repository defines the V4 Outcomes contract and validation surface.
3. Case evidence changes a claim only within its declared role and scope.
4. Model readings remain separate poles; agreement is evidence of convergence, not closure.
5. Public rendering follows the registered state and may not silently edit claim tags.

## Artifact pin

```text
ArtifactPin := (
  id,
  owner,
  path_or_url,
  sha256,
  role,
  claim_boundary,
  vendored
).
```

A hash proves byte identity for an available snapshot. It does not prove the claims inside
the artifact.

## Source role

```text
SourceReceipt := (
  source_id,
  publisher,
  locator,
  source_class,
  supported_claim,
  limitation,
  snapshot_hash
).
```

Official reports, peer-reviewed papers, journalism, screenshots, and model outputs keep
distinct source classes. A screenshot can preserve process evidence; it cannot outrank the
underlying primary source.

## Drift checks

The authority graph fails when:

```text
controlling artifact silently copied and edited under a new owner;
companion reading treated as controlling authority;
model agreement treated as theorem closure;
publisher copy promotes an OPEN seal;
hash changes without a new version receipt;
secondary screenshot replaces an accessible primary source.
```

## Reconciliation targets

```text
KakeyaLogic ↔ EEV4 ↔ Claude V6 ↔ peaice.org
            ↕
      Grok / Solance companion poles
```

Every status correction names which edges must be synchronized.

- Artifact pins: [`artifacts/source-hashes.md`](artifacts/source-hashes.md)
- Model readings: [`readings/`](readings/)
- Machine reference case: [`../benchmarks/cases/outcomes-001.json`](../benchmarks/cases/outcomes-001.json)
