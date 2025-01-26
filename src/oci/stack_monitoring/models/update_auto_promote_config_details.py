# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from .update_config_details import UpdateConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutoPromoteConfigDetails(UpdateConfigDetails):
    """
    Change the details of an AUTO_PROMOTE config
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutoPromoteConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.UpdateAutoPromoteConfigDetails.config_type` attribute
        of this class is ``AUTO_PROMOTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAutoPromoteConfigDetails.
        :type display_name: str

        :param config_type:
            The value to assign to the config_type property of this UpdateAutoPromoteConfigDetails.
        :type config_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAutoPromoteConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAutoPromoteConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateAutoPromoteConfigDetails.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'config_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'config_type': 'configType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_enabled': 'isEnabled'
        }

        self._display_name = None
        self._config_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_enabled = None
        self._config_type = 'AUTO_PROMOTE'

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateAutoPromoteConfigDetails.
        True if automatic promotion is enabled, false if it is not enabled.


        :return: The is_enabled of this UpdateAutoPromoteConfigDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateAutoPromoteConfigDetails.
        True if automatic promotion is enabled, false if it is not enabled.


        :param is_enabled: The is_enabled of this UpdateAutoPromoteConfigDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
