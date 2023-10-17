# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220315


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RedisClusterSummary(object):
    """
    Summary of information about a Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see `OCI Caching Service with Redis`__.

    __ https://docs.cloud.oracle.com/iaas/Content/redis/home.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RedisClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RedisClusterSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this RedisClusterSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RedisClusterSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RedisClusterSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this RedisClusterSummary.
        :type lifecycle_details: str

        :param node_count:
            The value to assign to the node_count property of this RedisClusterSummary.
        :type node_count: int

        :param node_memory_in_gbs:
            The value to assign to the node_memory_in_gbs property of this RedisClusterSummary.
        :type node_memory_in_gbs: float

        :param primary_fqdn:
            The value to assign to the primary_fqdn property of this RedisClusterSummary.
        :type primary_fqdn: str

        :param primary_endpoint_ip_address:
            The value to assign to the primary_endpoint_ip_address property of this RedisClusterSummary.
        :type primary_endpoint_ip_address: str

        :param replicas_fqdn:
            The value to assign to the replicas_fqdn property of this RedisClusterSummary.
        :type replicas_fqdn: str

        :param replicas_endpoint_ip_address:
            The value to assign to the replicas_endpoint_ip_address property of this RedisClusterSummary.
        :type replicas_endpoint_ip_address: str

        :param software_version:
            The value to assign to the software_version property of this RedisClusterSummary.
        :type software_version: str

        :param subnet_id:
            The value to assign to the subnet_id property of this RedisClusterSummary.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this RedisClusterSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RedisClusterSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RedisClusterSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RedisClusterSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RedisClusterSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'node_count': 'int',
            'node_memory_in_gbs': 'float',
            'primary_fqdn': 'str',
            'primary_endpoint_ip_address': 'str',
            'replicas_fqdn': 'str',
            'replicas_endpoint_ip_address': 'str',
            'software_version': 'str',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'node_count': 'nodeCount',
            'node_memory_in_gbs': 'nodeMemoryInGBs',
            'primary_fqdn': 'primaryFqdn',
            'primary_endpoint_ip_address': 'primaryEndpointIpAddress',
            'replicas_fqdn': 'replicasFqdn',
            'replicas_endpoint_ip_address': 'replicasEndpointIpAddress',
            'software_version': 'softwareVersion',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._node_count = None
        self._node_memory_in_gbs = None
        self._primary_fqdn = None
        self._primary_endpoint_ip_address = None
        self._replicas_fqdn = None
        self._replicas_endpoint_ip_address = None
        self._software_version = None
        self._subnet_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RedisClusterSummary.
        The `OCID`__ of the Redis cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :return: The id of this RedisClusterSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RedisClusterSummary.
        The `OCID`__ of the Redis cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :param id: The id of this RedisClusterSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RedisClusterSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this RedisClusterSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RedisClusterSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this RedisClusterSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RedisClusterSummary.
        The `OCID`__ of the compartment that contains the Redis cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :return: The compartment_id of this RedisClusterSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RedisClusterSummary.
        The `OCID`__ of the compartment that contains the Redis cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :param compartment_id: The compartment_id of this RedisClusterSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RedisClusterSummary.
        The current state of the Redis cluster.


        :return: The lifecycle_state of this RedisClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RedisClusterSummary.
        The current state of the Redis cluster.


        :param lifecycle_state: The lifecycle_state of this RedisClusterSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this RedisClusterSummary.
        A message describing the current state in more detail. For example, the message might provide actionable information for a resource in `FAILED` state.


        :return: The lifecycle_details of this RedisClusterSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this RedisClusterSummary.
        A message describing the current state in more detail. For example, the message might provide actionable information for a resource in `FAILED` state.


        :param lifecycle_details: The lifecycle_details of this RedisClusterSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def node_count(self):
        """
        **[Required]** Gets the node_count of this RedisClusterSummary.
        The number of nodes in the Redis cluster.


        :return: The node_count of this RedisClusterSummary.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this RedisClusterSummary.
        The number of nodes in the Redis cluster.


        :param node_count: The node_count of this RedisClusterSummary.
        :type: int
        """
        self._node_count = node_count

    @property
    def node_memory_in_gbs(self):
        """
        **[Required]** Gets the node_memory_in_gbs of this RedisClusterSummary.
        The amount of memory allocated to the Redis cluster's nodes, in gigabytes.


        :return: The node_memory_in_gbs of this RedisClusterSummary.
        :rtype: float
        """
        return self._node_memory_in_gbs

    @node_memory_in_gbs.setter
    def node_memory_in_gbs(self, node_memory_in_gbs):
        """
        Sets the node_memory_in_gbs of this RedisClusterSummary.
        The amount of memory allocated to the Redis cluster's nodes, in gigabytes.


        :param node_memory_in_gbs: The node_memory_in_gbs of this RedisClusterSummary.
        :type: float
        """
        self._node_memory_in_gbs = node_memory_in_gbs

    @property
    def primary_fqdn(self):
        """
        **[Required]** Gets the primary_fqdn of this RedisClusterSummary.
        The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's primary node.


        :return: The primary_fqdn of this RedisClusterSummary.
        :rtype: str
        """
        return self._primary_fqdn

    @primary_fqdn.setter
    def primary_fqdn(self, primary_fqdn):
        """
        Sets the primary_fqdn of this RedisClusterSummary.
        The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's primary node.


        :param primary_fqdn: The primary_fqdn of this RedisClusterSummary.
        :type: str
        """
        self._primary_fqdn = primary_fqdn

    @property
    def primary_endpoint_ip_address(self):
        """
        **[Required]** Gets the primary_endpoint_ip_address of this RedisClusterSummary.
        The private IP address of the API endpoint for the Redis cluster's primary node.


        :return: The primary_endpoint_ip_address of this RedisClusterSummary.
        :rtype: str
        """
        return self._primary_endpoint_ip_address

    @primary_endpoint_ip_address.setter
    def primary_endpoint_ip_address(self, primary_endpoint_ip_address):
        """
        Sets the primary_endpoint_ip_address of this RedisClusterSummary.
        The private IP address of the API endpoint for the Redis cluster's primary node.


        :param primary_endpoint_ip_address: The primary_endpoint_ip_address of this RedisClusterSummary.
        :type: str
        """
        self._primary_endpoint_ip_address = primary_endpoint_ip_address

    @property
    def replicas_fqdn(self):
        """
        **[Required]** Gets the replicas_fqdn of this RedisClusterSummary.
        The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's replica nodes.


        :return: The replicas_fqdn of this RedisClusterSummary.
        :rtype: str
        """
        return self._replicas_fqdn

    @replicas_fqdn.setter
    def replicas_fqdn(self, replicas_fqdn):
        """
        Sets the replicas_fqdn of this RedisClusterSummary.
        The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's replica nodes.


        :param replicas_fqdn: The replicas_fqdn of this RedisClusterSummary.
        :type: str
        """
        self._replicas_fqdn = replicas_fqdn

    @property
    def replicas_endpoint_ip_address(self):
        """
        **[Required]** Gets the replicas_endpoint_ip_address of this RedisClusterSummary.
        The private IP address of the API endpoint for the Redis cluster's replica nodes.


        :return: The replicas_endpoint_ip_address of this RedisClusterSummary.
        :rtype: str
        """
        return self._replicas_endpoint_ip_address

    @replicas_endpoint_ip_address.setter
    def replicas_endpoint_ip_address(self, replicas_endpoint_ip_address):
        """
        Sets the replicas_endpoint_ip_address of this RedisClusterSummary.
        The private IP address of the API endpoint for the Redis cluster's replica nodes.


        :param replicas_endpoint_ip_address: The replicas_endpoint_ip_address of this RedisClusterSummary.
        :type: str
        """
        self._replicas_endpoint_ip_address = replicas_endpoint_ip_address

    @property
    def software_version(self):
        """
        **[Required]** Gets the software_version of this RedisClusterSummary.
        The Redis version that the cluster is running.


        :return: The software_version of this RedisClusterSummary.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """
        Sets the software_version of this RedisClusterSummary.
        The Redis version that the cluster is running.


        :param software_version: The software_version of this RedisClusterSummary.
        :type: str
        """
        self._software_version = software_version

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this RedisClusterSummary.
        The `OCID`__ of the Redis cluster's subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :return: The subnet_id of this RedisClusterSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this RedisClusterSummary.
        The `OCID`__ of the Redis cluster's subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :param subnet_id: The subnet_id of this RedisClusterSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this RedisClusterSummary.
        The date and time the Redis cluster was created. An `RFC3339`__ formatted datetime string.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this RedisClusterSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RedisClusterSummary.
        The date and time the Redis cluster was created. An `RFC3339`__ formatted datetime string.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this RedisClusterSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RedisClusterSummary.
        The date and time the Redis cluster was updated. An `RFC3339`__ formatted datetime string.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this RedisClusterSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RedisClusterSummary.
        The date and time the Redis cluster was updated. An `RFC3339`__ formatted datetime string.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this RedisClusterSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RedisClusterSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this RedisClusterSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RedisClusterSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this RedisClusterSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RedisClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this RedisClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RedisClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this RedisClusterSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RedisClusterSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this RedisClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RedisClusterSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this RedisClusterSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
