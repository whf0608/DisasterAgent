## Run Overview

| Subset | System | Config | Taskset | Seed | Tier | Formal | Latency | Tool Calls | Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | disasteragentbench-eval-v1.0.0 | region_heldout_manifest | 0 | formal | yes | 0.116 | 5.000 | 0.000 |
| hidden_test | full_disasteragent | disasteragentbench-eval-v1.0.0 | time_heldout_manifest | 0 | formal | yes | 0.115 | 5.000 | 0.000 |
| hidden_test | full_disasteragent | disasteragentbench-eval-v1.0.0 | hazard_heldout_manifest | 0 | formal | yes | 0.117 | 5.000 | 0.000 |
| hidden_test | single_agent_all_tools | disasteragentbench-eval-v1.0.0 | region_heldout_manifest | 0 | formal | yes | 0.116 | 5.000 | 0.000 |
| hidden_test | single_agent_all_tools | disasteragentbench-eval-v1.0.0 | time_heldout_manifest | 0 | formal | yes | 0.115 | 5.000 | 0.000 |
| hidden_test | single_agent_all_tools | disasteragentbench-eval-v1.0.0 | hazard_heldout_manifest | 0 | formal | yes | 0.114 | 5.000 | 0.000 |

## Failure Distribution

| Subset | System | Taskset | Success | Reason | Infra | Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | region_heldout_manifest | 231 | 0 | 0 | 0 |
| hidden_test | full_disasteragent | time_heldout_manifest | 231 | 0 | 0 | 0 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | 87 | 0 | 0 | 0 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | 231 | 0 | 0 | 0 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | 231 | 0 | 0 | 0 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | 87 | 0 | 0 | 0 |

## Family Primary Metrics

| Subset | System | Taskset | Family | Primary Metric | Mean | Pass Rate | Tasks |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | region_heldout_manifest | assessment_synthesis | severity_f1 | 0.308 | 0.308 | 13 |
| hidden_test | full_disasteragent | region_heldout_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 13 |
| hidden_test | full_disasteragent | region_heldout_manifest | drone_reinspection | mission_validity | 1.000 | 1.000 | 12 |
| hidden_test | full_disasteragent | region_heldout_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 13 |
| hidden_test | full_disasteragent | region_heldout_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 13 |
| hidden_test | full_disasteragent | region_heldout_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 13 |
| hidden_test | full_disasteragent | time_heldout_manifest | assessment_synthesis | severity_f1 | 0.692 | 0.692 | 13 |
| hidden_test | full_disasteragent | time_heldout_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 13 |
| hidden_test | full_disasteragent | time_heldout_manifest | drone_reinspection | mission_validity | 1.000 | 1.000 | 12 |
| hidden_test | full_disasteragent | time_heldout_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 13 |
| hidden_test | full_disasteragent | time_heldout_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 13 |
| hidden_test | full_disasteragent | time_heldout_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 13 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | assessment_synthesis | severity_f1 | 0.200 | 0.200 | 5 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 5 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | drone_reinspection | mission_validity | 1.000 | 1.000 | 4 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 5 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 5 |
| hidden_test | full_disasteragent | hazard_heldout_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 5 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | assessment_synthesis | severity_f1 | 0.308 | 0.308 | 13 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 13 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | drone_reinspection | mission_validity | 1.000 | 1.000 | 12 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 13 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 13 |
| hidden_test | single_agent_all_tools | region_heldout_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 13 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | assessment_synthesis | severity_f1 | 0.692 | 0.692 | 13 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 13 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | drone_reinspection | mission_validity | 1.000 | 1.000 | 12 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 13 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 13 |
| hidden_test | single_agent_all_tools | time_heldout_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 13 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | assessment_synthesis | severity_f1 | 0.200 | 0.200 | 5 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 5 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | drone_reinspection | mission_validity | 1.000 | 1.000 | 4 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 5 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 5 |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 5 |

## Metric Coverage

| Subset | System | Taskset | Metric Coverage | Task Families | Formal Blockers |
| --- | ---: | ---: | ---: | ---: | ---: |
| hidden_test | full_disasteragent | region_heldout_manifest | center_distance_m=39, end_to_end_success=231, event_accuracy=39, evidence_coverage=39, geojson_f1=39, geojson_iou=39, geojson_precision=39, geojson_recall=39, grounding_success=39, intervention_rate=36, intervention_success=36, latency_s=231, layer_selection_accuracy=39, mission_validity=36, report_grounding_score=39, review_rate=231, roi_coverage=75, severity_accuracy=39, tool_calls=231, topk_recall=39 | assessment_synthesis=39, damage_localization=39, drone_reinspection=36, event_retrieval=39, map_grounding=39, report_generation=39 | - |
| hidden_test | full_disasteragent | time_heldout_manifest | center_distance_m=39, end_to_end_success=231, event_accuracy=39, evidence_coverage=39, geojson_f1=39, geojson_iou=39, geojson_precision=39, geojson_recall=39, grounding_success=39, intervention_rate=36, intervention_success=36, latency_s=231, layer_selection_accuracy=39, mission_validity=36, report_grounding_score=39, review_rate=231, roi_coverage=75, severity_accuracy=39, tool_calls=231, topk_recall=39 | assessment_synthesis=39, damage_localization=39, drone_reinspection=36, event_retrieval=39, map_grounding=39, report_generation=39 | - |
| hidden_test | full_disasteragent | hazard_heldout_manifest | center_distance_m=15, end_to_end_success=87, event_accuracy=15, evidence_coverage=15, geojson_f1=15, geojson_iou=15, geojson_precision=15, geojson_recall=15, grounding_success=15, intervention_rate=12, intervention_success=12, latency_s=87, layer_selection_accuracy=15, mission_validity=12, report_grounding_score=15, review_rate=87, roi_coverage=27, severity_accuracy=15, tool_calls=87, topk_recall=15 | assessment_synthesis=15, damage_localization=15, drone_reinspection=12, event_retrieval=15, map_grounding=15, report_generation=15 | - |
| hidden_test | single_agent_all_tools | region_heldout_manifest | center_distance_m=39, end_to_end_success=231, event_accuracy=39, evidence_coverage=39, geojson_f1=39, geojson_iou=39, geojson_precision=39, geojson_recall=39, grounding_success=39, intervention_rate=36, intervention_success=36, latency_s=231, layer_selection_accuracy=39, mission_validity=36, report_grounding_score=39, review_rate=231, roi_coverage=75, severity_accuracy=39, tool_calls=231, topk_recall=39 | assessment_synthesis=39, damage_localization=39, drone_reinspection=36, event_retrieval=39, map_grounding=39, report_generation=39 | - |
| hidden_test | single_agent_all_tools | time_heldout_manifest | center_distance_m=39, end_to_end_success=231, event_accuracy=39, evidence_coverage=39, geojson_f1=39, geojson_iou=39, geojson_precision=39, geojson_recall=39, grounding_success=39, intervention_rate=36, intervention_success=36, latency_s=231, layer_selection_accuracy=39, mission_validity=36, report_grounding_score=39, review_rate=231, roi_coverage=75, severity_accuracy=39, tool_calls=231, topk_recall=39 | assessment_synthesis=39, damage_localization=39, drone_reinspection=36, event_retrieval=39, map_grounding=39, report_generation=39 | - |
| hidden_test | single_agent_all_tools | hazard_heldout_manifest | center_distance_m=15, end_to_end_success=87, event_accuracy=15, evidence_coverage=15, geojson_f1=15, geojson_iou=15, geojson_precision=15, geojson_recall=15, grounding_success=15, intervention_rate=12, intervention_success=12, latency_s=87, layer_selection_accuracy=15, mission_validity=12, report_grounding_score=15, review_rate=87, roi_coverage=27, severity_accuracy=15, tool_calls=87, topk_recall=15 | assessment_synthesis=15, damage_localization=15, drone_reinspection=12, event_retrieval=15, map_grounding=15, report_generation=15 | - |

## Pairwise Tests

| Subset | Taskset | A | B | Metric | Delta | p-value | Seeds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | ece | 0.124 | 0.2318 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | end_to_end_success | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | evidence_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | family::assessment_synthesis::severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | family::drone_reinspection::mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | family::report_generation::report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | latency_s | 0.000 | 0.7433 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1_macro | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1_weighted | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | successful_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | tool_calls | 0.000 | 1.0000 | 3 |
| hidden_test | region_heldout_manifest | full_disasteragent | single_agent_all_tools | topk_recall | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | ece | 0.058 | 0.7423 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | end_to_end_success | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | evidence_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | family::assessment_synthesis::severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | family::drone_reinspection::mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | family::report_generation::report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | latency_s | -0.001 | 0.4885 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1_macro | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1_weighted | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | successful_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | tool_calls | 0.000 | 1.0000 | 3 |
| hidden_test | time_heldout_manifest | full_disasteragent | single_agent_all_tools | topk_recall | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | ece | 0.043 | 0.2318 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | end_to_end_success | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | evidence_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | family::assessment_synthesis::severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | family::drone_reinspection::mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | family::report_generation::report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | latency_s | 0.002 | 0.2318 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1_macro | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | severity_f1_weighted | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | successful_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | tool_calls | 0.000 | 1.0000 | 3 |
| hidden_test | hazard_heldout_manifest | full_disasteragent | single_agent_all_tools | topk_recall | 0.000 | 1.0000 | 3 |
