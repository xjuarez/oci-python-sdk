# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAddressListDetails(object):
    """
    The Request for creating the address List
    """

    #: A constant which can be used with the type property of a CreateAddressListDetails.
    #: This constant has a value of "FQDN"
    TYPE_FQDN = "FQDN"

    #: A constant which can be used with the type property of a CreateAddressListDetails.
    #: This constant has a value of "IP"
    TYPE_IP = "IP"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAddressListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateAddressListDetails.
        :type name: str

        :param type:
            The value to assign to the type property of this CreateAddressListDetails.
            Allowed values for this property are: "FQDN", "IP"
        :type type: str

        :param addresses:
            The value to assign to the addresses property of this CreateAddressListDetails.
        :type addresses: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'addresses': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'addresses': 'addresses'
        }

        self._name = None
        self._type = None
        self._addresses = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateAddressListDetails.
        Unique name to identify the group of addresses to be used in the policy rules.


        :return: The name of this CreateAddressListDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateAddressListDetails.
        Unique name to identify the group of addresses to be used in the policy rules.


        :param name: The name of this CreateAddressListDetails.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateAddressListDetails.
        Type of address List. The accepted values are - * FQDN * IP

        Allowed values for this property are: "FQDN", "IP"


        :return: The type of this CreateAddressListDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateAddressListDetails.
        Type of address List. The accepted values are - * FQDN * IP


        :param type: The type of this CreateAddressListDetails.
        :type: str
        """
        allowed_values = ["FQDN", "IP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def addresses(self):
        """
        **[Required]** Gets the addresses of this CreateAddressListDetails.
        List of addresses.


        :return: The addresses of this CreateAddressListDetails.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this CreateAddressListDetails.
        List of addresses.


        :param addresses: The addresses of this CreateAddressListDetails.
        :type: list[str]
        """
        self._addresses = addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
