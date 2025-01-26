# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledAction(object):
    """
    Details of a Scheduled Action.
    """

    #: A constant which can be used with the action_type property of a ScheduledAction.
    #: This constant has a value of "DB_SERVER_FULL_SOFTWARE_UPDATE"
    ACTION_TYPE_DB_SERVER_FULL_SOFTWARE_UPDATE = "DB_SERVER_FULL_SOFTWARE_UPDATE"

    #: A constant which can be used with the action_type property of a ScheduledAction.
    #: This constant has a value of "STORAGE_SERVER_FULL_SOFTWARE_UPDATE"
    ACTION_TYPE_STORAGE_SERVER_FULL_SOFTWARE_UPDATE = "STORAGE_SERVER_FULL_SOFTWARE_UPDATE"

    #: A constant which can be used with the action_type property of a ScheduledAction.
    #: This constant has a value of "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE"
    ACTION_TYPE_NETWORK_SWITCH_FULL_SOFTWARE_UPDATE = "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE"

    #: A constant which can be used with the lifecycle_state property of a ScheduledAction.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledAction.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a ScheduledAction.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ScheduledAction.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledAction.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ScheduledAction.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledAction.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledAction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduledAction.
        :type id: str

        :param scheduling_plan_id:
            The value to assign to the scheduling_plan_id property of this ScheduledAction.
        :type scheduling_plan_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduledAction.
        :type compartment_id: str

        :param scheduling_window_id:
            The value to assign to the scheduling_window_id property of this ScheduledAction.
        :type scheduling_window_id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledAction.
        :type display_name: str

        :param action_order:
            The value to assign to the action_order property of this ScheduledAction.
        :type action_order: int

        :param action_type:
            The value to assign to the action_type property of this ScheduledAction.
            Allowed values for this property are: "DB_SERVER_FULL_SOFTWARE_UPDATE", "STORAGE_SERVER_FULL_SOFTWARE_UPDATE", "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledAction.
            Allowed values for this property are: "CREATING", "NEEDS_ATTENTION", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param estimated_time_in_mins:
            The value to assign to the estimated_time_in_mins property of this ScheduledAction.
        :type estimated_time_in_mins: int

        :param action_params:
            The value to assign to the action_params property of this ScheduledAction.
        :type action_params: dict(str, str)

        :param action_members:
            The value to assign to the action_members property of this ScheduledAction.
        :type action_members: list[oci.database.models.ActionMember]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduledAction.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduledAction.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ScheduledAction.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this ScheduledAction.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ScheduledAction.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'scheduling_plan_id': 'str',
            'compartment_id': 'str',
            'scheduling_window_id': 'str',
            'display_name': 'str',
            'action_order': 'int',
            'action_type': 'str',
            'lifecycle_state': 'str',
            'estimated_time_in_mins': 'int',
            'action_params': 'dict(str, str)',
            'action_members': 'list[ActionMember]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'scheduling_plan_id': 'schedulingPlanId',
            'compartment_id': 'compartmentId',
            'scheduling_window_id': 'schedulingWindowId',
            'display_name': 'displayName',
            'action_order': 'actionOrder',
            'action_type': 'actionType',
            'lifecycle_state': 'lifecycleState',
            'estimated_time_in_mins': 'estimatedTimeInMins',
            'action_params': 'actionParams',
            'action_members': 'actionMembers',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._scheduling_plan_id = None
        self._compartment_id = None
        self._scheduling_window_id = None
        self._display_name = None
        self._action_order = None
        self._action_type = None
        self._lifecycle_state = None
        self._estimated_time_in_mins = None
        self._action_params = None
        self._action_members = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledAction.
        The `OCID`__ of the Scheduled Action.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ScheduledAction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledAction.
        The `OCID`__ of the Scheduled Action.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ScheduledAction.
        :type: str
        """
        self._id = id

    @property
    def scheduling_plan_id(self):
        """
        **[Required]** Gets the scheduling_plan_id of this ScheduledAction.
        The `OCID`__ of the Scheduling Plan.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scheduling_plan_id of this ScheduledAction.
        :rtype: str
        """
        return self._scheduling_plan_id

    @scheduling_plan_id.setter
    def scheduling_plan_id(self, scheduling_plan_id):
        """
        Sets the scheduling_plan_id of this ScheduledAction.
        The `OCID`__ of the Scheduling Plan.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scheduling_plan_id: The scheduling_plan_id of this ScheduledAction.
        :type: str
        """
        self._scheduling_plan_id = scheduling_plan_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ScheduledAction.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ScheduledAction.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduledAction.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ScheduledAction.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def scheduling_window_id(self):
        """
        Gets the scheduling_window_id of this ScheduledAction.
        The `OCID`__ of the Scheduling Window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scheduling_window_id of this ScheduledAction.
        :rtype: str
        """
        return self._scheduling_window_id

    @scheduling_window_id.setter
    def scheduling_window_id(self, scheduling_window_id):
        """
        Sets the scheduling_window_id of this ScheduledAction.
        The `OCID`__ of the Scheduling Window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scheduling_window_id: The scheduling_window_id of this ScheduledAction.
        :type: str
        """
        self._scheduling_window_id = scheduling_window_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduledAction.
        The display name of the Scheduled Action.


        :return: The display_name of this ScheduledAction.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduledAction.
        The display name of the Scheduled Action.


        :param display_name: The display_name of this ScheduledAction.
        :type: str
        """
        self._display_name = display_name

    @property
    def action_order(self):
        """
        **[Required]** Gets the action_order of this ScheduledAction.
        The order of the scheduled action.


        :return: The action_order of this ScheduledAction.
        :rtype: int
        """
        return self._action_order

    @action_order.setter
    def action_order(self, action_order):
        """
        Sets the action_order of this ScheduledAction.
        The order of the scheduled action.


        :param action_order: The action_order of this ScheduledAction.
        :type: int
        """
        self._action_order = action_order

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this ScheduledAction.
        The type of the scheduled action being performed

        Allowed values for this property are: "DB_SERVER_FULL_SOFTWARE_UPDATE", "STORAGE_SERVER_FULL_SOFTWARE_UPDATE", "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_type of this ScheduledAction.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this ScheduledAction.
        The type of the scheduled action being performed


        :param action_type: The action_type of this ScheduledAction.
        :type: str
        """
        allowed_values = ["DB_SERVER_FULL_SOFTWARE_UPDATE", "STORAGE_SERVER_FULL_SOFTWARE_UPDATE", "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            action_type = 'UNKNOWN_ENUM_VALUE'
        self._action_type = action_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduledAction.
        The current state of the Scheduled Action. Valid states are CREATING, NEEDS_ATTENTION, AVAILABLE, UPDATING, FAILED, DELETING and DELETED.

        Allowed values for this property are: "CREATING", "NEEDS_ATTENTION", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ScheduledAction.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledAction.
        The current state of the Scheduled Action. Valid states are CREATING, NEEDS_ATTENTION, AVAILABLE, UPDATING, FAILED, DELETING and DELETED.


        :param lifecycle_state: The lifecycle_state of this ScheduledAction.
        :type: str
        """
        allowed_values = ["CREATING", "NEEDS_ATTENTION", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def estimated_time_in_mins(self):
        """
        Gets the estimated_time_in_mins of this ScheduledAction.
        The estimated patching time for the scheduled action.


        :return: The estimated_time_in_mins of this ScheduledAction.
        :rtype: int
        """
        return self._estimated_time_in_mins

    @estimated_time_in_mins.setter
    def estimated_time_in_mins(self, estimated_time_in_mins):
        """
        Sets the estimated_time_in_mins of this ScheduledAction.
        The estimated patching time for the scheduled action.


        :param estimated_time_in_mins: The estimated_time_in_mins of this ScheduledAction.
        :type: int
        """
        self._estimated_time_in_mins = estimated_time_in_mins

    @property
    def action_params(self):
        """
        Gets the action_params of this ScheduledAction.
        Map<ParamName, ParamValue> where a key value pair describes the specific action parameter.
        Example: `{\"count\": \"3\"}`


        :return: The action_params of this ScheduledAction.
        :rtype: dict(str, str)
        """
        return self._action_params

    @action_params.setter
    def action_params(self, action_params):
        """
        Sets the action_params of this ScheduledAction.
        Map<ParamName, ParamValue> where a key value pair describes the specific action parameter.
        Example: `{\"count\": \"3\"}`


        :param action_params: The action_params of this ScheduledAction.
        :type: dict(str, str)
        """
        self._action_params = action_params

    @property
    def action_members(self):
        """
        Gets the action_members of this ScheduledAction.
        The list of action members in a scheduled action.


        :return: The action_members of this ScheduledAction.
        :rtype: list[oci.database.models.ActionMember]
        """
        return self._action_members

    @action_members.setter
    def action_members(self, action_members):
        """
        Sets the action_members of this ScheduledAction.
        The list of action members in a scheduled action.


        :param action_members: The action_members of this ScheduledAction.
        :type: list[oci.database.models.ActionMember]
        """
        self._action_members = action_members

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduledAction.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ScheduledAction.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduledAction.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ScheduledAction.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduledAction.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ScheduledAction.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduledAction.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ScheduledAction.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ScheduledAction.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ScheduledAction.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ScheduledAction.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ScheduledAction.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ScheduledAction.
        The date and time the Scheduled Action Resource was created.


        :return: The time_created of this ScheduledAction.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ScheduledAction.
        The date and time the Scheduled Action Resource was created.


        :param time_created: The time_created of this ScheduledAction.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ScheduledAction.
        The date and time the Scheduled Action Resource was updated.


        :return: The time_updated of this ScheduledAction.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ScheduledAction.
        The date and time the Scheduled Action Resource was updated.


        :param time_updated: The time_updated of this ScheduledAction.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
