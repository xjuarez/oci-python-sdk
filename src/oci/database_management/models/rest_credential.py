# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestCredential(object):
    """
    The user credential information.
    """

    #: A constant which can be used with the ssl_trust_store_type property of a RestCredential.
    #: This constant has a value of "JKS"
    SSL_TRUST_STORE_TYPE_JKS = "JKS"

    #: A constant which can be used with the ssl_trust_store_type property of a RestCredential.
    #: This constant has a value of "BCFKS"
    SSL_TRUST_STORE_TYPE_BCFKS = "BCFKS"

    def __init__(self, **kwargs):
        """
        Initializes a new RestCredential object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param username:
            The value to assign to the username property of this RestCredential.
        :type username: str

        :param password:
            The value to assign to the password property of this RestCredential.
        :type password: str

        :param ssl_trust_store_type:
            The value to assign to the ssl_trust_store_type property of this RestCredential.
            Allowed values for this property are: "JKS", "BCFKS"
        :type ssl_trust_store_type: str

        :param ssl_trust_store_location:
            The value to assign to the ssl_trust_store_location property of this RestCredential.
        :type ssl_trust_store_location: str

        :param ssl_trust_store_password:
            The value to assign to the ssl_trust_store_password property of this RestCredential.
        :type ssl_trust_store_password: str

        """
        self.swagger_types = {
            'username': 'str',
            'password': 'str',
            'ssl_trust_store_type': 'str',
            'ssl_trust_store_location': 'str',
            'ssl_trust_store_password': 'str'
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password',
            'ssl_trust_store_type': 'sslTrustStoreType',
            'ssl_trust_store_location': 'sslTrustStoreLocation',
            'ssl_trust_store_password': 'sslTrustStorePassword'
        }

        self._username = None
        self._password = None
        self._ssl_trust_store_type = None
        self._ssl_trust_store_location = None
        self._ssl_trust_store_password = None

    @property
    def username(self):
        """
        **[Required]** Gets the username of this RestCredential.
        The name of the user.


        :return: The username of this RestCredential.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this RestCredential.
        The name of the user.


        :param username: The username of this RestCredential.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this RestCredential.
        The password of the user.


        :return: The password of this RestCredential.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this RestCredential.
        The password of the user.


        :param password: The password of this RestCredential.
        :type: str
        """
        self._password = password

    @property
    def ssl_trust_store_type(self):
        """
        Gets the ssl_trust_store_type of this RestCredential.
        The SSL truststore type.

        Allowed values for this property are: "JKS", "BCFKS"


        :return: The ssl_trust_store_type of this RestCredential.
        :rtype: str
        """
        return self._ssl_trust_store_type

    @ssl_trust_store_type.setter
    def ssl_trust_store_type(self, ssl_trust_store_type):
        """
        Sets the ssl_trust_store_type of this RestCredential.
        The SSL truststore type.


        :param ssl_trust_store_type: The ssl_trust_store_type of this RestCredential.
        :type: str
        """
        allowed_values = ["JKS", "BCFKS"]
        if not value_allowed_none_or_none_sentinel(ssl_trust_store_type, allowed_values):
            raise ValueError(
                "Invalid value for `ssl_trust_store_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ssl_trust_store_type = ssl_trust_store_type

    @property
    def ssl_trust_store_location(self):
        """
        Gets the ssl_trust_store_location of this RestCredential.
        The full path of the SSL truststore location in the agent.


        :return: The ssl_trust_store_location of this RestCredential.
        :rtype: str
        """
        return self._ssl_trust_store_location

    @ssl_trust_store_location.setter
    def ssl_trust_store_location(self, ssl_trust_store_location):
        """
        Sets the ssl_trust_store_location of this RestCredential.
        The full path of the SSL truststore location in the agent.


        :param ssl_trust_store_location: The ssl_trust_store_location of this RestCredential.
        :type: str
        """
        self._ssl_trust_store_location = ssl_trust_store_location

    @property
    def ssl_trust_store_password(self):
        """
        Gets the ssl_trust_store_password of this RestCredential.
        The password of the SSL truststore location in the agent.


        :return: The ssl_trust_store_password of this RestCredential.
        :rtype: str
        """
        return self._ssl_trust_store_password

    @ssl_trust_store_password.setter
    def ssl_trust_store_password(self, ssl_trust_store_password):
        """
        Sets the ssl_trust_store_password of this RestCredential.
        The password of the SSL truststore location in the agent.


        :param ssl_trust_store_password: The ssl_trust_store_password of this RestCredential.
        :type: str
        """
        self._ssl_trust_store_password = ssl_trust_store_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
