# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LicensingConfig(object):
    """
    Configuration of the Operating System license.
    """

    #: A constant which can be used with the type property of a LicensingConfig.
    #: This constant has a value of "WINDOWS"
    TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the license_type property of a LicensingConfig.
    #: This constant has a value of "OCI_PROVIDED"
    LICENSE_TYPE_OCI_PROVIDED = "OCI_PROVIDED"

    #: A constant which can be used with the license_type property of a LicensingConfig.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new LicensingConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LicensingConfig.
            Allowed values for this property are: "WINDOWS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param license_type:
            The value to assign to the license_type property of this LicensingConfig.
            Allowed values for this property are: "OCI_PROVIDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_type: str

        :param os_version:
            The value to assign to the os_version property of this LicensingConfig.
        :type os_version: str

        """
        self.swagger_types = {
            'type': 'str',
            'license_type': 'str',
            'os_version': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'license_type': 'licenseType',
            'os_version': 'osVersion'
        }

        self._type = None
        self._license_type = None
        self._os_version = None

    @property
    def type(self):
        """
        Gets the type of this LicensingConfig.
        Operating System type of the Configuration.

        Allowed values for this property are: "WINDOWS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this LicensingConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LicensingConfig.
        Operating System type of the Configuration.


        :param type: The type of this LicensingConfig.
        :type: str
        """
        allowed_values = ["WINDOWS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def license_type(self):
        """
        Gets the license_type of this LicensingConfig.
        License Type for the OS license.
        * `OCI_PROVIDED` - OCI provided license (e.g. metered $/OCPU-hour).
        * `BRING_YOUR_OWN_LICENSE` - Bring your own license.

        Allowed values for this property are: "OCI_PROVIDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_type of this LicensingConfig.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this LicensingConfig.
        License Type for the OS license.
        * `OCI_PROVIDED` - OCI provided license (e.g. metered $/OCPU-hour).
        * `BRING_YOUR_OWN_LICENSE` - Bring your own license.


        :param license_type: The license_type of this LicensingConfig.
        :type: str
        """
        allowed_values = ["OCI_PROVIDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            license_type = 'UNKNOWN_ENUM_VALUE'
        self._license_type = license_type

    @property
    def os_version(self):
        """
        Gets the os_version of this LicensingConfig.
        The Operating System version of the license config.


        :return: The os_version of this LicensingConfig.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this LicensingConfig.
        The Operating System version of the license config.


        :param os_version: The os_version of this LicensingConfig.
        :type: str
        """
        self._os_version = os_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
