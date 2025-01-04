# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231

from .create_item_details import CreateItemDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAccountItemDetails(CreateItemDetails):
    """
    Details about the issue that the account support ticket relates to. Avoid entering confidential information.
    For information about `ACCOUNT` support tickets, see `Creating a Billing Support Request`__.

    __ https://docs.cloud.oracle.com/iaas/Content/GSG/support/create-incident-billing.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAccountItemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cims.models.CreateAccountItemDetails.type` attribute
        of this class is ``account`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateAccountItemDetails.
        :type type: str

        :param category:
            The value to assign to the category property of this CreateAccountItemDetails.
        :type category: oci.cims.models.CreateCategoryDetails

        :param sub_category:
            The value to assign to the sub_category property of this CreateAccountItemDetails.
        :type sub_category: oci.cims.models.CreateSubCategoryDetails

        :param issue_type:
            The value to assign to the issue_type property of this CreateAccountItemDetails.
        :type issue_type: oci.cims.models.CreateIssueTypeDetails

        :param name:
            The value to assign to the name property of this CreateAccountItemDetails.
        :type name: str

        """
        self.swagger_types = {
            'type': 'str',
            'category': 'CreateCategoryDetails',
            'sub_category': 'CreateSubCategoryDetails',
            'issue_type': 'CreateIssueTypeDetails',
            'name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'category': 'category',
            'sub_category': 'subCategory',
            'issue_type': 'issueType',
            'name': 'name'
        }

        self._type = None
        self._category = None
        self._sub_category = None
        self._issue_type = None
        self._name = None
        self._type = 'account'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
