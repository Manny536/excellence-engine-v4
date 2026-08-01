from pathlib import Path

def test_closed_negative_present():
    text = (Path(__file__).resolve().parents[1] / "STATUS.md").read_text()
    assert "CLOSED-NEGATIVE" in text
