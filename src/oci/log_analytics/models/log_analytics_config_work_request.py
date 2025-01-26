# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsConfigWorkRequest(object):
    """
    LogAnalyticsConfigWorkRequest
    """

    #: A constant which can be used with the operation_type property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "CREATE_ASSOCIATIONS"
    OPERATION_TYPE_CREATE_ASSOCIATIONS = "CREATE_ASSOCIATIONS"

    #: A constant which can be used with the operation_type property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "DELETE_ASSOCIATIONS"
    OPERATION_TYPE_DELETE_ASSOCIATIONS = "DELETE_ASSOCIATIONS"

    #: A constant which can be used with the operation_type property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "APPEND_LOOKUP_DATA"
    OPERATION_TYPE_APPEND_LOOKUP_DATA = "APPEND_LOOKUP_DATA"

    #: A constant which can be used with the operation_type property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "UPDATE_LOOKUP_DATA"
    OPERATION_TYPE_UPDATE_LOOKUP_DATA = "UPDATE_LOOKUP_DATA"

    #: A constant which can be used with the operation_type property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "DELETE_LOOKUP"
    OPERATION_TYPE_DELETE_LOOKUP = "DELETE_LOOKUP"

    #: A constant which can be used with the operation_type property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "ENABLE_INGEST_TIME_RULE"
    OPERATION_TYPE_ENABLE_INGEST_TIME_RULE = "ENABLE_INGEST_TIME_RULE"

    #: A constant which can be used with the operation_type property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "DISABLE_INGEST_TIME_RULE"
    OPERATION_TYPE_DISABLE_INGEST_TIME_RULE = "DISABLE_INGEST_TIME_RULE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsConfigWorkRequest.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsConfigWorkRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogAnalyticsConfigWorkRequest.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsConfigWorkRequest.
        :type compartment_id: str

        :param operation_type:
            The value to assign to the operation_type property of this LogAnalyticsConfigWorkRequest.
            Allowed values for this property are: "CREATE_ASSOCIATIONS", "DELETE_ASSOCIATIONS", "APPEND_LOOKUP_DATA", "UPDATE_LOOKUP_DATA", "DELETE_LOOKUP", "ENABLE_INGEST_TIME_RULE", "DISABLE_INGEST_TIME_RULE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param payload:
            The value to assign to the payload property of this LogAnalyticsConfigWorkRequest.
        :type payload: list[oci.log_analytics.models.LogAnalyticsConfigWorkRequestPayload]

        :param percent_complete:
            The value to assign to the percent_complete property of this LogAnalyticsConfigWorkRequest.
        :type percent_complete: int

        :param time_started:
            The value to assign to the time_started property of this LogAnalyticsConfigWorkRequest.
        :type time_started: datetime

        :param time_accepted:
            The value to assign to the time_accepted property of this LogAnalyticsConfigWorkRequest.
        :type time_accepted: datetime

        :param time_finished:
            The value to assign to the time_finished property of this LogAnalyticsConfigWorkRequest.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogAnalyticsConfigWorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'operation_type': 'str',
            'payload': 'list[LogAnalyticsConfigWorkRequestPayload]',
            'percent_complete': 'int',
            'time_started': 'datetime',
            'time_accepted': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'operation_type': 'operationType',
            'payload': 'payload',
            'percent_complete': 'percentComplete',
            'time_started': 'timeStarted',
            'time_accepted': 'timeAccepted',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._operation_type = None
        self._payload = None
        self._percent_complete = None
        self._time_started = None
        self._time_accepted = None
        self._time_finished = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        Gets the id of this LogAnalyticsConfigWorkRequest.
        The workrequest unique identifier.


        :return: The id of this LogAnalyticsConfigWorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogAnalyticsConfigWorkRequest.
        The workrequest unique identifier.


        :param id: The id of this LogAnalyticsConfigWorkRequest.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this LogAnalyticsConfigWorkRequest.
        The compartment unique identifier.


        :return: The compartment_id of this LogAnalyticsConfigWorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsConfigWorkRequest.
        The compartment unique identifier.


        :param compartment_id: The compartment_id of this LogAnalyticsConfigWorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def operation_type(self):
        """
        Gets the operation_type of this LogAnalyticsConfigWorkRequest.
        The operation type

        Allowed values for this property are: "CREATE_ASSOCIATIONS", "DELETE_ASSOCIATIONS", "APPEND_LOOKUP_DATA", "UPDATE_LOOKUP_DATA", "DELETE_LOOKUP", "ENABLE_INGEST_TIME_RULE", "DISABLE_INGEST_TIME_RULE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this LogAnalyticsConfigWorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this LogAnalyticsConfigWorkRequest.
        The operation type


        :param operation_type: The operation_type of this LogAnalyticsConfigWorkRequest.
        :type: str
        """
        allowed_values = ["CREATE_ASSOCIATIONS", "DELETE_ASSOCIATIONS", "APPEND_LOOKUP_DATA", "UPDATE_LOOKUP_DATA", "DELETE_LOOKUP", "ENABLE_INGEST_TIME_RULE", "DISABLE_INGEST_TIME_RULE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def payload(self):
        """
        Gets the payload of this LogAnalyticsConfigWorkRequest.
        The list of config work request responses.


        :return: The payload of this LogAnalyticsConfigWorkRequest.
        :rtype: list[oci.log_analytics.models.LogAnalyticsConfigWorkRequestPayload]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this LogAnalyticsConfigWorkRequest.
        The list of config work request responses.


        :param payload: The payload of this LogAnalyticsConfigWorkRequest.
        :type: list[oci.log_analytics.models.LogAnalyticsConfigWorkRequestPayload]
        """
        self._payload = payload

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this LogAnalyticsConfigWorkRequest.
        The completion percentage.


        :return: The percent_complete of this LogAnalyticsConfigWorkRequest.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this LogAnalyticsConfigWorkRequest.
        The completion percentage.


        :param percent_complete: The percent_complete of this LogAnalyticsConfigWorkRequest.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def time_started(self):
        """
        Gets the time_started of this LogAnalyticsConfigWorkRequest.
        The time at which the work request was started.


        :return: The time_started of this LogAnalyticsConfigWorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this LogAnalyticsConfigWorkRequest.
        The time at which the work request was started.


        :param time_started: The time_started of this LogAnalyticsConfigWorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this LogAnalyticsConfigWorkRequest.
        The time at which the work request was accepted.


        :return: The time_accepted of this LogAnalyticsConfigWorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this LogAnalyticsConfigWorkRequest.
        The time at which the work request was accepted.


        :param time_accepted: The time_accepted of this LogAnalyticsConfigWorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_finished(self):
        """
        Gets the time_finished of this LogAnalyticsConfigWorkRequest.
        The time at which the work request was finished.


        :return: The time_finished of this LogAnalyticsConfigWorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this LogAnalyticsConfigWorkRequest.
        The time at which the work request was finished.


        :param time_finished: The time_finished of this LogAnalyticsConfigWorkRequest.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this LogAnalyticsConfigWorkRequest.
        The lifecycle status.  Valid values are ACCEPTED, IN_PROGRESS, SUCCEEDED
        or FAILED

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogAnalyticsConfigWorkRequest.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogAnalyticsConfigWorkRequest.
        The lifecycle status.  Valid values are ACCEPTED, IN_PROGRESS, SUCCEEDED
        or FAILED


        :param lifecycle_state: The lifecycle_state of this LogAnalyticsConfigWorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
