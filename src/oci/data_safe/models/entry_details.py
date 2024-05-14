# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntryDetails(object):
    """
    Details specific to the security policy entry.
    """

    #: A constant which can be used with the entry_type property of a EntryDetails.
    #: This constant has a value of "FIREWALL_POLICY"
    ENTRY_TYPE_FIREWALL_POLICY = "FIREWALL_POLICY"

    def __init__(self, **kwargs):
        """
        Initializes a new EntryDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.FirewallPolicyEntryDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entry_type:
            The value to assign to the entry_type property of this EntryDetails.
            Allowed values for this property are: "FIREWALL_POLICY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entry_type: str

        """
        self.swagger_types = {
            'entry_type': 'str'
        }

        self.attribute_map = {
            'entry_type': 'entryType'
        }

        self._entry_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entryType']

        if type == 'FIREWALL_POLICY':
            return 'FirewallPolicyEntryDetails'
        else:
            return 'EntryDetails'

    @property
    def entry_type(self):
        """
        **[Required]** Gets the entry_type of this EntryDetails.
        The security policy entry type. Allowed values:
        - FIREWALL_POLICY - The SQL Firewall policy entry type.

        Allowed values for this property are: "FIREWALL_POLICY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entry_type of this EntryDetails.
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """
        Sets the entry_type of this EntryDetails.
        The security policy entry type. Allowed values:
        - FIREWALL_POLICY - The SQL Firewall policy entry type.


        :param entry_type: The entry_type of this EntryDetails.
        :type: str
        """
        allowed_values = ["FIREWALL_POLICY"]
        if not value_allowed_none_or_none_sentinel(entry_type, allowed_values):
            entry_type = 'UNKNOWN_ENUM_VALUE'
        self._entry_type = entry_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
