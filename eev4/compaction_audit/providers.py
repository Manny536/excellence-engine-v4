"""Stateless HTTPS adapters for live calls on the frozen synthetic workload."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .study import canonical

MAX_OUTPUT_TOKENS = 2048
TIMEOUT_SECONDS = 90
OPENAI_URL = "https://api.openai.com/v1/responses"
GEMINI_ROOT = "https://generativelanguage.googleapis.com/v1beta/models"


def request_spec(provider, model, prompt):
    if not re.fullmatch(r"[A-Za-z0-9._-]+", model):
        raise ValueError("Pass a provider model ID without a path prefix")
    if provider == "openai":
        return OPENAI_URL, {
            "model": model,
            "input": prompt,
            "store": False,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "text": {"format": {"type": "json_object"}},
        }
    if provider != "gemini":
        raise ValueError(f"Unsupported provider {provider}")
    return f"{GEMINI_ROOT}/{model}:generateContent", {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": MAX_OUTPUT_TOKENS,
            "responseMimeType": "application/json",
        },
    }


def credentials():
    names = {"openai": "OPENAI_API_KEY", "gemini": "GEMINI_API_KEY"}
    keys = {provider: os.environ.get(name) for provider, name in names.items()}
    missing = [names[provider] for provider, key in keys.items() if not key]
    if missing:
        raise ValueError("Set " + " and ".join(missing))
    return keys


def parse_response(provider, data):
    """Retain an empty output for a provider-completed refusal or no candidate."""
    if provider == "openai":
        status = data["status"]
        metadata = {
            "resolved_model": data.get("model"), "response_id": data.get("id"),
            "finish_status": status, "input_tokens": (data.get("usage") or {}).get("input_tokens"),
        }
        if status not in {"completed", "incomplete"}:
            return metadata | {"error": "PROVIDER_RESPONSE_UNAVAILABLE"}
        text = "".join(
            part.get("text", "")
            for item in data["output"]
            if item.get("type") == "message"
            for part in item.get("content", [])
            if part.get("type") == "output_text"
        )
        return metadata | {"output": text}
    if "candidates" not in data and "promptFeedback" not in data:
        raise ValueError("Missing Gemini candidates or prompt feedback")
    candidates = data.get("candidates", [])
    candidate = candidates[0] if candidates else {}
    text = "".join(
        part.get("text", "") for part in (candidate.get("content") or {}).get("parts", [])
        if not part.get("thought", False)
    )
    return {
        "output": text, "resolved_model": data.get("modelVersion"),
        "response_id": data.get("responseId"), "finish_status": candidate.get("finishReason"),
        "input_tokens": (data.get("usageMetadata") or {}).get("promptTokenCount"),
    }


def request_completion(provider, model, prompt, key):
    url, body = request_spec(provider, model, prompt)
    headers = {"Content-Type": "application/json"}
    if provider == "openai":
        headers["Authorization"] = f"Bearer {key}"
    else:
        headers["x-goog-api-key"] = key
    request = Request(url, data=canonical(body).encode("utf-8"), headers=headers, method="POST")
    receipt = {
        "requested_model": model, "endpoint": url, "request": body,
        "requested_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            data = json.load(response)
        outcome = parse_response(provider, data)
    except HTTPError as exc:
        outcome = {"error": f"HTTP_{exc.code}"}
    except (URLError, TimeoutError, OSError):
        outcome = {"error": "TRANSPORT_ERROR"}
    except (AttributeError, KeyError, TypeError, ValueError):
        outcome = {"error": "INVALID_PROVIDER_RESPONSE"}
    return receipt | outcome
