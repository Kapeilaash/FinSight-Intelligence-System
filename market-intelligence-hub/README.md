# Market Intelligence Hub

Scaffold for the Market Intelligence Hub project.

Structure and placeholder files created for backend, frontend, agents, orchestration, core, data, configs, tests, and logs.

## Backend (FastAPI)

On Windows, the `uvicorn` script is often **not on your PATH** (it lives under Python’s `Scripts` folder). Use the module form so it always uses the same Python you installed into:

```powershell
cd "path\to\market-intelligence-hub"
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --app-dir backend --host 127.0.0.1 --port 8000
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Alternatively, from the `backend` folder:

```powershell
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
