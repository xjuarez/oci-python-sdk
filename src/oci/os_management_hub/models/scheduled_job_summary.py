# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledJobSummary(object):
    """
    Summary of the scheduled job.
    """

    #: A constant which can be used with the schedule_type property of a ScheduledJobSummary.
    #: This constant has a value of "ONETIME"
    SCHEDULE_TYPE_ONETIME = "ONETIME"

    #: A constant which can be used with the schedule_type property of a ScheduledJobSummary.
    #: This constant has a value of "RECURRING"
    SCHEDULE_TYPE_RECURRING = "RECURRING"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledJobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduledJobSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledJobSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduledJobSummary.
        :type compartment_id: str

        :param schedule_type:
            The value to assign to the schedule_type property of this ScheduledJobSummary.
            Allowed values for this property are: "ONETIME", "RECURRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schedule_type: str

        :param time_created:
            The value to assign to the time_created property of this ScheduledJobSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ScheduledJobSummary.
        :type time_updated: datetime

        :param time_next_execution:
            The value to assign to the time_next_execution property of this ScheduledJobSummary.
        :type time_next_execution: datetime

        :param time_last_execution:
            The value to assign to the time_last_execution property of this ScheduledJobSummary.
        :type time_last_execution: datetime

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this ScheduledJobSummary.
        :type managed_instance_ids: list[str]

        :param managed_instance_group_ids:
            The value to assign to the managed_instance_group_ids property of this ScheduledJobSummary.
        :type managed_instance_group_ids: list[str]

        :param managed_compartment_ids:
            The value to assign to the managed_compartment_ids property of this ScheduledJobSummary.
        :type managed_compartment_ids: list[str]

        :param lifecycle_stage_ids:
            The value to assign to the lifecycle_stage_ids property of this ScheduledJobSummary.
        :type lifecycle_stage_ids: list[str]

        :param operations:
            The value to assign to the operations property of this ScheduledJobSummary.
        :type operations: list[oci.os_management_hub.models.ScheduledJobOperation]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledJobSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduledJobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduledJobSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param is_restricted:
            The value to assign to the is_restricted property of this ScheduledJobSummary.
        :type is_restricted: bool

        :param system_tags:
            The value to assign to the system_tags property of this ScheduledJobSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'schedule_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_next_execution': 'datetime',
            'time_last_execution': 'datetime',
            'managed_instance_ids': 'list[str]',
            'managed_instance_group_ids': 'list[str]',
            'managed_compartment_ids': 'list[str]',
            'lifecycle_stage_ids': 'list[str]',
            'operations': 'list[ScheduledJobOperation]',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_restricted': 'bool',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'schedule_type': 'scheduleType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_next_execution': 'timeNextExecution',
            'time_last_execution': 'timeLastExecution',
            'managed_instance_ids': 'managedInstanceIds',
            'managed_instance_group_ids': 'managedInstanceGroupIds',
            'managed_compartment_ids': 'managedCompartmentIds',
            'lifecycle_stage_ids': 'lifecycleStageIds',
            'operations': 'operations',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_restricted': 'isRestricted',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._schedule_type = None
        self._time_created = None
        self._time_updated = None
        self._time_next_execution = None
        self._time_last_execution = None
        self._managed_instance_ids = None
        self._managed_instance_group_ids = None
        self._managed_compartment_ids = None
        self._lifecycle_stage_ids = None
        self._operations = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_restricted = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledJobSummary.
        The OCID of the scheduled job.


        :return: The id of this ScheduledJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledJobSummary.
        The OCID of the scheduled job.


        :param id: The id of this ScheduledJobSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduledJobSummary.
        Scheduled job name.


        :return: The display_name of this ScheduledJobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduledJobSummary.
        Scheduled job name.


        :param display_name: The display_name of this ScheduledJobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ScheduledJobSummary.
        The OCID of the compartment containing the scheduled job.


        :return: The compartment_id of this ScheduledJobSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduledJobSummary.
        The OCID of the compartment containing the scheduled job.


        :param compartment_id: The compartment_id of this ScheduledJobSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def schedule_type(self):
        """
        **[Required]** Gets the schedule_type of this ScheduledJobSummary.
        The type of scheduling this scheduled job follows.

        Allowed values for this property are: "ONETIME", "RECURRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The schedule_type of this ScheduledJobSummary.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this ScheduledJobSummary.
        The type of scheduling this scheduled job follows.


        :param schedule_type: The schedule_type of this ScheduledJobSummary.
        :type: str
        """
        allowed_values = ["ONETIME", "RECURRING"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            schedule_type = 'UNKNOWN_ENUM_VALUE'
        self._schedule_type = schedule_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ScheduledJobSummary.
        The time this scheduled job was created. An RFC3339 formatted datetime string.


        :return: The time_created of this ScheduledJobSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ScheduledJobSummary.
        The time this scheduled job was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this ScheduledJobSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ScheduledJobSummary.
        The time this scheduled job was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this ScheduledJobSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ScheduledJobSummary.
        The time this scheduled job was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this ScheduledJobSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_next_execution(self):
        """
        **[Required]** Gets the time_next_execution of this ScheduledJobSummary.
        The time/date of the next scheduled execution of this scheduled job.


        :return: The time_next_execution of this ScheduledJobSummary.
        :rtype: datetime
        """
        return self._time_next_execution

    @time_next_execution.setter
    def time_next_execution(self, time_next_execution):
        """
        Sets the time_next_execution of this ScheduledJobSummary.
        The time/date of the next scheduled execution of this scheduled job.


        :param time_next_execution: The time_next_execution of this ScheduledJobSummary.
        :type: datetime
        """
        self._time_next_execution = time_next_execution

    @property
    def time_last_execution(self):
        """
        Gets the time_last_execution of this ScheduledJobSummary.
        The time/date of the last execution of this scheduled job.


        :return: The time_last_execution of this ScheduledJobSummary.
        :rtype: datetime
        """
        return self._time_last_execution

    @time_last_execution.setter
    def time_last_execution(self, time_last_execution):
        """
        Sets the time_last_execution of this ScheduledJobSummary.
        The time/date of the last execution of this scheduled job.


        :param time_last_execution: The time_last_execution of this ScheduledJobSummary.
        :type: datetime
        """
        self._time_last_execution = time_last_execution

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this ScheduledJobSummary.
        The list of managed instance OCIDs this scheduled job operates on (mutually exclusive with managedInstanceGroupIds, managedCompartmentIds and lifecycleStageIds).


        :return: The managed_instance_ids of this ScheduledJobSummary.
        :rtype: list[str]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this ScheduledJobSummary.
        The list of managed instance OCIDs this scheduled job operates on (mutually exclusive with managedInstanceGroupIds, managedCompartmentIds and lifecycleStageIds).


        :param managed_instance_ids: The managed_instance_ids of this ScheduledJobSummary.
        :type: list[str]
        """
        self._managed_instance_ids = managed_instance_ids

    @property
    def managed_instance_group_ids(self):
        """
        Gets the managed_instance_group_ids of this ScheduledJobSummary.
        The list of managed instance group OCIDs this scheduled job operates on (mutually exclusive with managedInstances, managedCompartmentIds and lifecycleStageIds).


        :return: The managed_instance_group_ids of this ScheduledJobSummary.
        :rtype: list[str]
        """
        return self._managed_instance_group_ids

    @managed_instance_group_ids.setter
    def managed_instance_group_ids(self, managed_instance_group_ids):
        """
        Sets the managed_instance_group_ids of this ScheduledJobSummary.
        The list of managed instance group OCIDs this scheduled job operates on (mutually exclusive with managedInstances, managedCompartmentIds and lifecycleStageIds).


        :param managed_instance_group_ids: The managed_instance_group_ids of this ScheduledJobSummary.
        :type: list[str]
        """
        self._managed_instance_group_ids = managed_instance_group_ids

    @property
    def managed_compartment_ids(self):
        """
        Gets the managed_compartment_ids of this ScheduledJobSummary.
        The list of target compartment OCIDs if this scheduled job operates on a compartment level (mutually exclusive with managedInstances, managedInstanceGroupIds and lifecycleStageIds).


        :return: The managed_compartment_ids of this ScheduledJobSummary.
        :rtype: list[str]
        """
        return self._managed_compartment_ids

    @managed_compartment_ids.setter
    def managed_compartment_ids(self, managed_compartment_ids):
        """
        Sets the managed_compartment_ids of this ScheduledJobSummary.
        The list of target compartment OCIDs if this scheduled job operates on a compartment level (mutually exclusive with managedInstances, managedInstanceGroupIds and lifecycleStageIds).


        :param managed_compartment_ids: The managed_compartment_ids of this ScheduledJobSummary.
        :type: list[str]
        """
        self._managed_compartment_ids = managed_compartment_ids

    @property
    def lifecycle_stage_ids(self):
        """
        Gets the lifecycle_stage_ids of this ScheduledJobSummary.
        The list of target lifecycle stage OCIDs if this scheduled job operates on lifecycle stages (mutually exclusive with managedInstances, managedInstanceGroupIds and managedCompartmentIds).


        :return: The lifecycle_stage_ids of this ScheduledJobSummary.
        :rtype: list[str]
        """
        return self._lifecycle_stage_ids

    @lifecycle_stage_ids.setter
    def lifecycle_stage_ids(self, lifecycle_stage_ids):
        """
        Sets the lifecycle_stage_ids of this ScheduledJobSummary.
        The list of target lifecycle stage OCIDs if this scheduled job operates on lifecycle stages (mutually exclusive with managedInstances, managedInstanceGroupIds and managedCompartmentIds).


        :param lifecycle_stage_ids: The lifecycle_stage_ids of this ScheduledJobSummary.
        :type: list[str]
        """
        self._lifecycle_stage_ids = lifecycle_stage_ids

    @property
    def operations(self):
        """
        **[Required]** Gets the operations of this ScheduledJobSummary.
        The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).


        :return: The operations of this ScheduledJobSummary.
        :rtype: list[oci.os_management_hub.models.ScheduledJobOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this ScheduledJobSummary.
        The list of operations this scheduled job needs to perform (can only support one operation if the operationType is not UPDATE_PACKAGES/UPDATE_ALL/UPDATE_SECURITY/UPDATE_BUGFIX/UPDATE_ENHANCEMENT/UPDATE_OTHER/UPDATE_KSPLICE_USERSPACE/UPDATE_KSPLICE_KERNEL).


        :param operations: The operations of this ScheduledJobSummary.
        :type: list[oci.os_management_hub.models.ScheduledJobOperation]
        """
        self._operations = operations

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduledJobSummary.
        The current state of the scheduled job.


        :return: The lifecycle_state of this ScheduledJobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledJobSummary.
        The current state of the scheduled job.


        :param lifecycle_state: The lifecycle_state of this ScheduledJobSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ScheduledJobSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ScheduledJobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduledJobSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ScheduledJobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ScheduledJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ScheduledJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduledJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ScheduledJobSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_restricted(self):
        """
        Gets the is_restricted of this ScheduledJobSummary.
        true, if the schedule job has its update/deletion capabilities restricted. (Used to track scheduled job for management station syncing).


        :return: The is_restricted of this ScheduledJobSummary.
        :rtype: bool
        """
        return self._is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted):
        """
        Sets the is_restricted of this ScheduledJobSummary.
        true, if the schedule job has its update/deletion capabilities restricted. (Used to track scheduled job for management station syncing).


        :param is_restricted: The is_restricted of this ScheduledJobSummary.
        :type: bool
        """
        self._is_restricted = is_restricted

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ScheduledJobSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ScheduledJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ScheduledJobSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ScheduledJobSummary.
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
