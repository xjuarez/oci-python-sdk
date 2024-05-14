# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DecryptionProfile(object):
    """
    Decryption Profile used on the firewall policy rules.
    """

    #: A constant which can be used with the type property of a DecryptionProfile.
    #: This constant has a value of "SSL_INBOUND_INSPECTION"
    TYPE_SSL_INBOUND_INSPECTION = "SSL_INBOUND_INSPECTION"

    #: A constant which can be used with the type property of a DecryptionProfile.
    #: This constant has a value of "SSL_FORWARD_PROXY"
    TYPE_SSL_FORWARD_PROXY = "SSL_FORWARD_PROXY"

    def __init__(self, **kwargs):
        """
        Initializes a new DecryptionProfile object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.network_firewall.models.SslInboundInspectionProfile`
        * :class:`~oci.network_firewall.models.SslForwardProxyProfile`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DecryptionProfile.
            Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param name:
            The value to assign to the name property of this DecryptionProfile.
        :type name: str

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this DecryptionProfile.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'parent_resource_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'parent_resource_id': 'parentResourceId'
        }

        self._type = None
        self._name = None
        self._parent_resource_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'SSL_INBOUND_INSPECTION':
            return 'SslInboundInspectionProfile'

        if type == 'SSL_FORWARD_PROXY':
            return 'SslForwardProxyProfile'
        else:
            return 'DecryptionProfile'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DecryptionProfile.
        Describes the type of Decryption Profile SslForwardProxy or SslInboundInspection.

        Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DecryptionProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DecryptionProfile.
        Describes the type of Decryption Profile SslForwardProxy or SslInboundInspection.


        :param type: The type of this DecryptionProfile.
        :type: str
        """
        allowed_values = ["SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DecryptionProfile.
        Unique Name of the decryption profile.


        :return: The name of this DecryptionProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DecryptionProfile.
        Unique Name of the decryption profile.


        :param name: The name of this DecryptionProfile.
        :type: str
        """
        self._name = name

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this DecryptionProfile.
        OCID of the Network Firewall Policy this decryption profile belongs to.


        :return: The parent_resource_id of this DecryptionProfile.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this DecryptionProfile.
        OCID of the Network Firewall Policy this decryption profile belongs to.


        :param parent_resource_id: The parent_resource_id of this DecryptionProfile.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
