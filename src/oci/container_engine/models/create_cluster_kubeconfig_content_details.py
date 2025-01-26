# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180222


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateClusterKubeconfigContentDetails(object):
    """
    The properties that define a request to create a cluster kubeconfig.
    """

    #: A constant which can be used with the endpoint property of a CreateClusterKubeconfigContentDetails.
    #: This constant has a value of "LEGACY_KUBERNETES"
    ENDPOINT_LEGACY_KUBERNETES = "LEGACY_KUBERNETES"

    #: A constant which can be used with the endpoint property of a CreateClusterKubeconfigContentDetails.
    #: This constant has a value of "PUBLIC_ENDPOINT"
    ENDPOINT_PUBLIC_ENDPOINT = "PUBLIC_ENDPOINT"

    #: A constant which can be used with the endpoint property of a CreateClusterKubeconfigContentDetails.
    #: This constant has a value of "PRIVATE_ENDPOINT"
    ENDPOINT_PRIVATE_ENDPOINT = "PRIVATE_ENDPOINT"

    #: A constant which can be used with the endpoint property of a CreateClusterKubeconfigContentDetails.
    #: This constant has a value of "VCN_HOSTNAME"
    ENDPOINT_VCN_HOSTNAME = "VCN_HOSTNAME"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateClusterKubeconfigContentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param token_version:
            The value to assign to the token_version property of this CreateClusterKubeconfigContentDetails.
        :type token_version: str

        :param expiration:
            The value to assign to the expiration property of this CreateClusterKubeconfigContentDetails.
        :type expiration: int

        :param endpoint:
            The value to assign to the endpoint property of this CreateClusterKubeconfigContentDetails.
            Allowed values for this property are: "LEGACY_KUBERNETES", "PUBLIC_ENDPOINT", "PRIVATE_ENDPOINT", "VCN_HOSTNAME"
        :type endpoint: str

        """
        self.swagger_types = {
            'token_version': 'str',
            'expiration': 'int',
            'endpoint': 'str'
        }

        self.attribute_map = {
            'token_version': 'tokenVersion',
            'expiration': 'expiration',
            'endpoint': 'endpoint'
        }

        self._token_version = None
        self._expiration = None
        self._endpoint = None

    @property
    def token_version(self):
        """
        Gets the token_version of this CreateClusterKubeconfigContentDetails.
        The version of the kubeconfig token. Supported value 2.0.0


        :return: The token_version of this CreateClusterKubeconfigContentDetails.
        :rtype: str
        """
        return self._token_version

    @token_version.setter
    def token_version(self, token_version):
        """
        Sets the token_version of this CreateClusterKubeconfigContentDetails.
        The version of the kubeconfig token. Supported value 2.0.0


        :param token_version: The token_version of this CreateClusterKubeconfigContentDetails.
        :type: str
        """
        self._token_version = token_version

    @property
    def expiration(self):
        """
        Gets the expiration of this CreateClusterKubeconfigContentDetails.
        Deprecated. This field is no longer used.


        :return: The expiration of this CreateClusterKubeconfigContentDetails.
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this CreateClusterKubeconfigContentDetails.
        Deprecated. This field is no longer used.


        :param expiration: The expiration of this CreateClusterKubeconfigContentDetails.
        :type: int
        """
        self._expiration = expiration

    @property
    def endpoint(self):
        """
        Gets the endpoint of this CreateClusterKubeconfigContentDetails.
        The endpoint to target. A cluster may have multiple endpoints exposed but the kubeconfig can only target one at a time.

        Allowed values for this property are: "LEGACY_KUBERNETES", "PUBLIC_ENDPOINT", "PRIVATE_ENDPOINT", "VCN_HOSTNAME"


        :return: The endpoint of this CreateClusterKubeconfigContentDetails.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this CreateClusterKubeconfigContentDetails.
        The endpoint to target. A cluster may have multiple endpoints exposed but the kubeconfig can only target one at a time.


        :param endpoint: The endpoint of this CreateClusterKubeconfigContentDetails.
        :type: str
        """
        allowed_values = ["LEGACY_KUBERNETES", "PUBLIC_ENDPOINT", "PRIVATE_ENDPOINT", "VCN_HOSTNAME"]
        if not value_allowed_none_or_none_sentinel(endpoint, allowed_values):
            raise ValueError(
                f"Invalid value for `endpoint`, must be None or one of {allowed_values}"
            )
        self._endpoint = endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
