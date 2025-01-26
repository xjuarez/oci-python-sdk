# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereParameterDefinition(object):
    """
    A definition of tool parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CohereParameterDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CohereParameterDefinition.
        :type description: str

        :param type:
            The value to assign to the type property of this CohereParameterDefinition.
        :type type: str

        :param is_required:
            The value to assign to the is_required property of this CohereParameterDefinition.
        :type is_required: bool

        """
        self.swagger_types = {
            'description': 'str',
            'type': 'str',
            'is_required': 'bool'
        }

        self.attribute_map = {
            'description': 'description',
            'type': 'type',
            'is_required': 'isRequired'
        }

        self._description = None
        self._type = None
        self._is_required = None

    @property
    def description(self):
        """
        Gets the description of this CohereParameterDefinition.
        The description of the parameter.


        :return: The description of this CohereParameterDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CohereParameterDefinition.
        The description of the parameter.


        :param description: The description of this CohereParameterDefinition.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CohereParameterDefinition.
        The type of the parameter. Must be a valid Python type.


        :return: The type of this CohereParameterDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CohereParameterDefinition.
        The type of the parameter. Must be a valid Python type.


        :param type: The type of this CohereParameterDefinition.
        :type: str
        """
        self._type = type

    @property
    def is_required(self):
        """
        Gets the is_required of this CohereParameterDefinition.
        Denotes whether the parameter is always present (required) or not. Defaults to not required.


        :return: The is_required of this CohereParameterDefinition.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this CohereParameterDefinition.
        Denotes whether the parameter is always present (required) or not. Defaults to not required.


        :param is_required: The is_required of this CohereParameterDefinition.
        :type: bool
        """
        self._is_required = is_required

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
