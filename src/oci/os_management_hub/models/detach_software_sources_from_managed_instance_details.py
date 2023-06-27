# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachSoftwareSourcesFromManagedInstanceDetails(object):
    """
    The details about the software sources to be detached.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachSoftwareSourcesFromManagedInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_sources:
            The value to assign to the software_sources property of this DetachSoftwareSourcesFromManagedInstanceDetails.
        :type software_sources: list[str]

        :param work_request_details:
            The value to assign to the work_request_details property of this DetachSoftwareSourcesFromManagedInstanceDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'software_sources': 'list[str]',
            'work_request_details': 'WorkRequestDetails'
        }

        self.attribute_map = {
            'software_sources': 'softwareSources',
            'work_request_details': 'workRequestDetails'
        }

        self._software_sources = None
        self._work_request_details = None

    @property
    def software_sources(self):
        """
        **[Required]** Gets the software_sources of this DetachSoftwareSourcesFromManagedInstanceDetails.
        The list of software source OCIDs to be attached/detached.


        :return: The software_sources of this DetachSoftwareSourcesFromManagedInstanceDetails.
        :rtype: list[str]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this DetachSoftwareSourcesFromManagedInstanceDetails.
        The list of software source OCIDs to be attached/detached.


        :param software_sources: The software_sources of this DetachSoftwareSourcesFromManagedInstanceDetails.
        :type: list[str]
        """
        self._software_sources = software_sources

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this DetachSoftwareSourcesFromManagedInstanceDetails.

        :return: The work_request_details of this DetachSoftwareSourcesFromManagedInstanceDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this DetachSoftwareSourcesFromManagedInstanceDetails.

        :param work_request_details: The work_request_details of this DetachSoftwareSourcesFromManagedInstanceDetails.
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
