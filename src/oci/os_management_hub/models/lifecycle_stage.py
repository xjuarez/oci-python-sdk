# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LifecycleStage(object):
    """
    Defines the lifecycle stage.
    """

    #: A constant which can be used with the os_family property of a LifecycleStage.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a LifecycleStage.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a LifecycleStage.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the arch_type property of a LifecycleStage.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a LifecycleStage.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a LifecycleStage.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a LifecycleStage.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a LifecycleStage.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the vendor_name property of a LifecycleStage.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    #: A constant which can be used with the lifecycle_state property of a LifecycleStage.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a LifecycleStage.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a LifecycleStage.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LifecycleStage.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a LifecycleStage.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a LifecycleStage.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new LifecycleStage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LifecycleStage.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LifecycleStage.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this LifecycleStage.
        :type display_name: str

        :param lifecycle_environment_id:
            The value to assign to the lifecycle_environment_id property of this LifecycleStage.
        :type lifecycle_environment_id: str

        :param rank:
            The value to assign to the rank property of this LifecycleStage.
        :type rank: int

        :param os_family:
            The value to assign to the os_family property of this LifecycleStage.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this LifecycleStage.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param vendor_name:
            The value to assign to the vendor_name property of this LifecycleStage.
            Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vendor_name: str

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this LifecycleStage.
        :type managed_instance_ids: list[oci.os_management_hub.models.ManagedInstanceDetails]

        :param software_source_id:
            The value to assign to the software_source_id property of this LifecycleStage.
        :type software_source_id: oci.os_management_hub.models.SoftwareSourceDetails

        :param time_created:
            The value to assign to the time_created property of this LifecycleStage.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this LifecycleStage.
        :type time_modified: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LifecycleStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LifecycleStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LifecycleStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this LifecycleStage.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_environment_id': 'str',
            'rank': 'int',
            'os_family': 'str',
            'arch_type': 'str',
            'vendor_name': 'str',
            'managed_instance_ids': 'list[ManagedInstanceDetails]',
            'software_source_id': 'SoftwareSourceDetails',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_environment_id': 'lifecycleEnvironmentId',
            'rank': 'rank',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'vendor_name': 'vendorName',
            'managed_instance_ids': 'managedInstanceIds',
            'software_source_id': 'softwareSourceId',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_environment_id = None
        self._rank = None
        self._os_family = None
        self._arch_type = None
        self._vendor_name = None
        self._managed_instance_ids = None
        self._software_source_id = None
        self._time_created = None
        self._time_modified = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        Gets the id of this LifecycleStage.
        The lifecycle stage OCID that is immutable on creation.


        :return: The id of this LifecycleStage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LifecycleStage.
        The lifecycle stage OCID that is immutable on creation.


        :param id: The id of this LifecycleStage.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LifecycleStage.
        The OCID of the tenancy containing the lifecycle stage.


        :return: The compartment_id of this LifecycleStage.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LifecycleStage.
        The OCID of the tenancy containing the lifecycle stage.


        :param compartment_id: The compartment_id of this LifecycleStage.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this LifecycleStage.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this LifecycleStage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LifecycleStage.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this LifecycleStage.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_environment_id(self):
        """
        Gets the lifecycle_environment_id of this LifecycleStage.
        The OCID of the lifecycle environment for the lifecycle stage.


        :return: The lifecycle_environment_id of this LifecycleStage.
        :rtype: str
        """
        return self._lifecycle_environment_id

    @lifecycle_environment_id.setter
    def lifecycle_environment_id(self, lifecycle_environment_id):
        """
        Sets the lifecycle_environment_id of this LifecycleStage.
        The OCID of the lifecycle environment for the lifecycle stage.


        :param lifecycle_environment_id: The lifecycle_environment_id of this LifecycleStage.
        :type: str
        """
        self._lifecycle_environment_id = lifecycle_environment_id

    @property
    def rank(self):
        """
        **[Required]** Gets the rank of this LifecycleStage.
        User specified rank for the lifecycle stage.
        Rank determines the hierarchy of the lifecycle stages for a given lifecycle environment.


        :return: The rank of this LifecycleStage.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this LifecycleStage.
        User specified rank for the lifecycle stage.
        Rank determines the hierarchy of the lifecycle stages for a given lifecycle environment.


        :param rank: The rank of this LifecycleStage.
        :type: int
        """
        self._rank = rank

    @property
    def os_family(self):
        """
        Gets the os_family of this LifecycleStage.
        The operating system type of the target instances.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this LifecycleStage.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this LifecycleStage.
        The operating system type of the target instances.


        :param os_family: The os_family of this LifecycleStage.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        Gets the arch_type of this LifecycleStage.
        The CPU architecture of the target instances.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this LifecycleStage.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this LifecycleStage.
        The CPU architecture of the target instances.


        :param arch_type: The arch_type of this LifecycleStage.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this LifecycleStage.
        The software source vendor name.

        Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vendor_name of this LifecycleStage.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this LifecycleStage.
        The software source vendor name.


        :param vendor_name: The vendor_name of this LifecycleStage.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            vendor_name = 'UNKNOWN_ENUM_VALUE'
        self._vendor_name = vendor_name

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this LifecycleStage.
        The list of managed instances specified lifecycle stage.


        :return: The managed_instance_ids of this LifecycleStage.
        :rtype: list[oci.os_management_hub.models.ManagedInstanceDetails]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this LifecycleStage.
        The list of managed instances specified lifecycle stage.


        :param managed_instance_ids: The managed_instance_ids of this LifecycleStage.
        :type: list[oci.os_management_hub.models.ManagedInstanceDetails]
        """
        self._managed_instance_ids = managed_instance_ids

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this LifecycleStage.

        :return: The software_source_id of this LifecycleStage.
        :rtype: oci.os_management_hub.models.SoftwareSourceDetails
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this LifecycleStage.

        :param software_source_id: The software_source_id of this LifecycleStage.
        :type: oci.os_management_hub.models.SoftwareSourceDetails
        """
        self._software_source_id = software_source_id

    @property
    def time_created(self):
        """
        Gets the time_created of this LifecycleStage.
        The time the lifecycle stage was created. An RFC3339 formatted datetime string.


        :return: The time_created of this LifecycleStage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LifecycleStage.
        The time the lifecycle stage was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this LifecycleStage.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        Gets the time_modified of this LifecycleStage.
        The time the lifecycle stage was last modified. An RFC3339 formatted datetime string.


        :return: The time_modified of this LifecycleStage.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this LifecycleStage.
        The time the lifecycle stage was last modified. An RFC3339 formatted datetime string.


        :param time_modified: The time_modified of this LifecycleStage.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this LifecycleStage.
        The current state of the lifecycle stage.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LifecycleStage.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LifecycleStage.
        The current state of the lifecycle stage.


        :param lifecycle_state: The lifecycle_state of this LifecycleStage.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LifecycleStage.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this LifecycleStage.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LifecycleStage.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this LifecycleStage.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LifecycleStage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this LifecycleStage.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LifecycleStage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this LifecycleStage.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this LifecycleStage.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this LifecycleStage.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this LifecycleStage.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this LifecycleStage.
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
