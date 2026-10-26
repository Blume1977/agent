from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from agent_cli.a38 import load_policy
from agent_cli.pr_guard_config import load_pr_guard_config

pytestmark = pytest.mark.no_pg

REPO_ROOT = Path(__file__).resolve().parent.parent


def _workflow_jobs() -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    workflows = REPO_ROOT / ".github" / "workflows"
    for path in sorted(workflows.glob("*.yml")) + sorted(workflows.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for job in (data.get("jobs") or {}).keys():
            found.add((f".github/workflows/{path.name}", str(job)))
    return found


def test_manifest_loads_and_classifies_every_workflow_job() -> None:
    policy = load_policy((REPO_ROOT / ".github" / "a38.json").read_text(encoding="utf-8"))
    required = {(job["workflow"], job["job"]) for job in policy["jobs"]}
    excluded = {
        (entry["workflow"], entry["job"]) for entry in json.loads(
            (REPO_ROOT / ".github" / "a38.json").read_text(encoding="utf-8")
        )["exclusions"]
    }
    classified = required | excluded
    found = _workflow_jobs()
    assert classified == found, (
        f"workflow inventory drifted: unclassified={sorted(found - classified)} "
        f"stale={sorted(classified - found)}"
    )


def test_pr_guard_config_is_valid() -> None:
    text = (REPO_ROOT / ".github" / "pr-guard.json").read_text(encoding="utf-8")
    config = load_pr_guard_config(text)
    assert config is not None
