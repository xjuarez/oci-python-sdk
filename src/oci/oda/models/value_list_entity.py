# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506

from .entity import Entity
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValueListEntity(Entity):
    """
    Metadata for a value list entity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValueListEntity object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.ValueListEntity.type` attribute
        of this class is ``ENUM_VALUES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ValueListEntity.
        :type id: str

        :param name:
            The value to assign to the name property of this ValueListEntity.
        :type name: str

        :param type:
            The value to assign to the type property of this ValueListEntity.
            Allowed values for this property are: "COMPOSITE", "ENUM_VALUES"
        :type type: str

        :param values:
            The value to assign to the values property of this ValueListEntity.
        :type values: list[oci.oda.models.StaticEntityValue]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'values': 'list[StaticEntityValue]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'values': 'values'
        }

        self._id = None
        self._name = None
        self._type = None
        self._values = None
        self._type = 'ENUM_VALUES'

    @property
    def values(self):
        """
        **[Required]** Gets the values of this ValueListEntity.
        List of values for a value list entity.


        :return: The values of this ValueListEntity.
        :rtype: list[oci.oda.models.StaticEntityValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this ValueListEntity.
        List of values for a value list entity.


        :param values: The values of this ValueListEntity.
        :type: list[oci.oda.models.StaticEntityValue]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
