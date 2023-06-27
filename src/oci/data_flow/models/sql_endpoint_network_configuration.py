# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlEndpointNetworkConfiguration(object):
    """
    The network configuration of a SQL Endpoint.
    """

    #: A constant which can be used with the network_type property of a SqlEndpointNetworkConfiguration.
    #: This constant has a value of "VCN"
    NETWORK_TYPE_VCN = "VCN"

    #: A constant which can be used with the network_type property of a SqlEndpointNetworkConfiguration.
    #: This constant has a value of "SECURE_ACCESS"
    NETWORK_TYPE_SECURE_ACCESS = "SECURE_ACCESS"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlEndpointNetworkConfiguration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_flow.models.SqlEndpointVcnConfig`
        * :class:`~oci.data_flow.models.SqlEndpointSecureAccessConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_type:
            The value to assign to the network_type property of this SqlEndpointNetworkConfiguration.
            Allowed values for this property are: "VCN", "SECURE_ACCESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_type: str

        """
        self.swagger_types = {
            'network_type': 'str'
        }

        self.attribute_map = {
            'network_type': 'networkType'
        }

        self._network_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['networkType']

        if type == 'VCN':
            return 'SqlEndpointVcnConfig'

        if type == 'SECURE_ACCESS':
            return 'SqlEndpointSecureAccessConfig'
        else:
            return 'SqlEndpointNetworkConfiguration'

    @property
    def network_type(self):
        """
        **[Required]** Gets the network_type of this SqlEndpointNetworkConfiguration.
        The type of network configuration.

        Allowed values for this property are: "VCN", "SECURE_ACCESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_type of this SqlEndpointNetworkConfiguration.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this SqlEndpointNetworkConfiguration.
        The type of network configuration.


        :param network_type: The network_type of this SqlEndpointNetworkConfiguration.
        :type: str
        """
        allowed_values = ["VCN", "SECURE_ACCESS"]
        if not value_allowed_none_or_none_sentinel(network_type, allowed_values):
            network_type = 'UNKNOWN_ENUM_VALUE'
        self._network_type = network_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
