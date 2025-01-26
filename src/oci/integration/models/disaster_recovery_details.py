# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisasterRecoveryDetails(object):
    """
    Disaster recovery details for the integration instance created in the region.
    """

    #: A constant which can be used with the role property of a DisasterRecoveryDetails.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a DisasterRecoveryDetails.
    #: This constant has a value of "SECONDARY"
    ROLE_SECONDARY = "SECONDARY"

    #: A constant which can be used with the role property of a DisasterRecoveryDetails.
    #: This constant has a value of "UNKNOWN"
    ROLE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new DisasterRecoveryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this DisasterRecoveryDetails.
            Allowed values for this property are: "PRIMARY", "SECONDARY", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param regional_instance_url:
            The value to assign to the regional_instance_url property of this DisasterRecoveryDetails.
        :type regional_instance_url: str

        :param cross_region_integration_instance_details:
            The value to assign to the cross_region_integration_instance_details property of this DisasterRecoveryDetails.
        :type cross_region_integration_instance_details: oci.integration.models.CrossRegionIntegrationInstanceDetails

        """
        self.swagger_types = {
            'role': 'str',
            'regional_instance_url': 'str',
            'cross_region_integration_instance_details': 'CrossRegionIntegrationInstanceDetails'
        }

        self.attribute_map = {
            'role': 'role',
            'regional_instance_url': 'regionalInstanceUrl',
            'cross_region_integration_instance_details': 'crossRegionIntegrationInstanceDetails'
        }

        self._role = None
        self._regional_instance_url = None
        self._cross_region_integration_instance_details = None

    @property
    def role(self):
        """
        **[Required]** Gets the role of this DisasterRecoveryDetails.
        Role of the integration instance in the region

        Allowed values for this property are: "PRIMARY", "SECONDARY", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this DisasterRecoveryDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DisasterRecoveryDetails.
        Role of the integration instance in the region


        :param role: The role of this DisasterRecoveryDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def regional_instance_url(self):
        """
        **[Required]** Gets the regional_instance_url of this DisasterRecoveryDetails.
        Region specific instance url for the integration instance in the region


        :return: The regional_instance_url of this DisasterRecoveryDetails.
        :rtype: str
        """
        return self._regional_instance_url

    @regional_instance_url.setter
    def regional_instance_url(self, regional_instance_url):
        """
        Sets the regional_instance_url of this DisasterRecoveryDetails.
        Region specific instance url for the integration instance in the region


        :param regional_instance_url: The regional_instance_url of this DisasterRecoveryDetails.
        :type: str
        """
        self._regional_instance_url = regional_instance_url

    @property
    def cross_region_integration_instance_details(self):
        """
        **[Required]** Gets the cross_region_integration_instance_details of this DisasterRecoveryDetails.

        :return: The cross_region_integration_instance_details of this DisasterRecoveryDetails.
        :rtype: oci.integration.models.CrossRegionIntegrationInstanceDetails
        """
        return self._cross_region_integration_instance_details

    @cross_region_integration_instance_details.setter
    def cross_region_integration_instance_details(self, cross_region_integration_instance_details):
        """
        Sets the cross_region_integration_instance_details of this DisasterRecoveryDetails.

        :param cross_region_integration_instance_details: The cross_region_integration_instance_details of this DisasterRecoveryDetails.
        :type: oci.integration.models.CrossRegionIntegrationInstanceDetails
        """
        self._cross_region_integration_instance_details = cross_region_integration_instance_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
