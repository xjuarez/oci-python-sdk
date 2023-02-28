# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    A summary of the status of a work request.
    """

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_MIGRATION"
    OPERATION_TYPE_CREATE_MIGRATION = "CREATE_MIGRATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_MIGRATION"
    OPERATION_TYPE_UPDATE_MIGRATION = "UPDATE_MIGRATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "REFRESH_MIGRATION"
    OPERATION_TYPE_REFRESH_MIGRATION = "REFRESH_MIGRATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_MIGRATION"
    OPERATION_TYPE_DELETE_MIGRATION = "DELETE_MIGRATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MOVE_MIGRATION"
    OPERATION_TYPE_MOVE_MIGRATION = "MOVE_MIGRATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "START_ASSET_REPLICATION"
    OPERATION_TYPE_START_ASSET_REPLICATION = "START_ASSET_REPLICATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "START_MIGRATION_REPLICATION"
    OPERATION_TYPE_START_MIGRATION_REPLICATION = "START_MIGRATION_REPLICATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_REPLICATION_SCHEDULE"
    OPERATION_TYPE_CREATE_REPLICATION_SCHEDULE = "CREATE_REPLICATION_SCHEDULE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_REPLICATION_SCHEDULE"
    OPERATION_TYPE_UPDATE_REPLICATION_SCHEDULE = "UPDATE_REPLICATION_SCHEDULE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_REPLICATION_SCHEDULE"
    OPERATION_TYPE_DELETE_REPLICATION_SCHEDULE = "DELETE_REPLICATION_SCHEDULE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MOVE_REPLICATION_SCHEDULE"
    OPERATION_TYPE_MOVE_REPLICATION_SCHEDULE = "MOVE_REPLICATION_SCHEDULE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_MIGRATION_PLAN"
    OPERATION_TYPE_CREATE_MIGRATION_PLAN = "CREATE_MIGRATION_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_MIGRATION_PLAN"
    OPERATION_TYPE_UPDATE_MIGRATION_PLAN = "UPDATE_MIGRATION_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_MIGRATION_PLAN"
    OPERATION_TYPE_DELETE_MIGRATION_PLAN = "DELETE_MIGRATION_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MOVE_MIGRATION_PLAN"
    OPERATION_TYPE_MOVE_MIGRATION_PLAN = "MOVE_MIGRATION_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "REFRESH_MIGRATION_PLAN"
    OPERATION_TYPE_REFRESH_MIGRATION_PLAN = "REFRESH_MIGRATION_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "EXECUTE_MIGRATION_PLAN"
    OPERATION_TYPE_EXECUTE_MIGRATION_PLAN = "EXECUTE_MIGRATION_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "REFRESH_MIGRATION_ASSET"
    OPERATION_TYPE_REFRESH_MIGRATION_ASSET = "REFRESH_MIGRATION_ASSET"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_MIGRATION_ASSET"
    OPERATION_TYPE_CREATE_MIGRATION_ASSET = "CREATE_MIGRATION_ASSET"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_MIGRATION_ASSET"
    OPERATION_TYPE_DELETE_MIGRATION_ASSET = "DELETE_MIGRATION_ASSET"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_TARGET_ASSET"
    OPERATION_TYPE_CREATE_TARGET_ASSET = "CREATE_TARGET_ASSET"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_TARGET_ASSET"
    OPERATION_TYPE_UPDATE_TARGET_ASSET = "UPDATE_TARGET_ASSET"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_TARGET_ASSET"
    OPERATION_TYPE_DELETE_TARGET_ASSET = "DELETE_TARGET_ASSET"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "WAITING"
    STATUS_WAITING = "WAITING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    STATUS_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
            Allowed values for this property are: "CREATE_MIGRATION", "UPDATE_MIGRATION", "REFRESH_MIGRATION", "DELETE_MIGRATION", "MOVE_MIGRATION", "START_ASSET_REPLICATION", "START_MIGRATION_REPLICATION", "CREATE_REPLICATION_SCHEDULE", "UPDATE_REPLICATION_SCHEDULE", "DELETE_REPLICATION_SCHEDULE", "MOVE_REPLICATION_SCHEDULE", "CREATE_MIGRATION_PLAN", "UPDATE_MIGRATION_PLAN", "DELETE_MIGRATION_PLAN", "MOVE_MIGRATION_PLAN", "REFRESH_MIGRATION_PLAN", "EXECUTE_MIGRATION_PLAN", "REFRESH_MIGRATION_ASSET", "CREATE_MIGRATION_ASSET", "DELETE_MIGRATION_ASSET", "CREATE_TARGET_ASSET", "UPDATE_TARGET_ASSET", "DELETE_TARGET_ASSET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[oci.cloud_migrations.models.WorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WorkRequestSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WorkRequestSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this WorkRequestSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        The type of work request.

        Allowed values for this property are: "CREATE_MIGRATION", "UPDATE_MIGRATION", "REFRESH_MIGRATION", "DELETE_MIGRATION", "MOVE_MIGRATION", "START_ASSET_REPLICATION", "START_MIGRATION_REPLICATION", "CREATE_REPLICATION_SCHEDULE", "UPDATE_REPLICATION_SCHEDULE", "DELETE_REPLICATION_SCHEDULE", "MOVE_REPLICATION_SCHEDULE", "CREATE_MIGRATION_PLAN", "UPDATE_MIGRATION_PLAN", "DELETE_MIGRATION_PLAN", "MOVE_MIGRATION_PLAN", "REFRESH_MIGRATION_PLAN", "EXECUTE_MIGRATION_PLAN", "REFRESH_MIGRATION_ASSET", "CREATE_MIGRATION_ASSET", "DELETE_MIGRATION_ASSET", "CREATE_TARGET_ASSET", "UPDATE_TARGET_ASSET", "DELETE_TARGET_ASSET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        The type of work request.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["CREATE_MIGRATION", "UPDATE_MIGRATION", "REFRESH_MIGRATION", "DELETE_MIGRATION", "MOVE_MIGRATION", "START_ASSET_REPLICATION", "START_MIGRATION_REPLICATION", "CREATE_REPLICATION_SCHEDULE", "UPDATE_REPLICATION_SCHEDULE", "DELETE_REPLICATION_SCHEDULE", "MOVE_REPLICATION_SCHEDULE", "CREATE_MIGRATION_PLAN", "UPDATE_MIGRATION_PLAN", "DELETE_MIGRATION_PLAN", "MOVE_MIGRATION_PLAN", "REFRESH_MIGRATION_PLAN", "EXECUTE_MIGRATION_PLAN", "REFRESH_MIGRATION_ASSET", "CREATE_MIGRATION_ASSET", "DELETE_MIGRATION_ASSET", "CREATE_TARGET_ASSET", "UPDATE_TARGET_ASSET", "DELETE_TARGET_ASSET"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        Status of the current work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        Status of the current work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The ID of the work request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The ID of the work request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource that is affected by the work request. If the work request affects multiple resources,
        and these resources are not in the same compartment, the service team can choose the primary
        resource of the compartment to be used.


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource that is affected by the work request. If the work request affects multiple resources,
        and these resources are not in the same compartment, the service team can choose the primary
        resource of the compartment to be used.


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[oci.cloud_migrations.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[oci.cloud_migrations.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequestSummary.
        The percentage of request completed.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        The percentage of request completed.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequestSummary.
        The date and time when the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        The date and time when the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequestSummary.
        The date and time when the request started, as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        The date and time when the request started, as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        The date and time when the object was complete, as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        The date and time when the object was complete, as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this WorkRequestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this WorkRequestSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this WorkRequestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this WorkRequestSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this WorkRequestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this WorkRequestSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this WorkRequestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this WorkRequestSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this WorkRequestSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this WorkRequestSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this WorkRequestSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this WorkRequestSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
