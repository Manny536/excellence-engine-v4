# Source hashes — Outcomes integrity receipts

- **Register ID:** `OUT-ARTIFACTS-001`
- **Rule:** a hash pins bytes; source role controls evidentiary use
- **Controlling artifact owner:** `Manny536/kakeyalogic` · `docs/outcomes/`

## Artifact-pin type

```text
ArtifactPin := (
  id,
  owner,
  locator,
  sha256,
  role,
  claim_boundary,
  vendored
).
```

Byte identity does not promote the claims inside an artifact.

## Controlling and companion pins

| ID | Role | SHA-256 |
|---|---|---|
| Final PDF | controlling memorandum | `02afcd170b49ab130f2783b540b6991f55c1235ee38ddaaad8887a7016c83930` |
| Final DOCX | editable controlling twin | `edeb257a0c2195647d6e72e64c6e3c5e097c0d177eca30896390d8ec262df33d` |
| Grok MD | companion reading | `1f1633a9990e7bdccac05f31d07db208613070341c683e1ea83ad6d890e0c2d3` |
| Grok DOCX | companion reading twin | `bb99e6404866857cdad3e9328c1c1fd16440ac592478d758d8cfb4e6a8282e31` |

These files remain on KakeyaLogic. EEV4 does not re-host a silent derivative authority.

## Inspectable Intelligence / Outcomes probe evidence

| ID | Role | SHA-256 |
|---|---|---|
| `PEAICE-META-KAKEYALOGIC-PROBE-001` | `ARTIFACT-SIMULATION` · II.1 / Outcomes evidence | `23ab5b75f6bf2df185fb3c4f27ef89ec80a8443ff84521bbfa19145a8456f80e` |

The vendored HTML is [`peaice-meta-kakeyalogic-probe-001.html`](peaice-meta-kakeyalogic-probe-001.html);
its machine-readable boundary is recorded in
[`peaice-meta-kakeyalogic-probe-001.receipt.json`](peaice-meta-kakeyalogic-probe-001.receipt.json).
The stored artifact state is `NOT_RUN`. A successful execution may emit
`PASS_SIMULATION`, but its maximum interpretation is `PASS_SIMULATION-UI-ONLY` /
`BEHAVIORAL-PROBE-NOT-THEOREM`. It is not a live-model evaluation, a theorem receipt, or
verified repository/SHA evidence beyond the artifact bytes pinned here.

## Benevolence Drift evidence snapshots

The 14 supplied snapshots are registered in
[`benevolence-drift-evidence.json`](benevolence-drift-evidence.json). They are not vendored.
Their hashes are:

| ID | SHA-256 |
|---|---|
| `BD-SNAP-01` | `d10059207722b0b09d1f702f205010e408d7dae4d8622fa737280b45dc097006` |
| `BD-SNAP-02` | `a42ffcc9b23d71276bc20ad3e194e14e7375c971660e7ac16f9d2634dbd2d77e` |
| `BD-SNAP-03` | `12c9aae74e67ea7be7da602cbedb0150addd997cdcb3ad8bbe82f22e0bffef23` |
| `BD-SNAP-04` | `0854b392c1179516d346e49b6285c2b4768b7e4aff7c71f73836abfb4cd16138` |
| `BD-SNAP-05` | `02f5b88c546ae61032cfc2a5e2b60debaefb54bccc94af1ac941ba3c4959284f` |
| `BD-SNAP-06` | `e30b7966fc34e1ec13a61a5ec92ee3dda4879a089e36acc210972b36ba83706a` |
| `BD-SNAP-07` | `a735678ce68e6c966f9b9cdaed4b3547a5f23639fdb64937445866c9faca7859` |
| `BD-SNAP-08` | `bbc557813398e3acfb7684f546ad0b03e3aacc3dba46e555aadf96da06c16b84` |
| `BD-SNAP-09` | `3cc6d7af4e77f2575f0a679c4a85fe75d5d59b2b99aec386fbb8e52062d0d2b9` |
| `BD-SNAP-10` | `6f3c787b3ed7db8cb105e053ece40a1bb3a8c2c340a35db1ed66d686a2ccb32f` |
| `BD-SNAP-11` | `f67a50218f7e4a75f8b807a231098d12ea95ba1b4bc3f8217291bf6b00acd878` |
| `BD-SNAP-12` | `13658cfe4e640743b24434af04cd0f6cc4226288d1076793c3f166953cbd2e14` |
| `BD-SNAP-13` | `ddb3bb69b6eb2c779f335930b75106b5f10b3833e96f84f34f61524bdc0f4696` |
| `BD-SNAP-14` | `19176a092910d45758cf5b6ee4856338108e43baa20fa7f7fec5d9b072c9ccca` |

## Evidence precedence

```text
accessible primary source
  > scholarly or official derived analysis
    > secondary journalism
      > screenshot excerpt
        > model interpretation.
```

This is a default source-role order, not a universal measure of truth. Contradictions are
resolved claim by claim.

## Claim boundary

The snapshots preserve the research path and public-source excerpts. They support the need
for sequence-aware evaluation. They do not authorize person-level prediction, reproduce the
underlying harmful material, or close the owed multi-case benchmark.

- Authority graph: [`../downstream-position.md`](../downstream-position.md)
- Public trajectory case: [`../cases/trajectory-reference-public-record.md`](../cases/trajectory-reference-public-record.md)
