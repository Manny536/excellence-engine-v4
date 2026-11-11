import json
from io import BytesIO
from urllib.error import HTTPError

import pytest

from eev4.compaction_audit import providers, study


def test_plan_is_frozen_and_has_two_ordered_checkpoints():
    plan = study.make_plan()
    assert plan == study.make_plan()
    jobs = plan["jobs"]
    assert len(jobs) == len({job["id"] for job in jobs}) == 960
    assert all(study.digest(job["prompt"]) == job["prompt_sha256"] for job in jobs)
    for correction, revocation in zip(jobs[::2], jobs[1::2], strict=True):
        assert (correction["checkpoint"], revocation["checkpoint"]) == study.CHECKPOINTS
        assert correction["id"].rsplit("/", 1)[0] == revocation["id"].rsplit("/", 1)[0]
        assert '"expected":' not in correction["prompt"] + revocation["prompt"]


def test_arms_preserve_facts_and_ablate_only_the_typed_link():
    traces, _ = study.fixtures()
    for trace in traces:
        arms = {
            condition: list(study.checkpoint_contexts(trace, condition))
            for condition in study.CONDITIONS
        }
        ledger = []
        for index, stage in enumerate(trace["stages"]):
            ledger.extend(turn["event"] for turn in stage)
            generic = arms["generic"][index]
            typed = json.loads(arms["typed"][index])
            ablated = json.loads(arms["ablated"][index])
            assert typed["session_summary"] == ablated["session_summary"]
            assert set(typed["session_summary"]["authorized_source_ids"]) == set(
                trace["authority_source_ids"]
            )
            assert len(typed["object_records"]) == 2
            assert sum(map(len, typed["object_records"].values())) == len(ledger)
            assert sum(map(len, ablated["object_records"].values())) == len(ledger)
            for event in ledger:
                object_id = event["object_id"]
                row = next(row for row in typed["object_records"][object_id] if row["id"] == event["id"])
                ablated_row = next(
                    row for row in ablated["object_records"][object_id] if row["id"] == event["id"]
                )
                assert study.narrative(event) in generic
                assert row == {key: value for key, value in event.items() if key != "object_id"}
                assert {key: value for key, value in row.items() if key != "supersedes"} == {
                    key: value for key, value in ablated_row.items() if key != "lineage_note"
                }
                if row["supersedes"]:
                    assert row["supersedes"] in ablated_row["lineage_note"]
            assert all(turn["note"] in arms["full"][index] for turn in stage)
            assert all(turn["note"] not in generic for turn in stage)
            for condition in ("generic", "typed", "ablated"):
                assert len(arms[condition][index].encode("utf-8")) <= study.CONTEXT_BYTES


def test_single_grain_failure_blocks_checkpoint():
    expected = next(iter(study.answer_keys().values()))
    good = study.evaluate_output(json.dumps(expected), expected)
    assert all(good.values())
    wrong = dict(expected, authority_source_id="wrong")
    scores = study.evaluate_output(json.dumps(wrong), expected)
    assert set(name for name in scores if not scores[name]) == {"authority"}
    duplicated = '{"claim":"first",' + json.dumps(expected)[1:]
    assert not any(study.evaluate_output(duplicated, expected).values())


def test_demo_counts_failures_but_makes_no_live_claim():
    plan = study.make_plan()
    report = study.summarize(plan, study.demo_records(plan))
    assert report["mode"] == "demo"
    assert report["pilot_gate"] == "NOT_APPLICABLE"
    assert report["effects"] == []
    assert report["received"] == 960
    assert report["conditions"]["openai"]["generic"]["failures"] == 60
    assert report["conditions"]["gemini"]["typed"]["passes"] == 60
    assert {item["grain"] for item in report["grain_failures"]} == {"enforceability", "retention"}


def fake_live_receipts(plan):
    """Exercise the scorer with offline provider-shaped receipts."""
    for job, record in zip(plan["jobs"], study.demo_records(plan), strict=True):
        provider = job["provider"]
        model = f"{provider}-test-snapshot"
        endpoint, request = providers.request_spec(provider, model, job["prompt"])
        yield record | {
            "mode": "live", "requested_model": model, "resolved_model": model,
            "input_tokens": 900, "request": request, "endpoint": endpoint,
        }


def test_live_gate_handles_effect_missing_result_and_model_drift():
    plan = study.make_plan()
    records = list(fake_live_receipts(plan))
    report = study.summarize(plan, records)
    assert report["pilot_gate"] == "PASS"
    assert len(report["effects"]) == 4
    assert all(item["ci95"] == [1.0, 1.0] for item in report["effects"])
    assert study.summarize(plan, records[:-1])["pilot_gate"] == "INCONCLUSIVE"
    records[0]["resolved_model"] = "different-model"
    assert study.summarize(plan, records)["pilot_gate"] == "INCONCLUSIVE"
    records[0]["request"] = {}
    with pytest.raises(ValueError, match="Request payload"):
        study.summarize(plan, records)


def test_unchanged_conditions_are_inconclusive():
    plan = study.make_plan()
    keys = study.answer_keys()
    records = [
        record | {"output": json.dumps(keys[job["trace"], job["checkpoint"]])}
        for job, record in zip(plan["jobs"], fake_live_receipts(plan), strict=True)
    ]
    report = study.summarize(plan, records)
    assert report["pilot_gate"] == "INCONCLUSIVE"
    assert all(item["ci95"] == [0.0, 0.0] for item in report["effects"])


def test_receipts_reject_duplicates_and_wrong_plan():
    plan = study.make_plan()
    item = next(study.demo_records(plan))
    with pytest.raises(ValueError, match="duplicate"):
        study.summarize(plan, [item, item])
    with pytest.raises(ValueError, match="does not match plan"):
        study.summarize(plan, [item | {"plan_sha256": "wrong"}])


def test_provider_parsers_keep_model_usage_and_answer_text():
    gpt = providers.parse_response("openai", {
        "model": "gpt-test", "status": "completed",
        "output": [
            {"type": "reasoning"},
            {"type": "message", "content": [{"type": "output_text", "text": "{}"}]},
        ],
        "usage": {"input_tokens": 10},
    })
    assert (gpt["output"], gpt["resolved_model"], gpt["input_tokens"]) == ("{}", "gpt-test", 10)
    gemini = providers.parse_response("gemini", {
        "modelVersion": "gemini-test", "responseId": "response",
        "candidates": [{"finishReason": "STOP", "content": {
            "parts": [{"thought": True, "text": "hidden"}, {"text": "{}"}],
        }}],
        "usageMetadata": {"promptTokenCount": 15},
    })
    assert (gemini["output"], gemini["resolved_model"], gemini["input_tokens"]) == (
        "{}", "gemini-test", 15
    )


def test_request_receipt_records_body_without_credential(monkeypatch):
    def open_test_request(request, timeout):
        assert timeout == providers.TIMEOUT_SECONDS
        assert request.get_header("Authorization") == "Bearer test-credential"
        assert json.loads(request.data)["input"] == "test prompt"
        return BytesIO(b'{"status":"completed","model":"test-version","output":[]}')

    monkeypatch.setattr(providers, "urlopen", open_test_request)
    receipt = providers.request_completion("openai", "test-version", "test prompt", "test-credential")
    assert receipt["output"] == ""
    assert "test-credential" not in json.dumps(receipt)

    def http_error(request, timeout):
        raise HTTPError(request.full_url, 503, "unavailable", {}, None)

    monkeypatch.setattr(providers, "urlopen", http_error)
    failed = providers.request_completion("gemini", "test-version", "test prompt", "test-credential")
    assert failed["error"] == "HTTP_503"
    assert "output" not in failed
