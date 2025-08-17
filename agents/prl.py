# agents/prl.py
from typing import Any


def prl_clarify(state: dict[str, Any]) -> dict[str, Any]:
    inputs = state.get("inputs", {})
    plan = inputs.get("project_plan", "UPA MVP 8-ball")
    state["clarifications"] = {
        "questions": [
            "Do we record break type per rack (Y/N/F/8)?",
            "How many timeouts per player?",
            "Track safeties per rack or per match?",
        ],
        "assumptions": [
            "Innings is an integer >= 0 per rack",
            "Break types are constrained to Y/N/F/8",
        ],
        "summary": f"Clarified plan for: {plan}",
    }
    # For now, treat assumptions as confirmed to keep the demo moving
    state["requirements"] = {"confirmed": ["break_type_per_rack", "innings_per_rack"]}
    return state
