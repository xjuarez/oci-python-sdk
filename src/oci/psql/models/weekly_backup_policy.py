# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915

from .backup_policy import BackupPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WeeklyBackupPolicy(BackupPolicy):
    """
    Weekly backup policy.
    """

    #: A constant which can be used with the days_of_the_week property of a WeeklyBackupPolicy.
    #: This constant has a value of "SUNDAY"
    DAYS_OF_THE_WEEK_SUNDAY = "SUNDAY"

    #: A constant which can be used with the days_of_the_week property of a WeeklyBackupPolicy.
    #: This constant has a value of "MONDAY"
    DAYS_OF_THE_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the days_of_the_week property of a WeeklyBackupPolicy.
    #: This constant has a value of "TUESDAY"
    DAYS_OF_THE_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the days_of_the_week property of a WeeklyBackupPolicy.
    #: This constant has a value of "WEDNESDAY"
    DAYS_OF_THE_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the days_of_the_week property of a WeeklyBackupPolicy.
    #: This constant has a value of "THURSDAY"
    DAYS_OF_THE_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the days_of_the_week property of a WeeklyBackupPolicy.
    #: This constant has a value of "FRIDAY"
    DAYS_OF_THE_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the days_of_the_week property of a WeeklyBackupPolicy.
    #: This constant has a value of "SATURDAY"
    DAYS_OF_THE_WEEK_SATURDAY = "SATURDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new WeeklyBackupPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.psql.models.WeeklyBackupPolicy.kind` attribute
        of this class is ``WEEKLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this WeeklyBackupPolicy.
            Allowed values for this property are: "DAILY", "WEEKLY", "MONTHLY", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param retention_days:
            The value to assign to the retention_days property of this WeeklyBackupPolicy.
        :type retention_days: int

        :param copy_policy:
            The value to assign to the copy_policy property of this WeeklyBackupPolicy.
        :type copy_policy: oci.psql.models.BackupCopyPolicy

        :param days_of_the_week:
            The value to assign to the days_of_the_week property of this WeeklyBackupPolicy.
            Allowed values for items in this list are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type days_of_the_week: list[str]

        :param backup_start:
            The value to assign to the backup_start property of this WeeklyBackupPolicy.
        :type backup_start: str

        """
        self.swagger_types = {
            'kind': 'str',
            'retention_days': 'int',
            'copy_policy': 'BackupCopyPolicy',
            'days_of_the_week': 'list[str]',
            'backup_start': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'retention_days': 'retentionDays',
            'copy_policy': 'copyPolicy',
            'days_of_the_week': 'daysOfTheWeek',
            'backup_start': 'backupStart'
        }

        self._kind = None
        self._retention_days = None
        self._copy_policy = None
        self._days_of_the_week = None
        self._backup_start = None
        self._kind = 'WEEKLY'

    @property
    def days_of_the_week(self):
        """
        **[Required]** Gets the days_of_the_week of this WeeklyBackupPolicy.
        The day of the week that the backup starts.

        Allowed values for items in this list are: "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The days_of_the_week of this WeeklyBackupPolicy.
        :rtype: list[str]
        """
        return self._days_of_the_week

    @days_of_the_week.setter
    def days_of_the_week(self, days_of_the_week):
        """
        Sets the days_of_the_week of this WeeklyBackupPolicy.
        The day of the week that the backup starts.


        :param days_of_the_week: The days_of_the_week of this WeeklyBackupPolicy.
        :type: list[str]
        """
        allowed_values = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        if days_of_the_week:
            days_of_the_week[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in days_of_the_week]
        self._days_of_the_week = days_of_the_week

    @property
    def backup_start(self):
        """
        **[Required]** Gets the backup_start of this WeeklyBackupPolicy.
        Hour of the day when the backup starts.


        :return: The backup_start of this WeeklyBackupPolicy.
        :rtype: str
        """
        return self._backup_start

    @backup_start.setter
    def backup_start(self, backup_start):
        """
        Sets the backup_start of this WeeklyBackupPolicy.
        Hour of the day when the backup starts.


        :param backup_start: The backup_start of this WeeklyBackupPolicy.
        :type: str
        """
        self._backup_start = backup_start

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
