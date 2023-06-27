# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageFilter(object):
    """
    Used to select packages from VendorSoftwareSources to create/update CustomSoftwareSources.
    """

    #: A constant which can be used with the filter_type property of a PackageFilter.
    #: This constant has a value of "INCLUDE"
    FILTER_TYPE_INCLUDE = "INCLUDE"

    #: A constant which can be used with the filter_type property of a PackageFilter.
    #: This constant has a value of "EXCLUDE"
    FILTER_TYPE_EXCLUDE = "EXCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new PackageFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_name:
            The value to assign to the package_name property of this PackageFilter.
        :type package_name: str

        :param package_name_pattern:
            The value to assign to the package_name_pattern property of this PackageFilter.
        :type package_name_pattern: str

        :param package_version:
            The value to assign to the package_version property of this PackageFilter.
        :type package_version: str

        :param filter_type:
            The value to assign to the filter_type property of this PackageFilter.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        """
        self.swagger_types = {
            'package_name': 'str',
            'package_name_pattern': 'str',
            'package_version': 'str',
            'filter_type': 'str'
        }

        self.attribute_map = {
            'package_name': 'packageName',
            'package_name_pattern': 'packageNamePattern',
            'package_version': 'packageVersion',
            'filter_type': 'filterType'
        }

        self._package_name = None
        self._package_name_pattern = None
        self._package_version = None
        self._filter_type = None

    @property
    def package_name(self):
        """
        Gets the package_name of this PackageFilter.
        The package name.


        :return: The package_name of this PackageFilter.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this PackageFilter.
        The package name.


        :param package_name: The package_name of this PackageFilter.
        :type: str
        """
        self._package_name = package_name

    @property
    def package_name_pattern(self):
        """
        Gets the package_name_pattern of this PackageFilter.
        The package name pattern.


        :return: The package_name_pattern of this PackageFilter.
        :rtype: str
        """
        return self._package_name_pattern

    @package_name_pattern.setter
    def package_name_pattern(self, package_name_pattern):
        """
        Sets the package_name_pattern of this PackageFilter.
        The package name pattern.


        :param package_name_pattern: The package_name_pattern of this PackageFilter.
        :type: str
        """
        self._package_name_pattern = package_name_pattern

    @property
    def package_version(self):
        """
        Gets the package_version of this PackageFilter.
        The package version, which is denoted by 'version-release', or 'epoch:version-release'.


        :return: The package_version of this PackageFilter.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this PackageFilter.
        The package version, which is denoted by 'version-release', or 'epoch:version-release'.


        :param package_version: The package_version of this PackageFilter.
        :type: str
        """
        self._package_version = package_version

    @property
    def filter_type(self):
        """
        **[Required]** Gets the filter_type of this PackageFilter.
        The type of the filter, which can be of two types - INCLUDE or EXCLUDE.

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The filter_type of this PackageFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this PackageFilter.
        The type of the filter, which can be of two types - INCLUDE or EXCLUDE.


        :param filter_type: The filter_type of this PackageFilter.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            filter_type = 'UNKNOWN_ENUM_VALUE'
        self._filter_type = filter_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
