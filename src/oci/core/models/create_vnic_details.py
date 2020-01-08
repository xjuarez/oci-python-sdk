# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVnicDetails(object):
    """
    Contains properties for a VNIC. You use this object when creating the
    primary VNIC during instance launch or when creating a secondary VNIC.
    For more information about VNICs, see
    `Virtual Network Interface Cards (VNICs)`__.

    __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingVNICs.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVnicDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param assign_public_ip:
            The value to assign to the assign_public_ip property of this CreateVnicDetails.
        :type assign_public_ip: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVnicDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVnicDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVnicDetails.
        :type freeform_tags: dict(str, str)

        :param hostname_label:
            The value to assign to the hostname_label property of this CreateVnicDetails.
        :type hostname_label: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateVnicDetails.
        :type nsg_ids: list[str]

        :param private_ip:
            The value to assign to the private_ip property of this CreateVnicDetails.
        :type private_ip: str

        :param skip_source_dest_check:
            The value to assign to the skip_source_dest_check property of this CreateVnicDetails.
        :type skip_source_dest_check: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateVnicDetails.
        :type subnet_id: str

        """
        self.swagger_types = {
            'assign_public_ip': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname_label': 'str',
            'nsg_ids': 'list[str]',
            'private_ip': 'str',
            'skip_source_dest_check': 'bool',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'assign_public_ip': 'assignPublicIp',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'hostname_label': 'hostnameLabel',
            'nsg_ids': 'nsgIds',
            'private_ip': 'privateIp',
            'skip_source_dest_check': 'skipSourceDestCheck',
            'subnet_id': 'subnetId'
        }

        self._assign_public_ip = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._hostname_label = None
        self._nsg_ids = None
        self._private_ip = None
        self._skip_source_dest_check = None
        self._subnet_id = None

    @property
    def assign_public_ip(self):
        """
        Gets the assign_public_ip of this CreateVnicDetails.
        Whether the VNIC should be assigned a public IP address. Defaults to whether
        the subnet is public or private. If not set and the VNIC is being created
        in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
        :class:`Subnet`), then no public IP address is assigned.
        If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
        a public IP address is assigned. If set to true and
        `prohibitPublicIpOnVnic` = true, an error is returned.

        **Note:** This public IP address is associated with the primary private IP
        on the VNIC. For more information, see
        `IP Addresses`__.

        **Note:** There's a limit to the number of :class:`PublicIp`
        a VNIC or instance can have. If you try to create a secondary VNIC
        with an assigned public IP for an instance that has already
        reached its public IP limit, an error is returned. For information
        about the public IP limits, see
        `Public IP Addresses`__.

        Example: `false`

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPaddresses.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm


        :return: The assign_public_ip of this CreateVnicDetails.
        :rtype: bool
        """
        return self._assign_public_ip

    @assign_public_ip.setter
    def assign_public_ip(self, assign_public_ip):
        """
        Sets the assign_public_ip of this CreateVnicDetails.
        Whether the VNIC should be assigned a public IP address. Defaults to whether
        the subnet is public or private. If not set and the VNIC is being created
        in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
        :class:`Subnet`), then no public IP address is assigned.
        If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
        a public IP address is assigned. If set to true and
        `prohibitPublicIpOnVnic` = true, an error is returned.

        **Note:** This public IP address is associated with the primary private IP
        on the VNIC. For more information, see
        `IP Addresses`__.

        **Note:** There's a limit to the number of :class:`PublicIp`
        a VNIC or instance can have. If you try to create a secondary VNIC
        with an assigned public IP for an instance that has already
        reached its public IP limit, an error is returned. For information
        about the public IP limits, see
        `Public IP Addresses`__.

        Example: `false`

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPaddresses.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm


        :param assign_public_ip: The assign_public_ip of this CreateVnicDetails.
        :type: bool
        """
        self._assign_public_ip = assign_public_ip

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVnicDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVnicDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVnicDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVnicDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVnicDetails.
        A user-friendly name for the VNIC. Does not have to be unique.
        Avoid entering confidential information.


        :return: The display_name of this CreateVnicDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVnicDetails.
        A user-friendly name for the VNIC. Does not have to be unique.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVnicDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVnicDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVnicDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVnicDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVnicDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this CreateVnicDetails.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value appears in the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        When launching an instance, use this `hostnameLabel` instead
        of the deprecated `hostnameLabel` in
        :func:`launch_instance_details`.
        If you provide both, the values must match.

        Example: `bminstance-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this CreateVnicDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this CreateVnicDetails.
        The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
        portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value appears in the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        When launching an instance, use this `hostnameLabel` instead
        of the deprecated `hostnameLabel` in
        :func:`launch_instance_details`.
        If you provide both, the values must match.

        Example: `bminstance-1`

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this CreateVnicDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateVnicDetails.
        A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this CreateVnicDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateVnicDetails.
        A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this CreateVnicDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def private_ip(self):
        """
        Gets the private_ip of this CreateVnicDetails.
        A private IP address of your choice to assign to the VNIC. Must be an
        available IP address within the subnet's CIDR. If you don't specify a
        value, Oracle automatically assigns a private IP address from the subnet.
        This is the VNIC's *primary* private IP address. The value appears in
        the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        Example: `10.0.3.3`


        :return: The private_ip of this CreateVnicDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this CreateVnicDetails.
        A private IP address of your choice to assign to the VNIC. Must be an
        available IP address within the subnet's CIDR. If you don't specify a
        value, Oracle automatically assigns a private IP address from the subnet.
        This is the VNIC's *primary* private IP address. The value appears in
        the :class:`Vnic` object and also the
        :class:`PrivateIp` object returned by
        :func:`list_private_ips` and
        :func:`get_private_ip`.

        Example: `10.0.3.3`


        :param private_ip: The private_ip of this CreateVnicDetails.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def skip_source_dest_check(self):
        """
        Gets the skip_source_dest_check of this CreateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information
        about why you would skip the source/destination check, see
        `Using a Private IP as a Route Target`__.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :return: The skip_source_dest_check of this CreateVnicDetails.
        :rtype: bool
        """
        return self._skip_source_dest_check

    @skip_source_dest_check.setter
    def skip_source_dest_check(self, skip_source_dest_check):
        """
        Sets the skip_source_dest_check of this CreateVnicDetails.
        Whether the source/destination check is disabled on the VNIC.
        Defaults to `false`, which means the check is performed. For information
        about why you would skip the source/destination check, see
        `Using a Private IP as a Route Target`__.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :param skip_source_dest_check: The skip_source_dest_check of this CreateVnicDetails.
        :type: bool
        """
        self._skip_source_dest_check = skip_source_dest_check

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateVnicDetails.
        The OCID of the subnet to create the VNIC in. When launching an instance,
        use this `subnetId` instead of the deprecated `subnetId` in
        :func:`launch_instance_details`.
        At least one of them is required; if you provide both, the values must match.


        :return: The subnet_id of this CreateVnicDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateVnicDetails.
        The OCID of the subnet to create the VNIC in. When launching an instance,
        use this `subnetId` instead of the deprecated `subnetId` in
        :func:`launch_instance_details`.
        At least one of them is required; if you provide both, the values must match.


        :param subnet_id: The subnet_id of this CreateVnicDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
