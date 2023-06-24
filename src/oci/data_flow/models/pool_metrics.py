# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PoolMetrics(object):
    """
    A collection of metrics related to a particular pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PoolMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_last_started:
            The value to assign to the time_last_started property of this PoolMetrics.
        :type time_last_started: datetime

        :param time_last_stopped:
            The value to assign to the time_last_stopped property of this PoolMetrics.
        :type time_last_stopped: datetime

        :param time_last_used:
            The value to assign to the time_last_used property of this PoolMetrics.
        :type time_last_used: datetime

        :param time_last_metrics_updated:
            The value to assign to the time_last_metrics_updated property of this PoolMetrics.
        :type time_last_metrics_updated: datetime

        :param active_runs_count:
            The value to assign to the active_runs_count property of this PoolMetrics.
        :type active_runs_count: int

        :param actively_used_node_count:
            The value to assign to the actively_used_node_count property of this PoolMetrics.
        :type actively_used_node_count: list[oci.data_flow.models.NodeCount]

        """
        self.swagger_types = {
            'time_last_started': 'datetime',
            'time_last_stopped': 'datetime',
            'time_last_used': 'datetime',
            'time_last_metrics_updated': 'datetime',
            'active_runs_count': 'int',
            'actively_used_node_count': 'list[NodeCount]'
        }

        self.attribute_map = {
            'time_last_started': 'timeLastStarted',
            'time_last_stopped': 'timeLastStopped',
            'time_last_used': 'timeLastUsed',
            'time_last_metrics_updated': 'timeLastMetricsUpdated',
            'active_runs_count': 'activeRunsCount',
            'actively_used_node_count': 'activelyUsedNodeCount'
        }

        self._time_last_started = None
        self._time_last_stopped = None
        self._time_last_used = None
        self._time_last_metrics_updated = None
        self._active_runs_count = None
        self._actively_used_node_count = None

    @property
    def time_last_started(self):
        """
        Gets the time_last_started of this PoolMetrics.
        The last time this pool was started.


        :return: The time_last_started of this PoolMetrics.
        :rtype: datetime
        """
        return self._time_last_started

    @time_last_started.setter
    def time_last_started(self, time_last_started):
        """
        Sets the time_last_started of this PoolMetrics.
        The last time this pool was started.


        :param time_last_started: The time_last_started of this PoolMetrics.
        :type: datetime
        """
        self._time_last_started = time_last_started

    @property
    def time_last_stopped(self):
        """
        Gets the time_last_stopped of this PoolMetrics.
        The last time this pool was stopped.


        :return: The time_last_stopped of this PoolMetrics.
        :rtype: datetime
        """
        return self._time_last_stopped

    @time_last_stopped.setter
    def time_last_stopped(self, time_last_stopped):
        """
        Sets the time_last_stopped of this PoolMetrics.
        The last time this pool was stopped.


        :param time_last_stopped: The time_last_stopped of this PoolMetrics.
        :type: datetime
        """
        self._time_last_stopped = time_last_stopped

    @property
    def time_last_used(self):
        """
        Gets the time_last_used of this PoolMetrics.
        The last time a run used this pool.


        :return: The time_last_used of this PoolMetrics.
        :rtype: datetime
        """
        return self._time_last_used

    @time_last_used.setter
    def time_last_used(self, time_last_used):
        """
        Sets the time_last_used of this PoolMetrics.
        The last time a run used this pool.


        :param time_last_used: The time_last_used of this PoolMetrics.
        :type: datetime
        """
        self._time_last_used = time_last_used

    @property
    def time_last_metrics_updated(self):
        """
        Gets the time_last_metrics_updated of this PoolMetrics.
        The last time the mertics were updated for this.


        :return: The time_last_metrics_updated of this PoolMetrics.
        :rtype: datetime
        """
        return self._time_last_metrics_updated

    @time_last_metrics_updated.setter
    def time_last_metrics_updated(self, time_last_metrics_updated):
        """
        Sets the time_last_metrics_updated of this PoolMetrics.
        The last time the mertics were updated for this.


        :param time_last_metrics_updated: The time_last_metrics_updated of this PoolMetrics.
        :type: datetime
        """
        self._time_last_metrics_updated = time_last_metrics_updated

    @property
    def active_runs_count(self):
        """
        Gets the active_runs_count of this PoolMetrics.
        The number of runs that are currently running that are using this pool.


        :return: The active_runs_count of this PoolMetrics.
        :rtype: int
        """
        return self._active_runs_count

    @active_runs_count.setter
    def active_runs_count(self, active_runs_count):
        """
        Sets the active_runs_count of this PoolMetrics.
        The number of runs that are currently running that are using this pool.


        :param active_runs_count: The active_runs_count of this PoolMetrics.
        :type: int
        """
        self._active_runs_count = active_runs_count

    @property
    def actively_used_node_count(self):
        """
        Gets the actively_used_node_count of this PoolMetrics.
        A count of the nodes that are currently being used for each shape in this pool.


        :return: The actively_used_node_count of this PoolMetrics.
        :rtype: list[oci.data_flow.models.NodeCount]
        """
        return self._actively_used_node_count

    @actively_used_node_count.setter
    def actively_used_node_count(self, actively_used_node_count):
        """
        Sets the actively_used_node_count of this PoolMetrics.
        A count of the nodes that are currently being used for each shape in this pool.


        :param actively_used_node_count: The actively_used_node_count of this PoolMetrics.
        :type: list[oci.data_flow.models.NodeCount]
        """
        self._actively_used_node_count = actively_used_node_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
