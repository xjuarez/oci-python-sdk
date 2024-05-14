# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .gi_fleet_discovery_details import GiFleetDiscoveryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiFiltersDiscovery(GiFleetDiscoveryDetails):
    """
    Collection discovery done from the results of the specified filters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GiFiltersDiscovery object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.GiFiltersDiscovery.strategy` attribute
        of this class is ``FILTERS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy:
            The value to assign to the strategy property of this GiFiltersDiscovery.
            Allowed values for this property are: "SEARCH_QUERY", "FILTERS", "TARGET_LIST", "DISCOVERY_RESULTS"
        :type strategy: str

        :param filters:
            The value to assign to the filters property of this GiFiltersDiscovery.
        :type filters: list[oci.fleet_software_update.models.GiFleetDiscoveryFilter]

        """
        self.swagger_types = {
            'strategy': 'str',
            'filters': 'list[GiFleetDiscoveryFilter]'
        }

        self.attribute_map = {
            'strategy': 'strategy',
            'filters': 'filters'
        }

        self._strategy = None
        self._filters = None
        self._strategy = 'FILTERS'

    @property
    def filters(self):
        """
        **[Required]** Gets the filters of this GiFiltersDiscovery.
        Filters to perform the target discovery.


        :return: The filters of this GiFiltersDiscovery.
        :rtype: list[oci.fleet_software_update.models.GiFleetDiscoveryFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this GiFiltersDiscovery.
        Filters to perform the target discovery.


        :param filters: The filters of this GiFiltersDiscovery.
        :type: list[oci.fleet_software_update.models.GiFleetDiscoveryFilter]
        """
        self._filters = filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
