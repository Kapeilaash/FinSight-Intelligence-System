from __future__ import annotations

from typing import Any

from .base_agent import BaseAgent


class WriterAgent(BaseAgent):
    """Assembles an institutional-style markdown brief from agent outputs."""

    def __init__(self) -> None:
        super().__init__(name="writer")

    def build_markdown(
        self,
        topic: str,
        news: list[str],
        financials: dict[str, Any],
        critic_verdict: str,
        critic_reason: str,
    ) -> str:
        news_block = "\n".join(f"- {line}" for line in news) or "- _(No headlines)_"

        fin_lines = []
        for key, val in (financials or {}).items():
            fin_lines.append(f"- **{key}:** {val}")
        fin_block = "\n".join(fin_lines) if fin_lines else "- _(No structured metrics)_"

        qa_note = ""
        if critic_verdict != "pass":
            qa_note = (
                f"\n\n> **Quality review:** `{critic_verdict}` — {critic_reason or 'See pipeline logs.'}\n"
                "> _Delivered after max retries or best-effort merge._\n"
            )

        return f"""# Market Intelligence Brief: {topic}

## Executive Summary
Automated multi-agent pass for **{topic}** combining recent headlines and structured (mock) financials. This document is for workflow validation; replace mocks with live SQL and expanded LLM prose when ready.{qa_note}

## Market News Overview
{news_block}

## Financial Analysis (structured / mock DB)
{fin_block}

## Risk Analysis
- **Data risk:** Mock financials do not reflect live filings; verify against primary sources before decisions.
- **News risk:** Headlines may omit material context; cross-check with exchange disclosures and macro data.

## Final Investment Insight
Pipeline successfully fused **news** + **financial metrics** for `{topic}` with critic gate `{critic_verdict}`. Upgrade Analyst node to SQL, Research node depth, and Writer node to LLM-guided narrative for production-grade briefs.
"""

    def run(self, analysis: Any) -> dict:
        raise NotImplementedError("Use build_markdown() from the graph writer node.")
