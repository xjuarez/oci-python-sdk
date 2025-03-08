# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrProtectionGroupMemberDetails(object):
    """
    Create properties for a member in a DR protection group.
    """

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "COMPUTE_INSTANCE"
    MEMBER_TYPE_COMPUTE_INSTANCE = "COMPUTE_INSTANCE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "COMPUTE_INSTANCE_MOVABLE"
    MEMBER_TYPE_COMPUTE_INSTANCE_MOVABLE = "COMPUTE_INSTANCE_MOVABLE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "COMPUTE_INSTANCE_NON_MOVABLE"
    MEMBER_TYPE_COMPUTE_INSTANCE_NON_MOVABLE = "COMPUTE_INSTANCE_NON_MOVABLE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "VOLUME_GROUP"
    MEMBER_TYPE_VOLUME_GROUP = "VOLUME_GROUP"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "DATABASE"
    MEMBER_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "AUTONOMOUS_DATABASE"
    MEMBER_TYPE_AUTONOMOUS_DATABASE = "AUTONOMOUS_DATABASE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "AUTONOMOUS_CONTAINER_DATABASE"
    MEMBER_TYPE_AUTONOMOUS_CONTAINER_DATABASE = "AUTONOMOUS_CONTAINER_DATABASE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "LOAD_BALANCER"
    MEMBER_TYPE_LOAD_BALANCER = "LOAD_BALANCER"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "NETWORK_LOAD_BALANCER"
    MEMBER_TYPE_NETWORK_LOAD_BALANCER = "NETWORK_LOAD_BALANCER"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "FILE_SYSTEM"
    MEMBER_TYPE_FILE_SYSTEM = "FILE_SYSTEM"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "OKE_CLUSTER"
    MEMBER_TYPE_OKE_CLUSTER = "OKE_CLUSTER"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "OBJECT_STORAGE_BUCKET"
    MEMBER_TYPE_OBJECT_STORAGE_BUCKET = "OBJECT_STORAGE_BUCKET"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrProtectionGroupMemberDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberComputeInstanceMovableDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberAutonomousContainerDatabaseDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberComputeInstanceNonMovableDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberComputeInstanceDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberDatabaseDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberAutonomousDatabaseDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberNetworkLoadBalancerDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberVolumeGroupDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberOkeClusterDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberFileSystemDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberObjectStorageBucketDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberLoadBalancerDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this CreateDrProtectionGroupMemberDetails.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this CreateDrProtectionGroupMemberDetails.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OKE_CLUSTER", "OBJECT_STORAGE_BUCKET"
        :type member_type: str

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType'
        }

        self._member_id = None
        self._member_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['memberType']

        if type == 'COMPUTE_INSTANCE_MOVABLE':
            return 'CreateDrProtectionGroupMemberComputeInstanceMovableDetails'

        if type == 'AUTONOMOUS_CONTAINER_DATABASE':
            return 'CreateDrProtectionGroupMemberAutonomousContainerDatabaseDetails'

        if type == 'COMPUTE_INSTANCE_NON_MOVABLE':
            return 'CreateDrProtectionGroupMemberComputeInstanceNonMovableDetails'

        if type == 'COMPUTE_INSTANCE':
            return 'CreateDrProtectionGroupMemberComputeInstanceDetails'

        if type == 'DATABASE':
            return 'CreateDrProtectionGroupMemberDatabaseDetails'

        if type == 'AUTONOMOUS_DATABASE':
            return 'CreateDrProtectionGroupMemberAutonomousDatabaseDetails'

        if type == 'NETWORK_LOAD_BALANCER':
            return 'CreateDrProtectionGroupMemberNetworkLoadBalancerDetails'

        if type == 'VOLUME_GROUP':
            return 'CreateDrProtectionGroupMemberVolumeGroupDetails'

        if type == 'OKE_CLUSTER':
            return 'CreateDrProtectionGroupMemberOkeClusterDetails'

        if type == 'FILE_SYSTEM':
            return 'CreateDrProtectionGroupMemberFileSystemDetails'

        if type == 'OBJECT_STORAGE_BUCKET':
            return 'CreateDrProtectionGroupMemberObjectStorageBucketDetails'

        if type == 'LOAD_BALANCER':
            return 'CreateDrProtectionGroupMemberLoadBalancerDetails'
        else:
            return 'CreateDrProtectionGroupMemberDetails'

    @property
    def member_id(self):
        """
        **[Required]** Gets the member_id of this CreateDrProtectionGroupMemberDetails.
        The OCID of the member.

        Example: `ocid1.instance.oc1..uniqueID`


        :return: The member_id of this CreateDrProtectionGroupMemberDetails.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this CreateDrProtectionGroupMemberDetails.
        The OCID of the member.

        Example: `ocid1.instance.oc1..uniqueID`


        :param member_id: The member_id of this CreateDrProtectionGroupMemberDetails.
        :type: str
        """
        self._member_id = member_id

    @property
    def member_type(self):
        """
        **[Required]** Gets the member_type of this CreateDrProtectionGroupMemberDetails.
        The type of the member.

        Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OKE_CLUSTER", "OBJECT_STORAGE_BUCKET"


        :return: The member_type of this CreateDrProtectionGroupMemberDetails.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """
        Sets the member_type of this CreateDrProtectionGroupMemberDetails.
        The type of the member.


        :param member_type: The member_type of this CreateDrProtectionGroupMemberDetails.
        :type: str
        """
        allowed_values = ["COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OKE_CLUSTER", "OBJECT_STORAGE_BUCKET"]
        if not value_allowed_none_or_none_sentinel(member_type, allowed_values):
            raise ValueError(
                f"Invalid value for `member_type`, must be None or one of {allowed_values}"
            )
        self._member_type = member_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
