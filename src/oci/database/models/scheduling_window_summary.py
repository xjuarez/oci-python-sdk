# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchedulingWindowSummary(object):
    """
    Details of a Scheduling Window.
    """

    #: A constant which can be used with the lifecycle_state property of a SchedulingWindowSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SchedulingWindowSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a SchedulingWindowSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SchedulingWindowSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SchedulingWindowSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SchedulingWindowSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new SchedulingWindowSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SchedulingWindowSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SchedulingWindowSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SchedulingWindowSummary.
        :type display_name: str

        :param time_next_scheduling_window_starts:
            The value to assign to the time_next_scheduling_window_starts property of this SchedulingWindowSummary.
        :type time_next_scheduling_window_starts: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SchedulingWindowSummary.
            Allowed values for this property are: "CREATING", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SchedulingWindowSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this SchedulingWindowSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SchedulingWindowSummary.
        :type time_updated: datetime

        :param window_preference:
            The value to assign to the window_preference property of this SchedulingWindowSummary.
        :type window_preference: oci.database.models.WindowPreferenceDetail

        :param scheduling_policy_id:
            The value to assign to the scheduling_policy_id property of this SchedulingWindowSummary.
        :type scheduling_policy_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SchedulingWindowSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SchedulingWindowSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_next_scheduling_window_starts': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'window_preference': 'WindowPreferenceDetail',
            'scheduling_policy_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_next_scheduling_window_starts': 'timeNextSchedulingWindowStarts',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'window_preference': 'windowPreference',
            'scheduling_policy_id': 'schedulingPolicyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_next_scheduling_window_starts = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._window_preference = None
        self._scheduling_policy_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SchedulingWindowSummary.
        The `OCID`__ of the Scheduling Window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this SchedulingWindowSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SchedulingWindowSummary.
        The `OCID`__ of the Scheduling Window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this SchedulingWindowSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this SchedulingWindowSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this SchedulingWindowSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SchedulingWindowSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this SchedulingWindowSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this SchedulingWindowSummary.
        The user-friendly name for the Scheduling Window. The name does not need to be unique.


        :return: The display_name of this SchedulingWindowSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SchedulingWindowSummary.
        The user-friendly name for the Scheduling Window. The name does not need to be unique.


        :param display_name: The display_name of this SchedulingWindowSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_next_scheduling_window_starts(self):
        """
        Gets the time_next_scheduling_window_starts of this SchedulingWindowSummary.
        The date and time of the next upcoming window associated within the schedulingWindow is planned to start.


        :return: The time_next_scheduling_window_starts of this SchedulingWindowSummary.
        :rtype: datetime
        """
        return self._time_next_scheduling_window_starts

    @time_next_scheduling_window_starts.setter
    def time_next_scheduling_window_starts(self, time_next_scheduling_window_starts):
        """
        Sets the time_next_scheduling_window_starts of this SchedulingWindowSummary.
        The date and time of the next upcoming window associated within the schedulingWindow is planned to start.


        :param time_next_scheduling_window_starts: The time_next_scheduling_window_starts of this SchedulingWindowSummary.
        :type: datetime
        """
        self._time_next_scheduling_window_starts = time_next_scheduling_window_starts

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SchedulingWindowSummary.
        The current state of the Scheduling Window. Valid states are CREATING, ACTIVE, UPDATING, FAILED, DELETING and DELETED.

        Allowed values for this property are: "CREATING", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SchedulingWindowSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SchedulingWindowSummary.
        The current state of the Scheduling Window. Valid states are CREATING, ACTIVE, UPDATING, FAILED, DELETING and DELETED.


        :param lifecycle_state: The lifecycle_state of this SchedulingWindowSummary.
        :type: str
        """
        allowed_values = ["CREATING", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SchedulingWindowSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this SchedulingWindowSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SchedulingWindowSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this SchedulingWindowSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        Gets the time_created of this SchedulingWindowSummary.
        The date and time the Scheduling Window was created.


        :return: The time_created of this SchedulingWindowSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SchedulingWindowSummary.
        The date and time the Scheduling Window was created.


        :param time_created: The time_created of this SchedulingWindowSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SchedulingWindowSummary.
        The last date and time that the Scheduling Window was updated.


        :return: The time_updated of this SchedulingWindowSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SchedulingWindowSummary.
        The last date and time that the Scheduling Window was updated.


        :param time_updated: The time_updated of this SchedulingWindowSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def window_preference(self):
        """
        **[Required]** Gets the window_preference of this SchedulingWindowSummary.

        :return: The window_preference of this SchedulingWindowSummary.
        :rtype: oci.database.models.WindowPreferenceDetail
        """
        return self._window_preference

    @window_preference.setter
    def window_preference(self, window_preference):
        """
        Sets the window_preference of this SchedulingWindowSummary.

        :param window_preference: The window_preference of this SchedulingWindowSummary.
        :type: oci.database.models.WindowPreferenceDetail
        """
        self._window_preference = window_preference

    @property
    def scheduling_policy_id(self):
        """
        **[Required]** Gets the scheduling_policy_id of this SchedulingWindowSummary.
        The `OCID`__ of the Scheduling Policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scheduling_policy_id of this SchedulingWindowSummary.
        :rtype: str
        """
        return self._scheduling_policy_id

    @scheduling_policy_id.setter
    def scheduling_policy_id(self, scheduling_policy_id):
        """
        Sets the scheduling_policy_id of this SchedulingWindowSummary.
        The `OCID`__ of the Scheduling Policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scheduling_policy_id: The scheduling_policy_id of this SchedulingWindowSummary.
        :type: str
        """
        self._scheduling_policy_id = scheduling_policy_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SchedulingWindowSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SchedulingWindowSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SchedulingWindowSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SchedulingWindowSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SchedulingWindowSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SchedulingWindowSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SchedulingWindowSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SchedulingWindowSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
