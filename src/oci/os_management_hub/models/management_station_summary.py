# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementStationSummary(object):
    """
    Summary of the Management Station.
    """

    #: A constant which can be used with the overall_state property of a ManagementStationSummary.
    #: This constant has a value of "NORMAL"
    OVERALL_STATE_NORMAL = "NORMAL"

    #: A constant which can be used with the overall_state property of a ManagementStationSummary.
    #: This constant has a value of "REGISTRATIONERROR"
    OVERALL_STATE_REGISTRATIONERROR = "REGISTRATIONERROR"

    #: A constant which can be used with the overall_state property of a ManagementStationSummary.
    #: This constant has a value of "SYNCING"
    OVERALL_STATE_SYNCING = "SYNCING"

    #: A constant which can be used with the overall_state property of a ManagementStationSummary.
    #: This constant has a value of "SYNCFAILED"
    OVERALL_STATE_SYNCFAILED = "SYNCFAILED"

    #: A constant which can be used with the overall_state property of a ManagementStationSummary.
    #: This constant has a value of "WARNING"
    OVERALL_STATE_WARNING = "WARNING"

    #: A constant which can be used with the overall_state property of a ManagementStationSummary.
    #: This constant has a value of "ERROR"
    OVERALL_STATE_ERROR = "ERROR"

    #: A constant which can be used with the overall_state property of a ManagementStationSummary.
    #: This constant has a value of "UNAVAILABLE"
    OVERALL_STATE_UNAVAILABLE = "UNAVAILABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementStationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagementStationSummary.
        :type id: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this ManagementStationSummary.
        :type managed_instance_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagementStationSummary.
        :type compartment_id: str

        :param profile_id:
            The value to assign to the profile_id property of this ManagementStationSummary.
        :type profile_id: str

        :param scheduled_job_id:
            The value to assign to the scheduled_job_id property of this ManagementStationSummary.
        :type scheduled_job_id: str

        :param time_next_execution:
            The value to assign to the time_next_execution property of this ManagementStationSummary.
        :type time_next_execution: datetime

        :param display_name:
            The value to assign to the display_name property of this ManagementStationSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagementStationSummary.
        :type description: str

        :param hostname:
            The value to assign to the hostname property of this ManagementStationSummary.
        :type hostname: str

        :param overall_state:
            The value to assign to the overall_state property of this ManagementStationSummary.
            Allowed values for this property are: "NORMAL", "REGISTRATIONERROR", "SYNCING", "SYNCFAILED", "WARNING", "ERROR", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type overall_state: str

        :param overall_percentage:
            The value to assign to the overall_percentage property of this ManagementStationSummary.
        :type overall_percentage: int

        :param mirror_capacity:
            The value to assign to the mirror_capacity property of this ManagementStationSummary.
        :type mirror_capacity: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementStationSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagementStationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagementStationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ManagementStationSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'managed_instance_id': 'str',
            'compartment_id': 'str',
            'profile_id': 'str',
            'scheduled_job_id': 'str',
            'time_next_execution': 'datetime',
            'display_name': 'str',
            'description': 'str',
            'hostname': 'str',
            'overall_state': 'str',
            'overall_percentage': 'int',
            'mirror_capacity': 'int',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'managed_instance_id': 'managedInstanceId',
            'compartment_id': 'compartmentId',
            'profile_id': 'profileId',
            'scheduled_job_id': 'scheduledJobId',
            'time_next_execution': 'timeNextExecution',
            'display_name': 'displayName',
            'description': 'description',
            'hostname': 'hostname',
            'overall_state': 'overallState',
            'overall_percentage': 'overallPercentage',
            'mirror_capacity': 'mirrorCapacity',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._managed_instance_id = None
        self._compartment_id = None
        self._profile_id = None
        self._scheduled_job_id = None
        self._time_next_execution = None
        self._display_name = None
        self._description = None
        self._hostname = None
        self._overall_state = None
        self._overall_percentage = None
        self._mirror_capacity = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementStationSummary.
        OCID for the Management Station


        :return: The id of this ManagementStationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementStationSummary.
        OCID for the Management Station


        :param id: The id of this ManagementStationSummary.
        :type: str
        """
        self._id = id

    @property
    def managed_instance_id(self):
        """
        Gets the managed_instance_id of this ManagementStationSummary.
        OCID for the Instance associated with the Management Station


        :return: The managed_instance_id of this ManagementStationSummary.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this ManagementStationSummary.
        OCID for the Instance associated with the Management Station


        :param managed_instance_id: The managed_instance_id of this ManagementStationSummary.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagementStationSummary.
        The OCID of the tenancy containing the Management Station.


        :return: The compartment_id of this ManagementStationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagementStationSummary.
        The OCID of the tenancy containing the Management Station.


        :param compartment_id: The compartment_id of this ManagementStationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def profile_id(self):
        """
        Gets the profile_id of this ManagementStationSummary.
        OCID of the Registration Profile associated with the Management Station


        :return: The profile_id of this ManagementStationSummary.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """
        Sets the profile_id of this ManagementStationSummary.
        OCID of the Registration Profile associated with the Management Station


        :param profile_id: The profile_id of this ManagementStationSummary.
        :type: str
        """
        self._profile_id = profile_id

    @property
    def scheduled_job_id(self):
        """
        Gets the scheduled_job_id of this ManagementStationSummary.
        OCID of the Scheduled Job for mirror sync


        :return: The scheduled_job_id of this ManagementStationSummary.
        :rtype: str
        """
        return self._scheduled_job_id

    @scheduled_job_id.setter
    def scheduled_job_id(self, scheduled_job_id):
        """
        Sets the scheduled_job_id of this ManagementStationSummary.
        OCID of the Scheduled Job for mirror sync


        :param scheduled_job_id: The scheduled_job_id of this ManagementStationSummary.
        :type: str
        """
        self._scheduled_job_id = scheduled_job_id

    @property
    def time_next_execution(self):
        """
        Gets the time_next_execution of this ManagementStationSummary.
        the time/date of the next scheduled execution of the Scheduled Job


        :return: The time_next_execution of this ManagementStationSummary.
        :rtype: datetime
        """
        return self._time_next_execution

    @time_next_execution.setter
    def time_next_execution(self, time_next_execution):
        """
        Sets the time_next_execution of this ManagementStationSummary.
        the time/date of the next scheduled execution of the Scheduled Job


        :param time_next_execution: The time_next_execution of this ManagementStationSummary.
        :type: datetime
        """
        self._time_next_execution = time_next_execution

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagementStationSummary.
        ManagementStation name


        :return: The display_name of this ManagementStationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementStationSummary.
        ManagementStation name


        :param display_name: The display_name of this ManagementStationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ManagementStationSummary.
        Details describing the Management Station config.


        :return: The description of this ManagementStationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagementStationSummary.
        Details describing the Management Station config.


        :param description: The description of this ManagementStationSummary.
        :type: str
        """
        self._description = description

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this ManagementStationSummary.
        Name of the host


        :return: The hostname of this ManagementStationSummary.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this ManagementStationSummary.
        Name of the host


        :param hostname: The hostname of this ManagementStationSummary.
        :type: str
        """
        self._hostname = hostname

    @property
    def overall_state(self):
        """
        Gets the overall_state of this ManagementStationSummary.
        Current state of the mirroring

        Allowed values for this property are: "NORMAL", "REGISTRATIONERROR", "SYNCING", "SYNCFAILED", "WARNING", "ERROR", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The overall_state of this ManagementStationSummary.
        :rtype: str
        """
        return self._overall_state

    @overall_state.setter
    def overall_state(self, overall_state):
        """
        Sets the overall_state of this ManagementStationSummary.
        Current state of the mirroring


        :param overall_state: The overall_state of this ManagementStationSummary.
        :type: str
        """
        allowed_values = ["NORMAL", "REGISTRATIONERROR", "SYNCING", "SYNCFAILED", "WARNING", "ERROR", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(overall_state, allowed_values):
            overall_state = 'UNKNOWN_ENUM_VALUE'
        self._overall_state = overall_state

    @property
    def overall_percentage(self):
        """
        Gets the overall_percentage of this ManagementStationSummary.
        A decimal number representing the completeness percentage


        :return: The overall_percentage of this ManagementStationSummary.
        :rtype: int
        """
        return self._overall_percentage

    @overall_percentage.setter
    def overall_percentage(self, overall_percentage):
        """
        Sets the overall_percentage of this ManagementStationSummary.
        A decimal number representing the completeness percentage


        :param overall_percentage: The overall_percentage of this ManagementStationSummary.
        :type: int
        """
        self._overall_percentage = overall_percentage

    @property
    def mirror_capacity(self):
        """
        Gets the mirror_capacity of this ManagementStationSummary.
        A decimal number representing the mirror capacity


        :return: The mirror_capacity of this ManagementStationSummary.
        :rtype: int
        """
        return self._mirror_capacity

    @mirror_capacity.setter
    def mirror_capacity(self, mirror_capacity):
        """
        Sets the mirror_capacity of this ManagementStationSummary.
        A decimal number representing the mirror capacity


        :param mirror_capacity: The mirror_capacity of this ManagementStationSummary.
        :type: int
        """
        self._mirror_capacity = mirror_capacity

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagementStationSummary.
        The current state of the Management Station config.


        :return: The lifecycle_state of this ManagementStationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementStationSummary.
        The current state of the Management Station config.


        :param lifecycle_state: The lifecycle_state of this ManagementStationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagementStationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ManagementStationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagementStationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ManagementStationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagementStationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ManagementStationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagementStationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ManagementStationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ManagementStationSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ManagementStationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ManagementStationSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ManagementStationSummary.
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
