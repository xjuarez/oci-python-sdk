# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeAttachment(object):
    """
    Describes volume attachment details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_delete_on_termination:
            The value to assign to the is_delete_on_termination property of this VolumeAttachment.
        :type is_delete_on_termination: bool

        :param device:
            The value to assign to the device property of this VolumeAttachment.
        :type device: str

        :param instance_key:
            The value to assign to the instance_key property of this VolumeAttachment.
        :type instance_key: str

        :param status:
            The value to assign to the status property of this VolumeAttachment.
        :type status: str

        :param volume_key:
            The value to assign to the volume_key property of this VolumeAttachment.
        :type volume_key: str

        """
        self.swagger_types = {
            'is_delete_on_termination': 'bool',
            'device': 'str',
            'instance_key': 'str',
            'status': 'str',
            'volume_key': 'str'
        }

        self.attribute_map = {
            'is_delete_on_termination': 'isDeleteOnTermination',
            'device': 'device',
            'instance_key': 'instanceKey',
            'status': 'status',
            'volume_key': 'volumeKey'
        }

        self._is_delete_on_termination = None
        self._device = None
        self._instance_key = None
        self._status = None
        self._volume_key = None

    @property
    def is_delete_on_termination(self):
        """
        Gets the is_delete_on_termination of this VolumeAttachment.
        Indicates whether the EBS volume is deleted on instance termination.


        :return: The is_delete_on_termination of this VolumeAttachment.
        :rtype: bool
        """
        return self._is_delete_on_termination

    @is_delete_on_termination.setter
    def is_delete_on_termination(self, is_delete_on_termination):
        """
        Sets the is_delete_on_termination of this VolumeAttachment.
        Indicates whether the EBS volume is deleted on instance termination.


        :param is_delete_on_termination: The is_delete_on_termination of this VolumeAttachment.
        :type: bool
        """
        self._is_delete_on_termination = is_delete_on_termination

    @property
    def device(self):
        """
        Gets the device of this VolumeAttachment.
        The device name.


        :return: The device of this VolumeAttachment.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this VolumeAttachment.
        The device name.


        :param device: The device of this VolumeAttachment.
        :type: str
        """
        self._device = device

    @property
    def instance_key(self):
        """
        Gets the instance_key of this VolumeAttachment.
        The ID of the instance.


        :return: The instance_key of this VolumeAttachment.
        :rtype: str
        """
        return self._instance_key

    @instance_key.setter
    def instance_key(self, instance_key):
        """
        Sets the instance_key of this VolumeAttachment.
        The ID of the instance.


        :param instance_key: The instance_key of this VolumeAttachment.
        :type: str
        """
        self._instance_key = instance_key

    @property
    def status(self):
        """
        Gets the status of this VolumeAttachment.
        The attachment state of the volume.


        :return: The status of this VolumeAttachment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VolumeAttachment.
        The attachment state of the volume.


        :param status: The status of this VolumeAttachment.
        :type: str
        """
        self._status = status

    @property
    def volume_key(self):
        """
        Gets the volume_key of this VolumeAttachment.
        The ID of the volume.


        :return: The volume_key of this VolumeAttachment.
        :rtype: str
        """
        return self._volume_key

    @volume_key.setter
    def volume_key(self, volume_key):
        """
        Sets the volume_key of this VolumeAttachment.
        The ID of the volume.


        :param volume_key: The volume_key of this VolumeAttachment.
        :type: str
        """
        self._volume_key = volume_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
