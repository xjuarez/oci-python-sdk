# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .package_summary import PackageSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailablePackageSummary(PackageSummary):
    """
    A software package available for install on a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailablePackageSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.AvailablePackageSummary.package_classification` attribute
        of this class is ``AVAILABLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this AvailablePackageSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this AvailablePackageSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this AvailablePackageSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this AvailablePackageSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this AvailablePackageSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        :param software_sources:
            The value to assign to the software_sources property of this AvailablePackageSummary.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param package_classification:
            The value to assign to the package_classification property of this AvailablePackageSummary.
            Allowed values for this property are: "INSTALLED", "AVAILABLE", "UPDATABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_classification: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'software_sources': 'list[SoftwareSourceDetails]',
            'package_classification': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'software_sources': 'softwareSources',
            'package_classification': 'packageClassification'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._software_sources = None
        self._package_classification = None
        self._package_classification = 'AVAILABLE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
