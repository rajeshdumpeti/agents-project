# agents/usg.py
from typing import Any, TypedDict


class Story(TypedDict):
    story_id: str
    as_a: str
    i_want: str
    so_that: str
    acceptance_criteria: list[dict[str, str]]
    rules: list[str]


def usg_stories(state: dict[str, Any]) -> dict[str, Any]:
    # rules = state.get("rules_json", {})
    _ = state.get("requirements", {})
    state["stories"] = [
        Story(
            story_id="US-08-001",
            as_a="Captain",
            i_want="record break type per rack",
            so_that="the digital scoresheet matches UPA rules",
            acceptance_criteria=[
                {"id": "AC1", "text": "User can set Y/N/F/8 per rack"},
                {"id": "AC2", "text": "Selected break type persists and reloads"},
            ],
            rules=["UPA-8B-3.3.4"],
        ),
        Story(
            story_id="US-08-002",
            as_a="Captain",
            i_want="record innings per rack",
            so_that="totals and stats stay accurate",
            acceptance_criteria=[
                {"id": "AC1", "text": "Innings accepts integer values >= 0"},
                {"id": "AC2", "text": "Negative values are rejected"},
            ],
            rules=["UPA-8B-2.1.0"],
        ),
    ]
    return state
