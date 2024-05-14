# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsLookupFields(object):
    """
    LogAnalyticsLookupFields
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsLookupFields object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param common_field_name:
            The value to assign to the common_field_name property of this LogAnalyticsLookupFields.
        :type common_field_name: str

        :param default_match_value:
            The value to assign to the default_match_value property of this LogAnalyticsLookupFields.
        :type default_match_value: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsLookupFields.
        :type display_name: str

        :param is_common_field:
            The value to assign to the is_common_field property of this LogAnalyticsLookupFields.
        :type is_common_field: bool

        :param match_operator:
            The value to assign to the match_operator property of this LogAnalyticsLookupFields.
        :type match_operator: str

        :param name:
            The value to assign to the name property of this LogAnalyticsLookupFields.
        :type name: str

        :param position:
            The value to assign to the position property of this LogAnalyticsLookupFields.
        :type position: int

        """
        self.swagger_types = {
            'common_field_name': 'str',
            'default_match_value': 'str',
            'display_name': 'str',
            'is_common_field': 'bool',
            'match_operator': 'str',
            'name': 'str',
            'position': 'int'
        }

        self.attribute_map = {
            'common_field_name': 'commonFieldName',
            'default_match_value': 'defaultMatchValue',
            'display_name': 'displayName',
            'is_common_field': 'isCommonField',
            'match_operator': 'matchOperator',
            'name': 'name',
            'position': 'position'
        }

        self._common_field_name = None
        self._default_match_value = None
        self._display_name = None
        self._is_common_field = None
        self._match_operator = None
        self._name = None
        self._position = None

    @property
    def common_field_name(self):
        """
        Gets the common_field_name of this LogAnalyticsLookupFields.
        The common field name.


        :return: The common_field_name of this LogAnalyticsLookupFields.
        :rtype: str
        """
        return self._common_field_name

    @common_field_name.setter
    def common_field_name(self, common_field_name):
        """
        Sets the common_field_name of this LogAnalyticsLookupFields.
        The common field name.


        :param common_field_name: The common_field_name of this LogAnalyticsLookupFields.
        :type: str
        """
        self._common_field_name = common_field_name

    @property
    def default_match_value(self):
        """
        Gets the default_match_value of this LogAnalyticsLookupFields.
        The default match value.


        :return: The default_match_value of this LogAnalyticsLookupFields.
        :rtype: str
        """
        return self._default_match_value

    @default_match_value.setter
    def default_match_value(self, default_match_value):
        """
        Sets the default_match_value of this LogAnalyticsLookupFields.
        The default match value.


        :param default_match_value: The default_match_value of this LogAnalyticsLookupFields.
        :type: str
        """
        self._default_match_value = default_match_value

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsLookupFields.
        The display name.


        :return: The display_name of this LogAnalyticsLookupFields.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsLookupFields.
        The display name.


        :param display_name: The display_name of this LogAnalyticsLookupFields.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_common_field(self):
        """
        Gets the is_common_field of this LogAnalyticsLookupFields.
        A flag indicating whether or not the field is a common field.


        :return: The is_common_field of this LogAnalyticsLookupFields.
        :rtype: bool
        """
        return self._is_common_field

    @is_common_field.setter
    def is_common_field(self, is_common_field):
        """
        Sets the is_common_field of this LogAnalyticsLookupFields.
        A flag indicating whether or not the field is a common field.


        :param is_common_field: The is_common_field of this LogAnalyticsLookupFields.
        :type: bool
        """
        self._is_common_field = is_common_field

    @property
    def match_operator(self):
        """
        Gets the match_operator of this LogAnalyticsLookupFields.
        The match operator.


        :return: The match_operator of this LogAnalyticsLookupFields.
        :rtype: str
        """
        return self._match_operator

    @match_operator.setter
    def match_operator(self, match_operator):
        """
        Sets the match_operator of this LogAnalyticsLookupFields.
        The match operator.


        :param match_operator: The match_operator of this LogAnalyticsLookupFields.
        :type: str
        """
        self._match_operator = match_operator

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsLookupFields.
        The field name.


        :return: The name of this LogAnalyticsLookupFields.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsLookupFields.
        The field name.


        :param name: The name of this LogAnalyticsLookupFields.
        :type: str
        """
        self._name = name

    @property
    def position(self):
        """
        Gets the position of this LogAnalyticsLookupFields.
        The position.


        :return: The position of this LogAnalyticsLookupFields.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this LogAnalyticsLookupFields.
        The position.


        :param position: The position of this LogAnalyticsLookupFields.
        :type: int
        """
        self._position = position

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
