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
INSTRUMENT   executes a bounded evaluation and emits a custody receipt
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
| Meta Thinking Machine V4 | this repo `docs/meta/` and `site/artifacts/meta/` | companion instrument and used-energy custody receipt |

## Registered downstream companion — Meta V4

| Field | Registration |
|---|---|
| Designation | `PEAICE-V4-META-COMPANION-FINAL-001` |
| Source receipt | merged [PR #6](https://github.com/Manny536/excellence-engine-v4/pull/6) · commit `f74715c0f32f2ade49ddf3f5d36fbbe6adf41d57` |
| Role | `COMPANION` + `INSTRUMENT` |
| Interactive surface | [Wired Telemetry HTML](../docs/meta/PeAIce-Thinking-Machine-V4-Wired-Telemetry.html) |
| Companion surface | [FINAL Markdown](../docs/meta/PeAIce_V4_Meta_Thinking_Machine_Companion_FINAL.md) · [FINAL DOCX](../docs/meta/PeAIce_V4_Meta_Thinking_Machine_Companion_FINAL.docx) |
| Site mirror | [public artifact path](../site/artifacts/meta/thinking-machine-v4-wired-telemetry.html) |
| Integrity pins | HTML `da18b5ea8a7919e8b031976898506cc69f8a5cfa63dbb5b2a561fd20ebcfbc51` · DOCX `69dcc2843a5bd80a44ad715d61b5ff7c27a1595bce0745eafe66562b77c33423` |
| Source state | companion `FINAL-PUBLIC-RESEARCH` · instrument `REGISTERED` |
| Open seals | RH `OPEN` · Coleman `OPEN` · CP-004 `OWED` |

The registered outcome trace is:

```text
Question   Meta receives the typed V4 research object.
Attempt    The interactive executes HELD, KNS(LB), L²_C, firewall, and Outcomes surfaces.
Receipt    Used energy is recorded as a custody receipt with real HTML captures and artifact hashes.
Correction Authoritative captures remain separate from Appendix Z synthetic, non-authoritative plates.
Status     The companion is final public research; the instrument is registered; OPEN seals persist.
Next burden Independent receipts remain required for CP-004 and every theorem-facing lift.
```

This registration is limited to the downstream evidence and instrument map. Every
theorem-facing truth state remains unchanged.

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
