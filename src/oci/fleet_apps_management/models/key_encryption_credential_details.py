# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .credential_details import CredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyEncryptionCredentialDetails(CredentialDetails):
    """
    Details for Credentials using key encryption.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyEncryptionCredentialDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.KeyEncryptionCredentialDetails.credential_type` attribute
        of this class is ``KEY_ENCRYPTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this KeyEncryptionCredentialDetails.
            Allowed values for this property are: "PLAIN_TEXT", "VAULT_SECRET", "KEY_ENCRYPTION"
        :type credential_type: str

        :param value:
            The value to assign to the value property of this KeyEncryptionCredentialDetails.
        :type value: str

        :param key_id:
            The value to assign to the key_id property of this KeyEncryptionCredentialDetails.
        :type key_id: str

        :param key_version:
            The value to assign to the key_version property of this KeyEncryptionCredentialDetails.
        :type key_version: str

        :param vault_id:
            The value to assign to the vault_id property of this KeyEncryptionCredentialDetails.
        :type vault_id: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'value': 'str',
            'key_id': 'str',
            'key_version': 'str',
            'vault_id': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType',
            'value': 'value',
            'key_id': 'keyId',
            'key_version': 'keyVersion',
            'vault_id': 'vaultId'
        }

        self._credential_type = None
        self._value = None
        self._key_id = None
        self._key_version = None
        self._vault_id = None
        self._credential_type = 'KEY_ENCRYPTION'

    @property
    def value(self):
        """
        **[Required]** Gets the value of this KeyEncryptionCredentialDetails.
        The value corresponding to the credential


        :return: The value of this KeyEncryptionCredentialDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this KeyEncryptionCredentialDetails.
        The value corresponding to the credential


        :param value: The value of this KeyEncryptionCredentialDetails.
        :type: str
        """
        self._value = value

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this KeyEncryptionCredentialDetails.
        OCID for the Vault Key that will be used to encrypt/decrypt the value given.


        :return: The key_id of this KeyEncryptionCredentialDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this KeyEncryptionCredentialDetails.
        OCID for the Vault Key that will be used to encrypt/decrypt the value given.


        :param key_id: The key_id of this KeyEncryptionCredentialDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_version(self):
        """
        Gets the key_version of this KeyEncryptionCredentialDetails.
        The Vault Key version.


        :return: The key_version of this KeyEncryptionCredentialDetails.
        :rtype: str
        """
        return self._key_version

    @key_version.setter
    def key_version(self, key_version):
        """
        Sets the key_version of this KeyEncryptionCredentialDetails.
        The Vault Key version.


        :param key_version: The key_version of this KeyEncryptionCredentialDetails.
        :type: str
        """
        self._key_version = key_version

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this KeyEncryptionCredentialDetails.
        OCID for the Vault that will be used to fetch key to encrypt/decrypt the value given.


        :return: The vault_id of this KeyEncryptionCredentialDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this KeyEncryptionCredentialDetails.
        OCID for the Vault that will be used to fetch key to encrypt/decrypt the value given.


        :param vault_id: The vault_id of this KeyEncryptionCredentialDetails.
        :type: str
        """
        self._vault_id = vault_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
