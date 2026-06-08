# Market Intelligence Hub

Autonomous **multi-agent** pipeline (Research → Analyst → **Critic retry loop** → Writer) orchestrated with **LangGraph**, exposed through **FastAPI**, and driven from a **Streamlit** UI. Mock financials and optional **Tavily** news keep the stack runnable without a database or LLM keys.

## Architecture (at a glance)

| Layer | Role |
|--------|------|
| **Streamlit** (`frontend/app.py`) | User enters a stock ticker or market theme; displays markdown report. |
| **FastAPI** (`backend/app/`) | `POST /api/reports/generate` runs the graph and returns JSON + markdown. |
| **LangGraph** (`orchestration/`) | `StateGraph`: research → analyst → critic → conditional retry → writer. |
| **Agents** (`agents/`) | Researcher (Tavily or mock), Analyst (mock dict “SQL”), Critic (rules), Writer (template). |
| **Core** (`core/`) | `web_search.py` — Tavily HTTP client when `TAVILY_API_KEY` is set. |

Orchestration uses **LangGraph** (explicit state machine + conditional edges). You can later add **CrewAI** or **PydanticAI** inside individual nodes without replacing the graph.

## Quick start

### 1. Install

```powershell
cd "G:\FinSight Intelligence System\market-intelligence-hub"
python -m pip install -r requirements.txt
```

### 2. Backend

From the project root (recommended; avoids Python path issues):

```powershell
python -m uvicorn app.main:app --reload --app-dir backend --host 127.0.0.1 --port 8000
```

- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Health: `GET http://127.0.0.1:8000/api/test`
- Report: `POST http://127.0.0.1:8000/api/reports/generate` with body `{"topic": "TSLA"}`

On Windows, prefer **`python -m uvicorn`** if `uvicorn` is not on your PATH.

### 3. Frontend

```powershell
cd frontend
python -m streamlit run app.py
```

Optional: `BACKEND_URL=http://127.0.0.1:8000` if the API is not on localhost.

### 4. Optional: live news (Tavily)

```powershell
set TAVILY_API_KEY=your_key_here
```

Without it, the Research agent uses deterministic mock headlines (still passes the critic when the topic appears in text).

## Tests

```powershell
cd "G:\FinSight Intelligence System\market-intelligence-hub"
python -m pytest tests/ -q
```

## Upgrade path

- Replace **mock financials** in `agents/analyst_agent.py` with SQL via `core/db_client.py`.
- Enrich **Writer** with `core/llm_client.py` (OpenAI / Gemini) for prose instead of templates.
- Tighten **Critic** with an LLM or structured checks on numeric consistency.
