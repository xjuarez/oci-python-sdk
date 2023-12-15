# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceTypeMetadataDetails(object):
    """
    The metadata details for resource type.
    """

    #: A constant which can be used with the format property of a ResourceTypeMetadataDetails.
    #: This constant has a value of "SYSTEM_FORMAT"
    FORMAT_SYSTEM_FORMAT = "SYSTEM_FORMAT"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceTypeMetadataDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.stack_monitoring.models.SystemFormatResourceTypeMetadataDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format:
            The value to assign to the format property of this ResourceTypeMetadataDetails.
            Allowed values for this property are: "SYSTEM_FORMAT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format: str

        """
        self.swagger_types = {
            'format': 'str'
        }

        self.attribute_map = {
            'format': 'format'
        }

        self._format = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['format']

        if type == 'SYSTEM_FORMAT':
            return 'SystemFormatResourceTypeMetadataDetails'
        else:
            return 'ResourceTypeMetadataDetails'

    @property
    def format(self):
        """
        **[Required]** Gets the format of this ResourceTypeMetadataDetails.
        ResourceType metadata format to be used. Currently supports only one format.
        Possible values - SYSTEM_FORMAT.
        * SYSTEM_FORMAT - The resource type metadata is defined in machine friendly format.

        Allowed values for this property are: "SYSTEM_FORMAT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format of this ResourceTypeMetadataDetails.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this ResourceTypeMetadataDetails.
        ResourceType metadata format to be used. Currently supports only one format.
        Possible values - SYSTEM_FORMAT.
        * SYSTEM_FORMAT - The resource type metadata is defined in machine friendly format.


        :param format: The format of this ResourceTypeMetadataDetails.
        :type: str
        """
        allowed_values = ["SYSTEM_FORMAT"]
        if not value_allowed_none_or_none_sentinel(format, allowed_values):
            format = 'UNKNOWN_ENUM_VALUE'
        self._format = format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other