# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRemediationRunDetails(object):
    """
    Details to create a new remediation run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRemediationRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param remediation_recipe_id:
            The value to assign to the remediation_recipe_id property of this CreateRemediationRunDetails.
        :type remediation_recipe_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateRemediationRunDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRemediationRunDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRemediationRunDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'remediation_recipe_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'remediation_recipe_id': 'remediationRecipeId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._remediation_recipe_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def remediation_recipe_id(self):
        """
        **[Required]** Gets the remediation_recipe_id of this CreateRemediationRunDetails.
        The Oracle Cloud identifier (`OCID`__) of the Remediation Recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The remediation_recipe_id of this CreateRemediationRunDetails.
        :rtype: str
        """
        return self._remediation_recipe_id

    @remediation_recipe_id.setter
    def remediation_recipe_id(self, remediation_recipe_id):
        """
        Sets the remediation_recipe_id of this CreateRemediationRunDetails.
        The Oracle Cloud identifier (`OCID`__) of the Remediation Recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param remediation_recipe_id: The remediation_recipe_id of this CreateRemediationRunDetails.
        :type: str
        """
        self._remediation_recipe_id = remediation_recipe_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRemediationRunDetails.
        The name of the remediation run.


        :return: The display_name of this CreateRemediationRunDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRemediationRunDetails.
        The name of the remediation run.


        :param display_name: The display_name of this CreateRemediationRunDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRemediationRunDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateRemediationRunDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRemediationRunDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateRemediationRunDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRemediationRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateRemediationRunDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRemediationRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateRemediationRunDetails.
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
