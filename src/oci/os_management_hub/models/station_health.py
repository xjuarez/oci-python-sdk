# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StationHealth(object):
    """
    Overall health information of the management station.
    """

    #: A constant which can be used with the state property of a StationHealth.
    #: This constant has a value of "HEALTHY"
    STATE_HEALTHY = "HEALTHY"

    #: A constant which can be used with the state property of a StationHealth.
    #: This constant has a value of "UNHEALTHY"
    STATE_UNHEALTHY = "UNHEALTHY"

    def __init__(self, **kwargs):
        """
        Initializes a new StationHealth object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param state:
            The value to assign to the state property of this StationHealth.
            Allowed values for this property are: "HEALTHY", "UNHEALTHY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        :param description:
            The value to assign to the description property of this StationHealth.
        :type description: str

        """
        self.swagger_types = {
            'state': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'state': 'state',
            'description': 'description'
        }

        self._state = None
        self._description = None

    @property
    def state(self):
        """
        **[Required]** Gets the state of this StationHealth.
        Overall health status of the management station.

        Allowed values for this property are: "HEALTHY", "UNHEALTHY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this StationHealth.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this StationHealth.
        Overall health status of the management station.


        :param state: The state of this StationHealth.
        :type: str
        """
        allowed_values = ["HEALTHY", "UNHEALTHY"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    @property
    def description(self):
        """
        Gets the description of this StationHealth.
        Explanation of the health status.


        :return: The description of this StationHealth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StationHealth.
        Explanation of the health status.


        :param description: The description of this StationHealth.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
