from __future__ import annotations

from typing import Any, Literal

from .base_agent import BaseAgent

Verdict = Literal["pass", "retry_research", "retry_analyst"]


class CriticAgent(BaseAgent):
    """
    Validates that news and mock DB financials align with the requested topic.

    Uses deterministic rules (no LLM) so the graph is stable without API keys.
    """

    def __init__(self) -> None:
        super().__init__(name="critic")

    def evaluate(
        self,
        topic: str,
        news: list[str],
        financials: dict[str, Any],
    ) -> dict[str, str]:
        topic_l = topic.strip().lower()
        if not news:
            return {"verdict": "retry_research", "reason": "No news items were collected."}

        if not financials:
            return {"verdict": "retry_analyst", "reason": "No financial metrics payload."}

        fin_stock = str(financials.get("stock", "")).strip().lower()
        if fin_stock and fin_stock != topic_l:
            return {
                "verdict": "retry_analyst",
                "reason": f"Financials symbol '{financials.get('stock')}' does not match topic '{topic}'.",
            }

        blob = " ".join(news).lower()
        if topic_l not in blob:
            return {
                "verdict": "retry_research",
                "reason": "News corpus does not clearly reference the requested topic.",
            }

        return {"verdict": "pass", "reason": ""}

    def run(self, report: Any) -> dict:
        raise NotImplementedError("Use evaluate() for the critic step.")
