# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GranularMaintenanceHistoryDetails(object):
    """
    Details of a granular maintenance history.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GranularMaintenanceHistoryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param execution_window:
            The value to assign to the execution_window property of this GranularMaintenanceHistoryDetails.
        :type execution_window: oci.database.models.ExecutionWindow

        :param execution_actions:
            The value to assign to the execution_actions property of this GranularMaintenanceHistoryDetails.
        :type execution_actions: list[oci.database.models.ExecutionAction]

        """
        self.swagger_types = {
            'execution_window': 'ExecutionWindow',
            'execution_actions': 'list[ExecutionAction]'
        }

        self.attribute_map = {
            'execution_window': 'executionWindow',
            'execution_actions': 'executionActions'
        }

        self._execution_window = None
        self._execution_actions = None

    @property
    def execution_window(self):
        """
        **[Required]** Gets the execution_window of this GranularMaintenanceHistoryDetails.

        :return: The execution_window of this GranularMaintenanceHistoryDetails.
        :rtype: oci.database.models.ExecutionWindow
        """
        return self._execution_window

    @execution_window.setter
    def execution_window(self, execution_window):
        """
        Sets the execution_window of this GranularMaintenanceHistoryDetails.

        :param execution_window: The execution_window of this GranularMaintenanceHistoryDetails.
        :type: oci.database.models.ExecutionWindow
        """
        self._execution_window = execution_window

    @property
    def execution_actions(self):
        """
        **[Required]** Gets the execution_actions of this GranularMaintenanceHistoryDetails.
        The list of execution actions for this granular maintenance history.


        :return: The execution_actions of this GranularMaintenanceHistoryDetails.
        :rtype: list[oci.database.models.ExecutionAction]
        """
        return self._execution_actions

    @execution_actions.setter
    def execution_actions(self, execution_actions):
        """
        Sets the execution_actions of this GranularMaintenanceHistoryDetails.
        The list of execution actions for this granular maintenance history.


        :param execution_actions: The execution_actions of this GranularMaintenanceHistoryDetails.
        :type: list[oci.database.models.ExecutionAction]
        """
        self._execution_actions = execution_actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
