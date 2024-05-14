# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180222


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNodePoolNodeConfigDetails(object):
    """
    The size and placement configuration of nodes in the node pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNodePoolNodeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param size:
            The value to assign to the size property of this UpdateNodePoolNodeConfigDetails.
        :type size: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateNodePoolNodeConfigDetails.
        :type nsg_ids: list[str]

        :param kms_key_id:
            The value to assign to the kms_key_id property of this UpdateNodePoolNodeConfigDetails.
        :type kms_key_id: str

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this UpdateNodePoolNodeConfigDetails.
        :type is_pv_encryption_in_transit_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNodePoolNodeConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNodePoolNodeConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param placement_configs:
            The value to assign to the placement_configs property of this UpdateNodePoolNodeConfigDetails.
        :type placement_configs: list[oci.container_engine.models.NodePoolPlacementConfigDetails]

        :param node_pool_pod_network_option_details:
            The value to assign to the node_pool_pod_network_option_details property of this UpdateNodePoolNodeConfigDetails.
        :type node_pool_pod_network_option_details: oci.container_engine.models.NodePoolPodNetworkOptionDetails

        """
        self.swagger_types = {
            'size': 'int',
            'nsg_ids': 'list[str]',
            'kms_key_id': 'str',
            'is_pv_encryption_in_transit_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'placement_configs': 'list[NodePoolPlacementConfigDetails]',
            'node_pool_pod_network_option_details': 'NodePoolPodNetworkOptionDetails'
        }

        self.attribute_map = {
            'size': 'size',
            'nsg_ids': 'nsgIds',
            'kms_key_id': 'kmsKeyId',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'placement_configs': 'placementConfigs',
            'node_pool_pod_network_option_details': 'nodePoolPodNetworkOptionDetails'
        }

        self._size = None
        self._nsg_ids = None
        self._kms_key_id = None
        self._is_pv_encryption_in_transit_enabled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._placement_configs = None
        self._node_pool_pod_network_option_details = None

    @property
    def size(self):
        """
        Gets the size of this UpdateNodePoolNodeConfigDetails.
        The number of nodes in the node pool.


        :return: The size of this UpdateNodePoolNodeConfigDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this UpdateNodePoolNodeConfigDetails.
        The number of nodes in the node pool.


        :param size: The size of this UpdateNodePoolNodeConfigDetails.
        :type: int
        """
        self._size = size

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateNodePoolNodeConfigDetails.
        The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this UpdateNodePoolNodeConfigDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateNodePoolNodeConfigDetails.
        The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this UpdateNodePoolNodeConfigDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this UpdateNodePoolNodeConfigDetails.
        The OCID of the Key Management Service key assigned to the boot volume.


        :return: The kms_key_id of this UpdateNodePoolNodeConfigDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this UpdateNodePoolNodeConfigDetails.
        The OCID of the Key Management Service key assigned to the boot volume.


        :param kms_key_id: The kms_key_id of this UpdateNodePoolNodeConfigDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def is_pv_encryption_in_transit_enabled(self):
        """
        Gets the is_pv_encryption_in_transit_enabled of this UpdateNodePoolNodeConfigDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.


        :return: The is_pv_encryption_in_transit_enabled of this UpdateNodePoolNodeConfigDetails.
        :rtype: bool
        """
        return self._is_pv_encryption_in_transit_enabled

    @is_pv_encryption_in_transit_enabled.setter
    def is_pv_encryption_in_transit_enabled(self, is_pv_encryption_in_transit_enabled):
        """
        Sets the is_pv_encryption_in_transit_enabled of this UpdateNodePoolNodeConfigDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.


        :param is_pv_encryption_in_transit_enabled: The is_pv_encryption_in_transit_enabled of this UpdateNodePoolNodeConfigDetails.
        :type: bool
        """
        self._is_pv_encryption_in_transit_enabled = is_pv_encryption_in_transit_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNodePoolNodeConfigDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateNodePoolNodeConfigDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNodePoolNodeConfigDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateNodePoolNodeConfigDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNodePoolNodeConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateNodePoolNodeConfigDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNodePoolNodeConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateNodePoolNodeConfigDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def placement_configs(self):
        """
        Gets the placement_configs of this UpdateNodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :return: The placement_configs of this UpdateNodePoolNodeConfigDetails.
        :rtype: list[oci.container_engine.models.NodePoolPlacementConfigDetails]
        """
        return self._placement_configs

    @placement_configs.setter
    def placement_configs(self, placement_configs):
        """
        Sets the placement_configs of this UpdateNodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :param placement_configs: The placement_configs of this UpdateNodePoolNodeConfigDetails.
        :type: list[oci.container_engine.models.NodePoolPlacementConfigDetails]
        """
        self._placement_configs = placement_configs

    @property
    def node_pool_pod_network_option_details(self):
        """
        Gets the node_pool_pod_network_option_details of this UpdateNodePoolNodeConfigDetails.
        The CNI related configuration of pods in the node pool.


        :return: The node_pool_pod_network_option_details of this UpdateNodePoolNodeConfigDetails.
        :rtype: oci.container_engine.models.NodePoolPodNetworkOptionDetails
        """
        return self._node_pool_pod_network_option_details

    @node_pool_pod_network_option_details.setter
    def node_pool_pod_network_option_details(self, node_pool_pod_network_option_details):
        """
        Sets the node_pool_pod_network_option_details of this UpdateNodePoolNodeConfigDetails.
        The CNI related configuration of pods in the node pool.


        :param node_pool_pod_network_option_details: The node_pool_pod_network_option_details of this UpdateNodePoolNodeConfigDetails.
        :type: oci.container_engine.models.NodePoolPodNetworkOptionDetails
        """
        self._node_pool_pod_network_option_details = node_pool_pod_network_option_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
