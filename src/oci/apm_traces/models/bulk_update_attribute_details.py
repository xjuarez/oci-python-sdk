# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkUpdateAttributeDetails(object):
    """
    Bulk request object containing the details of the attributes for which properties are to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkUpdateAttributeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_details:
            The value to assign to the attribute_details property of this BulkUpdateAttributeDetails.
        :type attribute_details: list[oci.apm_traces.models.BulkUpdateAttributeDetail]

        """
        self.swagger_types = {
            'attribute_details': 'list[BulkUpdateAttributeDetail]'
        }

        self.attribute_map = {
            'attribute_details': 'attributeDetails'
        }

        self._attribute_details = None

    @property
    def attribute_details(self):
        """
        Gets the attribute_details of this BulkUpdateAttributeDetails.
        Collection of objects containing the details about individual attribute for which properties are to be updated.


        :return: The attribute_details of this BulkUpdateAttributeDetails.
        :rtype: list[oci.apm_traces.models.BulkUpdateAttributeDetail]
        """
        return self._attribute_details

    @attribute_details.setter
    def attribute_details(self, attribute_details):
        """
        Sets the attribute_details of this BulkUpdateAttributeDetails.
        Collection of objects containing the details about individual attribute for which properties are to be updated.


        :param attribute_details: The attribute_details of this BulkUpdateAttributeDetails.
        :type: list[oci.apm_traces.models.BulkUpdateAttributeDetail]
        """
        self._attribute_details = attribute_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
