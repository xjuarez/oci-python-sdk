# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateUserSecurityTokenDetails(object):
    """
    Request parameters in body for obtaining a user principal session token (UPST) for self.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateUserSecurityTokenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param public_key:
            The value to assign to the public_key property of this GenerateUserSecurityTokenDetails.
        :type public_key: str

        :param session_expiration_in_minutes:
            The value to assign to the session_expiration_in_minutes property of this GenerateUserSecurityTokenDetails.
        :type session_expiration_in_minutes: int

        """
        self.swagger_types = {
            'public_key': 'str',
            'session_expiration_in_minutes': 'int'
        }

        self.attribute_map = {
            'public_key': 'publicKey',
            'session_expiration_in_minutes': 'sessionExpirationInMinutes'
        }

        self._public_key = None
        self._session_expiration_in_minutes = None

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this GenerateUserSecurityTokenDetails.
        The user-owned public key in PEM format that corresponds to the RSA key pair used for signing requests.
        The user also owns the corresponding private key. This public key will be put inside the user
        security token by the auth service after successful validation of the request.


        :return: The public_key of this GenerateUserSecurityTokenDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this GenerateUserSecurityTokenDetails.
        The user-owned public key in PEM format that corresponds to the RSA key pair used for signing requests.
        The user also owns the corresponding private key. This public key will be put inside the user
        security token by the auth service after successful validation of the request.


        :param public_key: The public_key of this GenerateUserSecurityTokenDetails.
        :type: str
        """
        self._public_key = public_key

    @property
    def session_expiration_in_minutes(self):
        """
        Gets the session_expiration_in_minutes of this GenerateUserSecurityTokenDetails.
        User session expiration in minutes to which the requested user principal session token (UPST) is bounded.
        Valid values are from 5 to 60 for all realms.


        :return: The session_expiration_in_minutes of this GenerateUserSecurityTokenDetails.
        :rtype: int
        """
        return self._session_expiration_in_minutes

    @session_expiration_in_minutes.setter
    def session_expiration_in_minutes(self, session_expiration_in_minutes):
        """
        Sets the session_expiration_in_minutes of this GenerateUserSecurityTokenDetails.
        User session expiration in minutes to which the requested user principal session token (UPST) is bounded.
        Valid values are from 5 to 60 for all realms.


        :param session_expiration_in_minutes: The session_expiration_in_minutes of this GenerateUserSecurityTokenDetails.
        :type: int
        """
        self._session_expiration_in_minutes = session_expiration_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
