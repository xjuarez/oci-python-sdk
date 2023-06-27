# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .software_source import SoftwareSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VendorSoftwareSource(SoftwareSource):
    """
    A vendor software source contains a collection of packages.
    """

    #: A constant which can be used with the vendor_name property of a VendorSoftwareSource.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new VendorSoftwareSource object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.VendorSoftwareSource.software_source_type` attribute
        of this class is ``VENDOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VendorSoftwareSource.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VendorSoftwareSource.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this VendorSoftwareSource.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this VendorSoftwareSource.
        :type time_created: datetime

        :param description:
            The value to assign to the description property of this VendorSoftwareSource.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this VendorSoftwareSource.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type software_source_type: str

        :param availability:
            The value to assign to the availability property of this VendorSoftwareSource.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability: str

        :param repo_id:
            The value to assign to the repo_id property of this VendorSoftwareSource.
        :type repo_id: str

        :param os_family:
            The value to assign to the os_family property of this VendorSoftwareSource.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this VendorSoftwareSource.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VendorSoftwareSource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param package_count:
            The value to assign to the package_count property of this VendorSoftwareSource.
        :type package_count: int

        :param url:
            The value to assign to the url property of this VendorSoftwareSource.
        :type url: str

        :param checksum_type:
            The value to assign to the checksum_type property of this VendorSoftwareSource.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type checksum_type: str

        :param gpg_key_url:
            The value to assign to the gpg_key_url property of this VendorSoftwareSource.
        :type gpg_key_url: str

        :param gpg_key_id:
            The value to assign to the gpg_key_id property of this VendorSoftwareSource.
        :type gpg_key_id: str

        :param gpg_key_fingerprint:
            The value to assign to the gpg_key_fingerprint property of this VendorSoftwareSource.
        :type gpg_key_fingerprint: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VendorSoftwareSource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VendorSoftwareSource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VendorSoftwareSource.
        :type system_tags: dict(str, dict(str, object))

        :param vendor_name:
            The value to assign to the vendor_name property of this VendorSoftwareSource.
            Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vendor_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'description': 'str',
            'software_source_type': 'str',
            'availability': 'str',
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
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'vendor_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'availability': 'availability',
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
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'vendor_name': 'vendorName'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._description = None
        self._software_source_type = None
        self._availability = None
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
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._vendor_name = None
        self._software_source_type = 'VENDOR'

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this VendorSoftwareSource.
        Name of the vendor providing the software source.

        Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vendor_name of this VendorSoftwareSource.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this VendorSoftwareSource.
        Name of the vendor providing the software source.


        :param vendor_name: The vendor_name of this VendorSoftwareSource.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            vendor_name = 'UNKNOWN_ENUM_VALUE'
        self._vendor_name = vendor_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
