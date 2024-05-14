# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .opsi_data_object import OpsiDataObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseInsightsDataObject(OpsiDataObject):
    """
    Database insights data object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseInsightsDataObject object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DatabaseInsightsDataObject.data_object_type` attribute
        of this class is ``DATABASE_INSIGHTS_DATA_OBJECT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param identifier:
            The value to assign to the identifier property of this DatabaseInsightsDataObject.
        :type identifier: str

        :param data_object_type:
            The value to assign to the data_object_type property of this DatabaseInsightsDataObject.
            Allowed values for this property are: "DATABASE_INSIGHTS_DATA_OBJECT", "HOST_INSIGHTS_DATA_OBJECT", "EXADATA_INSIGHTS_DATA_OBJECT"
        :type data_object_type: str

        :param display_name:
            The value to assign to the display_name property of this DatabaseInsightsDataObject.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DatabaseInsightsDataObject.
        :type description: str

        :param name:
            The value to assign to the name property of this DatabaseInsightsDataObject.
        :type name: str

        :param group_names:
            The value to assign to the group_names property of this DatabaseInsightsDataObject.
        :type group_names: list[str]

        :param supported_query_time_period:
            The value to assign to the supported_query_time_period property of this DatabaseInsightsDataObject.
        :type supported_query_time_period: str

        :param columns_metadata:
            The value to assign to the columns_metadata property of this DatabaseInsightsDataObject.
        :type columns_metadata: list[oci.opsi.models.DataObjectColumnMetadata]

        :param supported_query_params:
            The value to assign to the supported_query_params property of this DatabaseInsightsDataObject.
        :type supported_query_params: list[oci.opsi.models.OpsiDataObjectSupportedQueryParam]

        """
        self.swagger_types = {
            'identifier': 'str',
            'data_object_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'name': 'str',
            'group_names': 'list[str]',
            'supported_query_time_period': 'str',
            'columns_metadata': 'list[DataObjectColumnMetadata]',
            'supported_query_params': 'list[OpsiDataObjectSupportedQueryParam]'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'data_object_type': 'dataObjectType',
            'display_name': 'displayName',
            'description': 'description',
            'name': 'name',
            'group_names': 'groupNames',
            'supported_query_time_period': 'supportedQueryTimePeriod',
            'columns_metadata': 'columnsMetadata',
            'supported_query_params': 'supportedQueryParams'
        }

        self._identifier = None
        self._data_object_type = None
        self._display_name = None
        self._description = None
        self._name = None
        self._group_names = None
        self._supported_query_time_period = None
        self._columns_metadata = None
        self._supported_query_params = None
        self._data_object_type = 'DATABASE_INSIGHTS_DATA_OBJECT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
