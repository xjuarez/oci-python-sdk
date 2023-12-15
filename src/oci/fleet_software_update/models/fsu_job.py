# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FsuJob(object):
    """
    Exadata Fleet Update Job resource.
    """

    #: A constant which can be used with the type property of a FsuJob.
    #: This constant has a value of "STAGE"
    TYPE_STAGE = "STAGE"

    #: A constant which can be used with the type property of a FsuJob.
    #: This constant has a value of "PRECHECK"
    TYPE_PRECHECK = "PRECHECK"

    #: A constant which can be used with the type property of a FsuJob.
    #: This constant has a value of "APPLY"
    TYPE_APPLY = "APPLY"

    #: A constant which can be used with the type property of a FsuJob.
    #: This constant has a value of "ROLLBACK_AND_REMOVE_TARGET"
    TYPE_ROLLBACK_AND_REMOVE_TARGET = "ROLLBACK_AND_REMOVE_TARGET"

    #: A constant which can be used with the type property of a FsuJob.
    #: This constant has a value of "CLEANUP"
    TYPE_CLEANUP = "CLEANUP"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "UNKNOWN"
    LIFECYCLE_STATE_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a FsuJob.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new FsuJob object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.ApplyFsuJob`
        * :class:`~oci.fleet_software_update.models.StageFsuJob`
        * :class:`~oci.fleet_software_update.models.PrecheckFsuJob`
        * :class:`~oci.fleet_software_update.models.RollbackFsuJob`
        * :class:`~oci.fleet_software_update.models.CleanupFsuJob`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FsuJob.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this FsuJob.
        :type display_name: str

        :param type:
            The value to assign to the type property of this FsuJob.
            Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FsuJob.
        :type compartment_id: str

        :param fsu_action_id:
            The value to assign to the fsu_action_id property of this FsuJob.
        :type fsu_action_id: str

        :param progress:
            The value to assign to the progress property of this FsuJob.
        :type progress: oci.fleet_software_update.models.JobProgressDetails

        :param time_created:
            The value to assign to the time_created property of this FsuJob.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this FsuJob.
        :type time_started: datetime

        :param time_updated:
            The value to assign to the time_updated property of this FsuJob.
        :type time_updated: datetime

        :param time_finished:
            The value to assign to the time_finished property of this FsuJob.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FsuJob.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FsuJob.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FsuJob.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FsuJob.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this FsuJob.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'fsu_action_id': 'str',
            'progress': 'JobProgressDetails',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_updated': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'fsu_action_id': 'fsuActionId',
            'progress': 'progress',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_updated': 'timeUpdated',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._type = None
        self._compartment_id = None
        self._fsu_action_id = None
        self._progress = None
        self._time_created = None
        self._time_started = None
        self._time_updated = None
        self._time_finished = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'APPLY':
            return 'ApplyFsuJob'

        if type == 'STAGE':
            return 'StageFsuJob'

        if type == 'PRECHECK':
            return 'PrecheckFsuJob'

        if type == 'ROLLBACK_AND_REMOVE_TARGET':
            return 'RollbackFsuJob'

        if type == 'CLEANUP':
            return 'CleanupFsuJob'
        else:
            return 'FsuJob'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FsuJob.
        OCID identifier for the Exadata Fleet Update Job.


        :return: The id of this FsuJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FsuJob.
        OCID identifier for the Exadata Fleet Update Job.


        :param id: The id of this FsuJob.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this FsuJob.
        Exadata Fleet Update Job display name.


        :return: The display_name of this FsuJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FsuJob.
        Exadata Fleet Update Job display name.


        :param display_name: The display_name of this FsuJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this FsuJob.
        Exadata Fleet Update Job type.

        Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this FsuJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FsuJob.
        Exadata Fleet Update Job type.


        :param type: The type of this FsuJob.
        :type: str
        """
        allowed_values = ["STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FsuJob.
        Compartment Identifier, this will map to the owner Exadata Fleet Update Action resource.


        :return: The compartment_id of this FsuJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FsuJob.
        Compartment Identifier, this will map to the owner Exadata Fleet Update Action resource.


        :param compartment_id: The compartment_id of this FsuJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fsu_action_id(self):
        """
        **[Required]** Gets the fsu_action_id of this FsuJob.
        OCID of the Exadata Fleet Update Action that this job is part of.


        :return: The fsu_action_id of this FsuJob.
        :rtype: str
        """
        return self._fsu_action_id

    @fsu_action_id.setter
    def fsu_action_id(self, fsu_action_id):
        """
        Sets the fsu_action_id of this FsuJob.
        OCID of the Exadata Fleet Update Action that this job is part of.


        :param fsu_action_id: The fsu_action_id of this FsuJob.
        :type: str
        """
        self._fsu_action_id = fsu_action_id

    @property
    def progress(self):
        """
        Gets the progress of this FsuJob.

        :return: The progress of this FsuJob.
        :rtype: oci.fleet_software_update.models.JobProgressDetails
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this FsuJob.

        :param progress: The progress of this FsuJob.
        :type: oci.fleet_software_update.models.JobProgressDetails
        """
        self._progress = progress

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this FsuJob.
        The time the Exadata Fleet Update Job was created. An RFC3339 formatted datetime string.


        :return: The time_created of this FsuJob.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FsuJob.
        The time the Exadata Fleet Update Job was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this FsuJob.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this FsuJob.
        The time the Exadata Fleet Update Job started execution. An RFC3339 formatted datetime string.


        :return: The time_started of this FsuJob.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this FsuJob.
        The time the Exadata Fleet Update Job started execution. An RFC3339 formatted datetime string.


        :param time_started: The time_started of this FsuJob.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_updated(self):
        """
        Gets the time_updated of this FsuJob.
        The time the Exadata Fleet Update Job was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this FsuJob.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this FsuJob.
        The time the Exadata Fleet Update Job was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this FsuJob.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_finished(self):
        """
        Gets the time_finished of this FsuJob.
        The time the Exadata Fleet Update Job completed execution. An RFC3339 formatted datetime string.


        :return: The time_finished of this FsuJob.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this FsuJob.
        The time the Exadata Fleet Update Job completed execution. An RFC3339 formatted datetime string.


        :param time_finished: The time_finished of this FsuJob.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FsuJob.
        The current state of the Exadata Fleet Update Job.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FsuJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FsuJob.
        The current state of the Exadata Fleet Update Job.


        :param lifecycle_state: The lifecycle_state of this FsuJob.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this FsuJob.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this FsuJob.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this FsuJob.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this FsuJob.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FsuJob.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this FsuJob.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FsuJob.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this FsuJob.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FsuJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this FsuJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FsuJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this FsuJob.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this FsuJob.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this FsuJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this FsuJob.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this FsuJob.
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
