# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .credential_details import CredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PlainTextCredentialDetails(CredentialDetails):
    """
    Details for plain text credentials.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PlainTextCredentialDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.PlainTextCredentialDetails.credential_type` attribute
        of this class is ``PLAIN_TEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this PlainTextCredentialDetails.
            Allowed values for this property are: "PLAIN_TEXT", "VAULT_SECRET", "KEY_ENCRYPTION"
        :type credential_type: str

        :param value:
            The value to assign to the value property of this PlainTextCredentialDetails.
        :type value: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType',
            'value': 'value'
        }

        self._credential_type = None
        self._value = None
        self._credential_type = 'PLAIN_TEXT'

    @property
    def value(self):
        """
        **[Required]** Gets the value of this PlainTextCredentialDetails.
        The value corresponding to the credential.


        :return: The value of this PlainTextCredentialDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PlainTextCredentialDetails.
        The value corresponding to the credential.


        :param value: The value of this PlainTextCredentialDetails.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
