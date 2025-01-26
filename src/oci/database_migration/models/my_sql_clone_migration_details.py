# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .clone_migration_details import CloneMigrationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlCloneMigrationDetails(CloneMigrationDetails):
    """
    MySQL Clone Migration Summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlCloneMigrationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.MySqlCloneMigrationDetails.database_combination` attribute
        of this class is ``MYSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_combination:
            The value to assign to the database_combination property of this MySqlCloneMigrationDetails.
            Allowed values for this property are: "MYSQL", "ORACLE"
        :type database_combination: str

        :param display_name:
            The value to assign to the display_name property of this MySqlCloneMigrationDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MySqlCloneMigrationDetails.
        :type compartment_id: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this MySqlCloneMigrationDetails.
        :type source_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this MySqlCloneMigrationDetails.
        :type target_database_connection_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MySqlCloneMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MySqlCloneMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'database_combination': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'source_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'database_combination': 'databaseCombination',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._database_combination = None
        self._display_name = None
        self._compartment_id = None
        self._source_database_connection_id = None
        self._target_database_connection_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._database_combination = 'MYSQL'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
