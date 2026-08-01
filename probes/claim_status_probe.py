#!/usr/bin/env python3
"""Validate the exact claim-ID/status contract."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json, validate_status_register


def main() -> int:
    register = load_json("registry/status-register.yaml")
    errors = validate_status_register(register)
    result = {"probe": "claim_status", "ok": not errors, "errors": errors}
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
