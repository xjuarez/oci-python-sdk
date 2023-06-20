# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVmClusterNetworkDetails(object):
    """
    Details for an Exadata VM cluster network. Applies to Exadata Cloud@Customer instances only.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVmClusterNetworkDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scans:
            The value to assign to the scans property of this UpdateVmClusterNetworkDetails.
        :type scans: list[oci.database.models.ScanDetails]

        :param dns:
            The value to assign to the dns property of this UpdateVmClusterNetworkDetails.
        :type dns: list[str]

        :param ntp:
            The value to assign to the ntp property of this UpdateVmClusterNetworkDetails.
        :type ntp: list[str]

        :param vm_networks:
            The value to assign to the vm_networks property of this UpdateVmClusterNetworkDetails.
        :type vm_networks: list[oci.database.models.VmNetworkDetails]

        :param dr_scans:
            The value to assign to the dr_scans property of this UpdateVmClusterNetworkDetails.
        :type dr_scans: list[oci.database.models.DrScanDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVmClusterNetworkDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVmClusterNetworkDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'scans': 'list[ScanDetails]',
            'dns': 'list[str]',
            'ntp': 'list[str]',
            'vm_networks': 'list[VmNetworkDetails]',
            'dr_scans': 'list[DrScanDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'scans': 'scans',
            'dns': 'dns',
            'ntp': 'ntp',
            'vm_networks': 'vmNetworks',
            'dr_scans': 'drScans',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._scans = None
        self._dns = None
        self._ntp = None
        self._vm_networks = None
        self._dr_scans = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def scans(self):
        """
        Gets the scans of this UpdateVmClusterNetworkDetails.
        The SCAN details.


        :return: The scans of this UpdateVmClusterNetworkDetails.
        :rtype: list[oci.database.models.ScanDetails]
        """
        return self._scans

    @scans.setter
    def scans(self, scans):
        """
        Sets the scans of this UpdateVmClusterNetworkDetails.
        The SCAN details.


        :param scans: The scans of this UpdateVmClusterNetworkDetails.
        :type: list[oci.database.models.ScanDetails]
        """
        self._scans = scans

    @property
    def dns(self):
        """
        Gets the dns of this UpdateVmClusterNetworkDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :return: The dns of this UpdateVmClusterNetworkDetails.
        :rtype: list[str]
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """
        Sets the dns of this UpdateVmClusterNetworkDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :param dns: The dns of this UpdateVmClusterNetworkDetails.
        :type: list[str]
        """
        self._dns = dns

    @property
    def ntp(self):
        """
        Gets the ntp of this UpdateVmClusterNetworkDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :return: The ntp of this UpdateVmClusterNetworkDetails.
        :rtype: list[str]
        """
        return self._ntp

    @ntp.setter
    def ntp(self, ntp):
        """
        Sets the ntp of this UpdateVmClusterNetworkDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :param ntp: The ntp of this UpdateVmClusterNetworkDetails.
        :type: list[str]
        """
        self._ntp = ntp

    @property
    def vm_networks(self):
        """
        Gets the vm_networks of this UpdateVmClusterNetworkDetails.
        Details of the client and backup networks.


        :return: The vm_networks of this UpdateVmClusterNetworkDetails.
        :rtype: list[oci.database.models.VmNetworkDetails]
        """
        return self._vm_networks

    @vm_networks.setter
    def vm_networks(self, vm_networks):
        """
        Sets the vm_networks of this UpdateVmClusterNetworkDetails.
        Details of the client and backup networks.


        :param vm_networks: The vm_networks of this UpdateVmClusterNetworkDetails.
        :type: list[oci.database.models.VmNetworkDetails]
        """
        self._vm_networks = vm_networks

    @property
    def dr_scans(self):
        """
        Gets the dr_scans of this UpdateVmClusterNetworkDetails.
        The SCAN details for DR network


        :return: The dr_scans of this UpdateVmClusterNetworkDetails.
        :rtype: list[oci.database.models.DrScanDetails]
        """
        return self._dr_scans

    @dr_scans.setter
    def dr_scans(self, dr_scans):
        """
        Sets the dr_scans of this UpdateVmClusterNetworkDetails.
        The SCAN details for DR network


        :param dr_scans: The dr_scans of this UpdateVmClusterNetworkDetails.
        :type: list[oci.database.models.DrScanDetails]
        """
        self._dr_scans = dr_scans

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVmClusterNetworkDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateVmClusterNetworkDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVmClusterNetworkDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateVmClusterNetworkDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVmClusterNetworkDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateVmClusterNetworkDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVmClusterNetworkDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateVmClusterNetworkDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
