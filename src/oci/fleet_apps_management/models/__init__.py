# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from __future__ import absolute_import

from .action_group import ActionGroup
from .action_group_based_user_action_details import ActionGroupBasedUserActionDetails
from .action_group_details import ActionGroupDetails
from .activity_resource_target import ActivityResourceTarget
from .announcement_collection import AnnouncementCollection
from .announcement_summary import AnnouncementSummary
from .api_based_execution_details import ApiBasedExecutionDetails
from .artifact_details import ArtifactDetails
from .associated_fleet_credential_details import AssociatedFleetCredentialDetails
from .associated_fleet_property_details import AssociatedFleetPropertyDetails
from .associated_fleet_resource_details import AssociatedFleetResourceDetails
from .associated_local_task_details import AssociatedLocalTaskDetails
from .associated_scheduler_definition import AssociatedSchedulerDefinition
from .associated_shared_task_details import AssociatedSharedTaskDetails
from .associated_task_details import AssociatedTaskDetails
from .associations import Associations
from .check_resource_tagging_details import CheckResourceTaggingDetails
from .compliance_detail_policy import ComplianceDetailPolicy
from .compliance_detail_product import ComplianceDetailProduct
from .compliance_detail_resource import ComplianceDetailResource
from .compliance_detail_target import ComplianceDetailTarget
from .compliance_patch_detail import CompliancePatchDetail
from .compliance_policy import CompliancePolicy
from .compliance_policy_collection import CompliancePolicyCollection
from .compliance_policy_rule import CompliancePolicyRule
from .compliance_policy_rule_collection import CompliancePolicyRuleCollection
from .compliance_policy_rule_summary import CompliancePolicyRuleSummary
from .compliance_policy_summary import CompliancePolicySummary
from .compliance_record import ComplianceRecord
from .compliance_record_aggregation import ComplianceRecordAggregation
from .compliance_record_aggregation_collection import ComplianceRecordAggregationCollection
from .compliance_record_collection import ComplianceRecordCollection
from .compliance_record_dimension import ComplianceRecordDimension
from .compliance_record_summary import ComplianceRecordSummary
from .compliance_report import ComplianceReport
from .compliance_report_patch_detail import ComplianceReportPatchDetail
from .compliance_report_product import ComplianceReportProduct
from .compliance_report_resource import ComplianceReportResource
from .compliance_report_target import ComplianceReportTarget
from .component_properties import ComponentProperties
from .condition import Condition
from .config_association_details import ConfigAssociationDetails
from .config_category_details import ConfigCategoryDetails
from .confirm_targets_details import ConfirmTargetsDetails
from .content_details import ContentDetails
from .create_compliance_policy_rule_details import CreateCompliancePolicyRuleDetails
from .create_fleet_credential_details import CreateFleetCredentialDetails
from .create_fleet_details import CreateFleetDetails
from .create_fleet_property_details import CreateFleetPropertyDetails
from .create_fleet_resource_details import CreateFleetResourceDetails
from .create_maintenance_window_details import CreateMaintenanceWindowDetails
from .create_onboarding_details import CreateOnboardingDetails
from .create_patch_details import CreatePatchDetails
from .create_platform_configuration_details import CreatePlatformConfigurationDetails
from .create_property_details import CreatePropertyDetails
from .create_runbook_details import CreateRunbookDetails
from .create_scheduler_definition_details import CreateSchedulerDefinitionDetails
from .create_task_record_details import CreateTaskRecordDetails
from .credential_config_category_details import CredentialConfigCategoryDetails
from .credential_details import CredentialDetails
from .credential_entity_specific_details import CredentialEntitySpecificDetails
from .dependent_patch_details import DependentPatchDetails
from .details import Details
from .discovered_target import DiscoveredTarget
from .enable_latest_policy_details import EnableLatestPolicyDetails
from .entity_execution_details import EntityExecutionDetails
from .environment_config_category_details import EnvironmentConfigCategoryDetails
from .execution import Execution
from .execution_collection import ExecutionCollection
from .execution_details import ExecutionDetails
from .execution_summary import ExecutionSummary
from .execution_workflow_details import ExecutionWorkflowDetails
from .export_compliance_report_details import ExportComplianceReportDetails
from .fleet import Fleet
from .fleet_collection import FleetCollection
from .fleet_credential import FleetCredential
from .fleet_credential_collection import FleetCredentialCollection
from .fleet_credential_entity_specific_details import FleetCredentialEntitySpecificDetails
from .fleet_credential_summary import FleetCredentialSummary
from .fleet_product_collection import FleetProductCollection
from .fleet_product_summary import FleetProductSummary
from .fleet_property import FleetProperty
from .fleet_property_collection import FleetPropertyCollection
from .fleet_property_summary import FleetPropertySummary
from .fleet_resource import FleetResource
from .fleet_resource_collection import FleetResourceCollection
from .fleet_resource_summary import FleetResourceSummary
from .fleet_summary import FleetSummary
from .fleet_target import FleetTarget
from .fleet_target_collection import FleetTargetCollection
from .fleet_target_summary import FleetTargetSummary
from .generate_compliance_report_details import GenerateComplianceReportDetails
from .generic_artifact import GenericArtifact
from .generic_artifact_details import GenericArtifactDetails
from .group import Group
from .input_argument import InputArgument
from .input_parameter import InputParameter
from .inventory_resource_collection import InventoryResourceCollection
from .inventory_resource_summary import InventoryResourceSummary
from .job_activity import JobActivity
from .key_encryption_credential_details import KeyEncryptionCredentialDetails
from .maintenance_window import MaintenanceWindow
from .maintenance_window_collection import MaintenanceWindowCollection
from .maintenance_window_summary import MaintenanceWindowSummary
from .manage_job_execution_details import ManageJobExecutionDetails
from .manage_settings_details import ManageSettingsDetails
from .managed_entity_aggregation import ManagedEntityAggregation
from .managed_entity_aggregation_collection import ManagedEntityAggregationCollection
from .managed_entity_dimension import ManagedEntityDimension
from .model_property import ModelProperty
from .notification_preferences import NotificationPreferences
from .object_storage_bucket_content_details import ObjectStorageBucketContentDetails
from .onboarding import Onboarding
from .onboarding_collection import OnboardingCollection
from .onboarding_policy_collection import OnboardingPolicyCollection
from .onboarding_policy_summary import OnboardingPolicySummary
from .onboarding_summary import OnboardingSummary
from .operation_runbook import OperationRunbook
from .outcome import Outcome
from .output_variable_details import OutputVariableDetails
from .output_variable_input_argument import OutputVariableInputArgument
from .output_variable_mapping import OutputVariableMapping
from .patch import Patch
from .patch_collection import PatchCollection
from .patch_level_selection_details import PatchLevelSelectionDetails
from .patch_name_selection_details import PatchNameSelectionDetails
from .patch_product import PatchProduct
from .patch_release_date_selection_details import PatchReleaseDateSelectionDetails
from .patch_selection_details import PatchSelectionDetails
from .patch_summary import PatchSummary
from .patch_type import PatchType
from .patch_type_config_category_details import PatchTypeConfigCategoryDetails
from .pause_details import PauseDetails
from .plain_text_credential_details import PlainTextCredentialDetails
from .platform_configuration import PlatformConfiguration
from .platform_configuration_collection import PlatformConfigurationCollection
from .platform_configuration_summary import PlatformConfigurationSummary
from .platform_specific_artifact import PlatformSpecificArtifact
from .platform_specific_artifact_details import PlatformSpecificArtifactDetails
from .preferences import Preferences
from .product_config_category_details import ProductConfigCategoryDetails
from .product_stack_as_product_sub_category_details import ProductStackAsProductSubCategoryDetails
from .product_stack_config_category_details import ProductStackConfigCategoryDetails
from .product_stack_generic_sub_category_details import ProductStackGenericSubCategoryDetails
from .product_stack_sub_category_details import ProductStackSubCategoryDetails
from .product_version_details import ProductVersionDetails
from .properties import Properties
from .property_collection import PropertyCollection
from .property_summary import PropertySummary
from .publish_runbook_details import PublishRunbookDetails
from .request_resource_validation_details import RequestResourceValidationDetails
from .request_target_discovery_details import RequestTargetDiscoveryDetails
from .resource_collection import ResourceCollection
from .resource_credential_entity_specific_details import ResourceCredentialEntitySpecificDetails
from .resource_summary import ResourceSummary
from .resource_tag_check_details import ResourceTagCheckDetails
from .resource_tag_enablement_info import ResourceTagEnablementInfo
from .rollback_workflow_details import RollbackWorkflowDetails
from .rule import Rule
from .runbook import Runbook
from .runbook_collection import RunbookCollection
from .runbook_summary import RunbookSummary
from .schedule import Schedule
from .scheduled_fleet_collection import ScheduledFleetCollection
from .scheduled_fleet_summary import ScheduledFleetSummary
from .scheduler_definition import SchedulerDefinition
from .scheduler_definition_collection import SchedulerDefinitionCollection
from .scheduler_definition_summary import SchedulerDefinitionSummary
from .scheduler_job import SchedulerJob
from .scheduler_job_aggregation import SchedulerJobAggregation
from .scheduler_job_aggregation_collection import SchedulerJobAggregationCollection
from .scheduler_job_collection import SchedulerJobCollection
from .scheduler_job_dimension import SchedulerJobDimension
from .scheduler_job_summary import SchedulerJobSummary
from .script_based_execution_details import ScriptBasedExecutionDetails
from .selection_criteria import SelectionCriteria
from .set_default_runbook_details import SetDefaultRunbookDetails
from .step_based_user_action_details import StepBasedUserActionDetails
from .step_collection import StepCollection
from .step_summary import StepSummary
from .string_input_argument import StringInputArgument
from .target_credential_entity_specific_details import TargetCredentialEntitySpecificDetails
from .target_resource import TargetResource
from .task import Task
from .task_argument import TaskArgument
from .task_notification_preferences import TaskNotificationPreferences
from .task_record import TaskRecord
from .task_record_collection import TaskRecordCollection
from .task_record_summary import TaskRecordSummary
from .task_variable import TaskVariable
from .time_based_pause_details import TimeBasedPauseDetails
from .update_compliance_policy_rule_details import UpdateCompliancePolicyRuleDetails
from .update_fleet_credential_details import UpdateFleetCredentialDetails
from .update_fleet_details import UpdateFleetDetails
from .update_fleet_property_details import UpdateFleetPropertyDetails
from .update_fleet_resource_details import UpdateFleetResourceDetails
from .update_maintenance_window_details import UpdateMaintenanceWindowDetails
from .update_onboarding_details import UpdateOnboardingDetails
from .update_patch_details import UpdatePatchDetails
from .update_platform_configuration_details import UpdatePlatformConfigurationDetails
from .update_property_details import UpdatePropertyDetails
from .update_runbook_details import UpdateRunbookDetails
from .update_scheduler_definition_details import UpdateSchedulerDefinitionDetails
from .update_scheduler_job_details import UpdateSchedulerJobDetails
from .update_task_record_details import UpdateTaskRecordDetails
from .user_action_based_pause_details import UserActionBasedPauseDetails
from .user_action_details import UserActionDetails
from .variable import Variable
from .vault_secret_credential_details import VaultSecretCredentialDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection
from .workflow_component import WorkflowComponent
from .workflow_group import WorkflowGroup
from .workflow_group_component import WorkflowGroupComponent
from .workflow_task_component import WorkflowTaskComponent

# Maps type names to classes for fleet_apps_management services.
fleet_apps_management_type_mapping = {
    "ActionGroup": ActionGroup,
    "ActionGroupBasedUserActionDetails": ActionGroupBasedUserActionDetails,
    "ActionGroupDetails": ActionGroupDetails,
    "ActivityResourceTarget": ActivityResourceTarget,
    "AnnouncementCollection": AnnouncementCollection,
    "AnnouncementSummary": AnnouncementSummary,
    "ApiBasedExecutionDetails": ApiBasedExecutionDetails,
    "ArtifactDetails": ArtifactDetails,
    "AssociatedFleetCredentialDetails": AssociatedFleetCredentialDetails,
    "AssociatedFleetPropertyDetails": AssociatedFleetPropertyDetails,
    "AssociatedFleetResourceDetails": AssociatedFleetResourceDetails,
    "AssociatedLocalTaskDetails": AssociatedLocalTaskDetails,
    "AssociatedSchedulerDefinition": AssociatedSchedulerDefinition,
    "AssociatedSharedTaskDetails": AssociatedSharedTaskDetails,
    "AssociatedTaskDetails": AssociatedTaskDetails,
    "Associations": Associations,
    "CheckResourceTaggingDetails": CheckResourceTaggingDetails,
    "ComplianceDetailPolicy": ComplianceDetailPolicy,
    "ComplianceDetailProduct": ComplianceDetailProduct,
    "ComplianceDetailResource": ComplianceDetailResource,
    "ComplianceDetailTarget": ComplianceDetailTarget,
    "CompliancePatchDetail": CompliancePatchDetail,
    "CompliancePolicy": CompliancePolicy,
    "CompliancePolicyCollection": CompliancePolicyCollection,
    "CompliancePolicyRule": CompliancePolicyRule,
    "CompliancePolicyRuleCollection": CompliancePolicyRuleCollection,
    "CompliancePolicyRuleSummary": CompliancePolicyRuleSummary,
    "CompliancePolicySummary": CompliancePolicySummary,
    "ComplianceRecord": ComplianceRecord,
    "ComplianceRecordAggregation": ComplianceRecordAggregation,
    "ComplianceRecordAggregationCollection": ComplianceRecordAggregationCollection,
    "ComplianceRecordCollection": ComplianceRecordCollection,
    "ComplianceRecordDimension": ComplianceRecordDimension,
    "ComplianceRecordSummary": ComplianceRecordSummary,
    "ComplianceReport": ComplianceReport,
    "ComplianceReportPatchDetail": ComplianceReportPatchDetail,
    "ComplianceReportProduct": ComplianceReportProduct,
    "ComplianceReportResource": ComplianceReportResource,
    "ComplianceReportTarget": ComplianceReportTarget,
    "ComponentProperties": ComponentProperties,
    "Condition": Condition,
    "ConfigAssociationDetails": ConfigAssociationDetails,
    "ConfigCategoryDetails": ConfigCategoryDetails,
    "ConfirmTargetsDetails": ConfirmTargetsDetails,
    "ContentDetails": ContentDetails,
    "CreateCompliancePolicyRuleDetails": CreateCompliancePolicyRuleDetails,
    "CreateFleetCredentialDetails": CreateFleetCredentialDetails,
    "CreateFleetDetails": CreateFleetDetails,
    "CreateFleetPropertyDetails": CreateFleetPropertyDetails,
    "CreateFleetResourceDetails": CreateFleetResourceDetails,
    "CreateMaintenanceWindowDetails": CreateMaintenanceWindowDetails,
    "CreateOnboardingDetails": CreateOnboardingDetails,
    "CreatePatchDetails": CreatePatchDetails,
    "CreatePlatformConfigurationDetails": CreatePlatformConfigurationDetails,
    "CreatePropertyDetails": CreatePropertyDetails,
    "CreateRunbookDetails": CreateRunbookDetails,
    "CreateSchedulerDefinitionDetails": CreateSchedulerDefinitionDetails,
    "CreateTaskRecordDetails": CreateTaskRecordDetails,
    "CredentialConfigCategoryDetails": CredentialConfigCategoryDetails,
    "CredentialDetails": CredentialDetails,
    "CredentialEntitySpecificDetails": CredentialEntitySpecificDetails,
    "DependentPatchDetails": DependentPatchDetails,
    "Details": Details,
    "DiscoveredTarget": DiscoveredTarget,
    "EnableLatestPolicyDetails": EnableLatestPolicyDetails,
    "EntityExecutionDetails": EntityExecutionDetails,
    "EnvironmentConfigCategoryDetails": EnvironmentConfigCategoryDetails,
    "Execution": Execution,
    "ExecutionCollection": ExecutionCollection,
    "ExecutionDetails": ExecutionDetails,
    "ExecutionSummary": ExecutionSummary,
    "ExecutionWorkflowDetails": ExecutionWorkflowDetails,
    "ExportComplianceReportDetails": ExportComplianceReportDetails,
    "Fleet": Fleet,
    "FleetCollection": FleetCollection,
    "FleetCredential": FleetCredential,
    "FleetCredentialCollection": FleetCredentialCollection,
    "FleetCredentialEntitySpecificDetails": FleetCredentialEntitySpecificDetails,
    "FleetCredentialSummary": FleetCredentialSummary,
    "FleetProductCollection": FleetProductCollection,
    "FleetProductSummary": FleetProductSummary,
    "FleetProperty": FleetProperty,
    "FleetPropertyCollection": FleetPropertyCollection,
    "FleetPropertySummary": FleetPropertySummary,
    "FleetResource": FleetResource,
    "FleetResourceCollection": FleetResourceCollection,
    "FleetResourceSummary": FleetResourceSummary,
    "FleetSummary": FleetSummary,
    "FleetTarget": FleetTarget,
    "FleetTargetCollection": FleetTargetCollection,
    "FleetTargetSummary": FleetTargetSummary,
    "GenerateComplianceReportDetails": GenerateComplianceReportDetails,
    "GenericArtifact": GenericArtifact,
    "GenericArtifactDetails": GenericArtifactDetails,
    "Group": Group,
    "InputArgument": InputArgument,
    "InputParameter": InputParameter,
    "InventoryResourceCollection": InventoryResourceCollection,
    "InventoryResourceSummary": InventoryResourceSummary,
    "JobActivity": JobActivity,
    "KeyEncryptionCredentialDetails": KeyEncryptionCredentialDetails,
    "MaintenanceWindow": MaintenanceWindow,
    "MaintenanceWindowCollection": MaintenanceWindowCollection,
    "MaintenanceWindowSummary": MaintenanceWindowSummary,
    "ManageJobExecutionDetails": ManageJobExecutionDetails,
    "ManageSettingsDetails": ManageSettingsDetails,
    "ManagedEntityAggregation": ManagedEntityAggregation,
    "ManagedEntityAggregationCollection": ManagedEntityAggregationCollection,
    "ManagedEntityDimension": ManagedEntityDimension,
    "ModelProperty": ModelProperty,
    "NotificationPreferences": NotificationPreferences,
    "ObjectStorageBucketContentDetails": ObjectStorageBucketContentDetails,
    "Onboarding": Onboarding,
    "OnboardingCollection": OnboardingCollection,
    "OnboardingPolicyCollection": OnboardingPolicyCollection,
    "OnboardingPolicySummary": OnboardingPolicySummary,
    "OnboardingSummary": OnboardingSummary,
    "OperationRunbook": OperationRunbook,
    "Outcome": Outcome,
    "OutputVariableDetails": OutputVariableDetails,
    "OutputVariableInputArgument": OutputVariableInputArgument,
    "OutputVariableMapping": OutputVariableMapping,
    "Patch": Patch,
    "PatchCollection": PatchCollection,
    "PatchLevelSelectionDetails": PatchLevelSelectionDetails,
    "PatchNameSelectionDetails": PatchNameSelectionDetails,
    "PatchProduct": PatchProduct,
    "PatchReleaseDateSelectionDetails": PatchReleaseDateSelectionDetails,
    "PatchSelectionDetails": PatchSelectionDetails,
    "PatchSummary": PatchSummary,
    "PatchType": PatchType,
    "PatchTypeConfigCategoryDetails": PatchTypeConfigCategoryDetails,
    "PauseDetails": PauseDetails,
    "PlainTextCredentialDetails": PlainTextCredentialDetails,
    "PlatformConfiguration": PlatformConfiguration,
    "PlatformConfigurationCollection": PlatformConfigurationCollection,
    "PlatformConfigurationSummary": PlatformConfigurationSummary,
    "PlatformSpecificArtifact": PlatformSpecificArtifact,
    "PlatformSpecificArtifactDetails": PlatformSpecificArtifactDetails,
    "Preferences": Preferences,
    "ProductConfigCategoryDetails": ProductConfigCategoryDetails,
    "ProductStackAsProductSubCategoryDetails": ProductStackAsProductSubCategoryDetails,
    "ProductStackConfigCategoryDetails": ProductStackConfigCategoryDetails,
    "ProductStackGenericSubCategoryDetails": ProductStackGenericSubCategoryDetails,
    "ProductStackSubCategoryDetails": ProductStackSubCategoryDetails,
    "ProductVersionDetails": ProductVersionDetails,
    "Properties": Properties,
    "PropertyCollection": PropertyCollection,
    "PropertySummary": PropertySummary,
    "PublishRunbookDetails": PublishRunbookDetails,
    "RequestResourceValidationDetails": RequestResourceValidationDetails,
    "RequestTargetDiscoveryDetails": RequestTargetDiscoveryDetails,
    "ResourceCollection": ResourceCollection,
    "ResourceCredentialEntitySpecificDetails": ResourceCredentialEntitySpecificDetails,
    "ResourceSummary": ResourceSummary,
    "ResourceTagCheckDetails": ResourceTagCheckDetails,
    "ResourceTagEnablementInfo": ResourceTagEnablementInfo,
    "RollbackWorkflowDetails": RollbackWorkflowDetails,
    "Rule": Rule,
    "Runbook": Runbook,
    "RunbookCollection": RunbookCollection,
    "RunbookSummary": RunbookSummary,
    "Schedule": Schedule,
    "ScheduledFleetCollection": ScheduledFleetCollection,
    "ScheduledFleetSummary": ScheduledFleetSummary,
    "SchedulerDefinition": SchedulerDefinition,
    "SchedulerDefinitionCollection": SchedulerDefinitionCollection,
    "SchedulerDefinitionSummary": SchedulerDefinitionSummary,
    "SchedulerJob": SchedulerJob,
    "SchedulerJobAggregation": SchedulerJobAggregation,
    "SchedulerJobAggregationCollection": SchedulerJobAggregationCollection,
    "SchedulerJobCollection": SchedulerJobCollection,
    "SchedulerJobDimension": SchedulerJobDimension,
    "SchedulerJobSummary": SchedulerJobSummary,
    "ScriptBasedExecutionDetails": ScriptBasedExecutionDetails,
    "SelectionCriteria": SelectionCriteria,
    "SetDefaultRunbookDetails": SetDefaultRunbookDetails,
    "StepBasedUserActionDetails": StepBasedUserActionDetails,
    "StepCollection": StepCollection,
    "StepSummary": StepSummary,
    "StringInputArgument": StringInputArgument,
    "TargetCredentialEntitySpecificDetails": TargetCredentialEntitySpecificDetails,
    "TargetResource": TargetResource,
    "Task": Task,
    "TaskArgument": TaskArgument,
    "TaskNotificationPreferences": TaskNotificationPreferences,
    "TaskRecord": TaskRecord,
    "TaskRecordCollection": TaskRecordCollection,
    "TaskRecordSummary": TaskRecordSummary,
    "TaskVariable": TaskVariable,
    "TimeBasedPauseDetails": TimeBasedPauseDetails,
    "UpdateCompliancePolicyRuleDetails": UpdateCompliancePolicyRuleDetails,
    "UpdateFleetCredentialDetails": UpdateFleetCredentialDetails,
    "UpdateFleetDetails": UpdateFleetDetails,
    "UpdateFleetPropertyDetails": UpdateFleetPropertyDetails,
    "UpdateFleetResourceDetails": UpdateFleetResourceDetails,
    "UpdateMaintenanceWindowDetails": UpdateMaintenanceWindowDetails,
    "UpdateOnboardingDetails": UpdateOnboardingDetails,
    "UpdatePatchDetails": UpdatePatchDetails,
    "UpdatePlatformConfigurationDetails": UpdatePlatformConfigurationDetails,
    "UpdatePropertyDetails": UpdatePropertyDetails,
    "UpdateRunbookDetails": UpdateRunbookDetails,
    "UpdateSchedulerDefinitionDetails": UpdateSchedulerDefinitionDetails,
    "UpdateSchedulerJobDetails": UpdateSchedulerJobDetails,
    "UpdateTaskRecordDetails": UpdateTaskRecordDetails,
    "UserActionBasedPauseDetails": UserActionBasedPauseDetails,
    "UserActionDetails": UserActionDetails,
    "Variable": Variable,
    "VaultSecretCredentialDetails": VaultSecretCredentialDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection,
    "WorkflowComponent": WorkflowComponent,
    "WorkflowGroup": WorkflowGroup,
    "WorkflowGroupComponent": WorkflowGroupComponent,
    "WorkflowTaskComponent": WorkflowTaskComponent
}
