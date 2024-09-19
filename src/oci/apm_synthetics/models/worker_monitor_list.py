# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkerMonitorList(object):
    """
    Details of the monitor assigned to an On-premise vantage point worker.
    """

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "SCRIPTED_BROWSER"
    MONITOR_TYPE_SCRIPTED_BROWSER = "SCRIPTED_BROWSER"

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "BROWSER"
    MONITOR_TYPE_BROWSER = "BROWSER"

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "SCRIPTED_REST"
    MONITOR_TYPE_SCRIPTED_REST = "SCRIPTED_REST"

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "REST"
    MONITOR_TYPE_REST = "REST"

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "NETWORK"
    MONITOR_TYPE_NETWORK = "NETWORK"

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "DNS"
    MONITOR_TYPE_DNS = "DNS"

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "FTP"
    MONITOR_TYPE_FTP = "FTP"

    #: A constant which can be used with the monitor_type property of a WorkerMonitorList.
    #: This constant has a value of "SQL"
    MONITOR_TYPE_SQL = "SQL"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkerMonitorList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkerMonitorList.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this WorkerMonitorList.
        :type display_name: str

        :param monitor_type:
            The value to assign to the monitor_type property of this WorkerMonitorList.
            Allowed values for this property are: "SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST", "NETWORK", "DNS", "FTP", "SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type monitor_type: str

        :param is_run_now:
            The value to assign to the is_run_now property of this WorkerMonitorList.
        :type is_run_now: bool

        :param time_assigned:
            The value to assign to the time_assigned property of this WorkerMonitorList.
        :type time_assigned: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'monitor_type': 'str',
            'is_run_now': 'bool',
            'time_assigned': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'monitor_type': 'monitorType',
            'is_run_now': 'isRunNow',
            'time_assigned': 'timeAssigned'
        }

        self._id = None
        self._display_name = None
        self._monitor_type = None
        self._is_run_now = None
        self._time_assigned = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkerMonitorList.
        The `OCID`__ of the monitor.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this WorkerMonitorList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkerMonitorList.
        The `OCID`__ of the monitor.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this WorkerMonitorList.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this WorkerMonitorList.
        Unique name that can be edited. The name should not contain any confidential information.


        :return: The display_name of this WorkerMonitorList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WorkerMonitorList.
        Unique name that can be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this WorkerMonitorList.
        :type: str
        """
        self._display_name = display_name

    @property
    def monitor_type(self):
        """
        **[Required]** Gets the monitor_type of this WorkerMonitorList.
        Type of monitor.

        Allowed values for this property are: "SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST", "NETWORK", "DNS", "FTP", "SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The monitor_type of this WorkerMonitorList.
        :rtype: str
        """
        return self._monitor_type

    @monitor_type.setter
    def monitor_type(self, monitor_type):
        """
        Sets the monitor_type of this WorkerMonitorList.
        Type of monitor.


        :param monitor_type: The monitor_type of this WorkerMonitorList.
        :type: str
        """
        allowed_values = ["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST", "NETWORK", "DNS", "FTP", "SQL"]
        if not value_allowed_none_or_none_sentinel(monitor_type, allowed_values):
            monitor_type = 'UNKNOWN_ENUM_VALUE'
        self._monitor_type = monitor_type

    @property
    def is_run_now(self):
        """
        Gets the is_run_now of this WorkerMonitorList.
        If isRunNow is enabled, then the monitor will run immediately.


        :return: The is_run_now of this WorkerMonitorList.
        :rtype: bool
        """
        return self._is_run_now

    @is_run_now.setter
    def is_run_now(self, is_run_now):
        """
        Sets the is_run_now of this WorkerMonitorList.
        If isRunNow is enabled, then the monitor will run immediately.


        :param is_run_now: The is_run_now of this WorkerMonitorList.
        :type: bool
        """
        self._is_run_now = is_run_now

    @property
    def time_assigned(self):
        """
        Gets the time_assigned of this WorkerMonitorList.
        The time the resource was last assigned to an On-premise vantage point worker, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_assigned of this WorkerMonitorList.
        :rtype: datetime
        """
        return self._time_assigned

    @time_assigned.setter
    def time_assigned(self, time_assigned):
        """
        Sets the time_assigned of this WorkerMonitorList.
        The time the resource was last assigned to an On-premise vantage point worker, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_assigned: The time_assigned of this WorkerMonitorList.
        :type: datetime
        """
        self._time_assigned = time_assigned

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
