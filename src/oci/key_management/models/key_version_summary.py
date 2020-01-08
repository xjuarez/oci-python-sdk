# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyVersionSummary(object):
    """
    KeyVersionSummary model.
    """

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "ENABLING"
    LIFECYCLE_STATE_ENABLING = "ENABLING"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "ENABLED"
    LIFECYCLE_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "DISABLING"
    LIFECYCLE_STATE_DISABLING = "DISABLING"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "DISABLED"
    LIFECYCLE_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a KeyVersionSummary.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the origin property of a KeyVersionSummary.
    #: This constant has a value of "INTERNAL"
    ORIGIN_INTERNAL = "INTERNAL"

    #: A constant which can be used with the origin property of a KeyVersionSummary.
    #: This constant has a value of "EXTERNAL"
    ORIGIN_EXTERNAL = "EXTERNAL"

    def __init__(self, **kwargs):
        """
        Initializes a new KeyVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this KeyVersionSummary.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this KeyVersionSummary.
        :type id: str

        :param key_id:
            The value to assign to the key_id property of this KeyVersionSummary.
        :type key_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this KeyVersionSummary.
            Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param origin:
            The value to assign to the origin property of this KeyVersionSummary.
            Allowed values for this property are: "INTERNAL", "EXTERNAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type origin: str

        :param time_created:
            The value to assign to the time_created property of this KeyVersionSummary.
        :type time_created: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this KeyVersionSummary.
        :type time_of_deletion: datetime

        :param vault_id:
            The value to assign to the vault_id property of this KeyVersionSummary.
        :type vault_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'key_id': 'str',
            'lifecycle_state': 'str',
            'origin': 'str',
            'time_created': 'datetime',
            'time_of_deletion': 'datetime',
            'vault_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'id': 'id',
            'key_id': 'keyId',
            'lifecycle_state': 'lifecycleState',
            'origin': 'origin',
            'time_created': 'timeCreated',
            'time_of_deletion': 'timeOfDeletion',
            'vault_id': 'vaultId'
        }

        self._compartment_id = None
        self._id = None
        self._key_id = None
        self._lifecycle_state = None
        self._origin = None
        self._time_created = None
        self._time_of_deletion = None
        self._vault_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this KeyVersionSummary.
        The OCID of the compartment that contains this key version.


        :return: The compartment_id of this KeyVersionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this KeyVersionSummary.
        The OCID of the compartment that contains this key version.


        :param compartment_id: The compartment_id of this KeyVersionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this KeyVersionSummary.
        The OCID of the key version.


        :return: The id of this KeyVersionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this KeyVersionSummary.
        The OCID of the key version.


        :param id: The id of this KeyVersionSummary.
        :type: str
        """
        self._id = id

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this KeyVersionSummary.
        The OCID of the master encryption key associated with this key version.


        :return: The key_id of this KeyVersionSummary.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this KeyVersionSummary.
        The OCID of the master encryption key associated with this key version.


        :param key_id: The key_id of this KeyVersionSummary.
        :type: str
        """
        self._key_id = key_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this KeyVersionSummary.
        The key version's current state.

        Example: `ENABLED`

        Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this KeyVersionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this KeyVersionSummary.
        The key version's current state.

        Example: `ENABLED`


        :param lifecycle_state: The lifecycle_state of this KeyVersionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def origin(self):
        """
        **[Required]** Gets the origin of this KeyVersionSummary.
        The source of the key material. When this value is INTERNAL, OCI KMS created the key material. When this value is EXTERNAL, the key material was imported

        Allowed values for this property are: "INTERNAL", "EXTERNAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The origin of this KeyVersionSummary.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this KeyVersionSummary.
        The source of the key material. When this value is INTERNAL, OCI KMS created the key material. When this value is EXTERNAL, the key material was imported


        :param origin: The origin of this KeyVersionSummary.
        :type: str
        """
        allowed_values = ["INTERNAL", "EXTERNAL"]
        if not value_allowed_none_or_none_sentinel(origin, allowed_values):
            origin = 'UNKNOWN_ENUM_VALUE'
        self._origin = origin

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this KeyVersionSummary.
        The date and time this key version was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this KeyVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this KeyVersionSummary.
        The date and time this key version was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this KeyVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this KeyVersionSummary.
        An optional property to indicate when to delete the key version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this KeyVersionSummary.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this KeyVersionSummary.
        An optional property to indicate when to delete the key version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this KeyVersionSummary.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this KeyVersionSummary.
        The OCID of the vault that contains this key version.


        :return: The vault_id of this KeyVersionSummary.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this KeyVersionSummary.
        The OCID of the vault that contains this key version.


        :param vault_id: The vault_id of this KeyVersionSummary.
        :type: str
        """
        self._vault_id = vault_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
