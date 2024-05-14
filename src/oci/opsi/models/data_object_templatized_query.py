# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .data_object_query import DataObjectQuery
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectTemplatizedQuery(DataObjectQuery):
    """
    Information required in a structured template to form and execute query on a data object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectTemplatizedQuery object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DataObjectTemplatizedQuery.query_type` attribute
        of this class is ``TEMPLATIZED_QUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_type:
            The value to assign to the query_type property of this DataObjectTemplatizedQuery.
            Allowed values for this property are: "TEMPLATIZED_QUERY", "STANDARD_QUERY"
        :type query_type: str

        :param bind_params:
            The value to assign to the bind_params property of this DataObjectTemplatizedQuery.
        :type bind_params: list[oci.opsi.models.DataObjectBindParameter]

        :param query_execution_timeout_in_seconds:
            The value to assign to the query_execution_timeout_in_seconds property of this DataObjectTemplatizedQuery.
        :type query_execution_timeout_in_seconds: float

        :param select_list:
            The value to assign to the select_list property of this DataObjectTemplatizedQuery.
        :type select_list: list[str]

        :param from_clause:
            The value to assign to the from_clause property of this DataObjectTemplatizedQuery.
        :type from_clause: str

        :param where_conditions_list:
            The value to assign to the where_conditions_list property of this DataObjectTemplatizedQuery.
        :type where_conditions_list: list[str]

        :param group_by_list:
            The value to assign to the group_by_list property of this DataObjectTemplatizedQuery.
        :type group_by_list: list[str]

        :param having_conditions_list:
            The value to assign to the having_conditions_list property of this DataObjectTemplatizedQuery.
        :type having_conditions_list: list[str]

        :param order_by_list:
            The value to assign to the order_by_list property of this DataObjectTemplatizedQuery.
        :type order_by_list: list[str]

        :param time_filters:
            The value to assign to the time_filters property of this DataObjectTemplatizedQuery.
        :type time_filters: oci.opsi.models.DataObjectQueryTimeFilters

        """
        self.swagger_types = {
            'query_type': 'str',
            'bind_params': 'list[DataObjectBindParameter]',
            'query_execution_timeout_in_seconds': 'float',
            'select_list': 'list[str]',
            'from_clause': 'str',
            'where_conditions_list': 'list[str]',
            'group_by_list': 'list[str]',
            'having_conditions_list': 'list[str]',
            'order_by_list': 'list[str]',
            'time_filters': 'DataObjectQueryTimeFilters'
        }

        self.attribute_map = {
            'query_type': 'queryType',
            'bind_params': 'bindParams',
            'query_execution_timeout_in_seconds': 'queryExecutionTimeoutInSeconds',
            'select_list': 'selectList',
            'from_clause': 'fromClause',
            'where_conditions_list': 'whereConditionsList',
            'group_by_list': 'groupByList',
            'having_conditions_list': 'havingConditionsList',
            'order_by_list': 'orderByList',
            'time_filters': 'timeFilters'
        }

        self._query_type = None
        self._bind_params = None
        self._query_execution_timeout_in_seconds = None
        self._select_list = None
        self._from_clause = None
        self._where_conditions_list = None
        self._group_by_list = None
        self._having_conditions_list = None
        self._order_by_list = None
        self._time_filters = None
        self._query_type = 'TEMPLATIZED_QUERY'

    @property
    def select_list(self):
        """
        Gets the select_list of this DataObjectTemplatizedQuery.
        List of items to be added into the SELECT clause of the query; items will be added with comma separation.


        :return: The select_list of this DataObjectTemplatizedQuery.
        :rtype: list[str]
        """
        return self._select_list

    @select_list.setter
    def select_list(self, select_list):
        """
        Sets the select_list of this DataObjectTemplatizedQuery.
        List of items to be added into the SELECT clause of the query; items will be added with comma separation.


        :param select_list: The select_list of this DataObjectTemplatizedQuery.
        :type: list[str]
        """
        self._select_list = select_list

    @property
    def from_clause(self):
        """
        Gets the from_clause of this DataObjectTemplatizedQuery.
        Unique data object name that will be added into the FROM clause of the query, just like a view name in FROM clause.
        - Use actual name of the data objects (e.g: tables, views) in case of Warehouse (e.g: Awr hub) data objects query. SCHEMA.VIEW name syntax can also be used here.
        e.g: SYS.DBA_HIST_SNAPSHOT or DBA_HIST_SNAPSHOT
        - Use name of the data object (e.g: SQL_STATS_DO) in case of OPSI data objects. Identifier of the OPSI data object cannot be used here.


        :return: The from_clause of this DataObjectTemplatizedQuery.
        :rtype: str
        """
        return self._from_clause

    @from_clause.setter
    def from_clause(self, from_clause):
        """
        Sets the from_clause of this DataObjectTemplatizedQuery.
        Unique data object name that will be added into the FROM clause of the query, just like a view name in FROM clause.
        - Use actual name of the data objects (e.g: tables, views) in case of Warehouse (e.g: Awr hub) data objects query. SCHEMA.VIEW name syntax can also be used here.
        e.g: SYS.DBA_HIST_SNAPSHOT or DBA_HIST_SNAPSHOT
        - Use name of the data object (e.g: SQL_STATS_DO) in case of OPSI data objects. Identifier of the OPSI data object cannot be used here.


        :param from_clause: The from_clause of this DataObjectTemplatizedQuery.
        :type: str
        """
        self._from_clause = from_clause

    @property
    def where_conditions_list(self):
        """
        Gets the where_conditions_list of this DataObjectTemplatizedQuery.
        List of items to be added into the WHERE clause of the query; items will be added with AND separation.
        Item can contain a single condition or multiple conditions.
        Single condition e.g:  \"optimizer_mode='mode1'\"
        Multiple conditions e.g: (module='module1' OR module='module2')


        :return: The where_conditions_list of this DataObjectTemplatizedQuery.
        :rtype: list[str]
        """
        return self._where_conditions_list

    @where_conditions_list.setter
    def where_conditions_list(self, where_conditions_list):
        """
        Sets the where_conditions_list of this DataObjectTemplatizedQuery.
        List of items to be added into the WHERE clause of the query; items will be added with AND separation.
        Item can contain a single condition or multiple conditions.
        Single condition e.g:  \"optimizer_mode='mode1'\"
        Multiple conditions e.g: (module='module1' OR module='module2')


        :param where_conditions_list: The where_conditions_list of this DataObjectTemplatizedQuery.
        :type: list[str]
        """
        self._where_conditions_list = where_conditions_list

    @property
    def group_by_list(self):
        """
        Gets the group_by_list of this DataObjectTemplatizedQuery.
        List of items to be added into the GROUP BY clause of the query; items will be added with comma separation.


        :return: The group_by_list of this DataObjectTemplatizedQuery.
        :rtype: list[str]
        """
        return self._group_by_list

    @group_by_list.setter
    def group_by_list(self, group_by_list):
        """
        Sets the group_by_list of this DataObjectTemplatizedQuery.
        List of items to be added into the GROUP BY clause of the query; items will be added with comma separation.


        :param group_by_list: The group_by_list of this DataObjectTemplatizedQuery.
        :type: list[str]
        """
        self._group_by_list = group_by_list

    @property
    def having_conditions_list(self):
        """
        Gets the having_conditions_list of this DataObjectTemplatizedQuery.
        List of items to be added into the HAVING clause of the query; items will be added with AND separation.


        :return: The having_conditions_list of this DataObjectTemplatizedQuery.
        :rtype: list[str]
        """
        return self._having_conditions_list

    @having_conditions_list.setter
    def having_conditions_list(self, having_conditions_list):
        """
        Sets the having_conditions_list of this DataObjectTemplatizedQuery.
        List of items to be added into the HAVING clause of the query; items will be added with AND separation.


        :param having_conditions_list: The having_conditions_list of this DataObjectTemplatizedQuery.
        :type: list[str]
        """
        self._having_conditions_list = having_conditions_list

    @property
    def order_by_list(self):
        """
        Gets the order_by_list of this DataObjectTemplatizedQuery.
        List of items to be added into the ORDER BY clause of the query; items will be added with comma separation.


        :return: The order_by_list of this DataObjectTemplatizedQuery.
        :rtype: list[str]
        """
        return self._order_by_list

    @order_by_list.setter
    def order_by_list(self, order_by_list):
        """
        Sets the order_by_list of this DataObjectTemplatizedQuery.
        List of items to be added into the ORDER BY clause of the query; items will be added with comma separation.


        :param order_by_list: The order_by_list of this DataObjectTemplatizedQuery.
        :type: list[str]
        """
        self._order_by_list = order_by_list

    @property
    def time_filters(self):
        """
        Gets the time_filters of this DataObjectTemplatizedQuery.

        :return: The time_filters of this DataObjectTemplatizedQuery.
        :rtype: oci.opsi.models.DataObjectQueryTimeFilters
        """
        return self._time_filters

    @time_filters.setter
    def time_filters(self, time_filters):
        """
        Sets the time_filters of this DataObjectTemplatizedQuery.

        :param time_filters: The time_filters of this DataObjectTemplatizedQuery.
        :type: oci.opsi.models.DataObjectQueryTimeFilters
        """
        self._time_filters = time_filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
