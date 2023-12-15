# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppRoleMembers(object):
    """
    AppRole members - when requesting members attribute, it is recommended to use startIndex and count to return members in pages instead of in a single response, eg : #attributes=members[startIndex=1%26count=10]
    """

    #: A constant which can be used with the type property of a AppRoleMembers.
    #: This constant has a value of "User"
    TYPE_USER = "User"

    #: A constant which can be used with the type property of a AppRoleMembers.
    #: This constant has a value of "Group"
    TYPE_GROUP = "Group"

    #: A constant which can be used with the type property of a AppRoleMembers.
    #: This constant has a value of "DynamicResourceGroup"
    TYPE_DYNAMIC_RESOURCE_GROUP = "DynamicResourceGroup"

    def __init__(self, **kwargs):
        """
        Initializes a new AppRoleMembers object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppRoleMembers.
        :type value: str

        :param ref:
            The value to assign to the ref property of this AppRoleMembers.
        :type ref: str

        :param display:
            The value to assign to the display property of this AppRoleMembers.
        :type display: str

        :param type:
            The value to assign to the type property of this AppRoleMembers.
            Allowed values for this property are: "User", "Group", "DynamicResourceGroup", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'type': 'type'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._type = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AppRoleMembers.
        ID of the member of this AppRole

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: Member
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this AppRoleMembers.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppRoleMembers.
        ID of the member of this AppRole

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: Member
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this AppRoleMembers.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this AppRoleMembers.
        The URI corresponding to the member Resource of this Group

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AppRoleMembers.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AppRoleMembers.
        The URI corresponding to the member Resource of this Group

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AppRoleMembers.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this AppRoleMembers.
        Member display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this AppRoleMembers.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this AppRoleMembers.
        Member display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this AppRoleMembers.
        :type: str
        """
        self._display = display

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AppRoleMembers.
        Indicates the type of Resource--for example, User, Group or DynamicResourceGroup

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: Member Type
         - idcsDefaultValue: User
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "User", "Group", "DynamicResourceGroup", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AppRoleMembers.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AppRoleMembers.
        Indicates the type of Resource--for example, User, Group or DynamicResourceGroup

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: Member Type
         - idcsDefaultValue: User
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this AppRoleMembers.
        :type: str
        """
        allowed_values = ["User", "Group", "DynamicResourceGroup"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
