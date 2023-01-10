# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAlertPolicyRuleDetails(object):
    """
    The details used to create a new alert policy rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAlertPolicyRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param expression:
            The value to assign to the expression property of this CreateAlertPolicyRuleDetails.
        :type expression: str

        :param description:
            The value to assign to the description property of this CreateAlertPolicyRuleDetails.
        :type description: str

        """
        self.swagger_types = {
            'expression': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'expression': 'expression',
            'description': 'description'
        }

        self._expression = None
        self._description = None

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this CreateAlertPolicyRuleDetails.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :return: The expression of this CreateAlertPolicyRuleDetails.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this CreateAlertPolicyRuleDetails.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :param expression: The expression of this CreateAlertPolicyRuleDetails.
        :type: str
        """
        self._expression = expression

    @property
    def description(self):
        """
        Gets the description of this CreateAlertPolicyRuleDetails.
        Describes the alert policy rule.


        :return: The description of this CreateAlertPolicyRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAlertPolicyRuleDetails.
        Describes the alert policy rule.


        :param description: The description of this CreateAlertPolicyRuleDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
