# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwarePackageSummary(object):
    """
    Summary information for a software package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwarePackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this SoftwarePackageSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this SoftwarePackageSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this SoftwarePackageSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this SoftwarePackageSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this SoftwarePackageSummary.
        :type architecture: str

        :param checksum:
            The value to assign to the checksum property of this SoftwarePackageSummary.
        :type checksum: str

        :param checksum_type:
            The value to assign to the checksum_type property of this SoftwarePackageSummary.
        :type checksum_type: str

        :param is_latest:
            The value to assign to the is_latest property of this SoftwarePackageSummary.
        :type is_latest: bool

        :param software_sources:
            The value to assign to the software_sources property of this SoftwarePackageSummary.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'checksum': 'str',
            'checksum_type': 'str',
            'is_latest': 'bool',
            'software_sources': 'list[SoftwareSourceDetails]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'checksum': 'checksum',
            'checksum_type': 'checksumType',
            'is_latest': 'isLatest',
            'software_sources': 'softwareSources'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._checksum = None
        self._checksum_type = None
        self._is_latest = None
        self._software_sources = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SoftwarePackageSummary.
        Package name.


        :return: The display_name of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwarePackageSummary.
        Package name.


        :param display_name: The display_name of this SoftwarePackageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SoftwarePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID.


        :return: The name of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SoftwarePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID.


        :param name: The name of this SoftwarePackageSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SoftwarePackageSummary.
        Type of the package.


        :return: The type of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SoftwarePackageSummary.
        Type of the package.


        :param type: The type of this SoftwarePackageSummary.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this SoftwarePackageSummary.
        Version of the package.


        :return: The version of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SoftwarePackageSummary.
        Version of the package.


        :param version: The version of this SoftwarePackageSummary.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this SoftwarePackageSummary.
        The architecture for which this software was built.


        :return: The architecture of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this SoftwarePackageSummary.
        The architecture for which this software was built.


        :param architecture: The architecture of this SoftwarePackageSummary.
        :type: str
        """
        self._architecture = architecture

    @property
    def checksum(self):
        """
        Gets the checksum of this SoftwarePackageSummary.
        Checksum of the package.


        :return: The checksum of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this SoftwarePackageSummary.
        Checksum of the package.


        :param checksum: The checksum of this SoftwarePackageSummary.
        :type: str
        """
        self._checksum = checksum

    @property
    def checksum_type(self):
        """
        Gets the checksum_type of this SoftwarePackageSummary.
        Type of the checksum.


        :return: The checksum_type of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this SoftwarePackageSummary.
        Type of the checksum.


        :param checksum_type: The checksum_type of this SoftwarePackageSummary.
        :type: str
        """
        self._checksum_type = checksum_type

    @property
    def is_latest(self):
        """
        Gets the is_latest of this SoftwarePackageSummary.
        Indicates whether this package is the latest version.


        :return: The is_latest of this SoftwarePackageSummary.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """
        Sets the is_latest of this SoftwarePackageSummary.
        Indicates whether this package is the latest version.


        :param is_latest: The is_latest of this SoftwarePackageSummary.
        :type: bool
        """
        self._is_latest = is_latest

    @property
    def software_sources(self):
        """
        Gets the software_sources of this SoftwarePackageSummary.
        List of software sources that provide the software package.


        :return: The software_sources of this SoftwarePackageSummary.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this SoftwarePackageSummary.
        List of software sources that provide the software package.


        :param software_sources: The software_sources of this SoftwarePackageSummary.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_sources = software_sources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
