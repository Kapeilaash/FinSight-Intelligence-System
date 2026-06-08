from .base_agent import BaseAgent


def get_news(stock: str) -> list[str]:
    """Placeholder headlines for *stock* (no external APIs yet)."""
    return [f"{stock} shows strong market growth today"]


class ResearcherAgent(BaseAgent):
    """Collects market news for a stock; currently returns dummy data only."""

    def __init__(self) -> None:
        super().__init__(name="researcher")

    def run(self, stock: str) -> dict:
        return {"stock": stock, "news": get_news(stock)}
