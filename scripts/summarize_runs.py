"""Summarize packaged run metrics into a CSV table."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def iter_metrics_files(root: Path):
    for path in root.rglob("metrics.json"):
        if path.is_file():
            yield path


def flatten(prefix: str, value, out: dict[str, object]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            next_prefix = f"{prefix}.{key}" if prefix else key
            flatten(next_prefix, child, out)
    elif isinstance(value, (int, float, str, bool)) or value is None:
        out[prefix] = value


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("benchmark_release")
    rows: list[dict[str, object]] = []

    for path in iter_metrics_files(root):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue

        row: dict[str, object] = {"path": str(path.relative_to(root))}
        flatten("", data, row)
        rows.append(row)

    if not rows:
        print("No metrics files found.", file=sys.stderr)
        return 1

    fieldnames = sorted({key for row in rows for key in row.keys()})
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
