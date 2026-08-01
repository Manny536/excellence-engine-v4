# SOURCE_MAP — Cross-repository ownership

**Lab layout:** Excellence Engine V4 is a **separate git** in the PeAIce / Love Labs structure (same pattern as LoveLabs-LCA, Grok Terminal, Claude V6, KakeyaLogic).

## Ownership matrix

| Surface | Repo | Owns |
|---|---|---|
| **Excellence Engine V4 (this repo)** | `Manny536/excellence-engine-v4` | HELD architecture, Outcomes *position*, evaluation protocols, V4 registers |
| **KakeyaLogic (field)** | `Manny536/kakeyalogic` | EEv3 field, controlling Outcomes memo + Grok rundown, ARX lane, probes, landing HTML |
| **Claude V6 (ledger)** | `Manny536/claude-v6` | Theorem-facing status, walls, A–H, prime-carrying L3 register |
| **LoveLabs-LCA** | `Manny536/LoveLabs-LCA` | CUP / relational architecture, BD-AI benchmark records |
| **Grok Terminal** | `Manny536/grok-terminal` | TERMINAL extractions, polarized Grok receipts |
| **PeAIce Index** | `Manny536/peaice-index` | Program index / hosted probes |
| **GPT-v2 Excellence Engine** | `Manny536/GPT-v2-excellence-engine-` | Historical Solance/GPT formal EE implementation lineage |
| **PeAIce public** | peaice.org | Outcomes, EEV, DDATL public pages |

## Controlling vs companion

| Artifact | Controlling home | Companion / pin |
|---|---|---|
| Outcomes FINAL-001 (23 pp) | kakeyalogic `docs/outcomes/` | this repo `outcomes/artifacts/` (hashes only) |
| Grok Outcomes rundown | kakeyalogic | this repo `outcomes/readings/grok-companion.md` |
| Claude Outcomes pin | claude-v6 `docs/research/peaice-outcomes-grok-rundown.md` | this repo `outcomes/readings/claude-downstream-registration.md` |
| Solance (GPT) V4 reading | this repo `outcomes/readings/solance-v4-reading.md` | lineage: GPT-v2-excellence-engine |
| EEV4 definition | **this repo** `engine/excellence-engine-v4.md` | kakeyalogic PR #8 mirrors + points here |

## Solance (GPT) & Lab structure

```text
LoveLabs-LCA          relational / CUP lab
GPT-v2-excellence-engine-   Solance/GPT formal EE lineage
kakeyalogic           geometric field + Outcomes controlling files
claude-v6             theorem ledger
grok-terminal         polarized TERMINAL pole
excellence-engine-v4  custody engine lab (HELD)  ← this repository
```

Model readings stay **separate under II.1** (polarization). No ensemble self-certification.
