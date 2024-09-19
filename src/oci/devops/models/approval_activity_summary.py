# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .pull_request_activity_summary import PullRequestActivitySummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApprovalActivitySummary(PullRequestActivitySummary):
    """
    activity describing a reviewer's approval decision
    """

    #: A constant which can be used with the status property of a ApprovalActivitySummary.
    #: This constant has a value of "APPROVED"
    STATUS_APPROVED = "APPROVED"

    #: A constant which can be used with the status property of a ApprovalActivitySummary.
    #: This constant has a value of "UNAPPROVED"
    STATUS_UNAPPROVED = "UNAPPROVED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApprovalActivitySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ApprovalActivitySummary.activity_type` attribute
        of this class is ``APPROVAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApprovalActivitySummary.
        :type id: str

        :param principal:
            The value to assign to the principal property of this ApprovalActivitySummary.
        :type principal: oci.devops.models.PrincipalDetails

        :param pull_request_id:
            The value to assign to the pull_request_id property of this ApprovalActivitySummary.
        :type pull_request_id: str

        :param time_occurred:
            The value to assign to the time_occurred property of this ApprovalActivitySummary.
        :type time_occurred: datetime

        :param activity_type:
            The value to assign to the activity_type property of this ApprovalActivitySummary.
            Allowed values for this property are: "LIFECYCLE", "APPROVAL", "COMMIT", "REVIEWER", "COMMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type activity_type: str

        :param status:
            The value to assign to the status property of this ApprovalActivitySummary.
            Allowed values for this property are: "APPROVED", "UNAPPROVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'id': 'str',
            'principal': 'PrincipalDetails',
            'pull_request_id': 'str',
            'time_occurred': 'datetime',
            'activity_type': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'principal': 'principal',
            'pull_request_id': 'pullRequestId',
            'time_occurred': 'timeOccurred',
            'activity_type': 'activityType',
            'status': 'status'
        }

        self._id = None
        self._principal = None
        self._pull_request_id = None
        self._time_occurred = None
        self._activity_type = None
        self._status = None
        self._activity_type = 'APPROVAL'

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ApprovalActivitySummary.
        The approval status of a reviewer

        Allowed values for this property are: "APPROVED", "UNAPPROVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ApprovalActivitySummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ApprovalActivitySummary.
        The approval status of a reviewer


        :param status: The status of this ApprovalActivitySummary.
        :type: str
        """
        allowed_values = ["APPROVED", "UNAPPROVED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
