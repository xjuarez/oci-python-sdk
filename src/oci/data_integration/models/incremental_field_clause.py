# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IncrementalFieldClause(object):
    """
    Field clause for incremental read operation.
    """

    #: A constant which can be used with the incremental_comparator property of a IncrementalFieldClause.
    #: This constant has a value of "LESSTHAN"
    INCREMENTAL_COMPARATOR_LESSTHAN = "LESSTHAN"

    #: A constant which can be used with the incremental_comparator property of a IncrementalFieldClause.
    #: This constant has a value of "GREATERTHAN"
    INCREMENTAL_COMPARATOR_GREATERTHAN = "GREATERTHAN"

    #: A constant which can be used with the incremental_comparator property of a IncrementalFieldClause.
    #: This constant has a value of "EQUALS"
    INCREMENTAL_COMPARATOR_EQUALS = "EQUALS"

    #: A constant which can be used with the incremental_comparator property of a IncrementalFieldClause.
    #: This constant has a value of "LESSTHANEQUALS"
    INCREMENTAL_COMPARATOR_LESSTHANEQUALS = "LESSTHANEQUALS"

    #: A constant which can be used with the incremental_comparator property of a IncrementalFieldClause.
    #: This constant has a value of "GREATERTHANEQUALS"
    INCREMENTAL_COMPARATOR_GREATERTHANEQUALS = "GREATERTHANEQUALS"

    #: A constant which can be used with the incremental_comparator property of a IncrementalFieldClause.
    #: This constant has a value of "STARTSWITH"
    INCREMENTAL_COMPARATOR_STARTSWITH = "STARTSWITH"

    #: A constant which can be used with the incremental_comparator property of a IncrementalFieldClause.
    #: This constant has a value of "CONTAINS"
    INCREMENTAL_COMPARATOR_CONTAINS = "CONTAINS"

    def __init__(self, **kwargs):
        """
        Initializes a new IncrementalFieldClause object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param incremental_field_name:
            The value to assign to the incremental_field_name property of this IncrementalFieldClause.
        :type incremental_field_name: str

        :param incremental_field_value:
            The value to assign to the incremental_field_value property of this IncrementalFieldClause.
        :type incremental_field_value: dict(str, str)

        :param incremental_comparator:
            The value to assign to the incremental_comparator property of this IncrementalFieldClause.
            Allowed values for this property are: "LESSTHAN", "GREATERTHAN", "EQUALS", "LESSTHANEQUALS", "GREATERTHANEQUALS", "STARTSWITH", "CONTAINS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type incremental_comparator: str

        """
        self.swagger_types = {
            'incremental_field_name': 'str',
            'incremental_field_value': 'dict(str, str)',
            'incremental_comparator': 'str'
        }

        self.attribute_map = {
            'incremental_field_name': 'incrementalFieldName',
            'incremental_field_value': 'incrementalFieldValue',
            'incremental_comparator': 'incrementalComparator'
        }

        self._incremental_field_name = None
        self._incremental_field_value = None
        self._incremental_comparator = None

    @property
    def incremental_field_name(self):
        """
        **[Required]** Gets the incremental_field_name of this IncrementalFieldClause.
        Name of incremental field filter.


        :return: The incremental_field_name of this IncrementalFieldClause.
        :rtype: str
        """
        return self._incremental_field_name

    @incremental_field_name.setter
    def incremental_field_name(self, incremental_field_name):
        """
        Sets the incremental_field_name of this IncrementalFieldClause.
        Name of incremental field filter.


        :param incremental_field_name: The incremental_field_name of this IncrementalFieldClause.
        :type: str
        """
        self._incremental_field_name = incremental_field_name

    @property
    def incremental_field_value(self):
        """
        **[Required]** Gets the incremental_field_value of this IncrementalFieldClause.
        Value of incremental field filter.


        :return: The incremental_field_value of this IncrementalFieldClause.
        :rtype: dict(str, str)
        """
        return self._incremental_field_value

    @incremental_field_value.setter
    def incremental_field_value(self, incremental_field_value):
        """
        Sets the incremental_field_value of this IncrementalFieldClause.
        Value of incremental field filter.


        :param incremental_field_value: The incremental_field_value of this IncrementalFieldClause.
        :type: dict(str, str)
        """
        self._incremental_field_value = incremental_field_value

    @property
    def incremental_comparator(self):
        """
        **[Required]** Gets the incremental_comparator of this IncrementalFieldClause.
        Incremental comparator symbol.

        Allowed values for this property are: "LESSTHAN", "GREATERTHAN", "EQUALS", "LESSTHANEQUALS", "GREATERTHANEQUALS", "STARTSWITH", "CONTAINS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The incremental_comparator of this IncrementalFieldClause.
        :rtype: str
        """
        return self._incremental_comparator

    @incremental_comparator.setter
    def incremental_comparator(self, incremental_comparator):
        """
        Sets the incremental_comparator of this IncrementalFieldClause.
        Incremental comparator symbol.


        :param incremental_comparator: The incremental_comparator of this IncrementalFieldClause.
        :type: str
        """
        allowed_values = ["LESSTHAN", "GREATERTHAN", "EQUALS", "LESSTHANEQUALS", "GREATERTHANEQUALS", "STARTSWITH", "CONTAINS"]
        if not value_allowed_none_or_none_sentinel(incremental_comparator, allowed_values):
            incremental_comparator = 'UNKNOWN_ENUM_VALUE'
        self._incremental_comparator = incremental_comparator

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
