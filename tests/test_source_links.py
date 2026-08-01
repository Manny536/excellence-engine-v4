from pathlib import Path

def test_source_map_links():
    text = (Path(__file__).resolve().parents[1] / "SOURCE_MAP.md").read_text()
    for url in [
        "https://github.com/Manny536/kakeyalogic",
        "https://github.com/Manny536/claude-v6",
        "https://github.com/Manny536/LoveLabs-LCA",
        "https://github.com/Manny536/grok-terminal",
    ]:
        assert url in text
