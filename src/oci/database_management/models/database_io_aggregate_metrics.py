# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseIOAggregateMetrics(object):
    """
    The database Input/Output metric details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseIOAggregateMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param iops:
            The value to assign to the iops property of this DatabaseIOAggregateMetrics.
        :type iops: list[oci.database_management.models.MetricDataPoint]

        :param io_throughput:
            The value to assign to the io_throughput property of this DatabaseIOAggregateMetrics.
        :type io_throughput: list[oci.database_management.models.MetricDataPoint]

        :param iops_statistics:
            The value to assign to the iops_statistics property of this DatabaseIOAggregateMetrics.
        :type iops_statistics: list[oci.database_management.models.MetricStatisticsDefinition]

        :param io_throughput_statistics:
            The value to assign to the io_throughput_statistics property of this DatabaseIOAggregateMetrics.
        :type io_throughput_statistics: list[oci.database_management.models.MetricStatisticsDefinition]

        """
        self.swagger_types = {
            'iops': 'list[MetricDataPoint]',
            'io_throughput': 'list[MetricDataPoint]',
            'iops_statistics': 'list[MetricStatisticsDefinition]',
            'io_throughput_statistics': 'list[MetricStatisticsDefinition]'
        }

        self.attribute_map = {
            'iops': 'iops',
            'io_throughput': 'ioThroughput',
            'iops_statistics': 'iopsStatistics',
            'io_throughput_statistics': 'ioThroughputStatistics'
        }

        self._iops = None
        self._io_throughput = None
        self._iops_statistics = None
        self._io_throughput_statistics = None

    @property
    def iops(self):
        """
        Gets the iops of this DatabaseIOAggregateMetrics.
        The Input/Output Operations Per Second metrics grouped by IOType for a specific Managed Database.


        :return: The iops of this DatabaseIOAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricDataPoint]
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """
        Sets the iops of this DatabaseIOAggregateMetrics.
        The Input/Output Operations Per Second metrics grouped by IOType for a specific Managed Database.


        :param iops: The iops of this DatabaseIOAggregateMetrics.
        :type: list[oci.database_management.models.MetricDataPoint]
        """
        self._iops = iops

    @property
    def io_throughput(self):
        """
        Gets the io_throughput of this DatabaseIOAggregateMetrics.
        The IOThroughput metrics grouped by IOType for a specific Managed Database.


        :return: The io_throughput of this DatabaseIOAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricDataPoint]
        """
        return self._io_throughput

    @io_throughput.setter
    def io_throughput(self, io_throughput):
        """
        Sets the io_throughput of this DatabaseIOAggregateMetrics.
        The IOThroughput metrics grouped by IOType for a specific Managed Database.


        :param io_throughput: The io_throughput of this DatabaseIOAggregateMetrics.
        :type: list[oci.database_management.models.MetricDataPoint]
        """
        self._io_throughput = io_throughput

    @property
    def iops_statistics(self):
        """
        Gets the iops_statistics of this DatabaseIOAggregateMetrics.
        The Input/Output metric statistics such as min, max, mean, lowerQuartile, and upperQuartile.


        :return: The iops_statistics of this DatabaseIOAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricStatisticsDefinition]
        """
        return self._iops_statistics

    @iops_statistics.setter
    def iops_statistics(self, iops_statistics):
        """
        Sets the iops_statistics of this DatabaseIOAggregateMetrics.
        The Input/Output metric statistics such as min, max, mean, lowerQuartile, and upperQuartile.


        :param iops_statistics: The iops_statistics of this DatabaseIOAggregateMetrics.
        :type: list[oci.database_management.models.MetricStatisticsDefinition]
        """
        self._iops_statistics = iops_statistics

    @property
    def io_throughput_statistics(self):
        """
        Gets the io_throughput_statistics of this DatabaseIOAggregateMetrics.
        The IOThroughput metric statistics such as min, max, mean, lowerQuartile, and upperQuartile.


        :return: The io_throughput_statistics of this DatabaseIOAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricStatisticsDefinition]
        """
        return self._io_throughput_statistics

    @io_throughput_statistics.setter
    def io_throughput_statistics(self, io_throughput_statistics):
        """
        Sets the io_throughput_statistics of this DatabaseIOAggregateMetrics.
        The IOThroughput metric statistics such as min, max, mean, lowerQuartile, and upperQuartile.


        :param io_throughput_statistics: The io_throughput_statistics of this DatabaseIOAggregateMetrics.
        :type: list[oci.database_management.models.MetricStatisticsDefinition]
        """
        self._io_throughput_statistics = io_throughput_statistics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
