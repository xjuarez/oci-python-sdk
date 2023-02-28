# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .importable_compute_entity_summary import ImportableComputeEntitySummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudImportableComputeEntitySummary(ImportableComputeEntitySummary):
    """
    A compute host entity that can be imported into Operations Insights.
    """

    #: A constant which can be used with the platform_type property of a CloudImportableComputeEntitySummary.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a CloudImportableComputeEntitySummary.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the platform_type property of a CloudImportableComputeEntitySummary.
    #: This constant has a value of "SUNOS"
    PLATFORM_TYPE_SUNOS = "SUNOS"

    #: A constant which can be used with the platform_type property of a CloudImportableComputeEntitySummary.
    #: This constant has a value of "ZLINUX"
    PLATFORM_TYPE_ZLINUX = "ZLINUX"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudImportableComputeEntitySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CloudImportableComputeEntitySummary.entity_source` attribute
        of this class is ``MACS_MANAGED_CLOUD_HOST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this CloudImportableComputeEntitySummary.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "MACS_MANAGED_CLOUD_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param compute_id:
            The value to assign to the compute_id property of this CloudImportableComputeEntitySummary.
        :type compute_id: str

        :param compute_display_name:
            The value to assign to the compute_display_name property of this CloudImportableComputeEntitySummary.
        :type compute_display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloudImportableComputeEntitySummary.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this CloudImportableComputeEntitySummary.
        :type host_name: str

        :param platform_type:
            The value to assign to the platform_type property of this CloudImportableComputeEntitySummary.
            Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compute_id': 'str',
            'compute_display_name': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'platform_type': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compute_id': 'computeId',
            'compute_display_name': 'computeDisplayName',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'platform_type': 'platformType'
        }

        self._entity_source = None
        self._compute_id = None
        self._compute_display_name = None
        self._compartment_id = None
        self._host_name = None
        self._platform_type = None
        self._entity_source = 'MACS_MANAGED_CLOUD_HOST'

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this CloudImportableComputeEntitySummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :return: The host_name of this CloudImportableComputeEntitySummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this CloudImportableComputeEntitySummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :param host_name: The host_name of this CloudImportableComputeEntitySummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def platform_type(self):
        """
        **[Required]** Gets the platform_type of this CloudImportableComputeEntitySummary.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for MACS-managed cloud host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].

        Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this CloudImportableComputeEntitySummary.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this CloudImportableComputeEntitySummary.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for MACS-managed cloud host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].


        :param platform_type: The platform_type of this CloudImportableComputeEntitySummary.
        :type: str
        """
        allowed_values = ["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
