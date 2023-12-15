# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityPropagationTrustKeytab(object):
    """
    The keytab stored in the tenancy's Vault. This is required if the identity propagation type is 'SPNEGO'.

    **SCIM++ Properties:**
    - idcsCompositeKey: [secretOcid]
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityPropagationTrustKeytab object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param secret_ocid:
            The value to assign to the secret_ocid property of this IdentityPropagationTrustKeytab.
        :type secret_ocid: str

        :param secret_version:
            The value to assign to the secret_version property of this IdentityPropagationTrustKeytab.
        :type secret_version: int

        """
        self.swagger_types = {
            'secret_ocid': 'str',
            'secret_version': 'int'
        }

        self.attribute_map = {
            'secret_ocid': 'secretOcid',
            'secret_version': 'secretVersion'
        }

        self._secret_ocid = None
        self._secret_version = None

    @property
    def secret_ocid(self):
        """
        **[Required]** Gets the secret_ocid of this IdentityPropagationTrustKeytab.
        The OCID of the secret. The secret content corresponding to the OCID is expected to be in Base64 encoded content type.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The secret_ocid of this IdentityPropagationTrustKeytab.
        :rtype: str
        """
        return self._secret_ocid

    @secret_ocid.setter
    def secret_ocid(self, secret_ocid):
        """
        Sets the secret_ocid of this IdentityPropagationTrustKeytab.
        The OCID of the secret. The secret content corresponding to the OCID is expected to be in Base64 encoded content type.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param secret_ocid: The secret_ocid of this IdentityPropagationTrustKeytab.
        :type: str
        """
        self._secret_ocid = secret_ocid

    @property
    def secret_version(self):
        """
        Gets the secret_version of this IdentityPropagationTrustKeytab.
        The version of the secret. When the version is not specified, then the latest secret version is used during runtime.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The secret_version of this IdentityPropagationTrustKeytab.
        :rtype: int
        """
        return self._secret_version

    @secret_version.setter
    def secret_version(self, secret_version):
        """
        Sets the secret_version of this IdentityPropagationTrustKeytab.
        The version of the secret. When the version is not specified, then the latest secret version is used during runtime.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :param secret_version: The secret_version of this IdentityPropagationTrustKeytab.
        :type: int
        """
        self._secret_version = secret_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other