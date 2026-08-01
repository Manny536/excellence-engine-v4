# engine/ — Formal V4 architecture

Controlling custody architecture for Excellence Engine V4.

| File | Role |
|---|---|
| `excellence-engine-v4.md` | Full V4 definition (controlling) |
| `held-predicate.md` | HELD_t(q) |
| `held-state-transitions.md` | RECEIVED → … → HELD-CLOSED |
| `l2c-governance.md` | L²_C as field gate |
| `beta-continuity.md` | β continuity across evaluations |
| `h-evaluator-bound.md` | h < 1 non-sovereignty |
| `inspectable-intelligence.md` | II.1 link |
| `engine-pipeline.md` | Receive→…→Publish |

```text
EEV4-valid(q,t) ⇔ L²_C(q,t) ∧ β_continuity(q,t) > 0 ∧ HELD_t(q)
```

## Runnable package

Installable kernel at repository root:

- `../excellence_engine_v4/` — Python package
- `../run_demo.py` — demo report + firewall firings
- `../tests/test_engine.py` — 31 FORMAL-spine tests

```text
from excellence_engine_v4 import ExcellenceEngine, EngineInput, Claim, ClaimLedger, Status
```

HELD in the package means the **K→R ground frame** is held; Coleman implication remains OPEN. Aligns with `held-predicate.md` custody language.
