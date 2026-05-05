## Main Results

| Subset | System | Config | Taskset | Tier | Seed | Tasks | E2E | Retrieval | Grounding | Localization | Drone | Assessment | Report |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | disasteragentbench-eval-v1.0.0 | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 0 | 262 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| hidden_test | oracle_retrieval_single_agent | disasteragentbench-eval-v1.0.0 | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 0 | 262 | 0.588 | 1.000 | 1.000 | 1.000 | 0.000 | 0.500 | 0.278 |
| hidden_test | single_agent_react | disasteragentbench-eval-v1.0.0 | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 0 | 262 | 0.588 | 1.000 | 1.000 | 1.000 | 0.000 | 0.500 | 0.278 |

## Robustness

| Subset | System | Taskset | Tier | Tasks | E2E | Infra Fail | Reason Fail | Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 262 | 1.000 | 0 | 0 | 0 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 262 | 0.588 | 126 | 0 | 0 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 262 | 0.588 | 126 | 0 | 0 |

## Drone Review

| Subset | System | Taskset | Tier | Mission | ROI | Intervention | Review | E2E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 0.000 | 1.000 | 1.000 | 0.000 | 0.588 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 0.000 | 1.000 | 1.000 | 0.000 | 0.588 |

## Ablation

| System | Subset | Taskset | Tier | E2E | Retrieval | Grounding | Localization | Assessment | Report |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| oracle_all_gold | hidden_test | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| oracle_retrieval_single_agent | hidden_test | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 0.588 | 1.000 | 1.000 | 1.000 | 0.500 | 0.278 |
| single_agent_react | hidden_test | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 0.588 | 1.000 | 1.000 | 1.000 | 0.500 | 0.278 |

## Benchmark Validity

| Subset | System | Taskset | Tier | Tasks | Families | Formal | E2E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 262 | 6 | yes | 1.000 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 262 | 6 | yes | 0.588 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | formal/formal | 262 | 6 | yes | 0.588 |
