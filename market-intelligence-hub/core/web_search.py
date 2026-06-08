"""Web search integration (Tavily when API key is set; otherwise callers use mocks)."""
from __future__ import annotations

import os
from typing import Any

import httpx

TAVILY_URL = "https://api.tavily.com/search"


def search_news_tavily(query: str, max_results: int = 5) -> list[str]:
    """
    Run a Tavily search and return short headline-style strings.

    Returns an empty list if TAVILY_API_KEY is unset or the request fails.
    """
    api_key = os.getenv("TAVILY_API_KEY", "").strip()
    if not api_key:
        return []

    payload: dict[str, Any] = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic",
        "max_results": max_results,
        "include_answer": False,
    }
    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.post(TAVILY_URL, json=payload)
            resp.raise_for_status()
            data = resp.json()
    except (httpx.HTTPError, ValueError, KeyError):
        return []

    lines: list[str] = []
    for item in data.get("results") or []:
        title = (item.get("title") or "").strip()
        content = (item.get("content") or item.get("snippet") or "").strip()
        if title and content:
            lines.append(f"{title} — {content[:240]}")
        elif title:
            lines.append(title)
        elif content:
            lines.append(content[:280])
    return lines[:max_results]
