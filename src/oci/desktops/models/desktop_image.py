# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopImage(object):
    """
    Provides information about the desktop image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopImage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param image_id:
            The value to assign to the image_id property of this DesktopImage.
        :type image_id: str

        :param image_name:
            The value to assign to the image_name property of this DesktopImage.
        :type image_name: str

        :param operating_system:
            The value to assign to the operating_system property of this DesktopImage.
        :type operating_system: str

        """
        self.swagger_types = {
            'image_id': 'str',
            'image_name': 'str',
            'operating_system': 'str'
        }

        self.attribute_map = {
            'image_id': 'imageId',
            'image_name': 'imageName',
            'operating_system': 'operatingSystem'
        }

        self._image_id = None
        self._image_name = None
        self._operating_system = None

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this DesktopImage.
        The OCID of the desktop image.


        :return: The image_id of this DesktopImage.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this DesktopImage.
        The OCID of the desktop image.


        :param image_id: The image_id of this DesktopImage.
        :type: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        """
        **[Required]** Gets the image_name of this DesktopImage.
        The name of the desktop image.


        :return: The image_name of this DesktopImage.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """
        Sets the image_name of this DesktopImage.
        The name of the desktop image.


        :param image_name: The image_name of this DesktopImage.
        :type: str
        """
        self._image_name = image_name

    @property
    def operating_system(self):
        """
        Gets the operating_system of this DesktopImage.
        The operating system of the desktop image, e.g. \"Oracle Linux\", \"Windows\".


        :return: The operating_system of this DesktopImage.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this DesktopImage.
        The operating system of the desktop image, e.g. \"Oracle Linux\", \"Windows\".


        :param operating_system: The operating_system of this DesktopImage.
        :type: str
        """
        self._operating_system = operating_system

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
