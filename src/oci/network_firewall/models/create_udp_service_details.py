# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501

from .create_service_details import CreateServiceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateUdpServiceDetails(CreateServiceDetails):
    """
    Request for UDP Service used on the firewall policy rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateUdpServiceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.CreateUdpServiceDetails.type` attribute
        of this class is ``UDP_SERVICE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateUdpServiceDetails.
        :type name: str

        :param type:
            The value to assign to the type property of this CreateUdpServiceDetails.
            Allowed values for this property are: "TCP_SERVICE", "UDP_SERVICE"
        :type type: str

        :param port_ranges:
            The value to assign to the port_ranges property of this CreateUdpServiceDetails.
        :type port_ranges: list[oci.network_firewall.models.PortRange]

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'port_ranges': 'list[PortRange]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'port_ranges': 'portRanges'
        }

        self._name = None
        self._type = None
        self._port_ranges = None
        self._type = 'UDP_SERVICE'

    @property
    def port_ranges(self):
        """
        **[Required]** Gets the port_ranges of this CreateUdpServiceDetails.
        List of port-ranges to be used.


        :return: The port_ranges of this CreateUdpServiceDetails.
        :rtype: list[oci.network_firewall.models.PortRange]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        """
        Sets the port_ranges of this CreateUdpServiceDetails.
        List of port-ranges to be used.


        :param port_ranges: The port_ranges of this CreateUdpServiceDetails.
        :type: list[oci.network_firewall.models.PortRange]
        """
        self._port_ranges = port_ranges

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
