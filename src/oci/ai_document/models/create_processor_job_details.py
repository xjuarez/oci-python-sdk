# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateProcessorJobDetails(object):
    """
    The details used to create a processor job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateProcessorJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_location:
            The value to assign to the input_location property of this CreateProcessorJobDetails.
        :type input_location: oci.ai_document.models.InputLocation

        :param output_location:
            The value to assign to the output_location property of this CreateProcessorJobDetails.
        :type output_location: oci.ai_document.models.OutputLocation

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateProcessorJobDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateProcessorJobDetails.
        :type display_name: str

        :param processor_config:
            The value to assign to the processor_config property of this CreateProcessorJobDetails.
        :type processor_config: oci.ai_document.models.ProcessorConfig

        """
        self.swagger_types = {
            'input_location': 'InputLocation',
            'output_location': 'OutputLocation',
            'compartment_id': 'str',
            'display_name': 'str',
            'processor_config': 'ProcessorConfig'
        }

        self.attribute_map = {
            'input_location': 'inputLocation',
            'output_location': 'outputLocation',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'processor_config': 'processorConfig'
        }

        self._input_location = None
        self._output_location = None
        self._compartment_id = None
        self._display_name = None
        self._processor_config = None

    @property
    def input_location(self):
        """
        **[Required]** Gets the input_location of this CreateProcessorJobDetails.

        :return: The input_location of this CreateProcessorJobDetails.
        :rtype: oci.ai_document.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this CreateProcessorJobDetails.

        :param input_location: The input_location of this CreateProcessorJobDetails.
        :type: oci.ai_document.models.InputLocation
        """
        self._input_location = input_location

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this CreateProcessorJobDetails.

        :return: The output_location of this CreateProcessorJobDetails.
        :rtype: oci.ai_document.models.OutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this CreateProcessorJobDetails.

        :param output_location: The output_location of this CreateProcessorJobDetails.
        :type: oci.ai_document.models.OutputLocation
        """
        self._output_location = output_location

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateProcessorJobDetails.
        The compartment identifier.


        :return: The compartment_id of this CreateProcessorJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateProcessorJobDetails.
        The compartment identifier.


        :param compartment_id: The compartment_id of this CreateProcessorJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateProcessorJobDetails.
        The display name of the processor job.


        :return: The display_name of this CreateProcessorJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateProcessorJobDetails.
        The display name of the processor job.


        :param display_name: The display_name of this CreateProcessorJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def processor_config(self):
        """
        **[Required]** Gets the processor_config of this CreateProcessorJobDetails.

        :return: The processor_config of this CreateProcessorJobDetails.
        :rtype: oci.ai_document.models.ProcessorConfig
        """
        return self._processor_config

    @processor_config.setter
    def processor_config(self, processor_config):
        """
        Sets the processor_config of this CreateProcessorJobDetails.

        :param processor_config: The processor_config of this CreateProcessorJobDetails.
        :type: oci.ai_document.models.ProcessorConfig
        """
        self._processor_config = processor_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
