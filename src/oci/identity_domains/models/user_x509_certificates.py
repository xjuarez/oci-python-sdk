# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserX509Certificates(object):
    """
    A list of certificates issued to the User.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserX509Certificates object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserX509Certificates.
        :type value: object

        :param display:
            The value to assign to the display property of this UserX509Certificates.
        :type display: str

        :param type:
            The value to assign to the type property of this UserX509Certificates.
        :type type: str

        :param primary:
            The value to assign to the primary property of this UserX509Certificates.
        :type primary: bool

        """
        self.swagger_types = {
            'value': 'object',
            'display': 'str',
            'type': 'str',
            'primary': 'bool'
        }

        self.attribute_map = {
            'value': 'value',
            'display': 'display',
            'type': 'type',
            'primary': 'primary'
        }

        self._value = None
        self._display = None
        self._type = None
        self._primary = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserX509Certificates.
        The value of a X509 certificate.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: binary
         - uniqueness: none


        :return: The value of this UserX509Certificates.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserX509Certificates.
        The value of a X509 certificate.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: binary
         - uniqueness: none


        :param value: The value of this UserX509Certificates.
        :type: object
        """
        self._value = value

    @property
    def display(self):
        """
        Gets the display of this UserX509Certificates.
        A human readable name, primarily used for display purposes.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this UserX509Certificates.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this UserX509Certificates.
        A human readable name, primarily used for display purposes.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this UserX509Certificates.
        :type: str
        """
        self._display = display

    @property
    def type(self):
        """
        Gets the type of this UserX509Certificates.
        A label indicating the attribute's function.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The type of this UserX509Certificates.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserX509Certificates.
        A label indicating the attribute's function.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this UserX509Certificates.
        :type: str
        """
        self._type = type

    @property
    def primary(self):
        """
        Gets the primary of this UserX509Certificates.
        A Boolean value indicating the 'primary' or preferred attribute value for this attribute. The primary attribute value 'true' MUST appear no more than once.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The primary of this UserX509Certificates.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """
        Sets the primary of this UserX509Certificates.
        A Boolean value indicating the 'primary' or preferred attribute value for this attribute. The primary attribute value 'true' MUST appear no more than once.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param primary: The primary of this UserX509Certificates.
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
