# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAzureDataLakeStorageConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a Azure Data Lake Storage Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAzureDataLakeStorageConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateAzureDataLakeStorageConnectionDetails.connection_type` attribute
        of this class is ``AZURE_DATA_LAKE_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateAzureDataLakeStorageConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type nsg_ids: list[str]

        :param authentication_type:
            The value to assign to the authentication_type property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type authentication_type: str

        :param account_name:
            The value to assign to the account_name property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type account_name: str

        :param account_key:
            The value to assign to the account_key property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type account_key: str

        :param sas_token:
            The value to assign to the sas_token property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type sas_token: str

        :param azure_tenant_id:
            The value to assign to the azure_tenant_id property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type azure_tenant_id: str

        :param client_id:
            The value to assign to the client_id property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type client_id: str

        :param client_secret:
            The value to assign to the client_secret property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type client_secret: str

        :param endpoint:
            The value to assign to the endpoint property of this UpdateAzureDataLakeStorageConnectionDetails.
        :type endpoint: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'authentication_type': 'str',
            'account_name': 'str',
            'account_key': 'str',
            'sas_token': 'str',
            'azure_tenant_id': 'str',
            'client_id': 'str',
            'client_secret': 'str',
            'endpoint': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'authentication_type': 'authenticationType',
            'account_name': 'accountName',
            'account_key': 'accountKey',
            'sas_token': 'sasToken',
            'azure_tenant_id': 'azureTenantId',
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'endpoint': 'endpoint'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._authentication_type = None
        self._account_name = None
        self._account_key = None
        self._sas_token = None
        self._azure_tenant_id = None
        self._client_id = None
        self._client_secret = None
        self._endpoint = None
        self._connection_type = 'AZURE_DATA_LAKE_STORAGE'

    @property
    def authentication_type(self):
        """
        Gets the authentication_type of this UpdateAzureDataLakeStorageConnectionDetails.
        Used authentication mechanism to access Azure Data Lake Storage.


        :return: The authentication_type of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this UpdateAzureDataLakeStorageConnectionDetails.
        Used authentication mechanism to access Azure Data Lake Storage.


        :param authentication_type: The authentication_type of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._authentication_type = authentication_type

    @property
    def account_name(self):
        """
        Gets the account_name of this UpdateAzureDataLakeStorageConnectionDetails.
        Sets the Azure storage account name.


        :return: The account_name of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this UpdateAzureDataLakeStorageConnectionDetails.
        Sets the Azure storage account name.


        :param account_name: The account_name of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._account_name = account_name

    @property
    def account_key(self):
        """
        Gets the account_key of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure storage account key. This property is required when 'authenticationType' is set to 'SHARED_KEY'.
        e.g.: pa3WbhVATzj56xD4DH1VjOUhApRGEGHvOo58eQJVWIzX+j8j4CUVFcTjpIqDSRaSa1Wo2LbWY5at+AStEgLOIQ==


        :return: The account_key of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """
        Sets the account_key of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure storage account key. This property is required when 'authenticationType' is set to 'SHARED_KEY'.
        e.g.: pa3WbhVATzj56xD4DH1VjOUhApRGEGHvOo58eQJVWIzX+j8j4CUVFcTjpIqDSRaSa1Wo2LbWY5at+AStEgLOIQ==


        :param account_key: The account_key of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._account_key = account_key

    @property
    def sas_token(self):
        """
        Gets the sas_token of this UpdateAzureDataLakeStorageConnectionDetails.
        Credential that uses a shared access signature (SAS) to authenticate to an Azure Service. This property is
        required when 'authenticationType' is set to 'SHARED_ACCESS_SIGNATURE'.
        e.g.: ?sv=2020-06-08&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2020-09-10T20:27:28Z&st=2022-08-05T12:27:28Z&spr=https&sig=C1IgHsiLBmTSStYkXXGLTP8it0xBrArcgCqOsZbXwIQ%3D


        :return: The sas_token of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._sas_token

    @sas_token.setter
    def sas_token(self, sas_token):
        """
        Sets the sas_token of this UpdateAzureDataLakeStorageConnectionDetails.
        Credential that uses a shared access signature (SAS) to authenticate to an Azure Service. This property is
        required when 'authenticationType' is set to 'SHARED_ACCESS_SIGNATURE'.
        e.g.: ?sv=2020-06-08&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2020-09-10T20:27:28Z&st=2022-08-05T12:27:28Z&spr=https&sig=C1IgHsiLBmTSStYkXXGLTP8it0xBrArcgCqOsZbXwIQ%3D


        :param sas_token: The sas_token of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._sas_token = sas_token

    @property
    def azure_tenant_id(self):
        """
        Gets the azure_tenant_id of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :return: The azure_tenant_id of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._azure_tenant_id

    @azure_tenant_id.setter
    def azure_tenant_id(self, azure_tenant_id):
        """
        Sets the azure_tenant_id of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :param azure_tenant_id: The azure_tenant_id of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._azure_tenant_id = azure_tenant_id

    @property
    def client_id(self):
        """
        Gets the client_id of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :return: The client_id of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :param client_id: The client_id of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        """
        Gets the client_secret of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure client secret (aka application password) for authentication. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: dO29Q~F5-VwnA.lZdd11xFF_t5NAXCaGwDl9NbT1


        :return: The client_secret of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure client secret (aka application password) for authentication. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: dO29Q~F5-VwnA.lZdd11xFF_t5NAXCaGwDl9NbT1


        :param client_secret: The client_secret of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._client_secret = client_secret

    @property
    def endpoint(self):
        """
        Gets the endpoint of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure Storage service endpoint.
        e.g: https://test.blob.core.windows.net


        :return: The endpoint of this UpdateAzureDataLakeStorageConnectionDetails.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this UpdateAzureDataLakeStorageConnectionDetails.
        Azure Storage service endpoint.
        e.g: https://test.blob.core.windows.net


        :param endpoint: The endpoint of this UpdateAzureDataLakeStorageConnectionDetails.
        :type: str
        """
        self._endpoint = endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
