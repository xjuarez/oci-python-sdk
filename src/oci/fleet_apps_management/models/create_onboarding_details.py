# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOnboardingDetails(object):
    """
    The information about enabling onboarding.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOnboardingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOnboardingDetails.
        :type compartment_id: str

        :param is_fams_tag_enabled:
            The value to assign to the is_fams_tag_enabled property of this CreateOnboardingDetails.
        :type is_fams_tag_enabled: bool

        :param is_cost_tracking_tag_enabled:
            The value to assign to the is_cost_tracking_tag_enabled property of this CreateOnboardingDetails.
        :type is_cost_tracking_tag_enabled: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'is_fams_tag_enabled': 'bool',
            'is_cost_tracking_tag_enabled': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'is_fams_tag_enabled': 'isFamsTagEnabled',
            'is_cost_tracking_tag_enabled': 'isCostTrackingTagEnabled'
        }

        self._compartment_id = None
        self._is_fams_tag_enabled = None
        self._is_cost_tracking_tag_enabled = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOnboardingDetails.
        Tenancy OCID


        :return: The compartment_id of this CreateOnboardingDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOnboardingDetails.
        Tenancy OCID


        :param compartment_id: The compartment_id of this CreateOnboardingDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_fams_tag_enabled(self):
        """
        Gets the is_fams_tag_enabled of this CreateOnboardingDetails.
        A value determining if the Fleet Application Management tagging is enabled or not.
        Allow Fleet Application Management to tag resources with fleet name using \"Oracle$FAMS-Tags.FleetName\" tag.


        :return: The is_fams_tag_enabled of this CreateOnboardingDetails.
        :rtype: bool
        """
        return self._is_fams_tag_enabled

    @is_fams_tag_enabled.setter
    def is_fams_tag_enabled(self, is_fams_tag_enabled):
        """
        Sets the is_fams_tag_enabled of this CreateOnboardingDetails.
        A value determining if the Fleet Application Management tagging is enabled or not.
        Allow Fleet Application Management to tag resources with fleet name using \"Oracle$FAMS-Tags.FleetName\" tag.


        :param is_fams_tag_enabled: The is_fams_tag_enabled of this CreateOnboardingDetails.
        :type: bool
        """
        self._is_fams_tag_enabled = is_fams_tag_enabled

    @property
    def is_cost_tracking_tag_enabled(self):
        """
        Gets the is_cost_tracking_tag_enabled of this CreateOnboardingDetails.
        A value determining if the cost tracking tag is enabled or not.
        Allow Fleet Application Management to tag resources with cost tracking tag using \"Oracle$FAMS-Tags.FAMSManaged\" tag.


        :return: The is_cost_tracking_tag_enabled of this CreateOnboardingDetails.
        :rtype: bool
        """
        return self._is_cost_tracking_tag_enabled

    @is_cost_tracking_tag_enabled.setter
    def is_cost_tracking_tag_enabled(self, is_cost_tracking_tag_enabled):
        """
        Sets the is_cost_tracking_tag_enabled of this CreateOnboardingDetails.
        A value determining if the cost tracking tag is enabled or not.
        Allow Fleet Application Management to tag resources with cost tracking tag using \"Oracle$FAMS-Tags.FAMSManaged\" tag.


        :param is_cost_tracking_tag_enabled: The is_cost_tracking_tag_enabled of this CreateOnboardingDetails.
        :type: bool
        """
        self._is_cost_tracking_tag_enabled = is_cost_tracking_tag_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
