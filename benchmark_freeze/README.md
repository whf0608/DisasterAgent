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

Task-level policy overrides live in:

- `assessment_gold_overrides.jsonl`
- `report_gold_overrides.jsonl`

These override files are part of the freeze-directory contract. Public release
files expose the policy boundary and gold-removed hidden-test tasks; maintainer-
side hidden-test gold used for strict scoring is withheld from the public
repository.

Template helpers for writing those files:

- `assessment_gold_overrides.template.jsonl`
- `report_gold_overrides.template.jsonl`
- `OVERRIDE_TEMPLATES.md`

Practical interpretation:

- the core freeze package itself is frozen
- public files define the released scorer policy and task schema
- hidden-test gold labels are not distributed

Recommended workflow:

1. Freeze the split manifest and benchmark release config.
2. Maintain the core files in this directory as backward-compatible frozen assets.
3. Use the public gold-removed hidden-test task file for released inputs.
4. Use maintainer-side gold outside the public repository for strict scoring.
