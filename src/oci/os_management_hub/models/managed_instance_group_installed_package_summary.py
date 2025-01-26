# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceGroupInstalledPackageSummary(object):
    """
    Provides summary information for a package installed on a managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceGroupInstalledPackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ManagedInstanceGroupInstalledPackageSummary.
        :type name: str

        :param architecture:
            The value to assign to the architecture property of this ManagedInstanceGroupInstalledPackageSummary.
        :type architecture: str

        """
        self.swagger_types = {
            'name': 'str',
            'architecture': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'architecture': 'architecture'
        }

        self._name = None
        self._architecture = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedInstanceGroupInstalledPackageSummary.
        The name of the package that is installed on the managed instance group.


        :return: The name of this ManagedInstanceGroupInstalledPackageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedInstanceGroupInstalledPackageSummary.
        The name of the package that is installed on the managed instance group.


        :param name: The name of this ManagedInstanceGroupInstalledPackageSummary.
        :type: str
        """
        self._name = name

    @property
    def architecture(self):
        """
        **[Required]** Gets the architecture of this ManagedInstanceGroupInstalledPackageSummary.
        The architecture of the package that is installed on the managed instance group.


        :return: The architecture of this ManagedInstanceGroupInstalledPackageSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this ManagedInstanceGroupInstalledPackageSummary.
        The architecture of the package that is installed on the managed instance group.


        :param architecture: The architecture of this ManagedInstanceGroupInstalledPackageSummary.
        :type: str
        """
        self._architecture = architecture

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
