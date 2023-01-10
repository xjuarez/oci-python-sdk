# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskRunLogSummary(object):
    """
    A log message from the execution of a task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaskRunLogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this TaskRunLogSummary.
        :type message: str

        """
        self.swagger_types = {
            'message': 'str'
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = None

    @property
    def message(self):
        """
        Gets the message of this TaskRunLogSummary.
        A user-friendly log message.


        :return: The message of this TaskRunLogSummary.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this TaskRunLogSummary.
        A user-friendly log message.


        :param message: The message of this TaskRunLogSummary.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
