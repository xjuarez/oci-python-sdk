# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MergeSettings(object):
    """
    Enabled and disabled merge strategies for a project or repository, also contains a default strategy.
    """

    #: A constant which can be used with the default_merge_strategy property of a MergeSettings.
    #: This constant has a value of "MERGE_COMMIT"
    DEFAULT_MERGE_STRATEGY_MERGE_COMMIT = "MERGE_COMMIT"

    #: A constant which can be used with the default_merge_strategy property of a MergeSettings.
    #: This constant has a value of "FAST_FORWARD"
    DEFAULT_MERGE_STRATEGY_FAST_FORWARD = "FAST_FORWARD"

    #: A constant which can be used with the default_merge_strategy property of a MergeSettings.
    #: This constant has a value of "FAST_FORWARD_ONLY"
    DEFAULT_MERGE_STRATEGY_FAST_FORWARD_ONLY = "FAST_FORWARD_ONLY"

    #: A constant which can be used with the default_merge_strategy property of a MergeSettings.
    #: This constant has a value of "REBASE_AND_MERGE"
    DEFAULT_MERGE_STRATEGY_REBASE_AND_MERGE = "REBASE_AND_MERGE"

    #: A constant which can be used with the default_merge_strategy property of a MergeSettings.
    #: This constant has a value of "REBASE_AND_FAST_FORWARD"
    DEFAULT_MERGE_STRATEGY_REBASE_AND_FAST_FORWARD = "REBASE_AND_FAST_FORWARD"

    #: A constant which can be used with the default_merge_strategy property of a MergeSettings.
    #: This constant has a value of "SQUASH"
    DEFAULT_MERGE_STRATEGY_SQUASH = "SQUASH"

    #: A constant which can be used with the default_merge_strategy property of a MergeSettings.
    #: This constant has a value of "SQUASH_FAST_FORWARD_ONLY"
    DEFAULT_MERGE_STRATEGY_SQUASH_FAST_FORWARD_ONLY = "SQUASH_FAST_FORWARD_ONLY"

    def __init__(self, **kwargs):
        """
        Initializes a new MergeSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_merge_strategy:
            The value to assign to the default_merge_strategy property of this MergeSettings.
            Allowed values for this property are: "MERGE_COMMIT", "FAST_FORWARD", "FAST_FORWARD_ONLY", "REBASE_AND_MERGE", "REBASE_AND_FAST_FORWARD", "SQUASH", "SQUASH_FAST_FORWARD_ONLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type default_merge_strategy: str

        :param allowed_merge_strategies:
            The value to assign to the allowed_merge_strategies property of this MergeSettings.
        :type allowed_merge_strategies: list[oci.devops.models.MergeStrategy]

        """
        self.swagger_types = {
            'default_merge_strategy': 'str',
            'allowed_merge_strategies': 'list[MergeStrategy]'
        }

        self.attribute_map = {
            'default_merge_strategy': 'defaultMergeStrategy',
            'allowed_merge_strategies': 'allowedMergeStrategies'
        }

        self._default_merge_strategy = None
        self._allowed_merge_strategies = None

    @property
    def default_merge_strategy(self):
        """
        **[Required]** Gets the default_merge_strategy of this MergeSettings.
        Default type of merge strategy associated with the a Project or Repository.

        Allowed values for this property are: "MERGE_COMMIT", "FAST_FORWARD", "FAST_FORWARD_ONLY", "REBASE_AND_MERGE", "REBASE_AND_FAST_FORWARD", "SQUASH", "SQUASH_FAST_FORWARD_ONLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The default_merge_strategy of this MergeSettings.
        :rtype: str
        """
        return self._default_merge_strategy

    @default_merge_strategy.setter
    def default_merge_strategy(self, default_merge_strategy):
        """
        Sets the default_merge_strategy of this MergeSettings.
        Default type of merge strategy associated with the a Project or Repository.


        :param default_merge_strategy: The default_merge_strategy of this MergeSettings.
        :type: str
        """
        allowed_values = ["MERGE_COMMIT", "FAST_FORWARD", "FAST_FORWARD_ONLY", "REBASE_AND_MERGE", "REBASE_AND_FAST_FORWARD", "SQUASH", "SQUASH_FAST_FORWARD_ONLY"]
        if not value_allowed_none_or_none_sentinel(default_merge_strategy, allowed_values):
            default_merge_strategy = 'UNKNOWN_ENUM_VALUE'
        self._default_merge_strategy = default_merge_strategy

    @property
    def allowed_merge_strategies(self):
        """
        **[Required]** Gets the allowed_merge_strategies of this MergeSettings.
        List of merge strategies which are allowed for a Project or Repository.


        :return: The allowed_merge_strategies of this MergeSettings.
        :rtype: list[oci.devops.models.MergeStrategy]
        """
        return self._allowed_merge_strategies

    @allowed_merge_strategies.setter
    def allowed_merge_strategies(self, allowed_merge_strategies):
        """
        Sets the allowed_merge_strategies of this MergeSettings.
        List of merge strategies which are allowed for a Project or Repository.


        :param allowed_merge_strategies: The allowed_merge_strategies of this MergeSettings.
        :type: list[oci.devops.models.MergeStrategy]
        """
        self._allowed_merge_strategies = allowed_merge_strategies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
