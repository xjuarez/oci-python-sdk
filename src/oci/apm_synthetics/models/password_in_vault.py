# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .password import Password
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PasswordInVault(Password):
    """
    Vault secret OCID for password that can be used with monitor Resource Principal.
    Example, ocid1.vaultsecret.oc1.iad.amaaaaaagpihjxqadwyc4kjhpeis2bylhzmp5r2si6mz2h4eujevnmf3zoca.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PasswordInVault object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_synthetics.models.PasswordInVault.password_type` attribute
        of this class is ``VAULT_SECRET_ID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password_type:
            The value to assign to the password_type property of this PasswordInVault.
            Allowed values for this property are: "IN_TEXT", "VAULT_SECRET_ID"
        :type password_type: str

        :param vault_secret_id:
            The value to assign to the vault_secret_id property of this PasswordInVault.
        :type vault_secret_id: str

        """
        self.swagger_types = {
            'password_type': 'str',
            'vault_secret_id': 'str'
        }

        self.attribute_map = {
            'password_type': 'passwordType',
            'vault_secret_id': 'vaultSecretId'
        }

        self._password_type = None
        self._vault_secret_id = None
        self._password_type = 'VAULT_SECRET_ID'

    @property
    def vault_secret_id(self):
        """
        **[Required]** Gets the vault_secret_id of this PasswordInVault.
        Vault secret OCID.


        :return: The vault_secret_id of this PasswordInVault.
        :rtype: str
        """
        return self._vault_secret_id

    @vault_secret_id.setter
    def vault_secret_id(self, vault_secret_id):
        """
        Sets the vault_secret_id of this PasswordInVault.
        Vault secret OCID.


        :param vault_secret_id: The vault_secret_id of this PasswordInVault.
        :type: str
        """
        self._vault_secret_id = vault_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
