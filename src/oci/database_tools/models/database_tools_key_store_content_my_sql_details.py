# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201005


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsKeyStoreContentMySqlDetails(object):
    """
    The key store content.
    """

    #: A constant which can be used with the value_type property of a DatabaseToolsKeyStoreContentMySqlDetails.
    #: This constant has a value of "SECRETID"
    VALUE_TYPE_SECRETID = "SECRETID"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsKeyStoreContentMySqlDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_tools.models.DatabaseToolsKeyStoreContentSecretIdMySqlDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value_type:
            The value to assign to the value_type property of this DatabaseToolsKeyStoreContentMySqlDetails.
            Allowed values for this property are: "SECRETID"
        :type value_type: str

        """
        self.swagger_types = {
            'value_type': 'str'
        }

        self.attribute_map = {
            'value_type': 'valueType'
        }

        self._value_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['valueType']

        if type == 'SECRETID':
            return 'DatabaseToolsKeyStoreContentSecretIdMySqlDetails'
        else:
            return 'DatabaseToolsKeyStoreContentMySqlDetails'

    @property
    def value_type(self):
        """
        **[Required]** Gets the value_type of this DatabaseToolsKeyStoreContentMySqlDetails.
        The value type of the key store content.

        Allowed values for this property are: "SECRETID"


        :return: The value_type of this DatabaseToolsKeyStoreContentMySqlDetails.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this DatabaseToolsKeyStoreContentMySqlDetails.
        The value type of the key store content.


        :param value_type: The value_type of this DatabaseToolsKeyStoreContentMySqlDetails.
        :type: str
        """
        allowed_values = ["SECRETID"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            raise ValueError(
                f"Invalid value for `value_type`, must be None or one of {allowed_values}"
            )
        self._value_type = value_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
