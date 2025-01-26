# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531

from .unified_agent_monitoring_filter import UnifiedAgentMonitoringFilter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentUrlFilter(UnifiedAgentMonitoringFilter):
    """
    Kubernetes filter object
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentUrlFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentUrlFilter.filter_type` attribute
        of this class is ``URL_FILTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UnifiedAgentUrlFilter.
        :type name: str

        :param filter_type:
            The value to assign to the filter_type property of this UnifiedAgentUrlFilter.
            Allowed values for this property are: "KUBERNETES_FILTER", "URL_FILTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        :param allow_list:
            The value to assign to the allow_list property of this UnifiedAgentUrlFilter.
        :type allow_list: list[str]

        :param deny_list:
            The value to assign to the deny_list property of this UnifiedAgentUrlFilter.
        :type deny_list: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'filter_type': 'str',
            'allow_list': 'list[str]',
            'deny_list': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'filter_type': 'filterType',
            'allow_list': 'allowList',
            'deny_list': 'denyList'
        }

        self._name = None
        self._filter_type = None
        self._allow_list = None
        self._deny_list = None
        self._filter_type = 'URL_FILTER'

    @property
    def allow_list(self):
        """
        Gets the allow_list of this UnifiedAgentUrlFilter.
        List of metrics regex to be allowed.


        :return: The allow_list of this UnifiedAgentUrlFilter.
        :rtype: list[str]
        """
        return self._allow_list

    @allow_list.setter
    def allow_list(self, allow_list):
        """
        Sets the allow_list of this UnifiedAgentUrlFilter.
        List of metrics regex to be allowed.


        :param allow_list: The allow_list of this UnifiedAgentUrlFilter.
        :type: list[str]
        """
        self._allow_list = allow_list

    @property
    def deny_list(self):
        """
        Gets the deny_list of this UnifiedAgentUrlFilter.
        List of metrics regex to be denied.


        :return: The deny_list of this UnifiedAgentUrlFilter.
        :rtype: list[str]
        """
        return self._deny_list

    @deny_list.setter
    def deny_list(self, deny_list):
        """
        Sets the deny_list of this UnifiedAgentUrlFilter.
        List of metrics regex to be denied.


        :param deny_list: The deny_list of this UnifiedAgentUrlFilter.
        :type: list[str]
        """
        self._deny_list = deny_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
