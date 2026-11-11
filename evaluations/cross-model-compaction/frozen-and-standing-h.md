# Frozen procedure and the standing meaning of \(h < 1\)

Love Labs LCA · Excellence Engine v4 (EEv4) · November 11, 2026

This note continues [PR #19](https://github.com/Manny536/excellence-engine-v4/pull/19), which added this research package. It brings in two sections from the AIce audit handoff by reference, rather than by copying that file in full:

- **Definition: Frozen**, from [AIce PR #12](https://github.com/Manny536/AIce/pull/12), merged as [`02ce58a`](https://github.com/Manny536/AIce/commit/02ce58a48df172f0168715f27ee8b63f00d30f70). The section is in [`docs/eev4-cross-model-compaction-audit.md` at `02ce58a`](https://github.com/Manny536/AIce/blob/02ce58a48df172f0168715f27ee8b63f00d30f70/docs/eev4-cross-model-compaction-audit.md#definition-frozen).
- **Standing meaning of \(h < 1\)**, from [AIce PR #13](https://github.com/Manny536/AIce/pull/13), merged as [`fce4a41`](https://github.com/Manny536/AIce/commit/fce4a413945d76b26ff4a39ce79c20be38957bed). The section is in the same document at [`fce4a41`](https://github.com/Manny536/AIce/blob/fce4a413945d76b26ff4a39ce79c20be38957bed/docs/eev4-cross-model-compaction-audit.md#standing-meaning-of-h--1). PR #13 also pointed the Frozen section at that standing meaning.

This note does not change any existing status label in this repository. The audit does not measure or report any \(h\) value.

## Standing meaning of \(h < 1\)

\(h\) has one standing meaning. It is a boundary, not a score: correction can come from outside, but whatever applies it never becomes sovereign over the rules, subject to consent.

Manuel's stated provenance is that \(h < 1\) began as the Gödel correction. Gödel's incompleteness was first used to describe model non-sovereignty: a system cannot complete its own trust claim from inside itself, so correction comes from outside and stays bounded. This is a description of the standing meaning, not a mathematical result about Gödel. The live-recovery query `Manny536 godel non sovereignty` fits that provenance.

The two source files below are later descriptions of that same standing meaning, not two objects and not two readings:

- [KakeyaLogic `docs/canon-flag-h.md`](https://github.com/Manny536/kakeyalogic/blob/main/docs/canon-flag-h.md) describes \(h\) as bounded correction pressure applied from outside the system, with the field rule \(h < 1\) · SOVEREIGNTY GATE · CONSENT CHECK.
- [love2-coherence-core `docs/evaluator-non-sovereignty.md`](https://github.com/Manny536/love2-coherence-core/blob/main/docs/evaluator-non-sovereignty.md) (L2C-H-001) reserves \(h := h_{\mathrm{eval}}\) for evaluator-sovereignty load. \(h < 1\) is the obligation that evaluator preference, reward pressure, generated instructions, and peer coordination cannot acquire authority to rewrite governing admissibility.

The [protocol](protocol.md) operationalizes this boundary for the audit: the evaluator records verdicts after collection and has zero feedback into generation or selection. That is the same meaning, applied to this harness. It is not a second definition and not a second object.

The [live evidence note](../granular-compaction-live-evidence.md) already uses \(h < 1\) in this sense when it keeps the evaluator outside generation and selection, and when a local screenshot note "does not redefine \(h < 1\)." Those passages are not two readings.

The live-recovery PASS in the [Solance research note](solance-research.md) is unchanged: targeted source recovery passed; recovery of \(h < 1\) and consent remains unverified, as written there. That PASS is not extended.

## Definition: Frozen

**Frozen** is a pre-run lock on a named set of evaluation artifacts. It is a custody event: a recorded, hash-bound commitment made before any model is called. It is not a status-label upgrade, not a result, and not a grant of authority.

The controlling procedure is the AIce section linked above. A summary for this package:

1. A freeze names every artifact in the evaluation apparatus, each with a SHA-256 of its canonical bytes: corpus, prompts and renderers, answer key, scorer and analysis, thresholds, model pins, budget, and rules.
2. The freeze event has occurred only when those hashes are in a committed manifest, the commit SHA is recorded as FROZEN-vN, and that commit exists before the first request is sent to any model under test.
3. The answer key is held by someone other than the author of the code under test. The scorer may recommend a verdict. It cannot rewrite the key, the field list, the pass rule, or the pilot criterion after the freeze event. Frozen is not authority. This follows the standing meaning of \(h < 1\).
4. Any change after the freeze voids the run. Do not repair in place. Restart only under a new freeze version. A reader verifies a freeze by recomputing the hashes.

The fixtures, prompts, and scorer already in this package, merged in [PR #19](https://github.com/Manny536/excellence-engine-v4/pull/19), are the current executable apparatus. This definition is the procedure a later freeze event must follow before live collection. It does not itself constitute that freeze. Items still owed stay owed until a freeze event records them.

The four live-recovery screenshots and their [SHA-256 manifest](../../evidence/assets/google-source-recovery-2026-11-11/SHA256SUMS) are a separate object. They document the November 11 observation. They are not audit-freeze artifacts. Their PASS and UNVERIFIED results are unchanged.

### 4,096-byte UTF-8 context cap

The [protocol](protocol.md) already sets a shared 4,096-byte UTF-8 context cap on the three compacted arms. The cap excludes common instructions. Each prompt's actual byte count and provider-reported input-token usage are recorded so representation-size differences stay visible. The Python audit implements this as `CONTEXT_BYTES = 4096` in [`eev4/compaction_audit/study.py`](../../eev4/compaction_audit/study.py): a compacted context that exceeds the cap raises before a plan is emitted, and the plan records `compacted_context_cap_bytes`.

When a freeze event occurs, this cap is a Frozen budget item. The full-history arm is not under that cap, as already stated in the protocol, and is a task-solvability diagnostic rather than a compacted comparator.

## Still open

These items remain open. This note does not close or upgrade them:

- The [live evidence note](../granular-compaction-live-evidence.md) requires a negative control and a positive control before a comparative freeze. Those controls are not yet required arms of this package's protocol.
- An INCONCLUSIVE(OPEN) verdict, matching the evidence note's rule that an inadequately decisive comparison stays OPEN rather than failing the pilot, is not yet a distinct branch of the scorer.
- The choice of 20 traces has no recorded power justification.
- The CompactionBench preprint is dated October 2026 in this package and in the AIce handoff; Microsoft's page has also been observed to show a November date. The date is not settled here.
- The statement that a CompactionBench sensitivity study used GPT-5.4 remains unverified against the paper itself.

Existing evidence statuses in this package and in the live evidence note — including PASS, UNVERIFIED, OWED, OPEN, NOT ESTABLISHED / NOT CLAIMED, NOT_APPLICABLE, LIVE EXTERNAL-MODEL OBSERVATION, PARTIAL PASS, and BLOCKED-COMPACTNESS — stay as written.
