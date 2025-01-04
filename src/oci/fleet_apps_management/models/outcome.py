# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Outcome(object):
    """
    Execution Outcome.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Outcome object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output:
            The value to assign to the output property of this Outcome.
        :type output: str

        :param error:
            The value to assign to the error property of this Outcome.
        :type error: str

        :param exit_code:
            The value to assign to the exit_code property of this Outcome.
        :type exit_code: str

        """
        self.swagger_types = {
            'output': 'str',
            'error': 'str',
            'exit_code': 'str'
        }

        self.attribute_map = {
            'output': 'output',
            'error': 'error',
            'exit_code': 'exitCode'
        }

        self._output = None
        self._error = None
        self._exit_code = None

    @property
    def output(self):
        """
        **[Required]** Gets the output of this Outcome.
        A shortened version of Execution output.


        :return: The output of this Outcome.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this Outcome.
        A shortened version of Execution output.


        :param output: The output of this Outcome.
        :type: str
        """
        self._output = output

    @property
    def error(self):
        """
        Gets the error of this Outcome.
        Errors if any, associated with the execution.


        :return: The error of this Outcome.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this Outcome.
        Errors if any, associated with the execution.


        :param error: The error of this Outcome.
        :type: str
        """
        self._error = error

    @property
    def exit_code(self):
        """
        Gets the exit_code of this Outcome.
        Exit Code.


        :return: The exit_code of this Outcome.
        :rtype: str
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """
        Sets the exit_code of this Outcome.
        Exit Code.


        :param exit_code: The exit_code of this Outcome.
        :type: str
        """
        self._exit_code = exit_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
