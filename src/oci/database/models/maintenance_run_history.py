# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenanceRunHistory(object):
    """
    Details of a maintenance run history.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenanceRunHistory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MaintenanceRunHistory.
        :type id: str

        :param maintenance_run_details:
            The value to assign to the maintenance_run_details property of this MaintenanceRunHistory.
        :type maintenance_run_details: oci.database.models.MaintenanceRunSummary

        :param db_servers_history_details:
            The value to assign to the db_servers_history_details property of this MaintenanceRunHistory.
        :type db_servers_history_details: list[oci.database.models.DbServerHistorySummary]

        :param current_execution_window:
            The value to assign to the current_execution_window property of this MaintenanceRunHistory.
        :type current_execution_window: str

        :param granular_maintenance_history:
            The value to assign to the granular_maintenance_history property of this MaintenanceRunHistory.
        :type granular_maintenance_history: list[oci.database.models.GranularMaintenanceHistoryDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'maintenance_run_details': 'MaintenanceRunSummary',
            'db_servers_history_details': 'list[DbServerHistorySummary]',
            'current_execution_window': 'str',
            'granular_maintenance_history': 'list[GranularMaintenanceHistoryDetails]'
        }

        self.attribute_map = {
            'id': 'id',
            'maintenance_run_details': 'maintenanceRunDetails',
            'db_servers_history_details': 'dbServersHistoryDetails',
            'current_execution_window': 'currentExecutionWindow',
            'granular_maintenance_history': 'granularMaintenanceHistory'
        }

        self._id = None
        self._maintenance_run_details = None
        self._db_servers_history_details = None
        self._current_execution_window = None
        self._granular_maintenance_history = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MaintenanceRunHistory.
        The OCID of the maintenance run history.


        :return: The id of this MaintenanceRunHistory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaintenanceRunHistory.
        The OCID of the maintenance run history.


        :param id: The id of this MaintenanceRunHistory.
        :type: str
        """
        self._id = id

    @property
    def maintenance_run_details(self):
        """
        Gets the maintenance_run_details of this MaintenanceRunHistory.

        :return: The maintenance_run_details of this MaintenanceRunHistory.
        :rtype: oci.database.models.MaintenanceRunSummary
        """
        return self._maintenance_run_details

    @maintenance_run_details.setter
    def maintenance_run_details(self, maintenance_run_details):
        """
        Sets the maintenance_run_details of this MaintenanceRunHistory.

        :param maintenance_run_details: The maintenance_run_details of this MaintenanceRunHistory.
        :type: oci.database.models.MaintenanceRunSummary
        """
        self._maintenance_run_details = maintenance_run_details

    @property
    def db_servers_history_details(self):
        """
        Gets the db_servers_history_details of this MaintenanceRunHistory.
        List of database server history details.


        :return: The db_servers_history_details of this MaintenanceRunHistory.
        :rtype: list[oci.database.models.DbServerHistorySummary]
        """
        return self._db_servers_history_details

    @db_servers_history_details.setter
    def db_servers_history_details(self, db_servers_history_details):
        """
        Sets the db_servers_history_details of this MaintenanceRunHistory.
        List of database server history details.


        :param db_servers_history_details: The db_servers_history_details of this MaintenanceRunHistory.
        :type: list[oci.database.models.DbServerHistorySummary]
        """
        self._db_servers_history_details = db_servers_history_details

    @property
    def current_execution_window(self):
        """
        Gets the current_execution_window of this MaintenanceRunHistory.
        The OCID of the current execution window.


        :return: The current_execution_window of this MaintenanceRunHistory.
        :rtype: str
        """
        return self._current_execution_window

    @current_execution_window.setter
    def current_execution_window(self, current_execution_window):
        """
        Sets the current_execution_window of this MaintenanceRunHistory.
        The OCID of the current execution window.


        :param current_execution_window: The current_execution_window of this MaintenanceRunHistory.
        :type: str
        """
        self._current_execution_window = current_execution_window

    @property
    def granular_maintenance_history(self):
        """
        Gets the granular_maintenance_history of this MaintenanceRunHistory.
        The list of granular maintenance history details.


        :return: The granular_maintenance_history of this MaintenanceRunHistory.
        :rtype: list[oci.database.models.GranularMaintenanceHistoryDetails]
        """
        return self._granular_maintenance_history

    @granular_maintenance_history.setter
    def granular_maintenance_history(self, granular_maintenance_history):
        """
        Sets the granular_maintenance_history of this MaintenanceRunHistory.
        The list of granular maintenance history details.


        :param granular_maintenance_history: The granular_maintenance_history of this MaintenanceRunHistory.
        :type: list[oci.database.models.GranularMaintenanceHistoryDetails]
        """
        self._granular_maintenance_history = granular_maintenance_history

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
