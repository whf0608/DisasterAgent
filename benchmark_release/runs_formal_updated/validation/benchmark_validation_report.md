# Benchmark Validation Results

Annotation source: `provided`.

## Inter-Annotator Agreement

| Family | Source | N | Compared | Agreement | Kappa | BBox IoU | Evidence F1 | Slot F1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| event_retrieval | provided | 44 | 0 | 0.000 |  |  |  |  |
| map_grounding | provided | 44 | 0 | 0.000 |  |  |  |  |
| damage_localization | provided | 44 | 0 | 0.000 |  |  |  |  |
| drone_reinspection | provided | 42 | 0 | 0.000 |  |  |  |  |
| assessment_synthesis | provided | 44 | 0 | 0.000 |  |  |  |  |
| report_generation | provided | 44 | 0 | 0.000 |  |  |  |  |

## Human / Reference Validation

| Family | Source | N | Event | BBox IoU | Severity | Evidence F1 | Slot F1 | Drone |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| event_retrieval | provided | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| map_grounding | provided | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| damage_localization | provided | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| drone_reinspection | provided | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| assessment_synthesis | provided | 44 | 1.000 | 0.977 | 0.432 | 1.000 | 1.000 | 1.000 |
| report_generation | provided | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Oracle Validity

| System | Seeds | Tier | Formal | E2E | Retrieval | Grounding | Localization | Drone | Assessment | Report |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| oracle_all_gold | 3 | formal | yes | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| oracle_retrieval_single_agent | 3 | formal | yes | 0.588 | 1.000 | 1.000 | 1.000 | 0.000 | 0.500 | 0.278 |
| single_agent_react | 3 | formal | yes | 0.588 | 1.000 | 1.000 | 1.000 | 0.000 | 0.500 | 0.278 |
