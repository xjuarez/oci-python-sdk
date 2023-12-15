# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppUserAssertionAttributes(object):
    """
    Each value of this attribute describes an attribute of User that will be sent in a Security Assertion Markup Language (SAML) assertion.

    **Deprecated Since: 18.2.2**

    **SCIM++ Properties:**
    - caseExact: false
    - idcsCompositeKey: [name]
    - idcsSearchable: false
    - idcsValuePersistedInOtherAttribute: true
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppUserAssertionAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AppUserAssertionAttributes.
        :type name: str

        :param user_store_attribute_name:
            The value to assign to the user_store_attribute_name property of this AppUserAssertionAttributes.
        :type user_store_attribute_name: str

        :param format:
            The value to assign to the format property of this AppUserAssertionAttributes.
        :type format: str

        """
        self.swagger_types = {
            'name': 'str',
            'user_store_attribute_name': 'str',
            'format': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'user_store_attribute_name': 'userStoreAttributeName',
            'format': 'format'
        }

        self._name = None
        self._user_store_attribute_name = None
        self._format = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AppUserAssertionAttributes.
        The attribute represents the name of the attribute that will be used in the Security Assertion Markup Language (SAML) assertion

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this AppUserAssertionAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppUserAssertionAttributes.
        The attribute represents the name of the attribute that will be used in the Security Assertion Markup Language (SAML) assertion

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this AppUserAssertionAttributes.
        :type: str
        """
        self._name = name

    @property
    def user_store_attribute_name(self):
        """
        **[Required]** Gets the user_store_attribute_name of this AppUserAssertionAttributes.
        This attribute specifies which user attribute should be used to create the value of the SAML assertion attribute. The userstore attribute can be constructed by using attributes from the Oracle Identity Cloud Service Core Users schema. <br><b>Note</b>: Attributes from extensions to the Core User schema are not supported in v1.0.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The user_store_attribute_name of this AppUserAssertionAttributes.
        :rtype: str
        """
        return self._user_store_attribute_name

    @user_store_attribute_name.setter
    def user_store_attribute_name(self, user_store_attribute_name):
        """
        Sets the user_store_attribute_name of this AppUserAssertionAttributes.
        This attribute specifies which user attribute should be used to create the value of the SAML assertion attribute. The userstore attribute can be constructed by using attributes from the Oracle Identity Cloud Service Core Users schema. <br><b>Note</b>: Attributes from extensions to the Core User schema are not supported in v1.0.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param user_store_attribute_name: The user_store_attribute_name of this AppUserAssertionAttributes.
        :type: str
        """
        self._user_store_attribute_name = user_store_attribute_name

    @property
    def format(self):
        """
        Gets the format of this AppUserAssertionAttributes.
        Indicates the format of the assertion attribute.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The format of this AppUserAssertionAttributes.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this AppUserAssertionAttributes.
        Indicates the format of the assertion attribute.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param format: The format of this AppUserAssertionAttributes.
        :type: str
        """
        self._format = format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
