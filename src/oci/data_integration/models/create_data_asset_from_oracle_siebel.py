# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .create_data_asset_details import CreateDataAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataAssetFromOracleSiebel(CreateDataAssetDetails):
    """
    Details for the Oracle Siebel data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataAssetFromOracleSiebel object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateDataAssetFromOracleSiebel.model_type` attribute
        of this class is ``ORACLE_SIEBEL_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateDataAssetFromOracleSiebel.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_DATA_ASSET", "ORACLE_PEOPLESOFT_DATA_ASSET", "ORACLE_SIEBEL_DATA_ASSET", "ORACLE_EBS_DATA_ASSET", "HDFS_DATA_ASSET", "MYSQL_HEATWAVE_DATA_ASSET", "REST_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateDataAssetFromOracleSiebel.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDataAssetFromOracleSiebel.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreateDataAssetFromOracleSiebel.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDataAssetFromOracleSiebel.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDataAssetFromOracleSiebel.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateDataAssetFromOracleSiebel.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this CreateDataAssetFromOracleSiebel.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this CreateDataAssetFromOracleSiebel.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateDataAssetFromOracleSiebel.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param host:
            The value to assign to the host property of this CreateDataAssetFromOracleSiebel.
        :type host: str

        :param port:
            The value to assign to the port property of this CreateDataAssetFromOracleSiebel.
        :type port: str

        :param service_name:
            The value to assign to the service_name property of this CreateDataAssetFromOracleSiebel.
        :type service_name: str

        :param driver_class:
            The value to assign to the driver_class property of this CreateDataAssetFromOracleSiebel.
        :type driver_class: str

        :param sid:
            The value to assign to the sid property of this CreateDataAssetFromOracleSiebel.
        :type sid: str

        :param wallet_secret:
            The value to assign to the wallet_secret property of this CreateDataAssetFromOracleSiebel.
        :type wallet_secret: oci.data_integration.models.SensitiveAttribute

        :param wallet_password_secret:
            The value to assign to the wallet_password_secret property of this CreateDataAssetFromOracleSiebel.
        :type wallet_password_secret: oci.data_integration.models.SensitiveAttribute

        :param default_connection:
            The value to assign to the default_connection property of this CreateDataAssetFromOracleSiebel.
        :type default_connection: oci.data_integration.models.CreateConnectionFromOracleSiebel

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'registry_metadata': 'RegistryMetadata',
            'host': 'str',
            'port': 'str',
            'service_name': 'str',
            'driver_class': 'str',
            'sid': 'str',
            'wallet_secret': 'SensitiveAttribute',
            'wallet_password_secret': 'SensitiveAttribute',
            'default_connection': 'CreateConnectionFromOracleSiebel'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'registry_metadata': 'registryMetadata',
            'host': 'host',
            'port': 'port',
            'service_name': 'serviceName',
            'driver_class': 'driverClass',
            'sid': 'sid',
            'wallet_secret': 'walletSecret',
            'wallet_password_secret': 'walletPasswordSecret',
            'default_connection': 'defaultConnection'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._registry_metadata = None
        self._host = None
        self._port = None
        self._service_name = None
        self._driver_class = None
        self._sid = None
        self._wallet_secret = None
        self._wallet_password_secret = None
        self._default_connection = None
        self._model_type = 'ORACLE_SIEBEL_DATA_ASSET'

    @property
    def host(self):
        """
        **[Required]** Gets the host of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel hostname.


        :return: The host of this CreateDataAssetFromOracleSiebel.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel hostname.


        :param host: The host of this CreateDataAssetFromOracleSiebel.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel port.


        :return: The port of this CreateDataAssetFromOracleSiebel.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel port.


        :param port: The port of this CreateDataAssetFromOracleSiebel.
        :type: str
        """
        self._port = port

    @property
    def service_name(self):
        """
        Gets the service_name of this CreateDataAssetFromOracleSiebel.
        The service name for the data asset.


        :return: The service_name of this CreateDataAssetFromOracleSiebel.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this CreateDataAssetFromOracleSiebel.
        The service name for the data asset.


        :param service_name: The service_name of this CreateDataAssetFromOracleSiebel.
        :type: str
        """
        self._service_name = service_name

    @property
    def driver_class(self):
        """
        Gets the driver_class of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel driver class.


        :return: The driver_class of this CreateDataAssetFromOracleSiebel.
        :rtype: str
        """
        return self._driver_class

    @driver_class.setter
    def driver_class(self, driver_class):
        """
        Sets the driver_class of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel driver class.


        :param driver_class: The driver_class of this CreateDataAssetFromOracleSiebel.
        :type: str
        """
        self._driver_class = driver_class

    @property
    def sid(self):
        """
        Gets the sid of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel SID.


        :return: The sid of this CreateDataAssetFromOracleSiebel.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this CreateDataAssetFromOracleSiebel.
        The Oracle Siebel SID.


        :param sid: The sid of this CreateDataAssetFromOracleSiebel.
        :type: str
        """
        self._sid = sid

    @property
    def wallet_secret(self):
        """
        Gets the wallet_secret of this CreateDataAssetFromOracleSiebel.

        :return: The wallet_secret of this CreateDataAssetFromOracleSiebel.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._wallet_secret

    @wallet_secret.setter
    def wallet_secret(self, wallet_secret):
        """
        Sets the wallet_secret of this CreateDataAssetFromOracleSiebel.

        :param wallet_secret: The wallet_secret of this CreateDataAssetFromOracleSiebel.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._wallet_secret = wallet_secret

    @property
    def wallet_password_secret(self):
        """
        Gets the wallet_password_secret of this CreateDataAssetFromOracleSiebel.

        :return: The wallet_password_secret of this CreateDataAssetFromOracleSiebel.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._wallet_password_secret

    @wallet_password_secret.setter
    def wallet_password_secret(self, wallet_password_secret):
        """
        Sets the wallet_password_secret of this CreateDataAssetFromOracleSiebel.

        :param wallet_password_secret: The wallet_password_secret of this CreateDataAssetFromOracleSiebel.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._wallet_password_secret = wallet_password_secret

    @property
    def default_connection(self):
        """
        **[Required]** Gets the default_connection of this CreateDataAssetFromOracleSiebel.

        :return: The default_connection of this CreateDataAssetFromOracleSiebel.
        :rtype: oci.data_integration.models.CreateConnectionFromOracleSiebel
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this CreateDataAssetFromOracleSiebel.

        :param default_connection: The default_connection of this CreateDataAssetFromOracleSiebel.
        :type: oci.data_integration.models.CreateConnectionFromOracleSiebel
        """
        self._default_connection = default_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
