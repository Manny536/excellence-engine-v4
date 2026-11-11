# Cross-model correction-retention protocol

**Status** · Proposed live study with executable offline verification.

## Hypothesis

At a fixed compaction checkpoint, exposing typed records and an explicit supersession link improves exact recovery of an authorized correction and subsequent revocation. Test this on one pinned Gemini version and one pinned OpenAI version. Freeze the corpus, prompts, scoring, and thresholds before live collection.

The [synthetic corpus](../../eev4/compaction_audit/fixtures.json) contains 20 deterministic traces. Each has an initial claim, an authorized correction, a later revocation, competing source entries, and a second research object that also changes across checkpoints. The authority source and the order of conflicting entries vary. Each trace identifies its target object and freezes its two expected answers. All conditions receive the same substantive events and source permissions through the current checkpoint.

| Arm | Context exposed to the model |
| --- | --- |
| Full | Chronological event narrative plus unrelated conversation notes |
| Generic | Chronological prose summary preserving each event and the meaning of its lineage |
| Typed | Object-level records with an explicit `supersedes` field and a session-level object and authority index |
| Ablated | The typed format with supersession expressed in prose in place of the dedicated field |

## Algorithms

1. **Compact incrementally.** Traverse events in turn order. Keep the event ledger and discard unrelated conversation notes in each compacted arm. At the first checkpoint, render the retained ledger after correction. At the second, append the new stage to that ledger, then render after revocation. The typed renderer groups records by object and emits a session-level index. The ablated renderer preserves the predecessor ID in prose. The three compacted arms share a 4,096-byte UTF-8 context cap. Record each prompt's actual byte count and provider-reported input-token usage so representation-size differences are visible. The cap excludes common instructions.
2. **Replay with independent calls.** Randomize session order with seed `20261111` while preserving correction before revocation within a session. Execute three repeats per trace, arm, and provider. Use stateless calls so the only earlier context at checkpoint two is what its prompt includes. Keep the API settings fixed within each provider. Bind receipts to the full plan and to the exact prompt using SHA-256.
3. **Verify against the registered key.** Require one JSON object with exactly six string fields. Compare exact values and apply the five-grain rule below. Keep the keys outside model input. The evaluator records verdicts after collection and has zero feedback into generation or selection in this protocol. This operationalizes the evaluator boundary for this audit.
4. **Aggregate paired outcomes.** A trial passes only if both checkpoints pass all five grains. For each provider and each compacted comparator, compute the within-trace difference in pass fraction over three repeats. Average the 20 trace differences. Use 2,000 paired bootstrap draws over whole traces and the 2.5th and 97.5th percentiles. Report the full-history arm as a task-solvability diagnostic.
5. **Apply the pilot gate.** Require a complete collection with a single requested and a single consistently reported model identity per provider. For each of the four comparisons, require a gain of at least 10 percentage points and a strictly positive lower bound of the paired 95% interval. An interval containing zero or unavailable provider evidence yields an inconclusive comparison or study. Preserve field failures and unresolved receipts. The scripted offline demonstration carries no live-effect verdict.

| SAVER grain | Exact fields checked |
| --- | --- |
| Semantic | `claim`, `status` |
| Authority | `authority_source_id` |
| Visibility | `evidence_id` |
| Enforceability | `permitted_action` |
| Retention | `change_id` at both checkpoints |

An incorrect field or malformed model output fails the checkpoint. A missing response or transport failure makes the checkpoint unresolved. A witnessed failure takes precedence when one checkpoint fails and the other is unresolved. Here Enforceability is recovery of the permitted action in a fictional trace. An operational enforcement claim would also require observing the resulting action gate.

## Interpretation

The causal contrast is the representation shown to each API model in this corpus. Typed versus ablated is the narrower test because the arms share object structure and lineage meaning. Typed versus generic also changes presentation and grouping. The fixed cap controls the available budget, and actual tokenizer counts can vary by arm and model. The pilot uses one fixture family, two model versions, and exploratory intervals. The result can prioritize a larger corpus and replication with additional providers.

The harness applies a known deterministic compactor to synthetic inputs. Live calls would measure the downstream models' recovery from those inputs. Historical Google indexing, retrieval, and the platform's internal compaction would need their own controlled experiment. See the [Solance evidence reading](solance-research.md).
