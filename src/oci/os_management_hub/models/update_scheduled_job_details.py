# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScheduledJobDetails(object):
    """
    Information for updating a scheduled job.
    """

    #: A constant which can be used with the schedule_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "ONETIME"
    SCHEDULE_TYPE_ONETIME = "ONETIME"

    #: A constant which can be used with the schedule_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "RECURRING"
    SCHEDULE_TYPE_RECURRING = "RECURRING"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScheduledJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateScheduledJobDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateScheduledJobDetails.
        :type description: str

        :param schedule_type:
            The value to assign to the schedule_type property of this UpdateScheduledJobDetails.
            Allowed values for this property are: "ONETIME", "RECURRING"
        :type schedule_type: str

        :param time_next_execution:
            The value to assign to the time_next_execution property of this UpdateScheduledJobDetails.
        :type time_next_execution: datetime

        :param recurring_rule:
            The value to assign to the recurring_rule property of this UpdateScheduledJobDetails.
        :type recurring_rule: str

        :param operations:
            The value to assign to the operations property of this UpdateScheduledJobDetails.
        :type operations: list[oci.os_management_hub.models.ScheduledJobOperation]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateScheduledJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateScheduledJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'schedule_type': 'str',
            'time_next_execution': 'datetime',
            'recurring_rule': 'str',
            'operations': 'list[ScheduledJobOperation]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'schedule_type': 'scheduleType',
            'time_next_execution': 'timeNextExecution',
            'recurring_rule': 'recurringRule',
            'operations': 'operations',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._schedule_type = None
        self._time_next_execution = None
        self._recurring_rule = None
        self._operations = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateScheduledJobDetails.
        Scheduled job name.


        :return: The display_name of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateScheduledJobDetails.
        Scheduled job name.


        :param display_name: The display_name of this UpdateScheduledJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateScheduledJobDetails.
        Details describing the scheduled job.


        :return: The description of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateScheduledJobDetails.
        Details describing the scheduled job.


        :param description: The description of this UpdateScheduledJobDetails.
        :type: str
        """
        self._description = description

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this UpdateScheduledJobDetails.
        The type of scheduling this scheduled job follows.

        Allowed values for this property are: "ONETIME", "RECURRING"


        :return: The schedule_type of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this UpdateScheduledJobDetails.
        The type of scheduling this scheduled job follows.


        :param schedule_type: The schedule_type of this UpdateScheduledJobDetails.
        :type: str
        """
        allowed_values = ["ONETIME", "RECURRING"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            raise ValueError(
                "Invalid value for `schedule_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._schedule_type = schedule_type

    @property
    def time_next_execution(self):
        """
        Gets the time_next_execution of this UpdateScheduledJobDetails.
        The desired time for the next execution of this scheduled job.


        :return: The time_next_execution of this UpdateScheduledJobDetails.
        :rtype: datetime
        """
        return self._time_next_execution

    @time_next_execution.setter
    def time_next_execution(self, time_next_execution):
        """
        Sets the time_next_execution of this UpdateScheduledJobDetails.
        The desired time for the next execution of this scheduled job.


        :param time_next_execution: The time_next_execution of this UpdateScheduledJobDetails.
        :type: datetime
        """
        self._time_next_execution = time_next_execution

    @property
    def recurring_rule(self):
        """
        Gets the recurring_rule of this UpdateScheduledJobDetails.
        The recurring rule for a recurring scheduled job.


        :return: The recurring_rule of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._recurring_rule

    @recurring_rule.setter
    def recurring_rule(self, recurring_rule):
        """
        Sets the recurring_rule of this UpdateScheduledJobDetails.
        The recurring rule for a recurring scheduled job.


        :param recurring_rule: The recurring_rule of this UpdateScheduledJobDetails.
        :type: str
        """
        self._recurring_rule = recurring_rule

    @property
    def operations(self):
        """
        Gets the operations of this UpdateScheduledJobDetails.
        The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).


        :return: The operations of this UpdateScheduledJobDetails.
        :rtype: list[oci.os_management_hub.models.ScheduledJobOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this UpdateScheduledJobDetails.
        The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).


        :param operations: The operations of this UpdateScheduledJobDetails.
        :type: list[oci.os_management_hub.models.ScheduledJobOperation]
        """
        self._operations = operations

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateScheduledJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateScheduledJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateScheduledJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateScheduledJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateScheduledJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateScheduledJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateScheduledJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateScheduledJobDetails.
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
