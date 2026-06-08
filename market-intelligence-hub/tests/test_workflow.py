from orchestration.workflow import run_report_workflow


def test_run_report_workflow_smoke():
    out = run_report_workflow("NVDA")
    assert out["topic"] == "NVDA"
    assert "markdown" in out
    assert "## Executive Summary" in out["markdown"]
