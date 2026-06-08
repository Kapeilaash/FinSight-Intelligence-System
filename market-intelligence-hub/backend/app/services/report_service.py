from __future__ import annotations

import app.repo_path  # noqa: F401 — register project root import path

from orchestration.workflow import run_report_workflow


def generate_report(request_data: dict) -> dict:
    """Run LangGraph multi-agent workflow; returns markdown-focused payload."""
    topic = (request_data.get("topic") or request_data.get("symbol") or "").strip()
    if not topic:
        raise ValueError("`topic` (or legacy `symbol`) is required")
    return run_report_workflow(topic)
