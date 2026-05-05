# DisasterAgentBench Artifacts

This repository contains the paper source, benchmark configuration, frozen policy files, and experimental run data needed to reproduce the reported results for DisasterAgentBench.

## Main contents

- `Formatting_Instructions_For_NeurIPS_2026/`
  - current NeurIPS paper source and compiled PDF
- `disasteragentbench_preliminary_split.csv`
  - split manifest
- `disasteragentbench_task_schema.json`
  - benchmark task schema
- `benchmark_freeze/`
  - frozen benchmark policy files and adjudicated override files
- `benchmark_release/`
  - hidden-test package, evaluation configuration, validation files, and run outputs

## Required run artifacts

Each packaged run directory follows the same file contract:

- `config.json`
- `predictions.jsonl`
- `trace.jsonl`
- `metrics.json`
- `failures.csv`
