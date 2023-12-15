# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201005

from .update_database_tools_connection_details import UpdateDatabaseToolsConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDatabaseToolsConnectionGenericJdbcDetails(UpdateDatabaseToolsConnectionDetails):
    """
    The update details for a Database Tools Generic JDBC database system connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDatabaseToolsConnectionGenericJdbcDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_tools.models.UpdateDatabaseToolsConnectionGenericJdbcDetails.type` attribute
        of this class is ``GENERIC_JDBC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type display_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type freeform_tags: dict(str, str)

        :param type:
            The value to assign to the type property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
            Allowed values for this property are: "ORACLE_DATABASE", "MYSQL", "POSTGRESQL", "GENERIC_JDBC"
        :type type: str

        :param url:
            The value to assign to the url property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type url: str

        :param user_name:
            The value to assign to the user_name property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type user_name: str

        :param user_password:
            The value to assign to the user_password property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type user_password: oci.database_tools.models.DatabaseToolsUserPasswordDetails

        :param advanced_properties:
            The value to assign to the advanced_properties property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type advanced_properties: dict(str, str)

        :param key_stores:
            The value to assign to the key_stores property of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type key_stores: list[oci.database_tools.models.DatabaseToolsKeyStoreGenericJdbcDetails]

        """
        self.swagger_types = {
            'display_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'type': 'str',
            'url': 'str',
            'user_name': 'str',
            'user_password': 'DatabaseToolsUserPasswordDetails',
            'advanced_properties': 'dict(str, str)',
            'key_stores': 'list[DatabaseToolsKeyStoreGenericJdbcDetails]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'type': 'type',
            'url': 'url',
            'user_name': 'userName',
            'user_password': 'userPassword',
            'advanced_properties': 'advancedProperties',
            'key_stores': 'keyStores'
        }

        self._display_name = None
        self._defined_tags = None
        self._freeform_tags = None
        self._type = None
        self._url = None
        self._user_name = None
        self._user_password = None
        self._advanced_properties = None
        self._key_stores = None
        self._type = 'GENERIC_JDBC'

    @property
    def url(self):
        """
        Gets the url of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The JDBC URL used to connect to the Generic JDBC database system.


        :return: The url of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The JDBC URL used to connect to the Generic JDBC database system.


        :param url: The url of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type: str
        """
        self._url = url

    @property
    def user_name(self):
        """
        Gets the user_name of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The user name.


        :return: The user_name of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The user name.


        :param user_name: The user_name of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_password(self):
        """
        Gets the user_password of this UpdateDatabaseToolsConnectionGenericJdbcDetails.

        :return: The user_password of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :rtype: oci.database_tools.models.DatabaseToolsUserPasswordDetails
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this UpdateDatabaseToolsConnectionGenericJdbcDetails.

        :param user_password: The user_password of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type: oci.database_tools.models.DatabaseToolsUserPasswordDetails
        """
        self._user_password = user_password

    @property
    def advanced_properties(self):
        """
        Gets the advanced_properties of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The advanced connection properties key-value pair.


        :return: The advanced_properties of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :rtype: dict(str, str)
        """
        return self._advanced_properties

    @advanced_properties.setter
    def advanced_properties(self, advanced_properties):
        """
        Sets the advanced_properties of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The advanced connection properties key-value pair.


        :param advanced_properties: The advanced_properties of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type: dict(str, str)
        """
        self._advanced_properties = advanced_properties

    @property
    def key_stores(self):
        """
        Gets the key_stores of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The CA certificate to verify the server's certificate and
        the client private key and associated certificate required for client authentication.


        :return: The key_stores of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :rtype: list[oci.database_tools.models.DatabaseToolsKeyStoreGenericJdbcDetails]
        """
        return self._key_stores

    @key_stores.setter
    def key_stores(self, key_stores):
        """
        Sets the key_stores of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        The CA certificate to verify the server's certificate and
        the client private key and associated certificate required for client authentication.


        :param key_stores: The key_stores of this UpdateDatabaseToolsConnectionGenericJdbcDetails.
        :type: list[oci.database_tools.models.DatabaseToolsKeyStoreGenericJdbcDetails]
        """
        self._key_stores = key_stores

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
