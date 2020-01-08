# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchInstanceAgentConfigDetails(object):
    """
    Instance agent configuration options to choose for launching the instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchInstanceAgentConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_monitoring_disabled:
            The value to assign to the is_monitoring_disabled property of this LaunchInstanceAgentConfigDetails.
        :type is_monitoring_disabled: bool

        :param is_management_disabled:
            The value to assign to the is_management_disabled property of this LaunchInstanceAgentConfigDetails.
        :type is_management_disabled: bool

        """
        self.swagger_types = {
            'is_monitoring_disabled': 'bool',
            'is_management_disabled': 'bool'
        }

        self.attribute_map = {
            'is_monitoring_disabled': 'isMonitoringDisabled',
            'is_management_disabled': 'isManagementDisabled'
        }

        self._is_monitoring_disabled = None
        self._is_management_disabled = None

    @property
    def is_monitoring_disabled(self):
        """
        Gets the is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        Whether the agent running on the instance can gather performance metrics and monitor the instance.
        Default value is false.


        :return: The is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        :rtype: bool
        """
        return self._is_monitoring_disabled

    @is_monitoring_disabled.setter
    def is_monitoring_disabled(self, is_monitoring_disabled):
        """
        Sets the is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        Whether the agent running on the instance can gather performance metrics and monitor the instance.
        Default value is false.


        :param is_monitoring_disabled: The is_monitoring_disabled of this LaunchInstanceAgentConfigDetails.
        :type: bool
        """
        self._is_monitoring_disabled = is_monitoring_disabled

    @property
    def is_management_disabled(self):
        """
        Gets the is_management_disabled of this LaunchInstanceAgentConfigDetails.
        Whether the agent running on the instance can run all the available management plugins.
        Default value is false.


        :return: The is_management_disabled of this LaunchInstanceAgentConfigDetails.
        :rtype: bool
        """
        return self._is_management_disabled

    @is_management_disabled.setter
    def is_management_disabled(self, is_management_disabled):
        """
        Sets the is_management_disabled of this LaunchInstanceAgentConfigDetails.
        Whether the agent running on the instance can run all the available management plugins.
        Default value is false.


        :param is_management_disabled: The is_management_disabled of this LaunchInstanceAgentConfigDetails.
        :type: bool
        """
        self._is_management_disabled = is_management_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
