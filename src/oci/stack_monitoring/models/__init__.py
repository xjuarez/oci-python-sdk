# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from __future__ import absolute_import

from .anomaly_data_point import AnomalyDataPoint
from .anomaly_metric_data import AnomalyMetricData
from .associate_monitored_resources_details import AssociateMonitoredResourcesDetails
from .associated_monitored_resource import AssociatedMonitoredResource
from .associated_resources_collection import AssociatedResourcesCollection
from .associated_resources_summary import AssociatedResourcesSummary
from .association_details import AssociationDetails
from .association_resource_details import AssociationResourceDetails
from .auto_promote_config_details import AutoPromoteConfigDetails
from .auto_promote_config_summary import AutoPromoteConfigSummary
from .baselineable_metric import BaselineableMetric
from .baselineable_metric_summary import BaselineableMetricSummary
from .baselineable_metric_summary_collection import BaselineableMetricSummaryCollection
from .change_config_compartment_details import ChangeConfigCompartmentDetails
from .change_metric_extension_compartment_details import ChangeMetricExtensionCompartmentDetails
from .change_monitored_resource_compartment_details import ChangeMonitoredResourceCompartmentDetails
from .change_monitored_resource_task_compartment_details import ChangeMonitoredResourceTaskCompartmentDetails
from .change_process_set_compartment_details import ChangeProcessSetCompartmentDetails
from .config import Config
from .config_collection import ConfigCollection
from .config_summary import ConfigSummary
from .connection_details import ConnectionDetails
from .create_auto_promote_config_details import CreateAutoPromoteConfigDetails
from .create_baselineable_metric_details import CreateBaselineableMetricDetails
from .create_config_details import CreateConfigDetails
from .create_discovery_job_details import CreateDiscoveryJobDetails
from .create_license_auto_assign_config_details import CreateLicenseAutoAssignConfigDetails
from .create_license_enterprise_extensibility_config_details import CreateLicenseEnterpriseExtensibilityConfigDetails
from .create_maintenance_window_details import CreateMaintenanceWindowDetails
from .create_maintenance_window_resource_details import CreateMaintenanceWindowResourceDetails
from .create_metric_extension_details import CreateMetricExtensionDetails
from .create_monitored_resource_details import CreateMonitoredResourceDetails
from .create_monitored_resource_task_details import CreateMonitoredResourceTaskDetails
from .create_monitored_resource_type_details import CreateMonitoredResourceTypeDetails
from .create_process_set_details import CreateProcessSetDetails
from .credential_collection import CredentialCollection
from .credential_details import CredentialDetails
from .credential_property import CredentialProperty
from .data_point import DataPoint
from .disable_metric_extension_details import DisableMetricExtensionDetails
from .disassociate_monitored_resources_details import DisassociateMonitoredResourcesDetails
from .discovery_details import DiscoveryDetails
from .discovery_job import DiscoveryJob
from .discovery_job_collection import DiscoveryJobCollection
from .discovery_job_log_collection import DiscoveryJobLogCollection
from .discovery_job_log_summary import DiscoveryJobLogSummary
from .discovery_job_summary import DiscoveryJobSummary
from .enable_metric_extension_details import EnableMetricExtensionDetails
from .enabled_resource_details import EnabledResourceDetails
from .encrypted_credentials import EncryptedCredentials
from .evaluate_baselineable_metric_details import EvaluateBaselineableMetricDetails
from .evaluate_baselineable_metric_result import EvaluateBaselineableMetricResult
from .http_query_properties import HttpQueryProperties
from .http_script_file_details import HttpScriptFileDetails
from .http_update_query_properties import HttpUpdateQueryProperties
from .import_oci_telemetry_resources_task_details import ImportOciTelemetryResourcesTaskDetails
from .jmx_query_properties import JmxQueryProperties
from .jmx_update_query_properties import JmxUpdateQueryProperties
from .license_auto_assign_config_details import LicenseAutoAssignConfigDetails
from .license_auto_assign_config_summary import LicenseAutoAssignConfigSummary
from .license_enterprise_extensibility_config_details import LicenseEnterpriseExtensibilityConfigDetails
from .license_enterprise_extensibility_config_summary import LicenseEnterpriseExtensibilityConfigSummary
from .maintenance_window import MaintenanceWindow
from .maintenance_window_collection import MaintenanceWindowCollection
from .maintenance_window_schedule import MaintenanceWindowSchedule
from .maintenance_window_summary import MaintenanceWindowSummary
from .manage_license_details import ManageLicenseDetails
from .metric import Metric
from .metric_data import MetricData
from .metric_extension import MetricExtension
from .metric_extension_collection import MetricExtensionCollection
from .metric_extension_query_properties import MetricExtensionQueryProperties
from .metric_extension_summary import MetricExtensionSummary
from .metric_extension_update_query_properties import MetricExtensionUpdateQueryProperties
from .monitored_resource import MonitoredResource
from .monitored_resource_alias_credential import MonitoredResourceAliasCredential
from .monitored_resource_alias_source_credential import MonitoredResourceAliasSourceCredential
from .monitored_resource_association import MonitoredResourceAssociation
from .monitored_resource_association_summary import MonitoredResourceAssociationSummary
from .monitored_resource_associations_collection import MonitoredResourceAssociationsCollection
from .monitored_resource_collection import MonitoredResourceCollection
from .monitored_resource_credential import MonitoredResourceCredential
from .monitored_resource_details import MonitoredResourceDetails
from .monitored_resource_member_summary import MonitoredResourceMemberSummary
from .monitored_resource_members_collection import MonitoredResourceMembersCollection
from .monitored_resource_property import MonitoredResourceProperty
from .monitored_resource_summary import MonitoredResourceSummary
from .monitored_resource_task import MonitoredResourceTask
from .monitored_resource_task_details import MonitoredResourceTaskDetails
from .monitored_resource_task_summary import MonitoredResourceTaskSummary
from .monitored_resource_tasks_collection import MonitoredResourceTasksCollection
from .monitored_resource_type import MonitoredResourceType
from .monitored_resource_type_summary import MonitoredResourceTypeSummary
from .monitored_resource_types_collection import MonitoredResourceTypesCollection
from .monitored_resources_count_aggregation import MonitoredResourcesCountAggregation
from .monitored_resources_count_aggregation_collection import MonitoredResourcesCountAggregationCollection
from .one_time_maintenance_window_schedule import OneTimeMaintenanceWindowSchedule
from .os_command_query_properties import OsCommandQueryProperties
from .os_command_update_query_properties import OsCommandUpdateQueryProperties
from .plain_text_credentials import PlainTextCredentials
from .pre_existing_credentials import PreExistingCredentials
from .process_set import ProcessSet
from .process_set_collection import ProcessSetCollection
from .process_set_specification import ProcessSetSpecification
from .process_set_specification_details import ProcessSetSpecificationDetails
from .process_set_summary import ProcessSetSummary
from .property_details import PropertyDetails
from .recurrent_maintenance_window_schedule import RecurrentMaintenanceWindowSchedule
from .resource_type_metadata_details import ResourceTypeMetadataDetails
from .script_file_details import ScriptFileDetails
from .search_associated_resources_details import SearchAssociatedResourcesDetails
from .search_monitored_resource_associations_details import SearchMonitoredResourceAssociationsDetails
from .search_monitored_resource_members_details import SearchMonitoredResourceMembersDetails
from .search_monitored_resources_details import SearchMonitoredResourcesDetails
from .sql_details import SqlDetails
from .sql_in_param_details import SqlInParamDetails
from .sql_out_param_details import SqlOutParamDetails
from .sql_query_properties import SqlQueryProperties
from .sql_update_query_properties import SqlUpdateQueryProperties
from .system_format_resource_type_metadata_details import SystemFormatResourceTypeMetadataDetails
from .test_metric_extension_data import TestMetricExtensionData
from .test_metric_extension_details import TestMetricExtensionDetails
from .unique_property_set import UniquePropertySet
from .update_and_propagate_tags_details import UpdateAndPropagateTagsDetails
from .update_auto_promote_config_details import UpdateAutoPromoteConfigDetails
from .update_baselineable_metric_details import UpdateBaselineableMetricDetails
from .update_config_details import UpdateConfigDetails
from .update_http_script_file_details import UpdateHttpScriptFileDetails
from .update_license_auto_assign_config_details import UpdateLicenseAutoAssignConfigDetails
from .update_license_enterprise_extensibility_config_details import UpdateLicenseEnterpriseExtensibilityConfigDetails
from .update_maintenance_window_details import UpdateMaintenanceWindowDetails
from .update_metric_extension_details import UpdateMetricExtensionDetails
from .update_monitored_resource_details import UpdateMonitoredResourceDetails
from .update_monitored_resource_task_details import UpdateMonitoredResourceTaskDetails
from .update_monitored_resource_type_details import UpdateMonitoredResourceTypeDetails
from .update_process_set_details import UpdateProcessSetDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for stack_monitoring services.
stack_monitoring_type_mapping = {
    "AnomalyDataPoint": AnomalyDataPoint,
    "AnomalyMetricData": AnomalyMetricData,
    "AssociateMonitoredResourcesDetails": AssociateMonitoredResourcesDetails,
    "AssociatedMonitoredResource": AssociatedMonitoredResource,
    "AssociatedResourcesCollection": AssociatedResourcesCollection,
    "AssociatedResourcesSummary": AssociatedResourcesSummary,
    "AssociationDetails": AssociationDetails,
    "AssociationResourceDetails": AssociationResourceDetails,
    "AutoPromoteConfigDetails": AutoPromoteConfigDetails,
    "AutoPromoteConfigSummary": AutoPromoteConfigSummary,
    "BaselineableMetric": BaselineableMetric,
    "BaselineableMetricSummary": BaselineableMetricSummary,
    "BaselineableMetricSummaryCollection": BaselineableMetricSummaryCollection,
    "ChangeConfigCompartmentDetails": ChangeConfigCompartmentDetails,
    "ChangeMetricExtensionCompartmentDetails": ChangeMetricExtensionCompartmentDetails,
    "ChangeMonitoredResourceCompartmentDetails": ChangeMonitoredResourceCompartmentDetails,
    "ChangeMonitoredResourceTaskCompartmentDetails": ChangeMonitoredResourceTaskCompartmentDetails,
    "ChangeProcessSetCompartmentDetails": ChangeProcessSetCompartmentDetails,
    "Config": Config,
    "ConfigCollection": ConfigCollection,
    "ConfigSummary": ConfigSummary,
    "ConnectionDetails": ConnectionDetails,
    "CreateAutoPromoteConfigDetails": CreateAutoPromoteConfigDetails,
    "CreateBaselineableMetricDetails": CreateBaselineableMetricDetails,
    "CreateConfigDetails": CreateConfigDetails,
    "CreateDiscoveryJobDetails": CreateDiscoveryJobDetails,
    "CreateLicenseAutoAssignConfigDetails": CreateLicenseAutoAssignConfigDetails,
    "CreateLicenseEnterpriseExtensibilityConfigDetails": CreateLicenseEnterpriseExtensibilityConfigDetails,
    "CreateMaintenanceWindowDetails": CreateMaintenanceWindowDetails,
    "CreateMaintenanceWindowResourceDetails": CreateMaintenanceWindowResourceDetails,
    "CreateMetricExtensionDetails": CreateMetricExtensionDetails,
    "CreateMonitoredResourceDetails": CreateMonitoredResourceDetails,
    "CreateMonitoredResourceTaskDetails": CreateMonitoredResourceTaskDetails,
    "CreateMonitoredResourceTypeDetails": CreateMonitoredResourceTypeDetails,
    "CreateProcessSetDetails": CreateProcessSetDetails,
    "CredentialCollection": CredentialCollection,
    "CredentialDetails": CredentialDetails,
    "CredentialProperty": CredentialProperty,
    "DataPoint": DataPoint,
    "DisableMetricExtensionDetails": DisableMetricExtensionDetails,
    "DisassociateMonitoredResourcesDetails": DisassociateMonitoredResourcesDetails,
    "DiscoveryDetails": DiscoveryDetails,
    "DiscoveryJob": DiscoveryJob,
    "DiscoveryJobCollection": DiscoveryJobCollection,
    "DiscoveryJobLogCollection": DiscoveryJobLogCollection,
    "DiscoveryJobLogSummary": DiscoveryJobLogSummary,
    "DiscoveryJobSummary": DiscoveryJobSummary,
    "EnableMetricExtensionDetails": EnableMetricExtensionDetails,
    "EnabledResourceDetails": EnabledResourceDetails,
    "EncryptedCredentials": EncryptedCredentials,
    "EvaluateBaselineableMetricDetails": EvaluateBaselineableMetricDetails,
    "EvaluateBaselineableMetricResult": EvaluateBaselineableMetricResult,
    "HttpQueryProperties": HttpQueryProperties,
    "HttpScriptFileDetails": HttpScriptFileDetails,
    "HttpUpdateQueryProperties": HttpUpdateQueryProperties,
    "ImportOciTelemetryResourcesTaskDetails": ImportOciTelemetryResourcesTaskDetails,
    "JmxQueryProperties": JmxQueryProperties,
    "JmxUpdateQueryProperties": JmxUpdateQueryProperties,
    "LicenseAutoAssignConfigDetails": LicenseAutoAssignConfigDetails,
    "LicenseAutoAssignConfigSummary": LicenseAutoAssignConfigSummary,
    "LicenseEnterpriseExtensibilityConfigDetails": LicenseEnterpriseExtensibilityConfigDetails,
    "LicenseEnterpriseExtensibilityConfigSummary": LicenseEnterpriseExtensibilityConfigSummary,
    "MaintenanceWindow": MaintenanceWindow,
    "MaintenanceWindowCollection": MaintenanceWindowCollection,
    "MaintenanceWindowSchedule": MaintenanceWindowSchedule,
    "MaintenanceWindowSummary": MaintenanceWindowSummary,
    "ManageLicenseDetails": ManageLicenseDetails,
    "Metric": Metric,
    "MetricData": MetricData,
    "MetricExtension": MetricExtension,
    "MetricExtensionCollection": MetricExtensionCollection,
    "MetricExtensionQueryProperties": MetricExtensionQueryProperties,
    "MetricExtensionSummary": MetricExtensionSummary,
    "MetricExtensionUpdateQueryProperties": MetricExtensionUpdateQueryProperties,
    "MonitoredResource": MonitoredResource,
    "MonitoredResourceAliasCredential": MonitoredResourceAliasCredential,
    "MonitoredResourceAliasSourceCredential": MonitoredResourceAliasSourceCredential,
    "MonitoredResourceAssociation": MonitoredResourceAssociation,
    "MonitoredResourceAssociationSummary": MonitoredResourceAssociationSummary,
    "MonitoredResourceAssociationsCollection": MonitoredResourceAssociationsCollection,
    "MonitoredResourceCollection": MonitoredResourceCollection,
    "MonitoredResourceCredential": MonitoredResourceCredential,
    "MonitoredResourceDetails": MonitoredResourceDetails,
    "MonitoredResourceMemberSummary": MonitoredResourceMemberSummary,
    "MonitoredResourceMembersCollection": MonitoredResourceMembersCollection,
    "MonitoredResourceProperty": MonitoredResourceProperty,
    "MonitoredResourceSummary": MonitoredResourceSummary,
    "MonitoredResourceTask": MonitoredResourceTask,
    "MonitoredResourceTaskDetails": MonitoredResourceTaskDetails,
    "MonitoredResourceTaskSummary": MonitoredResourceTaskSummary,
    "MonitoredResourceTasksCollection": MonitoredResourceTasksCollection,
    "MonitoredResourceType": MonitoredResourceType,
    "MonitoredResourceTypeSummary": MonitoredResourceTypeSummary,
    "MonitoredResourceTypesCollection": MonitoredResourceTypesCollection,
    "MonitoredResourcesCountAggregation": MonitoredResourcesCountAggregation,
    "MonitoredResourcesCountAggregationCollection": MonitoredResourcesCountAggregationCollection,
    "OneTimeMaintenanceWindowSchedule": OneTimeMaintenanceWindowSchedule,
    "OsCommandQueryProperties": OsCommandQueryProperties,
    "OsCommandUpdateQueryProperties": OsCommandUpdateQueryProperties,
    "PlainTextCredentials": PlainTextCredentials,
    "PreExistingCredentials": PreExistingCredentials,
    "ProcessSet": ProcessSet,
    "ProcessSetCollection": ProcessSetCollection,
    "ProcessSetSpecification": ProcessSetSpecification,
    "ProcessSetSpecificationDetails": ProcessSetSpecificationDetails,
    "ProcessSetSummary": ProcessSetSummary,
    "PropertyDetails": PropertyDetails,
    "RecurrentMaintenanceWindowSchedule": RecurrentMaintenanceWindowSchedule,
    "ResourceTypeMetadataDetails": ResourceTypeMetadataDetails,
    "ScriptFileDetails": ScriptFileDetails,
    "SearchAssociatedResourcesDetails": SearchAssociatedResourcesDetails,
    "SearchMonitoredResourceAssociationsDetails": SearchMonitoredResourceAssociationsDetails,
    "SearchMonitoredResourceMembersDetails": SearchMonitoredResourceMembersDetails,
    "SearchMonitoredResourcesDetails": SearchMonitoredResourcesDetails,
    "SqlDetails": SqlDetails,
    "SqlInParamDetails": SqlInParamDetails,
    "SqlOutParamDetails": SqlOutParamDetails,
    "SqlQueryProperties": SqlQueryProperties,
    "SqlUpdateQueryProperties": SqlUpdateQueryProperties,
    "SystemFormatResourceTypeMetadataDetails": SystemFormatResourceTypeMetadataDetails,
    "TestMetricExtensionData": TestMetricExtensionData,
    "TestMetricExtensionDetails": TestMetricExtensionDetails,
    "UniquePropertySet": UniquePropertySet,
    "UpdateAndPropagateTagsDetails": UpdateAndPropagateTagsDetails,
    "UpdateAutoPromoteConfigDetails": UpdateAutoPromoteConfigDetails,
    "UpdateBaselineableMetricDetails": UpdateBaselineableMetricDetails,
    "UpdateConfigDetails": UpdateConfigDetails,
    "UpdateHttpScriptFileDetails": UpdateHttpScriptFileDetails,
    "UpdateLicenseAutoAssignConfigDetails": UpdateLicenseAutoAssignConfigDetails,
    "UpdateLicenseEnterpriseExtensibilityConfigDetails": UpdateLicenseEnterpriseExtensibilityConfigDetails,
    "UpdateMaintenanceWindowDetails": UpdateMaintenanceWindowDetails,
    "UpdateMetricExtensionDetails": UpdateMetricExtensionDetails,
    "UpdateMonitoredResourceDetails": UpdateMonitoredResourceDetails,
    "UpdateMonitoredResourceTaskDetails": UpdateMonitoredResourceTaskDetails,
    "UpdateMonitoredResourceTypeDetails": UpdateMonitoredResourceTypeDetails,
    "UpdateProcessSetDetails": UpdateProcessSetDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
