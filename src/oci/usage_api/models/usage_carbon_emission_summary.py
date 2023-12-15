# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UsageCarbonEmissionSummary(object):
    """
    The usage carbon emission store result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UsageCarbonEmissionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this UsageCarbonEmissionSummary.
        :type tenant_id: str

        :param tenant_name:
            The value to assign to the tenant_name property of this UsageCarbonEmissionSummary.
        :type tenant_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this UsageCarbonEmissionSummary.
        :type compartment_id: str

        :param compartment_path:
            The value to assign to the compartment_path property of this UsageCarbonEmissionSummary.
        :type compartment_path: str

        :param compartment_name:
            The value to assign to the compartment_name property of this UsageCarbonEmissionSummary.
        :type compartment_name: str

        :param service:
            The value to assign to the service property of this UsageCarbonEmissionSummary.
        :type service: str

        :param resource_name:
            The value to assign to the resource_name property of this UsageCarbonEmissionSummary.
        :type resource_name: str

        :param resource_id:
            The value to assign to the resource_id property of this UsageCarbonEmissionSummary.
        :type resource_id: str

        :param region:
            The value to assign to the region property of this UsageCarbonEmissionSummary.
        :type region: str

        :param ad:
            The value to assign to the ad property of this UsageCarbonEmissionSummary.
        :type ad: str

        :param sku_part_number:
            The value to assign to the sku_part_number property of this UsageCarbonEmissionSummary.
        :type sku_part_number: str

        :param sku_name:
            The value to assign to the sku_name property of this UsageCarbonEmissionSummary.
        :type sku_name: str

        :param platform:
            The value to assign to the platform property of this UsageCarbonEmissionSummary.
        :type platform: str

        :param time_usage_started:
            The value to assign to the time_usage_started property of this UsageCarbonEmissionSummary.
        :type time_usage_started: datetime

        :param time_usage_ended:
            The value to assign to the time_usage_ended property of this UsageCarbonEmissionSummary.
        :type time_usage_ended: datetime

        :param computed_carbon_emission:
            The value to assign to the computed_carbon_emission property of this UsageCarbonEmissionSummary.
        :type computed_carbon_emission: float

        :param emission_calculation_method:
            The value to assign to the emission_calculation_method property of this UsageCarbonEmissionSummary.
        :type emission_calculation_method: str

        :param subscription_id:
            The value to assign to the subscription_id property of this UsageCarbonEmissionSummary.
        :type subscription_id: str

        :param tags:
            The value to assign to the tags property of this UsageCarbonEmissionSummary.
        :type tags: list[oci.usage_api.models.Tag]

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'tenant_name': 'str',
            'compartment_id': 'str',
            'compartment_path': 'str',
            'compartment_name': 'str',
            'service': 'str',
            'resource_name': 'str',
            'resource_id': 'str',
            'region': 'str',
            'ad': 'str',
            'sku_part_number': 'str',
            'sku_name': 'str',
            'platform': 'str',
            'time_usage_started': 'datetime',
            'time_usage_ended': 'datetime',
            'computed_carbon_emission': 'float',
            'emission_calculation_method': 'str',
            'subscription_id': 'str',
            'tags': 'list[Tag]'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'tenant_name': 'tenantName',
            'compartment_id': 'compartmentId',
            'compartment_path': 'compartmentPath',
            'compartment_name': 'compartmentName',
            'service': 'service',
            'resource_name': 'resourceName',
            'resource_id': 'resourceId',
            'region': 'region',
            'ad': 'ad',
            'sku_part_number': 'skuPartNumber',
            'sku_name': 'skuName',
            'platform': 'platform',
            'time_usage_started': 'timeUsageStarted',
            'time_usage_ended': 'timeUsageEnded',
            'computed_carbon_emission': 'computedCarbonEmission',
            'emission_calculation_method': 'emissionCalculationMethod',
            'subscription_id': 'subscriptionId',
            'tags': 'tags'
        }

        self._tenant_id = None
        self._tenant_name = None
        self._compartment_id = None
        self._compartment_path = None
        self._compartment_name = None
        self._service = None
        self._resource_name = None
        self._resource_id = None
        self._region = None
        self._ad = None
        self._sku_part_number = None
        self._sku_name = None
        self._platform = None
        self._time_usage_started = None
        self._time_usage_ended = None
        self._computed_carbon_emission = None
        self._emission_calculation_method = None
        self._subscription_id = None
        self._tags = None

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this UsageCarbonEmissionSummary.
        The tenancy OCID.


        :return: The tenant_id of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this UsageCarbonEmissionSummary.
        The tenancy OCID.


        :param tenant_id: The tenant_id of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """
        Gets the tenant_name of this UsageCarbonEmissionSummary.
        The tenancy name.


        :return: The tenant_name of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """
        Sets the tenant_name of this UsageCarbonEmissionSummary.
        The tenancy name.


        :param tenant_name: The tenant_name of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._tenant_name = tenant_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UsageCarbonEmissionSummary.
        The compartment OCID.


        :return: The compartment_id of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UsageCarbonEmissionSummary.
        The compartment OCID.


        :param compartment_id: The compartment_id of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_path(self):
        """
        Gets the compartment_path of this UsageCarbonEmissionSummary.
        The compartment path, starting from root.


        :return: The compartment_path of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._compartment_path

    @compartment_path.setter
    def compartment_path(self, compartment_path):
        """
        Sets the compartment_path of this UsageCarbonEmissionSummary.
        The compartment path, starting from root.


        :param compartment_path: The compartment_path of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._compartment_path = compartment_path

    @property
    def compartment_name(self):
        """
        Gets the compartment_name of this UsageCarbonEmissionSummary.
        The compartment name.


        :return: The compartment_name of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._compartment_name

    @compartment_name.setter
    def compartment_name(self, compartment_name):
        """
        Sets the compartment_name of this UsageCarbonEmissionSummary.
        The compartment name.


        :param compartment_name: The compartment_name of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._compartment_name = compartment_name

    @property
    def service(self):
        """
        Gets the service of this UsageCarbonEmissionSummary.
        The service name that is incurring the cost.


        :return: The service of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this UsageCarbonEmissionSummary.
        The service name that is incurring the cost.


        :param service: The service of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._service = service

    @property
    def resource_name(self):
        """
        Gets the resource_name of this UsageCarbonEmissionSummary.
        The resource name that is incurring the cost.


        :return: The resource_name of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this UsageCarbonEmissionSummary.
        The resource name that is incurring the cost.


        :param resource_name: The resource_name of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        """
        Gets the resource_id of this UsageCarbonEmissionSummary.
        The resource OCID that is incurring the cost.


        :return: The resource_id of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this UsageCarbonEmissionSummary.
        The resource OCID that is incurring the cost.


        :param resource_id: The resource_id of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def region(self):
        """
        Gets the region of this UsageCarbonEmissionSummary.
        The region of the usage.


        :return: The region of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this UsageCarbonEmissionSummary.
        The region of the usage.


        :param region: The region of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._region = region

    @property
    def ad(self):
        """
        Gets the ad of this UsageCarbonEmissionSummary.
        The availability domain of the usage.


        :return: The ad of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """
        Sets the ad of this UsageCarbonEmissionSummary.
        The availability domain of the usage.


        :param ad: The ad of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._ad = ad

    @property
    def sku_part_number(self):
        """
        Gets the sku_part_number of this UsageCarbonEmissionSummary.
        The SKU part number.


        :return: The sku_part_number of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._sku_part_number

    @sku_part_number.setter
    def sku_part_number(self, sku_part_number):
        """
        Sets the sku_part_number of this UsageCarbonEmissionSummary.
        The SKU part number.


        :param sku_part_number: The sku_part_number of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._sku_part_number = sku_part_number

    @property
    def sku_name(self):
        """
        Gets the sku_name of this UsageCarbonEmissionSummary.
        The SKU friendly name.


        :return: The sku_name of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._sku_name

    @sku_name.setter
    def sku_name(self, sku_name):
        """
        Sets the sku_name of this UsageCarbonEmissionSummary.
        The SKU friendly name.


        :param sku_name: The sku_name of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._sku_name = sku_name

    @property
    def platform(self):
        """
        Gets the platform of this UsageCarbonEmissionSummary.
        Platform for the cost.


        :return: The platform of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this UsageCarbonEmissionSummary.
        Platform for the cost.


        :param platform: The platform of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._platform = platform

    @property
    def time_usage_started(self):
        """
        **[Required]** Gets the time_usage_started of this UsageCarbonEmissionSummary.
        The usage start time.


        :return: The time_usage_started of this UsageCarbonEmissionSummary.
        :rtype: datetime
        """
        return self._time_usage_started

    @time_usage_started.setter
    def time_usage_started(self, time_usage_started):
        """
        Sets the time_usage_started of this UsageCarbonEmissionSummary.
        The usage start time.


        :param time_usage_started: The time_usage_started of this UsageCarbonEmissionSummary.
        :type: datetime
        """
        self._time_usage_started = time_usage_started

    @property
    def time_usage_ended(self):
        """
        **[Required]** Gets the time_usage_ended of this UsageCarbonEmissionSummary.
        The usage end time.


        :return: The time_usage_ended of this UsageCarbonEmissionSummary.
        :rtype: datetime
        """
        return self._time_usage_ended

    @time_usage_ended.setter
    def time_usage_ended(self, time_usage_ended):
        """
        Sets the time_usage_ended of this UsageCarbonEmissionSummary.
        The usage end time.


        :param time_usage_ended: The time_usage_ended of this UsageCarbonEmissionSummary.
        :type: datetime
        """
        self._time_usage_ended = time_usage_ended

    @property
    def computed_carbon_emission(self):
        """
        **[Required]** Gets the computed_carbon_emission of this UsageCarbonEmissionSummary.
        The carbon emission in MTCO2 unit.


        :return: The computed_carbon_emission of this UsageCarbonEmissionSummary.
        :rtype: float
        """
        return self._computed_carbon_emission

    @computed_carbon_emission.setter
    def computed_carbon_emission(self, computed_carbon_emission):
        """
        Sets the computed_carbon_emission of this UsageCarbonEmissionSummary.
        The carbon emission in MTCO2 unit.


        :param computed_carbon_emission: The computed_carbon_emission of this UsageCarbonEmissionSummary.
        :type: float
        """
        self._computed_carbon_emission = computed_carbon_emission

    @property
    def emission_calculation_method(self):
        """
        **[Required]** Gets the emission_calculation_method of this UsageCarbonEmissionSummary.
        The method used to calculate carbon emission.


        :return: The emission_calculation_method of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._emission_calculation_method

    @emission_calculation_method.setter
    def emission_calculation_method(self, emission_calculation_method):
        """
        Sets the emission_calculation_method of this UsageCarbonEmissionSummary.
        The method used to calculate carbon emission.


        :param emission_calculation_method: The emission_calculation_method of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._emission_calculation_method = emission_calculation_method

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this UsageCarbonEmissionSummary.
        The subscription ID.


        :return: The subscription_id of this UsageCarbonEmissionSummary.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this UsageCarbonEmissionSummary.
        The subscription ID.


        :param subscription_id: The subscription_id of this UsageCarbonEmissionSummary.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def tags(self):
        """
        Gets the tags of this UsageCarbonEmissionSummary.
        For grouping, a tag definition. For filtering, a definition and key.


        :return: The tags of this UsageCarbonEmissionSummary.
        :rtype: list[oci.usage_api.models.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UsageCarbonEmissionSummary.
        For grouping, a tag definition. For filtering, a definition and key.


        :param tags: The tags of this UsageCarbonEmissionSummary.
        :type: list[oci.usage_api.models.Tag]
        """
        self._tags = tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
