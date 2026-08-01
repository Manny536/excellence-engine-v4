"""Metaphor / mechanism firewall and metric-discipline guards for EE v4.

This module makes three v3 seams *unrepresentable at runtime*:

  1. zeta(0) = -1/2 transport. Binding the codomain value -1/2 onto the domain
     coordinate Re(s)=1/2 is a type error (CLOSED-NEGATIVE). Encoded so it raises.
  2. NP framing. May enter only as an Analogy; using it as a mechanism raises.
  3. Undefined headline numbers. The v3 headline percentages (94% / 60%) had no
     defined metric. Here a headline number must be a Metric with counted /
     population / source, or construction raises.

Plus the evaluator ceiling: h must be strictly < 1 (FLAG-001).
"""
from __future__ import annotations

from dataclasses import dataclass

from .status import Status

FIREWALL_CANON = (
    "zeta(0) = -1/2 is admissible as METAPHOR / IMAGE only. Binding the codomain "
    "value -1/2 to the domain coordinate Re(s)=1/2 is a type error "
    "(CLOSED-NEGATIVE). NP framing is STRUCTURAL ANALOGY only, never a mechanism."
)


class FirewallError(TypeError):
    """Raised when the metaphor/mechanism boundary is crossed."""


class UndefinedMetricError(ValueError):
    """Raised when a headline number lacks an operational metric definition."""


class NonSovereigntyError(ValueError):
    """Raised when the evaluator ceiling h < 1 is violated (FLAG-001)."""


# --- provenance-tagged quantities -------------------------------------------

@dataclass(frozen=True)
class Quantity:
    """A number that carries its type slot (`role`), so illegal binds can be
    detected. The archetype: zeta(0) = -1/2 has role 'codomain_value'."""

    value: float
    role: str            # e.g. "codomain_value", "domain_coordinate", "score"
    label: str = ""


def bind_domain_coordinate(q: Quantity) -> float:
    """Bind a quantity into a domain-coordinate slot.

    The standing zeta(0) firewall, made executable: a codomain value may not be
    transported into a domain coordinate.
    """
    if q.role == "codomain_value":
        raise FirewallError(
            f"illegal transport: codomain value {q.label or q.value!r} -> "
            f"domain coordinate. {FIREWALL_CANON}"
        )
    return float(q.value)


# --- metric discipline (retires the undefined 94% / 60% headline numbers) ----

@dataclass(frozen=True)
class Metric:
    """An operationally defined number. No bare headline floats are admitted:
    a headline figure must say what is counted, over what population, from what
    source."""

    value: float
    counted: str
    population: str
    source: str

    def __post_init__(self) -> None:
        for name in ("counted", "population", "source"):
            if not str(getattr(self, name)).strip():
                raise UndefinedMetricError(
                    f"headline metric (value={self.value!r}) is missing its "
                    f"'{name}' definition; undefined headline numbers are barred in v4"
                )


@dataclass(frozen=True)
class Analogy:
    """An explicitly fenced analogy. Status is pinned to ANALOGY and it cannot be
    used as a mechanism."""

    name: str
    maps_to: str
    status: Status = Status.ANALOGY

    def as_mechanism(self):  # noqa: ANN201 - always raises
        raise FirewallError(
            f"{self.name!r} is fenced ANALOGY and cannot be used as a mechanism. "
            f"{FIREWALL_CANON}"
        )


def require_h_below_one(h: float) -> float:
    """Enforce evaluator non-sovereignty: 0 <= h < 1 (FLAG-001)."""
    if not (0.0 <= h < 1.0):
        raise NonSovereigntyError(
            f"h = {h}: evaluator non-sovereignty requires 0 <= h < 1 "
            "(Godel does not ground h; non-sovereignty grounds h)."
        )
    return float(h)
