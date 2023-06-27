# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PromoteSoftwareSourceToLifecycleStageDetails(object):
    """
    A versioned custom software source OCID (softwareSourceId)
    is required when promoting software source content to
    lifecycle stage rank one. Software source content must be
    promoted to lifecycle stage rank one before being
    eligible for promotion to subsequent lifecycle stages,
    else an error is returned. Software source content is
    expected to be promoted in order starting with
    lifecycle stage rank one, followed by rank two, then rank
    three and so on.

    When promoting software source content to lifecycle stage
    rank two, three, four or five, softwareSourceId is optional.
    If a softwareSourceId is provided for a lifecycle stage
    between two and five, the system validates that the
    softwareSourceId is already promoted to the previous lifecycle stage.
    If the softwareSourceId from the previous lifecycle stage
    does not match the provided softwareSourceId an error returns.
    If a softwareSourceId is not provided for a lifecycle stage
    between two and five, the system promotes the
    softwareSourceId from the previous lifecycle stage. If the
    previous lifecycle stage has no SourceSource content
    an error returns.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PromoteSoftwareSourceToLifecycleStageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param work_request_details:
            The value to assign to the work_request_details property of this PromoteSoftwareSourceToLifecycleStageDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'work_request_details': 'WorkRequestDetails'
        }

        self.attribute_map = {
            'work_request_details': 'workRequestDetails'
        }

        self._work_request_details = None

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this PromoteSoftwareSourceToLifecycleStageDetails.

        :return: The work_request_details of this PromoteSoftwareSourceToLifecycleStageDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this PromoteSoftwareSourceToLifecycleStageDetails.

        :param work_request_details: The work_request_details of this PromoteSoftwareSourceToLifecycleStageDetails.
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
