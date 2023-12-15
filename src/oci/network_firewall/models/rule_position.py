# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RulePosition(object):
    """
    An object which defines the position of the rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RulePosition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param before_rule:
            The value to assign to the before_rule property of this RulePosition.
        :type before_rule: str

        :param after_rule:
            The value to assign to the after_rule property of this RulePosition.
        :type after_rule: str

        """
        self.swagger_types = {
            'before_rule': 'str',
            'after_rule': 'str'
        }

        self.attribute_map = {
            'before_rule': 'beforeRule',
            'after_rule': 'afterRule'
        }

        self._before_rule = None
        self._after_rule = None

    @property
    def before_rule(self):
        """
        Gets the before_rule of this RulePosition.
        Identifier for rule before which this rule lies.


        :return: The before_rule of this RulePosition.
        :rtype: str
        """
        return self._before_rule

    @before_rule.setter
    def before_rule(self, before_rule):
        """
        Sets the before_rule of this RulePosition.
        Identifier for rule before which this rule lies.


        :param before_rule: The before_rule of this RulePosition.
        :type: str
        """
        self._before_rule = before_rule

    @property
    def after_rule(self):
        """
        Gets the after_rule of this RulePosition.
        Identifier for rule after which this rule lies.


        :return: The after_rule of this RulePosition.
        :rtype: str
        """
        return self._after_rule

    @after_rule.setter
    def after_rule(self, after_rule):
        """
        Sets the after_rule of this RulePosition.
        Identifier for rule after which this rule lies.


        :param after_rule: The after_rule of this RulePosition.
        :type: str
        """
        self._after_rule = after_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other