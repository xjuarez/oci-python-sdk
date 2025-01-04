# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .user_action_details import UserActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StepBasedUserActionDetails(UserActionDetails):
    """
    Details for a user action to be performed on a step.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StepBasedUserActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.StepBasedUserActionDetails.level` attribute
        of this class is ``STEP_NAME`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level:
            The value to assign to the level property of this StepBasedUserActionDetails.
            Allowed values for this property are: "ACTION_GROUP", "STEP_NAME"
        :type level: str

        :param action:
            The value to assign to the action property of this StepBasedUserActionDetails.
            Allowed values for this property are: "RETRY", "RESUME"
        :type action: str

        :param action_group_id:
            The value to assign to the action_group_id property of this StepBasedUserActionDetails.
        :type action_group_id: str

        :param resource_id:
            The value to assign to the resource_id property of this StepBasedUserActionDetails.
        :type resource_id: str

        :param target_id:
            The value to assign to the target_id property of this StepBasedUserActionDetails.
        :type target_id: str

        :param step_name:
            The value to assign to the step_name property of this StepBasedUserActionDetails.
        :type step_name: str

        """
        self.swagger_types = {
            'level': 'str',
            'action': 'str',
            'action_group_id': 'str',
            'resource_id': 'str',
            'target_id': 'str',
            'step_name': 'str'
        }

        self.attribute_map = {
            'level': 'level',
            'action': 'action',
            'action_group_id': 'actionGroupId',
            'resource_id': 'resourceId',
            'target_id': 'targetId',
            'step_name': 'stepName'
        }

        self._level = None
        self._action = None
        self._action_group_id = None
        self._resource_id = None
        self._target_id = None
        self._step_name = None
        self._level = 'STEP_NAME'

    @property
    def action_group_id(self):
        """
        **[Required]** Gets the action_group_id of this StepBasedUserActionDetails.
        Unique identifier for the action group.


        :return: The action_group_id of this StepBasedUserActionDetails.
        :rtype: str
        """
        return self._action_group_id

    @action_group_id.setter
    def action_group_id(self, action_group_id):
        """
        Sets the action_group_id of this StepBasedUserActionDetails.
        Unique identifier for the action group.


        :param action_group_id: The action_group_id of this StepBasedUserActionDetails.
        :type: str
        """
        self._action_group_id = action_group_id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this StepBasedUserActionDetails.
        Resource OCID


        :return: The resource_id of this StepBasedUserActionDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this StepBasedUserActionDetails.
        Resource OCID


        :param resource_id: The resource_id of this StepBasedUserActionDetails.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def target_id(self):
        """
        Gets the target_id of this StepBasedUserActionDetails.
        Target associated with the execution.


        :return: The target_id of this StepBasedUserActionDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this StepBasedUserActionDetails.
        Target associated with the execution.


        :param target_id: The target_id of this StepBasedUserActionDetails.
        :type: str
        """
        self._target_id = target_id

    @property
    def step_name(self):
        """
        **[Required]** Gets the step_name of this StepBasedUserActionDetails.
        Name of the step on which user action needs to be performed.


        :return: The step_name of this StepBasedUserActionDetails.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this StepBasedUserActionDetails.
        Name of the step on which user action needs to be performed.


        :param step_name: The step_name of this StepBasedUserActionDetails.
        :type: str
        """
        self._step_name = step_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
