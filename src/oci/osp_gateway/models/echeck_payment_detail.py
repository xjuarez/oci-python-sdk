# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001

from .payment_detail import PaymentDetail
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EcheckPaymentDetail(PaymentDetail):
    """
    Echeck Payment related details
    """

    #: A constant which can be used with the card_type property of a EcheckPaymentDetail.
    #: This constant has a value of "SAVING"
    CARD_TYPE_SAVING = "SAVING"

    #: A constant which can be used with the card_type property of a EcheckPaymentDetail.
    #: This constant has a value of "CHECKING"
    CARD_TYPE_CHECKING = "CHECKING"

    #: A constant which can be used with the card_type property of a EcheckPaymentDetail.
    #: This constant has a value of "CORPORATE_CHECKING"
    CARD_TYPE_CORPORATE_CHECKING = "CORPORATE_CHECKING"

    def __init__(self, **kwargs):
        """
        Initializes a new EcheckPaymentDetail object with values from keyword arguments. The default value of the :py:attr:`~oci.osp_gateway.models.EcheckPaymentDetail.payment_method` attribute
        of this class is ``ECHECK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_paid_on:
            The value to assign to the time_paid_on property of this EcheckPaymentDetail.
        :type time_paid_on: datetime

        :param paid_by:
            The value to assign to the paid_by property of this EcheckPaymentDetail.
        :type paid_by: str

        :param payment_method:
            The value to assign to the payment_method property of this EcheckPaymentDetail.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL", "ECHECK", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type payment_method: str

        :param amount_paid:
            The value to assign to the amount_paid property of this EcheckPaymentDetail.
        :type amount_paid: float

        :param name_on_card:
            The value to assign to the name_on_card property of this EcheckPaymentDetail.
        :type name_on_card: str

        :param card_type:
            The value to assign to the card_type property of this EcheckPaymentDetail.
            Allowed values for this property are: "SAVING", "CHECKING", "CORPORATE_CHECKING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type card_type: str

        :param account_number:
            The value to assign to the account_number property of this EcheckPaymentDetail.
        :type account_number: str

        :param routing_number:
            The value to assign to the routing_number property of this EcheckPaymentDetail.
        :type routing_number: str

        """
        self.swagger_types = {
            'time_paid_on': 'datetime',
            'paid_by': 'str',
            'payment_method': 'str',
            'amount_paid': 'float',
            'name_on_card': 'str',
            'card_type': 'str',
            'account_number': 'str',
            'routing_number': 'str'
        }

        self.attribute_map = {
            'time_paid_on': 'timePaidOn',
            'paid_by': 'paidBy',
            'payment_method': 'paymentMethod',
            'amount_paid': 'amountPaid',
            'name_on_card': 'nameOnCard',
            'card_type': 'cardType',
            'account_number': 'accountNumber',
            'routing_number': 'routingNumber'
        }

        self._time_paid_on = None
        self._paid_by = None
        self._payment_method = None
        self._amount_paid = None
        self._name_on_card = None
        self._card_type = None
        self._account_number = None
        self._routing_number = None
        self._payment_method = 'ECHECK'

    @property
    def name_on_card(self):
        """
        Gets the name_on_card of this EcheckPaymentDetail.
        Name on the echeck card


        :return: The name_on_card of this EcheckPaymentDetail.
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card):
        """
        Sets the name_on_card of this EcheckPaymentDetail.
        Name on the echeck card


        :param name_on_card: The name_on_card of this EcheckPaymentDetail.
        :type: str
        """
        self._name_on_card = name_on_card

    @property
    def card_type(self):
        """
        Gets the card_type of this EcheckPaymentDetail.
        Echeck card type

        Allowed values for this property are: "SAVING", "CHECKING", "CORPORATE_CHECKING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The card_type of this EcheckPaymentDetail.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this EcheckPaymentDetail.
        Echeck card type


        :param card_type: The card_type of this EcheckPaymentDetail.
        :type: str
        """
        allowed_values = ["SAVING", "CHECKING", "CORPORATE_CHECKING"]
        if not value_allowed_none_or_none_sentinel(card_type, allowed_values):
            card_type = 'UNKNOWN_ENUM_VALUE'
        self._card_type = card_type

    @property
    def account_number(self):
        """
        Gets the account_number of this EcheckPaymentDetail.
        Account number of the card owner


        :return: The account_number of this EcheckPaymentDetail.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """
        Sets the account_number of this EcheckPaymentDetail.
        Account number of the card owner


        :param account_number: The account_number of this EcheckPaymentDetail.
        :type: str
        """
        self._account_number = account_number

    @property
    def routing_number(self):
        """
        Gets the routing_number of this EcheckPaymentDetail.
        Routing number of the echeck card


        :return: The routing_number of this EcheckPaymentDetail.
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """
        Sets the routing_number of this EcheckPaymentDetail.
        Routing number of the echeck card


        :param routing_number: The routing_number of this EcheckPaymentDetail.
        :type: str
        """
        self._routing_number = routing_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
