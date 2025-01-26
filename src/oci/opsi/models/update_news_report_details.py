# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNewsReportDetails(object):
    """
    The information about the news report to be updated.
    """

    #: A constant which can be used with the status property of a UpdateNewsReportDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a UpdateNewsReportDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateNewsReportDetails.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the news_frequency property of a UpdateNewsReportDetails.
    #: This constant has a value of "WEEKLY"
    NEWS_FREQUENCY_WEEKLY = "WEEKLY"

    #: A constant which can be used with the locale property of a UpdateNewsReportDetails.
    #: This constant has a value of "EN"
    LOCALE_EN = "EN"

    #: A constant which can be used with the day_of_week property of a UpdateNewsReportDetails.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a UpdateNewsReportDetails.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a UpdateNewsReportDetails.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a UpdateNewsReportDetails.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a UpdateNewsReportDetails.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a UpdateNewsReportDetails.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    #: A constant which can be used with the day_of_week property of a UpdateNewsReportDetails.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNewsReportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateNewsReportDetails.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param news_frequency:
            The value to assign to the news_frequency property of this UpdateNewsReportDetails.
            Allowed values for this property are: "WEEKLY"
        :type news_frequency: str

        :param locale:
            The value to assign to the locale property of this UpdateNewsReportDetails.
            Allowed values for this property are: "EN"
        :type locale: str

        :param content_types:
            The value to assign to the content_types property of this UpdateNewsReportDetails.
        :type content_types: oci.opsi.models.NewsContentTypes

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this UpdateNewsReportDetails.
        :type ons_topic_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNewsReportDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNewsReportDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param name:
            The value to assign to the name property of this UpdateNewsReportDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateNewsReportDetails.
        :type description: str

        :param day_of_week:
            The value to assign to the day_of_week property of this UpdateNewsReportDetails.
            Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
        :type day_of_week: str

        :param are_child_compartments_included:
            The value to assign to the are_child_compartments_included property of this UpdateNewsReportDetails.
        :type are_child_compartments_included: bool

        """
        self.swagger_types = {
            'status': 'str',
            'news_frequency': 'str',
            'locale': 'str',
            'content_types': 'NewsContentTypes',
            'ons_topic_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'name': 'str',
            'description': 'str',
            'day_of_week': 'str',
            'are_child_compartments_included': 'bool'
        }

        self.attribute_map = {
            'status': 'status',
            'news_frequency': 'newsFrequency',
            'locale': 'locale',
            'content_types': 'contentTypes',
            'ons_topic_id': 'onsTopicId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'name': 'name',
            'description': 'description',
            'day_of_week': 'dayOfWeek',
            'are_child_compartments_included': 'areChildCompartmentsIncluded'
        }

        self._status = None
        self._news_frequency = None
        self._locale = None
        self._content_types = None
        self._ons_topic_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._name = None
        self._description = None
        self._day_of_week = None
        self._are_child_compartments_included = None

    @property
    def status(self):
        """
        Gets the status of this UpdateNewsReportDetails.
        Defines if the news report will be enabled or disabled.

        Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"


        :return: The status of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateNewsReportDetails.
        Defines if the news report will be enabled or disabled.


        :param status: The status of this UpdateNewsReportDetails.
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                f"Invalid value for `status`, must be None or one of {allowed_values}"
            )
        self._status = status

    @property
    def news_frequency(self):
        """
        Gets the news_frequency of this UpdateNewsReportDetails.
        News report frequency.

        Allowed values for this property are: "WEEKLY"


        :return: The news_frequency of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._news_frequency

    @news_frequency.setter
    def news_frequency(self, news_frequency):
        """
        Sets the news_frequency of this UpdateNewsReportDetails.
        News report frequency.


        :param news_frequency: The news_frequency of this UpdateNewsReportDetails.
        :type: str
        """
        allowed_values = ["WEEKLY"]
        if not value_allowed_none_or_none_sentinel(news_frequency, allowed_values):
            raise ValueError(
                f"Invalid value for `news_frequency`, must be None or one of {allowed_values}"
            )
        self._news_frequency = news_frequency

    @property
    def locale(self):
        """
        Gets the locale of this UpdateNewsReportDetails.
        Language of the news report.

        Allowed values for this property are: "EN"


        :return: The locale of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this UpdateNewsReportDetails.
        Language of the news report.


        :param locale: The locale of this UpdateNewsReportDetails.
        :type: str
        """
        allowed_values = ["EN"]
        if not value_allowed_none_or_none_sentinel(locale, allowed_values):
            raise ValueError(
                f"Invalid value for `locale`, must be None or one of {allowed_values}"
            )
        self._locale = locale

    @property
    def content_types(self):
        """
        Gets the content_types of this UpdateNewsReportDetails.

        :return: The content_types of this UpdateNewsReportDetails.
        :rtype: oci.opsi.models.NewsContentTypes
        """
        return self._content_types

    @content_types.setter
    def content_types(self, content_types):
        """
        Sets the content_types of this UpdateNewsReportDetails.

        :param content_types: The content_types of this UpdateNewsReportDetails.
        :type: oci.opsi.models.NewsContentTypes
        """
        self._content_types = content_types

    @property
    def ons_topic_id(self):
        """
        Gets the ons_topic_id of this UpdateNewsReportDetails.
        The `OCID`__ of the ONS topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The ons_topic_id of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this UpdateNewsReportDetails.
        The `OCID`__ of the ONS topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param ons_topic_id: The ons_topic_id of this UpdateNewsReportDetails.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNewsReportDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateNewsReportDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNewsReportDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateNewsReportDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNewsReportDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateNewsReportDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNewsReportDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateNewsReportDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def name(self):
        """
        Gets the name of this UpdateNewsReportDetails.
        The news report name.


        :return: The name of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateNewsReportDetails.
        The news report name.


        :param name: The name of this UpdateNewsReportDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateNewsReportDetails.
        The description of the news report.


        :return: The description of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateNewsReportDetails.
        The description of the news report.


        :param description: The description of this UpdateNewsReportDetails.
        :type: str
        """
        self._description = description

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this UpdateNewsReportDetails.
        Day of the week in which the news report will be sent if the frequency is set to WEEKLY.

        Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"


        :return: The day_of_week of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this UpdateNewsReportDetails.
        Day of the week in which the news report will be sent if the frequency is set to WEEKLY.


        :param day_of_week: The day_of_week of this UpdateNewsReportDetails.
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            raise ValueError(
                f"Invalid value for `day_of_week`, must be None or one of {allowed_values}"
            )
        self._day_of_week = day_of_week

    @property
    def are_child_compartments_included(self):
        """
        Gets the are_child_compartments_included of this UpdateNewsReportDetails.
        A flag to consider the resources within a given compartment and all sub-compartments.


        :return: The are_child_compartments_included of this UpdateNewsReportDetails.
        :rtype: bool
        """
        return self._are_child_compartments_included

    @are_child_compartments_included.setter
    def are_child_compartments_included(self, are_child_compartments_included):
        """
        Sets the are_child_compartments_included of this UpdateNewsReportDetails.
        A flag to consider the resources within a given compartment and all sub-compartments.


        :param are_child_compartments_included: The are_child_compartments_included of this UpdateNewsReportDetails.
        :type: bool
        """
        self._are_child_compartments_included = are_child_compartments_included

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
