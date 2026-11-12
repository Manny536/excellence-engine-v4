"""Plan, exercise, execute, and verify the compaction audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from uuid import uuid4

from . import providers, study


def write_json(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def write_receipts(path, records):
    with path.open("x", encoding="utf-8") as stream:
        for record in records:
            stream.write(study.canonical(record) + "\n")
            stream.flush()


def read_receipts(path):
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            yield json.loads(line)


def live_records(plan, models, keys):
    collection_id = str(uuid4())
    plan_sha = study.digest(study.canonical(plan))
    for job in plan["jobs"]:
        provider = job["provider"]
        response = providers.request_completion(
            provider, models[provider], job["prompt"], keys[provider]
        )
        yield study.receipt_identity(job, plan_sha, "live") | response | {
            "collection_id": collection_id,
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("plan", "demo", "live", "score"):
        command = commands.add_parser(name)
        command.add_argument("--out", type=Path, required=True)
        if name == "score":
            command.add_argument("--receipts", type=Path, required=True)
        if name == "live":
            command.add_argument("--gemini-model", required=True, help="Pinned Gemini model ID")
            command.add_argument("--openai-model", required=True, help="Pinned OpenAI model ID")
    args = parser.parse_args()
    try:
        plan = study.make_plan()
        if args.command == "plan":
            write_json(args.out, plan)
        elif args.command == "demo":
            write_receipts(args.out, study.demo_records(plan))
        elif args.command == "score":
            write_json(args.out, study.summarize(plan, read_receipts(args.receipts)))
        else:
            models = {"gemini": args.gemini_model, "openai": args.openai_model}
            for provider, model in models.items():
                providers.request_spec(provider, model, "")
            write_receipts(args.out, live_records(plan, models, providers.credentials()))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(2, f"audit: {exc}\n")


if __name__ == "__main__":
    main()
