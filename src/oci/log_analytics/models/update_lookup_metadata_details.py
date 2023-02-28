# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLookupMetadataDetails(object):
    """
    UpdateLookupMetadataDetails
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLookupMetadataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_match_value:
            The value to assign to the default_match_value property of this UpdateLookupMetadataDetails.
        :type default_match_value: str

        :param description:
            The value to assign to the description property of this UpdateLookupMetadataDetails.
        :type description: str

        :param fields:
            The value to assign to the fields property of this UpdateLookupMetadataDetails.
        :type fields: list[oci.log_analytics.models.LogAnalyticsLookupFields]

        :param max_matches:
            The value to assign to the max_matches property of this UpdateLookupMetadataDetails.
        :type max_matches: int

        :param categories:
            The value to assign to the categories property of this UpdateLookupMetadataDetails.
        :type categories: list[oci.log_analytics.models.LogAnalyticsCategory]

        """
        self.swagger_types = {
            'default_match_value': 'str',
            'description': 'str',
            'fields': 'list[LogAnalyticsLookupFields]',
            'max_matches': 'int',
            'categories': 'list[LogAnalyticsCategory]'
        }

        self.attribute_map = {
            'default_match_value': 'defaultMatchValue',
            'description': 'description',
            'fields': 'fields',
            'max_matches': 'maxMatches',
            'categories': 'categories'
        }

        self._default_match_value = None
        self._description = None
        self._fields = None
        self._max_matches = None
        self._categories = None

    @property
    def default_match_value(self):
        """
        Gets the default_match_value of this UpdateLookupMetadataDetails.
        The default match value.


        :return: The default_match_value of this UpdateLookupMetadataDetails.
        :rtype: str
        """
        return self._default_match_value

    @default_match_value.setter
    def default_match_value(self, default_match_value):
        """
        Sets the default_match_value of this UpdateLookupMetadataDetails.
        The default match value.


        :param default_match_value: The default_match_value of this UpdateLookupMetadataDetails.
        :type: str
        """
        self._default_match_value = default_match_value

    @property
    def description(self):
        """
        Gets the description of this UpdateLookupMetadataDetails.
        The lookup description.


        :return: The description of this UpdateLookupMetadataDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateLookupMetadataDetails.
        The lookup description.


        :param description: The description of this UpdateLookupMetadataDetails.
        :type: str
        """
        self._description = description

    @property
    def fields(self):
        """
        Gets the fields of this UpdateLookupMetadataDetails.
        The lookup fields.


        :return: The fields of this UpdateLookupMetadataDetails.
        :rtype: list[oci.log_analytics.models.LogAnalyticsLookupFields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this UpdateLookupMetadataDetails.
        The lookup fields.


        :param fields: The fields of this UpdateLookupMetadataDetails.
        :type: list[oci.log_analytics.models.LogAnalyticsLookupFields]
        """
        self._fields = fields

    @property
    def max_matches(self):
        """
        Gets the max_matches of this UpdateLookupMetadataDetails.
        The maximum number of matches.


        :return: The max_matches of this UpdateLookupMetadataDetails.
        :rtype: int
        """
        return self._max_matches

    @max_matches.setter
    def max_matches(self, max_matches):
        """
        Sets the max_matches of this UpdateLookupMetadataDetails.
        The maximum number of matches.


        :param max_matches: The max_matches of this UpdateLookupMetadataDetails.
        :type: int
        """
        self._max_matches = max_matches

    @property
    def categories(self):
        """
        Gets the categories of this UpdateLookupMetadataDetails.
        An array of categories to assign to the lookup. Specifying the name attribute for each category would suffice.
        Oracle-defined category assignments cannot be removed.


        :return: The categories of this UpdateLookupMetadataDetails.
        :rtype: list[oci.log_analytics.models.LogAnalyticsCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this UpdateLookupMetadataDetails.
        An array of categories to assign to the lookup. Specifying the name attribute for each category would suffice.
        Oracle-defined category assignments cannot be removed.


        :param categories: The categories of this UpdateLookupMetadataDetails.
        :type: list[oci.log_analytics.models.LogAnalyticsCategory]
        """
        self._categories = categories

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
