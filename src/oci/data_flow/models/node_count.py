# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeCount(object):
    """
    An object with a logical shape and count of the number of nodes with that shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeCount object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param logical_shape:
            The value to assign to the logical_shape property of this NodeCount.
        :type logical_shape: str

        :param count:
            The value to assign to the count property of this NodeCount.
        :type count: int

        """
        self.swagger_types = {
            'logical_shape': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'logical_shape': 'logicalShape',
            'count': 'count'
        }

        self._logical_shape = None
        self._count = None

    @property
    def logical_shape(self):
        """
        Gets the logical_shape of this NodeCount.
        The compute shape of the nodes that the count is for.


        :return: The logical_shape of this NodeCount.
        :rtype: str
        """
        return self._logical_shape

    @logical_shape.setter
    def logical_shape(self, logical_shape):
        """
        Sets the logical_shape of this NodeCount.
        The compute shape of the nodes that the count is for.


        :param logical_shape: The logical_shape of this NodeCount.
        :type: str
        """
        self._logical_shape = logical_shape

    @property
    def count(self):
        """
        Gets the count of this NodeCount.
        The node count of this compute shape.


        :return: The count of this NodeCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this NodeCount.
        The node count of this compute shape.


        :param count: The count of this NodeCount.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
