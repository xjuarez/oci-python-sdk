# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .execution_details import ExecutionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScriptBasedExecutionDetails(ExecutionDetails):
    """
    Details for script-based execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScriptBasedExecutionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.ScriptBasedExecutionDetails.execution_type` attribute
        of this class is ``SCRIPT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param execution_type:
            The value to assign to the execution_type property of this ScriptBasedExecutionDetails.
            Allowed values for this property are: "SCRIPT", "API"
        :type execution_type: str

        :param variables:
            The value to assign to the variables property of this ScriptBasedExecutionDetails.
        :type variables: oci.fleet_apps_management.models.TaskVariable

        :param content:
            The value to assign to the content property of this ScriptBasedExecutionDetails.
        :type content: oci.fleet_apps_management.models.ContentDetails

        :param command:
            The value to assign to the command property of this ScriptBasedExecutionDetails.
        :type command: str

        :param credentials:
            The value to assign to the credentials property of this ScriptBasedExecutionDetails.
        :type credentials: list[oci.fleet_apps_management.models.ConfigAssociationDetails]

        """
        self.swagger_types = {
            'execution_type': 'str',
            'variables': 'TaskVariable',
            'content': 'ContentDetails',
            'command': 'str',
            'credentials': 'list[ConfigAssociationDetails]'
        }

        self.attribute_map = {
            'execution_type': 'executionType',
            'variables': 'variables',
            'content': 'content',
            'command': 'command',
            'credentials': 'credentials'
        }

        self._execution_type = None
        self._variables = None
        self._content = None
        self._command = None
        self._credentials = None
        self._execution_type = 'SCRIPT'

    @property
    def variables(self):
        """
        Gets the variables of this ScriptBasedExecutionDetails.

        :return: The variables of this ScriptBasedExecutionDetails.
        :rtype: oci.fleet_apps_management.models.TaskVariable
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this ScriptBasedExecutionDetails.

        :param variables: The variables of this ScriptBasedExecutionDetails.
        :type: oci.fleet_apps_management.models.TaskVariable
        """
        self._variables = variables

    @property
    def content(self):
        """
        Gets the content of this ScriptBasedExecutionDetails.

        :return: The content of this ScriptBasedExecutionDetails.
        :rtype: oci.fleet_apps_management.models.ContentDetails
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this ScriptBasedExecutionDetails.

        :param content: The content of this ScriptBasedExecutionDetails.
        :type: oci.fleet_apps_management.models.ContentDetails
        """
        self._content = content

    @property
    def command(self):
        """
        Gets the command of this ScriptBasedExecutionDetails.
        Optional command to execute the content.
        You can provide any commands/arguments that can't be part of the script.


        :return: The command of this ScriptBasedExecutionDetails.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this ScriptBasedExecutionDetails.
        Optional command to execute the content.
        You can provide any commands/arguments that can't be part of the script.


        :param command: The command of this ScriptBasedExecutionDetails.
        :type: str
        """
        self._command = command

    @property
    def credentials(self):
        """
        Gets the credentials of this ScriptBasedExecutionDetails.
        Credentials required for executing the task.


        :return: The credentials of this ScriptBasedExecutionDetails.
        :rtype: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ScriptBasedExecutionDetails.
        Credentials required for executing the task.


        :param credentials: The credentials of this ScriptBasedExecutionDetails.
        :type: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        self._credentials = credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
