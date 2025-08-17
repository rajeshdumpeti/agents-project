# run.py
from agents.prl import prl_clarify
from agents.qat import qat_tests
from agents.sra import sra_rules
from agents.usg import usg_stories
from pipelines.plan_graph import Pipeline

if __name__ == "__main__":
    pipeline = Pipeline([prl_clarify, sra_rules, usg_stories, qat_tests])
    initial = {"inputs": {"project_plan": "UPA scorer MVP for 8-ball"}}
    result = pipeline.run(initial)

    print("\n=== Clarifications ===")
    print(result["clarifications"])

    print("\n=== Rules JSON ===")
    print(result["rules_json"])

    print("\n=== Stories ===")
    for s in result["stories"]:
        print(s)

    print("\n=== Test Plan ===")
    for t in result["test_plan"]:
        print("-", t)
