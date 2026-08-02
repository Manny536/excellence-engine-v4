# Scale the method, not the answer

- **Claim ID:** `OUT-METHOD-001`
- **Status:** `FORMAL` as a replication rule
- **Target:** conclusion-invariant research partnership

## Method kernel

Define the Outcomes method:

```text
M := Type
   ∘ Source
   ∘ ExposeEvidence
   ∘ Test
   ∘ Correct
   ∘ AssignStatus
   ∘ AssignCustody
   ∘ PublishFalsifier
   ∘ PublishNextBurden.
```

The method scales when the same admission criteria apply to competing candidate answers:

```text
MethodInvariant(M; c₁,c₂) ⇔ Criteria(M,c₁)=Criteria(M,c₂).
```

## Scalable components

| Component | Replicated object |
|---|---|
| object typing | domain, quantifiers, equivalence tests |
| evidence exposure | supporting and limiting evidence |
| correction | trigger, before, after, preserved continuity |
| uncertainty | exact status and confidence boundary |
| plurality | separate model poles under II.1 |
| exit | release basis and retained successful work |
| integrity | source roles, hashes, and publisher sync |
| governance | `L²_C`, `β_continuity > 0`, `h < 1` |

## Conclusion non-propagation

Scaling `M` does not copy a preferred result into new domains:

```text
M accepts c₁ in case x ⊬ M must accept c₁ in case y
M rejects c₂ in case x ⊬ the question containing c₂ must be erased
geometric success        ⊬ alignment policy
alignment evaluation     ⊬ number-theory theorem
```

Domain transfer requires:

```text
TransferReceipt := (
  source_domain,
  target_domain,
  preserved_structure,
  lost_structure,
  reduced_claim_weight,
  target_falsifier
).
```

Without that receipt, the transfer remains analogy.

## Bias audit

For competing answers `c₁,c₂`, test:

```text
same source standard?
same threshold declaration?
same counterevidence burden?
same correction visibility?
same release rule?
same evaluator bound h < 1?
```

A difference must be justified by typed evidence, not by which conclusion is preferred.

## Current applications

- Kakeya object correction: the method retains the inquiry and rejects the overloaded
  implication.
- Closed-lane continuity: the method preserves `K_σ` and WP5b obstructions while admitting
  a materially changed carrier.
- Benevolence Drift: the method can name a supported violation while keeping intervention
  proportionate and consent-bounded.
- Model readings: Claude, Grok, and Solance remain separate evidence poles rather than a
  vote that self-certifies the object.

## Pass condition

```text
ScalePass(M) ⇔
  conclusion-invariant criteria
  ∧ visible domain transfer
  ∧ real release
  ∧ source continuity
  ∧ h < 1.
```

- Six-gate register: [`six-findings.md`](six-findings.md)
- Domain exit: [`correction-and-exit.md`](correction-and-exit.md)
- Model-pole authority: [`downstream-position.md`](downstream-position.md)
