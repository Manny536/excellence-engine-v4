import re
from pathlib import Path

def test_source_hashes_md():
    text = (Path(__file__).resolve().parents[1] / "outcomes/artifacts/source-hashes.md").read_text()
    assert len(re.findall(r"`[a-f0-9]{64}`", text)) >= 4
