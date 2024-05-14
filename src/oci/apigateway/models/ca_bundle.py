# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaBundle(object):
    """
    Reference to the CA bundle that should be used on the gateway
    """

    #: A constant which can be used with the type property of a CaBundle.
    #: This constant has a value of "CA_BUNDLE"
    TYPE_CA_BUNDLE = "CA_BUNDLE"

    #: A constant which can be used with the type property of a CaBundle.
    #: This constant has a value of "CERTIFICATE_AUTHORITY"
    TYPE_CERTIFICATE_AUTHORITY = "CERTIFICATE_AUTHORITY"

    def __init__(self, **kwargs):
        """
        Initializes a new CaBundle object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.CertificatesCaBundle`
        * :class:`~oci.apigateway.models.CertificatesCertificateAuthority`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CaBundle.
            Allowed values for this property are: "CA_BUNDLE", "CERTIFICATE_AUTHORITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'CA_BUNDLE':
            return 'CertificatesCaBundle'

        if type == 'CERTIFICATE_AUTHORITY':
            return 'CertificatesCertificateAuthority'
        else:
            return 'CaBundle'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CaBundle.
        Type of the CA bundle

        Allowed values for this property are: "CA_BUNDLE", "CERTIFICATE_AUTHORITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this CaBundle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CaBundle.
        Type of the CA bundle


        :param type: The type of this CaBundle.
        :type: str
        """
        allowed_values = ["CA_BUNDLE", "CERTIFICATE_AUTHORITY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
