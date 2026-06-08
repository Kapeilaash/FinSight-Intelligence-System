from .base_agent import BaseAgent


def get_financial_data(stock: str) -> dict:
    """Mock financials for *stock* (replaces SQL until real queries exist)."""
    return {
        "stock": stock,
        "revenue": "80B",
        "profit_margin": "15%",
        "growth": "12%",
        "debt_ratio": "low",
    }


class AnalystAgent(BaseAgent):
    """Extracts structured financial metrics; currently returns mock data only."""

    def __init__(self) -> None:
        super().__init__(name="analyst")

    def run(self, stock: str) -> dict:
        return get_financial_data(stock)
