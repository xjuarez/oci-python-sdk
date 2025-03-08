# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .create_software_source_details import CreateSoftwareSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePrivateSoftwareSourceDetails(CreateSoftwareSourceDetails):
    """
    Provides the information used to create a private software source.
    """

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "ORACLE_LINUX_6"
    OS_FAMILY_ORACLE_LINUX_6 = "ORACLE_LINUX_6"

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "WINDOWS_SERVER_2016"
    OS_FAMILY_WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "WINDOWS_SERVER_2019"
    OS_FAMILY_WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "WINDOWS_SERVER_2022"
    OS_FAMILY_WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"

    #: A constant which can be used with the os_family property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    #: A constant which can be used with the arch_type property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the arch_type property of a CreatePrivateSoftwareSourceDetails.
    #: This constant has a value of "I386"
    ARCH_TYPE_I386 = "I386"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePrivateSoftwareSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CreatePrivateSoftwareSourceDetails.software_source_type` attribute
        of this class is ``PRIVATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePrivateSoftwareSourceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreatePrivateSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreatePrivateSoftwareSourceDetails.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this CreatePrivateSoftwareSourceDetails.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", "PRIVATE", "THIRD_PARTY"
        :type software_source_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePrivateSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePrivateSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param os_family:
            The value to assign to the os_family property of this CreatePrivateSoftwareSourceDetails.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this CreatePrivateSoftwareSourceDetails.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"
        :type arch_type: str

        :param url:
            The value to assign to the url property of this CreatePrivateSoftwareSourceDetails.
        :type url: str

        :param gpg_key_url:
            The value to assign to the gpg_key_url property of this CreatePrivateSoftwareSourceDetails.
        :type gpg_key_url: str

        :param is_gpg_check_enabled:
            The value to assign to the is_gpg_check_enabled property of this CreatePrivateSoftwareSourceDetails.
        :type is_gpg_check_enabled: bool

        :param is_ssl_verify_enabled:
            The value to assign to the is_ssl_verify_enabled property of this CreatePrivateSoftwareSourceDetails.
        :type is_ssl_verify_enabled: bool

        :param advanced_repo_options:
            The value to assign to the advanced_repo_options property of this CreatePrivateSoftwareSourceDetails.
        :type advanced_repo_options: str

        :param is_mirror_sync_allowed:
            The value to assign to the is_mirror_sync_allowed property of this CreatePrivateSoftwareSourceDetails.
        :type is_mirror_sync_allowed: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'software_source_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'os_family': 'str',
            'arch_type': 'str',
            'url': 'str',
            'gpg_key_url': 'str',
            'is_gpg_check_enabled': 'bool',
            'is_ssl_verify_enabled': 'bool',
            'advanced_repo_options': 'str',
            'is_mirror_sync_allowed': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'url': 'url',
            'gpg_key_url': 'gpgKeyUrl',
            'is_gpg_check_enabled': 'isGpgCheckEnabled',
            'is_ssl_verify_enabled': 'isSslVerifyEnabled',
            'advanced_repo_options': 'advancedRepoOptions',
            'is_mirror_sync_allowed': 'isMirrorSyncAllowed'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._software_source_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._os_family = None
        self._arch_type = None
        self._url = None
        self._gpg_key_url = None
        self._is_gpg_check_enabled = None
        self._is_ssl_verify_enabled = None
        self._advanced_repo_options = None
        self._is_mirror_sync_allowed = None
        self._software_source_type = 'PRIVATE'

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this CreatePrivateSoftwareSourceDetails.
        The OS family for the private software source.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"


        :return: The os_family of this CreatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this CreatePrivateSoftwareSourceDetails.
        The OS family for the private software source.


        :param os_family: The os_family of this CreatePrivateSoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            raise ValueError(
                f"Invalid value for `os_family`, must be None or one of {allowed_values}"
            )
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this CreatePrivateSoftwareSourceDetails.
        The architecture type supported by the private software source.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"


        :return: The arch_type of this CreatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this CreatePrivateSoftwareSourceDetails.
        The architecture type supported by the private software source.


        :param arch_type: The arch_type of this CreatePrivateSoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            raise ValueError(
                f"Invalid value for `arch_type`, must be None or one of {allowed_values}"
            )
        self._arch_type = arch_type

    @property
    def url(self):
        """
        **[Required]** Gets the url of this CreatePrivateSoftwareSourceDetails.
        URL for the private software source.


        :return: The url of this CreatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CreatePrivateSoftwareSourceDetails.
        URL for the private software source.


        :param url: The url of this CreatePrivateSoftwareSourceDetails.
        :type: str
        """
        self._url = url

    @property
    def gpg_key_url(self):
        """
        Gets the gpg_key_url of this CreatePrivateSoftwareSourceDetails.
        URI of the GPG key for this software source.


        :return: The gpg_key_url of this CreatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._gpg_key_url

    @gpg_key_url.setter
    def gpg_key_url(self, gpg_key_url):
        """
        Sets the gpg_key_url of this CreatePrivateSoftwareSourceDetails.
        URI of the GPG key for this software source.


        :param gpg_key_url: The gpg_key_url of this CreatePrivateSoftwareSourceDetails.
        :type: str
        """
        self._gpg_key_url = gpg_key_url

    @property
    def is_gpg_check_enabled(self):
        """
        Gets the is_gpg_check_enabled of this CreatePrivateSoftwareSourceDetails.
        Whether signature verification should be done for the software source


        :return: The is_gpg_check_enabled of this CreatePrivateSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_gpg_check_enabled

    @is_gpg_check_enabled.setter
    def is_gpg_check_enabled(self, is_gpg_check_enabled):
        """
        Sets the is_gpg_check_enabled of this CreatePrivateSoftwareSourceDetails.
        Whether signature verification should be done for the software source


        :param is_gpg_check_enabled: The is_gpg_check_enabled of this CreatePrivateSoftwareSourceDetails.
        :type: bool
        """
        self._is_gpg_check_enabled = is_gpg_check_enabled

    @property
    def is_ssl_verify_enabled(self):
        """
        Gets the is_ssl_verify_enabled of this CreatePrivateSoftwareSourceDetails.
        Whether SSL validation needs to be turned on


        :return: The is_ssl_verify_enabled of this CreatePrivateSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_ssl_verify_enabled

    @is_ssl_verify_enabled.setter
    def is_ssl_verify_enabled(self, is_ssl_verify_enabled):
        """
        Sets the is_ssl_verify_enabled of this CreatePrivateSoftwareSourceDetails.
        Whether SSL validation needs to be turned on


        :param is_ssl_verify_enabled: The is_ssl_verify_enabled of this CreatePrivateSoftwareSourceDetails.
        :type: bool
        """
        self._is_ssl_verify_enabled = is_ssl_verify_enabled

    @property
    def advanced_repo_options(self):
        """
        Gets the advanced_repo_options of this CreatePrivateSoftwareSourceDetails.
        Advanced repository options for the software source


        :return: The advanced_repo_options of this CreatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._advanced_repo_options

    @advanced_repo_options.setter
    def advanced_repo_options(self, advanced_repo_options):
        """
        Sets the advanced_repo_options of this CreatePrivateSoftwareSourceDetails.
        Advanced repository options for the software source


        :param advanced_repo_options: The advanced_repo_options of this CreatePrivateSoftwareSourceDetails.
        :type: str
        """
        self._advanced_repo_options = advanced_repo_options

    @property
    def is_mirror_sync_allowed(self):
        """
        Gets the is_mirror_sync_allowed of this CreatePrivateSoftwareSourceDetails.
        Whether this software source can be synced to a management station


        :return: The is_mirror_sync_allowed of this CreatePrivateSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_mirror_sync_allowed

    @is_mirror_sync_allowed.setter
    def is_mirror_sync_allowed(self, is_mirror_sync_allowed):
        """
        Sets the is_mirror_sync_allowed of this CreatePrivateSoftwareSourceDetails.
        Whether this software source can be synced to a management station


        :param is_mirror_sync_allowed: The is_mirror_sync_allowed of this CreatePrivateSoftwareSourceDetails.
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
