## Main Results

| Subset | System | Config | Taskset | Tier | Seed | Tasks | E2E | Retrieval | Grounding | Localization | Drone | Assessment | Report |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | disasteragentbench-eval-v1.0.0 | region_heldout_manifest | formal/formal | 0 | 77 | 0.714 | 1.000 | 1.000 | 1.000 | 1.000 | 0.308 | 0.278 |
| hidden_test | full_disasteragent | disasteragentbench-eval-v1.0.0 | time_heldout_manifest | formal/formal | 0 | 77 | 0.779 | 1.000 | 1.000 | 1.000 | 1.000 | 0.692 | 0.278 |
| hidden_test | full_disasteragent | disasteragentbench-eval-v1.0.0 | hazard_heldout_manifest | formal/formal | 0 | 29 | 0.690 | 1.000 | 1.000 | 1.000 | 1.000 | 0.200 | 0.278 |
| hidden_test | single_agent_all_tools | disasteragentbench-eval-v1.0.0 | region_heldout_manifest | formal/formal | 0 | 77 | 0.714 | 1.000 | 1.000 | 1.000 | 1.000 | 0.308 | 0.278 |
| hidden_test | single_agent_all_tools | disasteragentbench-eval-v1.0.0 | time_heldout_manifest | formal/formal | 0 | 77 | 0.779 | 1.000 | 1.000 | 1.000 | 1.000 | 0.692 | 0.278 |
| hidden_test | single_agent_all_tools | disasteragentbench-eval-v1.0.0 | hazard_heldout_manifest | formal/formal | 0 | 29 | 0.690 | 1.000 | 1.000 | 1.000 | 1.000 | 0.200 | 0.278 |

## Robustness

| Subset | System | Taskset | Tier | Tasks | E2E | Infra Fail | Reason Fail | Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | region_heldout_manifest | formal/formal | 77 | 0.714 | 0 | 0 | 0 |
| hidden_test | full_disasteragent | time_heldout_manifest | formal/formal | 77 | 0.779 | 0 | 0 | 0 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | formal/formal | 29 | 0.690 | 0 | 0 | 0 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | formal/formal | 77 | 0.714 | 0 | 0 | 0 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | formal/formal | 77 | 0.779 | 0 | 0 | 0 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | formal/formal | 29 | 0.690 | 0 | 0 | 0 |

## Drone Review

| Subset | System | Taskset | Tier | Mission | ROI | Intervention | Review | E2E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | region_heldout_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 0.000 | 0.714 |
| hidden_test | full_disasteragent | time_heldout_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 0.000 | 0.779 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 0.000 | 0.690 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 0.000 | 0.714 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 0.000 | 0.779 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | formal/formal | 1.000 | 1.000 | 1.000 | 0.000 | 0.690 |

## Ablation

| System | Subset | Taskset | Tier | E2E | Retrieval | Grounding | Localization | Assessment | Report |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| full_disasteragent | hidden_test | region_heldout_manifest | formal/formal | 0.714 | 1.000 | 1.000 | 1.000 | 0.308 | 0.278 |
| full_disasteragent | hidden_test | time_heldout_manifest | formal/formal | 0.779 | 1.000 | 1.000 | 1.000 | 0.692 | 0.278 |
| full_disasteragent | hidden_test | hazard_heldout_manifest | formal/formal | 0.690 | 1.000 | 1.000 | 1.000 | 0.200 | 0.278 |
| single_agent_all_tools | hidden_test | region_heldout_manifest | formal/formal | 0.714 | 1.000 | 1.000 | 1.000 | 0.308 | 0.278 |
| single_agent_all_tools | hidden_test | time_heldout_manifest | formal/formal | 0.779 | 1.000 | 1.000 | 1.000 | 0.692 | 0.278 |
| single_agent_all_tools | hidden_test | hazard_heldout_manifest | formal/formal | 0.690 | 1.000 | 1.000 | 1.000 | 0.200 | 0.278 |

## Benchmark Validity

| Subset | System | Taskset | Tier | Tasks | Families | Formal | E2E |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | region_heldout_manifest | formal/formal | 77 | 6 | yes | 0.714 |
| hidden_test | full_disasteragent | time_heldout_manifest | formal/formal | 77 | 6 | yes | 0.779 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | formal/formal | 29 | 6 | yes | 0.690 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | formal/formal | 77 | 6 | yes | 0.714 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | formal/formal | 77 | 6 | yes | 0.779 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | formal/formal | 29 | 6 | yes | 0.690 |
