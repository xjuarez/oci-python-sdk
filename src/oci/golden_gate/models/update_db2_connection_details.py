# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDb2ConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a DB2 Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDb2ConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateDb2ConnectionDetails.connection_type` attribute
        of this class is ``DB2`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateDb2ConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateDb2ConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDb2ConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDb2ConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDb2ConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateDb2ConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateDb2ConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateDb2ConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateDb2ConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateDb2ConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param database_name:
            The value to assign to the database_name property of this UpdateDb2ConnectionDetails.
        :type database_name: str

        :param host:
            The value to assign to the host property of this UpdateDb2ConnectionDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this UpdateDb2ConnectionDetails.
        :type port: int

        :param username:
            The value to assign to the username property of this UpdateDb2ConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateDb2ConnectionDetails.
        :type password: str

        :param additional_attributes:
            The value to assign to the additional_attributes property of this UpdateDb2ConnectionDetails.
        :type additional_attributes: list[oci.golden_gate.models.NameValuePair]

        :param security_protocol:
            The value to assign to the security_protocol property of this UpdateDb2ConnectionDetails.
        :type security_protocol: str

        :param ssl_client_keystoredb:
            The value to assign to the ssl_client_keystoredb property of this UpdateDb2ConnectionDetails.
        :type ssl_client_keystoredb: str

        :param ssl_client_keystash:
            The value to assign to the ssl_client_keystash property of this UpdateDb2ConnectionDetails.
        :type ssl_client_keystash: str

        :param ssl_server_certificate:
            The value to assign to the ssl_server_certificate property of this UpdateDb2ConnectionDetails.
        :type ssl_server_certificate: str

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
            'subnet_id': 'str',
            'routing_method': 'str',
            'database_name': 'str',
            'host': 'str',
            'port': 'int',
            'username': 'str',
            'password': 'str',
            'additional_attributes': 'list[NameValuePair]',
            'security_protocol': 'str',
            'ssl_client_keystoredb': 'str',
            'ssl_client_keystash': 'str',
            'ssl_server_certificate': 'str'
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
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'database_name': 'databaseName',
            'host': 'host',
            'port': 'port',
            'username': 'username',
            'password': 'password',
            'additional_attributes': 'additionalAttributes',
            'security_protocol': 'securityProtocol',
            'ssl_client_keystoredb': 'sslClientKeystoredb',
            'ssl_client_keystash': 'sslClientKeystash',
            'ssl_server_certificate': 'sslServerCertificate'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._database_name = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._additional_attributes = None
        self._security_protocol = None
        self._ssl_client_keystoredb = None
        self._ssl_client_keystash = None
        self._ssl_server_certificate = None
        self._connection_type = 'DB2'

    @property
    def database_name(self):
        """
        Gets the database_name of this UpdateDb2ConnectionDetails.
        The name of the database.


        :return: The database_name of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this UpdateDb2ConnectionDetails.
        The name of the database.


        :param database_name: The database_name of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._database_name = database_name

    @property
    def host(self):
        """
        Gets the host of this UpdateDb2ConnectionDetails.
        The name or address of a host.


        :return: The host of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this UpdateDb2ConnectionDetails.
        The name or address of a host.


        :param host: The host of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this UpdateDb2ConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :return: The port of this UpdateDb2ConnectionDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateDb2ConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this UpdateDb2ConnectionDetails.
        :type: int
        """
        self._port = port

    @property
    def username(self):
        """
        Gets the username of this UpdateDb2ConnectionDetails.
        The username Oracle GoldenGate uses to connect to the DB2 database.
        This username must already exist and be available by the DB2 to be connected to.


        :return: The username of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateDb2ConnectionDetails.
        The username Oracle GoldenGate uses to connect to the DB2 database.
        This username must already exist and be available by the DB2 to be connected to.


        :param username: The username of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UpdateDb2ConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated DB2 database.


        :return: The password of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateDb2ConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated DB2 database.


        :param password: The password of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def additional_attributes(self):
        """
        Gets the additional_attributes of this UpdateDb2ConnectionDetails.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :return: The additional_attributes of this UpdateDb2ConnectionDetails.
        :rtype: list[oci.golden_gate.models.NameValuePair]
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """
        Sets the additional_attributes of this UpdateDb2ConnectionDetails.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :param additional_attributes: The additional_attributes of this UpdateDb2ConnectionDetails.
        :type: list[oci.golden_gate.models.NameValuePair]
        """
        self._additional_attributes = additional_attributes

    @property
    def security_protocol(self):
        """
        Gets the security_protocol of this UpdateDb2ConnectionDetails.
        Security protocol for the DB2 database.


        :return: The security_protocol of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this UpdateDb2ConnectionDetails.
        Security protocol for the DB2 database.


        :param security_protocol: The security_protocol of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def ssl_client_keystoredb(self):
        """
        Gets the ssl_client_keystoredb of this UpdateDb2ConnectionDetails.
        The base64 encoded keystore file created at the client containing the server certificate / CA root certificate.


        :return: The ssl_client_keystoredb of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._ssl_client_keystoredb

    @ssl_client_keystoredb.setter
    def ssl_client_keystoredb(self, ssl_client_keystoredb):
        """
        Sets the ssl_client_keystoredb of this UpdateDb2ConnectionDetails.
        The base64 encoded keystore file created at the client containing the server certificate / CA root certificate.


        :param ssl_client_keystoredb: The ssl_client_keystoredb of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._ssl_client_keystoredb = ssl_client_keystoredb

    @property
    def ssl_client_keystash(self):
        """
        Gets the ssl_client_keystash of this UpdateDb2ConnectionDetails.
        The base64 encoded keystash file which contains the encrypted password to the key database file.


        :return: The ssl_client_keystash of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._ssl_client_keystash

    @ssl_client_keystash.setter
    def ssl_client_keystash(self, ssl_client_keystash):
        """
        Sets the ssl_client_keystash of this UpdateDb2ConnectionDetails.
        The base64 encoded keystash file which contains the encrypted password to the key database file.


        :param ssl_client_keystash: The ssl_client_keystash of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._ssl_client_keystash = ssl_client_keystash

    @property
    def ssl_server_certificate(self):
        """
        Gets the ssl_server_certificate of this UpdateDb2ConnectionDetails.
        The base64 encoded file which contains the self-signed server certificate / Certificate Authority (CA) certificate.


        :return: The ssl_server_certificate of this UpdateDb2ConnectionDetails.
        :rtype: str
        """
        return self._ssl_server_certificate

    @ssl_server_certificate.setter
    def ssl_server_certificate(self, ssl_server_certificate):
        """
        Sets the ssl_server_certificate of this UpdateDb2ConnectionDetails.
        The base64 encoded file which contains the self-signed server certificate / Certificate Authority (CA) certificate.


        :param ssl_server_certificate: The ssl_server_certificate of this UpdateDb2ConnectionDetails.
        :type: str
        """
        self._ssl_server_certificate = ssl_server_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other