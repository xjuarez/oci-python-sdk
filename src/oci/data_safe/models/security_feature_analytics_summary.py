# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityFeatureAnalyticsSummary(object):
    """
    The summary of database security feature analytics data.
    """

    #: A constant which can be used with the metric_name property of a SecurityFeatureAnalyticsSummary.
    #: This constant has a value of "SECURITY_FEATURE_STATS"
    METRIC_NAME_SECURITY_FEATURE_STATS = "SECURITY_FEATURE_STATS"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityFeatureAnalyticsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this SecurityFeatureAnalyticsSummary.
            Allowed values for this property are: "SECURITY_FEATURE_STATS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_name: str

        :param dimensions:
            The value to assign to the dimensions property of this SecurityFeatureAnalyticsSummary.
        :type dimensions: oci.data_safe.models.SecurityFeatureAnalyticsDimensions

        :param count:
            The value to assign to the count property of this SecurityFeatureAnalyticsSummary.
        :type count: int

        """
        self.swagger_types = {
            'metric_name': 'str',
            'dimensions': 'SecurityFeatureAnalyticsDimensions',
            'count': 'int'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'dimensions': 'dimensions',
            'count': 'count'
        }

        self._metric_name = None
        self._dimensions = None
        self._count = None

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this SecurityFeatureAnalyticsSummary.
        The name of the aggregation metric.

        Allowed values for this property are: "SECURITY_FEATURE_STATS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_name of this SecurityFeatureAnalyticsSummary.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this SecurityFeatureAnalyticsSummary.
        The name of the aggregation metric.


        :param metric_name: The metric_name of this SecurityFeatureAnalyticsSummary.
        :type: str
        """
        allowed_values = ["SECURITY_FEATURE_STATS"]
        if not value_allowed_none_or_none_sentinel(metric_name, allowed_values):
            metric_name = 'UNKNOWN_ENUM_VALUE'
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """
        Gets the dimensions of this SecurityFeatureAnalyticsSummary.

        :return: The dimensions of this SecurityFeatureAnalyticsSummary.
        :rtype: oci.data_safe.models.SecurityFeatureAnalyticsDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this SecurityFeatureAnalyticsSummary.

        :param dimensions: The dimensions of this SecurityFeatureAnalyticsSummary.
        :type: oci.data_safe.models.SecurityFeatureAnalyticsDimensions
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        **[Required]** Gets the count of this SecurityFeatureAnalyticsSummary.
        The total count for the aggregation metric.


        :return: The count of this SecurityFeatureAnalyticsSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SecurityFeatureAnalyticsSummary.
        The total count for the aggregation metric.


        :param count: The count of this SecurityFeatureAnalyticsSummary.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
