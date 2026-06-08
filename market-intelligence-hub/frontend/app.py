from __future__ import annotations

import sys
from pathlib import Path

# Allow `streamlit run app.py` from the frontend directory
_FRONTEND = Path(__file__).resolve().parent
if str(_FRONTEND) not in sys.path:
    sys.path.insert(0, str(_FRONTEND))

import streamlit as st
import requests
from utils.api_client import backend_base, generate_market_report, health_check

st.set_page_config(page_title="Market Intelligence Hub", layout="wide")
st.title("Market Intelligence Hub")
st.caption("Multi-agent research → analysis → critic → writer (LangGraph + FastAPI)")

with st.sidebar:
    st.subheader("Backend")
    st.text(backend_base())
    if st.button("Ping API"):
        try:
            st.success(health_check())
        except requests.RequestException as e:
            st.error(f"Backend unreachable: {e}")

topic = st.text_input(
    "Stock ticker or market theme",
    placeholder="e.g. TSLA, renewable energy grid",
    help="Sent to FastAPI → LangGraph. Set TAVILY_API_KEY for live news; otherwise mock headlines are used.",
)

if st.button("Generate report", type="primary", disabled=not (topic or "").strip()):
    with st.spinner("Running agent graph (research → analyst → critic → writer)…"):
        try:
            payload = generate_market_report(topic.strip())
        except requests.HTTPError as e:
            st.error(f"API error: {e.response.status_code} — {e.response.text}")
        except requests.RequestException as e:
            st.error(f"Request failed: {e}")
        else:
            st.success(
                f"Critic: **{payload.get('critic_verdict', '')}** "
                f"(retries: {payload.get('retry_loops', 0)})"
            )
            if payload.get("critic_reason"):
                st.info(payload["critic_reason"])
            st.markdown(payload.get("markdown", "_No markdown returned._"))
