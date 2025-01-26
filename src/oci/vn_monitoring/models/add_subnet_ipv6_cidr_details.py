# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddSubnetIpv6CidrDetails(object):
    """
    Details used when adding an IPv6 CIDR block to a subnet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddSubnetIpv6CidrDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this AddSubnetIpv6CidrDetails.
        :type ipv6_cidr_block: str

        """
        self.swagger_types = {
            'ipv6_cidr_block': 'str'
        }

        self.attribute_map = {
            'ipv6_cidr_block': 'ipv6CidrBlock'
        }

        self._ipv6_cidr_block = None

    @property
    def ipv6_cidr_block(self):
        """
        **[Required]** Gets the ipv6_cidr_block of this AddSubnetIpv6CidrDetails.
        This field is not required and should only be specified when adding an IPv6 CIDR
        to a subnet's IPv6 address space.
        See`IPv6 Addresses`__.

        Example: `2001:0db8:0123::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The ipv6_cidr_block of this AddSubnetIpv6CidrDetails.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this AddSubnetIpv6CidrDetails.
        This field is not required and should only be specified when adding an IPv6 CIDR
        to a subnet's IPv6 address space.
        See`IPv6 Addresses`__.

        Example: `2001:0db8:0123::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param ipv6_cidr_block: The ipv6_cidr_block of this AddSubnetIpv6CidrDetails.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
