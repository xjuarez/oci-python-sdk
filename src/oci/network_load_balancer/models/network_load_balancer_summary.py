# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkLoadBalancerSummary(object):
    """
    Network load balancer object to be used for list operations.
    """

    #: A constant which can be used with the lifecycle_state property of a NetworkLoadBalancerSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a NetworkLoadBalancerSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a NetworkLoadBalancerSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a NetworkLoadBalancerSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a NetworkLoadBalancerSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a NetworkLoadBalancerSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkLoadBalancerSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NetworkLoadBalancerSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NetworkLoadBalancerSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this NetworkLoadBalancerSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NetworkLoadBalancerSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this NetworkLoadBalancerSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this NetworkLoadBalancerSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this NetworkLoadBalancerSummary.
        :type time_updated: datetime

        :param ip_addresses:
            The value to assign to the ip_addresses property of this NetworkLoadBalancerSummary.
        :type ip_addresses: list[oci.network_load_balancer.models.IpAddress]

        :param is_private:
            The value to assign to the is_private property of this NetworkLoadBalancerSummary.
        :type is_private: bool

        :param is_preserve_source_destination:
            The value to assign to the is_preserve_source_destination property of this NetworkLoadBalancerSummary.
        :type is_preserve_source_destination: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this NetworkLoadBalancerSummary.
        :type subnet_id: str

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this NetworkLoadBalancerSummary.
        :type network_security_group_ids: list[str]

        :param listeners:
            The value to assign to the listeners property of this NetworkLoadBalancerSummary.
        :type listeners: dict(str, Listener)

        :param backend_sets:
            The value to assign to the backend_sets property of this NetworkLoadBalancerSummary.
        :type backend_sets: dict(str, BackendSet)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this NetworkLoadBalancerSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this NetworkLoadBalancerSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this NetworkLoadBalancerSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'ip_addresses': 'list[IpAddress]',
            'is_private': 'bool',
            'is_preserve_source_destination': 'bool',
            'subnet_id': 'str',
            'network_security_group_ids': 'list[str]',
            'listeners': 'dict(str, Listener)',
            'backend_sets': 'dict(str, BackendSet)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'ip_addresses': 'ipAddresses',
            'is_private': 'isPrivate',
            'is_preserve_source_destination': 'isPreserveSourceDestination',
            'subnet_id': 'subnetId',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'listeners': 'listeners',
            'backend_sets': 'backendSets',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._ip_addresses = None
        self._is_private = None
        self._is_preserve_source_destination = None
        self._subnet_id = None
        self._network_security_group_ids = None
        self._listeners = None
        self._backend_sets = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this NetworkLoadBalancerSummary.
        The `OCID`__ of the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this NetworkLoadBalancerSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NetworkLoadBalancerSummary.
        The `OCID`__ of the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this NetworkLoadBalancerSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this NetworkLoadBalancerSummary.
        The `OCID`__ of the compartment containing the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this NetworkLoadBalancerSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NetworkLoadBalancerSummary.
        The `OCID`__ of the compartment containing the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this NetworkLoadBalancerSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this NetworkLoadBalancerSummary.
        A user-friendly name, which does not have to be unique, and can be changed.

        Example: `example_load_balancer`


        :return: The display_name of this NetworkLoadBalancerSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NetworkLoadBalancerSummary.
        A user-friendly name, which does not have to be unique, and can be changed.

        Example: `example_load_balancer`


        :param display_name: The display_name of this NetworkLoadBalancerSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this NetworkLoadBalancerSummary.
        The current state of the network load balancer.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this NetworkLoadBalancerSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NetworkLoadBalancerSummary.
        The current state of the network load balancer.


        :param lifecycle_state: The lifecycle_state of this NetworkLoadBalancerSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this NetworkLoadBalancerSummary.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this NetworkLoadBalancerSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this NetworkLoadBalancerSummary.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this NetworkLoadBalancerSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this NetworkLoadBalancerSummary.
        The date and time the network load balancer was created, in the format defined by RFC3339.

        Example: `2020-05-01T21:10:29.600Z`


        :return: The time_created of this NetworkLoadBalancerSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NetworkLoadBalancerSummary.
        The date and time the network load balancer was created, in the format defined by RFC3339.

        Example: `2020-05-01T21:10:29.600Z`


        :param time_created: The time_created of this NetworkLoadBalancerSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this NetworkLoadBalancerSummary.
        The time the network load balancer was updated. An RFC3339 formatted date-time string.

        Example: `2020-05-01T22:10:29.600Z`


        :return: The time_updated of this NetworkLoadBalancerSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this NetworkLoadBalancerSummary.
        The time the network load balancer was updated. An RFC3339 formatted date-time string.

        Example: `2020-05-01T22:10:29.600Z`


        :param time_updated: The time_updated of this NetworkLoadBalancerSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def ip_addresses(self):
        """
        **[Required]** Gets the ip_addresses of this NetworkLoadBalancerSummary.
        An array of IP addresses.


        :return: The ip_addresses of this NetworkLoadBalancerSummary.
        :rtype: list[oci.network_load_balancer.models.IpAddress]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this NetworkLoadBalancerSummary.
        An array of IP addresses.


        :param ip_addresses: The ip_addresses of this NetworkLoadBalancerSummary.
        :type: list[oci.network_load_balancer.models.IpAddress]
        """
        self._ip_addresses = ip_addresses

    @property
    def is_private(self):
        """
        Gets the is_private of this NetworkLoadBalancerSummary.
        Whether the network load balancer has a virtual cloud network-local (private) IP address.

        If \"true\", then the service assigns a private IP address to the network load balancer.

        If \"false\", then the service assigns a public IP address to the network load balancer.

        A public network load balancer is accessible from the internet, depending the
        `security list rules`__ for your virtual cloudn network. For more information about public and
        private network load balancers,
        see `How Network Load Balancing Works`__.
        This value is true by default.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-works


        :return: The is_private of this NetworkLoadBalancerSummary.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """
        Sets the is_private of this NetworkLoadBalancerSummary.
        Whether the network load balancer has a virtual cloud network-local (private) IP address.

        If \"true\", then the service assigns a private IP address to the network load balancer.

        If \"false\", then the service assigns a public IP address to the network load balancer.

        A public network load balancer is accessible from the internet, depending the
        `security list rules`__ for your virtual cloudn network. For more information about public and
        private network load balancers,
        see `How Network Load Balancing Works`__.
        This value is true by default.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-works


        :param is_private: The is_private of this NetworkLoadBalancerSummary.
        :type: bool
        """
        self._is_private = is_private

    @property
    def is_preserve_source_destination(self):
        """
        Gets the is_preserve_source_destination of this NetworkLoadBalancerSummary.
        When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC.
        Packets are sent to the backend set without any changes to the source and destination IP.


        :return: The is_preserve_source_destination of this NetworkLoadBalancerSummary.
        :rtype: bool
        """
        return self._is_preserve_source_destination

    @is_preserve_source_destination.setter
    def is_preserve_source_destination(self, is_preserve_source_destination):
        """
        Sets the is_preserve_source_destination of this NetworkLoadBalancerSummary.
        When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC.
        Packets are sent to the backend set without any changes to the source and destination IP.


        :param is_preserve_source_destination: The is_preserve_source_destination of this NetworkLoadBalancerSummary.
        :type: bool
        """
        self._is_preserve_source_destination = is_preserve_source_destination

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this NetworkLoadBalancerSummary.
        The subnet in which the network load balancer is spawned `OCIDs`__.\"

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this NetworkLoadBalancerSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this NetworkLoadBalancerSummary.
        The subnet in which the network load balancer is spawned `OCIDs`__.\"

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this NetworkLoadBalancerSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this NetworkLoadBalancerSummary.
        An array of network security groups `OCIDs`__ associated with the network load
        balancer.

        During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.

        The benefits of associating the network load balancer with network security groups include:

        *  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

        *  The network security rules of other resources can reference the network security groups associated with the network load balancer
           to ensure access.

        Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this NetworkLoadBalancerSummary.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this NetworkLoadBalancerSummary.
        An array of network security groups `OCIDs`__ associated with the network load
        balancer.

        During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.

        The benefits of associating the network load balancer with network security groups include:

        *  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

        *  The network security rules of other resources can reference the network security groups associated with the network load balancer
           to ensure access.

        Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this NetworkLoadBalancerSummary.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def listeners(self):
        """
        Gets the listeners of this NetworkLoadBalancerSummary.
        Listeners associated with the network load balancer.


        :return: The listeners of this NetworkLoadBalancerSummary.
        :rtype: dict(str, Listener)
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """
        Sets the listeners of this NetworkLoadBalancerSummary.
        Listeners associated with the network load balancer.


        :param listeners: The listeners of this NetworkLoadBalancerSummary.
        :type: dict(str, Listener)
        """
        self._listeners = listeners

    @property
    def backend_sets(self):
        """
        Gets the backend_sets of this NetworkLoadBalancerSummary.
        Backend sets associated with the network load balancer.


        :return: The backend_sets of this NetworkLoadBalancerSummary.
        :rtype: dict(str, BackendSet)
        """
        return self._backend_sets

    @backend_sets.setter
    def backend_sets(self, backend_sets):
        """
        Sets the backend_sets of this NetworkLoadBalancerSummary.
        Backend sets associated with the network load balancer.


        :param backend_sets: The backend_sets of this NetworkLoadBalancerSummary.
        :type: dict(str, BackendSet)
        """
        self._backend_sets = backend_sets

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this NetworkLoadBalancerSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this NetworkLoadBalancerSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this NetworkLoadBalancerSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this NetworkLoadBalancerSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this NetworkLoadBalancerSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this NetworkLoadBalancerSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this NetworkLoadBalancerSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this NetworkLoadBalancerSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this NetworkLoadBalancerSummary.
        Key-value pair representing system tags' keys and values scoped to a namespace.
        Example: `{\"bar-key\": \"value\"}`


        :return: The system_tags of this NetworkLoadBalancerSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this NetworkLoadBalancerSummary.
        Key-value pair representing system tags' keys and values scoped to a namespace.
        Example: `{\"bar-key\": \"value\"}`


        :param system_tags: The system_tags of this NetworkLoadBalancerSummary.
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