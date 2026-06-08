from __future__ import annotations

from typing import Any

from .graph_builder import build_report_graph

_graph = None


def _get_graph():
    global _graph
    if _graph is None:
        _graph = build_report_graph()
    return _graph


def run_report_workflow(topic: str) -> dict[str, Any]:
    """
    Execute the full multi-agent graph for a stock or market theme.

    Returns markdown plus lightweight metadata for the API layer.
    """
    topic = topic.strip()
    if not topic:
        raise ValueError("topic must be non-empty")

    graph = _get_graph()
    final: dict[str, Any] = graph.invoke({"topic": topic})

    return {
        "topic": topic,
        "markdown": final.get("markdown", ""),
        "critic_verdict": final.get("critic_verdict", ""),
        "critic_reason": final.get("critic_reason", ""),
        "retry_loops": final.get("retry", 0),
    }
