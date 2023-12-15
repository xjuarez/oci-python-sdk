# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915

from .source_details import SourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupSourceDetails(SourceDetails):
    """
    Restoring to a new database system from the backup.
    The database system details that are part of the CreateDbSystem request are not required, but if present will override the details from the backup's database system snapshot.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.psql.models.BackupSourceDetails.source_type` attribute
        of this class is ``BACKUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this BackupSourceDetails.
            Allowed values for this property are: "BACKUP", "NONE"
        :type source_type: str

        :param backup_id:
            The value to assign to the backup_id property of this BackupSourceDetails.
        :type backup_id: str

        :param is_having_restore_config_overrides:
            The value to assign to the is_having_restore_config_overrides property of this BackupSourceDetails.
        :type is_having_restore_config_overrides: bool

        """
        self.swagger_types = {
            'source_type': 'str',
            'backup_id': 'str',
            'is_having_restore_config_overrides': 'bool'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'backup_id': 'backupId',
            'is_having_restore_config_overrides': 'isHavingRestoreConfigOverrides'
        }

        self._source_type = None
        self._backup_id = None
        self._is_having_restore_config_overrides = None
        self._source_type = 'BACKUP'

    @property
    def backup_id(self):
        """
        **[Required]** Gets the backup_id of this BackupSourceDetails.
        The `OCID`__ of the database system backup.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The backup_id of this BackupSourceDetails.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """
        Sets the backup_id of this BackupSourceDetails.
        The `OCID`__ of the database system backup.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param backup_id: The backup_id of this BackupSourceDetails.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def is_having_restore_config_overrides(self):
        """
        Gets the is_having_restore_config_overrides of this BackupSourceDetails.
        Deprecated. Don't use.


        :return: The is_having_restore_config_overrides of this BackupSourceDetails.
        :rtype: bool
        """
        return self._is_having_restore_config_overrides

    @is_having_restore_config_overrides.setter
    def is_having_restore_config_overrides(self, is_having_restore_config_overrides):
        """
        Sets the is_having_restore_config_overrides of this BackupSourceDetails.
        Deprecated. Don't use.


        :param is_having_restore_config_overrides: The is_having_restore_config_overrides of this BackupSourceDetails.
        :type: bool
        """
        self._is_having_restore_config_overrides = is_having_restore_config_overrides

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
