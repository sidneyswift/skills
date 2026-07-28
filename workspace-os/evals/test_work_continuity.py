from __future__ import annotations

import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ASSETS = REPO_ROOT / "workspace-os" / "assets"


def render_doctor(workspace: Path) -> Path:
    template = (ASSETS / "doctor.py.tmpl").read_text(encoding="utf-8")
    rendered = (
        template.replace("{DOMAIN}", "Test")
        .replace("{OS}", "test")
        .replace("{PIPELINE}", "pipeline")
        .replace("{ENTITY}", "entities")
    )
    script = workspace / "scripts" / "doctor.py"
    script.parent.mkdir(parents=True, exist_ok=True)
    script.write_text(rendered, encoding="utf-8")
    return script


def package_text(
    *,
    work_id: str = "memory-rd",
    status: str = "active",
    next_action: str = "Run W-002.",
    blocker: str = "Not applicable.",
    evidence: str = "No terminal outcome yet.",
    durable_value: str = "Not evaluated until closure.",
    closed: str = "",
) -> str:
    closed_line = f"closed: {closed}\n" if closed else ""
    return f"""---
id: {work_id}
status: {status}
owner: Test Owner
updated: 2026-07-28
{closed_line}---

# Memory R&D

## Outcome
Make agent decisions reusable.

## Done when
- [ ] A fresh agent retrieves the current decision.

## Current state
The baseline is recorded.

## Next action
{next_action}

## Blocker or review
{blocker}

## Links and authority
- Package coordination: this file

## Evidence and outcome
{evidence}

## Durable value
{durable_value}
"""


def run_doctor(workspace: Path) -> str:
    script = render_doctor(workspace)
    result = subprocess.run(
        ["python3", str(script), str(workspace)],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout


def write_package(workspace: Path, folder: str, text: str) -> Path:
    package = workspace / "work" / folder
    package.mkdir(parents=True, exist_ok=True)
    readme = package / "README.md"
    readme.write_text(text, encoding="utf-8")
    return readme


def write_work_contract(workspace: Path, entries: list[tuple[str, str]]) -> None:
    work = workspace / "work"
    work.mkdir(parents=True, exist_ok=True)
    (work / "AGENTS.md").write_text("# Managed-work contract\n", encoding="utf-8")
    (work / "CLAUDE.md").symlink_to("AGENTS.md")
    lines = [
        "# Managed work",
        "",
        "<!-- WORK-INDEX:START -->",
        *[
            f"- [{folder}]({folder}/README.md) — {status} — Test Owner — updated 2026-07-28"
            for folder, status in entries
        ],
        "<!-- WORK-INDEX:END -->",
        "",
    ]
    (work / "README.md").write_text("\n".join(lines), encoding="utf-8")


def work_findings(output: str) -> list[str]:
    return [
        line
        for line in output.splitlines()
        if "[FINDING] work package:" in line
    ]


class WorkTemplateContractTests(unittest.TestCase):
    def test_required_templates_exist(self) -> None:
        names = {
            "work-AGENTS.md.tmpl",
            "work-README.md.tmpl",
            "work-package-README.md.tmpl",
            "work-plan.md.tmpl",
            "process-input-SKILL.md.tmpl",
        }
        self.assertEqual(names, {path.name for path in ASSETS.iterdir() if path.name in names})

    def test_package_readme_is_the_canonical_record(self) -> None:
        text = (ASSETS / "work-package-README.md.tmpl").read_text(encoding="utf-8")
        for field in ("id:", "status:", "owner:", "updated:"):
            self.assertIn(field, text)
        for heading in (
            "## Outcome",
            "## Done when",
            "## Current state",
            "## Next action",
            "## Blocker or review",
            "## Links and authority",
            "## Evidence and outcome",
            "## Durable value",
        ):
            self.assertIn(heading, text)

    def test_optional_plan_does_not_duplicate_package_state(self) -> None:
        text = (ASSETS / "work-plan.md.tmpl").read_text(encoding="utf-8")
        self.assertNotRegex(text, re.compile(r"^status:", re.MULTILINE | re.IGNORECASE))
        self.assertNotRegex(text, re.compile(r"^owner:", re.MULTILINE | re.IGNORECASE))
        self.assertIn("## Work items", text)

    def test_work_contract_contains_every_lifecycle_status(self) -> None:
        text = (ASSETS / "work-AGENTS.md.tmpl").read_text(encoding="utf-8")
        for status in ("active", "blocked", "paused", "review", "complete", "cancelled"):
            self.assertIn(f"`{status}`", text)

    def test_process_input_uses_the_required_organ_name(self) -> None:
        text = (ASSETS / "process-input-SKILL.md.tmpl").read_text(encoding="utf-8")
        self.assertIn("name: {OS}-system-process-input", text)
        self.assertIn("work/AGENTS.md", text)


class BuilderContractTests(unittest.TestCase):
    def test_builder_bootstraps_managed_work_before_discovery(self) -> None:
        text = (REPO_ROOT / "workspace-os" / "SKILL.md").read_text(encoding="utf-8")
        bootstrap = text.index("Bootstrap managed work")
        discovery = text.index("Discovery & Design")
        self.assertLess(bootstrap, discovery)
        for asset in (
            "work-AGENTS.md.tmpl",
            "work-README.md.tmpl",
            "work-package-README.md.tmpl",
            "process-input-SKILL.md.tmpl",
        ):
            self.assertIn(asset, text)
        self.assertIn("including naming examples", text)

    def test_generated_brain_routes_to_the_work_contract(self) -> None:
        text = (ASSETS / "CLAUDE.md.tmpl").read_text(encoding="utf-8")
        self.assertIn("work/AGENTS.md", text)
        self.assertIn("another session or agent", text)
        self.assertIn("material lifecycle", text)
        self.assertNotIn("50/50", text)
        self.assertNotIn("at least one durable learning each session", text.lower())

    def test_references_define_coordination_without_copying_domain_state(self) -> None:
        blueprint = (
            REPO_ROOT / "workspace-os" / "references" / "blueprint.md"
        ).read_text(encoding="utf-8")
        self.assertIn("coordination overlay", blueprint.lower())
        self.assertIn("stable", blueprint.lower())
        self.assertIn("derived", blueprint.lower())

    def test_agent_adapters_and_routines_route_managed_work(self) -> None:
        references = REPO_ROOT / "workspace-os" / "references"
        packaging = (references / "packaging.md").read_text(encoding="utf-8")
        routine = (ASSETS / "routine.md.tmpl").read_text(encoding="utf-8")
        self.assertIn("work/CLAUDE.md", packaging)
        self.assertIn("work/AGENTS.md", routine)


class WorkDoctorMutationTests(unittest.TestCase):
    def test_valid_active_package_has_no_work_findings(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text())
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertEqual([], work_findings(run_doctor(workspace)))

    def test_duplicate_ids_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text())
            write_package(workspace, "memory-copy", package_text())
            write_work_contract(
                workspace,
                [("memory-rd", "active"), ("memory-copy", "active")],
            )
            self.assertTrue(
                any("duplicate id" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_invalid_status_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="finished"))
            write_work_contract(workspace, [("memory-rd", "finished")])
            self.assertTrue(
                any("invalid status" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_missing_required_heading_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            text = package_text().replace("## Done when", "## Acceptance")
            write_package(workspace, "memory-rd", text)
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("missing section" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_active_package_requires_next_action(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(next_action="Not applicable."))
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("next action" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_blocked_package_requires_continuation_details(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="blocked"))
            write_work_contract(workspace, [("memory-rd", "blocked")])
            self.assertTrue(
                any("blocked details" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_paused_package_requires_restart_details(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="paused"))
            write_work_contract(workspace, [("memory-rd", "paused")])
            self.assertTrue(
                any("paused details" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_review_package_requires_review_details(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="review"))
            write_work_contract(workspace, [("memory-rd", "review")])
            self.assertTrue(
                any("review details" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_terminal_package_requires_closeout(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="complete"))
            write_work_contract(workspace, [("memory-rd", "complete")])
            self.assertTrue(
                any("terminal closeout" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_broken_relative_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            text = package_text().replace(
                "- Package coordination: this file",
                "- Evidence: [missing](missing.md)",
            )
            write_package(workspace, "memory-rd", text)
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("broken link" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_empty_optional_folder_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text())
            (workspace / "work" / "memory-rd" / "research").mkdir()
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("empty optional" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_index_status_mismatch_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="active"))
            write_work_contract(workspace, [("memory-rd", "blocked")])
            self.assertTrue(
                any("index mismatch" in line for line in work_findings(run_doctor(workspace)))
            )


class StaticValidatorContractTests(unittest.TestCase):
    def test_static_validator_scores_the_work_control_surface(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(
                workspace,
                "workspace-os-setup",
                package_text(work_id="workspace-os-setup"),
            )
            write_work_contract(workspace, [("workspace-os-setup", "active")])
            (workspace / "CLAUDE.md").write_text(
                "When work crosses a session or agent boundary, read work/AGENTS.md.\n",
                encoding="utf-8",
            )
            validator = REPO_ROOT / "workspace-os" / "evals" / "validate.py"
            result = subprocess.run(
                ["python3", str(validator), str(workspace), "--json"],
                check=True,
                capture_output=True,
                text=True,
            )
            payload = json.loads(result.stdout)
            check = next(item for item in payload["checks"] if item["id"] == "work_contract")
            self.assertEqual(8, check["points"])
            self.assertEqual("PASS", check["status"])


class OrganContractTests(unittest.TestCase):
    def test_janitor_never_invents_terminal_state(self) -> None:
        text = (ASSETS / "janitor-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        self.assertIn("never complete or cancel", text)
        self.assertIn("derived work index", text)

    def test_learning_is_event_driven_and_allows_clean_noop(self) -> None:
        text = (ASSETS / "compound-learn-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        self.assertIn("meaningful discovery or closure", text)
        self.assertIn("nothing reusable", text)
        self.assertNotIn("every session", text)

    def test_reflect_distinguishes_applied_from_verified(self) -> None:
        text = (ASSETS / "reflect-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        for status in ("proposed", "applied", "verified", "rejected"):
            self.assertIn(status, text)
        self.assertIn("replay", text)
        self.assertNotIn("50/50", text)

    def test_skillify_uses_package_provenance(self) -> None:
        text = (ASSETS / "skillify-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        self.assertIn("package", text)
        self.assertIn("provenance", text)
        self.assertIn("staged", text)


if __name__ == "__main__":
    unittest.main()
