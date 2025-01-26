# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .workflow_component import WorkflowComponent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkflowGroupComponent(WorkflowComponent):
    """
    Workflow Group Component Details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkflowGroupComponent object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.WorkflowGroupComponent.type` attribute
        of this class is ``PARALLEL_TASK_GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this WorkflowGroupComponent.
            Allowed values for this property are: "TASK", "PARALLEL_TASK_GROUP"
        :type type: str

        :param group_name:
            The value to assign to the group_name property of this WorkflowGroupComponent.
        :type group_name: str

        :param steps:
            The value to assign to the steps property of this WorkflowGroupComponent.
        :type steps: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'group_name': 'str',
            'steps': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'group_name': 'groupName',
            'steps': 'steps'
        }

        self._type = None
        self._group_name = None
        self._steps = None
        self._type = 'PARALLEL_TASK_GROUP'

    @property
    def group_name(self):
        """
        **[Required]** Gets the group_name of this WorkflowGroupComponent.
        Name of the group.


        :return: The group_name of this WorkflowGroupComponent.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this WorkflowGroupComponent.
        Name of the group.


        :param group_name: The group_name of this WorkflowGroupComponent.
        :type: str
        """
        self._group_name = group_name

    @property
    def steps(self):
        """
        Gets the steps of this WorkflowGroupComponent.
        Tasks within the Group.
        Provide the stepName for all applicable tasks.


        :return: The steps of this WorkflowGroupComponent.
        :rtype: list[str]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps of this WorkflowGroupComponent.
        Tasks within the Group.
        Provide the stepName for all applicable tasks.


        :param steps: The steps of this WorkflowGroupComponent.
        :type: list[str]
        """
        self._steps = steps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
