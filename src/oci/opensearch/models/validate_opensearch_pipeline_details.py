# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateOpensearchPipelineDetails(object):
    """
    The configuration details for validating pipeline configuration provided as input.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateOpensearchPipelineDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ValidateOpensearchPipelineDetails.
        :type compartment_id: str

        :param pipeline_configuration_body:
            The value to assign to the pipeline_configuration_body property of this ValidateOpensearchPipelineDetails.
        :type pipeline_configuration_body: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'pipeline_configuration_body': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'pipeline_configuration_body': 'pipelineConfigurationBody'
        }

        self._compartment_id = None
        self._pipeline_configuration_body = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ValidateOpensearchPipelineDetails.
        The OCID of the compartment where the pipeline will be created.


        :return: The compartment_id of this ValidateOpensearchPipelineDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ValidateOpensearchPipelineDetails.
        The OCID of the compartment where the pipeline will be created.


        :param compartment_id: The compartment_id of this ValidateOpensearchPipelineDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def pipeline_configuration_body(self):
        """
        **[Required]** Gets the pipeline_configuration_body of this ValidateOpensearchPipelineDetails.
        The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :return: The pipeline_configuration_body of this ValidateOpensearchPipelineDetails.
        :rtype: str
        """
        return self._pipeline_configuration_body

    @pipeline_configuration_body.setter
    def pipeline_configuration_body(self, pipeline_configuration_body):
        """
        Sets the pipeline_configuration_body of this ValidateOpensearchPipelineDetails.
        The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :param pipeline_configuration_body: The pipeline_configuration_body of this ValidateOpensearchPipelineDetails.
        :type: str
        """
        self._pipeline_configuration_body = pipeline_configuration_body

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
