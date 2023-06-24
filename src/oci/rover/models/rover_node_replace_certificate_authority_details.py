# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNodeReplaceCertificateAuthorityDetails(object):
    """
    The information required to replace a certificate authority details for a roverNode.
    """

    #: A constant which can be used with the cert_key_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "RSA2048"
    CERT_KEY_ALGORITHM_RSA2048 = "RSA2048"

    #: A constant which can be used with the cert_key_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "RSA4096"
    CERT_KEY_ALGORITHM_RSA4096 = "RSA4096"

    #: A constant which can be used with the cert_key_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "ECDSA_P256"
    CERT_KEY_ALGORITHM_ECDSA_P256 = "ECDSA_P256"

    #: A constant which can be used with the cert_key_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "ECDSA_P384"
    CERT_KEY_ALGORITHM_ECDSA_P384 = "ECDSA_P384"

    #: A constant which can be used with the cert_signature_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "SHA256_WITH_RSA"
    CERT_SIGNATURE_ALGORITHM_SHA256_WITH_RSA = "SHA256_WITH_RSA"

    #: A constant which can be used with the cert_signature_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "SHA384_WITH_RSA"
    CERT_SIGNATURE_ALGORITHM_SHA384_WITH_RSA = "SHA384_WITH_RSA"

    #: A constant which can be used with the cert_signature_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "SHA512_WITH_RSA"
    CERT_SIGNATURE_ALGORITHM_SHA512_WITH_RSA = "SHA512_WITH_RSA"

    #: A constant which can be used with the cert_signature_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "SHA256_WITH_ECDSA"
    CERT_SIGNATURE_ALGORITHM_SHA256_WITH_ECDSA = "SHA256_WITH_ECDSA"

    #: A constant which can be used with the cert_signature_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "SHA384_WITH_ECDSA"
    CERT_SIGNATURE_ALGORITHM_SHA384_WITH_ECDSA = "SHA384_WITH_ECDSA"

    #: A constant which can be used with the cert_signature_algorithm property of a RoverNodeReplaceCertificateAuthorityDetails.
    #: This constant has a value of "SHA512_WITH_ECDSA"
    CERT_SIGNATURE_ALGORITHM_SHA512_WITH_ECDSA = "SHA512_WITH_ECDSA"

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNodeReplaceCertificateAuthorityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_authority_id:
            The value to assign to the certificate_authority_id property of this RoverNodeReplaceCertificateAuthorityDetails.
        :type certificate_authority_id: str

        :param cert_key_algorithm:
            The value to assign to the cert_key_algorithm property of this RoverNodeReplaceCertificateAuthorityDetails.
            Allowed values for this property are: "RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"
        :type cert_key_algorithm: str

        :param cert_signature_algorithm:
            The value to assign to the cert_signature_algorithm property of this RoverNodeReplaceCertificateAuthorityDetails.
            Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"
        :type cert_signature_algorithm: str

        """
        self.swagger_types = {
            'certificate_authority_id': 'str',
            'cert_key_algorithm': 'str',
            'cert_signature_algorithm': 'str'
        }

        self.attribute_map = {
            'certificate_authority_id': 'certificateAuthorityId',
            'cert_key_algorithm': 'certKeyAlgorithm',
            'cert_signature_algorithm': 'certSignatureAlgorithm'
        }

        self._certificate_authority_id = None
        self._cert_key_algorithm = None
        self._cert_signature_algorithm = None

    @property
    def certificate_authority_id(self):
        """
        **[Required]** Gets the certificate_authority_id of this RoverNodeReplaceCertificateAuthorityDetails.
        The certificate authority id.


        :return: The certificate_authority_id of this RoverNodeReplaceCertificateAuthorityDetails.
        :rtype: str
        """
        return self._certificate_authority_id

    @certificate_authority_id.setter
    def certificate_authority_id(self, certificate_authority_id):
        """
        Sets the certificate_authority_id of this RoverNodeReplaceCertificateAuthorityDetails.
        The certificate authority id.


        :param certificate_authority_id: The certificate_authority_id of this RoverNodeReplaceCertificateAuthorityDetails.
        :type: str
        """
        self._certificate_authority_id = certificate_authority_id

    @property
    def cert_key_algorithm(self):
        """
        Gets the cert_key_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        key algorithm for issuing leaf certificate.

        Allowed values for this property are: "RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"


        :return: The cert_key_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        :rtype: str
        """
        return self._cert_key_algorithm

    @cert_key_algorithm.setter
    def cert_key_algorithm(self, cert_key_algorithm):
        """
        Sets the cert_key_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        key algorithm for issuing leaf certificate.


        :param cert_key_algorithm: The cert_key_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        :type: str
        """
        allowed_values = ["RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"]
        if not value_allowed_none_or_none_sentinel(cert_key_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `cert_key_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._cert_key_algorithm = cert_key_algorithm

    @property
    def cert_signature_algorithm(self):
        """
        Gets the cert_signature_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        signature algorithm for issuing leaf certificate.

        Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"


        :return: The cert_signature_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        :rtype: str
        """
        return self._cert_signature_algorithm

    @cert_signature_algorithm.setter
    def cert_signature_algorithm(self, cert_signature_algorithm):
        """
        Sets the cert_signature_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        signature algorithm for issuing leaf certificate.


        :param cert_signature_algorithm: The cert_signature_algorithm of this RoverNodeReplaceCertificateAuthorityDetails.
        :type: str
        """
        allowed_values = ["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]
        if not value_allowed_none_or_none_sentinel(cert_signature_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `cert_signature_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._cert_signature_algorithm = cert_signature_algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
