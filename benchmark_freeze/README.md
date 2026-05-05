# Benchmark Freeze Package

This directory is the versioned freeze package for global benchmark policies and
report/assessment scaffolding.

The package is now frozen at the file-contract level:

- severity label semantics
- impact-fact record schema
- evidence-key vocabulary
- report slot template and scoring contract

What is frozen here:

- `freeze_package_manifest.json`: top-level freeze manifest and package policy
- `severity_label_glossary.json`: label ordinals, definitions, and adjudication policy
- `impact_fact_template.json`: canonical schema for atomic impact facts
- `evidence_key_registry.json`: controlled evidence vocabulary
- `report_template.json`: required report slots and scorer-side grounding contract

Task-level adjudicated gold still lives in:

- `assessment_gold_overrides.jsonl`
- `report_gold_overrides.jsonl`

These override files are part of the freeze-directory contract, but they may
remain empty until benchmark owners finish task-level adjudication.

Template helpers for writing those files:

- `assessment_gold_overrides.template.jsonl`
- `report_gold_overrides.template.jsonl`
- `OVERRIDE_TEMPLATES.md`

Practical interpretation:

- the core freeze package itself is frozen
- formal hidden-test `assessment_synthesis` and `report_generation` results
  still require adjudicated override rows

Recommended workflow:

1. Freeze the split manifest and benchmark release config.
2. Maintain the core files in this directory as backward-compatible frozen assets.
3. Populate `assessment_gold_overrides.jsonl` and `report_gold_overrides.jsonl`
   with adjudicated task-level gold rows.
4. Run `formal_readiness` and `--strict-formal` before claiming formal results.
