# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScanListenerInfo(object):
    """
    Customer's Real Application Cluster (RAC)'s SCAN listener FQDN, port or list IPs and their ports.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScanListenerInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scan_listener_fqdn:
            The value to assign to the scan_listener_fqdn property of this ScanListenerInfo.
        :type scan_listener_fqdn: str

        :param scan_listener_ip:
            The value to assign to the scan_listener_ip property of this ScanListenerInfo.
        :type scan_listener_ip: str

        :param scan_listener_port:
            The value to assign to the scan_listener_port property of this ScanListenerInfo.
        :type scan_listener_port: int

        """
        self.swagger_types = {
            'scan_listener_fqdn': 'str',
            'scan_listener_ip': 'str',
            'scan_listener_port': 'int'
        }

        self.attribute_map = {
            'scan_listener_fqdn': 'scanListenerFqdn',
            'scan_listener_ip': 'scanListenerIp',
            'scan_listener_port': 'scanListenerPort'
        }

        self._scan_listener_fqdn = None
        self._scan_listener_ip = None
        self._scan_listener_port = None

    @property
    def scan_listener_fqdn(self):
        """
        Gets the scan_listener_fqdn of this ScanListenerInfo.
        FQDN of the customer's Real Application Cluster (RAC)'s SCAN listeners.


        :return: The scan_listener_fqdn of this ScanListenerInfo.
        :rtype: str
        """
        return self._scan_listener_fqdn

    @scan_listener_fqdn.setter
    def scan_listener_fqdn(self, scan_listener_fqdn):
        """
        Sets the scan_listener_fqdn of this ScanListenerInfo.
        FQDN of the customer's Real Application Cluster (RAC)'s SCAN listeners.


        :param scan_listener_fqdn: The scan_listener_fqdn of this ScanListenerInfo.
        :type: str
        """
        self._scan_listener_fqdn = scan_listener_fqdn

    @property
    def scan_listener_ip(self):
        """
        Gets the scan_listener_ip of this ScanListenerInfo.
        A SCAN listener's IP of the customer's Real Application Cluster (RAC).


        :return: The scan_listener_ip of this ScanListenerInfo.
        :rtype: str
        """
        return self._scan_listener_ip

    @scan_listener_ip.setter
    def scan_listener_ip(self, scan_listener_ip):
        """
        Sets the scan_listener_ip of this ScanListenerInfo.
        A SCAN listener's IP of the customer's Real Application Cluster (RAC).


        :param scan_listener_ip: The scan_listener_ip of this ScanListenerInfo.
        :type: str
        """
        self._scan_listener_ip = scan_listener_ip

    @property
    def scan_listener_port(self):
        """
        Gets the scan_listener_port of this ScanListenerInfo.
        The port that customer's Real Application Cluster (RAC)'s SCAN listeners are listening on.


        :return: The scan_listener_port of this ScanListenerInfo.
        :rtype: int
        """
        return self._scan_listener_port

    @scan_listener_port.setter
    def scan_listener_port(self, scan_listener_port):
        """
        Sets the scan_listener_port of this ScanListenerInfo.
        The port that customer's Real Application Cluster (RAC)'s SCAN listeners are listening on.


        :param scan_listener_port: The scan_listener_port of this ScanListenerInfo.
        :type: int
        """
        self._scan_listener_port = scan_listener_port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
