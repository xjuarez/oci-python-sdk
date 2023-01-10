# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RateCardTier(object):
    """
    Rate Card Tier details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RateCardTier object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param up_to_quantity:
            The value to assign to the up_to_quantity property of this RateCardTier.
        :type up_to_quantity: str

        :param net_unit_price:
            The value to assign to the net_unit_price property of this RateCardTier.
        :type net_unit_price: str

        :param overage_price:
            The value to assign to the overage_price property of this RateCardTier.
        :type overage_price: str

        """
        self.swagger_types = {
            'up_to_quantity': 'str',
            'net_unit_price': 'str',
            'overage_price': 'str'
        }

        self.attribute_map = {
            'up_to_quantity': 'upToQuantity',
            'net_unit_price': 'netUnitPrice',
            'overage_price': 'overagePrice'
        }

        self._up_to_quantity = None
        self._net_unit_price = None
        self._overage_price = None

    @property
    def up_to_quantity(self):
        """
        Gets the up_to_quantity of this RateCardTier.
        Rate card tier quantity range


        :return: The up_to_quantity of this RateCardTier.
        :rtype: str
        """
        return self._up_to_quantity

    @up_to_quantity.setter
    def up_to_quantity(self, up_to_quantity):
        """
        Sets the up_to_quantity of this RateCardTier.
        Rate card tier quantity range


        :param up_to_quantity: The up_to_quantity of this RateCardTier.
        :type: str
        """
        self._up_to_quantity = up_to_quantity

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this RateCardTier.
        Rate card tier net unit price


        :return: The net_unit_price of this RateCardTier.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this RateCardTier.
        Rate card tier net unit price


        :param net_unit_price: The net_unit_price of this RateCardTier.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def overage_price(self):
        """
        Gets the overage_price of this RateCardTier.
        Rate card tier overage price


        :return: The overage_price of this RateCardTier.
        :rtype: str
        """
        return self._overage_price

    @overage_price.setter
    def overage_price(self, overage_price):
        """
        Sets the overage_price of this RateCardTier.
        Rate card tier overage price


        :param overage_price: The overage_price of this RateCardTier.
        :type: str
        """
        self._overage_price = overage_price

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
