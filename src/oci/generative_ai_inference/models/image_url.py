# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageUrl(object):
    """
    Represents a single instance of chat image url.
    """

    #: A constant which can be used with the detail property of a ImageUrl.
    #: This constant has a value of "AUTO"
    DETAIL_AUTO = "AUTO"

    #: A constant which can be used with the detail property of a ImageUrl.
    #: This constant has a value of "HIGH"
    DETAIL_HIGH = "HIGH"

    #: A constant which can be used with the detail property of a ImageUrl.
    #: This constant has a value of "LOW"
    DETAIL_LOW = "LOW"

    def __init__(self, **kwargs):
        """
        Initializes a new ImageUrl object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param url:
            The value to assign to the url property of this ImageUrl.
        :type url: str

        :param detail:
            The value to assign to the detail property of this ImageUrl.
            Allowed values for this property are: "AUTO", "HIGH", "LOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type detail: str

        """
        self.swagger_types = {
            'url': 'str',
            'detail': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'detail': 'detail'
        }

        self._url = None
        self._detail = None

    @property
    def url(self):
        """
        **[Required]** Gets the url of this ImageUrl.
        The URL of the image.


        :return: The url of this ImageUrl.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ImageUrl.
        The URL of the image.


        :param url: The url of this ImageUrl.
        :type: str
        """
        self._url = url

    @property
    def detail(self):
        """
        Gets the detail of this ImageUrl.
        The level of the detail.

        Allowed values for this property are: "AUTO", "HIGH", "LOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The detail of this ImageUrl.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """
        Sets the detail of this ImageUrl.
        The level of the detail.


        :param detail: The detail of this ImageUrl.
        :type: str
        """
        allowed_values = ["AUTO", "HIGH", "LOW"]
        if not value_allowed_none_or_none_sentinel(detail, allowed_values):
            detail = 'UNKNOWN_ENUM_VALUE'
        self._detail = detail

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
