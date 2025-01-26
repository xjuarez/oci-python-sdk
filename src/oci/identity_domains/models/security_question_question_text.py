# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityQuestionQuestionText(object):
    """
    Locale values for the Question
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityQuestionQuestionText object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this SecurityQuestionQuestionText.
        :type value: str

        :param locale:
            The value to assign to the locale property of this SecurityQuestionQuestionText.
        :type locale: str

        :param default:
            The value to assign to the default property of this SecurityQuestionQuestionText.
        :type default: bool

        """
        self.swagger_types = {
            'value': 'str',
            'locale': 'str',
            'default': 'bool'
        }

        self.attribute_map = {
            'value': 'value',
            'locale': 'locale',
            'default': 'default'
        }

        self._value = None
        self._locale = None
        self._default = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SecurityQuestionQuestionText.
        The question text

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this SecurityQuestionQuestionText.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SecurityQuestionQuestionText.
        The question text

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this SecurityQuestionQuestionText.
        :type: str
        """
        self._value = value

    @property
    def locale(self):
        """
        **[Required]** Gets the locale of this SecurityQuestionQuestionText.
        The locale

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"locales\" and attrValues.value eq \"$(locale)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The locale of this SecurityQuestionQuestionText.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this SecurityQuestionQuestionText.
        The locale

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"locales\" and attrValues.value eq \"$(locale)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param locale: The locale of this SecurityQuestionQuestionText.
        :type: str
        """
        self._locale = locale

    @property
    def default(self):
        """
        Gets the default of this SecurityQuestionQuestionText.
        If true, specifies that the localized attribute instance value is the default and will be returned if no localized value found for requesting user's preferred locale. One and only one instance should have this attribute set to true.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The default of this SecurityQuestionQuestionText.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this SecurityQuestionQuestionText.
        If true, specifies that the localized attribute instance value is the default and will be returned if no localized value found for requesting user's preferred locale. One and only one instance should have this attribute set to true.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param default: The default of this SecurityQuestionQuestionText.
        :type: bool
        """
        self._default = default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
