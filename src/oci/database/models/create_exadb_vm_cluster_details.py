# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExadbVmClusterDetails(object):
    """
    Details for the create Exadata VM cluster on Exascale Infrastructure operation. Applies to Exadata Database Service on Exascale Infrastructure only.
    """

    #: A constant which can be used with the license_model property of a CreateExadbVmClusterDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateExadbVmClusterDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExadbVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateExadbVmClusterDetails.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateExadbVmClusterDetails.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateExadbVmClusterDetails.
        :type subnet_id: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this CreateExadbVmClusterDetails.
        :type backup_subnet_id: str

        :param cluster_name:
            The value to assign to the cluster_name property of this CreateExadbVmClusterDetails.
        :type cluster_name: str

        :param display_name:
            The value to assign to the display_name property of this CreateExadbVmClusterDetails.
        :type display_name: str

        :param hostname:
            The value to assign to the hostname property of this CreateExadbVmClusterDetails.
        :type hostname: str

        :param domain:
            The value to assign to the domain property of this CreateExadbVmClusterDetails.
        :type domain: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this CreateExadbVmClusterDetails.
        :type ssh_public_keys: list[str]

        :param license_model:
            The value to assign to the license_model property of this CreateExadbVmClusterDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param time_zone:
            The value to assign to the time_zone property of this CreateExadbVmClusterDetails.
        :type time_zone: str

        :param scan_listener_port_tcp:
            The value to assign to the scan_listener_port_tcp property of this CreateExadbVmClusterDetails.
        :type scan_listener_port_tcp: int

        :param scan_listener_port_tcp_ssl:
            The value to assign to the scan_listener_port_tcp_ssl property of this CreateExadbVmClusterDetails.
        :type scan_listener_port_tcp_ssl: int

        :param private_zone_id:
            The value to assign to the private_zone_id property of this CreateExadbVmClusterDetails.
        :type private_zone_id: str

        :param shape:
            The value to assign to the shape property of this CreateExadbVmClusterDetails.
        :type shape: str

        :param node_count:
            The value to assign to the node_count property of this CreateExadbVmClusterDetails.
        :type node_count: int

        :param total_e_cpu_count:
            The value to assign to the total_e_cpu_count property of this CreateExadbVmClusterDetails.
        :type total_e_cpu_count: int

        :param enabled_e_cpu_count:
            The value to assign to the enabled_e_cpu_count property of this CreateExadbVmClusterDetails.
        :type enabled_e_cpu_count: int

        :param vm_file_system_storage:
            The value to assign to the vm_file_system_storage property of this CreateExadbVmClusterDetails.
        :type vm_file_system_storage: oci.database.models.ExadbVmClusterStorageDetails

        :param exascale_db_storage_vault_id:
            The value to assign to the exascale_db_storage_vault_id property of this CreateExadbVmClusterDetails.
        :type exascale_db_storage_vault_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateExadbVmClusterDetails.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this CreateExadbVmClusterDetails.
        :type backup_network_nsg_ids: list[str]

        :param grid_image_id:
            The value to assign to the grid_image_id property of this CreateExadbVmClusterDetails.
        :type grid_image_id: str

        :param system_version:
            The value to assign to the system_version property of this CreateExadbVmClusterDetails.
        :type system_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateExadbVmClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateExadbVmClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param data_collection_options:
            The value to assign to the data_collection_options property of this CreateExadbVmClusterDetails.
        :type data_collection_options: oci.database.models.DataCollectionOptions

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'backup_subnet_id': 'str',
            'cluster_name': 'str',
            'display_name': 'str',
            'hostname': 'str',
            'domain': 'str',
            'ssh_public_keys': 'list[str]',
            'license_model': 'str',
            'time_zone': 'str',
            'scan_listener_port_tcp': 'int',
            'scan_listener_port_tcp_ssl': 'int',
            'private_zone_id': 'str',
            'shape': 'str',
            'node_count': 'int',
            'total_e_cpu_count': 'int',
            'enabled_e_cpu_count': 'int',
            'vm_file_system_storage': 'ExadbVmClusterStorageDetails',
            'exascale_db_storage_vault_id': 'str',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'grid_image_id': 'str',
            'system_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'data_collection_options': 'DataCollectionOptions'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'backup_subnet_id': 'backupSubnetId',
            'cluster_name': 'clusterName',
            'display_name': 'displayName',
            'hostname': 'hostname',
            'domain': 'domain',
            'ssh_public_keys': 'sshPublicKeys',
            'license_model': 'licenseModel',
            'time_zone': 'timeZone',
            'scan_listener_port_tcp': 'scanListenerPortTcp',
            'scan_listener_port_tcp_ssl': 'scanListenerPortTcpSsl',
            'private_zone_id': 'privateZoneId',
            'shape': 'shape',
            'node_count': 'nodeCount',
            'total_e_cpu_count': 'totalECpuCount',
            'enabled_e_cpu_count': 'enabledECpuCount',
            'vm_file_system_storage': 'vmFileSystemStorage',
            'exascale_db_storage_vault_id': 'exascaleDbStorageVaultId',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'grid_image_id': 'gridImageId',
            'system_version': 'systemVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'data_collection_options': 'dataCollectionOptions'
        }

        self._compartment_id = None
        self._availability_domain = None
        self._subnet_id = None
        self._backup_subnet_id = None
        self._cluster_name = None
        self._display_name = None
        self._hostname = None
        self._domain = None
        self._ssh_public_keys = None
        self._license_model = None
        self._time_zone = None
        self._scan_listener_port_tcp = None
        self._scan_listener_port_tcp_ssl = None
        self._private_zone_id = None
        self._shape = None
        self._node_count = None
        self._total_e_cpu_count = None
        self._enabled_e_cpu_count = None
        self._vm_file_system_storage = None
        self._exascale_db_storage_vault_id = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._grid_image_id = None
        self._system_version = None
        self._freeform_tags = None
        self._defined_tags = None
        self._data_collection_options = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateExadbVmClusterDetails.
        The name of the availability domain in which the Exadata VM cluster on Exascale Infrastructure is located.


        :return: The availability_domain of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateExadbVmClusterDetails.
        The name of the availability domain in which the Exadata VM cluster on Exascale Infrastructure is located.


        :param availability_domain: The availability_domain of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the subnet associated with the Exadata VM cluster on Exascale Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the subnet associated with the Exadata VM cluster on Exascale Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def backup_subnet_id(self):
        """
        **[Required]** Gets the backup_subnet_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the backup network subnet associated with the Exadata VM cluster on Exascale Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The backup_subnet_id of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._backup_subnet_id

    @backup_subnet_id.setter
    def backup_subnet_id(self, backup_subnet_id):
        """
        Sets the backup_subnet_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the backup network subnet associated with the Exadata VM cluster on Exascale Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param backup_subnet_id: The backup_subnet_id of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._backup_subnet_id = backup_subnet_id

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this CreateExadbVmClusterDetails.
        The cluster name for Exadata VM cluster on Exascale Infrastructure. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :return: The cluster_name of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this CreateExadbVmClusterDetails.
        The cluster name for Exadata VM cluster on Exascale Infrastructure. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :param cluster_name: The cluster_name of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateExadbVmClusterDetails.
        The user-friendly name for the Exadata VM cluster on Exascale Infrastructure. The name does not need to be unique.


        :return: The display_name of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateExadbVmClusterDetails.
        The user-friendly name for the Exadata VM cluster on Exascale Infrastructure. The name does not need to be unique.


        :param display_name: The display_name of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this CreateExadbVmClusterDetails.
        The hostname for the Exadata VM cluster on Exascale Infrastructure. The hostname must begin with an alphabetic character, and
        can contain alphanumeric characters and hyphens (-). For Exadata systems, the maximum length of the hostname is 12 characters.

        The maximum length of the combined hostname and domain is 63 characters.

        **Note:** The hostname must be unique within the subnet. If it is not unique,
        then the Exadata VM cluster on Exascale Infrastructure will fail to provision.


        :return: The hostname of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CreateExadbVmClusterDetails.
        The hostname for the Exadata VM cluster on Exascale Infrastructure. The hostname must begin with an alphabetic character, and
        can contain alphanumeric characters and hyphens (-). For Exadata systems, the maximum length of the hostname is 12 characters.

        The maximum length of the combined hostname and domain is 63 characters.

        **Note:** The hostname must be unique within the subnet. If it is not unique,
        then the Exadata VM cluster on Exascale Infrastructure will fail to provision.


        :param hostname: The hostname of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def domain(self):
        """
        Gets the domain of this CreateExadbVmClusterDetails.
        A domain name used for the Exadata VM cluster on Exascale Infrastructure. If the Oracle-provided internet and VCN
        resolver is enabled for the specified subnet, then the domain name for the subnet is used
        (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
        Applies to Exadata Database Service on Exascale Infrastructure only.


        :return: The domain of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this CreateExadbVmClusterDetails.
        A domain name used for the Exadata VM cluster on Exascale Infrastructure. If the Oracle-provided internet and VCN
        resolver is enabled for the specified subnet, then the domain name for the subnet is used
        (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
        Applies to Exadata Database Service on Exascale Infrastructure only.


        :param domain: The domain of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._domain = domain

    @property
    def ssh_public_keys(self):
        """
        **[Required]** Gets the ssh_public_keys of this CreateExadbVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the Exadata VM cluster on Exascale Infrastructure.


        :return: The ssh_public_keys of this CreateExadbVmClusterDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this CreateExadbVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the Exadata VM cluster on Exascale Infrastructure.


        :param ssh_public_keys: The ssh_public_keys of this CreateExadbVmClusterDetails.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateExadbVmClusterDetails.
        The Oracle license model that applies to the Exadata VM cluster on Exascale Infrastructure. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateExadbVmClusterDetails.
        The Oracle license model that applies to the Exadata VM cluster on Exascale Infrastructure. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this CreateExadbVmClusterDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                f"Invalid value for `license_model`, must be None or one of {allowed_values}"
            )
        self._license_model = license_model

    @property
    def time_zone(self):
        """
        Gets the time_zone of this CreateExadbVmClusterDetails.
        The time zone to use for the Exadata VM cluster on Exascale Infrastructure. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CreateExadbVmClusterDetails.
        The time zone to use for the Exadata VM cluster on Exascale Infrastructure. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def scan_listener_port_tcp(self):
        """
        Gets the scan_listener_port_tcp of this CreateExadbVmClusterDetails.
        The TCP Single Client Access Name (SCAN) port. The default port is 1521.


        :return: The scan_listener_port_tcp of this CreateExadbVmClusterDetails.
        :rtype: int
        """
        return self._scan_listener_port_tcp

    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, scan_listener_port_tcp):
        """
        Sets the scan_listener_port_tcp of this CreateExadbVmClusterDetails.
        The TCP Single Client Access Name (SCAN) port. The default port is 1521.


        :param scan_listener_port_tcp: The scan_listener_port_tcp of this CreateExadbVmClusterDetails.
        :type: int
        """
        self._scan_listener_port_tcp = scan_listener_port_tcp

    @property
    def scan_listener_port_tcp_ssl(self):
        """
        Gets the scan_listener_port_tcp_ssl of this CreateExadbVmClusterDetails.
        The Secured Communication (TCPS) protocol Single Client Access Name (SCAN) port. The default port is 2484.


        :return: The scan_listener_port_tcp_ssl of this CreateExadbVmClusterDetails.
        :rtype: int
        """
        return self._scan_listener_port_tcp_ssl

    @scan_listener_port_tcp_ssl.setter
    def scan_listener_port_tcp_ssl(self, scan_listener_port_tcp_ssl):
        """
        Sets the scan_listener_port_tcp_ssl of this CreateExadbVmClusterDetails.
        The Secured Communication (TCPS) protocol Single Client Access Name (SCAN) port. The default port is 2484.


        :param scan_listener_port_tcp_ssl: The scan_listener_port_tcp_ssl of this CreateExadbVmClusterDetails.
        :type: int
        """
        self._scan_listener_port_tcp_ssl = scan_listener_port_tcp_ssl

    @property
    def private_zone_id(self):
        """
        Gets the private_zone_id of this CreateExadbVmClusterDetails.
        The private zone ID in which you want DNS records to be created.


        :return: The private_zone_id of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._private_zone_id

    @private_zone_id.setter
    def private_zone_id(self, private_zone_id):
        """
        Sets the private_zone_id of this CreateExadbVmClusterDetails.
        The private zone ID in which you want DNS records to be created.


        :param private_zone_id: The private_zone_id of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._private_zone_id = private_zone_id

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CreateExadbVmClusterDetails.
        The shape of the Exadata VM cluster on Exascale Infrastructure resource


        :return: The shape of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateExadbVmClusterDetails.
        The shape of the Exadata VM cluster on Exascale Infrastructure resource


        :param shape: The shape of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._shape = shape

    @property
    def node_count(self):
        """
        **[Required]** Gets the node_count of this CreateExadbVmClusterDetails.
        The number of nodes in the Exadata VM cluster on Exascale Infrastructure.


        :return: The node_count of this CreateExadbVmClusterDetails.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this CreateExadbVmClusterDetails.
        The number of nodes in the Exadata VM cluster on Exascale Infrastructure.


        :param node_count: The node_count of this CreateExadbVmClusterDetails.
        :type: int
        """
        self._node_count = node_count

    @property
    def total_e_cpu_count(self):
        """
        **[Required]** Gets the total_e_cpu_count of this CreateExadbVmClusterDetails.
        The number of Total ECPUs for an Exadata VM cluster on Exascale Infrastructure.


        :return: The total_e_cpu_count of this CreateExadbVmClusterDetails.
        :rtype: int
        """
        return self._total_e_cpu_count

    @total_e_cpu_count.setter
    def total_e_cpu_count(self, total_e_cpu_count):
        """
        Sets the total_e_cpu_count of this CreateExadbVmClusterDetails.
        The number of Total ECPUs for an Exadata VM cluster on Exascale Infrastructure.


        :param total_e_cpu_count: The total_e_cpu_count of this CreateExadbVmClusterDetails.
        :type: int
        """
        self._total_e_cpu_count = total_e_cpu_count

    @property
    def enabled_e_cpu_count(self):
        """
        **[Required]** Gets the enabled_e_cpu_count of this CreateExadbVmClusterDetails.
        The number of ECPUs to enable for an Exadata VM cluster on Exascale Infrastructure.


        :return: The enabled_e_cpu_count of this CreateExadbVmClusterDetails.
        :rtype: int
        """
        return self._enabled_e_cpu_count

    @enabled_e_cpu_count.setter
    def enabled_e_cpu_count(self, enabled_e_cpu_count):
        """
        Sets the enabled_e_cpu_count of this CreateExadbVmClusterDetails.
        The number of ECPUs to enable for an Exadata VM cluster on Exascale Infrastructure.


        :param enabled_e_cpu_count: The enabled_e_cpu_count of this CreateExadbVmClusterDetails.
        :type: int
        """
        self._enabled_e_cpu_count = enabled_e_cpu_count

    @property
    def vm_file_system_storage(self):
        """
        **[Required]** Gets the vm_file_system_storage of this CreateExadbVmClusterDetails.

        :return: The vm_file_system_storage of this CreateExadbVmClusterDetails.
        :rtype: oci.database.models.ExadbVmClusterStorageDetails
        """
        return self._vm_file_system_storage

    @vm_file_system_storage.setter
    def vm_file_system_storage(self, vm_file_system_storage):
        """
        Sets the vm_file_system_storage of this CreateExadbVmClusterDetails.

        :param vm_file_system_storage: The vm_file_system_storage of this CreateExadbVmClusterDetails.
        :type: oci.database.models.ExadbVmClusterStorageDetails
        """
        self._vm_file_system_storage = vm_file_system_storage

    @property
    def exascale_db_storage_vault_id(self):
        """
        **[Required]** Gets the exascale_db_storage_vault_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the Exadata Database Storage Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exascale_db_storage_vault_id of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._exascale_db_storage_vault_id

    @exascale_db_storage_vault_id.setter
    def exascale_db_storage_vault_id(self, exascale_db_storage_vault_id):
        """
        Sets the exascale_db_storage_vault_id of this CreateExadbVmClusterDetails.
        The `OCID`__ of the Exadata Database Storage Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exascale_db_storage_vault_id: The exascale_db_storage_vault_id of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._exascale_db_storage_vault_id = exascale_db_storage_vault_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateExadbVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CreateExadbVmClusterDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateExadbVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CreateExadbVmClusterDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this CreateExadbVmClusterDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this CreateExadbVmClusterDetails.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this CreateExadbVmClusterDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this CreateExadbVmClusterDetails.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def grid_image_id(self):
        """
        **[Required]** Gets the grid_image_id of this CreateExadbVmClusterDetails.
        Grid Setup will be done using this grid image id


        :return: The grid_image_id of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._grid_image_id

    @grid_image_id.setter
    def grid_image_id(self, grid_image_id):
        """
        Sets the grid_image_id of this CreateExadbVmClusterDetails.
        Grid Setup will be done using this grid image id


        :param grid_image_id: The grid_image_id of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._grid_image_id = grid_image_id

    @property
    def system_version(self):
        """
        Gets the system_version of this CreateExadbVmClusterDetails.
        Operating system version of the image.


        :return: The system_version of this CreateExadbVmClusterDetails.
        :rtype: str
        """
        return self._system_version

    @system_version.setter
    def system_version(self, system_version):
        """
        Sets the system_version of this CreateExadbVmClusterDetails.
        Operating system version of the image.


        :param system_version: The system_version of this CreateExadbVmClusterDetails.
        :type: str
        """
        self._system_version = system_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateExadbVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateExadbVmClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateExadbVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateExadbVmClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateExadbVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateExadbVmClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateExadbVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateExadbVmClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def data_collection_options(self):
        """
        Gets the data_collection_options of this CreateExadbVmClusterDetails.

        :return: The data_collection_options of this CreateExadbVmClusterDetails.
        :rtype: oci.database.models.DataCollectionOptions
        """
        return self._data_collection_options

    @data_collection_options.setter
    def data_collection_options(self, data_collection_options):
        """
        Sets the data_collection_options of this CreateExadbVmClusterDetails.

        :param data_collection_options: The data_collection_options of this CreateExadbVmClusterDetails.
        :type: oci.database.models.DataCollectionOptions
        """
        self._data_collection_options = data_collection_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
