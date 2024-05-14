# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpenAlertSummary(object):
    """
    An alert from the Exadata storage server.
    """

    #: A constant which can be used with the severity property of a OpenAlertSummary.
    #: This constant has a value of "CLEAR"
    SEVERITY_CLEAR = "CLEAR"

    #: A constant which can be used with the severity property of a OpenAlertSummary.
    #: This constant has a value of "INFO"
    SEVERITY_INFO = "INFO"

    #: A constant which can be used with the severity property of a OpenAlertSummary.
    #: This constant has a value of "WARNING"
    SEVERITY_WARNING = "WARNING"

    #: A constant which can be used with the severity property of a OpenAlertSummary.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the type property of a OpenAlertSummary.
    #: This constant has a value of "STATEFUL"
    TYPE_STATEFUL = "STATEFUL"

    #: A constant which can be used with the type property of a OpenAlertSummary.
    #: This constant has a value of "STATELESS"
    TYPE_STATELESS = "STATELESS"

    def __init__(self, **kwargs):
        """
        Initializes a new OpenAlertSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param severity:
            The value to assign to the severity property of this OpenAlertSummary.
            Allowed values for this property are: "CLEAR", "INFO", "WARNING", "CRITICAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param type:
            The value to assign to the type property of this OpenAlertSummary.
            Allowed values for this property are: "STATEFUL", "STATELESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param time_start_at:
            The value to assign to the time_start_at property of this OpenAlertSummary.
        :type time_start_at: datetime

        :param message:
            The value to assign to the message property of this OpenAlertSummary.
        :type message: str

        """
        self.swagger_types = {
            'severity': 'str',
            'type': 'str',
            'time_start_at': 'datetime',
            'message': 'str'
        }

        self.attribute_map = {
            'severity': 'severity',
            'type': 'type',
            'time_start_at': 'timeStartAt',
            'message': 'message'
        }

        self._severity = None
        self._type = None
        self._time_start_at = None
        self._message = None

    @property
    def severity(self):
        """
        Gets the severity of this OpenAlertSummary.
        The severity of the alert.

        Allowed values for this property are: "CLEAR", "INFO", "WARNING", "CRITICAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this OpenAlertSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this OpenAlertSummary.
        The severity of the alert.


        :param severity: The severity of this OpenAlertSummary.
        :type: str
        """
        allowed_values = ["CLEAR", "INFO", "WARNING", "CRITICAL"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def type(self):
        """
        Gets the type of this OpenAlertSummary.
        The type of alert.

        Allowed values for this property are: "STATEFUL", "STATELESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this OpenAlertSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this OpenAlertSummary.
        The type of alert.


        :param type: The type of this OpenAlertSummary.
        :type: str
        """
        allowed_values = ["STATEFUL", "STATELESS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def time_start_at(self):
        """
        Gets the time_start_at of this OpenAlertSummary.
        The start time of the alert.


        :return: The time_start_at of this OpenAlertSummary.
        :rtype: datetime
        """
        return self._time_start_at

    @time_start_at.setter
    def time_start_at(self, time_start_at):
        """
        Sets the time_start_at of this OpenAlertSummary.
        The start time of the alert.


        :param time_start_at: The time_start_at of this OpenAlertSummary.
        :type: datetime
        """
        self._time_start_at = time_start_at

    @property
    def message(self):
        """
        Gets the message of this OpenAlertSummary.
        The alert message.


        :return: The message of this OpenAlertSummary.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this OpenAlertSummary.
        The alert message.


        :param message: The message of this OpenAlertSummary.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
