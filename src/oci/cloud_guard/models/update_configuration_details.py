# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConfigurationDetails(object):
    """
    Update cloud guard configuration details for a tenancy.
    """

    #: A constant which can be used with the status property of a UpdateConfigurationDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateConfigurationDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reporting_region:
            The value to assign to the reporting_region property of this UpdateConfigurationDetails.
        :type reporting_region: str

        :param status:
            The value to assign to the status property of this UpdateConfigurationDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type status: str

        :param self_manage_resources:
            The value to assign to the self_manage_resources property of this UpdateConfigurationDetails.
        :type self_manage_resources: bool

        """
        self.swagger_types = {
            'reporting_region': 'str',
            'status': 'str',
            'self_manage_resources': 'bool'
        }

        self.attribute_map = {
            'reporting_region': 'reportingRegion',
            'status': 'status',
            'self_manage_resources': 'selfManageResources'
        }

        self._reporting_region = None
        self._status = None
        self._self_manage_resources = None

    @property
    def reporting_region(self):
        """
        **[Required]** Gets the reporting_region of this UpdateConfigurationDetails.
        The reporting region value


        :return: The reporting_region of this UpdateConfigurationDetails.
        :rtype: str
        """
        return self._reporting_region

    @reporting_region.setter
    def reporting_region(self, reporting_region):
        """
        Sets the reporting_region of this UpdateConfigurationDetails.
        The reporting region value


        :param reporting_region: The reporting_region of this UpdateConfigurationDetails.
        :type: str
        """
        self._reporting_region = reporting_region

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateConfigurationDetails.
        Status of Cloud Guard Tenant

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The status of this UpdateConfigurationDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateConfigurationDetails.
        Status of Cloud Guard Tenant


        :param status: The status of this UpdateConfigurationDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def self_manage_resources(self):
        """
        Gets the self_manage_resources of this UpdateConfigurationDetails.
        Identifies if Oracle managed resources will be created by customers.
        If no value is specified false is the default.


        :return: The self_manage_resources of this UpdateConfigurationDetails.
        :rtype: bool
        """
        return self._self_manage_resources

    @self_manage_resources.setter
    def self_manage_resources(self, self_manage_resources):
        """
        Sets the self_manage_resources of this UpdateConfigurationDetails.
        Identifies if Oracle managed resources will be created by customers.
        If no value is specified false is the default.


        :param self_manage_resources: The self_manage_resources of this UpdateConfigurationDetails.
        :type: bool
        """
        self._self_manage_resources = self_manage_resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
