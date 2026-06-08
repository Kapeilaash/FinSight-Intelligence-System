from __future__ import annotations

from typing import Any

from core.web_search import search_news_tavily

from .base_agent import BaseAgent


def get_news(stock: str) -> list[str]:
    """
    Headlines for *stock*: Tavily when TAVILY_API_KEY is set, else deterministic mock.
    """
    tavily_lines = search_news_tavily(f"{stock} stock market news earnings")
    if tavily_lines:
        return [f"[{stock}] {line}" for line in tavily_lines]
    return [f"{stock} shows strong market growth today"]


class ResearcherAgent(BaseAgent):
    """Collects market news for a stock or theme (Tavily optional, mock fallback)."""

    def __init__(self) -> None:
        super().__init__(name="researcher")

    def run(self, stock: str) -> dict:
        return {"stock": stock, "news": get_news(stock)}
