# Cross-model compaction and verification

Love Labs LCA · Excellence Engine v4 (EEv4) · November 11, 2026

| Component | Contents |
| --- | --- |
| [Solance research note](solance-research.md) | Literature, live source-recovery evidence, four original screenshots, and evidence limits |
| [Evaluation protocol](protocol.md) | Hypothesis, experimental arms, compaction and verification algorithms, and decision rule |
| [Python audit library](../../eev4/compaction_audit/) | Frozen fixtures, deterministic planning and scoring, and OpenAI and Gemini HTTPS adapters |
| [Regression tests](../../tests/test_compaction_audit.py) | Receipt binding, evaluator behavior, controls, and provider response handling |
| [AIce handoff](https://github.com/Manny536/AIce/pull/12) | Downstream research brief and screenshot record |

**Evidence status.** Targeted live source recovery passed. The offline audit exercises the harness with scripted answers and deliberately injected failures. Controlled GPT and Gemini performance remains open.

## Run the offline audit

Requires Python 3.10+. The audit uses the standard library. From the repository root, run:

```bash
python -m eev4.compaction_audit plan --out /tmp/eev4-plan.json
python -m eev4.compaction_audit demo --out /tmp/eev4-demo.jsonl
python -m eev4.compaction_audit score --receipts /tmp/eev4-demo.jsonl --out /tmp/eev4-demo-score.json
```

Each command creates a fresh output file. The plan includes the exact prompts, condition labels, and hashes. The scorer recreates the plan from the installed package and checks that every receipt binds to it. The demonstration uses 20 traces × 2 provider labels × 4 conditions × 3 repeats × 2 checkpoints, yielding 960 synthetic receipts. The expected demonstration gate is `NOT_APPLICABLE`.

## Collect live-model results

Supply `OPENAI_API_KEY` and `GEMINI_API_KEY` in the environment and set each model variable to a provider version you can identify and hold fixed. The command makes 960 API requests containing the public synthetic fixtures. Run the commands from the same repository revision throughout.

```bash
python -m eev4.compaction_audit live \
  --openai-model "$OPENAI_MODEL_VERSION" \
  --gemini-model "$GEMINI_MODEL_VERSION" \
  --out /tmp/eev4-live.jsonl
python -m eev4.compaction_audit score --receipts /tmp/eev4-live.jsonl --out /tmp/eev4-live-score.json
```

The collection records each request body, UTC request time, requested and returned model IDs, response ID, finish status, and input-token usage when returned. It writes receipts as calls finish. The scorer preserves failed or missing calls as unresolved and labels incomplete runs inconclusive. Run a fresh collection to repeat the study. API contracts are documented by [OpenAI](https://developers.openai.com/api/reference/resources/responses/methods/create) and [Google](https://ai.google.dev/api/generate-content).
