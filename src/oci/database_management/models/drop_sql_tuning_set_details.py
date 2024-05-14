# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DropSqlTuningSetDetails(object):
    """
    The details required to drop a Sql tuning set.
    It takes either credentialDetails or databaseCredential. It's recommended to provide databaseCredential
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DropSqlTuningSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this DropSqlTuningSetDetails.
        :type credential_details: oci.database_management.models.SqlTuningSetAdminCredentialDetails

        :param database_credential:
            The value to assign to the database_credential property of this DropSqlTuningSetDetails.
        :type database_credential: oci.database_management.models.DatabaseCredentialDetails

        :param name:
            The value to assign to the name property of this DropSqlTuningSetDetails.
        :type name: str

        :param owner:
            The value to assign to the owner property of this DropSqlTuningSetDetails.
        :type owner: str

        :param show_sql_only:
            The value to assign to the show_sql_only property of this DropSqlTuningSetDetails.
        :type show_sql_only: int

        """
        self.swagger_types = {
            'credential_details': 'SqlTuningSetAdminCredentialDetails',
            'database_credential': 'DatabaseCredentialDetails',
            'name': 'str',
            'owner': 'str',
            'show_sql_only': 'int'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'database_credential': 'databaseCredential',
            'name': 'name',
            'owner': 'owner',
            'show_sql_only': 'showSqlOnly'
        }

        self._credential_details = None
        self._database_credential = None
        self._name = None
        self._owner = None
        self._show_sql_only = None

    @property
    def credential_details(self):
        """
        Gets the credential_details of this DropSqlTuningSetDetails.

        :return: The credential_details of this DropSqlTuningSetDetails.
        :rtype: oci.database_management.models.SqlTuningSetAdminCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this DropSqlTuningSetDetails.

        :param credential_details: The credential_details of this DropSqlTuningSetDetails.
        :type: oci.database_management.models.SqlTuningSetAdminCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def database_credential(self):
        """
        Gets the database_credential of this DropSqlTuningSetDetails.

        :return: The database_credential of this DropSqlTuningSetDetails.
        :rtype: oci.database_management.models.DatabaseCredentialDetails
        """
        return self._database_credential

    @database_credential.setter
    def database_credential(self, database_credential):
        """
        Sets the database_credential of this DropSqlTuningSetDetails.

        :param database_credential: The database_credential of this DropSqlTuningSetDetails.
        :type: oci.database_management.models.DatabaseCredentialDetails
        """
        self._database_credential = database_credential

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DropSqlTuningSetDetails.
        A unique Sql tuning set name.


        :return: The name of this DropSqlTuningSetDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DropSqlTuningSetDetails.
        A unique Sql tuning set name.


        :param name: The name of this DropSqlTuningSetDetails.
        :type: str
        """
        self._name = name

    @property
    def owner(self):
        """
        Gets the owner of this DropSqlTuningSetDetails.
        Owner of the Sql tuning set.


        :return: The owner of this DropSqlTuningSetDetails.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DropSqlTuningSetDetails.
        Owner of the Sql tuning set.


        :param owner: The owner of this DropSqlTuningSetDetails.
        :type: str
        """
        self._owner = owner

    @property
    def show_sql_only(self):
        """
        Gets the show_sql_only of this DropSqlTuningSetDetails.
        Flag to indicate whether to drop  the Sql tuning set or just display the plsql used to drop Sql tuning set.


        :return: The show_sql_only of this DropSqlTuningSetDetails.
        :rtype: int
        """
        return self._show_sql_only

    @show_sql_only.setter
    def show_sql_only(self, show_sql_only):
        """
        Sets the show_sql_only of this DropSqlTuningSetDetails.
        Flag to indicate whether to drop  the Sql tuning set or just display the plsql used to drop Sql tuning set.


        :param show_sql_only: The show_sql_only of this DropSqlTuningSetDetails.
        :type: int
        """
        self._show_sql_only = show_sql_only

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
