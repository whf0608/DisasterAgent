# DisasterAgentBench

## Overview

This repository contains the paper source, benchmark files, frozen evaluation policy files, and experimental run outputs for **DisasterAgentBench**, an evaluation benchmark for retrieval-grounded disaster assessment with drone-in-the-loop reinspection.

The repository is organized to support:

- inspection of the paper and benchmark specification
- access to the released hidden-test package and evaluation configuration
- audit of formal, supplementary, and held-out experimental runs
- reproduction of the file contract described in the paper's `Required run artifacts`

## Data

The benchmark definition and released data are centered on the following files and directories:

- `Formatting_Instructions_For_NeurIPS_2026/`
  - current NeurIPS paper source and compiled PDF
- `disasteragentbench_preliminary_split.csv`
  - split manifest over train, development, and hidden-test units
- `disasteragentbench_task_schema.json`
  - benchmark task schema
- `benchmark_freeze/`
  - frozen benchmark policy files
  - severity labels, evidence-key registry, report template, and adjudicated override files
- `benchmark_release/hidden_test_tasks.jsonl`
  - distributed hidden-test task instances with gold outputs removed
- `benchmark_release/internal_hidden_test_tasks.formal.jsonl`
  - internal formal hidden-test task file used for strict evaluation
- `benchmark_release/hidden_test_package_manifest.json`
  - hidden-test package manifest
- `benchmark_release/evaluation_config.json`
  - frozen evaluation configuration

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

## Reproduce

To reproduce the released evaluation setup:

1. Read the paper source in `Formatting_Instructions_For_NeurIPS_2026/main.tex`.
2. Use `benchmark_release/evaluation_config.json` as the frozen evaluation configuration.
3. Use `benchmark_release/hidden_test_package_manifest.json` together with `benchmark_release/hidden_test_tasks.jsonl` for the released hidden-test package.
4. Use `benchmark_freeze/` for frozen benchmark policy files and adjudicated override files.
5. Follow the run-directory contract under `benchmark_release/runs_*` when generating new runs.

For paper-aligned evaluation, the most important directories are:

- `benchmark_release/runs_formal_updated/`
- `benchmark_release/runs_supplementary_20260503/`
- `benchmark_release/runs_transfer_heldout_20260504_separate/`
- `benchmark_release/validation_supplementary_20260503/`

This repository is intended as a reproducibility-oriented artifact release rather than as a standalone software package.
