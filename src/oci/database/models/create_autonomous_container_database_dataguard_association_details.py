# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousContainerDatabaseDataguardAssociationDetails(object):
    """
    Create Autonomous Dataguard Association to an existing Autonomous Container Database
    """

    #: A constant which can be used with the protection_mode property of a CreateAutonomousContainerDatabaseDataguardAssociationDetails.
    #: This constant has a value of "MAXIMUM_AVAILABILITY"
    PROTECTION_MODE_MAXIMUM_AVAILABILITY = "MAXIMUM_AVAILABILITY"

    #: A constant which can be used with the protection_mode property of a CreateAutonomousContainerDatabaseDataguardAssociationDetails.
    #: This constant has a value of "MAXIMUM_PERFORMANCE"
    PROTECTION_MODE_MAXIMUM_PERFORMANCE = "MAXIMUM_PERFORMANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousContainerDatabaseDataguardAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_autonomous_container_database_display_name:
            The value to assign to the peer_autonomous_container_database_display_name property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type peer_autonomous_container_database_display_name: str

        :param peer_autonomous_container_database_compartment_id:
            The value to assign to the peer_autonomous_container_database_compartment_id property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type peer_autonomous_container_database_compartment_id: str

        :param peer_cloud_autonomous_vm_cluster_id:
            The value to assign to the peer_cloud_autonomous_vm_cluster_id property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type peer_cloud_autonomous_vm_cluster_id: str

        :param peer_autonomous_container_database_backup_config:
            The value to assign to the peer_autonomous_container_database_backup_config property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type peer_autonomous_container_database_backup_config: oci.database.models.PeerAutonomousContainerDatabaseBackupConfig

        :param is_automatic_failover_enabled:
            The value to assign to the is_automatic_failover_enabled property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type is_automatic_failover_enabled: bool

        :param protection_mode:
            The value to assign to the protection_mode property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE"
        :type protection_mode: str

        :param fast_start_fail_over_lag_limit_in_seconds:
            The value to assign to the fast_start_fail_over_lag_limit_in_seconds property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type fast_start_fail_over_lag_limit_in_seconds: int

        :param standby_maintenance_buffer_in_days:
            The value to assign to the standby_maintenance_buffer_in_days property of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type standby_maintenance_buffer_in_days: int

        """
        self.swagger_types = {
            'peer_autonomous_container_database_display_name': 'str',
            'peer_autonomous_container_database_compartment_id': 'str',
            'peer_cloud_autonomous_vm_cluster_id': 'str',
            'peer_autonomous_container_database_backup_config': 'PeerAutonomousContainerDatabaseBackupConfig',
            'is_automatic_failover_enabled': 'bool',
            'protection_mode': 'str',
            'fast_start_fail_over_lag_limit_in_seconds': 'int',
            'standby_maintenance_buffer_in_days': 'int'
        }

        self.attribute_map = {
            'peer_autonomous_container_database_display_name': 'peerAutonomousContainerDatabaseDisplayName',
            'peer_autonomous_container_database_compartment_id': 'peerAutonomousContainerDatabaseCompartmentId',
            'peer_cloud_autonomous_vm_cluster_id': 'peerCloudAutonomousVmClusterId',
            'peer_autonomous_container_database_backup_config': 'peerAutonomousContainerDatabaseBackupConfig',
            'is_automatic_failover_enabled': 'isAutomaticFailoverEnabled',
            'protection_mode': 'protectionMode',
            'fast_start_fail_over_lag_limit_in_seconds': 'fastStartFailOverLagLimitInSeconds',
            'standby_maintenance_buffer_in_days': 'standbyMaintenanceBufferInDays'
        }

        self._peer_autonomous_container_database_display_name = None
        self._peer_autonomous_container_database_compartment_id = None
        self._peer_cloud_autonomous_vm_cluster_id = None
        self._peer_autonomous_container_database_backup_config = None
        self._is_automatic_failover_enabled = None
        self._protection_mode = None
        self._fast_start_fail_over_lag_limit_in_seconds = None
        self._standby_maintenance_buffer_in_days = None

    @property
    def peer_autonomous_container_database_display_name(self):
        """
        **[Required]** Gets the peer_autonomous_container_database_display_name of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The display name for the peer Autonomous Container Database.


        :return: The peer_autonomous_container_database_display_name of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: str
        """
        return self._peer_autonomous_container_database_display_name

    @peer_autonomous_container_database_display_name.setter
    def peer_autonomous_container_database_display_name(self, peer_autonomous_container_database_display_name):
        """
        Sets the peer_autonomous_container_database_display_name of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The display name for the peer Autonomous Container Database.


        :param peer_autonomous_container_database_display_name: The peer_autonomous_container_database_display_name of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: str
        """
        self._peer_autonomous_container_database_display_name = peer_autonomous_container_database_display_name

    @property
    def peer_autonomous_container_database_compartment_id(self):
        """
        Gets the peer_autonomous_container_database_compartment_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The `OCID`__ of the compartment where the standby Autonomous Container Database
        will be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_autonomous_container_database_compartment_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: str
        """
        return self._peer_autonomous_container_database_compartment_id

    @peer_autonomous_container_database_compartment_id.setter
    def peer_autonomous_container_database_compartment_id(self, peer_autonomous_container_database_compartment_id):
        """
        Sets the peer_autonomous_container_database_compartment_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The `OCID`__ of the compartment where the standby Autonomous Container Database
        will be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_autonomous_container_database_compartment_id: The peer_autonomous_container_database_compartment_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: str
        """
        self._peer_autonomous_container_database_compartment_id = peer_autonomous_container_database_compartment_id

    @property
    def peer_cloud_autonomous_vm_cluster_id(self):
        """
        **[Required]** Gets the peer_cloud_autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The `OCID`__ of the peer cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_cloud_autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: str
        """
        return self._peer_cloud_autonomous_vm_cluster_id

    @peer_cloud_autonomous_vm_cluster_id.setter
    def peer_cloud_autonomous_vm_cluster_id(self, peer_cloud_autonomous_vm_cluster_id):
        """
        Sets the peer_cloud_autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The `OCID`__ of the peer cloud Autonomous Exadata VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_cloud_autonomous_vm_cluster_id: The peer_cloud_autonomous_vm_cluster_id of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: str
        """
        self._peer_cloud_autonomous_vm_cluster_id = peer_cloud_autonomous_vm_cluster_id

    @property
    def peer_autonomous_container_database_backup_config(self):
        """
        Gets the peer_autonomous_container_database_backup_config of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.

        :return: The peer_autonomous_container_database_backup_config of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: oci.database.models.PeerAutonomousContainerDatabaseBackupConfig
        """
        return self._peer_autonomous_container_database_backup_config

    @peer_autonomous_container_database_backup_config.setter
    def peer_autonomous_container_database_backup_config(self, peer_autonomous_container_database_backup_config):
        """
        Sets the peer_autonomous_container_database_backup_config of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.

        :param peer_autonomous_container_database_backup_config: The peer_autonomous_container_database_backup_config of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: oci.database.models.PeerAutonomousContainerDatabaseBackupConfig
        """
        self._peer_autonomous_container_database_backup_config = peer_autonomous_container_database_backup_config

    @property
    def is_automatic_failover_enabled(self):
        """
        Gets the is_automatic_failover_enabled of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :return: The is_automatic_failover_enabled of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: bool
        """
        return self._is_automatic_failover_enabled

    @is_automatic_failover_enabled.setter
    def is_automatic_failover_enabled(self, is_automatic_failover_enabled):
        """
        Sets the is_automatic_failover_enabled of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :param is_automatic_failover_enabled: The is_automatic_failover_enabled of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: bool
        """
        self._is_automatic_failover_enabled = is_automatic_failover_enabled

    @property
    def protection_mode(self):
        """
        **[Required]** Gets the protection_mode of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The protection mode of this Autonomous Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE"


        :return: The protection_mode of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The protection mode of this Autonomous Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            raise ValueError(
                f"Invalid value for `protection_mode`, must be None or one of {allowed_values}"
            )
        self._protection_mode = protection_mode

    @property
    def fast_start_fail_over_lag_limit_in_seconds(self):
        """
        Gets the fast_start_fail_over_lag_limit_in_seconds of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The lag time for my preference based on data loss tolerance in seconds.


        :return: The fast_start_fail_over_lag_limit_in_seconds of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: int
        """
        return self._fast_start_fail_over_lag_limit_in_seconds

    @fast_start_fail_over_lag_limit_in_seconds.setter
    def fast_start_fail_over_lag_limit_in_seconds(self, fast_start_fail_over_lag_limit_in_seconds):
        """
        Sets the fast_start_fail_over_lag_limit_in_seconds of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The lag time for my preference based on data loss tolerance in seconds.


        :param fast_start_fail_over_lag_limit_in_seconds: The fast_start_fail_over_lag_limit_in_seconds of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: int
        """
        self._fast_start_fail_over_lag_limit_in_seconds = fast_start_fail_over_lag_limit_in_seconds

    @property
    def standby_maintenance_buffer_in_days(self):
        """
        Gets the standby_maintenance_buffer_in_days of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database.
        This value represents the number of days before scheduled maintenance of the primary database.


        :return: The standby_maintenance_buffer_in_days of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :rtype: int
        """
        return self._standby_maintenance_buffer_in_days

    @standby_maintenance_buffer_in_days.setter
    def standby_maintenance_buffer_in_days(self, standby_maintenance_buffer_in_days):
        """
        Sets the standby_maintenance_buffer_in_days of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database.
        This value represents the number of days before scheduled maintenance of the primary database.


        :param standby_maintenance_buffer_in_days: The standby_maintenance_buffer_in_days of this CreateAutonomousContainerDatabaseDataguardAssociationDetails.
        :type: int
        """
        self._standby_maintenance_buffer_in_days = standby_maintenance_buffer_in_days

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
