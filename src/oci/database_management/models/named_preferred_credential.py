# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .preferred_credential import PreferredCredential
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamedPreferredCredential(PreferredCredential):
    """
    The details of the 'NAMED_CREDENTIAL' preferred credential.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NamedPreferredCredential object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.NamedPreferredCredential.type` attribute
        of this class is ``NAMED_CREDENTIAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NamedPreferredCredential.
            Allowed values for this property are: "BASIC", "NAMED_CREDENTIAL"
        :type type: str

        :param credential_name:
            The value to assign to the credential_name property of this NamedPreferredCredential.
        :type credential_name: str

        :param status:
            The value to assign to the status property of this NamedPreferredCredential.
            Allowed values for this property are: "SET", "NOT_SET"
        :type status: str

        :param is_accessible:
            The value to assign to the is_accessible property of this NamedPreferredCredential.
        :type is_accessible: bool

        :param named_credential_id:
            The value to assign to the named_credential_id property of this NamedPreferredCredential.
        :type named_credential_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'credential_name': 'str',
            'status': 'str',
            'is_accessible': 'bool',
            'named_credential_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'credential_name': 'credentialName',
            'status': 'status',
            'is_accessible': 'isAccessible',
            'named_credential_id': 'namedCredentialId'
        }

        self._type = None
        self._credential_name = None
        self._status = None
        self._is_accessible = None
        self._named_credential_id = None
        self._type = 'NAMED_CREDENTIAL'

    @property
    def named_credential_id(self):
        """
        Gets the named_credential_id of this NamedPreferredCredential.
        The `OCID`__ of the Named Credential that contains the database user password metadata.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The named_credential_id of this NamedPreferredCredential.
        :rtype: str
        """
        return self._named_credential_id

    @named_credential_id.setter
    def named_credential_id(self, named_credential_id):
        """
        Sets the named_credential_id of this NamedPreferredCredential.
        The `OCID`__ of the Named Credential that contains the database user password metadata.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param named_credential_id: The named_credential_id of this NamedPreferredCredential.
        :type: str
        """
        self._named_credential_id = named_credential_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
