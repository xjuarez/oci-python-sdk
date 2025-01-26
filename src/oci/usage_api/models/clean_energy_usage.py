# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CleanEnergyUsage(object):
    """
    Clean energy usage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CleanEnergyUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this CleanEnergyUsage.
        :type region: str

        :param ad:
            The value to assign to the ad property of this CleanEnergyUsage.
        :type ad: str

        :param usage:
            The value to assign to the usage property of this CleanEnergyUsage.
        :type usage: float

        """
        self.swagger_types = {
            'region': 'str',
            'ad': 'str',
            'usage': 'float'
        }

        self.attribute_map = {
            'region': 'region',
            'ad': 'ad',
            'usage': 'usage'
        }

        self._region = None
        self._ad = None
        self._usage = None

    @property
    def region(self):
        """
        **[Required]** Gets the region of this CleanEnergyUsage.
        The region.


        :return: The region of this CleanEnergyUsage.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CleanEnergyUsage.
        The region.


        :param region: The region of this CleanEnergyUsage.
        :type: str
        """
        self._region = region

    @property
    def ad(self):
        """
        Gets the ad of this CleanEnergyUsage.
        The availability domain.


        :return: The ad of this CleanEnergyUsage.
        :rtype: str
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """
        Sets the ad of this CleanEnergyUsage.
        The availability domain.


        :param ad: The ad of this CleanEnergyUsage.
        :type: str
        """
        self._ad = ad

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this CleanEnergyUsage.
        The percentage of clean enery used.


        :return: The usage of this CleanEnergyUsage.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this CleanEnergyUsage.
        The percentage of clean enery used.


        :param usage: The usage of this CleanEnergyUsage.
        :type: float
        """
        self._usage = usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
