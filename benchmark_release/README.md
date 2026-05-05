# Benchmark Release

This directory now contains both:

- active release files
- remaining templates or draft assets

## Active release file

- `evaluation_config.json`
  - current non-template benchmark evaluation config
  - frozen at the release-config level
  - intended to be used by the `evaluation/` layer

## Remaining template or draft assets

- `evaluation_config.template.json`
  - retained as a scaffolding reference
- `task_record.template.json`
  - schema-conformant task-record template
- `hidden_test_package_manifest.template.json`
  - hidden-test package scaffold; still not a finalized package
- `assessment_report_candidate_units.csv`
  - candidate pool only, not final formal hidden-test task gold

## Current status

What is finalized here:

- the main evaluation config file
- lock fields for prompts, routing, and thresholds
- baseline metric thresholds and required run artifacts

What is not fully finalized yet:

- hidden-test package final freeze state
- task-level adjudicated assessment/report gold
- final hidden-test task package distribution

## Practical usage

Use:

- `evaluation_config.json`
- `hidden_test_package_manifest.json`

Do not use for real runs unless you explicitly want scaffolding:

- `evaluation_config.template.json`
- `hidden_test_package_manifest.template.json`

## Recommended next steps

1. finalize the hidden-test package manifest as a non-template file
2. promote the hidden-test package from `preformal` to `frozen`
3. populate adjudicated assessment/report override files under `benchmark_freeze/`
4. regenerate hidden-test task records in `formal-mode`
5. run `formal_readiness`
6. run `run_eval --strict-formal`
