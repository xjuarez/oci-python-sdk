# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SellerInformation(object):
    """
    The information related to the seller of an Offer
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SellerInformation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param primary_contact:
            The value to assign to the primary_contact property of this SellerInformation.
        :type primary_contact: oci.marketplace_private_offer.models.Contact

        :param additional_contacts:
            The value to assign to the additional_contacts property of this SellerInformation.
        :type additional_contacts: list[oci.marketplace_private_offer.models.Contact]

        """
        self.swagger_types = {
            'primary_contact': 'Contact',
            'additional_contacts': 'list[Contact]'
        }

        self.attribute_map = {
            'primary_contact': 'primaryContact',
            'additional_contacts': 'additionalContacts'
        }

        self._primary_contact = None
        self._additional_contacts = None

    @property
    def primary_contact(self):
        """
        Gets the primary_contact of this SellerInformation.

        :return: The primary_contact of this SellerInformation.
        :rtype: oci.marketplace_private_offer.models.Contact
        """
        return self._primary_contact

    @primary_contact.setter
    def primary_contact(self, primary_contact):
        """
        Sets the primary_contact of this SellerInformation.

        :param primary_contact: The primary_contact of this SellerInformation.
        :type: oci.marketplace_private_offer.models.Contact
        """
        self._primary_contact = primary_contact

    @property
    def additional_contacts(self):
        """
        Gets the additional_contacts of this SellerInformation.
        the additional contacts associated with the seller


        :return: The additional_contacts of this SellerInformation.
        :rtype: list[oci.marketplace_private_offer.models.Contact]
        """
        return self._additional_contacts

    @additional_contacts.setter
    def additional_contacts(self, additional_contacts):
        """
        Sets the additional_contacts of this SellerInformation.
        the additional contacts associated with the seller


        :param additional_contacts: The additional_contacts of this SellerInformation.
        :type: list[oci.marketplace_private_offer.models.Contact]
        """
        self._additional_contacts = additional_contacts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
