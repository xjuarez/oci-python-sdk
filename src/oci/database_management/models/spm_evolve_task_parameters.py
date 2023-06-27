# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SpmEvolveTaskParameters(object):
    """
    The set of parameters used in an SPM evolve task.
    """

    #: A constant which can be used with the alternate_plan_sources property of a SpmEvolveTaskParameters.
    #: This constant has a value of "AUTO"
    ALTERNATE_PLAN_SOURCES_AUTO = "AUTO"

    #: A constant which can be used with the alternate_plan_sources property of a SpmEvolveTaskParameters.
    #: This constant has a value of "AUTOMATIC_WORKLOAD_REPOSITORY"
    ALTERNATE_PLAN_SOURCES_AUTOMATIC_WORKLOAD_REPOSITORY = "AUTOMATIC_WORKLOAD_REPOSITORY"

    #: A constant which can be used with the alternate_plan_sources property of a SpmEvolveTaskParameters.
    #: This constant has a value of "CURSOR_CACHE"
    ALTERNATE_PLAN_SOURCES_CURSOR_CACHE = "CURSOR_CACHE"

    #: A constant which can be used with the alternate_plan_sources property of a SpmEvolveTaskParameters.
    #: This constant has a value of "SQL_TUNING_SET"
    ALTERNATE_PLAN_SOURCES_SQL_TUNING_SET = "SQL_TUNING_SET"

    #: A constant which can be used with the alternate_plan_baselines property of a SpmEvolveTaskParameters.
    #: This constant has a value of "AUTO"
    ALTERNATE_PLAN_BASELINES_AUTO = "AUTO"

    #: A constant which can be used with the alternate_plan_baselines property of a SpmEvolveTaskParameters.
    #: This constant has a value of "EXISTING"
    ALTERNATE_PLAN_BASELINES_EXISTING = "EXISTING"

    #: A constant which can be used with the alternate_plan_baselines property of a SpmEvolveTaskParameters.
    #: This constant has a value of "NEW"
    ALTERNATE_PLAN_BASELINES_NEW = "NEW"

    def __init__(self, **kwargs):
        """
        Initializes a new SpmEvolveTaskParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alternate_plan_sources:
            The value to assign to the alternate_plan_sources property of this SpmEvolveTaskParameters.
            Allowed values for items in this list are: "AUTO", "AUTOMATIC_WORKLOAD_REPOSITORY", "CURSOR_CACHE", "SQL_TUNING_SET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type alternate_plan_sources: list[str]

        :param alternate_plan_baselines:
            The value to assign to the alternate_plan_baselines property of this SpmEvolveTaskParameters.
            Allowed values for items in this list are: "AUTO", "EXISTING", "NEW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type alternate_plan_baselines: list[str]

        :param alternate_plan_limit:
            The value to assign to the alternate_plan_limit property of this SpmEvolveTaskParameters.
        :type alternate_plan_limit: int

        :param are_plans_auto_accepted:
            The value to assign to the are_plans_auto_accepted property of this SpmEvolveTaskParameters.
        :type are_plans_auto_accepted: bool

        :param allowed_time_limit:
            The value to assign to the allowed_time_limit property of this SpmEvolveTaskParameters.
        :type allowed_time_limit: int

        """
        self.swagger_types = {
            'alternate_plan_sources': 'list[str]',
            'alternate_plan_baselines': 'list[str]',
            'alternate_plan_limit': 'int',
            'are_plans_auto_accepted': 'bool',
            'allowed_time_limit': 'int'
        }

        self.attribute_map = {
            'alternate_plan_sources': 'alternatePlanSources',
            'alternate_plan_baselines': 'alternatePlanBaselines',
            'alternate_plan_limit': 'alternatePlanLimit',
            'are_plans_auto_accepted': 'arePlansAutoAccepted',
            'allowed_time_limit': 'allowedTimeLimit'
        }

        self._alternate_plan_sources = None
        self._alternate_plan_baselines = None
        self._alternate_plan_limit = None
        self._are_plans_auto_accepted = None
        self._allowed_time_limit = None

    @property
    def alternate_plan_sources(self):
        """
        Gets the alternate_plan_sources of this SpmEvolveTaskParameters.
        Determines which sources to search for additional plans.

        Allowed values for items in this list are: "AUTO", "AUTOMATIC_WORKLOAD_REPOSITORY", "CURSOR_CACHE", "SQL_TUNING_SET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The alternate_plan_sources of this SpmEvolveTaskParameters.
        :rtype: list[str]
        """
        return self._alternate_plan_sources

    @alternate_plan_sources.setter
    def alternate_plan_sources(self, alternate_plan_sources):
        """
        Sets the alternate_plan_sources of this SpmEvolveTaskParameters.
        Determines which sources to search for additional plans.


        :param alternate_plan_sources: The alternate_plan_sources of this SpmEvolveTaskParameters.
        :type: list[str]
        """
        allowed_values = ["AUTO", "AUTOMATIC_WORKLOAD_REPOSITORY", "CURSOR_CACHE", "SQL_TUNING_SET"]
        if alternate_plan_sources:
            alternate_plan_sources[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in alternate_plan_sources]
        self._alternate_plan_sources = alternate_plan_sources

    @property
    def alternate_plan_baselines(self):
        """
        Gets the alternate_plan_baselines of this SpmEvolveTaskParameters.
        Determines which alternative plans should be loaded.

        Allowed values for items in this list are: "AUTO", "EXISTING", "NEW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The alternate_plan_baselines of this SpmEvolveTaskParameters.
        :rtype: list[str]
        """
        return self._alternate_plan_baselines

    @alternate_plan_baselines.setter
    def alternate_plan_baselines(self, alternate_plan_baselines):
        """
        Sets the alternate_plan_baselines of this SpmEvolveTaskParameters.
        Determines which alternative plans should be loaded.


        :param alternate_plan_baselines: The alternate_plan_baselines of this SpmEvolveTaskParameters.
        :type: list[str]
        """
        allowed_values = ["AUTO", "EXISTING", "NEW"]
        if alternate_plan_baselines:
            alternate_plan_baselines[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in alternate_plan_baselines]
        self._alternate_plan_baselines = alternate_plan_baselines

    @property
    def alternate_plan_limit(self):
        """
        Gets the alternate_plan_limit of this SpmEvolveTaskParameters.
        Specifies the maximum number of plans to load in total (that is, not
        the limit for each SQL statement). A value of zero indicates `UNLIMITED`
        number of plans.


        :return: The alternate_plan_limit of this SpmEvolveTaskParameters.
        :rtype: int
        """
        return self._alternate_plan_limit

    @alternate_plan_limit.setter
    def alternate_plan_limit(self, alternate_plan_limit):
        """
        Sets the alternate_plan_limit of this SpmEvolveTaskParameters.
        Specifies the maximum number of plans to load in total (that is, not
        the limit for each SQL statement). A value of zero indicates `UNLIMITED`
        number of plans.


        :param alternate_plan_limit: The alternate_plan_limit of this SpmEvolveTaskParameters.
        :type: int
        """
        self._alternate_plan_limit = alternate_plan_limit

    @property
    def are_plans_auto_accepted(self):
        """
        Gets the are_plans_auto_accepted of this SpmEvolveTaskParameters.
        Specifies whether to accept recommended plans automatically.


        :return: The are_plans_auto_accepted of this SpmEvolveTaskParameters.
        :rtype: bool
        """
        return self._are_plans_auto_accepted

    @are_plans_auto_accepted.setter
    def are_plans_auto_accepted(self, are_plans_auto_accepted):
        """
        Sets the are_plans_auto_accepted of this SpmEvolveTaskParameters.
        Specifies whether to accept recommended plans automatically.


        :param are_plans_auto_accepted: The are_plans_auto_accepted of this SpmEvolveTaskParameters.
        :type: bool
        """
        self._are_plans_auto_accepted = are_plans_auto_accepted

    @property
    def allowed_time_limit(self):
        """
        Gets the allowed_time_limit of this SpmEvolveTaskParameters.
        The global time limit in seconds. This is the total time allowed for the task.


        :return: The allowed_time_limit of this SpmEvolveTaskParameters.
        :rtype: int
        """
        return self._allowed_time_limit

    @allowed_time_limit.setter
    def allowed_time_limit(self, allowed_time_limit):
        """
        Sets the allowed_time_limit of this SpmEvolveTaskParameters.
        The global time limit in seconds. This is the total time allowed for the task.


        :param allowed_time_limit: The allowed_time_limit of this SpmEvolveTaskParameters.
        :type: int
        """
        self._allowed_time_limit = allowed_time_limit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
