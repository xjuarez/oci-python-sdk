# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Preferences(object):
    """
    Preferences to send notifications on the fleet activities
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Preferences object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param on_upcoming_schedule:
            The value to assign to the on_upcoming_schedule property of this Preferences.
        :type on_upcoming_schedule: bool

        :param on_job_failure:
            The value to assign to the on_job_failure property of this Preferences.
        :type on_job_failure: bool

        :param on_topology_modification:
            The value to assign to the on_topology_modification property of this Preferences.
        :type on_topology_modification: bool

        """
        self.swagger_types = {
            'on_upcoming_schedule': 'bool',
            'on_job_failure': 'bool',
            'on_topology_modification': 'bool'
        }

        self.attribute_map = {
            'on_upcoming_schedule': 'onUpcomingSchedule',
            'on_job_failure': 'onJobFailure',
            'on_topology_modification': 'onTopologyModification'
        }

        self._on_upcoming_schedule = None
        self._on_job_failure = None
        self._on_topology_modification = None

    @property
    def on_upcoming_schedule(self):
        """
        Gets the on_upcoming_schedule of this Preferences.
        Enables notification on upcoming schedule.


        :return: The on_upcoming_schedule of this Preferences.
        :rtype: bool
        """
        return self._on_upcoming_schedule

    @on_upcoming_schedule.setter
    def on_upcoming_schedule(self, on_upcoming_schedule):
        """
        Sets the on_upcoming_schedule of this Preferences.
        Enables notification on upcoming schedule.


        :param on_upcoming_schedule: The on_upcoming_schedule of this Preferences.
        :type: bool
        """
        self._on_upcoming_schedule = on_upcoming_schedule

    @property
    def on_job_failure(self):
        """
        Gets the on_job_failure of this Preferences.
        Enables or disables notification on Job Failures.'


        :return: The on_job_failure of this Preferences.
        :rtype: bool
        """
        return self._on_job_failure

    @on_job_failure.setter
    def on_job_failure(self, on_job_failure):
        """
        Sets the on_job_failure of this Preferences.
        Enables or disables notification on Job Failures.'


        :param on_job_failure: The on_job_failure of this Preferences.
        :type: bool
        """
        self._on_job_failure = on_job_failure

    @property
    def on_topology_modification(self):
        """
        Gets the on_topology_modification of this Preferences.
        Enables or disables notification on Environment Fleet Topology Modification.


        :return: The on_topology_modification of this Preferences.
        :rtype: bool
        """
        return self._on_topology_modification

    @on_topology_modification.setter
    def on_topology_modification(self, on_topology_modification):
        """
        Sets the on_topology_modification of this Preferences.
        Enables or disables notification on Environment Fleet Topology Modification.


        :param on_topology_modification: The on_topology_modification of this Preferences.
        :type: bool
        """
        self._on_topology_modification = on_topology_modification

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
