from pathlib import Path
import importlib.util

def test_claim_status():
    path = Path(__file__).resolve().parents[1] / "probes/claim_status_probe.py"
    spec = importlib.util.spec_from_file_location("c", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.main() == 0
