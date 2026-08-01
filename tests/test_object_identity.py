from pathlib import Path
import importlib.util

def test_object_identity():
    path = Path(__file__).resolve().parents[1] / "probes/object_identity_probe.py"
    spec = importlib.util.spec_from_file_location("o", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.main() == 0
