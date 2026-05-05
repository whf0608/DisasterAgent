# DisasterAgentBench

## Overview

This repository contains benchmark files, frozen evaluation policy files, reproducibility scripts, metadata, and experimental run outputs for **DisasterAgentBench**, an evaluation benchmark for retrieval-grounded disaster assessment with drone-in-the-loop reinspection.

The repository is organized to support:

- inspection of the benchmark specification
- access to the released hidden-test package and evaluation configuration
- audit of formal, supplementary, and held-out experimental runs
- validation of the public artifact boundary
- reproduction of the file contract described in the paper's `Required run artifacts`

## Data

The benchmark definition and released data are centered on the following files and directories:

- `disasteragentbench_preliminary_split.csv`
  - split manifest over train, development, and hidden-test units
- `disasteragentbench_task_schema.json`
  - benchmark task schema
- `benchmark_freeze/`
  - frozen benchmark policy files
  - severity labels, evidence-key registry, report template, and adjudicated override files
- `benchmark_release/hidden_test_tasks.jsonl`
  - distributed hidden-test task instances with gold outputs removed
- `benchmark_release/hidden_test_package_manifest.json`
  - hidden-test package manifest
- `benchmark_release/evaluation_config.json`
  - frozen evaluation configuration
- `croissant_metadata.json`
  - Croissant metadata for the released benchmark package
- `DATASET_CARD.md`
  - dataset-card summary of scope, release boundary, and known limitations
- `LICENSE`
  - mixed-asset license notice covering scripts and released benchmark materials

Hidden-test gold labels are not part of the public repository. They are retained
only by benchmark maintainers for scorer-side evaluation.

## Runs

Experimental outputs are stored under `benchmark_release/`:

- `runs_formal_updated/`
  - main hidden-test runs and aggregate tables
- `runs_supplementary_20260503/`
  - supplementary hidden-test runs, review variants, and ablations
- `runs_transfer_heldout_20260504_separate/`
  - hazard-held-out, region-held-out, and time-held-out transfer runs
- `validation_supplementary_20260503/`
  - validation reports, agreement summaries, oracle checks, and human-reference checks

Each packaged run directory follows the same required file contract:

- `config.json`
- `predictions.jsonl`
- `trace.jsonl`
- `metrics.json`
- `failures.csv`

Many runs also include derived files such as:

- `task_scores.jsonl`
- aggregate summaries
- appendix table exports
- pairwise comparison outputs

## Code

The `scripts/` directory contains lightweight reproducibility utilities:

- `scripts/validate_release.py`
  - validates the public release boundary, hidden-test gold removal, JSON/JSONL parseability, required run artifacts, and private-path hygiene
- `scripts/summarize_runs.py`
  - summarizes packaged run metrics into a compact CSV table

## Reproduce

To reproduce the released evaluation setup:

1. Use `benchmark_release/evaluation_config.json` as the frozen evaluation configuration.
2. Use `benchmark_release/hidden_test_package_manifest.json` together with `benchmark_release/hidden_test_tasks.jsonl` for the released hidden-test package.
3. Use `benchmark_freeze/` for frozen benchmark policy files and adjudicated override files.
4. Follow the run-directory contract under `benchmark_release/runs_*` when generating new runs.
5. Run `python scripts/validate_release.py` to verify that the public artifact remains gold-removed and complete.
6. Run `python scripts/summarize_runs.py` to generate a local run-summary CSV from packaged metrics.

For released evaluation results, the most important directories are:

- `benchmark_release/runs_formal_updated/`
- `benchmark_release/runs_supplementary_20260503/`
- `benchmark_release/runs_transfer_heldout_20260504_separate/`
- `benchmark_release/validation_supplementary_20260503/`

This repository is intended as a reproducibility-oriented artifact release rather than as a standalone software package. The underlying disaster imagery and private tile service used during benchmark construction are not redistributed here; public task records use offline map-source identifiers and task-level metadata instead.
