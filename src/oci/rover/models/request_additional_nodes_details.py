# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestAdditionalNodesDetails(object):
    """
    Object for request additional nodes for a roverCluster
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestAdditionalNodesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param number_of_additional_nodes:
            The value to assign to the number_of_additional_nodes property of this RequestAdditionalNodesDetails.
        :type number_of_additional_nodes: int

        """
        self.swagger_types = {
            'number_of_additional_nodes': 'int'
        }

        self.attribute_map = {
            'number_of_additional_nodes': 'numberOfAdditionalNodes'
        }

        self._number_of_additional_nodes = None

    @property
    def number_of_additional_nodes(self):
        """
        **[Required]** Gets the number_of_additional_nodes of this RequestAdditionalNodesDetails.
        Number of additional nodes to be requested for a roverCluster.


        :return: The number_of_additional_nodes of this RequestAdditionalNodesDetails.
        :rtype: int
        """
        return self._number_of_additional_nodes

    @number_of_additional_nodes.setter
    def number_of_additional_nodes(self, number_of_additional_nodes):
        """
        Sets the number_of_additional_nodes of this RequestAdditionalNodesDetails.
        Number of additional nodes to be requested for a roverCluster.


        :param number_of_additional_nodes: The number_of_additional_nodes of this RequestAdditionalNodesDetails.
        :type: int
        """
        self._number_of_additional_nodes = number_of_additional_nodes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
