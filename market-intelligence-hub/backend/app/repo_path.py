"""Ensure project root is on sys.path so `agents`, `orchestration`, and `core` resolve."""
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
_root_str = str(_ROOT)
if _root_str not in sys.path:
    sys.path.insert(0, _root_str)
