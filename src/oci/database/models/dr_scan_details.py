# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrScanDetails(object):
    """
    The Single Client Access Name (SCAN) details for Disaster recovery network.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DrScanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this DrScanDetails.
        :type hostname: str

        :param scan_listener_port_tcp:
            The value to assign to the scan_listener_port_tcp property of this DrScanDetails.
        :type scan_listener_port_tcp: int

        :param ips:
            The value to assign to the ips property of this DrScanDetails.
        :type ips: list[str]

        """
        self.swagger_types = {
            'hostname': 'str',
            'scan_listener_port_tcp': 'int',
            'ips': 'list[str]'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'scan_listener_port_tcp': 'scanListenerPortTcp',
            'ips': 'ips'
        }

        self._hostname = None
        self._scan_listener_port_tcp = None
        self._ips = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this DrScanDetails.
        The Disaster recovery SCAN hostname.


        :return: The hostname of this DrScanDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DrScanDetails.
        The Disaster recovery SCAN hostname.


        :param hostname: The hostname of this DrScanDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def scan_listener_port_tcp(self):
        """
        **[Required]** Gets the scan_listener_port_tcp of this DrScanDetails.
        The Disaster recovery SCAN TCPIP port. Default is 1521.


        :return: The scan_listener_port_tcp of this DrScanDetails.
        :rtype: int
        """
        return self._scan_listener_port_tcp

    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, scan_listener_port_tcp):
        """
        Sets the scan_listener_port_tcp of this DrScanDetails.
        The Disaster recovery SCAN TCPIP port. Default is 1521.


        :param scan_listener_port_tcp: The scan_listener_port_tcp of this DrScanDetails.
        :type: int
        """
        self._scan_listener_port_tcp = scan_listener_port_tcp

    @property
    def ips(self):
        """
        **[Required]** Gets the ips of this DrScanDetails.
        The list of Disaster recovery SCAN IP addresses. Three addresses should be provided.


        :return: The ips of this DrScanDetails.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """
        Sets the ips of this DrScanDetails.
        The list of Disaster recovery SCAN IP addresses. Three addresses should be provided.


        :param ips: The ips of this DrScanDetails.
        :type: list[str]
        """
        self._ips = ips

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
