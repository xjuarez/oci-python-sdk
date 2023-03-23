# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Addresses(object):
    """
    A physical mailing address for this User, as described in (address Element). Canonical Type Values of work, home, and other. The value attribute is a complex type with the following sub-attributes.
    """

    #: A constant which can be used with the type property of a Addresses.
    #: This constant has a value of "work"
    TYPE_WORK = "work"

    #: A constant which can be used with the type property of a Addresses.
    #: This constant has a value of "home"
    TYPE_HOME = "home"

    #: A constant which can be used with the type property of a Addresses.
    #: This constant has a value of "other"
    TYPE_OTHER = "other"

    def __init__(self, **kwargs):
        """
        Initializes a new Addresses object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param formatted:
            The value to assign to the formatted property of this Addresses.
        :type formatted: str

        :param street_address:
            The value to assign to the street_address property of this Addresses.
        :type street_address: str

        :param locality:
            The value to assign to the locality property of this Addresses.
        :type locality: str

        :param region:
            The value to assign to the region property of this Addresses.
        :type region: str

        :param postal_code:
            The value to assign to the postal_code property of this Addresses.
        :type postal_code: str

        :param country:
            The value to assign to the country property of this Addresses.
        :type country: str

        :param type:
            The value to assign to the type property of this Addresses.
            Allowed values for this property are: "work", "home", "other", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param primary:
            The value to assign to the primary property of this Addresses.
        :type primary: bool

        """
        self.swagger_types = {
            'formatted': 'str',
            'street_address': 'str',
            'locality': 'str',
            'region': 'str',
            'postal_code': 'str',
            'country': 'str',
            'type': 'str',
            'primary': 'bool'
        }

        self.attribute_map = {
            'formatted': 'formatted',
            'street_address': 'streetAddress',
            'locality': 'locality',
            'region': 'region',
            'postal_code': 'postalCode',
            'country': 'country',
            'type': 'type',
            'primary': 'primary'
        }

        self._formatted = None
        self._street_address = None
        self._locality = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._type = None
        self._primary = None

    @property
    def formatted(self):
        """
        Gets the formatted of this Addresses.
        The full mailing address, formatted for display or use with a mailing label. This attribute MAY contain newlines.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The formatted of this Addresses.
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        """
        Sets the formatted of this Addresses.
        The full mailing address, formatted for display or use with a mailing label. This attribute MAY contain newlines.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param formatted: The formatted of this Addresses.
        :type: str
        """
        self._formatted = formatted

    @property
    def street_address(self):
        """
        Gets the street_address of this Addresses.
        The full street address component, which may include house number, street name, PO BOX, and multi-line extended street address information. This attribute MAY contain newlines.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The street_address of this Addresses.
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """
        Sets the street_address of this Addresses.
        The full street address component, which may include house number, street name, PO BOX, and multi-line extended street address information. This attribute MAY contain newlines.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param street_address: The street_address of this Addresses.
        :type: str
        """
        self._street_address = street_address

    @property
    def locality(self):
        """
        Gets the locality of this Addresses.
        The city or locality component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The locality of this Addresses.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Addresses.
        The city or locality component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param locality: The locality of this Addresses.
        :type: str
        """
        self._locality = locality

    @property
    def region(self):
        """
        Gets the region of this Addresses.
        The state or region component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The region of this Addresses.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Addresses.
        The state or region component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param region: The region of this Addresses.
        :type: str
        """
        self._region = region

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Addresses.
        The zipcode or postal code component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The postal_code of this Addresses.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Addresses.
        The zipcode or postal code component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param postal_code: The postal_code of this Addresses.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Addresses.
        The country name component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"countries\" and attrValues.value eq \"upper($(country))\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The country of this Addresses.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Addresses.
        The country name component.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"countries\" and attrValues.value eq \"upper($(country))\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param country: The country of this Addresses.
        :type: str
        """
        self._country = country

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Addresses.
        A label indicating the attribute's function; e.g., 'work' or 'home'.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "work", "home", "other", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Addresses.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Addresses.
        A label indicating the attribute's function; e.g., 'work' or 'home'.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this Addresses.
        :type: str
        """
        allowed_values = ["work", "home", "other"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def primary(self):
        """
        Gets the primary of this Addresses.
        A Boolean value indicating the 'primary' or preferred attribute value for this attribute. The primary attribute value 'true' MUST appear no more than once.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The primary of this Addresses.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """
        Sets the primary of this Addresses.
        A Boolean value indicating the 'primary' or preferred attribute value for this attribute. The primary attribute value 'true' MUST appear no more than once.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param primary: The primary of this Addresses.
        :type: bool
        """
        self._primary = primary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
