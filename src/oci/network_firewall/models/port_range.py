# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PortRange(object):
    """
    A Port Range which can be used for the running service. It uses port information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PortRange object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param minimum_port:
            The value to assign to the minimum_port property of this PortRange.
        :type minimum_port: int

        :param maximum_port:
            The value to assign to the maximum_port property of this PortRange.
        :type maximum_port: int

        """
        self.swagger_types = {
            'minimum_port': 'int',
            'maximum_port': 'int'
        }

        self.attribute_map = {
            'minimum_port': 'minimumPort',
            'maximum_port': 'maximumPort'
        }

        self._minimum_port = None
        self._maximum_port = None

    @property
    def minimum_port(self):
        """
        **[Required]** Gets the minimum_port of this PortRange.
        The minimum port in the range (inclusive), or the sole port of a single-port range.


        :return: The minimum_port of this PortRange.
        :rtype: int
        """
        return self._minimum_port

    @minimum_port.setter
    def minimum_port(self, minimum_port):
        """
        Sets the minimum_port of this PortRange.
        The minimum port in the range (inclusive), or the sole port of a single-port range.


        :param minimum_port: The minimum_port of this PortRange.
        :type: int
        """
        self._minimum_port = minimum_port

    @property
    def maximum_port(self):
        """
        Gets the maximum_port of this PortRange.
        The maximum port in the range (inclusive), which may be absent for a single-port range.


        :return: The maximum_port of this PortRange.
        :rtype: int
        """
        return self._maximum_port

    @maximum_port.setter
    def maximum_port(self, maximum_port):
        """
        Sets the maximum_port of this PortRange.
        The maximum port in the range (inclusive), which may be absent for a single-port range.


        :param maximum_port: The maximum_port of this PortRange.
        :type: int
        """
        self._maximum_port = maximum_port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
