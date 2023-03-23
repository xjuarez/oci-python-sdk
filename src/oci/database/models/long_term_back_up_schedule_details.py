# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LongTermBackUpScheduleDetails(object):
    """
    Details for the long-term backup schedule.
    """

    #: A constant which can be used with the repeat_cadence property of a LongTermBackUpScheduleDetails.
    #: This constant has a value of "ONE_TIME"
    REPEAT_CADENCE_ONE_TIME = "ONE_TIME"

    #: A constant which can be used with the repeat_cadence property of a LongTermBackUpScheduleDetails.
    #: This constant has a value of "WEEKLY"
    REPEAT_CADENCE_WEEKLY = "WEEKLY"

    #: A constant which can be used with the repeat_cadence property of a LongTermBackUpScheduleDetails.
    #: This constant has a value of "MONTHLY"
    REPEAT_CADENCE_MONTHLY = "MONTHLY"

    #: A constant which can be used with the repeat_cadence property of a LongTermBackUpScheduleDetails.
    #: This constant has a value of "YEARLY"
    REPEAT_CADENCE_YEARLY = "YEARLY"

    def __init__(self, **kwargs):
        """
        Initializes a new LongTermBackUpScheduleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param repeat_cadence:
            The value to assign to the repeat_cadence property of this LongTermBackUpScheduleDetails.
            Allowed values for this property are: "ONE_TIME", "WEEKLY", "MONTHLY", "YEARLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type repeat_cadence: str

        :param time_of_backup:
            The value to assign to the time_of_backup property of this LongTermBackUpScheduleDetails.
        :type time_of_backup: datetime

        :param retention_period_in_days:
            The value to assign to the retention_period_in_days property of this LongTermBackUpScheduleDetails.
        :type retention_period_in_days: int

        :param is_disabled:
            The value to assign to the is_disabled property of this LongTermBackUpScheduleDetails.
        :type is_disabled: bool

        """
        self.swagger_types = {
            'repeat_cadence': 'str',
            'time_of_backup': 'datetime',
            'retention_period_in_days': 'int',
            'is_disabled': 'bool'
        }

        self.attribute_map = {
            'repeat_cadence': 'repeatCadence',
            'time_of_backup': 'timeOfBackup',
            'retention_period_in_days': 'retentionPeriodInDays',
            'is_disabled': 'isDisabled'
        }

        self._repeat_cadence = None
        self._time_of_backup = None
        self._retention_period_in_days = None
        self._is_disabled = None

    @property
    def repeat_cadence(self):
        """
        Gets the repeat_cadence of this LongTermBackUpScheduleDetails.
        The frequency of the long-term backup schedule

        Allowed values for this property are: "ONE_TIME", "WEEKLY", "MONTHLY", "YEARLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The repeat_cadence of this LongTermBackUpScheduleDetails.
        :rtype: str
        """
        return self._repeat_cadence

    @repeat_cadence.setter
    def repeat_cadence(self, repeat_cadence):
        """
        Sets the repeat_cadence of this LongTermBackUpScheduleDetails.
        The frequency of the long-term backup schedule


        :param repeat_cadence: The repeat_cadence of this LongTermBackUpScheduleDetails.
        :type: str
        """
        allowed_values = ["ONE_TIME", "WEEKLY", "MONTHLY", "YEARLY"]
        if not value_allowed_none_or_none_sentinel(repeat_cadence, allowed_values):
            repeat_cadence = 'UNKNOWN_ENUM_VALUE'
        self._repeat_cadence = repeat_cadence

    @property
    def time_of_backup(self):
        """
        Gets the time_of_backup of this LongTermBackUpScheduleDetails.
        The timestamp for the long-term backup schedule. For a MONTHLY cadence, months having fewer days than the provided date will have the backup taken on the last day of that month.


        :return: The time_of_backup of this LongTermBackUpScheduleDetails.
        :rtype: datetime
        """
        return self._time_of_backup

    @time_of_backup.setter
    def time_of_backup(self, time_of_backup):
        """
        Sets the time_of_backup of this LongTermBackUpScheduleDetails.
        The timestamp for the long-term backup schedule. For a MONTHLY cadence, months having fewer days than the provided date will have the backup taken on the last day of that month.


        :param time_of_backup: The time_of_backup of this LongTermBackUpScheduleDetails.
        :type: datetime
        """
        self._time_of_backup = time_of_backup

    @property
    def retention_period_in_days(self):
        """
        Gets the retention_period_in_days of this LongTermBackUpScheduleDetails.
        Retention period, in days, for long-term backups


        :return: The retention_period_in_days of this LongTermBackUpScheduleDetails.
        :rtype: int
        """
        return self._retention_period_in_days

    @retention_period_in_days.setter
    def retention_period_in_days(self, retention_period_in_days):
        """
        Sets the retention_period_in_days of this LongTermBackUpScheduleDetails.
        Retention period, in days, for long-term backups


        :param retention_period_in_days: The retention_period_in_days of this LongTermBackUpScheduleDetails.
        :type: int
        """
        self._retention_period_in_days = retention_period_in_days

    @property
    def is_disabled(self):
        """
        Gets the is_disabled of this LongTermBackUpScheduleDetails.
        Indicates if the long-term backup schedule should be deleted. The default value is `FALSE`.


        :return: The is_disabled of this LongTermBackUpScheduleDetails.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """
        Sets the is_disabled of this LongTermBackUpScheduleDetails.
        Indicates if the long-term backup schedule should be deleted. The default value is `FALSE`.


        :param is_disabled: The is_disabled of this LongTermBackUpScheduleDetails.
        :type: bool
        """
        self._is_disabled = is_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
