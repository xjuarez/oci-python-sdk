# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSource(object):
    """
    The object that defines a software source. A software source contains a collection of packages. For more information, see `Managing Software Sources`__.

    __ https://docs.cloud.oracle.com/iaas/osmh/doc/software-sources.htm
    """

    #: A constant which can be used with the software_source_type property of a SoftwareSource.
    #: This constant has a value of "VENDOR"
    SOFTWARE_SOURCE_TYPE_VENDOR = "VENDOR"

    #: A constant which can be used with the software_source_type property of a SoftwareSource.
    #: This constant has a value of "CUSTOM"
    SOFTWARE_SOURCE_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the software_source_type property of a SoftwareSource.
    #: This constant has a value of "VERSIONED"
    SOFTWARE_SOURCE_TYPE_VERSIONED = "VERSIONED"

    #: A constant which can be used with the software_source_type property of a SoftwareSource.
    #: This constant has a value of "PRIVATE"
    SOFTWARE_SOURCE_TYPE_PRIVATE = "PRIVATE"

    #: A constant which can be used with the software_source_type property of a SoftwareSource.
    #: This constant has a value of "THIRD_PARTY"
    SOFTWARE_SOURCE_TYPE_THIRD_PARTY = "THIRD_PARTY"

    #: A constant which can be used with the availability property of a SoftwareSource.
    #: This constant has a value of "AVAILABLE"
    AVAILABILITY_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the availability property of a SoftwareSource.
    #: This constant has a value of "SELECTED"
    AVAILABILITY_SELECTED = "SELECTED"

    #: A constant which can be used with the availability property of a SoftwareSource.
    #: This constant has a value of "RESTRICTED"
    AVAILABILITY_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the availability property of a SoftwareSource.
    #: This constant has a value of "UNAVAILABLE"
    AVAILABILITY_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSource.
    #: This constant has a value of "AVAILABLE"
    AVAILABILITY_AT_OCI_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSource.
    #: This constant has a value of "SELECTED"
    AVAILABILITY_AT_OCI_SELECTED = "SELECTED"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSource.
    #: This constant has a value of "RESTRICTED"
    AVAILABILITY_AT_OCI_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSource.
    #: This constant has a value of "UNAVAILABLE"
    AVAILABILITY_AT_OCI_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "ORACLE_LINUX_6"
    OS_FAMILY_ORACLE_LINUX_6 = "ORACLE_LINUX_6"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "WINDOWS_SERVER_2016"
    OS_FAMILY_WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "WINDOWS_SERVER_2019"
    OS_FAMILY_WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "WINDOWS_SERVER_2022"
    OS_FAMILY_WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"

    #: A constant which can be used with the os_family property of a SoftwareSource.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "I386"
    ARCH_TYPE_I386 = "I386"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA1"
    CHECKSUM_TYPE_SHA1 = "SHA1"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA256"
    CHECKSUM_TYPE_SHA256 = "SHA256"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA384"
    CHECKSUM_TYPE_SHA384 = "SHA384"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA512"
    CHECKSUM_TYPE_SHA512 = "SHA512"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.os_management_hub.models.VendorSoftwareSource`
        * :class:`~oci.os_management_hub.models.ThirdPartySoftwareSource`
        * :class:`~oci.os_management_hub.models.CustomSoftwareSource`
        * :class:`~oci.os_management_hub.models.VersionedCustomSoftwareSource`
        * :class:`~oci.os_management_hub.models.PrivateSoftwareSource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SoftwareSource.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SoftwareSource.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SoftwareSource.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this SoftwareSource.
        :type time_created: datetime

        :param description:
            The value to assign to the description property of this SoftwareSource.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this SoftwareSource.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", "PRIVATE", "THIRD_PARTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type software_source_type: str

        :param availability:
            The value to assign to the availability property of this SoftwareSource.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability: str

        :param availability_at_oci:
            The value to assign to the availability_at_oci property of this SoftwareSource.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability_at_oci: str

        :param repo_id:
            The value to assign to the repo_id property of this SoftwareSource.
        :type repo_id: str

        :param os_family:
            The value to assign to the os_family property of this SoftwareSource.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this SoftwareSource.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SoftwareSource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param package_count:
            The value to assign to the package_count property of this SoftwareSource.
        :type package_count: int

        :param url:
            The value to assign to the url property of this SoftwareSource.
        :type url: str

        :param checksum_type:
            The value to assign to the checksum_type property of this SoftwareSource.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type checksum_type: str

        :param gpg_key_url:
            The value to assign to the gpg_key_url property of this SoftwareSource.
        :type gpg_key_url: str

        :param gpg_key_id:
            The value to assign to the gpg_key_id property of this SoftwareSource.
        :type gpg_key_id: str

        :param gpg_key_fingerprint:
            The value to assign to the gpg_key_fingerprint property of this SoftwareSource.
        :type gpg_key_fingerprint: str

        :param size:
            The value to assign to the size property of this SoftwareSource.
        :type size: float

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SoftwareSource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SoftwareSource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SoftwareSource.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'description': 'str',
            'software_source_type': 'str',
            'availability': 'str',
            'availability_at_oci': 'str',
            'repo_id': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'lifecycle_state': 'str',
            'package_count': 'int',
            'url': 'str',
            'checksum_type': 'str',
            'gpg_key_url': 'str',
            'gpg_key_id': 'str',
            'gpg_key_fingerprint': 'str',
            'size': 'float',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'availability': 'availability',
            'availability_at_oci': 'availabilityAtOci',
            'repo_id': 'repoId',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'lifecycle_state': 'lifecycleState',
            'package_count': 'packageCount',
            'url': 'url',
            'checksum_type': 'checksumType',
            'gpg_key_url': 'gpgKeyUrl',
            'gpg_key_id': 'gpgKeyId',
            'gpg_key_fingerprint': 'gpgKeyFingerprint',
            'size': 'size',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._description = None
        self._software_source_type = None
        self._availability = None
        self._availability_at_oci = None
        self._repo_id = None
        self._os_family = None
        self._arch_type = None
        self._lifecycle_state = None
        self._package_count = None
        self._url = None
        self._checksum_type = None
        self._gpg_key_url = None
        self._gpg_key_id = None
        self._gpg_key_fingerprint = None
        self._size = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['softwareSourceType']

        if type == 'VENDOR':
            return 'VendorSoftwareSource'

        if type == 'THIRD_PARTY':
            return 'ThirdPartySoftwareSource'

        if type == 'CUSTOM':
            return 'CustomSoftwareSource'

        if type == 'VERSIONED':
            return 'VersionedCustomSoftwareSource'

        if type == 'PRIVATE':
            return 'PrivateSoftwareSource'
        else:
            return 'SoftwareSource'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SoftwareSource.
        The `OCID`__ of the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this SoftwareSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SoftwareSource.
        The `OCID`__ of the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this SoftwareSource.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SoftwareSource.
        The `OCID`__ of the compartment that contains the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this SoftwareSource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SoftwareSource.
        The `OCID`__ of the compartment that contains the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this SoftwareSource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SoftwareSource.
        User-friendly name for the software source.


        :return: The display_name of this SoftwareSource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwareSource.
        User-friendly name for the software source.


        :param display_name: The display_name of this SoftwareSource.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SoftwareSource.
        The date and time the software source was created (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this SoftwareSource.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SoftwareSource.
        The date and time the software source was created (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this SoftwareSource.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def description(self):
        """
        Gets the description of this SoftwareSource.
        User-specified description for the software source.


        :return: The description of this SoftwareSource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SoftwareSource.
        User-specified description for the software source.


        :param description: The description of this SoftwareSource.
        :type: str
        """
        self._description = description

    @property
    def software_source_type(self):
        """
        **[Required]** Gets the software_source_type of this SoftwareSource.
        Type of software source.

        Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", "PRIVATE", "THIRD_PARTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The software_source_type of this SoftwareSource.
        :rtype: str
        """
        return self._software_source_type

    @software_source_type.setter
    def software_source_type(self, software_source_type):
        """
        Sets the software_source_type of this SoftwareSource.
        Type of software source.


        :param software_source_type: The software_source_type of this SoftwareSource.
        :type: str
        """
        allowed_values = ["VENDOR", "CUSTOM", "VERSIONED", "PRIVATE", "THIRD_PARTY"]
        if not value_allowed_none_or_none_sentinel(software_source_type, allowed_values):
            software_source_type = 'UNKNOWN_ENUM_VALUE'
        self._software_source_type = software_source_type

    @property
    def availability(self):
        """
        **[Required]** Gets the availability of this SoftwareSource.
        Availability of the software source (for non-OCI environments).

        Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The availability of this SoftwareSource.
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """
        Sets the availability of this SoftwareSource.
        Availability of the software source (for non-OCI environments).


        :param availability: The availability of this SoftwareSource.
        :type: str
        """
        allowed_values = ["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability, allowed_values):
            availability = 'UNKNOWN_ENUM_VALUE'
        self._availability = availability

    @property
    def availability_at_oci(self):
        """
        **[Required]** Gets the availability_at_oci of this SoftwareSource.
        Availability of the software source (for OCI environments).

        Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The availability_at_oci of this SoftwareSource.
        :rtype: str
        """
        return self._availability_at_oci

    @availability_at_oci.setter
    def availability_at_oci(self, availability_at_oci):
        """
        Sets the availability_at_oci of this SoftwareSource.
        Availability of the software source (for OCI environments).


        :param availability_at_oci: The availability_at_oci of this SoftwareSource.
        :type: str
        """
        allowed_values = ["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability_at_oci, allowed_values):
            availability_at_oci = 'UNKNOWN_ENUM_VALUE'
        self._availability_at_oci = availability_at_oci

    @property
    def repo_id(self):
        """
        **[Required]** Gets the repo_id of this SoftwareSource.
        The repository ID for the software source.


        :return: The repo_id of this SoftwareSource.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """
        Sets the repo_id of this SoftwareSource.
        The repository ID for the software source.


        :param repo_id: The repo_id of this SoftwareSource.
        :type: str
        """
        self._repo_id = repo_id

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this SoftwareSource.
        The OS family of the software source.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this SoftwareSource.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this SoftwareSource.
        The OS family of the software source.


        :param os_family: The os_family of this SoftwareSource.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this SoftwareSource.
        The architecture type supported by the software source.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this SoftwareSource.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this SoftwareSource.
        The architecture type supported by the software source.


        :param arch_type: The arch_type of this SoftwareSource.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SoftwareSource.
        The current state of the software source.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SoftwareSource.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SoftwareSource.
        The current state of the software source.


        :param lifecycle_state: The lifecycle_state of this SoftwareSource.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def package_count(self):
        """
        Gets the package_count of this SoftwareSource.
        Number of packages the software source contains.


        :return: The package_count of this SoftwareSource.
        :rtype: int
        """
        return self._package_count

    @package_count.setter
    def package_count(self, package_count):
        """
        Sets the package_count of this SoftwareSource.
        Number of packages the software source contains.


        :param package_count: The package_count of this SoftwareSource.
        :type: int
        """
        self._package_count = package_count

    @property
    def url(self):
        """
        **[Required]** Gets the url of this SoftwareSource.
        URL for the repository. For vendor software sources, this is the URL to the regional yum server. For custom software sources, this is 'custom/<repoId>'.


        :return: The url of this SoftwareSource.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this SoftwareSource.
        URL for the repository. For vendor software sources, this is the URL to the regional yum server. For custom software sources, this is 'custom/<repoId>'.


        :param url: The url of this SoftwareSource.
        :type: str
        """
        self._url = url

    @property
    def checksum_type(self):
        """
        Gets the checksum_type of this SoftwareSource.
        The yum repository checksum type used by this software source.

        Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The checksum_type of this SoftwareSource.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this SoftwareSource.
        The yum repository checksum type used by this software source.


        :param checksum_type: The checksum_type of this SoftwareSource.
        :type: str
        """
        allowed_values = ["SHA1", "SHA256", "SHA384", "SHA512"]
        if not value_allowed_none_or_none_sentinel(checksum_type, allowed_values):
            checksum_type = 'UNKNOWN_ENUM_VALUE'
        self._checksum_type = checksum_type

    @property
    def gpg_key_url(self):
        """
        Gets the gpg_key_url of this SoftwareSource.
        URI of the GPG key for this software source.


        :return: The gpg_key_url of this SoftwareSource.
        :rtype: str
        """
        return self._gpg_key_url

    @gpg_key_url.setter
    def gpg_key_url(self, gpg_key_url):
        """
        Sets the gpg_key_url of this SoftwareSource.
        URI of the GPG key for this software source.


        :param gpg_key_url: The gpg_key_url of this SoftwareSource.
        :type: str
        """
        self._gpg_key_url = gpg_key_url

    @property
    def gpg_key_id(self):
        """
        Gets the gpg_key_id of this SoftwareSource.
        ID of the GPG key for this software source.


        :return: The gpg_key_id of this SoftwareSource.
        :rtype: str
        """
        return self._gpg_key_id

    @gpg_key_id.setter
    def gpg_key_id(self, gpg_key_id):
        """
        Sets the gpg_key_id of this SoftwareSource.
        ID of the GPG key for this software source.


        :param gpg_key_id: The gpg_key_id of this SoftwareSource.
        :type: str
        """
        self._gpg_key_id = gpg_key_id

    @property
    def gpg_key_fingerprint(self):
        """
        Gets the gpg_key_fingerprint of this SoftwareSource.
        Fingerprint of the GPG key for this software source.


        :return: The gpg_key_fingerprint of this SoftwareSource.
        :rtype: str
        """
        return self._gpg_key_fingerprint

    @gpg_key_fingerprint.setter
    def gpg_key_fingerprint(self, gpg_key_fingerprint):
        """
        Sets the gpg_key_fingerprint of this SoftwareSource.
        Fingerprint of the GPG key for this software source.


        :param gpg_key_fingerprint: The gpg_key_fingerprint of this SoftwareSource.
        :type: str
        """
        self._gpg_key_fingerprint = gpg_key_fingerprint

    @property
    def size(self):
        """
        Gets the size of this SoftwareSource.
        The size of the software source in bytes (B).


        :return: The size of this SoftwareSource.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SoftwareSource.
        The size of the software source in bytes (B).


        :param size: The size of this SoftwareSource.
        :type: float
        """
        self._size = size

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SoftwareSource.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SoftwareSource.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SoftwareSource.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SoftwareSource.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SoftwareSource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SoftwareSource.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SoftwareSource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SoftwareSource.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SoftwareSource.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SoftwareSource.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SoftwareSource.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SoftwareSource.
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
