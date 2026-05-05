# Benchmark Release

This directory contains the public DisasterAgentBench release files:

- frozen evaluation configuration
- gold-removed hidden-test tasks
- hidden-test package manifest
- formal, supplementary, held-out, and validation run outputs

Hidden-test gold labels are not included in this public directory. Maintainer-side
gold files used for strict scoring are withheld from the public artifact.

## Active release files

- `evaluation_config.json`
  - frozen benchmark evaluation configuration
- `hidden_test_package_manifest.json`
  - manifest for the released hidden-test package
- `hidden_test_tasks.jsonl`
  - 262 hidden-test task records with top-level `gold` fields removed
- `runs_formal_updated/`
  - main hidden-test runs and aggregate tables
- `runs_supplementary_20260503/`
  - supplementary review, oracle, and ablation runs
- `runs_transfer_heldout_20260504_separate/`
  - hazard-held-out, region-held-out, and time-held-out transfer runs
- `validation_supplementary_20260503/`
  - human-reference, agreement, oracle-validity, and validation summaries

## Non-release helpers

Some template and provenance files may be present for auditability, but they are
not required for scoring or reproducing reported tables:

- `evaluation_config.template.json`
- `task_record.template.json`
- `hidden_test_package_manifest.template.json`
- `assessment_report_candidate_units.csv`

## Practical usage

Use:

- `evaluation_config.json`
- `hidden_test_package_manifest.json`
- `hidden_test_tasks.jsonl`
- `runs_*`

Do not treat template files as the frozen scorer boundary.

## Release boundary

The public hidden-test task file is gold-removed. Private tile-server URLs and
local filesystem paths are not part of the public release boundary. When a task
record refers to a map source, the released artifact should be read as exposing
the map-source identifier and task metadata, not as redistributing the underlying
imagery or map tiles.
