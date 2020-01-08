# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserGroupMembership(object):
    """
    An object that represents the membership of a user in a group. When you add a user to a group, the result is a
    `UserGroupMembership` with its own OCID. To remove a user from a group, you delete the `UserGroupMembership` object.
    """

    #: A constant which can be used with the lifecycle_state property of a UserGroupMembership.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a UserGroupMembership.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a UserGroupMembership.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a UserGroupMembership.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a UserGroupMembership.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new UserGroupMembership object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UserGroupMembership.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this UserGroupMembership.
        :type compartment_id: str

        :param group_id:
            The value to assign to the group_id property of this UserGroupMembership.
        :type group_id: str

        :param user_id:
            The value to assign to the user_id property of this UserGroupMembership.
        :type user_id: str

        :param time_created:
            The value to assign to the time_created property of this UserGroupMembership.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UserGroupMembership.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this UserGroupMembership.
        :type inactive_status: int

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'group_id': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'group_id': 'groupId',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._id = None
        self._compartment_id = None
        self._group_id = None
        self._user_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this UserGroupMembership.
        The OCID of the membership.


        :return: The id of this UserGroupMembership.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserGroupMembership.
        The OCID of the membership.


        :param id: The id of this UserGroupMembership.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this UserGroupMembership.
        The OCID of the tenancy containing the user, group, and membership object.


        :return: The compartment_id of this UserGroupMembership.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UserGroupMembership.
        The OCID of the tenancy containing the user, group, and membership object.


        :param compartment_id: The compartment_id of this UserGroupMembership.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def group_id(self):
        """
        **[Required]** Gets the group_id of this UserGroupMembership.
        The OCID of the group.


        :return: The group_id of this UserGroupMembership.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this UserGroupMembership.
        The OCID of the group.


        :param group_id: The group_id of this UserGroupMembership.
        :type: str
        """
        self._group_id = group_id

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this UserGroupMembership.
        The OCID of the user.


        :return: The user_id of this UserGroupMembership.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserGroupMembership.
        The OCID of the user.


        :param user_id: The user_id of this UserGroupMembership.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this UserGroupMembership.
        Date and time the membership was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this UserGroupMembership.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UserGroupMembership.
        Date and time the membership was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this UserGroupMembership.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this UserGroupMembership.
        The membership's current state.  After creating a membership object, make sure its `lifecycleState` changes
        from CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this UserGroupMembership.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UserGroupMembership.
        The membership's current state.  After creating a membership object, make sure its `lifecycleState` changes
        from CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this UserGroupMembership.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this UserGroupMembership.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this UserGroupMembership.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this UserGroupMembership.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this UserGroupMembership.
        :type: int
        """
        self._inactive_status = inactive_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
