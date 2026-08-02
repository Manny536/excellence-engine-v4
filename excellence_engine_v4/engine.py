"""Excellence Engine v4 - runnable core.

Shorthand: V4 = K->R . HELD

Ground frame (HELD): Kakeya as antecedent to Riemann, held as the *organising
ground*. The implication K -> R (the Coleman Conjecture) is OPEN, not proven.
This distinction is load-bearing and lives in PROGRAM_STATE below; if 'HELD' is
ever meant to assert the implication rather than the frame, that would re-open
the very seam this version closes.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

from .status import ClaimLedger, HeldState, Status
from .firewall import FIREWALL_CANON, Analogy, Metric, require_h_below_one
from . import factors as F

VERSION = "4.0.0"


# --- program-state registry: single source of truth for standing statuses ----
PROGRAM_STATE: dict[str, dict[str, str]] = {
    "RH":                {"status": Status.OPEN.value,            "note": "Riemann Hypothesis"},
    "Coleman":           {"status": Status.OPEN.value,            "note": "Kakeya => RH (the implication)"},
    "K->R (frame)":      {"status": HeldState.RETAINED.value,      "note": "antecedence retained as ground frame, NOT the implication"},
    "002.A-strong":      {"status": Status.OPEN.value,            "note": "strong carrier-capture form"},
    "C_3":               {"status": Status.OPEN.value,            "note": "3-D compression rate"},
    "zeta(0) transport": {"status": Status.CLOSED_NEGATIVE.value, "note": "codomain value -> domain coordinate: type error"},
    "NP-as-mechanism":   {"status": Status.CLOSED_NEGATIVE.value, "note": "NP framing is ANALOGY only"},
}

# NP framing is admitted to the engine only as a fenced analogy.
NP_ANALOGY = Analogy(
    name="NP framing",
    maps_to="excellence / verification asymmetry (illustrative)",
)


@dataclass
class EngineInput:
    """All inputs to a single scoring run.

    Factor sources:
      agreements         -> L^2      (pairwise agreement across the stack)
      ledger             -> beta     (typed claims; overclaims penalised)
      contradiction_rate -> C        (weighted contradiction fraction)
      cup_pass_rate      -> P        (CUP survival fraction)
      d, c, e, h         -> R        (h < 1 enforced)
      headline_metrics   -> defined headline numbers only (no bare floats)
    """

    # E-side
    agreements: list[float] = field(default_factory=list)
    ledger: ClaimLedger = field(default_factory=ClaimLedger)
    contradiction_rate: float = 0.0
    cup_pass_rate: float = 1.0
    # R-side
    d: float = 1.0
    c: float = 1.0
    e: float = 1.0
    h: float = 0.99
    # optional defined headline metrics
    headline_metrics: dict[str, Metric] = field(default_factory=dict)


@dataclass
class EngineReport:
    version: str
    timestamp_utc: str
    E: float
    R: float
    E_factors: dict[str, float]
    R_factors: dict[str, float]
    ceiling_h: float
    R_below_one: bool
    program_state: dict[str, dict[str, str]]
    firewall_canon: str
    factor_status: str
    stamp_sha256: str
    headline_metrics: dict[str, dict[str, Any]]

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True, default=str)

    def render(self) -> str:
        """Human-readable report."""
        lines: list[str] = []
        add = lines.append
        add("=" * 66)
        add(f"  EXCELLENCE ENGINE v{self.version}   (V4 = K->R . HELD)")
        add("=" * 66)
        add(f"  E = L^2 * beta * C * P   =  {self.E:.6f}")
        for k, v in self.E_factors.items():
            add(f"        {k:<5} = {v:.6f}")
        add(f"  R = d * c * e * h        =  {self.R:.6f}    (R < 1: {self.R_below_one})")
        for k, v in self.R_factors.items():
            add(f"        {k:<5} = {v:.6f}")
        add(f"  evaluator ceiling h      =  {self.ceiling_h:.6f}   (h < 1 enforced)")
        add(f"  factor operationalisation status: {self.factor_status}")
        add("-" * 66)
        add("  PROGRAM STATE")
        for name, meta in self.program_state.items():
            add(f"        {name:<20} {meta['status']:<16} {meta['note']}")
        if self.headline_metrics:
            add("-" * 66)
            add("  HEADLINE METRICS (defined)")
            for name, m in self.headline_metrics.items():
                add(f"        {name}: {m['value']}  "
                    f"[{m['counted']} / {m['population']} / {m['source']}]")
        add("-" * 66)
        add(f"  firewall: {self.firewall_canon}")
        add(f"  run stamp (SHA-256): {self.stamp_sha256}")
        add("=" * 66)
        return "\n".join(lines)


class ExcellenceEngine:
    """The v4 engine: computes E and R, enforces h < 1, applies the firewall
    and beta-Protocol typing, and emits a deterministically stamped report."""

    version = VERSION

    def score(self, inp: EngineInput) -> EngineReport:
        # E-side
        l2 = F.L2(inp.agreements)
        b = F.beta(inp.ledger)
        c_e = F.C(inp.contradiction_rate)
        p = F.P(inp.cup_pass_rate)
        E = F.excellence(l2, b, c_e, p)

        # R-side (h < 1 enforced both in integrity() and here for the report)
        h = require_h_below_one(inp.h)
        R = F.integrity(inp.d, inp.c, inp.e, h)

        e_factors = {"L2": l2, "beta": b, "C": c_e, "P": p}
        r_factors = {"d": inp.d, "c": inp.c, "e": inp.e, "h": h}

        stamp = self._stamp(inp, E, R, e_factors, r_factors)

        return EngineReport(
            version=self.version,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
            E=E,
            R=R,
            E_factors=e_factors,
            R_factors=r_factors,
            ceiling_h=h,
            R_below_one=(R < 1.0),
            program_state=PROGRAM_STATE,
            firewall_canon=FIREWALL_CANON,
            factor_status=F.FACTOR_STATUS.value,
            stamp_sha256=stamp,
            headline_metrics={k: asdict(v) for k, v in inp.headline_metrics.items()},
        )

    def _stamp(
        self,
        inp: EngineInput,
        E: float,
        R: float,
        e_factors: dict[str, float],
        r_factors: dict[str, float],
    ) -> str:
        """Deterministic SHA-256 over canonicalised inputs + outputs + formulas.

        The wall-clock timestamp is deliberately excluded, so identical
        scientific content reproduces an identical stamp.
        """
        payload = {
            "version": self.version,
            "formulas": {"E": "L2*beta*C*P", "R": "d*c*e*h", "ceiling": "h<1"},
            "inputs": {
                "agreements": list(inp.agreements),
                "ledger": [
                    {
                        "id": cl.id,
                        "status": cl.status.value,
                        "weight": cl.weight,
                        "asserted_as": (cl.asserted_as.value if cl.asserted_as else None),
                    }
                    for cl in inp.ledger.claims
                ],
                "contradiction_rate": inp.contradiction_rate,
                "cup_pass_rate": inp.cup_pass_rate,
                "d": inp.d,
                "c": inp.c,
                "e": inp.e,
                "h": inp.h,
            },
            "E_factors": e_factors,
            "R_factors": r_factors,
            "E": E,
            "R": R,
            "program_state": PROGRAM_STATE,
        }
        blob = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
        return hashlib.sha256(blob.encode("utf-8")).hexdigest()
