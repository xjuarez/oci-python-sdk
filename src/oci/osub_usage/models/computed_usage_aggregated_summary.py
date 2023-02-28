# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputedUsageAggregatedSummary(object):
    """
    Subscribed Service Contract details
    """

    #: A constant which can be used with the pricing_model property of a ComputedUsageAggregatedSummary.
    #: This constant has a value of "PAY_AS_YOU_GO"
    PRICING_MODEL_PAY_AS_YOU_GO = "PAY_AS_YOU_GO"

    #: A constant which can be used with the pricing_model property of a ComputedUsageAggregatedSummary.
    #: This constant has a value of "MONTHLY"
    PRICING_MODEL_MONTHLY = "MONTHLY"

    #: A constant which can be used with the pricing_model property of a ComputedUsageAggregatedSummary.
    #: This constant has a value of "ANNUAL"
    PRICING_MODEL_ANNUAL = "ANNUAL"

    #: A constant which can be used with the pricing_model property of a ComputedUsageAggregatedSummary.
    #: This constant has a value of "PREPAID"
    PRICING_MODEL_PREPAID = "PREPAID"

    #: A constant which can be used with the pricing_model property of a ComputedUsageAggregatedSummary.
    #: This constant has a value of "FUNDED_ALLOCATION"
    PRICING_MODEL_FUNDED_ALLOCATION = "FUNDED_ALLOCATION"

    def __init__(self, **kwargs):
        """
        Initializes a new ComputedUsageAggregatedSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subscription_id:
            The value to assign to the subscription_id property of this ComputedUsageAggregatedSummary.
        :type subscription_id: str

        :param parent_subscribed_service_id:
            The value to assign to the parent_subscribed_service_id property of this ComputedUsageAggregatedSummary.
        :type parent_subscribed_service_id: str

        :param parent_product:
            The value to assign to the parent_product property of this ComputedUsageAggregatedSummary.
        :type parent_product: oci.osub_usage.models.Product

        :param time_start:
            The value to assign to the time_start property of this ComputedUsageAggregatedSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this ComputedUsageAggregatedSummary.
        :type time_end: datetime

        :param plan_number:
            The value to assign to the plan_number property of this ComputedUsageAggregatedSummary.
        :type plan_number: str

        :param currency_code:
            The value to assign to the currency_code property of this ComputedUsageAggregatedSummary.
        :type currency_code: str

        :param rate_card_id:
            The value to assign to the rate_card_id property of this ComputedUsageAggregatedSummary.
        :type rate_card_id: str

        :param pricing_model:
            The value to assign to the pricing_model property of this ComputedUsageAggregatedSummary.
            Allowed values for this property are: "PAY_AS_YOU_GO", "MONTHLY", "ANNUAL", "PREPAID", "FUNDED_ALLOCATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pricing_model: str

        :param aggregated_computed_usages:
            The value to assign to the aggregated_computed_usages property of this ComputedUsageAggregatedSummary.
        :type aggregated_computed_usages: list[oci.osub_usage.models.ComputedUsageAggregation]

        """
        self.swagger_types = {
            'subscription_id': 'str',
            'parent_subscribed_service_id': 'str',
            'parent_product': 'Product',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'plan_number': 'str',
            'currency_code': 'str',
            'rate_card_id': 'str',
            'pricing_model': 'str',
            'aggregated_computed_usages': 'list[ComputedUsageAggregation]'
        }

        self.attribute_map = {
            'subscription_id': 'subscriptionId',
            'parent_subscribed_service_id': 'parentSubscribedServiceId',
            'parent_product': 'parentProduct',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'plan_number': 'planNumber',
            'currency_code': 'currencyCode',
            'rate_card_id': 'rateCardId',
            'pricing_model': 'pricingModel',
            'aggregated_computed_usages': 'aggregatedComputedUsages'
        }

        self._subscription_id = None
        self._parent_subscribed_service_id = None
        self._parent_product = None
        self._time_start = None
        self._time_end = None
        self._plan_number = None
        self._currency_code = None
        self._rate_card_id = None
        self._pricing_model = None
        self._aggregated_computed_usages = None

    @property
    def subscription_id(self):
        """
        **[Required]** Gets the subscription_id of this ComputedUsageAggregatedSummary.
        Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM


        :return: The subscription_id of this ComputedUsageAggregatedSummary.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this ComputedUsageAggregatedSummary.
        Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM


        :param subscription_id: The subscription_id of this ComputedUsageAggregatedSummary.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def parent_subscribed_service_id(self):
        """
        Gets the parent_subscribed_service_id of this ComputedUsageAggregatedSummary.
        Subscribed service line parent id


        :return: The parent_subscribed_service_id of this ComputedUsageAggregatedSummary.
        :rtype: str
        """
        return self._parent_subscribed_service_id

    @parent_subscribed_service_id.setter
    def parent_subscribed_service_id(self, parent_subscribed_service_id):
        """
        Sets the parent_subscribed_service_id of this ComputedUsageAggregatedSummary.
        Subscribed service line parent id


        :param parent_subscribed_service_id: The parent_subscribed_service_id of this ComputedUsageAggregatedSummary.
        :type: str
        """
        self._parent_subscribed_service_id = parent_subscribed_service_id

    @property
    def parent_product(self):
        """
        Gets the parent_product of this ComputedUsageAggregatedSummary.

        :return: The parent_product of this ComputedUsageAggregatedSummary.
        :rtype: oci.osub_usage.models.Product
        """
        return self._parent_product

    @parent_product.setter
    def parent_product(self, parent_product):
        """
        Sets the parent_product of this ComputedUsageAggregatedSummary.

        :param parent_product: The parent_product of this ComputedUsageAggregatedSummary.
        :type: oci.osub_usage.models.Product
        """
        self._parent_product = parent_product

    @property
    def time_start(self):
        """
        Gets the time_start of this ComputedUsageAggregatedSummary.
        Subscribed services contract line start date, expressed in RFC 3339 timestamp format.


        :return: The time_start of this ComputedUsageAggregatedSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this ComputedUsageAggregatedSummary.
        Subscribed services contract line start date, expressed in RFC 3339 timestamp format.


        :param time_start: The time_start of this ComputedUsageAggregatedSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this ComputedUsageAggregatedSummary.
        Subscribed services contract line end date, expressed in RFC 3339 timestamp format.


        :return: The time_end of this ComputedUsageAggregatedSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this ComputedUsageAggregatedSummary.
        Subscribed services contract line end date, expressed in RFC 3339 timestamp format.


        :param time_end: The time_end of this ComputedUsageAggregatedSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def plan_number(self):
        """
        Gets the plan_number of this ComputedUsageAggregatedSummary.
        Subscribed service asociated subscription plan number.


        :return: The plan_number of this ComputedUsageAggregatedSummary.
        :rtype: str
        """
        return self._plan_number

    @plan_number.setter
    def plan_number(self, plan_number):
        """
        Sets the plan_number of this ComputedUsageAggregatedSummary.
        Subscribed service asociated subscription plan number.


        :param plan_number: The plan_number of this ComputedUsageAggregatedSummary.
        :type: str
        """
        self._plan_number = plan_number

    @property
    def currency_code(self):
        """
        Gets the currency_code of this ComputedUsageAggregatedSummary.
        Currency code


        :return: The currency_code of this ComputedUsageAggregatedSummary.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this ComputedUsageAggregatedSummary.
        Currency code


        :param currency_code: The currency_code of this ComputedUsageAggregatedSummary.
        :type: str
        """
        self._currency_code = currency_code

    @property
    def rate_card_id(self):
        """
        Gets the rate_card_id of this ComputedUsageAggregatedSummary.
        Inernal SPM Ratecard Id at line level


        :return: The rate_card_id of this ComputedUsageAggregatedSummary.
        :rtype: str
        """
        return self._rate_card_id

    @rate_card_id.setter
    def rate_card_id(self, rate_card_id):
        """
        Sets the rate_card_id of this ComputedUsageAggregatedSummary.
        Inernal SPM Ratecard Id at line level


        :param rate_card_id: The rate_card_id of this ComputedUsageAggregatedSummary.
        :type: str
        """
        self._rate_card_id = rate_card_id

    @property
    def pricing_model(self):
        """
        Gets the pricing_model of this ComputedUsageAggregatedSummary.
        Subscribed services pricing model

        Allowed values for this property are: "PAY_AS_YOU_GO", "MONTHLY", "ANNUAL", "PREPAID", "FUNDED_ALLOCATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pricing_model of this ComputedUsageAggregatedSummary.
        :rtype: str
        """
        return self._pricing_model

    @pricing_model.setter
    def pricing_model(self, pricing_model):
        """
        Sets the pricing_model of this ComputedUsageAggregatedSummary.
        Subscribed services pricing model


        :param pricing_model: The pricing_model of this ComputedUsageAggregatedSummary.
        :type: str
        """
        allowed_values = ["PAY_AS_YOU_GO", "MONTHLY", "ANNUAL", "PREPAID", "FUNDED_ALLOCATION"]
        if not value_allowed_none_or_none_sentinel(pricing_model, allowed_values):
            pricing_model = 'UNKNOWN_ENUM_VALUE'
        self._pricing_model = pricing_model

    @property
    def aggregated_computed_usages(self):
        """
        Gets the aggregated_computed_usages of this ComputedUsageAggregatedSummary.
        Aggregation of computed usages for the subscribed service.


        :return: The aggregated_computed_usages of this ComputedUsageAggregatedSummary.
        :rtype: list[oci.osub_usage.models.ComputedUsageAggregation]
        """
        return self._aggregated_computed_usages

    @aggregated_computed_usages.setter
    def aggregated_computed_usages(self, aggregated_computed_usages):
        """
        Sets the aggregated_computed_usages of this ComputedUsageAggregatedSummary.
        Aggregation of computed usages for the subscribed service.


        :param aggregated_computed_usages: The aggregated_computed_usages of this ComputedUsageAggregatedSummary.
        :type: list[oci.osub_usage.models.ComputedUsageAggregation]
        """
        self._aggregated_computed_usages = aggregated_computed_usages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
