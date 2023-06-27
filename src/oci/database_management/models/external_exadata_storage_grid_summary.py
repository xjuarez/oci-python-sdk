# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dbm_resource import DbmResource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataStorageGridSummary(DbmResource):
    """
    The Exadata storage server grid of the Exadata infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataStorageGridSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalExadataStorageGridSummary.resource_type` attribute
        of this class is ``STORAGE_GRID_SUMMARY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataStorageGridSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalExadataStorageGridSummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalExadataStorageGridSummary.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalExadataStorageGridSummary.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalExadataStorageGridSummary.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalExadataStorageGridSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ExternalExadataStorageGridSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalExadataStorageGridSummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalExadataStorageGridSummary.
        :type lifecycle_details: str

        :param additional_details:
            The value to assign to the additional_details property of this ExternalExadataStorageGridSummary.
        :type additional_details: dict(str, str)

        :param resource_type:
            The value to assign to the resource_type property of this ExternalExadataStorageGridSummary.
            Allowed values for this property are: "INFRASTRUCTURE_SUMMARY", "INFRASTRUCTURE", "STORAGE_SERVER_SUMMARY", "STORAGE_SERVER", "STORAGE_GRID_SUMMARY", "STORAGE_GRID", "STORAGE_CONNECTOR_SUMMARY", "STORAGE_CONNECTOR", "DATABASE_SYSTEM_SUMMARY", "DATABASE_SUMMARY"
        :type resource_type: str

        :param server_count:
            The value to assign to the server_count property of this ExternalExadataStorageGridSummary.
        :type server_count: float

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'additional_details': 'dict(str, str)',
            'resource_type': 'str',
            'server_count': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'additional_details': 'additionalDetails',
            'resource_type': 'resourceType',
            'server_count': 'serverCount'
        }

        self._id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._additional_details = None
        self._resource_type = None
        self._server_count = None
        self._resource_type = 'STORAGE_GRID_SUMMARY'

    @property
    def server_count(self):
        """
        Gets the server_count of this ExternalExadataStorageGridSummary.
        The number of Exadata storage servers in the Exadata infrastructure.


        :return: The server_count of this ExternalExadataStorageGridSummary.
        :rtype: float
        """
        return self._server_count

    @server_count.setter
    def server_count(self, server_count):
        """
        Sets the server_count of this ExternalExadataStorageGridSummary.
        The number of Exadata storage servers in the Exadata infrastructure.


        :param server_count: The server_count of this ExternalExadataStorageGridSummary.
        :type: float
        """
        self._server_count = server_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
