"""Validate the public DisasterAgentBench release boundary.

The checks are intentionally lightweight and dependency-free. They verify that
released JSON/JSONL files parse, hidden-test tasks do not expose top-level gold
answers, required run artifacts are present, and public tracked files do not
contain private filesystem paths or private tile-server addresses.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REQUIRED_RUN_ARTIFACTS = {
    "config.json",
    "predictions.jsonl",
    "trace.jsonl",
    "metrics.json",
    "failures.csv",
}

PRIVATE_PATTERNS = (
    "192.168.",
    "127.0.0.1",
    "localhost",
    "D:\\",
    "C:\\",
    "file://",
)


def repo_root() -> Path:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True, stderr=subprocess.DEVNULL
        ).strip()
        return Path(out)
    except Exception:
        return Path.cwd()


def tracked_files(root: Path) -> list[Path]:
    try:
        out = subprocess.check_output(
            ["git", "ls-files"], cwd=root, text=True, stderr=subprocess.DEVNULL
        )
        return [root / line for line in out.splitlines() if line.strip()]
    except Exception:
        return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]


def check_json_files(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in {".json", ".jsonl"}:
            continue
        try:
            if path.suffix.lower() == ".json":
                json.loads(path.read_text(encoding="utf-8"))
            else:
                with path.open(encoding="utf-8") as handle:
                    for lineno, line in enumerate(handle, 1):
                        if line.strip():
                            json.loads(line)
        except Exception as exc:
            errors.append(f"{path}: JSON parse failed: {exc}")
    return errors


def check_hidden_gold(root: Path) -> list[str]:
    errors: list[str] = []
    task_file = root / "benchmark_release" / "hidden_test_tasks.jsonl"
    if not task_file.exists():
        return [f"{task_file}: missing public hidden-test task file"]

    total = 0
    with task_file.open(encoding="utf-8") as handle:
        for lineno, line in enumerate(handle, 1):
            if not line.strip():
                continue
            total += 1
            obj = json.loads(line)
            if "gold" in obj:
                errors.append(f"{task_file}:{lineno}: top-level gold field is public")
            if not obj.get("distribution", {}).get("gold_removed", False):
                errors.append(f"{task_file}:{lineno}: missing distribution.gold_removed=true")

    if total != 262:
        errors.append(f"{task_file}: expected 262 tasks, found {total}")
    return errors


def check_public_gold_exposure(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    release_root = root / "benchmark_release"
    for path in files:
        if path.suffix.lower() != ".jsonl" or release_root not in path.parents:
            continue
        try:
            with path.open(encoding="utf-8") as handle:
                for lineno, line in enumerate(handle, 1):
                    if not line.strip():
                        continue
                    obj = json.loads(line)
                    if isinstance(obj, dict) and "gold" in obj:
                        rel = path.relative_to(root)
                        errors.append(f"{rel}:{lineno}: top-level gold field is public")
                        break
        except Exception as exc:
            rel = path.relative_to(root)
            errors.append(f"{rel}: JSONL scan failed: {exc}")
    return errors


def check_required_run_artifacts(root: Path) -> list[str]:
    errors: list[str] = []
    release_root = root / "benchmark_release"
    for seed_dir in release_root.rglob("seed_*"):
        if not seed_dir.is_dir():
            continue
        present = {p.name for p in seed_dir.iterdir() if p.is_file()}
        missing = sorted(REQUIRED_RUN_ARTIFACTS - present)
        if missing:
            errors.append(f"{seed_dir}: missing {', '.join(missing)}")
    return errors


def check_private_patterns(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = path.relative_to(root)
        for pattern in PRIVATE_PATTERNS:
            if pattern in text:
                errors.append(f"{rel}: contains private pattern {pattern!r}")
                break
    return errors


def main() -> int:
    root = repo_root()
    files = tracked_files(root)

    errors: list[str] = []
    errors.extend(check_json_files(files))
    errors.extend(check_hidden_gold(root))
    errors.extend(check_public_gold_exposure(root, files))
    errors.extend(check_required_run_artifacts(root))
    errors.extend(check_private_patterns(root, files))

    if errors:
        print("Release validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Release validation passed.")
    print(f"Checked {len(files)} tracked files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
