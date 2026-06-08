from typing import Any, TypedDict


class GraphState(TypedDict, total=False):
    """Shared state for the market intelligence LangGraph."""

    topic: str
    news: list[str]
    financials: dict[str, Any]
    critic_verdict: str
    critic_reason: str
    retry: int
    markdown: str
