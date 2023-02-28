# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFusionEnvironmentFamilyDetails(object):
    """
    The information about new FusionEnvironmentFamily.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFusionEnvironmentFamilyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateFusionEnvironmentFamilyDetails.
        :type display_name: str

        :param family_maintenance_policy:
            The value to assign to the family_maintenance_policy property of this CreateFusionEnvironmentFamilyDetails.
        :type family_maintenance_policy: oci.fusion_apps.models.FamilyMaintenancePolicy

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateFusionEnvironmentFamilyDetails.
        :type compartment_id: str

        :param subscription_ids:
            The value to assign to the subscription_ids property of this CreateFusionEnvironmentFamilyDetails.
        :type subscription_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFusionEnvironmentFamilyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFusionEnvironmentFamilyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'family_maintenance_policy': 'FamilyMaintenancePolicy',
            'compartment_id': 'str',
            'subscription_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'family_maintenance_policy': 'familyMaintenancePolicy',
            'compartment_id': 'compartmentId',
            'subscription_ids': 'subscriptionIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._family_maintenance_policy = None
        self._compartment_id = None
        self._subscription_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateFusionEnvironmentFamilyDetails.
        A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.


        :return: The display_name of this CreateFusionEnvironmentFamilyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateFusionEnvironmentFamilyDetails.
        A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.


        :param display_name: The display_name of this CreateFusionEnvironmentFamilyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def family_maintenance_policy(self):
        """
        Gets the family_maintenance_policy of this CreateFusionEnvironmentFamilyDetails.

        :return: The family_maintenance_policy of this CreateFusionEnvironmentFamilyDetails.
        :rtype: oci.fusion_apps.models.FamilyMaintenancePolicy
        """
        return self._family_maintenance_policy

    @family_maintenance_policy.setter
    def family_maintenance_policy(self, family_maintenance_policy):
        """
        Sets the family_maintenance_policy of this CreateFusionEnvironmentFamilyDetails.

        :param family_maintenance_policy: The family_maintenance_policy of this CreateFusionEnvironmentFamilyDetails.
        :type: oci.fusion_apps.models.FamilyMaintenancePolicy
        """
        self._family_maintenance_policy = family_maintenance_policy

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateFusionEnvironmentFamilyDetails.
        The OCID of the compartment where the environment family is located.


        :return: The compartment_id of this CreateFusionEnvironmentFamilyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateFusionEnvironmentFamilyDetails.
        The OCID of the compartment where the environment family is located.


        :param compartment_id: The compartment_id of this CreateFusionEnvironmentFamilyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subscription_ids(self):
        """
        **[Required]** Gets the subscription_ids of this CreateFusionEnvironmentFamilyDetails.
        The list of the IDs of the applications subscriptions that are associated with the environment family.


        :return: The subscription_ids of this CreateFusionEnvironmentFamilyDetails.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """
        Sets the subscription_ids of this CreateFusionEnvironmentFamilyDetails.
        The list of the IDs of the applications subscriptions that are associated with the environment family.


        :param subscription_ids: The subscription_ids of this CreateFusionEnvironmentFamilyDetails.
        :type: list[str]
        """
        self._subscription_ids = subscription_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateFusionEnvironmentFamilyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateFusionEnvironmentFamilyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateFusionEnvironmentFamilyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateFusionEnvironmentFamilyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateFusionEnvironmentFamilyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateFusionEnvironmentFamilyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateFusionEnvironmentFamilyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateFusionEnvironmentFamilyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
