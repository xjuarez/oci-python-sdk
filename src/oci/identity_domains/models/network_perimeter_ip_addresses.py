# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkPerimeterIpAddresses(object):
    """
    IPAddresses or Ranges assigned to the NetworkPerimeter
    """

    #: A constant which can be used with the type property of a NetworkPerimeterIpAddresses.
    #: This constant has a value of "CIDR"
    TYPE_CIDR = "CIDR"

    #: A constant which can be used with the type property of a NetworkPerimeterIpAddresses.
    #: This constant has a value of "RANGE"
    TYPE_RANGE = "RANGE"

    #: A constant which can be used with the type property of a NetworkPerimeterIpAddresses.
    #: This constant has a value of "EXACT"
    TYPE_EXACT = "EXACT"

    #: A constant which can be used with the version property of a NetworkPerimeterIpAddresses.
    #: This constant has a value of "IPV4"
    VERSION_IPV4 = "IPV4"

    #: A constant which can be used with the version property of a NetworkPerimeterIpAddresses.
    #: This constant has a value of "IPV6"
    VERSION_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkPerimeterIpAddresses object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NetworkPerimeterIpAddresses.
            Allowed values for this property are: "CIDR", "RANGE", "EXACT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param version:
            The value to assign to the version property of this NetworkPerimeterIpAddresses.
            Allowed values for this property are: "IPV4", "IPV6", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type version: str

        :param value:
            The value to assign to the value property of this NetworkPerimeterIpAddresses.
        :type value: str

        """
        self.swagger_types = {
            'type': 'str',
            'version': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'version': 'version',
            'value': 'value'
        }

        self._type = None
        self._version = None
        self._value = None

    @property
    def type(self):
        """
        Gets the type of this NetworkPerimeterIpAddresses.
        type of the ip address value

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "CIDR", "RANGE", "EXACT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this NetworkPerimeterIpAddresses.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NetworkPerimeterIpAddresses.
        type of the ip address value

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this NetworkPerimeterIpAddresses.
        :type: str
        """
        allowed_values = ["CIDR", "RANGE", "EXACT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def version(self):
        """
        Gets the version of this NetworkPerimeterIpAddresses.
        Indicates the type of Ip Address example, IPV4 or IPV6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "IPV4", "IPV6", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The version of this NetworkPerimeterIpAddresses.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this NetworkPerimeterIpAddresses.
        Indicates the type of Ip Address example, IPV4 or IPV6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param version: The version of this NetworkPerimeterIpAddresses.
        :type: str
        """
        allowed_values = ["IPV4", "IPV6"]
        if not value_allowed_none_or_none_sentinel(version, allowed_values):
            version = 'UNKNOWN_ENUM_VALUE'
        self._version = version

    @property
    def value(self):
        """
        **[Required]** Gets the value of this NetworkPerimeterIpAddresses.
        Value of exact ipaddress or the range in CIDR or the range with start and end ip addresses

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this NetworkPerimeterIpAddresses.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this NetworkPerimeterIpAddresses.
        Value of exact ipaddress or the range in CIDR or the range with start and end ip addresses

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this NetworkPerimeterIpAddresses.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
