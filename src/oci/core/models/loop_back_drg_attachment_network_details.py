# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .drg_attachment_network_details import DrgAttachmentNetworkDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoopBackDrgAttachmentNetworkDetails(DrgAttachmentNetworkDetails):
    """
    Specifies the loopback attachment on the DRG. A loopback attachment can be used to terminate a virtual circuit that is carrying an IPSec tunnel, routing traffic directly to the IPSec tunnel attachment where the tunnel can terminate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoopBackDrgAttachmentNetworkDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.LoopBackDrgAttachmentNetworkDetails.type` attribute
        of this class is ``LOOPBACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LoopBackDrgAttachmentNetworkDetails.
            Allowed values for this property are: "VCN", "IPSEC_TUNNEL", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION"
        :type type: str

        :param id:
            The value to assign to the id property of this LoopBackDrgAttachmentNetworkDetails.
        :type id: str

        :param ids:
            The value to assign to the ids property of this LoopBackDrgAttachmentNetworkDetails.
        :type ids: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'ids': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'ids': 'ids'
        }

        self._type = None
        self._id = None
        self._ids = None
        self._type = 'LOOPBACK'

    @property
    def ids(self):
        """
        Gets the ids of this LoopBackDrgAttachmentNetworkDetails.
        The `OCID`__ of the target IPSec tunnel attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The ids of this LoopBackDrgAttachmentNetworkDetails.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """
        Sets the ids of this LoopBackDrgAttachmentNetworkDetails.
        The `OCID`__ of the target IPSec tunnel attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param ids: The ids of this LoopBackDrgAttachmentNetworkDetails.
        :type: list[str]
        """
        self._ids = ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
