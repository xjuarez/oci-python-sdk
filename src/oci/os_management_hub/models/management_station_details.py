# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementStationDetails(object):
    """
    The config details of the management stations to be configured for a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementStationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param primary_management_station_id:
            The value to assign to the primary_management_station_id property of this ManagementStationDetails.
        :type primary_management_station_id: str

        :param secondary_management_station_id:
            The value to assign to the secondary_management_station_id property of this ManagementStationDetails.
        :type secondary_management_station_id: str

        :param work_request_details:
            The value to assign to the work_request_details property of this ManagementStationDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'primary_management_station_id': 'str',
            'secondary_management_station_id': 'str',
            'work_request_details': 'WorkRequestDetails'
        }

        self.attribute_map = {
            'primary_management_station_id': 'primaryManagementStationId',
            'secondary_management_station_id': 'secondaryManagementStationId',
            'work_request_details': 'workRequestDetails'
        }

        self._primary_management_station_id = None
        self._secondary_management_station_id = None
        self._work_request_details = None

    @property
    def primary_management_station_id(self):
        """
        **[Required]** Gets the primary_management_station_id of this ManagementStationDetails.
        The OCID of a management station to be used as the preferred primary.


        :return: The primary_management_station_id of this ManagementStationDetails.
        :rtype: str
        """
        return self._primary_management_station_id

    @primary_management_station_id.setter
    def primary_management_station_id(self, primary_management_station_id):
        """
        Sets the primary_management_station_id of this ManagementStationDetails.
        The OCID of a management station to be used as the preferred primary.


        :param primary_management_station_id: The primary_management_station_id of this ManagementStationDetails.
        :type: str
        """
        self._primary_management_station_id = primary_management_station_id

    @property
    def secondary_management_station_id(self):
        """
        Gets the secondary_management_station_id of this ManagementStationDetails.
        The OCID of a management station to be used as the preferred secondary.


        :return: The secondary_management_station_id of this ManagementStationDetails.
        :rtype: str
        """
        return self._secondary_management_station_id

    @secondary_management_station_id.setter
    def secondary_management_station_id(self, secondary_management_station_id):
        """
        Sets the secondary_management_station_id of this ManagementStationDetails.
        The OCID of a management station to be used as the preferred secondary.


        :param secondary_management_station_id: The secondary_management_station_id of this ManagementStationDetails.
        :type: str
        """
        self._secondary_management_station_id = secondary_management_station_id

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this ManagementStationDetails.

        :return: The work_request_details of this ManagementStationDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this ManagementStationDetails.

        :param work_request_details: The work_request_details of this ManagementStationDetails.
        :type: oci.os_management_hub.models.WorkRequestDetails
        """
        self._work_request_details = work_request_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
