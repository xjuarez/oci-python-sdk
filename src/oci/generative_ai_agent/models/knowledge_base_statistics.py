# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KnowledgeBaseStatistics(object):
    """
    Statistics for Default Knowledge Base.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KnowledgeBaseStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this KnowledgeBaseStatistics.
        :type size_in_bytes: int

        """
        self.swagger_types = {
            'size_in_bytes': 'int'
        }

        self.attribute_map = {
            'size_in_bytes': 'sizeInBytes'
        }

        self._size_in_bytes = None

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this KnowledgeBaseStatistics.
        Knowledge Base size in bytes.


        :return: The size_in_bytes of this KnowledgeBaseStatistics.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this KnowledgeBaseStatistics.
        Knowledge Base size in bytes.


        :param size_in_bytes: The size_in_bytes of this KnowledgeBaseStatistics.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
