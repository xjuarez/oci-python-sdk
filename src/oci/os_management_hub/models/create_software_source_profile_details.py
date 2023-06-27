# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_profile_details import CreateProfileDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSoftwareSourceProfileDetails(CreateProfileDetails):
    """
    Description of a software source registration profile to be created.
    """

    #: A constant which can be used with the vendor_name property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    #: A constant which can be used with the os_family property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceProfileDetails.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSoftwareSourceProfileDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CreateSoftwareSourceProfileDetails.profile_type` attribute
        of this class is ``SOFTWARESOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateSoftwareSourceProfileDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSoftwareSourceProfileDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateSoftwareSourceProfileDetails.
        :type description: str

        :param management_station_id:
            The value to assign to the management_station_id property of this CreateSoftwareSourceProfileDetails.
        :type management_station_id: str

        :param profile_type:
            The value to assign to the profile_type property of this CreateSoftwareSourceProfileDetails.
            Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"
        :type profile_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSoftwareSourceProfileDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSoftwareSourceProfileDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vendor_name:
            The value to assign to the vendor_name property of this CreateSoftwareSourceProfileDetails.
            Allowed values for this property are: "ORACLE"
        :type vendor_name: str

        :param os_family:
            The value to assign to the os_family property of this CreateSoftwareSourceProfileDetails.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this CreateSoftwareSourceProfileDetails.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"
        :type arch_type: str

        :param software_source_ids:
            The value to assign to the software_source_ids property of this CreateSoftwareSourceProfileDetails.
        :type software_source_ids: list[str]

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'management_station_id': 'str',
            'profile_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vendor_name': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'software_source_ids': 'list[str]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'management_station_id': 'managementStationId',
            'profile_type': 'profileType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vendor_name': 'vendorName',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'software_source_ids': 'softwareSourceIds'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._management_station_id = None
        self._profile_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vendor_name = None
        self._os_family = None
        self._arch_type = None
        self._software_source_ids = None
        self._profile_type = 'SOFTWARESOURCE'

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this CreateSoftwareSourceProfileDetails.
        The software source vendor name.

        Allowed values for this property are: "ORACLE"


        :return: The vendor_name of this CreateSoftwareSourceProfileDetails.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this CreateSoftwareSourceProfileDetails.
        The software source vendor name.


        :param vendor_name: The vendor_name of this CreateSoftwareSourceProfileDetails.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            raise ValueError(
                "Invalid value for `vendor_name`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._vendor_name = vendor_name

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this CreateSoftwareSourceProfileDetails.
        The operating system family.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"


        :return: The os_family of this CreateSoftwareSourceProfileDetails.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this CreateSoftwareSourceProfileDetails.
        The operating system family.


        :param os_family: The os_family of this CreateSoftwareSourceProfileDetails.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            raise ValueError(
                "Invalid value for `os_family`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this CreateSoftwareSourceProfileDetails.
        The architecture type.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"


        :return: The arch_type of this CreateSoftwareSourceProfileDetails.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this CreateSoftwareSourceProfileDetails.
        The architecture type.


        :param arch_type: The arch_type of this CreateSoftwareSourceProfileDetails.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            raise ValueError(
                "Invalid value for `arch_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._arch_type = arch_type

    @property
    def software_source_ids(self):
        """
        **[Required]** Gets the software_source_ids of this CreateSoftwareSourceProfileDetails.
        The list of software source OCIDs that the registration profile will use.


        :return: The software_source_ids of this CreateSoftwareSourceProfileDetails.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this CreateSoftwareSourceProfileDetails.
        The list of software source OCIDs that the registration profile will use.


        :param software_source_ids: The software_source_ids of this CreateSoftwareSourceProfileDetails.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
