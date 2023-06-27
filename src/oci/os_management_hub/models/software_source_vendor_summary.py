# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSourceVendorSummary(object):
    """
    Software vendor name, list of osFamily and archType.
    """

    #: A constant which can be used with the name property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "ORACLE"
    NAME_ORACLE = "ORACLE"

    #: A constant which can be used with the os_families property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILIES_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_families property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILIES_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_families property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILIES_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the arch_types property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "X86_64"
    ARCH_TYPES_X86_64 = "X86_64"

    #: A constant which can be used with the arch_types property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "AARCH64"
    ARCH_TYPES_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_types property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "I686"
    ARCH_TYPES_I686 = "I686"

    #: A constant which can be used with the arch_types property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "NOARCH"
    ARCH_TYPES_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_types property of a SoftwareSourceVendorSummary.
    #: This constant has a value of "SRC"
    ARCH_TYPES_SRC = "SRC"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSourceVendorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SoftwareSourceVendorSummary.
            Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param os_families:
            The value to assign to the os_families property of this SoftwareSourceVendorSummary.
            Allowed values for items in this list are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_families: list[str]

        :param arch_types:
            The value to assign to the arch_types property of this SoftwareSourceVendorSummary.
            Allowed values for items in this list are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_types: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'os_families': 'list[str]',
            'arch_types': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'os_families': 'osFamilies',
            'arch_types': 'archTypes'
        }

        self._name = None
        self._os_families = None
        self._arch_types = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SoftwareSourceVendorSummary.
        Name of the vendor providing the software source.

        Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this SoftwareSourceVendorSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SoftwareSourceVendorSummary.
        Name of the vendor providing the software source.


        :param name: The name of this SoftwareSourceVendorSummary.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def os_families(self):
        """
        **[Required]** Gets the os_families of this SoftwareSourceVendorSummary.
        List of corresponding osFamilies.

        Allowed values for items in this list are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_families of this SoftwareSourceVendorSummary.
        :rtype: list[str]
        """
        return self._os_families

    @os_families.setter
    def os_families(self, os_families):
        """
        Sets the os_families of this SoftwareSourceVendorSummary.
        List of corresponding osFamilies.


        :param os_families: The os_families of this SoftwareSourceVendorSummary.
        :type: list[str]
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if os_families:
            os_families[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in os_families]
        self._os_families = os_families

    @property
    def arch_types(self):
        """
        **[Required]** Gets the arch_types of this SoftwareSourceVendorSummary.
        List of corresponding archTypes.

        Allowed values for items in this list are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_types of this SoftwareSourceVendorSummary.
        :rtype: list[str]
        """
        return self._arch_types

    @arch_types.setter
    def arch_types(self, arch_types):
        """
        Sets the arch_types of this SoftwareSourceVendorSummary.
        List of corresponding archTypes.


        :param arch_types: The arch_types of this SoftwareSourceVendorSummary.
        :type: list[str]
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if arch_types:
            arch_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in arch_types]
        self._arch_types = arch_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
