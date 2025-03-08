# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .software_source import SoftwareSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThirdPartySoftwareSource(SoftwareSource):
    """
    The object that defines a third-party software source. A software source is a collection of packages. For more information, see `Managing Software Sources`__.

    __ https://docs.cloud.oracle.com/iaas/osmh/doc/software-sources.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ThirdPartySoftwareSource object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.ThirdPartySoftwareSource.software_source_type` attribute
        of this class is ``THIRD_PARTY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ThirdPartySoftwareSource.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ThirdPartySoftwareSource.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ThirdPartySoftwareSource.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this ThirdPartySoftwareSource.
        :type time_created: datetime

        :param description:
            The value to assign to the description property of this ThirdPartySoftwareSource.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this ThirdPartySoftwareSource.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", "PRIVATE", "THIRD_PARTY"
        :type software_source_type: str

        :param availability:
            The value to assign to the availability property of this ThirdPartySoftwareSource.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"
        :type availability: str

        :param availability_at_oci:
            The value to assign to the availability_at_oci property of this ThirdPartySoftwareSource.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"
        :type availability_at_oci: str

        :param repo_id:
            The value to assign to the repo_id property of this ThirdPartySoftwareSource.
        :type repo_id: str

        :param os_family:
            The value to assign to the os_family property of this ThirdPartySoftwareSource.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this ThirdPartySoftwareSource.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"
        :type arch_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ThirdPartySoftwareSource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"
        :type lifecycle_state: str

        :param package_count:
            The value to assign to the package_count property of this ThirdPartySoftwareSource.
        :type package_count: int

        :param url:
            The value to assign to the url property of this ThirdPartySoftwareSource.
        :type url: str

        :param checksum_type:
            The value to assign to the checksum_type property of this ThirdPartySoftwareSource.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512"
        :type checksum_type: str

        :param gpg_key_url:
            The value to assign to the gpg_key_url property of this ThirdPartySoftwareSource.
        :type gpg_key_url: str

        :param gpg_key_id:
            The value to assign to the gpg_key_id property of this ThirdPartySoftwareSource.
        :type gpg_key_id: str

        :param gpg_key_fingerprint:
            The value to assign to the gpg_key_fingerprint property of this ThirdPartySoftwareSource.
        :type gpg_key_fingerprint: str

        :param size:
            The value to assign to the size property of this ThirdPartySoftwareSource.
        :type size: float

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ThirdPartySoftwareSource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ThirdPartySoftwareSource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ThirdPartySoftwareSource.
        :type system_tags: dict(str, dict(str, object))

        :param is_gpg_check_enabled:
            The value to assign to the is_gpg_check_enabled property of this ThirdPartySoftwareSource.
        :type is_gpg_check_enabled: bool

        :param is_ssl_verify_enabled:
            The value to assign to the is_ssl_verify_enabled property of this ThirdPartySoftwareSource.
        :type is_ssl_verify_enabled: bool

        :param advanced_repo_options:
            The value to assign to the advanced_repo_options property of this ThirdPartySoftwareSource.
        :type advanced_repo_options: str

        :param is_mirror_sync_allowed:
            The value to assign to the is_mirror_sync_allowed property of this ThirdPartySoftwareSource.
        :type is_mirror_sync_allowed: bool

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
            'system_tags': 'dict(str, dict(str, object))',
            'is_gpg_check_enabled': 'bool',
            'is_ssl_verify_enabled': 'bool',
            'advanced_repo_options': 'str',
            'is_mirror_sync_allowed': 'bool'
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
            'system_tags': 'systemTags',
            'is_gpg_check_enabled': 'isGpgCheckEnabled',
            'is_ssl_verify_enabled': 'isSslVerifyEnabled',
            'advanced_repo_options': 'advancedRepoOptions',
            'is_mirror_sync_allowed': 'isMirrorSyncAllowed'
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
        self._is_gpg_check_enabled = None
        self._is_ssl_verify_enabled = None
        self._advanced_repo_options = None
        self._is_mirror_sync_allowed = None
        self._software_source_type = 'THIRD_PARTY'

    @property
    def is_gpg_check_enabled(self):
        """
        Gets the is_gpg_check_enabled of this ThirdPartySoftwareSource.
        Whether signature verification should be done for the software source


        :return: The is_gpg_check_enabled of this ThirdPartySoftwareSource.
        :rtype: bool
        """
        return self._is_gpg_check_enabled

    @is_gpg_check_enabled.setter
    def is_gpg_check_enabled(self, is_gpg_check_enabled):
        """
        Sets the is_gpg_check_enabled of this ThirdPartySoftwareSource.
        Whether signature verification should be done for the software source


        :param is_gpg_check_enabled: The is_gpg_check_enabled of this ThirdPartySoftwareSource.
        :type: bool
        """
        self._is_gpg_check_enabled = is_gpg_check_enabled

    @property
    def is_ssl_verify_enabled(self):
        """
        Gets the is_ssl_verify_enabled of this ThirdPartySoftwareSource.
        Whether SSL validation needs to be turned on


        :return: The is_ssl_verify_enabled of this ThirdPartySoftwareSource.
        :rtype: bool
        """
        return self._is_ssl_verify_enabled

    @is_ssl_verify_enabled.setter
    def is_ssl_verify_enabled(self, is_ssl_verify_enabled):
        """
        Sets the is_ssl_verify_enabled of this ThirdPartySoftwareSource.
        Whether SSL validation needs to be turned on


        :param is_ssl_verify_enabled: The is_ssl_verify_enabled of this ThirdPartySoftwareSource.
        :type: bool
        """
        self._is_ssl_verify_enabled = is_ssl_verify_enabled

    @property
    def advanced_repo_options(self):
        """
        Gets the advanced_repo_options of this ThirdPartySoftwareSource.
        Advanced repository options for the software source


        :return: The advanced_repo_options of this ThirdPartySoftwareSource.
        :rtype: str
        """
        return self._advanced_repo_options

    @advanced_repo_options.setter
    def advanced_repo_options(self, advanced_repo_options):
        """
        Sets the advanced_repo_options of this ThirdPartySoftwareSource.
        Advanced repository options for the software source


        :param advanced_repo_options: The advanced_repo_options of this ThirdPartySoftwareSource.
        :type: str
        """
        self._advanced_repo_options = advanced_repo_options

    @property
    def is_mirror_sync_allowed(self):
        """
        Gets the is_mirror_sync_allowed of this ThirdPartySoftwareSource.
        Whether this software source can be synced to a management station


        :return: The is_mirror_sync_allowed of this ThirdPartySoftwareSource.
        :rtype: bool
        """
        return self._is_mirror_sync_allowed

    @is_mirror_sync_allowed.setter
    def is_mirror_sync_allowed(self, is_mirror_sync_allowed):
        """
        Sets the is_mirror_sync_allowed of this ThirdPartySoftwareSource.
        Whether this software source can be synced to a management station


        :param is_mirror_sync_allowed: The is_mirror_sync_allowed of this ThirdPartySoftwareSource.
        :type: bool
        """
        self._is_mirror_sync_allowed = is_mirror_sync_allowed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
