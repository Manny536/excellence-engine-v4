import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANTECEDENT = ROOT / "antecedent"

EXPECTED_FILES = {
    "README.md",
    "closed-lanes.md",
    "dependency-tower.md",
    "exact-zero-location-burden.md",
    "faithful-kappa-bridge.md",
    "falsification-gates.md",
    "kakeya-as-antecedent-riemann.md",
    "prime-carrying-continuation.md",
    "sufficiency-trap.md",
}

REQUIRED_SURFACE = {
    "README.md": (
        "ClaimRecord",
        "ExactCarrier(B)",
        "A_dep",
        "A_inv",
        "A_con",
        "HELD-RETAINED",
        "L²_C",
        "h < 1",
    ),
    "closed-lanes.md": ("ClosureCertificate", "CL-KSIGMA", "CL-WP5B", "Reopening rule"),
    "dependency-tower.md": ("T_bound", "≼_m", "Fib(B)", "ExactCarrier(B)"),
    "exact-zero-location-burden.md": ("ExactCarrier(B)", "EC-1", "EC-9", "NonCircular(B)"),
    "faithful-kappa-bridge.md": ("Fκ-1", "Fκ-6", "Off(a)", "non-circular computability"),
    "falsification-gates.md": ("Gate :=", "FG-κ", "FG-ESS", "RETAIN", "RELEASE"),
    "kakeya-as-antecedent-riemann.md": ("ANT-KR-001", "A_dep", "A_inv", "A_con"),
    "prime-carrying-continuation.md": ("PrimeCarrying(B)", "log(p^k)", "Λ(p^k)p^{-k/2}"),
    "sufficiency-trap.md": ("Packaging theorem", "(K₃ ⇒ R) ⇔ R", "CLOSED"),
}


def test_antecedent_surface_has_exactly_nine_markdown_files() -> None:
    assert {path.name for path in ANTECEDENT.glob("*.md")} == EXPECTED_FILES


def test_every_antecedent_file_carries_its_formal_contract() -> None:
    for name, required in REQUIRED_SURFACE.items():
        text = (ANTECEDENT / name).read_text(encoding="utf-8")
        missing = [marker for marker in required if marker not in text]
        assert not missing, f"{name} missing {missing}"


def test_controlling_readme_keeps_relation_and_status_types_separate() -> None:
    text = (ANTECEDENT / "README.md").read_text(encoding="utf-8")
    assert "K→R" in text and "K⇒RH" in text
    assert "mathematical_status(K→R frame) = PROPOSED" in text
    assert "custody_state(K→R frame)       = HELD-RETAINED" in text
    assert "status(RH)                     = OPEN" in text
    assert "status(Coleman Conjecture)     = OPEN" in text
    assert "L²C" not in text


def test_relative_markdown_links_resolve() -> None:
    for path in sorted(ANTECEDENT.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            assert resolved.exists(), f"{path.name}: unresolved link {target}"
