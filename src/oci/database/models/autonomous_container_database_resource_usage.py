# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousContainerDatabaseResourceUsage(object):
    """
    Associated autonomous container databases usages.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousContainerDatabaseResourceUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousContainerDatabaseResourceUsage.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AutonomousContainerDatabaseResourceUsage.
        :type display_name: str

        :param reclaimable_cpus:
            The value to assign to the reclaimable_cpus property of this AutonomousContainerDatabaseResourceUsage.
        :type reclaimable_cpus: float

        :param available_cpus:
            The value to assign to the available_cpus property of this AutonomousContainerDatabaseResourceUsage.
        :type available_cpus: float

        :param largest_provisionable_autonomous_database_in_cpus:
            The value to assign to the largest_provisionable_autonomous_database_in_cpus property of this AutonomousContainerDatabaseResourceUsage.
        :type largest_provisionable_autonomous_database_in_cpus: float

        :param provisioned_cpus:
            The value to assign to the provisioned_cpus property of this AutonomousContainerDatabaseResourceUsage.
        :type provisioned_cpus: float

        :param reserved_cpus:
            The value to assign to the reserved_cpus property of this AutonomousContainerDatabaseResourceUsage.
        :type reserved_cpus: float

        :param used_cpus:
            The value to assign to the used_cpus property of this AutonomousContainerDatabaseResourceUsage.
        :type used_cpus: float

        :param provisionable_cpus:
            The value to assign to the provisionable_cpus property of this AutonomousContainerDatabaseResourceUsage.
        :type provisionable_cpus: list[float]

        :param autonomous_container_database_vm_usage:
            The value to assign to the autonomous_container_database_vm_usage property of this AutonomousContainerDatabaseResourceUsage.
        :type autonomous_container_database_vm_usage: list[oci.database.models.AcdAvmResourceStats]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousContainerDatabaseResourceUsage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousContainerDatabaseResourceUsage.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'reclaimable_cpus': 'float',
            'available_cpus': 'float',
            'largest_provisionable_autonomous_database_in_cpus': 'float',
            'provisioned_cpus': 'float',
            'reserved_cpus': 'float',
            'used_cpus': 'float',
            'provisionable_cpus': 'list[float]',
            'autonomous_container_database_vm_usage': 'list[AcdAvmResourceStats]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'reclaimable_cpus': 'reclaimableCpus',
            'available_cpus': 'availableCpus',
            'largest_provisionable_autonomous_database_in_cpus': 'largestProvisionableAutonomousDatabaseInCpus',
            'provisioned_cpus': 'provisionedCpus',
            'reserved_cpus': 'reservedCpus',
            'used_cpus': 'usedCpus',
            'provisionable_cpus': 'provisionableCpus',
            'autonomous_container_database_vm_usage': 'autonomousContainerDatabaseVmUsage',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._reclaimable_cpus = None
        self._available_cpus = None
        self._largest_provisionable_autonomous_database_in_cpus = None
        self._provisioned_cpus = None
        self._reserved_cpus = None
        self._used_cpus = None
        self._provisionable_cpus = None
        self._autonomous_container_database_vm_usage = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this AutonomousContainerDatabaseResourceUsage.
        The `OCID`__ of the Autonomous Container Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousContainerDatabaseResourceUsage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousContainerDatabaseResourceUsage.
        The `OCID`__ of the Autonomous Container Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousContainerDatabaseResourceUsage.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutonomousContainerDatabaseResourceUsage.
        The user-friendly name for the Autonomous Container Database. The name does not need to be unique.


        :return: The display_name of this AutonomousContainerDatabaseResourceUsage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousContainerDatabaseResourceUsage.
        The user-friendly name for the Autonomous Container Database. The name does not need to be unique.


        :param display_name: The display_name of this AutonomousContainerDatabaseResourceUsage.
        :type: str
        """
        self._display_name = display_name

    @property
    def reclaimable_cpus(self):
        """
        Gets the reclaimable_cpus of this AutonomousContainerDatabaseResourceUsage.
        Number of CPUs that are reclaimable or released to the AVMC on Autonomous Container Database restart.


        :return: The reclaimable_cpus of this AutonomousContainerDatabaseResourceUsage.
        :rtype: float
        """
        return self._reclaimable_cpus

    @reclaimable_cpus.setter
    def reclaimable_cpus(self, reclaimable_cpus):
        """
        Sets the reclaimable_cpus of this AutonomousContainerDatabaseResourceUsage.
        Number of CPUs that are reclaimable or released to the AVMC on Autonomous Container Database restart.


        :param reclaimable_cpus: The reclaimable_cpus of this AutonomousContainerDatabaseResourceUsage.
        :type: float
        """
        self._reclaimable_cpus = reclaimable_cpus

    @property
    def available_cpus(self):
        """
        Gets the available_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs available for provisioning or scaling an Autonomous Database in the Autonomous Container Database.


        :return: The available_cpus of this AutonomousContainerDatabaseResourceUsage.
        :rtype: float
        """
        return self._available_cpus

    @available_cpus.setter
    def available_cpus(self, available_cpus):
        """
        Sets the available_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs available for provisioning or scaling an Autonomous Database in the Autonomous Container Database.


        :param available_cpus: The available_cpus of this AutonomousContainerDatabaseResourceUsage.
        :type: float
        """
        self._available_cpus = available_cpus

    @property
    def largest_provisionable_autonomous_database_in_cpus(self):
        """
        Gets the largest_provisionable_autonomous_database_in_cpus of this AutonomousContainerDatabaseResourceUsage.
        Largest provisionable ADB in the Autonomous Container Database.


        :return: The largest_provisionable_autonomous_database_in_cpus of this AutonomousContainerDatabaseResourceUsage.
        :rtype: float
        """
        return self._largest_provisionable_autonomous_database_in_cpus

    @largest_provisionable_autonomous_database_in_cpus.setter
    def largest_provisionable_autonomous_database_in_cpus(self, largest_provisionable_autonomous_database_in_cpus):
        """
        Sets the largest_provisionable_autonomous_database_in_cpus of this AutonomousContainerDatabaseResourceUsage.
        Largest provisionable ADB in the Autonomous Container Database.


        :param largest_provisionable_autonomous_database_in_cpus: The largest_provisionable_autonomous_database_in_cpus of this AutonomousContainerDatabaseResourceUsage.
        :type: float
        """
        self._largest_provisionable_autonomous_database_in_cpus = largest_provisionable_autonomous_database_in_cpus

    @property
    def provisioned_cpus(self):
        """
        Gets the provisioned_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs / cores assigned to ADBs in the Autonomous Container Database.


        :return: The provisioned_cpus of this AutonomousContainerDatabaseResourceUsage.
        :rtype: float
        """
        return self._provisioned_cpus

    @provisioned_cpus.setter
    def provisioned_cpus(self, provisioned_cpus):
        """
        Sets the provisioned_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs / cores assigned to ADBs in the Autonomous Container Database.


        :param provisioned_cpus: The provisioned_cpus of this AutonomousContainerDatabaseResourceUsage.
        :type: float
        """
        self._provisioned_cpus = provisioned_cpus

    @property
    def reserved_cpus(self):
        """
        Gets the reserved_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs / cores reserved for scalability, resilliency and other overheads.
        This includes failover, autoscaling and idle instance overhead.


        :return: The reserved_cpus of this AutonomousContainerDatabaseResourceUsage.
        :rtype: float
        """
        return self._reserved_cpus

    @reserved_cpus.setter
    def reserved_cpus(self, reserved_cpus):
        """
        Sets the reserved_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs / cores reserved for scalability, resilliency and other overheads.
        This includes failover, autoscaling and idle instance overhead.


        :param reserved_cpus: The reserved_cpus of this AutonomousContainerDatabaseResourceUsage.
        :type: float
        """
        self._reserved_cpus = reserved_cpus

    @property
    def used_cpus(self):
        """
        Gets the used_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs / cores assigned to the Autonomous Container Database. Sum of provisioned,
        reserved and reclaimable CPUs/ cores.


        :return: The used_cpus of this AutonomousContainerDatabaseResourceUsage.
        :rtype: float
        """
        return self._used_cpus

    @used_cpus.setter
    def used_cpus(self, used_cpus):
        """
        Sets the used_cpus of this AutonomousContainerDatabaseResourceUsage.
        CPUs / cores assigned to the Autonomous Container Database. Sum of provisioned,
        reserved and reclaimable CPUs/ cores.


        :param used_cpus: The used_cpus of this AutonomousContainerDatabaseResourceUsage.
        :type: float
        """
        self._used_cpus = used_cpus

    @property
    def provisionable_cpus(self):
        """
        Gets the provisionable_cpus of this AutonomousContainerDatabaseResourceUsage.
        Valid list of provisionable CPUs for Autonomous Database.


        :return: The provisionable_cpus of this AutonomousContainerDatabaseResourceUsage.
        :rtype: list[float]
        """
        return self._provisionable_cpus

    @provisionable_cpus.setter
    def provisionable_cpus(self, provisionable_cpus):
        """
        Sets the provisionable_cpus of this AutonomousContainerDatabaseResourceUsage.
        Valid list of provisionable CPUs for Autonomous Database.


        :param provisionable_cpus: The provisionable_cpus of this AutonomousContainerDatabaseResourceUsage.
        :type: list[float]
        """
        self._provisionable_cpus = provisionable_cpus

    @property
    def autonomous_container_database_vm_usage(self):
        """
        Gets the autonomous_container_database_vm_usage of this AutonomousContainerDatabaseResourceUsage.
        List of autonomous container database resource usage per autonomous virtual machine.


        :return: The autonomous_container_database_vm_usage of this AutonomousContainerDatabaseResourceUsage.
        :rtype: list[oci.database.models.AcdAvmResourceStats]
        """
        return self._autonomous_container_database_vm_usage

    @autonomous_container_database_vm_usage.setter
    def autonomous_container_database_vm_usage(self, autonomous_container_database_vm_usage):
        """
        Sets the autonomous_container_database_vm_usage of this AutonomousContainerDatabaseResourceUsage.
        List of autonomous container database resource usage per autonomous virtual machine.


        :param autonomous_container_database_vm_usage: The autonomous_container_database_vm_usage of this AutonomousContainerDatabaseResourceUsage.
        :type: list[oci.database.models.AcdAvmResourceStats]
        """
        self._autonomous_container_database_vm_usage = autonomous_container_database_vm_usage

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousContainerDatabaseResourceUsage.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousContainerDatabaseResourceUsage.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousContainerDatabaseResourceUsage.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousContainerDatabaseResourceUsage.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousContainerDatabaseResourceUsage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousContainerDatabaseResourceUsage.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousContainerDatabaseResourceUsage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousContainerDatabaseResourceUsage.
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
