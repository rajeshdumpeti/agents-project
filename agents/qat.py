# agents/qat.py
from typing import Any


def qat_tests(state: dict[str, Any]) -> dict[str, Any]:
    stories = state.get("stories", [])
    plan: list[str] = []
    for s in stories:
        if "break type" in s["i_want"]:
            plan.append("Open Scoring -> set break type Y -> save -> reopen -> verify Y")
            plan.append("Set break type F -> save -> reopen -> verify F")
        if "innings" in s["i_want"]:
            plan.append("Enter innings 0,1,2 -> save -> verify totals")
            plan.append("Enter -1 -> expect validation error")
    state["test_plan"] = plan
    return state
