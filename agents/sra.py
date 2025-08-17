# agents/sra.py
from typing import Any


def sra_rules(state: dict[str, Any]) -> dict[str, Any]:
    state["rules_json"] = {
        "game": "8-ball",
        "version": "dev-seed",
        "sections": {
            "UPA-8B-3.3.4": {"name": "Break Types", "allowed_values": ["Y", "N", "F", "8"]},
            "UPA-8B-2.1.0": {"name": "Innings", "constraints": {"type": "int", "min": 0}},
        },
    }
    return state
