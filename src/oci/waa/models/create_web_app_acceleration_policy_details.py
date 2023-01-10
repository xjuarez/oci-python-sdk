# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWebAppAccelerationPolicyDetails(object):
    """
    The information about new WebAppAccelerationPolicy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWebAppAccelerationPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateWebAppAccelerationPolicyDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateWebAppAccelerationPolicyDetails.
        :type compartment_id: str

        :param response_caching_policy:
            The value to assign to the response_caching_policy property of this CreateWebAppAccelerationPolicyDetails.
        :type response_caching_policy: oci.waa.models.ResponseCachingPolicy

        :param response_compression_policy:
            The value to assign to the response_compression_policy property of this CreateWebAppAccelerationPolicyDetails.
        :type response_compression_policy: oci.waa.models.ResponseCompressionPolicy

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWebAppAccelerationPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWebAppAccelerationPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateWebAppAccelerationPolicyDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'response_caching_policy': 'ResponseCachingPolicy',
            'response_compression_policy': 'ResponseCompressionPolicy',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'response_caching_policy': 'responseCachingPolicy',
            'response_compression_policy': 'responseCompressionPolicy',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._response_caching_policy = None
        self._response_compression_policy = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateWebAppAccelerationPolicyDetails.
        WebAppAccelerationPolicy display name, can be renamed.


        :return: The display_name of this CreateWebAppAccelerationPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateWebAppAccelerationPolicyDetails.
        WebAppAccelerationPolicy display name, can be renamed.


        :param display_name: The display_name of this CreateWebAppAccelerationPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateWebAppAccelerationPolicyDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateWebAppAccelerationPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateWebAppAccelerationPolicyDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateWebAppAccelerationPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def response_caching_policy(self):
        """
        Gets the response_caching_policy of this CreateWebAppAccelerationPolicyDetails.

        :return: The response_caching_policy of this CreateWebAppAccelerationPolicyDetails.
        :rtype: oci.waa.models.ResponseCachingPolicy
        """
        return self._response_caching_policy

    @response_caching_policy.setter
    def response_caching_policy(self, response_caching_policy):
        """
        Sets the response_caching_policy of this CreateWebAppAccelerationPolicyDetails.

        :param response_caching_policy: The response_caching_policy of this CreateWebAppAccelerationPolicyDetails.
        :type: oci.waa.models.ResponseCachingPolicy
        """
        self._response_caching_policy = response_caching_policy

    @property
    def response_compression_policy(self):
        """
        Gets the response_compression_policy of this CreateWebAppAccelerationPolicyDetails.

        :return: The response_compression_policy of this CreateWebAppAccelerationPolicyDetails.
        :rtype: oci.waa.models.ResponseCompressionPolicy
        """
        return self._response_compression_policy

    @response_compression_policy.setter
    def response_compression_policy(self, response_compression_policy):
        """
        Sets the response_compression_policy of this CreateWebAppAccelerationPolicyDetails.

        :param response_compression_policy: The response_compression_policy of this CreateWebAppAccelerationPolicyDetails.
        :type: oci.waa.models.ResponseCompressionPolicy
        """
        self._response_compression_policy = response_compression_policy

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateWebAppAccelerationPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateWebAppAccelerationPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateWebAppAccelerationPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateWebAppAccelerationPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateWebAppAccelerationPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateWebAppAccelerationPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateWebAppAccelerationPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateWebAppAccelerationPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateWebAppAccelerationPolicyDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CreateWebAppAccelerationPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateWebAppAccelerationPolicyDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CreateWebAppAccelerationPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
