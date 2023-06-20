# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnvironmentRole(object):
    """
    Describes the role of the FA Environment.
    """

    #: A constant which can be used with the current_role property of a EnvironmentRole.
    #: This constant has a value of "PRIMARY"
    CURRENT_ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the current_role property of a EnvironmentRole.
    #: This constant has a value of "STANDBY"
    CURRENT_ROLE_STANDBY = "STANDBY"

    def __init__(self, **kwargs):
        """
        Initializes a new EnvironmentRole object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param current_role:
            The value to assign to the current_role property of this EnvironmentRole.
            Allowed values for this property are: "PRIMARY", "STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type current_role: str

        :param standby_environment_region:
            The value to assign to the standby_environment_region property of this EnvironmentRole.
        :type standby_environment_region: str

        :param standby_environment_id:
            The value to assign to the standby_environment_id property of this EnvironmentRole.
        :type standby_environment_id: str

        """
        self.swagger_types = {
            'current_role': 'str',
            'standby_environment_region': 'str',
            'standby_environment_id': 'str'
        }

        self.attribute_map = {
            'current_role': 'currentRole',
            'standby_environment_region': 'standbyEnvironmentRegion',
            'standby_environment_id': 'standbyEnvironmentId'
        }

        self._current_role = None
        self._standby_environment_region = None
        self._standby_environment_id = None

    @property
    def current_role(self):
        """
        Gets the current_role of this EnvironmentRole.
        The current role of the environment

        Allowed values for this property are: "PRIMARY", "STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The current_role of this EnvironmentRole.
        :rtype: str
        """
        return self._current_role

    @current_role.setter
    def current_role(self, current_role):
        """
        Sets the current_role of this EnvironmentRole.
        The current role of the environment


        :param current_role: The current_role of this EnvironmentRole.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY"]
        if not value_allowed_none_or_none_sentinel(current_role, allowed_values):
            current_role = 'UNKNOWN_ENUM_VALUE'
        self._current_role = current_role

    @property
    def standby_environment_region(self):
        """
        Gets the standby_environment_region of this EnvironmentRole.
        Region the standby environment is in


        :return: The standby_environment_region of this EnvironmentRole.
        :rtype: str
        """
        return self._standby_environment_region

    @standby_environment_region.setter
    def standby_environment_region(self, standby_environment_region):
        """
        Sets the standby_environment_region of this EnvironmentRole.
        Region the standby environment is in


        :param standby_environment_region: The standby_environment_region of this EnvironmentRole.
        :type: str
        """
        self._standby_environment_region = standby_environment_region

    @property
    def standby_environment_id(self):
        """
        Gets the standby_environment_id of this EnvironmentRole.
        Fusion Environment ID of the standby environment


        :return: The standby_environment_id of this EnvironmentRole.
        :rtype: str
        """
        return self._standby_environment_id

    @standby_environment_id.setter
    def standby_environment_id(self, standby_environment_id):
        """
        Sets the standby_environment_id of this EnvironmentRole.
        Fusion Environment ID of the standby environment


        :param standby_environment_id: The standby_environment_id of this EnvironmentRole.
        :type: str
        """
        self._standby_environment_id = standby_environment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
