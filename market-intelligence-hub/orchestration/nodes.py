from __future__ import annotations

from typing import Literal

from agents.analyst_agent import AnalystAgent
from agents.critic_agent import CriticAgent
from agents.researcher_agent import ResearcherAgent
from agents.writer_agent import WriterAgent

from .state import GraphState


def research_node(state: GraphState) -> dict:
    agent = ResearcherAgent()
    out = agent.run(state["topic"])
    return {"news": out.get("news", [])}


def analyst_node(state: GraphState) -> dict:
    agent = AnalystAgent()
    return {"financials": agent.run(state["topic"])}


def critic_node(state: GraphState) -> dict:
    agent = CriticAgent()
    verdict = agent.evaluate(
        topic=state["topic"],
        news=state.get("news") or [],
        financials=state.get("financials") or {},
    )
    updates: dict = {
        "critic_verdict": verdict["verdict"],
        "critic_reason": verdict.get("reason", ""),
    }
    if verdict["verdict"] != "pass":
        updates["retry"] = state.get("retry", 0) + 1
    return updates


def writer_node(state: GraphState) -> dict:
    agent = WriterAgent()
    markdown = agent.build_markdown(
        topic=state["topic"],
        news=state.get("news") or [],
        financials=state.get("financials") or {},
        critic_verdict=state.get("critic_verdict", "pass"),
        critic_reason=state.get("critic_reason", ""),
    )
    return {"markdown": markdown}


def route_after_critic(state: GraphState) -> Literal["research", "analyst", "writer"]:
    verdict = state.get("critic_verdict", "pass")
    retry = state.get("retry", 0)
    if verdict == "pass":
        return "writer"
    if retry >= 2:
        return "writer"
    if verdict == "retry_research":
        return "research"
    if verdict == "retry_analyst":
        return "analyst"
    return "writer"
