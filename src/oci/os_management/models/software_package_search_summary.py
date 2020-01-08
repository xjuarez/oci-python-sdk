# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwarePackageSearchSummary(object):
    """
    Summary information for a software package
    """

    #: A constant which can be used with the advisory_type property of a SoftwarePackageSearchSummary.
    #: This constant has a value of "SECURITY"
    ADVISORY_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the advisory_type property of a SoftwarePackageSearchSummary.
    #: This constant has a value of "BUG"
    ADVISORY_TYPE_BUG = "BUG"

    #: A constant which can be used with the advisory_type property of a SoftwarePackageSearchSummary.
    #: This constant has a value of "ENHANCEMENT"
    ADVISORY_TYPE_ENHANCEMENT = "ENHANCEMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwarePackageSearchSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this SoftwarePackageSearchSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this SoftwarePackageSearchSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this SoftwarePackageSearchSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this SoftwarePackageSearchSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this SoftwarePackageSearchSummary.
        :type architecture: str

        :param summary:
            The value to assign to the summary property of this SoftwarePackageSearchSummary.
        :type summary: str

        :param advisory_type:
            The value to assign to the advisory_type property of this SoftwarePackageSearchSummary.
            Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type advisory_type: str

        :param errata:
            The value to assign to the errata property of this SoftwarePackageSearchSummary.
        :type errata: list[Id]

        :param software_sources:
            The value to assign to the software_sources property of this SoftwarePackageSearchSummary.
        :type software_sources: list[SoftwareSourceId]

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'summary': 'str',
            'advisory_type': 'str',
            'errata': 'list[Id]',
            'software_sources': 'list[SoftwareSourceId]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'summary': 'summary',
            'advisory_type': 'advisoryType',
            'errata': 'errata',
            'software_sources': 'softwareSources'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._summary = None
        self._advisory_type = None
        self._errata = None
        self._software_sources = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SoftwarePackageSearchSummary.
        Package name


        :return: The display_name of this SoftwarePackageSearchSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwarePackageSearchSummary.
        Package name


        :param display_name: The display_name of this SoftwarePackageSearchSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SoftwarePackageSearchSummary.
        Unique identifier for the package. NOTE - This is not an OCID


        :return: The name of this SoftwarePackageSearchSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SoftwarePackageSearchSummary.
        Unique identifier for the package. NOTE - This is not an OCID


        :param name: The name of this SoftwarePackageSearchSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SoftwarePackageSearchSummary.
        Type of the package


        :return: The type of this SoftwarePackageSearchSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SoftwarePackageSearchSummary.
        Type of the package


        :param type: The type of this SoftwarePackageSearchSummary.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this SoftwarePackageSearchSummary.
        Version of the package


        :return: The version of this SoftwarePackageSearchSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SoftwarePackageSearchSummary.
        Version of the package


        :param version: The version of this SoftwarePackageSearchSummary.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this SoftwarePackageSearchSummary.
        the architecture for which this software was built


        :return: The architecture of this SoftwarePackageSearchSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this SoftwarePackageSearchSummary.
        the architecture for which this software was built


        :param architecture: The architecture of this SoftwarePackageSearchSummary.
        :type: str
        """
        self._architecture = architecture

    @property
    def summary(self):
        """
        Gets the summary of this SoftwarePackageSearchSummary.
        a summary description of the software package


        :return: The summary of this SoftwarePackageSearchSummary.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this SoftwarePackageSearchSummary.
        a summary description of the software package


        :param summary: The summary of this SoftwarePackageSearchSummary.
        :type: str
        """
        self._summary = summary

    @property
    def advisory_type(self):
        """
        Gets the advisory_type of this SoftwarePackageSearchSummary.
        Type of the erratum.

        Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The advisory_type of this SoftwarePackageSearchSummary.
        :rtype: str
        """
        return self._advisory_type

    @advisory_type.setter
    def advisory_type(self, advisory_type):
        """
        Sets the advisory_type of this SoftwarePackageSearchSummary.
        Type of the erratum.


        :param advisory_type: The advisory_type of this SoftwarePackageSearchSummary.
        :type: str
        """
        allowed_values = ["SECURITY", "BUG", "ENHANCEMENT"]
        if not value_allowed_none_or_none_sentinel(advisory_type, allowed_values):
            advisory_type = 'UNKNOWN_ENUM_VALUE'
        self._advisory_type = advisory_type

    @property
    def errata(self):
        """
        Gets the errata of this SoftwarePackageSearchSummary.
        List of errata containing this software package


        :return: The errata of this SoftwarePackageSearchSummary.
        :rtype: list[Id]
        """
        return self._errata

    @errata.setter
    def errata(self, errata):
        """
        Sets the errata of this SoftwarePackageSearchSummary.
        List of errata containing this software package


        :param errata: The errata of this SoftwarePackageSearchSummary.
        :type: list[Id]
        """
        self._errata = errata

    @property
    def software_sources(self):
        """
        Gets the software_sources of this SoftwarePackageSearchSummary.
        list of software sources that provide the software package


        :return: The software_sources of this SoftwarePackageSearchSummary.
        :rtype: list[SoftwareSourceId]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this SoftwarePackageSearchSummary.
        list of software sources that provide the software package


        :param software_sources: The software_sources of this SoftwarePackageSearchSummary.
        :type: list[SoftwareSourceId]
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
