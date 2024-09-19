# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSchedulerDefinitionDetails(object):
    """
    The information about new SchedulerDefinition.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSchedulerDefinitionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateSchedulerDefinitionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateSchedulerDefinitionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSchedulerDefinitionDetails.
        :type compartment_id: str

        :param activity_initiation_cut_off:
            The value to assign to the activity_initiation_cut_off property of this CreateSchedulerDefinitionDetails.
        :type activity_initiation_cut_off: int

        :param schedule:
            The value to assign to the schedule property of this CreateSchedulerDefinitionDetails.
        :type schedule: oci.fleet_apps_management.models.Schedule

        :param action_groups:
            The value to assign to the action_groups property of this CreateSchedulerDefinitionDetails.
        :type action_groups: list[oci.fleet_apps_management.models.ActionGroup]

        :param run_books:
            The value to assign to the run_books property of this CreateSchedulerDefinitionDetails.
        :type run_books: list[oci.fleet_apps_management.models.OperationRunbook]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSchedulerDefinitionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSchedulerDefinitionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'activity_initiation_cut_off': 'int',
            'schedule': 'Schedule',
            'action_groups': 'list[ActionGroup]',
            'run_books': 'list[OperationRunbook]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'activity_initiation_cut_off': 'activityInitiationCutOff',
            'schedule': 'schedule',
            'action_groups': 'actionGroups',
            'run_books': 'runBooks',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._activity_initiation_cut_off = None
        self._schedule = None
        self._action_groups = None
        self._run_books = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSchedulerDefinitionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateSchedulerDefinitionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSchedulerDefinitionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateSchedulerDefinitionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateSchedulerDefinitionDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this CreateSchedulerDefinitionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSchedulerDefinitionDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this CreateSchedulerDefinitionDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSchedulerDefinitionDetails.
        Tenancy OCID


        :return: The compartment_id of this CreateSchedulerDefinitionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSchedulerDefinitionDetails.
        Tenancy OCID


        :param compartment_id: The compartment_id of this CreateSchedulerDefinitionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def activity_initiation_cut_off(self):
        """
        Gets the activity_initiation_cut_off of this CreateSchedulerDefinitionDetails.
        Activity Initiation Cut Off


        :return: The activity_initiation_cut_off of this CreateSchedulerDefinitionDetails.
        :rtype: int
        """
        return self._activity_initiation_cut_off

    @activity_initiation_cut_off.setter
    def activity_initiation_cut_off(self, activity_initiation_cut_off):
        """
        Sets the activity_initiation_cut_off of this CreateSchedulerDefinitionDetails.
        Activity Initiation Cut Off


        :param activity_initiation_cut_off: The activity_initiation_cut_off of this CreateSchedulerDefinitionDetails.
        :type: int
        """
        self._activity_initiation_cut_off = activity_initiation_cut_off

    @property
    def schedule(self):
        """
        **[Required]** Gets the schedule of this CreateSchedulerDefinitionDetails.

        :return: The schedule of this CreateSchedulerDefinitionDetails.
        :rtype: oci.fleet_apps_management.models.Schedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this CreateSchedulerDefinitionDetails.

        :param schedule: The schedule of this CreateSchedulerDefinitionDetails.
        :type: oci.fleet_apps_management.models.Schedule
        """
        self._schedule = schedule

    @property
    def action_groups(self):
        """
        **[Required]** Gets the action_groups of this CreateSchedulerDefinitionDetails.
        Action Groups associated with the Schedule.


        :return: The action_groups of this CreateSchedulerDefinitionDetails.
        :rtype: list[oci.fleet_apps_management.models.ActionGroup]
        """
        return self._action_groups

    @action_groups.setter
    def action_groups(self, action_groups):
        """
        Sets the action_groups of this CreateSchedulerDefinitionDetails.
        Action Groups associated with the Schedule.


        :param action_groups: The action_groups of this CreateSchedulerDefinitionDetails.
        :type: list[oci.fleet_apps_management.models.ActionGroup]
        """
        self._action_groups = action_groups

    @property
    def run_books(self):
        """
        Gets the run_books of this CreateSchedulerDefinitionDetails.
        Runbooks.


        :return: The run_books of this CreateSchedulerDefinitionDetails.
        :rtype: list[oci.fleet_apps_management.models.OperationRunbook]
        """
        return self._run_books

    @run_books.setter
    def run_books(self, run_books):
        """
        Sets the run_books of this CreateSchedulerDefinitionDetails.
        Runbooks.


        :param run_books: The run_books of this CreateSchedulerDefinitionDetails.
        :type: list[oci.fleet_apps_management.models.OperationRunbook]
        """
        self._run_books = run_books

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSchedulerDefinitionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateSchedulerDefinitionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSchedulerDefinitionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateSchedulerDefinitionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSchedulerDefinitionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateSchedulerDefinitionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSchedulerDefinitionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateSchedulerDefinitionDetails.
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