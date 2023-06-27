# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAllPackagesOnManagedInstanceGroupDetails(object):
    """
    The work request details for the update operation on the managed instance group.
    """

    #: A constant which can be used with the update_types property of a UpdateAllPackagesOnManagedInstanceGroupDetails.
    #: This constant has a value of "SECURITY"
    UPDATE_TYPES_SECURITY = "SECURITY"

    #: A constant which can be used with the update_types property of a UpdateAllPackagesOnManagedInstanceGroupDetails.
    #: This constant has a value of "BUGFIX"
    UPDATE_TYPES_BUGFIX = "BUGFIX"

    #: A constant which can be used with the update_types property of a UpdateAllPackagesOnManagedInstanceGroupDetails.
    #: This constant has a value of "ENHANCEMENT"
    UPDATE_TYPES_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the update_types property of a UpdateAllPackagesOnManagedInstanceGroupDetails.
    #: This constant has a value of "OTHER"
    UPDATE_TYPES_OTHER = "OTHER"

    #: A constant which can be used with the update_types property of a UpdateAllPackagesOnManagedInstanceGroupDetails.
    #: This constant has a value of "KSPLICE_KERNEL"
    UPDATE_TYPES_KSPLICE_KERNEL = "KSPLICE_KERNEL"

    #: A constant which can be used with the update_types property of a UpdateAllPackagesOnManagedInstanceGroupDetails.
    #: This constant has a value of "KSPLICE_USERSPACE"
    UPDATE_TYPES_KSPLICE_USERSPACE = "KSPLICE_USERSPACE"

    #: A constant which can be used with the update_types property of a UpdateAllPackagesOnManagedInstanceGroupDetails.
    #: This constant has a value of "ALL"
    UPDATE_TYPES_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAllPackagesOnManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param update_types:
            The value to assign to the update_types property of this UpdateAllPackagesOnManagedInstanceGroupDetails.
            Allowed values for items in this list are: "SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", "KSPLICE_KERNEL", "KSPLICE_USERSPACE", "ALL"
        :type update_types: list[str]

        :param work_request_details:
            The value to assign to the work_request_details property of this UpdateAllPackagesOnManagedInstanceGroupDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'update_types': 'list[str]',
            'work_request_details': 'WorkRequestDetails'
        }

        self.attribute_map = {
            'update_types': 'updateTypes',
            'work_request_details': 'workRequestDetails'
        }

        self._update_types = None
        self._work_request_details = None

    @property
    def update_types(self):
        """
        Gets the update_types of this UpdateAllPackagesOnManagedInstanceGroupDetails.
        The type of updates to be applied.

        Allowed values for items in this list are: "SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", "KSPLICE_KERNEL", "KSPLICE_USERSPACE", "ALL"


        :return: The update_types of this UpdateAllPackagesOnManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._update_types

    @update_types.setter
    def update_types(self, update_types):
        """
        Sets the update_types of this UpdateAllPackagesOnManagedInstanceGroupDetails.
        The type of updates to be applied.


        :param update_types: The update_types of this UpdateAllPackagesOnManagedInstanceGroupDetails.
        :type: list[str]
        """
        allowed_values = ["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", "KSPLICE_KERNEL", "KSPLICE_USERSPACE", "ALL"]

        if update_types and update_types is not NONE_SENTINEL:
            for value in update_types:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `update_types`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._update_types = update_types

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this UpdateAllPackagesOnManagedInstanceGroupDetails.

        :return: The work_request_details of this UpdateAllPackagesOnManagedInstanceGroupDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this UpdateAllPackagesOnManagedInstanceGroupDetails.

        :param work_request_details: The work_request_details of this UpdateAllPackagesOnManagedInstanceGroupDetails.
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
