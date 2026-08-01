#!/usr/bin/env python3
"""Protect OPEN claims from promotion on public repository surfaces."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json, validate_status_register

FORBIDDEN = {
    "RH": re.compile(r"\bRH\s+(?:is\s+)?(?:proved|proven|solved|CLOSED-POSITIVE)\b", re.IGNORECASE),
    "Coleman": re.compile(r"\bColeman(?:\s+Conjecture)?\s+(?:is\s+)?(?:proved|proven|solved|CLOSED-POSITIVE)\b", re.IGNORECASE),
}


def main() -> int:
    public_paths = [ROOT / "README.md", ROOT / "STATUS.md", *sorted((ROOT / "site").glob("*.html"))]
    violations = []
    for path in public_paths:
        text = path.read_text(encoding="utf-8")
        for claim, pattern in FORBIDDEN.items():
            if pattern.search(text):
                violations.append(f"{path.relative_to(ROOT)}:{claim}")

    status_errors = validate_status_register(load_json("registry/status-register.yaml"))
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    marker_errors = []
    for path_name, text in (("README.md", readme), ("STATUS.md", status)):
        if "RH OPEN" not in text:
            marker_errors.append(f"{path_name}:missing_RH_OPEN")
        if "Coleman" not in text or "OPEN" not in text:
            marker_errors.append(f"{path_name}:missing_Coleman_OPEN")

    errors = status_errors + marker_errors + [f"promotion:{item}" for item in violations]
    result = {"probe": "open_status", "ok": not errors, "errors": errors}
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
