# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMaintenanceWindowDetails(object):
    """
    The information about the new MaintenanceWindow.
    """

    #: A constant which can be used with the maintenance_window_type property of a CreateMaintenanceWindowDetails.
    #: This constant has a value of "OPEN_ENDED"
    MAINTENANCE_WINDOW_TYPE_OPEN_ENDED = "OPEN_ENDED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMaintenanceWindowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMaintenanceWindowDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateMaintenanceWindowDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateMaintenanceWindowDetails.
        :type description: str

        :param is_outage:
            The value to assign to the is_outage property of this CreateMaintenanceWindowDetails.
        :type is_outage: bool

        :param maintenance_window_type:
            The value to assign to the maintenance_window_type property of this CreateMaintenanceWindowDetails.
            Allowed values for this property are: "OPEN_ENDED"
        :type maintenance_window_type: str

        :param time_schedule_start:
            The value to assign to the time_schedule_start property of this CreateMaintenanceWindowDetails.
        :type time_schedule_start: datetime

        :param duration:
            The value to assign to the duration property of this CreateMaintenanceWindowDetails.
        :type duration: str

        :param is_recurring:
            The value to assign to the is_recurring property of this CreateMaintenanceWindowDetails.
        :type is_recurring: bool

        :param recurrences:
            The value to assign to the recurrences property of this CreateMaintenanceWindowDetails.
        :type recurrences: str

        :param task_initiation_cutoff:
            The value to assign to the task_initiation_cutoff property of this CreateMaintenanceWindowDetails.
        :type task_initiation_cutoff: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMaintenanceWindowDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMaintenanceWindowDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'is_outage': 'bool',
            'maintenance_window_type': 'str',
            'time_schedule_start': 'datetime',
            'duration': 'str',
            'is_recurring': 'bool',
            'recurrences': 'str',
            'task_initiation_cutoff': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'is_outage': 'isOutage',
            'maintenance_window_type': 'maintenanceWindowType',
            'time_schedule_start': 'timeScheduleStart',
            'duration': 'duration',
            'is_recurring': 'isRecurring',
            'recurrences': 'recurrences',
            'task_initiation_cutoff': 'taskInitiationCutoff',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._is_outage = None
        self._maintenance_window_type = None
        self._time_schedule_start = None
        self._duration = None
        self._is_recurring = None
        self._recurrences = None
        self._task_initiation_cutoff = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMaintenanceWindowDetails.
        Tenancy OCID


        :return: The compartment_id of this CreateMaintenanceWindowDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMaintenanceWindowDetails.
        Tenancy OCID


        :param compartment_id: The compartment_id of this CreateMaintenanceWindowDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMaintenanceWindowDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateMaintenanceWindowDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMaintenanceWindowDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateMaintenanceWindowDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateMaintenanceWindowDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this CreateMaintenanceWindowDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateMaintenanceWindowDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this CreateMaintenanceWindowDetails.
        :type: str
        """
        self._description = description

    @property
    def is_outage(self):
        """
        Gets the is_outage of this CreateMaintenanceWindowDetails.
        Does the maintenenace window cause outage?
        An outage indicates whether a maintenance window can consider operations that require downtime.
        It means a period when the application is not accessible.


        :return: The is_outage of this CreateMaintenanceWindowDetails.
        :rtype: bool
        """
        return self._is_outage

    @is_outage.setter
    def is_outage(self, is_outage):
        """
        Sets the is_outage of this CreateMaintenanceWindowDetails.
        Does the maintenenace window cause outage?
        An outage indicates whether a maintenance window can consider operations that require downtime.
        It means a period when the application is not accessible.


        :param is_outage: The is_outage of this CreateMaintenanceWindowDetails.
        :type: bool
        """
        self._is_outage = is_outage

    @property
    def maintenance_window_type(self):
        """
        Gets the maintenance_window_type of this CreateMaintenanceWindowDetails.
        Type of maintenenace window

        Allowed values for this property are: "OPEN_ENDED"


        :return: The maintenance_window_type of this CreateMaintenanceWindowDetails.
        :rtype: str
        """
        return self._maintenance_window_type

    @maintenance_window_type.setter
    def maintenance_window_type(self, maintenance_window_type):
        """
        Sets the maintenance_window_type of this CreateMaintenanceWindowDetails.
        Type of maintenenace window


        :param maintenance_window_type: The maintenance_window_type of this CreateMaintenanceWindowDetails.
        :type: str
        """
        allowed_values = ["OPEN_ENDED"]
        if not value_allowed_none_or_none_sentinel(maintenance_window_type, allowed_values):
            raise ValueError(
                f"Invalid value for `maintenance_window_type`, must be None or one of {allowed_values}"
            )
        self._maintenance_window_type = maintenance_window_type

    @property
    def time_schedule_start(self):
        """
        Gets the time_schedule_start of this CreateMaintenanceWindowDetails.
        Specify the date and time of the day that the maintenance window starts.


        :return: The time_schedule_start of this CreateMaintenanceWindowDetails.
        :rtype: datetime
        """
        return self._time_schedule_start

    @time_schedule_start.setter
    def time_schedule_start(self, time_schedule_start):
        """
        Sets the time_schedule_start of this CreateMaintenanceWindowDetails.
        Specify the date and time of the day that the maintenance window starts.


        :param time_schedule_start: The time_schedule_start of this CreateMaintenanceWindowDetails.
        :type: datetime
        """
        self._time_schedule_start = time_schedule_start

    @property
    def duration(self):
        """
        **[Required]** Gets the duration of this CreateMaintenanceWindowDetails.
        Duration of the maintenance window.
        Specify how long the maintenance window remains open.


        :return: The duration of this CreateMaintenanceWindowDetails.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this CreateMaintenanceWindowDetails.
        Duration of the maintenance window.
        Specify how long the maintenance window remains open.


        :param duration: The duration of this CreateMaintenanceWindowDetails.
        :type: str
        """
        self._duration = duration

    @property
    def is_recurring(self):
        """
        Gets the is_recurring of this CreateMaintenanceWindowDetails.
        Is this a recurring maintenance window?


        :return: The is_recurring of this CreateMaintenanceWindowDetails.
        :rtype: bool
        """
        return self._is_recurring

    @is_recurring.setter
    def is_recurring(self, is_recurring):
        """
        Sets the is_recurring of this CreateMaintenanceWindowDetails.
        Is this a recurring maintenance window?


        :param is_recurring: The is_recurring of this CreateMaintenanceWindowDetails.
        :type: bool
        """
        self._is_recurring = is_recurring

    @property
    def recurrences(self):
        """
        Gets the recurrences of this CreateMaintenanceWindowDetails.
        Recurrence rule specification if maintenance window recurring.
        Specify the frequency of running the maintenance window.


        :return: The recurrences of this CreateMaintenanceWindowDetails.
        :rtype: str
        """
        return self._recurrences

    @recurrences.setter
    def recurrences(self, recurrences):
        """
        Sets the recurrences of this CreateMaintenanceWindowDetails.
        Recurrence rule specification if maintenance window recurring.
        Specify the frequency of running the maintenance window.


        :param recurrences: The recurrences of this CreateMaintenanceWindowDetails.
        :type: str
        """
        self._recurrences = recurrences

    @property
    def task_initiation_cutoff(self):
        """
        Gets the task_initiation_cutoff of this CreateMaintenanceWindowDetails.
        Task initiation cutoff time for the maintenance window.


        :return: The task_initiation_cutoff of this CreateMaintenanceWindowDetails.
        :rtype: int
        """
        return self._task_initiation_cutoff

    @task_initiation_cutoff.setter
    def task_initiation_cutoff(self, task_initiation_cutoff):
        """
        Sets the task_initiation_cutoff of this CreateMaintenanceWindowDetails.
        Task initiation cutoff time for the maintenance window.


        :param task_initiation_cutoff: The task_initiation_cutoff of this CreateMaintenanceWindowDetails.
        :type: int
        """
        self._task_initiation_cutoff = task_initiation_cutoff

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMaintenanceWindowDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMaintenanceWindowDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMaintenanceWindowDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMaintenanceWindowDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMaintenanceWindowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMaintenanceWindowDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMaintenanceWindowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMaintenanceWindowDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
