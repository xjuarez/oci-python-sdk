# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizedMetricData(object):
    """
    The recorded metric value at a specific timestamp.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizedMetricData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sample_time:
            The value to assign to the sample_time property of this SummarizedMetricData.
        :type sample_time: datetime

        :param resolution:
            The value to assign to the resolution property of this SummarizedMetricData.
        :type resolution: str

        :param dimensions:
            The value to assign to the dimensions property of this SummarizedMetricData.
        :type dimensions: dict(str, DimensionValue)

        :param aggregation_method:
            The value to assign to the aggregation_method property of this SummarizedMetricData.
        :type aggregation_method: str

        :param aggregated_value:
            The value to assign to the aggregated_value property of this SummarizedMetricData.
        :type aggregated_value: float

        """
        self.swagger_types = {
            'sample_time': 'datetime',
            'resolution': 'str',
            'dimensions': 'dict(str, DimensionValue)',
            'aggregation_method': 'str',
            'aggregated_value': 'float'
        }

        self.attribute_map = {
            'sample_time': 'sampleTime',
            'resolution': 'resolution',
            'dimensions': 'dimensions',
            'aggregation_method': 'aggregationMethod',
            'aggregated_value': 'aggregatedValue'
        }

        self._sample_time = None
        self._resolution = None
        self._dimensions = None
        self._aggregation_method = None
        self._aggregated_value = None

    @property
    def sample_time(self):
        """
        Gets the sample_time of this SummarizedMetricData.
        The time at which the metric data was recorded.


        :return: The sample_time of this SummarizedMetricData.
        :rtype: datetime
        """
        return self._sample_time

    @sample_time.setter
    def sample_time(self, sample_time):
        """
        Sets the sample_time of this SummarizedMetricData.
        The time at which the metric data was recorded.


        :param sample_time: The sample_time of this SummarizedMetricData.
        :type: datetime
        """
        self._sample_time = sample_time

    @property
    def resolution(self):
        """
        Gets the resolution of this SummarizedMetricData.
        The duration over which the metric data is aggregated. Supported values: `1m`-`60m`, `1h`-`24h`, `1d`.


        :return: The resolution of this SummarizedMetricData.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this SummarizedMetricData.
        The duration over which the metric data is aggregated. Supported values: `1m`-`60m`, `1h`-`24h`, `1d`.


        :param resolution: The resolution of this SummarizedMetricData.
        :type: str
        """
        self._resolution = resolution

    @property
    def dimensions(self):
        """
        Gets the dimensions of this SummarizedMetricData.
        Qualifiers provided in the definition of the returned metric. Available dimensions vary by metric namespace.


        :return: The dimensions of this SummarizedMetricData.
        :rtype: dict(str, DimensionValue)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this SummarizedMetricData.
        Qualifiers provided in the definition of the returned metric. Available dimensions vary by metric namespace.


        :param dimensions: The dimensions of this SummarizedMetricData.
        :type: dict(str, DimensionValue)
        """
        self._dimensions = dimensions

    @property
    def aggregation_method(self):
        """
        Gets the aggregation_method of this SummarizedMetricData.
        The aggregation method used for aggregating the metric values.  The aggregation method depends on the metric itself.


        :return: The aggregation_method of this SummarizedMetricData.
        :rtype: str
        """
        return self._aggregation_method

    @aggregation_method.setter
    def aggregation_method(self, aggregation_method):
        """
        Sets the aggregation_method of this SummarizedMetricData.
        The aggregation method used for aggregating the metric values.  The aggregation method depends on the metric itself.


        :param aggregation_method: The aggregation_method of this SummarizedMetricData.
        :type: str
        """
        self._aggregation_method = aggregation_method

    @property
    def aggregated_value(self):
        """
        Gets the aggregated_value of this SummarizedMetricData.
        The aggregated metric value for the specified request.


        :return: The aggregated_value of this SummarizedMetricData.
        :rtype: float
        """
        return self._aggregated_value

    @aggregated_value.setter
    def aggregated_value(self, aggregated_value):
        """
        Sets the aggregated_value of this SummarizedMetricData.
        The aggregated metric value for the specified request.


        :param aggregated_value: The aggregated_value of this SummarizedMetricData.
        :type: float
        """
        self._aggregated_value = aggregated_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
