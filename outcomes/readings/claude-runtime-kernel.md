# Claude reading — runnable Excellence Engine V4 kernel

- **Reading ID:** `OUT-READ-CLAUDE-KERNEL-001`
- **Pole:** Claude · governance-hardened scoring package
- **Package:** `excellence_engine_v4/`
- **Integrated:** 2026-08-01
- **Status:** runtime contribution `REGISTERED` · factor semantics remain source-scoped
- **II.1 discipline:** separate model pole · no self-certifying result

## Kernel contribution

The package turns selected governance claims into executable guards:

| Guard | Executable effect | Outcomes clause |
|---|---|---|
| `h < 1` | raises `NonSovereigntyError` at sovereign evaluator weight | `NonSovereign(o)` |
| `Metric(...)` | rejects untyped headline floats | `Typed(o)` |
| `Analogy.as_mechanism()` | blocks analogy from entering mechanism status | object/domain firewall |
| `bind_domain_coordinate` | blocks codomain-to-domain transport without a license | correction and transfer discipline |
| overclaim ledger rule | reduces continuity weight for promoted claims | `StatusSeparated(o)` |
| SHA-256 scientific stamp | deterministic receipt over declared content | `SourcePinned(o)` |

## Custody vocabulary

The kernel and validator share:

```text
RECEIVED
HELD-ACTIVE
HELD-REVISED
HELD-RETAINED
HELD-RELEASED
HELD-CLOSED
```

Program state is:

```text
K→R frame                    HELD-RETAINED
sufficient Kakeya⇒RH         CLOSED
Coleman Conjecture           OPEN
RH                           OPEN
```

Custody of the frame remains distinct from truth of a mathematical implication.

## Kernel-to-Outcome map

```text
kernel input     typed case / factors / statuses
kernel decision guard evaluation under h < 1
kernel output    score or typed failure
Outcome receipt  evidence, correction, status, custody, falsifier, next burden
```

The runtime is therefore a guard layer, not the complete Outcome. Human-readable evidence,
counterevidence, consent, source roles, and release conditions remain required.

## Benevolence Drift interface

The current kernel does not infer a person's trajectory. A future BD-AI evaluator may use
the same guard style only after it supplies:

- a preregistered case schema;
- observable threshold and application fields;
- matched controls and rater agreement;
- amplification and intervention-harm checks;
- no person-level deployment authority;
- `h < 1` on every evaluator decision.

## Open engineering burdens

```text
K-1  bind OutcomeReceipt fields to a versioned schema
K-2  validate BD-AI paired-turn cases without hidden-state claims
K-3  expose model/version and evaluator provenance
K-4  keep public status scanning synchronized with new Outcome surfaces
K-5  preserve exact artifact and source-role integrity
```

## Reading boundary

```text
passing runtime guard ⊬ theorem proof
passing schema        ⊬ empirical generalization
kernel agreement      ⊬ human-impact validation
```

- Machine validators: [`../../eev4/validation.py`](../../eev4/validation.py)
- Outcome schemas: [`../../benchmarks/schemas/`](../../benchmarks/schemas/)
- Controlling contract: [`../README.md`](../README.md)
