# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GeographicalLocation(object):
    """
    The geographical location of a problem in terms of latitude and longitude.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GeographicalLocation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param latitude:
            The value to assign to the latitude property of this GeographicalLocation.
        :type latitude: float

        :param longitude:
            The value to assign to the longitude property of this GeographicalLocation.
        :type longitude: float

        """
        self.swagger_types = {
            'latitude': 'float',
            'longitude': 'float'
        }

        self.attribute_map = {
            'latitude': 'latitude',
            'longitude': 'longitude'
        }

        self._latitude = None
        self._longitude = None

    @property
    def latitude(self):
        """
        **[Required]** Gets the latitude of this GeographicalLocation.
        Latitude of problem


        :return: The latitude of this GeographicalLocation.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this GeographicalLocation.
        Latitude of problem


        :param latitude: The latitude of this GeographicalLocation.
        :type: float
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """
        **[Required]** Gets the longitude of this GeographicalLocation.
        Longitude of problem


        :return: The longitude of this GeographicalLocation.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this GeographicalLocation.
        Longitude of problem


        :param longitude: The longitude of this GeographicalLocation.
        :type: float
        """
        self._longitude = longitude

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
