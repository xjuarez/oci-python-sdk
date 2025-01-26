# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220615


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessPolicyTarget(object):
    """
    Target of the access policy. This can either be the source or the destination of the traffic.
    """

    #: A constant which can be used with the type property of a AccessPolicyTarget.
    #: This constant has a value of "ALL_VIRTUAL_SERVICES"
    TYPE_ALL_VIRTUAL_SERVICES = "ALL_VIRTUAL_SERVICES"

    #: A constant which can be used with the type property of a AccessPolicyTarget.
    #: This constant has a value of "VIRTUAL_SERVICE"
    TYPE_VIRTUAL_SERVICE = "VIRTUAL_SERVICE"

    #: A constant which can be used with the type property of a AccessPolicyTarget.
    #: This constant has a value of "EXTERNAL_SERVICE"
    TYPE_EXTERNAL_SERVICE = "EXTERNAL_SERVICE"

    #: A constant which can be used with the type property of a AccessPolicyTarget.
    #: This constant has a value of "INGRESS_GATEWAY"
    TYPE_INGRESS_GATEWAY = "INGRESS_GATEWAY"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessPolicyTarget object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_mesh.models.VirtualServiceAccessPolicyTarget`
        * :class:`~oci.service_mesh.models.AllVirtualServicesAccessPolicyTarget`
        * :class:`~oci.service_mesh.models.ExternalServiceAccessPolicyTarget`
        * :class:`~oci.service_mesh.models.IngressGatewayAccessPolicyTarget`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AccessPolicyTarget.
            Allowed values for this property are: "ALL_VIRTUAL_SERVICES", "VIRTUAL_SERVICE", "EXTERNAL_SERVICE", "INGRESS_GATEWAY", 'UNKNOWN_ENUM_VALUE'.
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

        if type == 'VIRTUAL_SERVICE':
            return 'VirtualServiceAccessPolicyTarget'

        if type == 'ALL_VIRTUAL_SERVICES':
            return 'AllVirtualServicesAccessPolicyTarget'

        if type == 'EXTERNAL_SERVICE':
            return 'ExternalServiceAccessPolicyTarget'

        if type == 'INGRESS_GATEWAY':
            return 'IngressGatewayAccessPolicyTarget'
        else:
            return 'AccessPolicyTarget'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AccessPolicyTarget.
        Traffic type of the target.

        Allowed values for this property are: "ALL_VIRTUAL_SERVICES", "VIRTUAL_SERVICE", "EXTERNAL_SERVICE", "INGRESS_GATEWAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AccessPolicyTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AccessPolicyTarget.
        Traffic type of the target.


        :param type: The type of this AccessPolicyTarget.
        :type: str
        """
        allowed_values = ["ALL_VIRTUAL_SERVICES", "VIRTUAL_SERVICE", "EXTERNAL_SERVICE", "INGRESS_GATEWAY"]
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
