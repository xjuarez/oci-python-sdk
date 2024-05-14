# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531

from .unified_agent_monitoring_application_configuration_details import UnifiedAgentMonitoringApplicationConfigurationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentUrlConfigurationDetails(UnifiedAgentMonitoringApplicationConfigurationDetails):
    """
    Unified Agent scrape URL configuration object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentUrlConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentUrlConfigurationDetails.source_type` attribute
        of this class is ``URL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this UnifiedAgentUrlConfigurationDetails.
            Allowed values for this property are: "KUBERNETES", "TAIL", "URL"
        :type source_type: str

        :param source:
            The value to assign to the source property of this UnifiedAgentUrlConfigurationDetails.
        :type source: oci.logging.models.UnifiedAgentMonitoringUrlSource

        :param filter:
            The value to assign to the filter property of this UnifiedAgentUrlConfigurationDetails.
        :type filter: oci.logging.models.UnifiedAgentUrlFilter

        :param destination:
            The value to assign to the destination property of this UnifiedAgentUrlConfigurationDetails.
        :type destination: oci.logging.models.UnifiedAgentMonitoringDestination

        """
        self.swagger_types = {
            'source_type': 'str',
            'source': 'UnifiedAgentMonitoringUrlSource',
            'filter': 'UnifiedAgentUrlFilter',
            'destination': 'UnifiedAgentMonitoringDestination'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'source': 'source',
            'filter': 'filter',
            'destination': 'destination'
        }

        self._source_type = None
        self._source = None
        self._filter = None
        self._destination = None
        self._source_type = 'URL'

    @property
    def source(self):
        """
        **[Required]** Gets the source of this UnifiedAgentUrlConfigurationDetails.

        :return: The source of this UnifiedAgentUrlConfigurationDetails.
        :rtype: oci.logging.models.UnifiedAgentMonitoringUrlSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this UnifiedAgentUrlConfigurationDetails.

        :param source: The source of this UnifiedAgentUrlConfigurationDetails.
        :type: oci.logging.models.UnifiedAgentMonitoringUrlSource
        """
        self._source = source

    @property
    def filter(self):
        """
        Gets the filter of this UnifiedAgentUrlConfigurationDetails.

        :return: The filter of this UnifiedAgentUrlConfigurationDetails.
        :rtype: oci.logging.models.UnifiedAgentUrlFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this UnifiedAgentUrlConfigurationDetails.

        :param filter: The filter of this UnifiedAgentUrlConfigurationDetails.
        :type: oci.logging.models.UnifiedAgentUrlFilter
        """
        self._filter = filter

    @property
    def destination(self):
        """
        **[Required]** Gets the destination of this UnifiedAgentUrlConfigurationDetails.

        :return: The destination of this UnifiedAgentUrlConfigurationDetails.
        :rtype: oci.logging.models.UnifiedAgentMonitoringDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this UnifiedAgentUrlConfigurationDetails.

        :param destination: The destination of this UnifiedAgentUrlConfigurationDetails.
        :type: oci.logging.models.UnifiedAgentMonitoringDestination
        """
        self._destination = destination

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
