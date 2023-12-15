# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpsiWarehouseDataObjects(object):
    """
    Logical grouping used for Operations Insights Warehouse data objects operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpsiWarehouseDataObjects object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param opsi_warehouse_data_objects:
            The value to assign to the opsi_warehouse_data_objects property of this OpsiWarehouseDataObjects.
        :type opsi_warehouse_data_objects: object

        """
        self.swagger_types = {
            'opsi_warehouse_data_objects': 'object'
        }

        self.attribute_map = {
            'opsi_warehouse_data_objects': 'opsiWarehouseDataObjects'
        }

        self._opsi_warehouse_data_objects = None

    @property
    def opsi_warehouse_data_objects(self):
        """
        Gets the opsi_warehouse_data_objects of this OpsiWarehouseDataObjects.
        Operations Insights Warehouse Data Object.


        :return: The opsi_warehouse_data_objects of this OpsiWarehouseDataObjects.
        :rtype: object
        """
        return self._opsi_warehouse_data_objects

    @opsi_warehouse_data_objects.setter
    def opsi_warehouse_data_objects(self, opsi_warehouse_data_objects):
        """
        Sets the opsi_warehouse_data_objects of this OpsiWarehouseDataObjects.
        Operations Insights Warehouse Data Object.


        :param opsi_warehouse_data_objects: The opsi_warehouse_data_objects of this OpsiWarehouseDataObjects.
        :type: object
        """
        self._opsi_warehouse_data_objects = opsi_warehouse_data_objects

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
