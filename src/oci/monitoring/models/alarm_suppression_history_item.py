# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmSuppressionHistoryItem(object):
    """
    A summary of properties for the specified alarm suppression history item.
    """

    #: A constant which can be used with the level property of a AlarmSuppressionHistoryItem.
    #: This constant has a value of "ALARM"
    LEVEL_ALARM = "ALARM"

    #: A constant which can be used with the level property of a AlarmSuppressionHistoryItem.
    #: This constant has a value of "DIMENSION"
    LEVEL_DIMENSION = "DIMENSION"

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmSuppressionHistoryItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param suppression_id:
            The value to assign to the suppression_id property of this AlarmSuppressionHistoryItem.
        :type suppression_id: str

        :param alarm_suppression_target:
            The value to assign to the alarm_suppression_target property of this AlarmSuppressionHistoryItem.
        :type alarm_suppression_target: oci.monitoring.models.AlarmSuppressionTarget

        :param level:
            The value to assign to the level property of this AlarmSuppressionHistoryItem.
            Allowed values for this property are: "ALARM", "DIMENSION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type level: str

        :param display_name:
            The value to assign to the display_name property of this AlarmSuppressionHistoryItem.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AlarmSuppressionHistoryItem.
        :type description: str

        :param dimensions:
            The value to assign to the dimensions property of this AlarmSuppressionHistoryItem.
        :type dimensions: dict(str, str)

        :param time_effective_from:
            The value to assign to the time_effective_from property of this AlarmSuppressionHistoryItem.
        :type time_effective_from: datetime

        :param time_effective_until:
            The value to assign to the time_effective_until property of this AlarmSuppressionHistoryItem.
        :type time_effective_until: datetime

        :param suppression_conditions:
            The value to assign to the suppression_conditions property of this AlarmSuppressionHistoryItem.
        :type suppression_conditions: list[oci.monitoring.models.SuppressionCondition]

        """
        self.swagger_types = {
            'suppression_id': 'str',
            'alarm_suppression_target': 'AlarmSuppressionTarget',
            'level': 'str',
            'display_name': 'str',
            'description': 'str',
            'dimensions': 'dict(str, str)',
            'time_effective_from': 'datetime',
            'time_effective_until': 'datetime',
            'suppression_conditions': 'list[SuppressionCondition]'
        }

        self.attribute_map = {
            'suppression_id': 'suppressionId',
            'alarm_suppression_target': 'alarmSuppressionTarget',
            'level': 'level',
            'display_name': 'displayName',
            'description': 'description',
            'dimensions': 'dimensions',
            'time_effective_from': 'timeEffectiveFrom',
            'time_effective_until': 'timeEffectiveUntil',
            'suppression_conditions': 'suppressionConditions'
        }

        self._suppression_id = None
        self._alarm_suppression_target = None
        self._level = None
        self._display_name = None
        self._description = None
        self._dimensions = None
        self._time_effective_from = None
        self._time_effective_until = None
        self._suppression_conditions = None

    @property
    def suppression_id(self):
        """
        **[Required]** Gets the suppression_id of this AlarmSuppressionHistoryItem.
        The `OCID`__ of the alarm suppression.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The suppression_id of this AlarmSuppressionHistoryItem.
        :rtype: str
        """
        return self._suppression_id

    @suppression_id.setter
    def suppression_id(self, suppression_id):
        """
        Sets the suppression_id of this AlarmSuppressionHistoryItem.
        The `OCID`__ of the alarm suppression.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param suppression_id: The suppression_id of this AlarmSuppressionHistoryItem.
        :type: str
        """
        self._suppression_id = suppression_id

    @property
    def alarm_suppression_target(self):
        """
        **[Required]** Gets the alarm_suppression_target of this AlarmSuppressionHistoryItem.

        :return: The alarm_suppression_target of this AlarmSuppressionHistoryItem.
        :rtype: oci.monitoring.models.AlarmSuppressionTarget
        """
        return self._alarm_suppression_target

    @alarm_suppression_target.setter
    def alarm_suppression_target(self, alarm_suppression_target):
        """
        Sets the alarm_suppression_target of this AlarmSuppressionHistoryItem.

        :param alarm_suppression_target: The alarm_suppression_target of this AlarmSuppressionHistoryItem.
        :type: oci.monitoring.models.AlarmSuppressionTarget
        """
        self._alarm_suppression_target = alarm_suppression_target

    @property
    def level(self):
        """
        **[Required]** Gets the level of this AlarmSuppressionHistoryItem.
        The level of this alarm suppression.
        `ALARM` indicates a suppression of the entire alarm, regardless of dimension.
        `DIMENSION` indicates a suppression configured for specified dimensions.

        Allowed values for this property are: "ALARM", "DIMENSION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The level of this AlarmSuppressionHistoryItem.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this AlarmSuppressionHistoryItem.
        The level of this alarm suppression.
        `ALARM` indicates a suppression of the entire alarm, regardless of dimension.
        `DIMENSION` indicates a suppression configured for specified dimensions.


        :param level: The level of this AlarmSuppressionHistoryItem.
        :type: str
        """
        allowed_values = ["ALARM", "DIMENSION"]
        if not value_allowed_none_or_none_sentinel(level, allowed_values):
            level = 'UNKNOWN_ENUM_VALUE'
        self._level = level

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AlarmSuppressionHistoryItem.
        A user-friendly name for the alarm suppression. It does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this AlarmSuppressionHistoryItem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AlarmSuppressionHistoryItem.
        A user-friendly name for the alarm suppression. It does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this AlarmSuppressionHistoryItem.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this AlarmSuppressionHistoryItem.
        Human-readable reason for this alarm suppression.
        It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Oracle recommends including tracking information for the event or associated work,
        such as a ticket number.

        Example: `Planned outage due to change IT-1234.`


        :return: The description of this AlarmSuppressionHistoryItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AlarmSuppressionHistoryItem.
        Human-readable reason for this alarm suppression.
        It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Oracle recommends including tracking information for the event or associated work,
        such as a ticket number.

        Example: `Planned outage due to change IT-1234.`


        :param description: The description of this AlarmSuppressionHistoryItem.
        :type: str
        """
        self._description = description

    @property
    def dimensions(self):
        """
        Gets the dimensions of this AlarmSuppressionHistoryItem.
        Configured dimension filter for suppressing alarm state entries that include the set of specified dimension key-value pairs.

        Example: `{\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"}`


        :return: The dimensions of this AlarmSuppressionHistoryItem.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this AlarmSuppressionHistoryItem.
        Configured dimension filter for suppressing alarm state entries that include the set of specified dimension key-value pairs.

        Example: `{\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"}`


        :param dimensions: The dimensions of this AlarmSuppressionHistoryItem.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    @property
    def time_effective_from(self):
        """
        **[Required]** Gets the time_effective_from of this AlarmSuppressionHistoryItem.
        The start date and time for the suppression actually starts, inclusive. Format defined by RFC3339.

        Example: `2023-02-01T01:02:29.600Z`


        :return: The time_effective_from of this AlarmSuppressionHistoryItem.
        :rtype: datetime
        """
        return self._time_effective_from

    @time_effective_from.setter
    def time_effective_from(self, time_effective_from):
        """
        Sets the time_effective_from of this AlarmSuppressionHistoryItem.
        The start date and time for the suppression actually starts, inclusive. Format defined by RFC3339.

        Example: `2023-02-01T01:02:29.600Z`


        :param time_effective_from: The time_effective_from of this AlarmSuppressionHistoryItem.
        :type: datetime
        """
        self._time_effective_from = time_effective_from

    @property
    def time_effective_until(self):
        """
        **[Required]** Gets the time_effective_until of this AlarmSuppressionHistoryItem.
        The end date and time for the suppression actually ends, inclusive. Format defined by RFC3339.

        Example: `2023-02-01T02:02:29.600Z`


        :return: The time_effective_until of this AlarmSuppressionHistoryItem.
        :rtype: datetime
        """
        return self._time_effective_until

    @time_effective_until.setter
    def time_effective_until(self, time_effective_until):
        """
        Sets the time_effective_until of this AlarmSuppressionHistoryItem.
        The end date and time for the suppression actually ends, inclusive. Format defined by RFC3339.

        Example: `2023-02-01T02:02:29.600Z`


        :param time_effective_until: The time_effective_until of this AlarmSuppressionHistoryItem.
        :type: datetime
        """
        self._time_effective_until = time_effective_until

    @property
    def suppression_conditions(self):
        """
        Gets the suppression_conditions of this AlarmSuppressionHistoryItem.
        Array of all preconditions for alarm suppression.
        Example: `[{
          conditionType: \"RECURRENCE\",
          suppressionRecurrence: \"FRQ=DAILY;BYHOUR=10\",
          suppressionDuration: \"PT1H\"
        }]`


        :return: The suppression_conditions of this AlarmSuppressionHistoryItem.
        :rtype: list[oci.monitoring.models.SuppressionCondition]
        """
        return self._suppression_conditions

    @suppression_conditions.setter
    def suppression_conditions(self, suppression_conditions):
        """
        Sets the suppression_conditions of this AlarmSuppressionHistoryItem.
        Array of all preconditions for alarm suppression.
        Example: `[{
          conditionType: \"RECURRENCE\",
          suppressionRecurrence: \"FRQ=DAILY;BYHOUR=10\",
          suppressionDuration: \"PT1H\"
        }]`


        :param suppression_conditions: The suppression_conditions of this AlarmSuppressionHistoryItem.
        :type: list[oci.monitoring.models.SuppressionCondition]
        """
        self._suppression_conditions = suppression_conditions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
