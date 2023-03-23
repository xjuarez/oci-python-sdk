# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaMessageServiceConnection(Connection):
    """
    Represents the metadata of a Java Message Service Connection.
    """

    #: A constant which can be used with the technology_type property of a JavaMessageServiceConnection.
    #: This constant has a value of "ORACLE_WEBLOGIC_JMS"
    TECHNOLOGY_TYPE_ORACLE_WEBLOGIC_JMS = "ORACLE_WEBLOGIC_JMS"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaMessageServiceConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.JavaMessageServiceConnection.connection_type` attribute
        of this class is ``JAVA_MESSAGE_SERVICE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this JavaMessageServiceConnection.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this JavaMessageServiceConnection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this JavaMessageServiceConnection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this JavaMessageServiceConnection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this JavaMessageServiceConnection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this JavaMessageServiceConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this JavaMessageServiceConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this JavaMessageServiceConnection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JavaMessageServiceConnection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this JavaMessageServiceConnection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this JavaMessageServiceConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this JavaMessageServiceConnection.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this JavaMessageServiceConnection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this JavaMessageServiceConnection.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this JavaMessageServiceConnection.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this JavaMessageServiceConnection.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this JavaMessageServiceConnection.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this JavaMessageServiceConnection.
            Allowed values for this property are: "ORACLE_WEBLOGIC_JMS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param should_use_jndi:
            The value to assign to the should_use_jndi property of this JavaMessageServiceConnection.
        :type should_use_jndi: bool

        :param jndi_connection_factory:
            The value to assign to the jndi_connection_factory property of this JavaMessageServiceConnection.
        :type jndi_connection_factory: str

        :param jndi_provider_url:
            The value to assign to the jndi_provider_url property of this JavaMessageServiceConnection.
        :type jndi_provider_url: str

        :param jndi_initial_context_factory:
            The value to assign to the jndi_initial_context_factory property of this JavaMessageServiceConnection.
        :type jndi_initial_context_factory: str

        :param jndi_security_principal:
            The value to assign to the jndi_security_principal property of this JavaMessageServiceConnection.
        :type jndi_security_principal: str

        :param connection_url:
            The value to assign to the connection_url property of this JavaMessageServiceConnection.
        :type connection_url: str

        :param connection_factory:
            The value to assign to the connection_factory property of this JavaMessageServiceConnection.
        :type connection_factory: str

        :param username:
            The value to assign to the username property of this JavaMessageServiceConnection.
        :type username: str

        :param private_ip:
            The value to assign to the private_ip property of this JavaMessageServiceConnection.
        :type private_ip: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'should_use_jndi': 'bool',
            'jndi_connection_factory': 'str',
            'jndi_provider_url': 'str',
            'jndi_initial_context_factory': 'str',
            'jndi_security_principal': 'str',
            'connection_url': 'str',
            'connection_factory': 'str',
            'username': 'str',
            'private_ip': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'should_use_jndi': 'shouldUseJndi',
            'jndi_connection_factory': 'jndiConnectionFactory',
            'jndi_provider_url': 'jndiProviderUrl',
            'jndi_initial_context_factory': 'jndiInitialContextFactory',
            'jndi_security_principal': 'jndiSecurityPrincipal',
            'connection_url': 'connectionUrl',
            'connection_factory': 'connectionFactory',
            'username': 'username',
            'private_ip': 'privateIp'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._technology_type = None
        self._should_use_jndi = None
        self._jndi_connection_factory = None
        self._jndi_provider_url = None
        self._jndi_initial_context_factory = None
        self._jndi_security_principal = None
        self._connection_url = None
        self._connection_factory = None
        self._username = None
        self._private_ip = None
        self._connection_type = 'JAVA_MESSAGE_SERVICE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this JavaMessageServiceConnection.
        The Java Message Service technology type.

        Allowed values for this property are: "ORACLE_WEBLOGIC_JMS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this JavaMessageServiceConnection.
        The Java Message Service technology type.


        :param technology_type: The technology_type of this JavaMessageServiceConnection.
        :type: str
        """
        allowed_values = ["ORACLE_WEBLOGIC_JMS"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def should_use_jndi(self):
        """
        **[Required]** Gets the should_use_jndi of this JavaMessageServiceConnection.
        If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.


        :return: The should_use_jndi of this JavaMessageServiceConnection.
        :rtype: bool
        """
        return self._should_use_jndi

    @should_use_jndi.setter
    def should_use_jndi(self, should_use_jndi):
        """
        Sets the should_use_jndi of this JavaMessageServiceConnection.
        If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.


        :param should_use_jndi: The should_use_jndi of this JavaMessageServiceConnection.
        :type: bool
        """
        self._should_use_jndi = should_use_jndi

    @property
    def jndi_connection_factory(self):
        """
        Gets the jndi_connection_factory of this JavaMessageServiceConnection.
        The Connection Factory can be looked up using this name.
        e.g.: 'ConnectionFactory'


        :return: The jndi_connection_factory of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._jndi_connection_factory

    @jndi_connection_factory.setter
    def jndi_connection_factory(self, jndi_connection_factory):
        """
        Sets the jndi_connection_factory of this JavaMessageServiceConnection.
        The Connection Factory can be looked up using this name.
        e.g.: 'ConnectionFactory'


        :param jndi_connection_factory: The jndi_connection_factory of this JavaMessageServiceConnection.
        :type: str
        """
        self._jndi_connection_factory = jndi_connection_factory

    @property
    def jndi_provider_url(self):
        """
        Gets the jndi_provider_url of this JavaMessageServiceConnection.
        The URL that Java Message Service will use to contact the JNDI provider.
        e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'


        :return: The jndi_provider_url of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._jndi_provider_url

    @jndi_provider_url.setter
    def jndi_provider_url(self, jndi_provider_url):
        """
        Sets the jndi_provider_url of this JavaMessageServiceConnection.
        The URL that Java Message Service will use to contact the JNDI provider.
        e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'


        :param jndi_provider_url: The jndi_provider_url of this JavaMessageServiceConnection.
        :type: str
        """
        self._jndi_provider_url = jndi_provider_url

    @property
    def jndi_initial_context_factory(self):
        """
        Gets the jndi_initial_context_factory of this JavaMessageServiceConnection.
        The implementation of javax.naming.spi.InitialContextFactory interface
        that the client uses to obtain initial naming context.
        e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'


        :return: The jndi_initial_context_factory of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._jndi_initial_context_factory

    @jndi_initial_context_factory.setter
    def jndi_initial_context_factory(self, jndi_initial_context_factory):
        """
        Sets the jndi_initial_context_factory of this JavaMessageServiceConnection.
        The implementation of javax.naming.spi.InitialContextFactory interface
        that the client uses to obtain initial naming context.
        e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'


        :param jndi_initial_context_factory: The jndi_initial_context_factory of this JavaMessageServiceConnection.
        :type: str
        """
        self._jndi_initial_context_factory = jndi_initial_context_factory

    @property
    def jndi_security_principal(self):
        """
        Gets the jndi_security_principal of this JavaMessageServiceConnection.
        Specifies the identity of the principal (user) to be authenticated.
        e.g.: 'admin2'


        :return: The jndi_security_principal of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._jndi_security_principal

    @jndi_security_principal.setter
    def jndi_security_principal(self, jndi_security_principal):
        """
        Sets the jndi_security_principal of this JavaMessageServiceConnection.
        Specifies the identity of the principal (user) to be authenticated.
        e.g.: 'admin2'


        :param jndi_security_principal: The jndi_security_principal of this JavaMessageServiceConnection.
        :type: str
        """
        self._jndi_security_principal = jndi_security_principal

    @property
    def connection_url(self):
        """
        Gets the connection_url of this JavaMessageServiceConnection.
        Connectin URL of the Java Message Service, specifying the protocol, host, and port.
        e.g.: 'mq://myjms.host.domain:7676'


        :return: The connection_url of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """
        Sets the connection_url of this JavaMessageServiceConnection.
        Connectin URL of the Java Message Service, specifying the protocol, host, and port.
        e.g.: 'mq://myjms.host.domain:7676'


        :param connection_url: The connection_url of this JavaMessageServiceConnection.
        :type: str
        """
        self._connection_url = connection_url

    @property
    def connection_factory(self):
        """
        Gets the connection_factory of this JavaMessageServiceConnection.
        The of Java class implementing javax.jms.ConnectionFactory interface
        supplied by the Java Message Service provider.
        e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'


        :return: The connection_factory of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._connection_factory

    @connection_factory.setter
    def connection_factory(self, connection_factory):
        """
        Sets the connection_factory of this JavaMessageServiceConnection.
        The of Java class implementing javax.jms.ConnectionFactory interface
        supplied by the Java Message Service provider.
        e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'


        :param connection_factory: The connection_factory of this JavaMessageServiceConnection.
        :type: str
        """
        self._connection_factory = connection_factory

    @property
    def username(self):
        """
        Gets the username of this JavaMessageServiceConnection.
        The username Oracle GoldenGate uses to connect to the Java Message Service.
        This username must already exist and be available by the Java Message Service to be connected to.


        :return: The username of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this JavaMessageServiceConnection.
        The username Oracle GoldenGate uses to connect to the Java Message Service.
        This username must already exist and be available by the Java Message Service to be connected to.


        :param username: The username of this JavaMessageServiceConnection.
        :type: str
        """
        self._username = username

    @property
    def private_ip(self):
        """
        Gets the private_ip of this JavaMessageServiceConnection.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this JavaMessageServiceConnection.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this JavaMessageServiceConnection.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this JavaMessageServiceConnection.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
