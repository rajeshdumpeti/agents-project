# tests/test_pipeline_smoke.py
from agents.prl import prl_clarify
from agents.qat import qat_tests
from agents.sra import sra_rules
from agents.usg import usg_stories
from pipelines.plan_graph import Pipeline


def test_pipeline_smoke():
    p = Pipeline([prl_clarify, sra_rules, usg_stories, qat_tests])
    out = p.run({"inputs": {"project_plan": "UPA scorer MVP for 8-ball"}})
    assert "clarifications" in out
    assert "rules_json" in out
    assert "stories" in out and len(out["stories"]) >= 2
    assert "test_plan" in out and len(out["test_plan"]) >= 1
