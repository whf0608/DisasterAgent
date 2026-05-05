## Run Overview

| Subset | System | Config | Taskset | Seed | Tier | Formal | Latency | Tool Calls | Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | disasteragentbench-eval-v1.0.0 | updated_tasks_with_bbox.hidden_test_manifest | 0 | formal | yes | 0.000 | 0.000 | 0.000 |
| hidden_test | oracle_retrieval_single_agent | disasteragentbench-eval-v1.0.0 | updated_tasks_with_bbox.hidden_test_manifest | 0 | formal | yes | 0.105 | 4.511 | 0.000 |
| hidden_test | single_agent_react | disasteragentbench-eval-v1.0.0 | updated_tasks_with_bbox.hidden_test_manifest | 0 | formal | yes | 0.106 | 5.511 | 0.000 |
| hidden_test | wo_drone_and_review | disasteragentbench-eval-v1.0.0 | updated_tasks_with_bbox.hidden_test_manifest | 0 | formal | yes | 0.115 | 5.000 | 0.000 |

## Failure Distribution

| Subset | System | Taskset | Success | Reason | Infra | Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | 786 | 0 | 0 | 0 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | 660 | 0 | 126 | 0 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | 660 | 0 | 126 | 0 |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | 660 | 0 | 126 | 0 |

## Family Primary Metrics

| Subset | System | Taskset | Family | Primary Metric | Mean | Pass Rate | Tasks |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | assessment_synthesis | severity_f1 | 1.000 | 1.000 | 44 |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 44 |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | drone_reinspection | mission_validity | 1.000 | 1.000 | 42 |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 44 |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 44 |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | report_generation | report_grounding_score | 1.000 | 1.000 | 44 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | assessment_synthesis | severity_f1 | 0.500 | 0.500 | 44 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 44 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | drone_reinspection | mission_validity | 0.000 | 0.000 | 42 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 44 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 44 |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 44 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | assessment_synthesis | severity_f1 | 0.500 | 0.500 | 44 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 44 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | drone_reinspection | mission_validity | 0.000 | 0.000 | 42 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 44 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 44 |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 44 |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | assessment_synthesis | severity_f1 | 0.500 | 0.500 | 44 |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | damage_localization | geojson_f1 | 1.000 | 1.000 | 44 |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | drone_reinspection | mission_validity | 0.000 | 0.000 | 42 |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | event_retrieval | event_accuracy | 1.000 | 1.000 | 44 |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | map_grounding | grounding_success | 1.000 | 1.000 | 44 |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | report_generation | report_grounding_score | 0.278 | 0.000 | 44 |

## Metric Coverage

| Subset | System | Taskset | Metric Coverage | Task Families | Formal Blockers |
| --- | ---: | ---: | ---: | ---: | ---: |
| hidden_test | oracle_all_gold | updated_tasks_with_bbox.hidden_test_manifest | center_distance_m=132, end_to_end_success=786, event_accuracy=132, evidence_coverage=132, geojson_f1=132, geojson_iou=132, geojson_precision=132, geojson_recall=132, grounding_success=132, intervention_rate=126, intervention_success=126, latency_s=786, layer_selection_accuracy=132, mission_validity=126, report_grounding_score=132, review_rate=786, roi_coverage=258, severity_accuracy=132, tool_calls=786, topk_recall=132 | assessment_synthesis=132, damage_localization=132, drone_reinspection=126, event_retrieval=132, map_grounding=132, report_generation=132 | - |
| hidden_test | oracle_retrieval_single_agent | updated_tasks_with_bbox.hidden_test_manifest | center_distance_m=132, end_to_end_success=786, event_accuracy=132, evidence_coverage=132, geojson_f1=132, geojson_iou=132, geojson_precision=132, geojson_recall=132, grounding_success=132, intervention_rate=126, intervention_success=126, latency_s=786, layer_selection_accuracy=132, mission_validity=126, report_grounding_score=132, review_rate=786, roi_coverage=258, severity_accuracy=132, tool_calls=786, topk_recall=132 | assessment_synthesis=132, damage_localization=132, drone_reinspection=126, event_retrieval=132, map_grounding=132, report_generation=132 | - |
| hidden_test | single_agent_react | updated_tasks_with_bbox.hidden_test_manifest | center_distance_m=132, end_to_end_success=786, event_accuracy=132, evidence_coverage=132, geojson_f1=132, geojson_iou=132, geojson_precision=132, geojson_recall=132, grounding_success=132, intervention_rate=126, intervention_success=126, latency_s=786, layer_selection_accuracy=132, mission_validity=126, report_grounding_score=132, review_rate=786, roi_coverage=258, severity_accuracy=132, tool_calls=786, topk_recall=132 | assessment_synthesis=132, damage_localization=132, drone_reinspection=126, event_retrieval=132, map_grounding=132, report_generation=132 | - |
| hidden_test | wo_drone_and_review | updated_tasks_with_bbox.hidden_test_manifest | center_distance_m=132, end_to_end_success=786, event_accuracy=132, evidence_coverage=132, geojson_f1=132, geojson_iou=132, geojson_precision=132, geojson_recall=132, grounding_success=132, intervention_rate=126, intervention_success=126, latency_s=786, layer_selection_accuracy=132, mission_validity=126, report_grounding_score=132, review_rate=786, roi_coverage=258, severity_accuracy=132, tool_calls=786, topk_recall=132 | assessment_synthesis=132, damage_localization=132, drone_reinspection=126, event_retrieval=132, map_grounding=132, report_generation=132 | - |

## Pairwise Tests

| Subset | Taskset | A | B | Metric | Delta | p-value | Seeds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | ece | -0.186 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | end_to_end_success | 0.412 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | evidence_coverage | 0.444 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | family::assessment_synthesis::severity_f1 | 0.500 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | family::drone_reinspection::mission_validity | 1.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | family::report_generation::report_grounding_score | 0.722 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | latency_s | -0.105 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | mission_validity | 1.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | report_grounding_score | 0.722 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | severity_accuracy | 0.500 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | severity_f1 | 0.811 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | severity_f1_macro | 0.811 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | severity_f1_weighted | 0.616 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | successful_tasks | 108.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | tool_calls | -4.511 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | oracle_retrieval_single_agent | topk_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | ece | -0.161 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | end_to_end_success | 0.412 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | evidence_coverage | 0.444 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | family::assessment_synthesis::severity_f1 | 0.500 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | family::drone_reinspection::mission_validity | 1.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | family::report_generation::report_grounding_score | 0.722 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | latency_s | -0.106 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | mission_validity | 1.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | report_grounding_score | 0.722 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | severity_accuracy | 0.500 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | severity_f1 | 0.811 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | severity_f1_macro | 0.811 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | severity_f1_weighted | 0.616 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | successful_tasks | 108.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | tool_calls | -5.511 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | single_agent_react | topk_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | ece | -0.087 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | end_to_end_success | 0.412 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | evidence_coverage | 0.444 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | family::assessment_synthesis::severity_f1 | 0.500 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | family::drone_reinspection::mission_validity | 1.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | family::report_generation::report_grounding_score | 0.722 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | latency_s | -0.115 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | mission_validity | 1.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | report_grounding_score | 0.722 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | severity_accuracy | 0.500 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | severity_f1 | 0.811 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | severity_f1_macro | 0.811 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | severity_f1_weighted | 0.616 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | successful_tasks | 108.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | tool_calls | -5.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_all_gold | wo_drone_and_review | topk_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | ece | 0.025 | 0.7433 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | end_to_end_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | evidence_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | family::assessment_synthesis::severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | family::drone_reinspection::mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | family::report_generation::report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | latency_s | -0.001 | 0.4885 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | severity_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | severity_f1_macro | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | severity_f1_weighted | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | successful_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | tool_calls | -1.000 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | single_agent_react | topk_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | ece | 0.100 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | end_to_end_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | evidence_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | family::assessment_synthesis::severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | family::drone_reinspection::mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | family::report_generation::report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | latency_s | -0.010 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | severity_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | severity_f1_macro | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | severity_f1_weighted | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | successful_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | tool_calls | -0.489 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | oracle_retrieval_single_agent | wo_drone_and_review | topk_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | center_distance_m | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | ece | 0.075 | 0.4855 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | end_to_end_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | evidence_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | family::assessment_synthesis::severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | family::damage_localization::geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | family::drone_reinspection::mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | family::event_retrieval::event_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | family::map_grounding::grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | family::report_generation::report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | geojson_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | geojson_iou | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | geojson_precision | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | geojson_recall | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | grounding_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | intervention_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | intervention_success | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | latency_s | -0.009 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | layer_selection_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | mission_validity | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | report_grounding_score | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | review_rate | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | reviewed_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | roi_coverage | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | severity_accuracy | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | severity_f1 | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | severity_f1_macro | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | severity_f1_weighted | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | successful_tasks | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | task_count | 0.000 | 1.0000 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | tool_calls | 0.511 | 0.2318 | 3 |
| hidden_test | updated_tasks_with_bbox.hidden_test_manifest | single_agent_react | wo_drone_and_review | topk_recall | 0.000 | 1.0000 | 3 |
