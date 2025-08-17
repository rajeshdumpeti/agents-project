# pipelines/plan_graph.py
from collections.abc import Callable
from typing import Any

Stage = Callable[[dict[str, Any]], dict[str, Any]]


class Pipeline:
    def __init__(self, stages: list[Stage]):
        self.stages = stages

    def run(self, state: dict[str, Any]) -> dict[str, Any]:
        for stage in self.stages:
            state = stage(state)
        return state
