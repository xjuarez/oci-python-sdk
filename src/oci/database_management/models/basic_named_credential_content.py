# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .named_credential_content import NamedCredentialContent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BasicNamedCredentialContent(NamedCredentialContent):
    """
    The details of the 'BASIC' named credential.
    """

    #: A constant which can be used with the role property of a BasicNamedCredentialContent.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a BasicNamedCredentialContent.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    #: A constant which can be used with the password_secret_access_mode property of a BasicNamedCredentialContent.
    #: This constant has a value of "USER_PRINCIPAL"
    PASSWORD_SECRET_ACCESS_MODE_USER_PRINCIPAL = "USER_PRINCIPAL"

    #: A constant which can be used with the password_secret_access_mode property of a BasicNamedCredentialContent.
    #: This constant has a value of "RESOURCE_PRINCIPAL"
    PASSWORD_SECRET_ACCESS_MODE_RESOURCE_PRINCIPAL = "RESOURCE_PRINCIPAL"

    def __init__(self, **kwargs):
        """
        Initializes a new BasicNamedCredentialContent object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.BasicNamedCredentialContent.credential_type` attribute
        of this class is ``BASIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this BasicNamedCredentialContent.
            Allowed values for this property are: "BASIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        :param user_name:
            The value to assign to the user_name property of this BasicNamedCredentialContent.
        :type user_name: str

        :param role:
            The value to assign to the role property of this BasicNamedCredentialContent.
            Allowed values for this property are: "NORMAL", "SYSDBA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this BasicNamedCredentialContent.
        :type password_secret_id: str

        :param password_secret_access_mode:
            The value to assign to the password_secret_access_mode property of this BasicNamedCredentialContent.
            Allowed values for this property are: "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type password_secret_access_mode: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'user_name': 'str',
            'role': 'str',
            'password_secret_id': 'str',
            'password_secret_access_mode': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType',
            'user_name': 'userName',
            'role': 'role',
            'password_secret_id': 'passwordSecretId',
            'password_secret_access_mode': 'passwordSecretAccessMode'
        }

        self._credential_type = None
        self._user_name = None
        self._role = None
        self._password_secret_id = None
        self._password_secret_access_mode = None
        self._credential_type = 'BASIC'

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this BasicNamedCredentialContent.
        The user name used to connect to the database.


        :return: The user_name of this BasicNamedCredentialContent.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this BasicNamedCredentialContent.
        The user name used to connect to the database.


        :param user_name: The user_name of this BasicNamedCredentialContent.
        :type: str
        """
        self._user_name = user_name

    @property
    def role(self):
        """
        **[Required]** Gets the role of this BasicNamedCredentialContent.
        The role of the database user.

        Allowed values for this property are: "NORMAL", "SYSDBA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this BasicNamedCredentialContent.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this BasicNamedCredentialContent.
        The role of the database user.


        :param role: The role of this BasicNamedCredentialContent.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def password_secret_id(self):
        """
        **[Required]** Gets the password_secret_id of this BasicNamedCredentialContent.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this BasicNamedCredentialContent.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this BasicNamedCredentialContent.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this BasicNamedCredentialContent.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def password_secret_access_mode(self):
        """
        **[Required]** Gets the password_secret_access_mode of this BasicNamedCredentialContent.
        The mechanism used to access the password plain text value.

        Allowed values for this property are: "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The password_secret_access_mode of this BasicNamedCredentialContent.
        :rtype: str
        """
        return self._password_secret_access_mode

    @password_secret_access_mode.setter
    def password_secret_access_mode(self, password_secret_access_mode):
        """
        Sets the password_secret_access_mode of this BasicNamedCredentialContent.
        The mechanism used to access the password plain text value.


        :param password_secret_access_mode: The password_secret_access_mode of this BasicNamedCredentialContent.
        :type: str
        """
        allowed_values = ["USER_PRINCIPAL", "RESOURCE_PRINCIPAL"]
        if not value_allowed_none_or_none_sentinel(password_secret_access_mode, allowed_values):
            password_secret_access_mode = 'UNKNOWN_ENUM_VALUE'
        self._password_secret_access_mode = password_secret_access_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
