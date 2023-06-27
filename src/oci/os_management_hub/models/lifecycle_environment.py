# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LifecycleEnvironment(object):
    """
    Contains versioned software source content and lifecycle stages for a managed instance.
    """

    #: A constant which can be used with the lifecycle_state property of a LifecycleEnvironment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a LifecycleEnvironment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a LifecycleEnvironment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LifecycleEnvironment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a LifecycleEnvironment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a LifecycleEnvironment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the os_family property of a LifecycleEnvironment.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a LifecycleEnvironment.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a LifecycleEnvironment.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the arch_type property of a LifecycleEnvironment.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a LifecycleEnvironment.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a LifecycleEnvironment.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a LifecycleEnvironment.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a LifecycleEnvironment.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the vendor_name property of a LifecycleEnvironment.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new LifecycleEnvironment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LifecycleEnvironment.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LifecycleEnvironment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this LifecycleEnvironment.
        :type display_name: str

        :param description:
            The value to assign to the description property of this LifecycleEnvironment.
        :type description: str

        :param stages:
            The value to assign to the stages property of this LifecycleEnvironment.
        :type stages: list[oci.os_management_hub.models.LifecycleStage]

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this LifecycleEnvironment.
        :type managed_instance_ids: list[oci.os_management_hub.models.ManagedInstanceDetails]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LifecycleEnvironment.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param os_family:
            The value to assign to the os_family property of this LifecycleEnvironment.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this LifecycleEnvironment.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param vendor_name:
            The value to assign to the vendor_name property of this LifecycleEnvironment.
            Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vendor_name: str

        :param time_created:
            The value to assign to the time_created property of this LifecycleEnvironment.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this LifecycleEnvironment.
        :type time_modified: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LifecycleEnvironment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LifecycleEnvironment.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this LifecycleEnvironment.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'stages': 'list[LifecycleStage]',
            'managed_instance_ids': 'list[ManagedInstanceDetails]',
            'lifecycle_state': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'vendor_name': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'stages': 'stages',
            'managed_instance_ids': 'managedInstanceIds',
            'lifecycle_state': 'lifecycleState',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'vendor_name': 'vendorName',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._stages = None
        self._managed_instance_ids = None
        self._lifecycle_state = None
        self._os_family = None
        self._arch_type = None
        self._vendor_name = None
        self._time_created = None
        self._time_modified = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LifecycleEnvironment.
        The OCID of the resource that is immutable on creation.


        :return: The id of this LifecycleEnvironment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LifecycleEnvironment.
        The OCID of the resource that is immutable on creation.


        :param id: The id of this LifecycleEnvironment.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LifecycleEnvironment.
        The OCID of the tenancy containing the lifecycle environment.


        :return: The compartment_id of this LifecycleEnvironment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LifecycleEnvironment.
        The OCID of the tenancy containing the lifecycle environment.


        :param compartment_id: The compartment_id of this LifecycleEnvironment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this LifecycleEnvironment.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this LifecycleEnvironment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LifecycleEnvironment.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this LifecycleEnvironment.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this LifecycleEnvironment.
        User specified information about the lifecycle environment.


        :return: The description of this LifecycleEnvironment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LifecycleEnvironment.
        User specified information about the lifecycle environment.


        :param description: The description of this LifecycleEnvironment.
        :type: str
        """
        self._description = description

    @property
    def stages(self):
        """
        **[Required]** Gets the stages of this LifecycleEnvironment.
        User specified list of lifecycle stages to be created for the lifecycle environment.


        :return: The stages of this LifecycleEnvironment.
        :rtype: list[oci.os_management_hub.models.LifecycleStage]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this LifecycleEnvironment.
        User specified list of lifecycle stages to be created for the lifecycle environment.


        :param stages: The stages of this LifecycleEnvironment.
        :type: list[oci.os_management_hub.models.LifecycleStage]
        """
        self._stages = stages

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this LifecycleEnvironment.
        The list of managed instance OCIDs specified in the lifecycle stage.


        :return: The managed_instance_ids of this LifecycleEnvironment.
        :rtype: list[oci.os_management_hub.models.ManagedInstanceDetails]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this LifecycleEnvironment.
        The list of managed instance OCIDs specified in the lifecycle stage.


        :param managed_instance_ids: The managed_instance_ids of this LifecycleEnvironment.
        :type: list[oci.os_management_hub.models.ManagedInstanceDetails]
        """
        self._managed_instance_ids = managed_instance_ids

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LifecycleEnvironment.
        The current state of the lifecycle environment.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LifecycleEnvironment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LifecycleEnvironment.
        The current state of the lifecycle environment.


        :param lifecycle_state: The lifecycle_state of this LifecycleEnvironment.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this LifecycleEnvironment.
        The operating system type of the target instances.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this LifecycleEnvironment.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this LifecycleEnvironment.
        The operating system type of the target instances.


        :param os_family: The os_family of this LifecycleEnvironment.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this LifecycleEnvironment.
        The CPU architecture of the target instances.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this LifecycleEnvironment.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this LifecycleEnvironment.
        The CPU architecture of the target instances.


        :param arch_type: The arch_type of this LifecycleEnvironment.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this LifecycleEnvironment.
        The software source vendor name.

        Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vendor_name of this LifecycleEnvironment.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this LifecycleEnvironment.
        The software source vendor name.


        :param vendor_name: The vendor_name of this LifecycleEnvironment.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            vendor_name = 'UNKNOWN_ENUM_VALUE'
        self._vendor_name = vendor_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LifecycleEnvironment.
        The time the lifecycle environment was created. An RFC3339 formatted datetime string.


        :return: The time_created of this LifecycleEnvironment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LifecycleEnvironment.
        The time the lifecycle environment was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this LifecycleEnvironment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        Gets the time_modified of this LifecycleEnvironment.
        The time the lifecycle environment was last modified. An RFC3339 formatted datetime string.


        :return: The time_modified of this LifecycleEnvironment.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this LifecycleEnvironment.
        The time the lifecycle environment was last modified. An RFC3339 formatted datetime string.


        :param time_modified: The time_modified of this LifecycleEnvironment.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LifecycleEnvironment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this LifecycleEnvironment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LifecycleEnvironment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this LifecycleEnvironment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LifecycleEnvironment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this LifecycleEnvironment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LifecycleEnvironment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this LifecycleEnvironment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this LifecycleEnvironment.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this LifecycleEnvironment.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this LifecycleEnvironment.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this LifecycleEnvironment.
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
