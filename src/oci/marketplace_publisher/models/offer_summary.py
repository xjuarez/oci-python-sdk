# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OfferSummary(object):
    """
    Summary of the Offers.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OfferSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OfferSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OfferSummary.
        :type display_name: str

        :param buyer_compartment_id:
            The value to assign to the buyer_compartment_id property of this OfferSummary.
        :type buyer_compartment_id: str

        :param seller_compartment_id:
            The value to assign to the seller_compartment_id property of this OfferSummary.
        :type seller_compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this OfferSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OfferSummary.
        :type time_updated: datetime

        :param time_accept_by:
            The value to assign to the time_accept_by property of this OfferSummary.
        :type time_accept_by: datetime

        :param time_accepted:
            The value to assign to the time_accepted property of this OfferSummary.
        :type time_accepted: datetime

        :param time_start_date:
            The value to assign to the time_start_date property of this OfferSummary.
        :type time_start_date: datetime

        :param time_offer_end:
            The value to assign to the time_offer_end property of this OfferSummary.
        :type time_offer_end: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OfferSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OfferSummary.
        :type lifecycle_details: str

        :param offer_status:
            The value to assign to the offer_status property of this OfferSummary.
        :type offer_status: str

        :param buyer_information:
            The value to assign to the buyer_information property of this OfferSummary.
        :type buyer_information: oci.marketplace_publisher.models.BuyerInformation

        :param seller_information:
            The value to assign to the seller_information property of this OfferSummary.
        :type seller_information: oci.marketplace_publisher.models.SellerInformation

        :param pricing:
            The value to assign to the pricing property of this OfferSummary.
        :type pricing: oci.marketplace_publisher.models.Pricing

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OfferSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OfferSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'buyer_compartment_id': 'str',
            'seller_compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_accept_by': 'datetime',
            'time_accepted': 'datetime',
            'time_start_date': 'datetime',
            'time_offer_end': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'offer_status': 'str',
            'buyer_information': 'BuyerInformation',
            'seller_information': 'SellerInformation',
            'pricing': 'Pricing',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'buyer_compartment_id': 'buyerCompartmentId',
            'seller_compartment_id': 'sellerCompartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_accept_by': 'timeAcceptBy',
            'time_accepted': 'timeAccepted',
            'time_start_date': 'timeStartDate',
            'time_offer_end': 'timeOfferEnd',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'offer_status': 'offerStatus',
            'buyer_information': 'buyerInformation',
            'seller_information': 'sellerInformation',
            'pricing': 'pricing',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._buyer_compartment_id = None
        self._seller_compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._time_accept_by = None
        self._time_accepted = None
        self._time_start_date = None
        self._time_offer_end = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._offer_status = None
        self._buyer_information = None
        self._seller_information = None
        self._pricing = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OfferSummary.
        Unique identifier that is immutable on creation


        :return: The id of this OfferSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OfferSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this OfferSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OfferSummary.
        Offer Identifier, can be renamed


        :return: The display_name of this OfferSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OfferSummary.
        Offer Identifier, can be renamed


        :param display_name: The display_name of this OfferSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def buyer_compartment_id(self):
        """
        **[Required]** Gets the buyer_compartment_id of this OfferSummary.
        Ocid of the buyer tenancy.


        :return: The buyer_compartment_id of this OfferSummary.
        :rtype: str
        """
        return self._buyer_compartment_id

    @buyer_compartment_id.setter
    def buyer_compartment_id(self, buyer_compartment_id):
        """
        Sets the buyer_compartment_id of this OfferSummary.
        Ocid of the buyer tenancy.


        :param buyer_compartment_id: The buyer_compartment_id of this OfferSummary.
        :type: str
        """
        self._buyer_compartment_id = buyer_compartment_id

    @property
    def seller_compartment_id(self):
        """
        **[Required]** Gets the seller_compartment_id of this OfferSummary.
        Ocid of the seller tenancy.


        :return: The seller_compartment_id of this OfferSummary.
        :rtype: str
        """
        return self._seller_compartment_id

    @seller_compartment_id.setter
    def seller_compartment_id(self, seller_compartment_id):
        """
        Sets the seller_compartment_id of this OfferSummary.
        Ocid of the seller tenancy.


        :param seller_compartment_id: The seller_compartment_id of this OfferSummary.
        :type: str
        """
        self._seller_compartment_id = seller_compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OfferSummary.
        The time the the Offer was created. An RFC3339 formatted datetime string


        :return: The time_created of this OfferSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OfferSummary.
        The time the the Offer was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this OfferSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OfferSummary.
        The time the Offer was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this OfferSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OfferSummary.
        The time the Offer was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this OfferSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_accept_by(self):
        """
        Gets the time_accept_by of this OfferSummary.
        The time the Offer must be accepted by the Buyer before the Offer becomes invalid. An RFC3339 formatted datetime string


        :return: The time_accept_by of this OfferSummary.
        :rtype: datetime
        """
        return self._time_accept_by

    @time_accept_by.setter
    def time_accept_by(self, time_accept_by):
        """
        Sets the time_accept_by of this OfferSummary.
        The time the Offer must be accepted by the Buyer before the Offer becomes invalid. An RFC3339 formatted datetime string


        :param time_accept_by: The time_accept_by of this OfferSummary.
        :type: datetime
        """
        self._time_accept_by = time_accept_by

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this OfferSummary.
        The time the Offer was accepted by the Buyer of the Offer. An RFC3339 formatted datetime string


        :return: The time_accepted of this OfferSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this OfferSummary.
        The time the Offer was accepted by the Buyer of the Offer. An RFC3339 formatted datetime string


        :param time_accepted: The time_accepted of this OfferSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_start_date(self):
        """
        Gets the time_start_date of this OfferSummary.
        The time the Offer will become active after it has been accepted by the Buyer. An RFC3339 formatted datetime string


        :return: The time_start_date of this OfferSummary.
        :rtype: datetime
        """
        return self._time_start_date

    @time_start_date.setter
    def time_start_date(self, time_start_date):
        """
        Sets the time_start_date of this OfferSummary.
        The time the Offer will become active after it has been accepted by the Buyer. An RFC3339 formatted datetime string


        :param time_start_date: The time_start_date of this OfferSummary.
        :type: datetime
        """
        self._time_start_date = time_start_date

    @property
    def time_offer_end(self):
        """
        Gets the time_offer_end of this OfferSummary.
        The time the accepted Offer will end. An RFC3339 formatted datetime string


        :return: The time_offer_end of this OfferSummary.
        :rtype: datetime
        """
        return self._time_offer_end

    @time_offer_end.setter
    def time_offer_end(self, time_offer_end):
        """
        Sets the time_offer_end of this OfferSummary.
        The time the accepted Offer will end. An RFC3339 formatted datetime string


        :param time_offer_end: The time_offer_end of this OfferSummary.
        :type: datetime
        """
        self._time_offer_end = time_offer_end

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OfferSummary.
        The current state of the Offer.


        :return: The lifecycle_state of this OfferSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OfferSummary.
        The current state of the Offer.


        :param lifecycle_state: The lifecycle_state of this OfferSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OfferSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this OfferSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OfferSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this OfferSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def offer_status(self):
        """
        Gets the offer_status of this OfferSummary.
        The human readable representation of where the offer is at in it's contract lifecycle.


        :return: The offer_status of this OfferSummary.
        :rtype: str
        """
        return self._offer_status

    @offer_status.setter
    def offer_status(self, offer_status):
        """
        Sets the offer_status of this OfferSummary.
        The human readable representation of where the offer is at in it's contract lifecycle.


        :param offer_status: The offer_status of this OfferSummary.
        :type: str
        """
        self._offer_status = offer_status

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this OfferSummary.

        :return: The buyer_information of this OfferSummary.
        :rtype: oci.marketplace_publisher.models.BuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this OfferSummary.

        :param buyer_information: The buyer_information of this OfferSummary.
        :type: oci.marketplace_publisher.models.BuyerInformation
        """
        self._buyer_information = buyer_information

    @property
    def seller_information(self):
        """
        Gets the seller_information of this OfferSummary.

        :return: The seller_information of this OfferSummary.
        :rtype: oci.marketplace_publisher.models.SellerInformation
        """
        return self._seller_information

    @seller_information.setter
    def seller_information(self, seller_information):
        """
        Sets the seller_information of this OfferSummary.

        :param seller_information: The seller_information of this OfferSummary.
        :type: oci.marketplace_publisher.models.SellerInformation
        """
        self._seller_information = seller_information

    @property
    def pricing(self):
        """
        Gets the pricing of this OfferSummary.

        :return: The pricing of this OfferSummary.
        :rtype: oci.marketplace_publisher.models.Pricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """
        Sets the pricing of this OfferSummary.

        :param pricing: The pricing of this OfferSummary.
        :type: oci.marketplace_publisher.models.Pricing
        """
        self._pricing = pricing

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this OfferSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OfferSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OfferSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OfferSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this OfferSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OfferSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OfferSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OfferSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
