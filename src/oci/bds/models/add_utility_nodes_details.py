# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddUtilityNodesDetails(object):
    """
    The information about added utility nodes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddUtilityNodesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this AddUtilityNodesDetails.
        :type cluster_admin_password: str

        :param number_of_utility_nodes:
            The value to assign to the number_of_utility_nodes property of this AddUtilityNodesDetails.
        :type number_of_utility_nodes: int

        :param shape:
            The value to assign to the shape property of this AddUtilityNodesDetails.
        :type shape: str

        :param block_volume_size_in_gbs:
            The value to assign to the block_volume_size_in_gbs property of this AddUtilityNodesDetails.
        :type block_volume_size_in_gbs: int

        :param shape_config:
            The value to assign to the shape_config property of this AddUtilityNodesDetails.
        :type shape_config: oci.bds.models.ShapeConfigDetails

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'number_of_utility_nodes': 'int',
            'shape': 'str',
            'block_volume_size_in_gbs': 'int',
            'shape_config': 'ShapeConfigDetails'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'number_of_utility_nodes': 'numberOfUtilityNodes',
            'shape': 'shape',
            'block_volume_size_in_gbs': 'blockVolumeSizeInGBs',
            'shape_config': 'shapeConfig'
        }

        self._cluster_admin_password = None
        self._number_of_utility_nodes = None
        self._shape = None
        self._block_volume_size_in_gbs = None
        self._shape_config = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this AddUtilityNodesDetails.
        Base-64 encoded Cluster Admin Password for cluster admin user.


        :return: The cluster_admin_password of this AddUtilityNodesDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this AddUtilityNodesDetails.
        Base-64 encoded Cluster Admin Password for cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this AddUtilityNodesDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def number_of_utility_nodes(self):
        """
        **[Required]** Gets the number_of_utility_nodes of this AddUtilityNodesDetails.
        Number of additional utility nodes for the cluster.


        :return: The number_of_utility_nodes of this AddUtilityNodesDetails.
        :rtype: int
        """
        return self._number_of_utility_nodes

    @number_of_utility_nodes.setter
    def number_of_utility_nodes(self, number_of_utility_nodes):
        """
        Sets the number_of_utility_nodes of this AddUtilityNodesDetails.
        Number of additional utility nodes for the cluster.


        :param number_of_utility_nodes: The number_of_utility_nodes of this AddUtilityNodesDetails.
        :type: int
        """
        self._number_of_utility_nodes = number_of_utility_nodes

    @property
    def shape(self):
        """
        Gets the shape of this AddUtilityNodesDetails.
        Shape of the node. It's a read-only property derived from existing Utility node.


        :return: The shape of this AddUtilityNodesDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this AddUtilityNodesDetails.
        Shape of the node. It's a read-only property derived from existing Utility node.


        :param shape: The shape of this AddUtilityNodesDetails.
        :type: str
        """
        self._shape = shape

    @property
    def block_volume_size_in_gbs(self):
        """
        Gets the block_volume_size_in_gbs of this AddUtilityNodesDetails.
        The size of block volume in GB to be attached to the given node. It's a read-only property.


        :return: The block_volume_size_in_gbs of this AddUtilityNodesDetails.
        :rtype: int
        """
        return self._block_volume_size_in_gbs

    @block_volume_size_in_gbs.setter
    def block_volume_size_in_gbs(self, block_volume_size_in_gbs):
        """
        Sets the block_volume_size_in_gbs of this AddUtilityNodesDetails.
        The size of block volume in GB to be attached to the given node. It's a read-only property.


        :param block_volume_size_in_gbs: The block_volume_size_in_gbs of this AddUtilityNodesDetails.
        :type: int
        """
        self._block_volume_size_in_gbs = block_volume_size_in_gbs

    @property
    def shape_config(self):
        """
        Gets the shape_config of this AddUtilityNodesDetails.

        :return: The shape_config of this AddUtilityNodesDetails.
        :rtype: oci.bds.models.ShapeConfigDetails
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this AddUtilityNodesDetails.

        :param shape_config: The shape_config of this AddUtilityNodesDetails.
        :type: oci.bds.models.ShapeConfigDetails
        """
        self._shape_config = shape_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
