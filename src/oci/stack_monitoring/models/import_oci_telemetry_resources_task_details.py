# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from .monitored_resource_task_details import MonitoredResourceTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportOciTelemetryResourcesTaskDetails(MonitoredResourceTaskDetails):
    """
    Request details for importing resources from Telemetry like resources from OCI Native Services and prometheus.
    """

    #: A constant which can be used with the source property of a ImportOciTelemetryResourcesTaskDetails.
    #: This constant has a value of "OCI_TELEMETRY_NATIVE"
    SOURCE_OCI_TELEMETRY_NATIVE = "OCI_TELEMETRY_NATIVE"

    #: A constant which can be used with the source property of a ImportOciTelemetryResourcesTaskDetails.
    #: This constant has a value of "OCI_TELEMETRY_PROMETHEUS"
    SOURCE_OCI_TELEMETRY_PROMETHEUS = "OCI_TELEMETRY_PROMETHEUS"

    def __init__(self, **kwargs):
        """
        Initializes a new ImportOciTelemetryResourcesTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.ImportOciTelemetryResourcesTaskDetails.type` attribute
        of this class is ``IMPORT_OCI_TELEMETRY_RESOURCES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ImportOciTelemetryResourcesTaskDetails.
            Allowed values for this property are: "IMPORT_OCI_TELEMETRY_RESOURCES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param source:
            The value to assign to the source property of this ImportOciTelemetryResourcesTaskDetails.
            Allowed values for this property are: "OCI_TELEMETRY_NATIVE", "OCI_TELEMETRY_PROMETHEUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source: str

        :param namespace:
            The value to assign to the namespace property of this ImportOciTelemetryResourcesTaskDetails.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this ImportOciTelemetryResourcesTaskDetails.
        :type resource_group: str

        :param should_use_metrics_flow_for_status:
            The value to assign to the should_use_metrics_flow_for_status property of this ImportOciTelemetryResourcesTaskDetails.
        :type should_use_metrics_flow_for_status: bool

        :param service_base_url:
            The value to assign to the service_base_url property of this ImportOciTelemetryResourcesTaskDetails.
        :type service_base_url: str

        :param console_path_prefix:
            The value to assign to the console_path_prefix property of this ImportOciTelemetryResourcesTaskDetails.
        :type console_path_prefix: str

        :param lifecycle_status_mappings_for_up_status:
            The value to assign to the lifecycle_status_mappings_for_up_status property of this ImportOciTelemetryResourcesTaskDetails.
        :type lifecycle_status_mappings_for_up_status: list[str]

        :param resource_name_mapping:
            The value to assign to the resource_name_mapping property of this ImportOciTelemetryResourcesTaskDetails.
        :type resource_name_mapping: str

        :param external_id_mapping:
            The value to assign to the external_id_mapping property of this ImportOciTelemetryResourcesTaskDetails.
        :type external_id_mapping: str

        :param resource_type_mapping:
            The value to assign to the resource_type_mapping property of this ImportOciTelemetryResourcesTaskDetails.
        :type resource_type_mapping: str

        :param resource_name_filter:
            The value to assign to the resource_name_filter property of this ImportOciTelemetryResourcesTaskDetails.
        :type resource_name_filter: str

        :param resource_type_filter:
            The value to assign to the resource_type_filter property of this ImportOciTelemetryResourcesTaskDetails.
        :type resource_type_filter: str

        :param availability_proxy_metrics:
            The value to assign to the availability_proxy_metrics property of this ImportOciTelemetryResourcesTaskDetails.
        :type availability_proxy_metrics: list[str]

        :param availability_proxy_metric_collection_interval:
            The value to assign to the availability_proxy_metric_collection_interval property of this ImportOciTelemetryResourcesTaskDetails.
        :type availability_proxy_metric_collection_interval: int

        """
        self.swagger_types = {
            'type': 'str',
            'source': 'str',
            'namespace': 'str',
            'resource_group': 'str',
            'should_use_metrics_flow_for_status': 'bool',
            'service_base_url': 'str',
            'console_path_prefix': 'str',
            'lifecycle_status_mappings_for_up_status': 'list[str]',
            'resource_name_mapping': 'str',
            'external_id_mapping': 'str',
            'resource_type_mapping': 'str',
            'resource_name_filter': 'str',
            'resource_type_filter': 'str',
            'availability_proxy_metrics': 'list[str]',
            'availability_proxy_metric_collection_interval': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'source': 'source',
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'should_use_metrics_flow_for_status': 'shouldUseMetricsFlowForStatus',
            'service_base_url': 'serviceBaseUrl',
            'console_path_prefix': 'consolePathPrefix',
            'lifecycle_status_mappings_for_up_status': 'lifecycleStatusMappingsForUpStatus',
            'resource_name_mapping': 'resourceNameMapping',
            'external_id_mapping': 'externalIdMapping',
            'resource_type_mapping': 'resourceTypeMapping',
            'resource_name_filter': 'resourceNameFilter',
            'resource_type_filter': 'resourceTypeFilter',
            'availability_proxy_metrics': 'availabilityProxyMetrics',
            'availability_proxy_metric_collection_interval': 'availabilityProxyMetricCollectionInterval'
        }

        self._type = None
        self._source = None
        self._namespace = None
        self._resource_group = None
        self._should_use_metrics_flow_for_status = None
        self._service_base_url = None
        self._console_path_prefix = None
        self._lifecycle_status_mappings_for_up_status = None
        self._resource_name_mapping = None
        self._external_id_mapping = None
        self._resource_type_mapping = None
        self._resource_name_filter = None
        self._resource_type_filter = None
        self._availability_proxy_metrics = None
        self._availability_proxy_metric_collection_interval = None
        self._type = 'IMPORT_OCI_TELEMETRY_RESOURCES'

    @property
    def source(self):
        """
        **[Required]** Gets the source of this ImportOciTelemetryResourcesTaskDetails.
        Source from where the metrics pushed to telemetry.
        Possible values:
          * OCI_TELEMETRY_NATIVE      - The metrics are pushed to telemetry from OCI Native Services.
          * OCI_TELEMETRY_PROMETHEUS  - The metrics are pushed to telemetry from Prometheus.

        Allowed values for this property are: "OCI_TELEMETRY_NATIVE", "OCI_TELEMETRY_PROMETHEUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ImportOciTelemetryResourcesTaskDetails.
        Source from where the metrics pushed to telemetry.
        Possible values:
          * OCI_TELEMETRY_NATIVE      - The metrics are pushed to telemetry from OCI Native Services.
          * OCI_TELEMETRY_PROMETHEUS  - The metrics are pushed to telemetry from Prometheus.


        :param source: The source of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        allowed_values = ["OCI_TELEMETRY_NATIVE", "OCI_TELEMETRY_PROMETHEUS"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            source = 'UNKNOWN_ENUM_VALUE'
        self._source = source

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this ImportOciTelemetryResourcesTaskDetails.
        Name space to be used for OCI Native service resources discovery.


        :return: The namespace of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ImportOciTelemetryResourcesTaskDetails.
        Name space to be used for OCI Native service resources discovery.


        :param namespace: The namespace of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this ImportOciTelemetryResourcesTaskDetails.
        The resource group to use while fetching metrics from telemetry.
        If not specified, resource group will be skipped in the list metrics request.


        :return: The resource_group of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this ImportOciTelemetryResourcesTaskDetails.
        The resource group to use while fetching metrics from telemetry.
        If not specified, resource group will be skipped in the list metrics request.


        :param resource_group: The resource_group of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def should_use_metrics_flow_for_status(self):
        """
        Gets the should_use_metrics_flow_for_status of this ImportOciTelemetryResourcesTaskDetails.
        Flag to indicate whether status is calculated using metrics or
        LifeCycleState attribute of the resource in OCI service.


        :return: The should_use_metrics_flow_for_status of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: bool
        """
        return self._should_use_metrics_flow_for_status

    @should_use_metrics_flow_for_status.setter
    def should_use_metrics_flow_for_status(self, should_use_metrics_flow_for_status):
        """
        Sets the should_use_metrics_flow_for_status of this ImportOciTelemetryResourcesTaskDetails.
        Flag to indicate whether status is calculated using metrics or
        LifeCycleState attribute of the resource in OCI service.


        :param should_use_metrics_flow_for_status: The should_use_metrics_flow_for_status of this ImportOciTelemetryResourcesTaskDetails.
        :type: bool
        """
        self._should_use_metrics_flow_for_status = should_use_metrics_flow_for_status

    @property
    def service_base_url(self):
        """
        Gets the service_base_url of this ImportOciTelemetryResourcesTaskDetails.
        The base URL of the OCI service to which the resource belongs to.
        Also this property is applicable only when source is OCI_TELEMETRY_NATIVE.


        :return: The service_base_url of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._service_base_url

    @service_base_url.setter
    def service_base_url(self, service_base_url):
        """
        Sets the service_base_url of this ImportOciTelemetryResourcesTaskDetails.
        The base URL of the OCI service to which the resource belongs to.
        Also this property is applicable only when source is OCI_TELEMETRY_NATIVE.


        :param service_base_url: The service_base_url of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._service_base_url = service_base_url

    @property
    def console_path_prefix(self):
        """
        Gets the console_path_prefix of this ImportOciTelemetryResourcesTaskDetails.
        The console path prefix to use for providing service home url page navigation.
        For example if the prefix provided is 'security/bastion/bastions', the URL used for navigation will be
        https://<cloudhostname>/security/bastion/bastions/<resourceOcid>. If not provided, service home page link
        will not be shown in the stack monitoring home page.


        :return: The console_path_prefix of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._console_path_prefix

    @console_path_prefix.setter
    def console_path_prefix(self, console_path_prefix):
        """
        Sets the console_path_prefix of this ImportOciTelemetryResourcesTaskDetails.
        The console path prefix to use for providing service home url page navigation.
        For example if the prefix provided is 'security/bastion/bastions', the URL used for navigation will be
        https://<cloudhostname>/security/bastion/bastions/<resourceOcid>. If not provided, service home page link
        will not be shown in the stack monitoring home page.


        :param console_path_prefix: The console_path_prefix of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._console_path_prefix = console_path_prefix

    @property
    def lifecycle_status_mappings_for_up_status(self):
        """
        Gets the lifecycle_status_mappings_for_up_status of this ImportOciTelemetryResourcesTaskDetails.
        Lifecycle states of the external resource which reflects the status of the resource being up.


        :return: The lifecycle_status_mappings_for_up_status of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: list[str]
        """
        return self._lifecycle_status_mappings_for_up_status

    @lifecycle_status_mappings_for_up_status.setter
    def lifecycle_status_mappings_for_up_status(self, lifecycle_status_mappings_for_up_status):
        """
        Sets the lifecycle_status_mappings_for_up_status of this ImportOciTelemetryResourcesTaskDetails.
        Lifecycle states of the external resource which reflects the status of the resource being up.


        :param lifecycle_status_mappings_for_up_status: The lifecycle_status_mappings_for_up_status of this ImportOciTelemetryResourcesTaskDetails.
        :type: list[str]
        """
        self._lifecycle_status_mappings_for_up_status = lifecycle_status_mappings_for_up_status

    @property
    def resource_name_mapping(self):
        """
        Gets the resource_name_mapping of this ImportOciTelemetryResourcesTaskDetails.
        The resource name property in the metric dimensions.
        Resources imported will be using this property value for resource name.


        :return: The resource_name_mapping of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._resource_name_mapping

    @resource_name_mapping.setter
    def resource_name_mapping(self, resource_name_mapping):
        """
        Sets the resource_name_mapping of this ImportOciTelemetryResourcesTaskDetails.
        The resource name property in the metric dimensions.
        Resources imported will be using this property value for resource name.


        :param resource_name_mapping: The resource_name_mapping of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._resource_name_mapping = resource_name_mapping

    @property
    def external_id_mapping(self):
        """
        Gets the external_id_mapping of this ImportOciTelemetryResourcesTaskDetails.
        The external resource identifier property in the metric dimensions.
        Resources imported will be using this property value for external id.


        :return: The external_id_mapping of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._external_id_mapping

    @external_id_mapping.setter
    def external_id_mapping(self, external_id_mapping):
        """
        Sets the external_id_mapping of this ImportOciTelemetryResourcesTaskDetails.
        The external resource identifier property in the metric dimensions.
        Resources imported will be using this property value for external id.


        :param external_id_mapping: The external_id_mapping of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._external_id_mapping = external_id_mapping

    @property
    def resource_type_mapping(self):
        """
        Gets the resource_type_mapping of this ImportOciTelemetryResourcesTaskDetails.
        The resource type property in the metric dimensions.
        Resources imported will be using this property value for resource type.
        If not specified, namespace will be used for resource type.


        :return: The resource_type_mapping of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._resource_type_mapping

    @resource_type_mapping.setter
    def resource_type_mapping(self, resource_type_mapping):
        """
        Sets the resource_type_mapping of this ImportOciTelemetryResourcesTaskDetails.
        The resource type property in the metric dimensions.
        Resources imported will be using this property value for resource type.
        If not specified, namespace will be used for resource type.


        :param resource_type_mapping: The resource_type_mapping of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._resource_type_mapping = resource_type_mapping

    @property
    def resource_name_filter(self):
        """
        Gets the resource_name_filter of this ImportOciTelemetryResourcesTaskDetails.
        The resource name filter. Resources matching with the resource name filter will be imported.
        Regular expressions will be accepted.


        :return: The resource_name_filter of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._resource_name_filter

    @resource_name_filter.setter
    def resource_name_filter(self, resource_name_filter):
        """
        Sets the resource_name_filter of this ImportOciTelemetryResourcesTaskDetails.
        The resource name filter. Resources matching with the resource name filter will be imported.
        Regular expressions will be accepted.


        :param resource_name_filter: The resource_name_filter of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._resource_name_filter = resource_name_filter

    @property
    def resource_type_filter(self):
        """
        Gets the resource_type_filter of this ImportOciTelemetryResourcesTaskDetails.
        The resource type filter. Resources matching with the resource type filter will be imported.
        Regular expressions will be accepted.


        :return: The resource_type_filter of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: str
        """
        return self._resource_type_filter

    @resource_type_filter.setter
    def resource_type_filter(self, resource_type_filter):
        """
        Sets the resource_type_filter of this ImportOciTelemetryResourcesTaskDetails.
        The resource type filter. Resources matching with the resource type filter will be imported.
        Regular expressions will be accepted.


        :param resource_type_filter: The resource_type_filter of this ImportOciTelemetryResourcesTaskDetails.
        :type: str
        """
        self._resource_type_filter = resource_type_filter

    @property
    def availability_proxy_metrics(self):
        """
        Gets the availability_proxy_metrics of this ImportOciTelemetryResourcesTaskDetails.
        List of metrics to be used to calculate the availability of the resource.
        Resource is considered to be up if at least one of the specified metrics is available for
        the resource during the specified interval using the property
        'availabilityProxyMetricCollectionIntervalInSeconds'.
        If no metrics are specified, availability will not be calculated for the resource.


        :return: The availability_proxy_metrics of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: list[str]
        """
        return self._availability_proxy_metrics

    @availability_proxy_metrics.setter
    def availability_proxy_metrics(self, availability_proxy_metrics):
        """
        Sets the availability_proxy_metrics of this ImportOciTelemetryResourcesTaskDetails.
        List of metrics to be used to calculate the availability of the resource.
        Resource is considered to be up if at least one of the specified metrics is available for
        the resource during the specified interval using the property
        'availabilityProxyMetricCollectionIntervalInSeconds'.
        If no metrics are specified, availability will not be calculated for the resource.


        :param availability_proxy_metrics: The availability_proxy_metrics of this ImportOciTelemetryResourcesTaskDetails.
        :type: list[str]
        """
        self._availability_proxy_metrics = availability_proxy_metrics

    @property
    def availability_proxy_metric_collection_interval(self):
        """
        Gets the availability_proxy_metric_collection_interval of this ImportOciTelemetryResourcesTaskDetails.
        Metrics collection interval in seconds used when calculating the availability of the
        resource based on metrics specified using the property 'availabilityProxyMetrics'.


        :return: The availability_proxy_metric_collection_interval of this ImportOciTelemetryResourcesTaskDetails.
        :rtype: int
        """
        return self._availability_proxy_metric_collection_interval

    @availability_proxy_metric_collection_interval.setter
    def availability_proxy_metric_collection_interval(self, availability_proxy_metric_collection_interval):
        """
        Sets the availability_proxy_metric_collection_interval of this ImportOciTelemetryResourcesTaskDetails.
        Metrics collection interval in seconds used when calculating the availability of the
        resource based on metrics specified using the property 'availabilityProxyMetrics'.


        :param availability_proxy_metric_collection_interval: The availability_proxy_metric_collection_interval of this ImportOciTelemetryResourcesTaskDetails.
        :type: int
        """
        self._availability_proxy_metric_collection_interval = availability_proxy_metric_collection_interval

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
