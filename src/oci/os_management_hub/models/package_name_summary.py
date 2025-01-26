# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageNameSummary(object):
    """
    Provides summary information about a package.
    """

    #: A constant which can be used with the architecture property of a PackageNameSummary.
    #: This constant has a value of "X86_64"
    ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the architecture property of a PackageNameSummary.
    #: This constant has a value of "AARCH64"
    ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the architecture property of a PackageNameSummary.
    #: This constant has a value of "I686"
    ARCHITECTURE_I686 = "I686"

    #: A constant which can be used with the architecture property of a PackageNameSummary.
    #: This constant has a value of "NOARCH"
    ARCHITECTURE_NOARCH = "NOARCH"

    #: A constant which can be used with the architecture property of a PackageNameSummary.
    #: This constant has a value of "SRC"
    ARCHITECTURE_SRC = "SRC"

    def __init__(self, **kwargs):
        """
        Initializes a new PackageNameSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this PackageNameSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this PackageNameSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this PackageNameSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this PackageNameSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this PackageNameSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PackageNameSummary.
        Full package name in NERVA format. This value should be unique.


        :return: The display_name of this PackageNameSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PackageNameSummary.
        Full package name in NERVA format. This value should be unique.


        :param display_name: The display_name of this PackageNameSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PackageNameSummary.
        The name of the software package.


        :return: The name of this PackageNameSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PackageNameSummary.
        The name of the software package.


        :param name: The name of this PackageNameSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this PackageNameSummary.
        Type of the package.


        :return: The type of this PackageNameSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PackageNameSummary.
        Type of the package.


        :param type: The type of this PackageNameSummary.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        Gets the version of this PackageNameSummary.
        The version of the software package.


        :return: The version of this PackageNameSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PackageNameSummary.
        The version of the software package.


        :param version: The version of this PackageNameSummary.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this PackageNameSummary.
        The CPU architecture type for which this package was built.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The architecture of this PackageNameSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this PackageNameSummary.
        The CPU architecture type for which this package was built.


        :param architecture: The architecture of this PackageNameSummary.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(architecture, allowed_values):
            architecture = 'UNKNOWN_ENUM_VALUE'
        self._architecture = architecture

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
