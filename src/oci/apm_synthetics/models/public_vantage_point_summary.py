# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicVantagePointSummary(object):
    """
    Information about public vantage points.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PublicVantagePointSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this PublicVantagePointSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this PublicVantagePointSummary.
        :type name: str

        :param geo:
            The value to assign to the geo property of this PublicVantagePointSummary.
        :type geo: oci.apm_synthetics.models.GeoSummary

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'geo': 'GeoSummary'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'geo': 'geo'
        }

        self._display_name = None
        self._name = None
        self._geo = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PublicVantagePointSummary.
        Unique name that can be edited. The name should not contain any confidential information.


        :return: The display_name of this PublicVantagePointSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PublicVantagePointSummary.
        Unique name that can be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this PublicVantagePointSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PublicVantagePointSummary.
        Unique permanent name of the vantage point.


        :return: The name of this PublicVantagePointSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PublicVantagePointSummary.
        Unique permanent name of the vantage point.


        :param name: The name of this PublicVantagePointSummary.
        :type: str
        """
        self._name = name

    @property
    def geo(self):
        """
        Gets the geo of this PublicVantagePointSummary.

        :return: The geo of this PublicVantagePointSummary.
        :rtype: oci.apm_synthetics.models.GeoSummary
        """
        return self._geo

    @geo.setter
    def geo(self, geo):
        """
        Sets the geo of this PublicVantagePointSummary.

        :param geo: The geo of this PublicVantagePointSummary.
        :type: oci.apm_synthetics.models.GeoSummary
        """
        self._geo = geo

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
