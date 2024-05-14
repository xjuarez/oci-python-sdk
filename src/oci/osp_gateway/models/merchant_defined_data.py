# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MerchantDefinedData(object):
    """
    Merchant details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MerchantDefinedData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param promo_type:
            The value to assign to the promo_type property of this MerchantDefinedData.
        :type promo_type: str

        :param cloud_account_name:
            The value to assign to the cloud_account_name property of this MerchantDefinedData.
        :type cloud_account_name: str

        """
        self.swagger_types = {
            'promo_type': 'str',
            'cloud_account_name': 'str'
        }

        self.attribute_map = {
            'promo_type': 'promoType',
            'cloud_account_name': 'cloudAccountName'
        }

        self._promo_type = None
        self._cloud_account_name = None

    @property
    def promo_type(self):
        """
        Gets the promo_type of this MerchantDefinedData.
        Promotion type code.


        :return: The promo_type of this MerchantDefinedData.
        :rtype: str
        """
        return self._promo_type

    @promo_type.setter
    def promo_type(self, promo_type):
        """
        Sets the promo_type of this MerchantDefinedData.
        Promotion type code.


        :param promo_type: The promo_type of this MerchantDefinedData.
        :type: str
        """
        self._promo_type = promo_type

    @property
    def cloud_account_name(self):
        """
        Gets the cloud_account_name of this MerchantDefinedData.
        Cloud account name.


        :return: The cloud_account_name of this MerchantDefinedData.
        :rtype: str
        """
        return self._cloud_account_name

    @cloud_account_name.setter
    def cloud_account_name(self, cloud_account_name):
        """
        Sets the cloud_account_name of this MerchantDefinedData.
        Cloud account name.


        :param cloud_account_name: The cloud_account_name of this MerchantDefinedData.
        :type: str
        """
        self._cloud_account_name = cloud_account_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
