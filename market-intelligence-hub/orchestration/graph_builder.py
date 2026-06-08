from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from .nodes import (
    analyst_node,
    critic_node,
    research_node,
    route_after_critic,
    writer_node,
)
from .state import GraphState


def build_report_graph():
    """Research → Analyst → Critic → (retry loop) → Writer."""
    builder = StateGraph(GraphState)
    builder.add_node("research", research_node)
    builder.add_node("analyst", analyst_node)
    builder.add_node("critic", critic_node)
    builder.add_node("writer", writer_node)

    builder.add_edge(START, "research")
    builder.add_edge("research", "analyst")
    builder.add_edge("analyst", "critic")
    builder.add_conditional_edges(
        "critic",
        route_after_critic,
        {
            "research": "research",
            "analyst": "analyst",
            "writer": "writer",
        },
    )
    builder.add_edge("writer", END)
    return builder.compile()
