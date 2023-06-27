# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .sql_endpoint_network_configuration import SqlEndpointNetworkConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlEndpointSecureAccessConfig(SqlEndpointNetworkConfiguration):
    """
    Access control rules for secure access selection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlEndpointSecureAccessConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.data_flow.models.SqlEndpointSecureAccessConfig.network_type` attribute
        of this class is ``SECURE_ACCESS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_type:
            The value to assign to the network_type property of this SqlEndpointSecureAccessConfig.
            Allowed values for this property are: "VCN", "SECURE_ACCESS"
        :type network_type: str

        :param access_control_rules:
            The value to assign to the access_control_rules property of this SqlEndpointSecureAccessConfig.
        :type access_control_rules: list[oci.data_flow.models.SecureAccessControlRule]

        :param public_endpoint_ip:
            The value to assign to the public_endpoint_ip property of this SqlEndpointSecureAccessConfig.
        :type public_endpoint_ip: str

        """
        self.swagger_types = {
            'network_type': 'str',
            'access_control_rules': 'list[SecureAccessControlRule]',
            'public_endpoint_ip': 'str'
        }

        self.attribute_map = {
            'network_type': 'networkType',
            'access_control_rules': 'accessControlRules',
            'public_endpoint_ip': 'publicEndpointIp'
        }

        self._network_type = None
        self._access_control_rules = None
        self._public_endpoint_ip = None
        self._network_type = 'SECURE_ACCESS'

    @property
    def access_control_rules(self):
        """
        Gets the access_control_rules of this SqlEndpointSecureAccessConfig.
        A list of SecureAccessControlRule's to which access is limited to


        :return: The access_control_rules of this SqlEndpointSecureAccessConfig.
        :rtype: list[oci.data_flow.models.SecureAccessControlRule]
        """
        return self._access_control_rules

    @access_control_rules.setter
    def access_control_rules(self, access_control_rules):
        """
        Sets the access_control_rules of this SqlEndpointSecureAccessConfig.
        A list of SecureAccessControlRule's to which access is limited to


        :param access_control_rules: The access_control_rules of this SqlEndpointSecureAccessConfig.
        :type: list[oci.data_flow.models.SecureAccessControlRule]
        """
        self._access_control_rules = access_control_rules

    @property
    def public_endpoint_ip(self):
        """
        Gets the public_endpoint_ip of this SqlEndpointSecureAccessConfig.
        Ip Address of public endpoint


        :return: The public_endpoint_ip of this SqlEndpointSecureAccessConfig.
        :rtype: str
        """
        return self._public_endpoint_ip

    @public_endpoint_ip.setter
    def public_endpoint_ip(self, public_endpoint_ip):
        """
        Sets the public_endpoint_ip of this SqlEndpointSecureAccessConfig.
        Ip Address of public endpoint


        :param public_endpoint_ip: The public_endpoint_ip of this SqlEndpointSecureAccessConfig.
        :type: str
        """
        self._public_endpoint_ip = public_endpoint_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
