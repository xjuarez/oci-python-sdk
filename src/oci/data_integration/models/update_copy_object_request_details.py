# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCopyObjectRequestDetails(object):
    """
    Properties used in copy object request update operations.
    """

    #: A constant which can be used with the status property of a UpdateCopyObjectRequestDetails.
    #: This constant has a value of "TERMINATING"
    STATUS_TERMINATING = "TERMINATING"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCopyObjectRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateCopyObjectRequestDetails.
            Allowed values for this property are: "TERMINATING"
        :type status: str

        """
        self.swagger_types = {
            'status': 'str'
        }

        self.attribute_map = {
            'status': 'status'
        }

        self._status = None

    @property
    def status(self):
        """
        Gets the status of this UpdateCopyObjectRequestDetails.
        The status of the object.

        Allowed values for this property are: "TERMINATING"


        :return: The status of this UpdateCopyObjectRequestDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateCopyObjectRequestDetails.
        The status of the object.


        :param status: The status of this UpdateCopyObjectRequestDetails.
        :type: str
        """
        allowed_values = ["TERMINATING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
