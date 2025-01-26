# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NewsContentTypes(object):
    """
    Content types that the news report can handle.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NewsContentTypes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity_planning_resources:
            The value to assign to the capacity_planning_resources property of this NewsContentTypes.
        :type capacity_planning_resources: list[oci.opsi.models.NewsContentTypesResource]

        :param sql_insights_fleet_analysis_resources:
            The value to assign to the sql_insights_fleet_analysis_resources property of this NewsContentTypes.
        :type sql_insights_fleet_analysis_resources: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]

        :param sql_insights_plan_changes_resources:
            The value to assign to the sql_insights_plan_changes_resources property of this NewsContentTypes.
        :type sql_insights_plan_changes_resources: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]

        :param sql_insights_top_databases_resources:
            The value to assign to the sql_insights_top_databases_resources property of this NewsContentTypes.
        :type sql_insights_top_databases_resources: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]

        :param sql_insights_top_sql_by_insights_resources:
            The value to assign to the sql_insights_top_sql_by_insights_resources property of this NewsContentTypes.
        :type sql_insights_top_sql_by_insights_resources: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]

        :param sql_insights_top_sql_resources:
            The value to assign to the sql_insights_top_sql_resources property of this NewsContentTypes.
        :type sql_insights_top_sql_resources: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]

        :param sql_insights_performance_degradation_resources:
            The value to assign to the sql_insights_performance_degradation_resources property of this NewsContentTypes.
        :type sql_insights_performance_degradation_resources: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]

        """
        self.swagger_types = {
            'capacity_planning_resources': 'list[NewsContentTypesResource]',
            'sql_insights_fleet_analysis_resources': 'list[NewsSqlInsightsContentTypesResource]',
            'sql_insights_plan_changes_resources': 'list[NewsSqlInsightsContentTypesResource]',
            'sql_insights_top_databases_resources': 'list[NewsSqlInsightsContentTypesResource]',
            'sql_insights_top_sql_by_insights_resources': 'list[NewsSqlInsightsContentTypesResource]',
            'sql_insights_top_sql_resources': 'list[NewsSqlInsightsContentTypesResource]',
            'sql_insights_performance_degradation_resources': 'list[NewsSqlInsightsContentTypesResource]'
        }

        self.attribute_map = {
            'capacity_planning_resources': 'capacityPlanningResources',
            'sql_insights_fleet_analysis_resources': 'sqlInsightsFleetAnalysisResources',
            'sql_insights_plan_changes_resources': 'sqlInsightsPlanChangesResources',
            'sql_insights_top_databases_resources': 'sqlInsightsTopDatabasesResources',
            'sql_insights_top_sql_by_insights_resources': 'sqlInsightsTopSqlByInsightsResources',
            'sql_insights_top_sql_resources': 'sqlInsightsTopSqlResources',
            'sql_insights_performance_degradation_resources': 'sqlInsightsPerformanceDegradationResources'
        }

        self._capacity_planning_resources = None
        self._sql_insights_fleet_analysis_resources = None
        self._sql_insights_plan_changes_resources = None
        self._sql_insights_top_databases_resources = None
        self._sql_insights_top_sql_by_insights_resources = None
        self._sql_insights_top_sql_resources = None
        self._sql_insights_performance_degradation_resources = None

    @property
    def capacity_planning_resources(self):
        """
        Gets the capacity_planning_resources of this NewsContentTypes.
        Supported resources for capacity planning content type.


        :return: The capacity_planning_resources of this NewsContentTypes.
        :rtype: list[oci.opsi.models.NewsContentTypesResource]
        """
        return self._capacity_planning_resources

    @capacity_planning_resources.setter
    def capacity_planning_resources(self, capacity_planning_resources):
        """
        Sets the capacity_planning_resources of this NewsContentTypes.
        Supported resources for capacity planning content type.


        :param capacity_planning_resources: The capacity_planning_resources of this NewsContentTypes.
        :type: list[oci.opsi.models.NewsContentTypesResource]
        """
        self._capacity_planning_resources = capacity_planning_resources

    @property
    def sql_insights_fleet_analysis_resources(self):
        """
        Gets the sql_insights_fleet_analysis_resources of this NewsContentTypes.
        Supported resources for SQL insights - fleet analysis content type.


        :return: The sql_insights_fleet_analysis_resources of this NewsContentTypes.
        :rtype: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        return self._sql_insights_fleet_analysis_resources

    @sql_insights_fleet_analysis_resources.setter
    def sql_insights_fleet_analysis_resources(self, sql_insights_fleet_analysis_resources):
        """
        Sets the sql_insights_fleet_analysis_resources of this NewsContentTypes.
        Supported resources for SQL insights - fleet analysis content type.


        :param sql_insights_fleet_analysis_resources: The sql_insights_fleet_analysis_resources of this NewsContentTypes.
        :type: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        self._sql_insights_fleet_analysis_resources = sql_insights_fleet_analysis_resources

    @property
    def sql_insights_plan_changes_resources(self):
        """
        Gets the sql_insights_plan_changes_resources of this NewsContentTypes.
        Supported resources for SQL insights - plan changes content type.


        :return: The sql_insights_plan_changes_resources of this NewsContentTypes.
        :rtype: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        return self._sql_insights_plan_changes_resources

    @sql_insights_plan_changes_resources.setter
    def sql_insights_plan_changes_resources(self, sql_insights_plan_changes_resources):
        """
        Sets the sql_insights_plan_changes_resources of this NewsContentTypes.
        Supported resources for SQL insights - plan changes content type.


        :param sql_insights_plan_changes_resources: The sql_insights_plan_changes_resources of this NewsContentTypes.
        :type: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        self._sql_insights_plan_changes_resources = sql_insights_plan_changes_resources

    @property
    def sql_insights_top_databases_resources(self):
        """
        Gets the sql_insights_top_databases_resources of this NewsContentTypes.
        Supported resources for SQL insights - top databases content type.


        :return: The sql_insights_top_databases_resources of this NewsContentTypes.
        :rtype: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        return self._sql_insights_top_databases_resources

    @sql_insights_top_databases_resources.setter
    def sql_insights_top_databases_resources(self, sql_insights_top_databases_resources):
        """
        Sets the sql_insights_top_databases_resources of this NewsContentTypes.
        Supported resources for SQL insights - top databases content type.


        :param sql_insights_top_databases_resources: The sql_insights_top_databases_resources of this NewsContentTypes.
        :type: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        self._sql_insights_top_databases_resources = sql_insights_top_databases_resources

    @property
    def sql_insights_top_sql_by_insights_resources(self):
        """
        Gets the sql_insights_top_sql_by_insights_resources of this NewsContentTypes.
        Supported resources for SQL insights - top SQL by insights content type.


        :return: The sql_insights_top_sql_by_insights_resources of this NewsContentTypes.
        :rtype: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        return self._sql_insights_top_sql_by_insights_resources

    @sql_insights_top_sql_by_insights_resources.setter
    def sql_insights_top_sql_by_insights_resources(self, sql_insights_top_sql_by_insights_resources):
        """
        Sets the sql_insights_top_sql_by_insights_resources of this NewsContentTypes.
        Supported resources for SQL insights - top SQL by insights content type.


        :param sql_insights_top_sql_by_insights_resources: The sql_insights_top_sql_by_insights_resources of this NewsContentTypes.
        :type: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        self._sql_insights_top_sql_by_insights_resources = sql_insights_top_sql_by_insights_resources

    @property
    def sql_insights_top_sql_resources(self):
        """
        Gets the sql_insights_top_sql_resources of this NewsContentTypes.
        Supported resources for SQL insights - top SQL content type.


        :return: The sql_insights_top_sql_resources of this NewsContentTypes.
        :rtype: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        return self._sql_insights_top_sql_resources

    @sql_insights_top_sql_resources.setter
    def sql_insights_top_sql_resources(self, sql_insights_top_sql_resources):
        """
        Sets the sql_insights_top_sql_resources of this NewsContentTypes.
        Supported resources for SQL insights - top SQL content type.


        :param sql_insights_top_sql_resources: The sql_insights_top_sql_resources of this NewsContentTypes.
        :type: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        self._sql_insights_top_sql_resources = sql_insights_top_sql_resources

    @property
    def sql_insights_performance_degradation_resources(self):
        """
        Gets the sql_insights_performance_degradation_resources of this NewsContentTypes.
        Supported resources for SQL insights - performance degradation content type.


        :return: The sql_insights_performance_degradation_resources of this NewsContentTypes.
        :rtype: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        return self._sql_insights_performance_degradation_resources

    @sql_insights_performance_degradation_resources.setter
    def sql_insights_performance_degradation_resources(self, sql_insights_performance_degradation_resources):
        """
        Sets the sql_insights_performance_degradation_resources of this NewsContentTypes.
        Supported resources for SQL insights - performance degradation content type.


        :param sql_insights_performance_degradation_resources: The sql_insights_performance_degradation_resources of this NewsContentTypes.
        :type: list[oci.opsi.models.NewsSqlInsightsContentTypesResource]
        """
        self._sql_insights_performance_degradation_resources = sql_insights_performance_degradation_resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
