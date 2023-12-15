# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MessageMetadata(object):
    """
    Object that represents metadata for message.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MessageMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param channel_id:
            The value to assign to the channel_id property of this MessageMetadata.
        :type channel_id: str

        :param custom_properties:
            The value to assign to the custom_properties property of this MessageMetadata.
        :type custom_properties: dict(str, str)

        """
        self.swagger_types = {
            'channel_id': 'str',
            'custom_properties': 'dict(str, str)'
        }

        self.attribute_map = {
            'channel_id': 'channelId',
            'custom_properties': 'customProperties'
        }

        self._channel_id = None
        self._custom_properties = None

    @property
    def channel_id(self):
        """
        **[Required]** Gets the channel_id of this MessageMetadata.
        The channel ID which specifies the channel to publish or retrieve messages.


        :return: The channel_id of this MessageMetadata.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """
        Sets the channel_id of this MessageMetadata.
        The channel ID which specifies the channel to publish or retrieve messages.


        :param channel_id: The channel_id of this MessageMetadata.
        :type: str
        """
        self._channel_id = channel_id

    @property
    def custom_properties(self):
        """
        Gets the custom_properties of this MessageMetadata.
        Additional message properties


        :return: The custom_properties of this MessageMetadata.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """
        Sets the custom_properties of this MessageMetadata.
        Additional message properties


        :param custom_properties: The custom_properties of this MessageMetadata.
        :type: dict(str, str)
        """
        self._custom_properties = custom_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
