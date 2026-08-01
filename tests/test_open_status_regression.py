from pathlib import Path

def test_rh_coleman_open():
    text = (Path(__file__).resolve().parents[1] / "STATUS.md").read_text()
    assert "RH" in text and "OPEN" in text
    assert "Coleman" in text
    low = text.lower()
    assert "rh proved" not in low
    assert "coleman proved" not in low
