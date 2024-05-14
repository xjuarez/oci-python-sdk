# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostSpecificCertificateDetails(object):
    """
    Host specific certificate details
    """

    #: A constant which can be used with the certificate_type property of a HostSpecificCertificateDetails.
    #: This constant has a value of "CUSTOM_SIGNED"
    CERTIFICATE_TYPE_CUSTOM_SIGNED = "CUSTOM_SIGNED"

    #: A constant which can be used with the certificate_type property of a HostSpecificCertificateDetails.
    #: This constant has a value of "SELF_SIGNED"
    CERTIFICATE_TYPE_SELF_SIGNED = "SELF_SIGNED"

    def __init__(self, **kwargs):
        """
        Initializes a new HostSpecificCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_name:
            The value to assign to the host_name property of this HostSpecificCertificateDetails.
        :type host_name: str

        :param certificate_type:
            The value to assign to the certificate_type property of this HostSpecificCertificateDetails.
            Allowed values for this property are: "CUSTOM_SIGNED", "SELF_SIGNED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type certificate_type: str

        :param time_expiry:
            The value to assign to the time_expiry property of this HostSpecificCertificateDetails.
        :type time_expiry: datetime

        """
        self.swagger_types = {
            'host_name': 'str',
            'certificate_type': 'str',
            'time_expiry': 'datetime'
        }

        self.attribute_map = {
            'host_name': 'hostName',
            'certificate_type': 'certificateType',
            'time_expiry': 'timeExpiry'
        }

        self._host_name = None
        self._certificate_type = None
        self._time_expiry = None

    @property
    def host_name(self):
        """
        Gets the host_name of this HostSpecificCertificateDetails.
        Name of the host.


        :return: The host_name of this HostSpecificCertificateDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this HostSpecificCertificateDetails.
        Name of the host.


        :param host_name: The host_name of this HostSpecificCertificateDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def certificate_type(self):
        """
        Gets the certificate_type of this HostSpecificCertificateDetails.
        Type of certificate self signed or CA signed

        Allowed values for this property are: "CUSTOM_SIGNED", "SELF_SIGNED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The certificate_type of this HostSpecificCertificateDetails.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """
        Sets the certificate_type of this HostSpecificCertificateDetails.
        Type of certificate self signed or CA signed


        :param certificate_type: The certificate_type of this HostSpecificCertificateDetails.
        :type: str
        """
        allowed_values = ["CUSTOM_SIGNED", "SELF_SIGNED"]
        if not value_allowed_none_or_none_sentinel(certificate_type, allowed_values):
            certificate_type = 'UNKNOWN_ENUM_VALUE'
        self._certificate_type = certificate_type

    @property
    def time_expiry(self):
        """
        Gets the time_expiry of this HostSpecificCertificateDetails.
        The time the certificate expires, shown as an RFC 3339 formatted datetime string.


        :return: The time_expiry of this HostSpecificCertificateDetails.
        :rtype: datetime
        """
        return self._time_expiry

    @time_expiry.setter
    def time_expiry(self, time_expiry):
        """
        Sets the time_expiry of this HostSpecificCertificateDetails.
        The time the certificate expires, shown as an RFC 3339 formatted datetime string.


        :param time_expiry: The time_expiry of this HostSpecificCertificateDetails.
        :type: datetime
        """
        self._time_expiry = time_expiry

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
