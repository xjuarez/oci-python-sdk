# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserSummary(object):
    """
    The summary of a specific User.
    """

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "OPEN"
    STATUS_OPEN = "OPEN"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED"
    STATUS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_GRACE"
    STATUS_EXPIRED_GRACE = "EXPIRED_GRACE"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "LOCKED"
    STATUS_LOCKED = "LOCKED"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "LOCKED_TIMED"
    STATUS_LOCKED_TIMED = "LOCKED_TIMED"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_AND_LOCKED"
    STATUS_EXPIRED_AND_LOCKED = "EXPIRED_AND_LOCKED"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_GRACE_AND_LOCKED"
    STATUS_EXPIRED_GRACE_AND_LOCKED = "EXPIRED_GRACE_AND_LOCKED"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_AND_LOCKED_TIMED"
    STATUS_EXPIRED_AND_LOCKED_TIMED = "EXPIRED_AND_LOCKED_TIMED"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_GRACE_AND_LOCKED_TIMED"
    STATUS_EXPIRED_GRACE_AND_LOCKED_TIMED = "EXPIRED_GRACE_AND_LOCKED_TIMED"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "OPEN_AND_IN_ROLLOVER"
    STATUS_OPEN_AND_IN_ROLLOVER = "OPEN_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_AND_IN_ROLLOVER"
    STATUS_EXPIRED_AND_IN_ROLLOVER = "EXPIRED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "LOCKED_AND_IN_ROLLOVER"
    STATUS_LOCKED_AND_IN_ROLLOVER = "LOCKED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER"
    STATUS_EXPIRED_AND_LOCKED_AND_IN_ROLLOVER = "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "LOCKED_TIMED_AND_IN_ROLLOVER"
    STATUS_LOCKED_TIMED_AND_IN_ROLLOVER = "LOCKED_TIMED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a UserSummary.
    #: This constant has a value of "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL"
    STATUS_EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL = "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL"

    def __init__(self, **kwargs):
        """
        Initializes a new UserSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UserSummary.
        :type name: str

        :param status:
            The value to assign to the status property of this UserSummary.
            Allowed values for this property are: "OPEN", "EXPIRED", "EXPIRED_GRACE", "LOCKED", "LOCKED_TIMED", "EXPIRED_AND_LOCKED", "EXPIRED_GRACE_AND_LOCKED", "EXPIRED_AND_LOCKED_TIMED", "EXPIRED_GRACE_AND_LOCKED_TIMED", "OPEN_AND_IN_ROLLOVER", "EXPIRED_AND_IN_ROLLOVER", "LOCKED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER", "LOCKED_TIMED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_expiring:
            The value to assign to the time_expiring property of this UserSummary.
        :type time_expiring: datetime

        :param default_tablespace:
            The value to assign to the default_tablespace property of this UserSummary.
        :type default_tablespace: str

        :param temp_tablespace:
            The value to assign to the temp_tablespace property of this UserSummary.
        :type temp_tablespace: str

        :param time_created:
            The value to assign to the time_created property of this UserSummary.
        :type time_created: datetime

        :param time_locked:
            The value to assign to the time_locked property of this UserSummary.
        :type time_locked: datetime

        :param profile:
            The value to assign to the profile property of this UserSummary.
        :type profile: str

        """
        self.swagger_types = {
            'name': 'str',
            'status': 'str',
            'time_expiring': 'datetime',
            'default_tablespace': 'str',
            'temp_tablespace': 'str',
            'time_created': 'datetime',
            'time_locked': 'datetime',
            'profile': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status',
            'time_expiring': 'timeExpiring',
            'default_tablespace': 'defaultTablespace',
            'temp_tablespace': 'tempTablespace',
            'time_created': 'timeCreated',
            'time_locked': 'timeLocked',
            'profile': 'profile'
        }

        self._name = None
        self._status = None
        self._time_expiring = None
        self._default_tablespace = None
        self._temp_tablespace = None
        self._time_created = None
        self._time_locked = None
        self._profile = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this UserSummary.
        The name of the User.


        :return: The name of this UserSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserSummary.
        The name of the User.


        :param name: The name of this UserSummary.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UserSummary.
        The status of the user account.

        Allowed values for this property are: "OPEN", "EXPIRED", "EXPIRED_GRACE", "LOCKED", "LOCKED_TIMED", "EXPIRED_AND_LOCKED", "EXPIRED_GRACE_AND_LOCKED", "EXPIRED_AND_LOCKED_TIMED", "EXPIRED_GRACE_AND_LOCKED_TIMED", "OPEN_AND_IN_ROLLOVER", "EXPIRED_AND_IN_ROLLOVER", "LOCKED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER", "LOCKED_TIMED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this UserSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserSummary.
        The status of the user account.


        :param status: The status of this UserSummary.
        :type: str
        """
        allowed_values = ["OPEN", "EXPIRED", "EXPIRED_GRACE", "LOCKED", "LOCKED_TIMED", "EXPIRED_AND_LOCKED", "EXPIRED_GRACE_AND_LOCKED", "EXPIRED_AND_LOCKED_TIMED", "EXPIRED_GRACE_AND_LOCKED_TIMED", "OPEN_AND_IN_ROLLOVER", "EXPIRED_AND_IN_ROLLOVER", "LOCKED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER", "LOCKED_TIMED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_expiring(self):
        """
        Gets the time_expiring of this UserSummary.
        The date and time of the expiration of the user account.


        :return: The time_expiring of this UserSummary.
        :rtype: datetime
        """
        return self._time_expiring

    @time_expiring.setter
    def time_expiring(self, time_expiring):
        """
        Sets the time_expiring of this UserSummary.
        The date and time of the expiration of the user account.


        :param time_expiring: The time_expiring of this UserSummary.
        :type: datetime
        """
        self._time_expiring = time_expiring

    @property
    def default_tablespace(self):
        """
        **[Required]** Gets the default_tablespace of this UserSummary.
        The default tablespace for data.


        :return: The default_tablespace of this UserSummary.
        :rtype: str
        """
        return self._default_tablespace

    @default_tablespace.setter
    def default_tablespace(self, default_tablespace):
        """
        Sets the default_tablespace of this UserSummary.
        The default tablespace for data.


        :param default_tablespace: The default_tablespace of this UserSummary.
        :type: str
        """
        self._default_tablespace = default_tablespace

    @property
    def temp_tablespace(self):
        """
        **[Required]** Gets the temp_tablespace of this UserSummary.
        The name of the default tablespace for temporary tables or the name of a tablespace group.


        :return: The temp_tablespace of this UserSummary.
        :rtype: str
        """
        return self._temp_tablespace

    @temp_tablespace.setter
    def temp_tablespace(self, temp_tablespace):
        """
        Sets the temp_tablespace of this UserSummary.
        The name of the default tablespace for temporary tables or the name of a tablespace group.


        :param temp_tablespace: The temp_tablespace of this UserSummary.
        :type: str
        """
        self._temp_tablespace = temp_tablespace

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this UserSummary.
        The date and time the user was created.


        :return: The time_created of this UserSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UserSummary.
        The date and time the user was created.


        :param time_created: The time_created of this UserSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_locked(self):
        """
        Gets the time_locked of this UserSummary.
        The date the account was locked, if the status of the account is LOCKED.


        :return: The time_locked of this UserSummary.
        :rtype: datetime
        """
        return self._time_locked

    @time_locked.setter
    def time_locked(self, time_locked):
        """
        Sets the time_locked of this UserSummary.
        The date the account was locked, if the status of the account is LOCKED.


        :param time_locked: The time_locked of this UserSummary.
        :type: datetime
        """
        self._time_locked = time_locked

    @property
    def profile(self):
        """
        **[Required]** Gets the profile of this UserSummary.
        The profile name of the user.


        :return: The profile of this UserSummary.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this UserSummary.
        The profile name of the user.


        :param profile: The profile of this UserSummary.
        :type: str
        """
        self._profile = profile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
