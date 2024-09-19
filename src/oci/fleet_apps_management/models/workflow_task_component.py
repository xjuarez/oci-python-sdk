# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .workflow_component import WorkflowComponent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkflowTaskComponent(WorkflowComponent):
    """
    Workflow Task Component Details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkflowTaskComponent object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.WorkflowTaskComponent.type` attribute
        of this class is ``TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this WorkflowTaskComponent.
            Allowed values for this property are: "TASK", "PARALLEL_TASK_GROUP"
        :type type: str

        :param step_name:
            The value to assign to the step_name property of this WorkflowTaskComponent.
        :type step_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'step_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'step_name': 'stepName'
        }

        self._type = None
        self._step_name = None
        self._type = 'TASK'

    @property
    def step_name(self):
        """
        **[Required]** Gets the step_name of this WorkflowTaskComponent.
        Provide StepName for the Task.


        :return: The step_name of this WorkflowTaskComponent.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this WorkflowTaskComponent.
        Provide StepName for the Task.


        :param step_name: The step_name of this WorkflowTaskComponent.
        :type: str
        """
        self._step_name = step_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other