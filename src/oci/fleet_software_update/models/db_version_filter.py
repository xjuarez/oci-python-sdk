# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .db_fleet_discovery_filter import DbFleetDiscoveryFilter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbVersionFilter(DbFleetDiscoveryFilter):
    """
    Versions to include in the discovery. These should be under the Source Major Version of the Collection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbVersionFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.DbVersionFilter.type` attribute
        of this class is ``VERSION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DbVersionFilter.
            Allowed values for this property are: "COMPARTMENT_ID", "VERSION", "DB_NAME", "DB_UNIQUE_NAME", "DB_HOME_NAME", "FREEFORM_TAG", "DEFINED_TAG", "RESOURCE_ID"
        :type type: str

        :param mode:
            The value to assign to the mode property of this DbVersionFilter.
            Allowed values for this property are: "INCLUDE", "EXCLUDE"
        :type mode: str

        :param versions:
            The value to assign to the versions property of this DbVersionFilter.
        :type versions: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'mode': 'str',
            'versions': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'mode': 'mode',
            'versions': 'versions'
        }

        self._type = None
        self._mode = None
        self._versions = None
        self._type = 'VERSION'

    @property
    def versions(self):
        """
        **[Required]** Gets the versions of this DbVersionFilter.
        List of Version strings to include in the discovery.


        :return: The versions of this DbVersionFilter.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this DbVersionFilter.
        List of Version strings to include in the discovery.


        :param versions: The versions of this DbVersionFilter.
        :type: list[str]
        """
        self._versions = versions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
