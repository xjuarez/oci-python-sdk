# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails(object):
    """
    Optional. Used to specify from which subnet prefixes an IPv6 address should be allocated, or to assign valid available IPv6 addresses.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ipv6_subnet_cidr:
            The value to assign to the ipv6_subnet_cidr property of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        :type ipv6_subnet_cidr: str

        :param ipv6_address:
            The value to assign to the ipv6_address property of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        :type ipv6_address: str

        """
        self.swagger_types = {
            'ipv6_subnet_cidr': 'str',
            'ipv6_address': 'str'
        }

        self.attribute_map = {
            'ipv6_subnet_cidr': 'ipv6SubnetCidr',
            'ipv6_address': 'ipv6Address'
        }

        self._ipv6_subnet_cidr = None
        self._ipv6_address = None

    @property
    def ipv6_subnet_cidr(self):
        """
        Gets the ipv6_subnet_cidr of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.


        :return: The ipv6_subnet_cidr of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        :rtype: str
        """
        return self._ipv6_subnet_cidr

    @ipv6_subnet_cidr.setter
    def ipv6_subnet_cidr(self, ipv6_subnet_cidr):
        """
        Sets the ipv6_subnet_cidr of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        Optional. Used to disambiguate which subnet prefix should be used to create an IPv6 allocation.


        :param ipv6_subnet_cidr: The ipv6_subnet_cidr of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        :type: str
        """
        self._ipv6_subnet_cidr = ipv6_subnet_cidr

    @property
    def ipv6_address(self):
        """
        Gets the ipv6_address of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        Optional. An available IPv6 address of your subnet from a valid IPv6 prefix on the subnet (otherwise the IP address is automatically assigned).


        :return: The ipv6_address of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """
        Sets the ipv6_address of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        Optional. An available IPv6 address of your subnet from a valid IPv6 prefix on the subnet (otherwise the IP address is automatically assigned).


        :param ipv6_address: The ipv6_address of this InstanceConfigurationIpv6AddressIpv6SubnetCidrPairDetails.
        :type: str
        """
        self._ipv6_address = ipv6_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
