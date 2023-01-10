# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VsphereUpgradeObject(object):
    """
    Binary object needed for vSphere upgrade
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VsphereUpgradeObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param download_link:
            The value to assign to the download_link property of this VsphereUpgradeObject.
        :type download_link: str

        :param link_description:
            The value to assign to the link_description property of this VsphereUpgradeObject.
        :type link_description: str

        """
        self.swagger_types = {
            'download_link': 'str',
            'link_description': 'str'
        }

        self.attribute_map = {
            'download_link': 'downloadLink',
            'link_description': 'linkDescription'
        }

        self._download_link = None
        self._link_description = None

    @property
    def download_link(self):
        """
        **[Required]** Gets the download_link of this VsphereUpgradeObject.
        Binary object download link.


        :return: The download_link of this VsphereUpgradeObject.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """
        Sets the download_link of this VsphereUpgradeObject.
        Binary object download link.


        :param download_link: The download_link of this VsphereUpgradeObject.
        :type: str
        """
        self._download_link = download_link

    @property
    def link_description(self):
        """
        **[Required]** Gets the link_description of this VsphereUpgradeObject.
        Binary object description.


        :return: The link_description of this VsphereUpgradeObject.
        :rtype: str
        """
        return self._link_description

    @link_description.setter
    def link_description(self, link_description):
        """
        Sets the link_description of this VsphereUpgradeObject.
        Binary object description.


        :param link_description: The link_description of this VsphereUpgradeObject.
        :type: str
        """
        self._link_description = link_description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
