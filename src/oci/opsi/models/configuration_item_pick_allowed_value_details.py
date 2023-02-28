# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .configuration_item_allowed_value_details import ConfigurationItemAllowedValueDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationItemPickAllowedValueDetails(ConfigurationItemAllowedValueDetails):
    """
    Allowed value details of configuration item for PICK type. Value has to be from one of the possibleValues.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationItemPickAllowedValueDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.ConfigurationItemPickAllowedValueDetails.allowed_value_type` attribute
        of this class is ``PICK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allowed_value_type:
            The value to assign to the allowed_value_type property of this ConfigurationItemPickAllowedValueDetails.
            Allowed values for this property are: "LIMIT", "PICK", "FREE_TEXT"
        :type allowed_value_type: str

        :param possible_values:
            The value to assign to the possible_values property of this ConfigurationItemPickAllowedValueDetails.
        :type possible_values: list[str]

        """
        self.swagger_types = {
            'allowed_value_type': 'str',
            'possible_values': 'list[str]'
        }

        self.attribute_map = {
            'allowed_value_type': 'allowedValueType',
            'possible_values': 'possibleValues'
        }

        self._allowed_value_type = None
        self._possible_values = None
        self._allowed_value_type = 'PICK'

    @property
    def possible_values(self):
        """
        Gets the possible_values of this ConfigurationItemPickAllowedValueDetails.
        Allowed values to pick for the configuration item.


        :return: The possible_values of this ConfigurationItemPickAllowedValueDetails.
        :rtype: list[str]
        """
        return self._possible_values

    @possible_values.setter
    def possible_values(self, possible_values):
        """
        Sets the possible_values of this ConfigurationItemPickAllowedValueDetails.
        Allowed values to pick for the configuration item.


        :param possible_values: The possible_values of this ConfigurationItemPickAllowedValueDetails.
        :type: list[str]
        """
        self._possible_values = possible_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
