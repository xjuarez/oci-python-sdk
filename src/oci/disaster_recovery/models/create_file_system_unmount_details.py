# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFileSystemUnmountDetails(object):
    """
    The details for creating a file system unmount.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFileSystemUnmountDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mount_target_id:
            The value to assign to the mount_target_id property of this CreateFileSystemUnmountDetails.
        :type mount_target_id: str

        """
        self.swagger_types = {
            'mount_target_id': 'str'
        }

        self.attribute_map = {
            'mount_target_id': 'mountTargetId'
        }

        self._mount_target_id = None

    @property
    def mount_target_id(self):
        """
        Gets the mount_target_id of this CreateFileSystemUnmountDetails.
        The OCID of the mount target.

        Example: `ocid1.mounttarget.oc1..uniqueID`


        :return: The mount_target_id of this CreateFileSystemUnmountDetails.
        :rtype: str
        """
        return self._mount_target_id

    @mount_target_id.setter
    def mount_target_id(self, mount_target_id):
        """
        Sets the mount_target_id of this CreateFileSystemUnmountDetails.
        The OCID of the mount target.

        Example: `ocid1.mounttarget.oc1..uniqueID`


        :param mount_target_id: The mount_target_id of this CreateFileSystemUnmountDetails.
        :type: str
        """
        self._mount_target_id = mount_target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
