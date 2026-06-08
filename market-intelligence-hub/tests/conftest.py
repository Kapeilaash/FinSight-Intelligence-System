"""Pytest bootstrap: project root + backend on path, then register repo imports."""
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "backend"):
    _s = str(_p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import app.repo_path  # noqa: E402, F401
