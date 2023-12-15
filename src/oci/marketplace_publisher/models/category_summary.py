# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CategorySummary(object):
    """
    The model for the category summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CategorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CategorySummary.
        :type name: str

        :param code:
            The value to assign to the code property of this CategorySummary.
        :type code: str

        :param product_code:
            The value to assign to the product_code property of this CategorySummary.
        :type product_code: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CategorySummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this CategorySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CategorySummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'code': 'str',
            'product_code': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'code': 'code',
            'product_code': 'productCode',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._name = None
        self._code = None
        self._product_code = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CategorySummary.
        The name of the category.


        :return: The name of this CategorySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CategorySummary.
        The name of the category.


        :param name: The name of this CategorySummary.
        :type: str
        """
        self._name = name

    @property
    def code(self):
        """
        **[Required]** Gets the code of this CategorySummary.
        The code of the category.


        :return: The code of this CategorySummary.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CategorySummary.
        The code of the category.


        :param code: The code of this CategorySummary.
        :type: str
        """
        self._code = code

    @property
    def product_code(self):
        """
        **[Required]** Gets the product_code of this CategorySummary.
        The product that the category belongs.


        :return: The product_code of this CategorySummary.
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """
        Sets the product_code of this CategorySummary.
        The product that the category belongs.


        :param product_code: The product_code of this CategorySummary.
        :type: str
        """
        self._product_code = product_code

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CategorySummary.
        The current state of the category.


        :return: The lifecycle_state of this CategorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CategorySummary.
        The current state of the category.


        :param lifecycle_state: The lifecycle_state of this CategorySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CategorySummary.
        The date and time the category was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CategorySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CategorySummary.
        The date and time the category was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CategorySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this CategorySummary.
        The date and time the category was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this CategorySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CategorySummary.
        The date and time the category was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this CategorySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
