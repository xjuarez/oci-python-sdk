# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScheduledActionDetails(object):
    """
    Describes the modification parameters for the Scheduled Action.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScheduledActionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_params:
            The value to assign to the action_params property of this UpdateScheduledActionDetails.
        :type action_params: dict(str, str)

        :param action_members:
            The value to assign to the action_members property of this UpdateScheduledActionDetails.
        :type action_members: list[oci.database.models.ActionMember]

        :param scheduling_window_id:
            The value to assign to the scheduling_window_id property of this UpdateScheduledActionDetails.
        :type scheduling_window_id: str

        """
        self.swagger_types = {
            'action_params': 'dict(str, str)',
            'action_members': 'list[ActionMember]',
            'scheduling_window_id': 'str'
        }

        self.attribute_map = {
            'action_params': 'actionParams',
            'action_members': 'actionMembers',
            'scheduling_window_id': 'schedulingWindowId'
        }

        self._action_params = None
        self._action_members = None
        self._scheduling_window_id = None

    @property
    def action_params(self):
        """
        Gets the action_params of this UpdateScheduledActionDetails.
        Map<ParamName, ParamValue> where a key value pair describes the specific action parameter.
        Example: `{\"count\": \"3\"}`


        :return: The action_params of this UpdateScheduledActionDetails.
        :rtype: dict(str, str)
        """
        return self._action_params

    @action_params.setter
    def action_params(self, action_params):
        """
        Sets the action_params of this UpdateScheduledActionDetails.
        Map<ParamName, ParamValue> where a key value pair describes the specific action parameter.
        Example: `{\"count\": \"3\"}`


        :param action_params: The action_params of this UpdateScheduledActionDetails.
        :type: dict(str, str)
        """
        self._action_params = action_params

    @property
    def action_members(self):
        """
        Gets the action_members of this UpdateScheduledActionDetails.
        The list of action members in a scheduled action.


        :return: The action_members of this UpdateScheduledActionDetails.
        :rtype: list[oci.database.models.ActionMember]
        """
        return self._action_members

    @action_members.setter
    def action_members(self, action_members):
        """
        Sets the action_members of this UpdateScheduledActionDetails.
        The list of action members in a scheduled action.


        :param action_members: The action_members of this UpdateScheduledActionDetails.
        :type: list[oci.database.models.ActionMember]
        """
        self._action_members = action_members

    @property
    def scheduling_window_id(self):
        """
        Gets the scheduling_window_id of this UpdateScheduledActionDetails.
        The `OCID`__ of the Scheduling Window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scheduling_window_id of this UpdateScheduledActionDetails.
        :rtype: str
        """
        return self._scheduling_window_id

    @scheduling_window_id.setter
    def scheduling_window_id(self, scheduling_window_id):
        """
        Sets the scheduling_window_id of this UpdateScheduledActionDetails.
        The `OCID`__ of the Scheduling Window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scheduling_window_id: The scheduling_window_id of this UpdateScheduledActionDetails.
        :type: str
        """
        self._scheduling_window_id = scheduling_window_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
