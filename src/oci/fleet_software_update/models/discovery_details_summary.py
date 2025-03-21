# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveryDetailsSummary(object):
    """
    Summarized Discovery details.
    """

    #: A constant which can be used with the type property of a DiscoveryDetailsSummary.
    #: This constant has a value of "DB"
    TYPE_DB = "DB"

    #: A constant which can be used with the type property of a DiscoveryDetailsSummary.
    #: This constant has a value of "GI"
    TYPE_GI = "GI"

    #: A constant which can be used with the service_type property of a DiscoveryDetailsSummary.
    #: This constant has a value of "EXACS"
    SERVICE_TYPE_EXACS = "EXACS"

    #: A constant which can be used with the service_type property of a DiscoveryDetailsSummary.
    #: This constant has a value of "EXACC"
    SERVICE_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the criteria property of a DiscoveryDetailsSummary.
    #: This constant has a value of "SEARCH_QUERY"
    CRITERIA_SEARCH_QUERY = "SEARCH_QUERY"

    #: A constant which can be used with the criteria property of a DiscoveryDetailsSummary.
    #: This constant has a value of "FILTERS"
    CRITERIA_FILTERS = "FILTERS"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveryDetailsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DiscoveryDetailsSummary.
            Allowed values for this property are: "DB", "GI", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param service_type:
            The value to assign to the service_type property of this DiscoveryDetailsSummary.
            Allowed values for this property are: "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_type: str

        :param criteria:
            The value to assign to the criteria property of this DiscoveryDetailsSummary.
            Allowed values for this property are: "SEARCH_QUERY", "FILTERS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type criteria: str

        """
        self.swagger_types = {
            'type': 'str',
            'service_type': 'str',
            'criteria': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'service_type': 'serviceType',
            'criteria': 'criteria'
        }

        self._type = None
        self._service_type = None
        self._criteria = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DiscoveryDetailsSummary.
        Exadata Fleet Update Discovery type.

        Allowed values for this property are: "DB", "GI", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DiscoveryDetailsSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DiscoveryDetailsSummary.
        Exadata Fleet Update Discovery type.


        :param type: The type of this DiscoveryDetailsSummary.
        :type: str
        """
        allowed_values = ["DB", "GI"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def service_type(self):
        """
        **[Required]** Gets the service_type of this DiscoveryDetailsSummary.
        Exadata service type for the target resource members.

        Allowed values for this property are: "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The service_type of this DiscoveryDetailsSummary.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this DiscoveryDetailsSummary.
        Exadata service type for the target resource members.


        :param service_type: The service_type of this DiscoveryDetailsSummary.
        :type: str
        """
        allowed_values = ["EXACS", "EXACC"]
        if not value_allowed_none_or_none_sentinel(service_type, allowed_values):
            service_type = 'UNKNOWN_ENUM_VALUE'
        self._service_type = service_type

    @property
    def criteria(self):
        """
        Gets the criteria of this DiscoveryDetailsSummary.
        Criteria used for Exadata Fleet Update Discovery.

        Allowed values for this property are: "SEARCH_QUERY", "FILTERS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The criteria of this DiscoveryDetailsSummary.
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this DiscoveryDetailsSummary.
        Criteria used for Exadata Fleet Update Discovery.


        :param criteria: The criteria of this DiscoveryDetailsSummary.
        :type: str
        """
        allowed_values = ["SEARCH_QUERY", "FILTERS"]
        if not value_allowed_none_or_none_sentinel(criteria, allowed_values):
            criteria = 'UNKNOWN_ENUM_VALUE'
        self._criteria = criteria

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
