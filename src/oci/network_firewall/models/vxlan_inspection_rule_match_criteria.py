# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VxlanInspectionRuleMatchCriteria(object):
    """
    Criteria to evaluate against incoming network traffic.
    A match occurs when at least one item in the array associated with each specified property corresponds with the relevant aspect of the traffic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VxlanInspectionRuleMatchCriteria object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_address:
            The value to assign to the source_address property of this VxlanInspectionRuleMatchCriteria.
        :type source_address: list[str]

        :param destination_address:
            The value to assign to the destination_address property of this VxlanInspectionRuleMatchCriteria.
        :type destination_address: list[str]

        """
        self.swagger_types = {
            'source_address': 'list[str]',
            'destination_address': 'list[str]'
        }

        self.attribute_map = {
            'source_address': 'sourceAddress',
            'destination_address': 'destinationAddress'
        }

        self._source_address = None
        self._destination_address = None

    @property
    def source_address(self):
        """
        Gets the source_address of this VxlanInspectionRuleMatchCriteria.
        An array of address list names to be evaluated against the traffic source address.


        :return: The source_address of this VxlanInspectionRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """
        Sets the source_address of this VxlanInspectionRuleMatchCriteria.
        An array of address list names to be evaluated against the traffic source address.


        :param source_address: The source_address of this VxlanInspectionRuleMatchCriteria.
        :type: list[str]
        """
        self._source_address = source_address

    @property
    def destination_address(self):
        """
        Gets the destination_address of this VxlanInspectionRuleMatchCriteria.
        An array of address list names to be evaluated against the traffic destination address.


        :return: The destination_address of this VxlanInspectionRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """
        Sets the destination_address of this VxlanInspectionRuleMatchCriteria.
        An array of address list names to be evaluated against the traffic destination address.


        :param destination_address: The destination_address of this VxlanInspectionRuleMatchCriteria.
        :type: list[str]
        """
        self._destination_address = destination_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
