# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215

from .outbound_connector import OutboundConnector
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LdapBindAccount(OutboundConnector):
    """
    Account details for the LDAP bind account used by the outbound connector.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LdapBindAccount object with values from keyword arguments. The default value of the :py:attr:`~oci.file_storage.models.LdapBindAccount.connector_type` attribute
        of this class is ``LDAPBIND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this LdapBindAccount.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LdapBindAccount.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this LdapBindAccount.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LdapBindAccount.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED"
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this LdapBindAccount.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this LdapBindAccount.
        :type time_created: datetime

        :param connector_type:
            The value to assign to the connector_type property of this LdapBindAccount.
            Allowed values for this property are: "LDAPBIND"
        :type connector_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LdapBindAccount.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LdapBindAccount.
        :type defined_tags: dict(str, dict(str, object))

        :param endpoints:
            The value to assign to the endpoints property of this LdapBindAccount.
        :type endpoints: list[oci.file_storage.models.Endpoint]

        :param bind_distinguished_name:
            The value to assign to the bind_distinguished_name property of this LdapBindAccount.
        :type bind_distinguished_name: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this LdapBindAccount.
        :type password_secret_id: str

        :param password_secret_version:
            The value to assign to the password_secret_version property of this LdapBindAccount.
        :type password_secret_version: int

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'connector_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'endpoints': 'list[Endpoint]',
            'bind_distinguished_name': 'str',
            'password_secret_id': 'str',
            'password_secret_version': 'int'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'connector_type': 'connectorType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'endpoints': 'endpoints',
            'bind_distinguished_name': 'bindDistinguishedName',
            'password_secret_id': 'passwordSecretId',
            'password_secret_version': 'passwordSecretVersion'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._id = None
        self._lifecycle_state = None
        self._display_name = None
        self._time_created = None
        self._connector_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._endpoints = None
        self._bind_distinguished_name = None
        self._password_secret_id = None
        self._password_secret_version = None
        self._connector_type = 'LDAPBIND'

    @property
    def endpoints(self):
        """
        **[Required]** Gets the endpoints of this LdapBindAccount.
        Array of server endpoints to use when connecting with the LDAP bind account.


        :return: The endpoints of this LdapBindAccount.
        :rtype: list[oci.file_storage.models.Endpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this LdapBindAccount.
        Array of server endpoints to use when connecting with the LDAP bind account.


        :param endpoints: The endpoints of this LdapBindAccount.
        :type: list[oci.file_storage.models.Endpoint]
        """
        self._endpoints = endpoints

    @property
    def bind_distinguished_name(self):
        """
        **[Required]** Gets the bind_distinguished_name of this LdapBindAccount.
        The LDAP Distinguished Name of the account.


        :return: The bind_distinguished_name of this LdapBindAccount.
        :rtype: str
        """
        return self._bind_distinguished_name

    @bind_distinguished_name.setter
    def bind_distinguished_name(self, bind_distinguished_name):
        """
        Sets the bind_distinguished_name of this LdapBindAccount.
        The LDAP Distinguished Name of the account.


        :param bind_distinguished_name: The bind_distinguished_name of this LdapBindAccount.
        :type: str
        """
        self._bind_distinguished_name = bind_distinguished_name

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this LdapBindAccount.
        The `OCID`__ of the password for the LDAP bind account in the Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this LdapBindAccount.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this LdapBindAccount.
        The `OCID`__ of the password for the LDAP bind account in the Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this LdapBindAccount.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def password_secret_version(self):
        """
        Gets the password_secret_version of this LdapBindAccount.
        Version of the password secret in the Vault to use.


        :return: The password_secret_version of this LdapBindAccount.
        :rtype: int
        """
        return self._password_secret_version

    @password_secret_version.setter
    def password_secret_version(self, password_secret_version):
        """
        Sets the password_secret_version of this LdapBindAccount.
        Version of the password secret in the Vault to use.


        :param password_secret_version: The password_secret_version of this LdapBindAccount.
        :type: int
        """
        self._password_secret_version = password_secret_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
