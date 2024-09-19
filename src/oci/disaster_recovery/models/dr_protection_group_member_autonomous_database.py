# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .dr_protection_group_member import DrProtectionGroupMember
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrProtectionGroupMemberAutonomousDatabase(DrProtectionGroupMember):
    """
    The properties for an Autonomous Database Serverless member of a DR protection group.
    """

    #: A constant which can be used with the autonomous_database_standby_type_for_dr_drills property of a DrProtectionGroupMemberAutonomousDatabase.
    #: This constant has a value of "FULL_CLONE"
    AUTONOMOUS_DATABASE_STANDBY_TYPE_FOR_DR_DRILLS_FULL_CLONE = "FULL_CLONE"

    #: A constant which can be used with the autonomous_database_standby_type_for_dr_drills property of a DrProtectionGroupMemberAutonomousDatabase.
    #: This constant has a value of "REFRESHABLE_CLONE"
    AUTONOMOUS_DATABASE_STANDBY_TYPE_FOR_DR_DRILLS_REFRESHABLE_CLONE = "REFRESHABLE_CLONE"

    #: A constant which can be used with the autonomous_database_standby_type_for_dr_drills property of a DrProtectionGroupMemberAutonomousDatabase.
    #: This constant has a value of "SNAPSHOT_STANDBY"
    AUTONOMOUS_DATABASE_STANDBY_TYPE_FOR_DR_DRILLS_SNAPSHOT_STANDBY = "SNAPSHOT_STANDBY"

    def __init__(self, **kwargs):
        """
        Initializes a new DrProtectionGroupMemberAutonomousDatabase object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.DrProtectionGroupMemberAutonomousDatabase.member_type` attribute
        of this class is ``AUTONOMOUS_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this DrProtectionGroupMemberAutonomousDatabase.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this DrProtectionGroupMemberAutonomousDatabase.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OBJECT_STORAGE_BUCKET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type member_type: str

        :param autonomous_database_standby_type_for_dr_drills:
            The value to assign to the autonomous_database_standby_type_for_dr_drills property of this DrProtectionGroupMemberAutonomousDatabase.
            Allowed values for this property are: "FULL_CLONE", "REFRESHABLE_CLONE", "SNAPSHOT_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type autonomous_database_standby_type_for_dr_drills: str

        :param password_vault_secret_id:
            The value to assign to the password_vault_secret_id property of this DrProtectionGroupMemberAutonomousDatabase.
        :type password_vault_secret_id: str

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'autonomous_database_standby_type_for_dr_drills': 'str',
            'password_vault_secret_id': 'str'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'autonomous_database_standby_type_for_dr_drills': 'autonomousDatabaseStandbyTypeForDrDrills',
            'password_vault_secret_id': 'passwordVaultSecretId'
        }

        self._member_id = None
        self._member_type = None
        self._autonomous_database_standby_type_for_dr_drills = None
        self._password_vault_secret_id = None
        self._member_type = 'AUTONOMOUS_DATABASE'

    @property
    def autonomous_database_standby_type_for_dr_drills(self):
        """
        Gets the autonomous_database_standby_type_for_dr_drills of this DrProtectionGroupMemberAutonomousDatabase.
        This specifies the mechanism used to create a temporary Autonomous Database instance for DR Drills.
        See https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-clone-about.html for information about these clone types.
        See https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-data-guard-snapshot-standby.html for information about snapshot standby.

        Allowed values for this property are: "FULL_CLONE", "REFRESHABLE_CLONE", "SNAPSHOT_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The autonomous_database_standby_type_for_dr_drills of this DrProtectionGroupMemberAutonomousDatabase.
        :rtype: str
        """
        return self._autonomous_database_standby_type_for_dr_drills

    @autonomous_database_standby_type_for_dr_drills.setter
    def autonomous_database_standby_type_for_dr_drills(self, autonomous_database_standby_type_for_dr_drills):
        """
        Sets the autonomous_database_standby_type_for_dr_drills of this DrProtectionGroupMemberAutonomousDatabase.
        This specifies the mechanism used to create a temporary Autonomous Database instance for DR Drills.
        See https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-clone-about.html for information about these clone types.
        See https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-data-guard-snapshot-standby.html for information about snapshot standby.


        :param autonomous_database_standby_type_for_dr_drills: The autonomous_database_standby_type_for_dr_drills of this DrProtectionGroupMemberAutonomousDatabase.
        :type: str
        """
        allowed_values = ["FULL_CLONE", "REFRESHABLE_CLONE", "SNAPSHOT_STANDBY"]
        if not value_allowed_none_or_none_sentinel(autonomous_database_standby_type_for_dr_drills, allowed_values):
            autonomous_database_standby_type_for_dr_drills = 'UNKNOWN_ENUM_VALUE'
        self._autonomous_database_standby_type_for_dr_drills = autonomous_database_standby_type_for_dr_drills

    @property
    def password_vault_secret_id(self):
        """
        Gets the password_vault_secret_id of this DrProtectionGroupMemberAutonomousDatabase.
        The OCID of the vault secret where the database SYSDBA password is stored.
        This password is required and used for performing database DR Drill operations when using full clone.

        Example: `ocid1.vaultsecret.oc1..uniqueID`


        :return: The password_vault_secret_id of this DrProtectionGroupMemberAutonomousDatabase.
        :rtype: str
        """
        return self._password_vault_secret_id

    @password_vault_secret_id.setter
    def password_vault_secret_id(self, password_vault_secret_id):
        """
        Sets the password_vault_secret_id of this DrProtectionGroupMemberAutonomousDatabase.
        The OCID of the vault secret where the database SYSDBA password is stored.
        This password is required and used for performing database DR Drill operations when using full clone.

        Example: `ocid1.vaultsecret.oc1..uniqueID`


        :param password_vault_secret_id: The password_vault_secret_id of this DrProtectionGroupMemberAutonomousDatabase.
        :type: str
        """
        self._password_vault_secret_id = password_vault_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
