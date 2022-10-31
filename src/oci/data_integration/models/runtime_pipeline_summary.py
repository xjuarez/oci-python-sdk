# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuntimePipelineSummary(object):
    """
    The information about RuntimePipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RuntimePipelineSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pipeline:
            The value to assign to the pipeline property of this RuntimePipelineSummary.
        :type pipeline: oci.data_integration.models.Pipeline

        :param runtime_operators:
            The value to assign to the runtime_operators property of this RuntimePipelineSummary.
        :type runtime_operators: list[oci.data_integration.models.RuntimeOperator]

        :param parent_runtime_operator_key:
            The value to assign to the parent_runtime_operator_key property of this RuntimePipelineSummary.
        :type parent_runtime_operator_key: str

        """
        self.swagger_types = {
            'pipeline': 'Pipeline',
            'runtime_operators': 'list[RuntimeOperator]',
            'parent_runtime_operator_key': 'str'
        }

        self.attribute_map = {
            'pipeline': 'pipeline',
            'runtime_operators': 'runtimeOperators',
            'parent_runtime_operator_key': 'parentRuntimeOperatorKey'
        }

        self._pipeline = None
        self._runtime_operators = None
        self._parent_runtime_operator_key = None

    @property
    def pipeline(self):
        """
        Gets the pipeline of this RuntimePipelineSummary.

        :return: The pipeline of this RuntimePipelineSummary.
        :rtype: oci.data_integration.models.Pipeline
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """
        Sets the pipeline of this RuntimePipelineSummary.

        :param pipeline: The pipeline of this RuntimePipelineSummary.
        :type: oci.data_integration.models.Pipeline
        """
        self._pipeline = pipeline

    @property
    def runtime_operators(self):
        """
        Gets the runtime_operators of this RuntimePipelineSummary.
        A list of RuntimeOperators attached to the RuntimePipeline.


        :return: The runtime_operators of this RuntimePipelineSummary.
        :rtype: list[oci.data_integration.models.RuntimeOperator]
        """
        return self._runtime_operators

    @runtime_operators.setter
    def runtime_operators(self, runtime_operators):
        """
        Sets the runtime_operators of this RuntimePipelineSummary.
        A list of RuntimeOperators attached to the RuntimePipeline.


        :param runtime_operators: The runtime_operators of this RuntimePipelineSummary.
        :type: list[oci.data_integration.models.RuntimeOperator]
        """
        self._runtime_operators = runtime_operators

    @property
    def parent_runtime_operator_key(self):
        """
        Gets the parent_runtime_operator_key of this RuntimePipelineSummary.
        The parent RuntimePipeline's RuntimeOperator key.


        :return: The parent_runtime_operator_key of this RuntimePipelineSummary.
        :rtype: str
        """
        return self._parent_runtime_operator_key

    @parent_runtime_operator_key.setter
    def parent_runtime_operator_key(self, parent_runtime_operator_key):
        """
        Sets the parent_runtime_operator_key of this RuntimePipelineSummary.
        The parent RuntimePipeline's RuntimeOperator key.


        :param parent_runtime_operator_key: The parent_runtime_operator_key of this RuntimePipelineSummary.
        :type: str
        """
        self._parent_runtime_operator_key = parent_runtime_operator_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
