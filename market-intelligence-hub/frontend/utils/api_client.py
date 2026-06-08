from __future__ import annotations

import os

import requests

DEFAULT_BASE = "http://127.0.0.1:8000"


def backend_base() -> str:
    return os.getenv("BACKEND_URL", DEFAULT_BASE).rstrip("/")


def generate_market_report(topic: str, timeout: int = 120) -> dict:
    """POST /api/reports/generate and return JSON (markdown + metadata)."""
    url = f"{backend_base()}/api/reports/generate"
    resp = requests.post(url, json={"topic": topic}, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def health_check() -> dict:
    """GET /api/test — lightweight backend probe."""
    url = f"{backend_base()}/api/test"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()
