# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230701


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Cluster(object):
    """
    An `Oracle Cloud VMware Solution`__ Cluster contains the resources required for a
    functional VMware environment. Instances in a Cluster
    (see :class:`EsxiHost`) run in a virtual cloud network (VCN)
    and are preconfigured with VMware and storage. Use the vCenter utility to manage
    and deploy VMware virtual machines (VMs) in the Cluster.

    The Cluster uses a single management subnet for provisioning the Cluster. It also uses a
    set of VLANs for various components of the VMware environment (vSphere, vMotion,
    vSAN, and so on). See the Core Services API for information about VCN subnets and VLANs.

    __ https://docs.cloud.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm
    """

    #: A constant which can be used with the initial_commitment property of a Cluster.
    #: This constant has a value of "HOUR"
    INITIAL_COMMITMENT_HOUR = "HOUR"

    #: A constant which can be used with the initial_commitment property of a Cluster.
    #: This constant has a value of "MONTH"
    INITIAL_COMMITMENT_MONTH = "MONTH"

    #: A constant which can be used with the initial_commitment property of a Cluster.
    #: This constant has a value of "ONE_YEAR"
    INITIAL_COMMITMENT_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the initial_commitment property of a Cluster.
    #: This constant has a value of "THREE_YEARS"
    INITIAL_COMMITMENT_THREE_YEARS = "THREE_YEARS"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Cluster.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the vsphere_type property of a Cluster.
    #: This constant has a value of "MANAGEMENT"
    VSPHERE_TYPE_MANAGEMENT = "MANAGEMENT"

    #: A constant which can be used with the vsphere_type property of a Cluster.
    #: This constant has a value of "WORKLOAD"
    VSPHERE_TYPE_WORKLOAD = "WORKLOAD"

    def __init__(self, **kwargs):
        """
        Initializes a new Cluster object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Cluster.
        :type id: str

        :param compute_availability_domain:
            The value to assign to the compute_availability_domain property of this Cluster.
        :type compute_availability_domain: str

        :param display_name:
            The value to assign to the display_name property of this Cluster.
        :type display_name: str

        :param instance_display_name_prefix:
            The value to assign to the instance_display_name_prefix property of this Cluster.
        :type instance_display_name_prefix: str

        :param vmware_software_version:
            The value to assign to the vmware_software_version property of this Cluster.
        :type vmware_software_version: str

        :param esxi_software_version:
            The value to assign to the esxi_software_version property of this Cluster.
        :type esxi_software_version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Cluster.
        :type compartment_id: str

        :param sddc_id:
            The value to assign to the sddc_id property of this Cluster.
        :type sddc_id: str

        :param esxi_hosts_count:
            The value to assign to the esxi_hosts_count property of this Cluster.
        :type esxi_hosts_count: int

        :param initial_commitment:
            The value to assign to the initial_commitment property of this Cluster.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type initial_commitment: str

        :param workload_network_cidr:
            The value to assign to the workload_network_cidr property of this Cluster.
        :type workload_network_cidr: str

        :param network_configuration:
            The value to assign to the network_configuration property of this Cluster.
        :type network_configuration: oci.ocvp.models.NetworkConfiguration

        :param time_created:
            The value to assign to the time_created property of this Cluster.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Cluster.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Cluster.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param upgrade_licenses:
            The value to assign to the upgrade_licenses property of this Cluster.
        :type upgrade_licenses: list[oci.ocvp.models.VsphereLicense]

        :param vsphere_upgrade_objects:
            The value to assign to the vsphere_upgrade_objects property of this Cluster.
        :type vsphere_upgrade_objects: list[oci.ocvp.models.VsphereUpgradeObject]

        :param initial_host_shape_name:
            The value to assign to the initial_host_shape_name property of this Cluster.
        :type initial_host_shape_name: str

        :param initial_host_ocpu_count:
            The value to assign to the initial_host_ocpu_count property of this Cluster.
        :type initial_host_ocpu_count: float

        :param is_shielded_instance_enabled:
            The value to assign to the is_shielded_instance_enabled property of this Cluster.
        :type is_shielded_instance_enabled: bool

        :param capacity_reservation_id:
            The value to assign to the capacity_reservation_id property of this Cluster.
        :type capacity_reservation_id: str

        :param datastores:
            The value to assign to the datastores property of this Cluster.
        :type datastores: list[oci.ocvp.models.DatastoreDetails]

        :param vsphere_type:
            The value to assign to the vsphere_type property of this Cluster.
            Allowed values for this property are: "MANAGEMENT", "WORKLOAD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vsphere_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Cluster.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Cluster.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compute_availability_domain': 'str',
            'display_name': 'str',
            'instance_display_name_prefix': 'str',
            'vmware_software_version': 'str',
            'esxi_software_version': 'str',
            'compartment_id': 'str',
            'sddc_id': 'str',
            'esxi_hosts_count': 'int',
            'initial_commitment': 'str',
            'workload_network_cidr': 'str',
            'network_configuration': 'NetworkConfiguration',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'upgrade_licenses': 'list[VsphereLicense]',
            'vsphere_upgrade_objects': 'list[VsphereUpgradeObject]',
            'initial_host_shape_name': 'str',
            'initial_host_ocpu_count': 'float',
            'is_shielded_instance_enabled': 'bool',
            'capacity_reservation_id': 'str',
            'datastores': 'list[DatastoreDetails]',
            'vsphere_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compute_availability_domain': 'computeAvailabilityDomain',
            'display_name': 'displayName',
            'instance_display_name_prefix': 'instanceDisplayNamePrefix',
            'vmware_software_version': 'vmwareSoftwareVersion',
            'esxi_software_version': 'esxiSoftwareVersion',
            'compartment_id': 'compartmentId',
            'sddc_id': 'sddcId',
            'esxi_hosts_count': 'esxiHostsCount',
            'initial_commitment': 'initialCommitment',
            'workload_network_cidr': 'workloadNetworkCidr',
            'network_configuration': 'networkConfiguration',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'upgrade_licenses': 'upgradeLicenses',
            'vsphere_upgrade_objects': 'vsphereUpgradeObjects',
            'initial_host_shape_name': 'initialHostShapeName',
            'initial_host_ocpu_count': 'initialHostOcpuCount',
            'is_shielded_instance_enabled': 'isShieldedInstanceEnabled',
            'capacity_reservation_id': 'capacityReservationId',
            'datastores': 'datastores',
            'vsphere_type': 'vsphereType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compute_availability_domain = None
        self._display_name = None
        self._instance_display_name_prefix = None
        self._vmware_software_version = None
        self._esxi_software_version = None
        self._compartment_id = None
        self._sddc_id = None
        self._esxi_hosts_count = None
        self._initial_commitment = None
        self._workload_network_cidr = None
        self._network_configuration = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._upgrade_licenses = None
        self._vsphere_upgrade_objects = None
        self._initial_host_shape_name = None
        self._initial_host_ocpu_count = None
        self._is_shielded_instance_enabled = None
        self._capacity_reservation_id = None
        self._datastores = None
        self._vsphere_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Cluster.
        The `OCID`__ of the Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Cluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Cluster.
        The `OCID`__ of the Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Cluster.
        :type: str
        """
        self._id = id

    @property
    def compute_availability_domain(self):
        """
        **[Required]** Gets the compute_availability_domain of this Cluster.
        The availability domain the ESXi hosts are running in. For Multi-AD Cluster, it is `multi-AD`.

        Example: `Uocm:PHX-AD-1`, `multi-AD`


        :return: The compute_availability_domain of this Cluster.
        :rtype: str
        """
        return self._compute_availability_domain

    @compute_availability_domain.setter
    def compute_availability_domain(self, compute_availability_domain):
        """
        Sets the compute_availability_domain of this Cluster.
        The availability domain the ESXi hosts are running in. For Multi-AD Cluster, it is `multi-AD`.

        Example: `Uocm:PHX-AD-1`, `multi-AD`


        :param compute_availability_domain: The compute_availability_domain of this Cluster.
        :type: str
        """
        self._compute_availability_domain = compute_availability_domain

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Cluster.
        A descriptive name for the Cluster. It must be unique, start with a letter, and contain only letters, digits,
        whitespaces, dashes and underscores.
        Avoid entering confidential information.


        :return: The display_name of this Cluster.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Cluster.
        A descriptive name for the Cluster. It must be unique, start with a letter, and contain only letters, digits,
        whitespaces, dashes and underscores.
        Avoid entering confidential information.


        :param display_name: The display_name of this Cluster.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_display_name_prefix(self):
        """
        Gets the instance_display_name_prefix of this Cluster.
        A prefix used in the name of each ESXi host and Compute instance in the Cluster.
        If this isn't set, the Cluster's `displayName` is used as the prefix.

        For example, if the value is `MyCluster`, the ESXi hosts are named `MyCluster-1`,
        `MyCluster-2`, and so on.


        :return: The instance_display_name_prefix of this Cluster.
        :rtype: str
        """
        return self._instance_display_name_prefix

    @instance_display_name_prefix.setter
    def instance_display_name_prefix(self, instance_display_name_prefix):
        """
        Sets the instance_display_name_prefix of this Cluster.
        A prefix used in the name of each ESXi host and Compute instance in the Cluster.
        If this isn't set, the Cluster's `displayName` is used as the prefix.

        For example, if the value is `MyCluster`, the ESXi hosts are named `MyCluster-1`,
        `MyCluster-2`, and so on.


        :param instance_display_name_prefix: The instance_display_name_prefix of this Cluster.
        :type: str
        """
        self._instance_display_name_prefix = instance_display_name_prefix

    @property
    def vmware_software_version(self):
        """
        **[Required]** Gets the vmware_software_version of this Cluster.
        In general, this is a specific version of bundled VMware software supported by
        Oracle Cloud VMware Solution (see
        :func:`list_supported_vmware_software_versions`).

        This attribute is not guaranteed to reflect the version of
        software currently installed on the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the version of software that the Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you upgrade the existing ESXi hosts in the Cluster to use a newer
        version of bundled VMware software supported by the Oracle Cloud VMware Solution, you
        should use :func:`update_cluster` to update the Cluster's
        `vmwareSoftwareVersion` with that new version.


        :return: The vmware_software_version of this Cluster.
        :rtype: str
        """
        return self._vmware_software_version

    @vmware_software_version.setter
    def vmware_software_version(self, vmware_software_version):
        """
        Sets the vmware_software_version of this Cluster.
        In general, this is a specific version of bundled VMware software supported by
        Oracle Cloud VMware Solution (see
        :func:`list_supported_vmware_software_versions`).

        This attribute is not guaranteed to reflect the version of
        software currently installed on the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the version of software that the Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you upgrade the existing ESXi hosts in the Cluster to use a newer
        version of bundled VMware software supported by the Oracle Cloud VMware Solution, you
        should use :func:`update_cluster` to update the Cluster's
        `vmwareSoftwareVersion` with that new version.


        :param vmware_software_version: The vmware_software_version of this Cluster.
        :type: str
        """
        self._vmware_software_version = vmware_software_version

    @property
    def esxi_software_version(self):
        """
        Gets the esxi_software_version of this Cluster.
        In general, this is a specific version of bundled ESXi software supported by
        Oracle Cloud VMware Solution (see
        :func:`list_supported_vmware_software_versions`).

        This attribute is not guaranteed to reflect the version of
        software currently installed on the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the version of software that the Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`
        unless a different version is configured on the ESXi host level.

        Therefore, if you upgrade the existing ESXi hosts in the Cluster to use a newer
        version of bundled ESXi software supported by the Oracle Cloud VMware Solution, you
        should use :func:`update_cluster` to update the Cluster's
        `esxiSoftwareVersion` with that new version.


        :return: The esxi_software_version of this Cluster.
        :rtype: str
        """
        return self._esxi_software_version

    @esxi_software_version.setter
    def esxi_software_version(self, esxi_software_version):
        """
        Sets the esxi_software_version of this Cluster.
        In general, this is a specific version of bundled ESXi software supported by
        Oracle Cloud VMware Solution (see
        :func:`list_supported_vmware_software_versions`).

        This attribute is not guaranteed to reflect the version of
        software currently installed on the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the version of software that the Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`
        unless a different version is configured on the ESXi host level.

        Therefore, if you upgrade the existing ESXi hosts in the Cluster to use a newer
        version of bundled ESXi software supported by the Oracle Cloud VMware Solution, you
        should use :func:`update_cluster` to update the Cluster's
        `esxiSoftwareVersion` with that new version.


        :param esxi_software_version: The esxi_software_version of this Cluster.
        :type: str
        """
        self._esxi_software_version = esxi_software_version

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Cluster.
        The `OCID`__ of the compartment that
        contains the Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Cluster.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Cluster.
        The `OCID`__ of the compartment that
        contains the Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Cluster.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def sddc_id(self):
        """
        **[Required]** Gets the sddc_id of this Cluster.
        The `OCID`__ of the SDDC that the
        Cluster belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sddc_id of this Cluster.
        :rtype: str
        """
        return self._sddc_id

    @sddc_id.setter
    def sddc_id(self, sddc_id):
        """
        Sets the sddc_id of this Cluster.
        The `OCID`__ of the SDDC that the
        Cluster belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sddc_id: The sddc_id of this Cluster.
        :type: str
        """
        self._sddc_id = sddc_id

    @property
    def esxi_hosts_count(self):
        """
        **[Required]** Gets the esxi_hosts_count of this Cluster.
        The number of ESXi hosts in the Cluster.


        :return: The esxi_hosts_count of this Cluster.
        :rtype: int
        """
        return self._esxi_hosts_count

    @esxi_hosts_count.setter
    def esxi_hosts_count(self, esxi_hosts_count):
        """
        Sets the esxi_hosts_count of this Cluster.
        The number of ESXi hosts in the Cluster.


        :param esxi_hosts_count: The esxi_hosts_count of this Cluster.
        :type: int
        """
        self._esxi_hosts_count = esxi_hosts_count

    @property
    def initial_commitment(self):
        """
        Gets the initial_commitment of this Cluster.
        The billing option selected during Cluster creation.
        :func:`list_supported_commitments`.

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The initial_commitment of this Cluster.
        :rtype: str
        """
        return self._initial_commitment

    @initial_commitment.setter
    def initial_commitment(self, initial_commitment):
        """
        Sets the initial_commitment of this Cluster.
        The billing option selected during Cluster creation.
        :func:`list_supported_commitments`.


        :param initial_commitment: The initial_commitment of this Cluster.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(initial_commitment, allowed_values):
            initial_commitment = 'UNKNOWN_ENUM_VALUE'
        self._initial_commitment = initial_commitment

    @property
    def workload_network_cidr(self):
        """
        Gets the workload_network_cidr of this Cluster.
        The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
        workloads.


        :return: The workload_network_cidr of this Cluster.
        :rtype: str
        """
        return self._workload_network_cidr

    @workload_network_cidr.setter
    def workload_network_cidr(self, workload_network_cidr):
        """
        Sets the workload_network_cidr of this Cluster.
        The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
        workloads.


        :param workload_network_cidr: The workload_network_cidr of this Cluster.
        :type: str
        """
        self._workload_network_cidr = workload_network_cidr

    @property
    def network_configuration(self):
        """
        **[Required]** Gets the network_configuration of this Cluster.

        :return: The network_configuration of this Cluster.
        :rtype: oci.ocvp.models.NetworkConfiguration
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        """
        Sets the network_configuration of this Cluster.

        :param network_configuration: The network_configuration of this Cluster.
        :type: oci.ocvp.models.NetworkConfiguration
        """
        self._network_configuration = network_configuration

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Cluster.
        The date and time the Cluster was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Cluster.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Cluster.
        The date and time the Cluster was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Cluster.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Cluster.
        The date and time the Cluster was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Cluster.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Cluster.
        The date and time the Cluster was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Cluster.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Cluster.
        The current state of the Cluster.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Cluster.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Cluster.
        The current state of the Cluster.


        :param lifecycle_state: The lifecycle_state of this Cluster.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def upgrade_licenses(self):
        """
        Gets the upgrade_licenses of this Cluster.
        The vSphere licenses to use when upgrading the Cluster.


        :return: The upgrade_licenses of this Cluster.
        :rtype: list[oci.ocvp.models.VsphereLicense]
        """
        return self._upgrade_licenses

    @upgrade_licenses.setter
    def upgrade_licenses(self, upgrade_licenses):
        """
        Sets the upgrade_licenses of this Cluster.
        The vSphere licenses to use when upgrading the Cluster.


        :param upgrade_licenses: The upgrade_licenses of this Cluster.
        :type: list[oci.ocvp.models.VsphereLicense]
        """
        self._upgrade_licenses = upgrade_licenses

    @property
    def vsphere_upgrade_objects(self):
        """
        Gets the vsphere_upgrade_objects of this Cluster.
        The links to binary objects needed to upgrade vSphere.


        :return: The vsphere_upgrade_objects of this Cluster.
        :rtype: list[oci.ocvp.models.VsphereUpgradeObject]
        """
        return self._vsphere_upgrade_objects

    @vsphere_upgrade_objects.setter
    def vsphere_upgrade_objects(self, vsphere_upgrade_objects):
        """
        Sets the vsphere_upgrade_objects of this Cluster.
        The links to binary objects needed to upgrade vSphere.


        :param vsphere_upgrade_objects: The vsphere_upgrade_objects of this Cluster.
        :type: list[oci.ocvp.models.VsphereUpgradeObject]
        """
        self._vsphere_upgrade_objects = vsphere_upgrade_objects

    @property
    def initial_host_shape_name(self):
        """
        **[Required]** Gets the initial_host_shape_name of this Cluster.
        The initial compute shape of the Cluster's ESXi hosts.
        :func:`list_supported_host_shapes`.


        :return: The initial_host_shape_name of this Cluster.
        :rtype: str
        """
        return self._initial_host_shape_name

    @initial_host_shape_name.setter
    def initial_host_shape_name(self, initial_host_shape_name):
        """
        Sets the initial_host_shape_name of this Cluster.
        The initial compute shape of the Cluster's ESXi hosts.
        :func:`list_supported_host_shapes`.


        :param initial_host_shape_name: The initial_host_shape_name of this Cluster.
        :type: str
        """
        self._initial_host_shape_name = initial_host_shape_name

    @property
    def initial_host_ocpu_count(self):
        """
        Gets the initial_host_ocpu_count of this Cluster.
        The initial OCPU count of the Cluster's ESXi hosts.


        :return: The initial_host_ocpu_count of this Cluster.
        :rtype: float
        """
        return self._initial_host_ocpu_count

    @initial_host_ocpu_count.setter
    def initial_host_ocpu_count(self, initial_host_ocpu_count):
        """
        Sets the initial_host_ocpu_count of this Cluster.
        The initial OCPU count of the Cluster's ESXi hosts.


        :param initial_host_ocpu_count: The initial_host_ocpu_count of this Cluster.
        :type: float
        """
        self._initial_host_ocpu_count = initial_host_ocpu_count

    @property
    def is_shielded_instance_enabled(self):
        """
        Gets the is_shielded_instance_enabled of this Cluster.
        Indicates whether shielded instance is enabled at the Cluster level.


        :return: The is_shielded_instance_enabled of this Cluster.
        :rtype: bool
        """
        return self._is_shielded_instance_enabled

    @is_shielded_instance_enabled.setter
    def is_shielded_instance_enabled(self, is_shielded_instance_enabled):
        """
        Sets the is_shielded_instance_enabled of this Cluster.
        Indicates whether shielded instance is enabled at the Cluster level.


        :param is_shielded_instance_enabled: The is_shielded_instance_enabled of this Cluster.
        :type: bool
        """
        self._is_shielded_instance_enabled = is_shielded_instance_enabled

    @property
    def capacity_reservation_id(self):
        """
        Gets the capacity_reservation_id of this Cluster.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The capacity_reservation_id of this Cluster.
        :rtype: str
        """
        return self._capacity_reservation_id

    @capacity_reservation_id.setter
    def capacity_reservation_id(self, capacity_reservation_id):
        """
        Sets the capacity_reservation_id of this Cluster.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param capacity_reservation_id: The capacity_reservation_id of this Cluster.
        :type: str
        """
        self._capacity_reservation_id = capacity_reservation_id

    @property
    def datastores(self):
        """
        Gets the datastores of this Cluster.
        Datastores used for the Cluster.


        :return: The datastores of this Cluster.
        :rtype: list[oci.ocvp.models.DatastoreDetails]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """
        Sets the datastores of this Cluster.
        Datastores used for the Cluster.


        :param datastores: The datastores of this Cluster.
        :type: list[oci.ocvp.models.DatastoreDetails]
        """
        self._datastores = datastores

    @property
    def vsphere_type(self):
        """
        **[Required]** Gets the vsphere_type of this Cluster.
        vSphere Cluster types.

        Allowed values for this property are: "MANAGEMENT", "WORKLOAD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vsphere_type of this Cluster.
        :rtype: str
        """
        return self._vsphere_type

    @vsphere_type.setter
    def vsphere_type(self, vsphere_type):
        """
        Sets the vsphere_type of this Cluster.
        vSphere Cluster types.


        :param vsphere_type: The vsphere_type of this Cluster.
        :type: str
        """
        allowed_values = ["MANAGEMENT", "WORKLOAD"]
        if not value_allowed_none_or_none_sentinel(vsphere_type, allowed_values):
            vsphere_type = 'UNKNOWN_ENUM_VALUE'
        self._vsphere_type = vsphere_type

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this Cluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Cluster.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Cluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Cluster.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this Cluster.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Cluster.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Cluster.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Cluster.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
