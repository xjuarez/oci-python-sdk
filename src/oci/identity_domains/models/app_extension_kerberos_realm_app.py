# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppExtensionKerberosRealmApp(object):
    """
    Kerberos Realm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppExtensionKerberosRealmApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param realm_name:
            The value to assign to the realm_name property of this AppExtensionKerberosRealmApp.
        :type realm_name: str

        :param master_key:
            The value to assign to the master_key property of this AppExtensionKerberosRealmApp.
        :type master_key: str

        :param default_encryption_salt_type:
            The value to assign to the default_encryption_salt_type property of this AppExtensionKerberosRealmApp.
        :type default_encryption_salt_type: str

        :param supported_encryption_salt_types:
            The value to assign to the supported_encryption_salt_types property of this AppExtensionKerberosRealmApp.
        :type supported_encryption_salt_types: list[str]

        :param ticket_flags:
            The value to assign to the ticket_flags property of this AppExtensionKerberosRealmApp.
        :type ticket_flags: int

        :param max_ticket_life:
            The value to assign to the max_ticket_life property of this AppExtensionKerberosRealmApp.
        :type max_ticket_life: int

        :param max_renewable_age:
            The value to assign to the max_renewable_age property of this AppExtensionKerberosRealmApp.
        :type max_renewable_age: int

        """
        self.swagger_types = {
            'realm_name': 'str',
            'master_key': 'str',
            'default_encryption_salt_type': 'str',
            'supported_encryption_salt_types': 'list[str]',
            'ticket_flags': 'int',
            'max_ticket_life': 'int',
            'max_renewable_age': 'int'
        }

        self.attribute_map = {
            'realm_name': 'realmName',
            'master_key': 'masterKey',
            'default_encryption_salt_type': 'defaultEncryptionSaltType',
            'supported_encryption_salt_types': 'supportedEncryptionSaltTypes',
            'ticket_flags': 'ticketFlags',
            'max_ticket_life': 'maxTicketLife',
            'max_renewable_age': 'maxRenewableAge'
        }

        self._realm_name = None
        self._master_key = None
        self._default_encryption_salt_type = None
        self._supported_encryption_salt_types = None
        self._ticket_flags = None
        self._max_ticket_life = None
        self._max_renewable_age = None

    @property
    def realm_name(self):
        """
        Gets the realm_name of this AppExtensionKerberosRealmApp.
        The name of the Kerberos Realm that this App uses for authentication.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The realm_name of this AppExtensionKerberosRealmApp.
        :rtype: str
        """
        return self._realm_name

    @realm_name.setter
    def realm_name(self, realm_name):
        """
        Sets the realm_name of this AppExtensionKerberosRealmApp.
        The name of the Kerberos Realm that this App uses for authentication.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param realm_name: The realm_name of this AppExtensionKerberosRealmApp.
        :type: str
        """
        self._realm_name = realm_name

    @property
    def master_key(self):
        """
        Gets the master_key of this AppExtensionKerberosRealmApp.
        The primary key that the system should use to encrypt artifacts that are specific to this Kerberos realm -- for example, to encrypt the Principal Key in each KerberosRealmUser.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The master_key of this AppExtensionKerberosRealmApp.
        :rtype: str
        """
        return self._master_key

    @master_key.setter
    def master_key(self, master_key):
        """
        Sets the master_key of this AppExtensionKerberosRealmApp.
        The primary key that the system should use to encrypt artifacts that are specific to this Kerberos realm -- for example, to encrypt the Principal Key in each KerberosRealmUser.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param master_key: The master_key of this AppExtensionKerberosRealmApp.
        :type: str
        """
        self._master_key = master_key

    @property
    def default_encryption_salt_type(self):
        """
        Gets the default_encryption_salt_type of this AppExtensionKerberosRealmApp.
        The type of salt that the system will use to encrypt Kerberos-specific artifacts of this App unless another type of salt is specified.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The default_encryption_salt_type of this AppExtensionKerberosRealmApp.
        :rtype: str
        """
        return self._default_encryption_salt_type

    @default_encryption_salt_type.setter
    def default_encryption_salt_type(self, default_encryption_salt_type):
        """
        Sets the default_encryption_salt_type of this AppExtensionKerberosRealmApp.
        The type of salt that the system will use to encrypt Kerberos-specific artifacts of this App unless another type of salt is specified.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param default_encryption_salt_type: The default_encryption_salt_type of this AppExtensionKerberosRealmApp.
        :type: str
        """
        self._default_encryption_salt_type = default_encryption_salt_type

    @property
    def supported_encryption_salt_types(self):
        """
        Gets the supported_encryption_salt_types of this AppExtensionKerberosRealmApp.
        The types of salt that are available for the system to use when encrypting Kerberos-specific artifacts for this App.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The supported_encryption_salt_types of this AppExtensionKerberosRealmApp.
        :rtype: list[str]
        """
        return self._supported_encryption_salt_types

    @supported_encryption_salt_types.setter
    def supported_encryption_salt_types(self, supported_encryption_salt_types):
        """
        Sets the supported_encryption_salt_types of this AppExtensionKerberosRealmApp.
        The types of salt that are available for the system to use when encrypting Kerberos-specific artifacts for this App.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param supported_encryption_salt_types: The supported_encryption_salt_types of this AppExtensionKerberosRealmApp.
        :type: list[str]
        """
        self._supported_encryption_salt_types = supported_encryption_salt_types

    @property
    def ticket_flags(self):
        """
        Gets the ticket_flags of this AppExtensionKerberosRealmApp.
        Ticket Flags

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :return: The ticket_flags of this AppExtensionKerberosRealmApp.
        :rtype: int
        """
        return self._ticket_flags

    @ticket_flags.setter
    def ticket_flags(self, ticket_flags):
        """
        Sets the ticket_flags of this AppExtensionKerberosRealmApp.
        Ticket Flags

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :param ticket_flags: The ticket_flags of this AppExtensionKerberosRealmApp.
        :type: int
        """
        self._ticket_flags = ticket_flags

    @property
    def max_ticket_life(self):
        """
        Gets the max_ticket_life of this AppExtensionKerberosRealmApp.
        Max Ticket Life in seconds

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :return: The max_ticket_life of this AppExtensionKerberosRealmApp.
        :rtype: int
        """
        return self._max_ticket_life

    @max_ticket_life.setter
    def max_ticket_life(self, max_ticket_life):
        """
        Sets the max_ticket_life of this AppExtensionKerberosRealmApp.
        Max Ticket Life in seconds

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :param max_ticket_life: The max_ticket_life of this AppExtensionKerberosRealmApp.
        :type: int
        """
        self._max_ticket_life = max_ticket_life

    @property
    def max_renewable_age(self):
        """
        Gets the max_renewable_age of this AppExtensionKerberosRealmApp.
        Max Renewable Age in seconds

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :return: The max_renewable_age of this AppExtensionKerberosRealmApp.
        :rtype: int
        """
        return self._max_renewable_age

    @max_renewable_age.setter
    def max_renewable_age(self, max_renewable_age):
        """
        Sets the max_renewable_age of this AppExtensionKerberosRealmApp.
        Max Renewable Age in seconds

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :param max_renewable_age: The max_renewable_age of this AppExtensionKerberosRealmApp.
        :type: int
        """
        self._max_renewable_age = max_renewable_age

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
