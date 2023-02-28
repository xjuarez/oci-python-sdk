# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_connection_credentials import DatabaseConnectionCredentials
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseSslConnectionCredentials(DatabaseConnectionCredentials):
    """
    The SSL connection credential details used to connect to the database.
    """

    #: A constant which can be used with the role property of a DatabaseSslConnectionCredentials.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    #: A constant which can be used with the role property of a DatabaseSslConnectionCredentials.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseSslConnectionCredentials object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DatabaseSslConnectionCredentials.credential_type` attribute
        of this class is ``SSL_DETAILS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this DatabaseSslConnectionCredentials.
            Allowed values for this property are: "NAME_REFERENCE", "DETAILS", "SSL_DETAILS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        :param credential_name:
            The value to assign to the credential_name property of this DatabaseSslConnectionCredentials.
        :type credential_name: str

        :param user_name:
            The value to assign to the user_name property of this DatabaseSslConnectionCredentials.
        :type user_name: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this DatabaseSslConnectionCredentials.
        :type password_secret_id: str

        :param role:
            The value to assign to the role property of this DatabaseSslConnectionCredentials.
            Allowed values for this property are: "SYSDBA", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param ssl_secret_id:
            The value to assign to the ssl_secret_id property of this DatabaseSslConnectionCredentials.
        :type ssl_secret_id: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'credential_name': 'str',
            'user_name': 'str',
            'password_secret_id': 'str',
            'role': 'str',
            'ssl_secret_id': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType',
            'credential_name': 'credentialName',
            'user_name': 'userName',
            'password_secret_id': 'passwordSecretId',
            'role': 'role',
            'ssl_secret_id': 'sslSecretId'
        }

        self._credential_type = None
        self._credential_name = None
        self._user_name = None
        self._password_secret_id = None
        self._role = None
        self._ssl_secret_id = None
        self._credential_type = 'SSL_DETAILS'

    @property
    def credential_name(self):
        """
        Gets the credential_name of this DatabaseSslConnectionCredentials.
        The name of the credential information that used to connect to the DB system resource.
        The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters,
        and length of \"y\" has a maximum of 199 characters. The name strings can contain letters,
        numbers and the underscore character only. Other characters are not valid, except for
        the \".\" character that separates the \"x\" and \"y\" portions of the name.
        *IMPORTANT* - The name must be unique within the OCI region the credential is being created in.
        If you specify a name that duplicates the name of another credential within the same OCI region,
        you may overwrite or corrupt the credential that is already using the name.

        For example: inventorydb.abc112233445566778899


        :return: The credential_name of this DatabaseSslConnectionCredentials.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this DatabaseSslConnectionCredentials.
        The name of the credential information that used to connect to the DB system resource.
        The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters,
        and length of \"y\" has a maximum of 199 characters. The name strings can contain letters,
        numbers and the underscore character only. Other characters are not valid, except for
        the \".\" character that separates the \"x\" and \"y\" portions of the name.
        *IMPORTANT* - The name must be unique within the OCI region the credential is being created in.
        If you specify a name that duplicates the name of another credential within the same OCI region,
        you may overwrite or corrupt the credential that is already using the name.

        For example: inventorydb.abc112233445566778899


        :param credential_name: The credential_name of this DatabaseSslConnectionCredentials.
        :type: str
        """
        self._credential_name = credential_name

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this DatabaseSslConnectionCredentials.
        The user name used to connect to the database.


        :return: The user_name of this DatabaseSslConnectionCredentials.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DatabaseSslConnectionCredentials.
        The user name used to connect to the database.


        :param user_name: The user_name of this DatabaseSslConnectionCredentials.
        :type: str
        """
        self._user_name = user_name

    @property
    def password_secret_id(self):
        """
        **[Required]** Gets the password_secret_id of this DatabaseSslConnectionCredentials.
        The `OCID`__ of the secret containing the user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this DatabaseSslConnectionCredentials.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this DatabaseSslConnectionCredentials.
        The `OCID`__ of the secret containing the user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this DatabaseSslConnectionCredentials.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def role(self):
        """
        **[Required]** Gets the role of this DatabaseSslConnectionCredentials.
        The role of the user connecting to the database.

        Allowed values for this property are: "SYSDBA", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this DatabaseSslConnectionCredentials.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DatabaseSslConnectionCredentials.
        The role of the user connecting to the database.


        :param role: The role of this DatabaseSslConnectionCredentials.
        :type: str
        """
        allowed_values = ["SYSDBA", "NORMAL"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def ssl_secret_id(self):
        """
        **[Required]** Gets the ssl_secret_id of this DatabaseSslConnectionCredentials.
        The `OCID`__ of the secret containing the SSL keystore and truststore details.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The ssl_secret_id of this DatabaseSslConnectionCredentials.
        :rtype: str
        """
        return self._ssl_secret_id

    @ssl_secret_id.setter
    def ssl_secret_id(self, ssl_secret_id):
        """
        Sets the ssl_secret_id of this DatabaseSslConnectionCredentials.
        The `OCID`__ of the secret containing the SSL keystore and truststore details.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param ssl_secret_id: The ssl_secret_id of this DatabaseSslConnectionCredentials.
        :type: str
        """
        self._ssl_secret_id = ssl_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
