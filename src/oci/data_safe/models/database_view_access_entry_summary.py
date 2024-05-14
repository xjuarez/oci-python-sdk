# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseViewAccessEntrySummary(object):
    """
    Summary of DatabaseViewAccess Object.
    """

    #: A constant which can be used with the access_type property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "SELECT"
    ACCESS_TYPE_SELECT = "SELECT"

    #: A constant which can be used with the access_type property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "UPDATE"
    ACCESS_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the access_type property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "INSERT"
    ACCESS_TYPE_INSERT = "INSERT"

    #: A constant which can be used with the access_type property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "DELETE"
    ACCESS_TYPE_DELETE = "DELETE"

    #: A constant which can be used with the access_type property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "OWNER"
    ACCESS_TYPE_OWNER = "OWNER"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "SELECT"
    PRIVILEGE_SELECT = "SELECT"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "UPDATE"
    PRIVILEGE_UPDATE = "UPDATE"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "INSERT"
    PRIVILEGE_INSERT = "INSERT"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "DELETE"
    PRIVILEGE_DELETE = "DELETE"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "READ"
    PRIVILEGE_READ = "READ"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "OWNER"
    PRIVILEGE_OWNER = "OWNER"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "INDEX"
    PRIVILEGE_INDEX = "INDEX"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "SELECT_ANY_TABLE"
    PRIVILEGE_SELECT_ANY_TABLE = "SELECT_ANY_TABLE"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "UPDATE_ANY_TABLE"
    PRIVILEGE_UPDATE_ANY_TABLE = "UPDATE_ANY_TABLE"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "INSERT_ANY_TABLE"
    PRIVILEGE_INSERT_ANY_TABLE = "INSERT_ANY_TABLE"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "DELETE_ANY_TABLE"
    PRIVILEGE_DELETE_ANY_TABLE = "DELETE_ANY_TABLE"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "READ_ANY_TABLE"
    PRIVILEGE_READ_ANY_TABLE = "READ_ANY_TABLE"

    #: A constant which can be used with the privilege property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "CREATE_ANY_INDEX"
    PRIVILEGE_CREATE_ANY_INDEX = "CREATE_ANY_INDEX"

    #: A constant which can be used with the privilege_grantable property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "ADMIN_OPTION"
    PRIVILEGE_GRANTABLE_ADMIN_OPTION = "ADMIN_OPTION"

    #: A constant which can be used with the privilege_grantable property of a DatabaseViewAccessEntrySummary.
    #: This constant has a value of "GRANT_OPTION"
    PRIVILEGE_GRANTABLE_GRANT_OPTION = "GRANT_OPTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseViewAccessEntrySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DatabaseViewAccessEntrySummary.
        :type key: str

        :param grantee:
            The value to assign to the grantee property of this DatabaseViewAccessEntrySummary.
        :type grantee: str

        :param grant_from_role:
            The value to assign to the grant_from_role property of this DatabaseViewAccessEntrySummary.
        :type grant_from_role: str

        :param access_type:
            The value to assign to the access_type property of this DatabaseViewAccessEntrySummary.
            Allowed values for this property are: "SELECT", "UPDATE", "INSERT", "DELETE", "OWNER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type access_type: str

        :param privilege:
            The value to assign to the privilege property of this DatabaseViewAccessEntrySummary.
            Allowed values for this property are: "SELECT", "UPDATE", "INSERT", "DELETE", "READ", "OWNER", "INDEX", "SELECT_ANY_TABLE", "UPDATE_ANY_TABLE", "INSERT_ANY_TABLE", "DELETE_ANY_TABLE", "READ_ANY_TABLE", "CREATE_ANY_INDEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type privilege: str

        :param target_id:
            The value to assign to the target_id property of this DatabaseViewAccessEntrySummary.
        :type target_id: str

        :param privilege_grantable:
            The value to assign to the privilege_grantable property of this DatabaseViewAccessEntrySummary.
            Allowed values for this property are: "ADMIN_OPTION", "GRANT_OPTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type privilege_grantable: str

        :param privilege_type:
            The value to assign to the privilege_type property of this DatabaseViewAccessEntrySummary.
        :type privilege_type: str

        :param table_schema:
            The value to assign to the table_schema property of this DatabaseViewAccessEntrySummary.
        :type table_schema: str

        :param table_name:
            The value to assign to the table_name property of this DatabaseViewAccessEntrySummary.
        :type table_name: str

        :param view_schema:
            The value to assign to the view_schema property of this DatabaseViewAccessEntrySummary.
        :type view_schema: str

        :param view_name:
            The value to assign to the view_name property of this DatabaseViewAccessEntrySummary.
        :type view_name: str

        :param view_text:
            The value to assign to the view_text property of this DatabaseViewAccessEntrySummary.
        :type view_text: str

        :param column_name:
            The value to assign to the column_name property of this DatabaseViewAccessEntrySummary.
        :type column_name: str

        :param grantor:
            The value to assign to the grantor property of this DatabaseViewAccessEntrySummary.
        :type grantor: str

        :param is_access_constrained_by_database_vault:
            The value to assign to the is_access_constrained_by_database_vault property of this DatabaseViewAccessEntrySummary.
        :type is_access_constrained_by_database_vault: bool

        :param is_access_constrained_by_virtual_private_database:
            The value to assign to the is_access_constrained_by_virtual_private_database property of this DatabaseViewAccessEntrySummary.
        :type is_access_constrained_by_virtual_private_database: bool

        :param is_access_constrained_by_redaction:
            The value to assign to the is_access_constrained_by_redaction property of this DatabaseViewAccessEntrySummary.
        :type is_access_constrained_by_redaction: bool

        :param is_access_constrained_by_real_application_security:
            The value to assign to the is_access_constrained_by_real_application_security property of this DatabaseViewAccessEntrySummary.
        :type is_access_constrained_by_real_application_security: bool

        :param is_access_constrained_by_sql_firewall:
            The value to assign to the is_access_constrained_by_sql_firewall property of this DatabaseViewAccessEntrySummary.
        :type is_access_constrained_by_sql_firewall: bool

        """
        self.swagger_types = {
            'key': 'str',
            'grantee': 'str',
            'grant_from_role': 'str',
            'access_type': 'str',
            'privilege': 'str',
            'target_id': 'str',
            'privilege_grantable': 'str',
            'privilege_type': 'str',
            'table_schema': 'str',
            'table_name': 'str',
            'view_schema': 'str',
            'view_name': 'str',
            'view_text': 'str',
            'column_name': 'str',
            'grantor': 'str',
            'is_access_constrained_by_database_vault': 'bool',
            'is_access_constrained_by_virtual_private_database': 'bool',
            'is_access_constrained_by_redaction': 'bool',
            'is_access_constrained_by_real_application_security': 'bool',
            'is_access_constrained_by_sql_firewall': 'bool'
        }

        self.attribute_map = {
            'key': 'key',
            'grantee': 'grantee',
            'grant_from_role': 'grantFromRole',
            'access_type': 'accessType',
            'privilege': 'privilege',
            'target_id': 'targetId',
            'privilege_grantable': 'privilegeGrantable',
            'privilege_type': 'privilegeType',
            'table_schema': 'tableSchema',
            'table_name': 'tableName',
            'view_schema': 'viewSchema',
            'view_name': 'viewName',
            'view_text': 'viewText',
            'column_name': 'columnName',
            'grantor': 'grantor',
            'is_access_constrained_by_database_vault': 'isAccessConstrainedByDatabaseVault',
            'is_access_constrained_by_virtual_private_database': 'isAccessConstrainedByVirtualPrivateDatabase',
            'is_access_constrained_by_redaction': 'isAccessConstrainedByRedaction',
            'is_access_constrained_by_real_application_security': 'isAccessConstrainedByRealApplicationSecurity',
            'is_access_constrained_by_sql_firewall': 'isAccessConstrainedBySqlFirewall'
        }

        self._key = None
        self._grantee = None
        self._grant_from_role = None
        self._access_type = None
        self._privilege = None
        self._target_id = None
        self._privilege_grantable = None
        self._privilege_type = None
        self._table_schema = None
        self._table_name = None
        self._view_schema = None
        self._view_name = None
        self._view_text = None
        self._column_name = None
        self._grantor = None
        self._is_access_constrained_by_database_vault = None
        self._is_access_constrained_by_virtual_private_database = None
        self._is_access_constrained_by_redaction = None
        self._is_access_constrained_by_real_application_security = None
        self._is_access_constrained_by_sql_firewall = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DatabaseViewAccessEntrySummary.
        The unique key that identifies the view report. It is numeric and unique within a security policy report.


        :return: The key of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DatabaseViewAccessEntrySummary.
        The unique key that identifies the view report. It is numeric and unique within a security policy report.


        :param key: The key of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._key = key

    @property
    def grantee(self):
        """
        **[Required]** Gets the grantee of this DatabaseViewAccessEntrySummary.
        Grantee is the user who can access the view.


        :return: The grantee of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._grantee

    @grantee.setter
    def grantee(self, grantee):
        """
        Sets the grantee of this DatabaseViewAccessEntrySummary.
        Grantee is the user who can access the view.


        :param grantee: The grantee of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._grantee = grantee

    @property
    def grant_from_role(self):
        """
        Gets the grant_from_role of this DatabaseViewAccessEntrySummary.
        This can be empty in case of direct grant, in case of indirect grant, this attribute displays the name of the
        role which is granted to the user though which the user has access to the table.


        :return: The grant_from_role of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._grant_from_role

    @grant_from_role.setter
    def grant_from_role(self, grant_from_role):
        """
        Sets the grant_from_role of this DatabaseViewAccessEntrySummary.
        This can be empty in case of direct grant, in case of indirect grant, this attribute displays the name of the
        role which is granted to the user though which the user has access to the table.


        :param grant_from_role: The grant_from_role of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._grant_from_role = grant_from_role

    @property
    def access_type(self):
        """
        Gets the access_type of this DatabaseViewAccessEntrySummary.
        The type of the access the user has on the table, there can be one or more from SELECT, DELETE, INSERT, READ or UPDATE.

        Allowed values for this property are: "SELECT", "UPDATE", "INSERT", "DELETE", "OWNER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The access_type of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this DatabaseViewAccessEntrySummary.
        The type of the access the user has on the table, there can be one or more from SELECT, DELETE, INSERT, READ or UPDATE.


        :param access_type: The access_type of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        allowed_values = ["SELECT", "UPDATE", "INSERT", "DELETE", "OWNER"]
        if not value_allowed_none_or_none_sentinel(access_type, allowed_values):
            access_type = 'UNKNOWN_ENUM_VALUE'
        self._access_type = access_type

    @property
    def privilege(self):
        """
        Gets the privilege of this DatabaseViewAccessEntrySummary.
        The name of the privilege.

        Allowed values for this property are: "SELECT", "UPDATE", "INSERT", "DELETE", "READ", "OWNER", "INDEX", "SELECT_ANY_TABLE", "UPDATE_ANY_TABLE", "INSERT_ANY_TABLE", "DELETE_ANY_TABLE", "READ_ANY_TABLE", "CREATE_ANY_INDEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The privilege of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """
        Sets the privilege of this DatabaseViewAccessEntrySummary.
        The name of the privilege.


        :param privilege: The privilege of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        allowed_values = ["SELECT", "UPDATE", "INSERT", "DELETE", "READ", "OWNER", "INDEX", "SELECT_ANY_TABLE", "UPDATE_ANY_TABLE", "INSERT_ANY_TABLE", "DELETE_ANY_TABLE", "READ_ANY_TABLE", "CREATE_ANY_INDEX"]
        if not value_allowed_none_or_none_sentinel(privilege, allowed_values):
            privilege = 'UNKNOWN_ENUM_VALUE'
        self._privilege = privilege

    @property
    def target_id(self):
        """
        Gets the target_id of this DatabaseViewAccessEntrySummary.
        The OCID of the of the  target database.


        :return: The target_id of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this DatabaseViewAccessEntrySummary.
        The OCID of the of the  target database.


        :param target_id: The target_id of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def privilege_grantable(self):
        """
        Gets the privilege_grantable of this DatabaseViewAccessEntrySummary.
        Indicates whether the grantee can grant this privilege to other users. Privileges can be granted to a user or role with
        GRANT_OPTION or ADMIN_OPTION

        Allowed values for this property are: "ADMIN_OPTION", "GRANT_OPTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The privilege_grantable of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._privilege_grantable

    @privilege_grantable.setter
    def privilege_grantable(self, privilege_grantable):
        """
        Sets the privilege_grantable of this DatabaseViewAccessEntrySummary.
        Indicates whether the grantee can grant this privilege to other users. Privileges can be granted to a user or role with
        GRANT_OPTION or ADMIN_OPTION


        :param privilege_grantable: The privilege_grantable of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        allowed_values = ["ADMIN_OPTION", "GRANT_OPTION"]
        if not value_allowed_none_or_none_sentinel(privilege_grantable, allowed_values):
            privilege_grantable = 'UNKNOWN_ENUM_VALUE'
        self._privilege_grantable = privilege_grantable

    @property
    def privilege_type(self):
        """
        Gets the privilege_type of this DatabaseViewAccessEntrySummary.
        Type of the privilege user has, this includes System Privilege, Schema Privilege, Object Privilege, Column Privilege,
        Owner or Schema Privilege on a schema.


        :return: The privilege_type of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._privilege_type

    @privilege_type.setter
    def privilege_type(self, privilege_type):
        """
        Sets the privilege_type of this DatabaseViewAccessEntrySummary.
        Type of the privilege user has, this includes System Privilege, Schema Privilege, Object Privilege, Column Privilege,
        Owner or Schema Privilege on a schema.


        :param privilege_type: The privilege_type of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._privilege_type = privilege_type

    @property
    def table_schema(self):
        """
        Gets the table_schema of this DatabaseViewAccessEntrySummary.
        The name of the schema


        :return: The table_schema of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._table_schema

    @table_schema.setter
    def table_schema(self, table_schema):
        """
        Sets the table_schema of this DatabaseViewAccessEntrySummary.
        The name of the schema


        :param table_schema: The table_schema of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._table_schema = table_schema

    @property
    def table_name(self):
        """
        Gets the table_name of this DatabaseViewAccessEntrySummary.
        The name of the table.


        :return: The table_name of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this DatabaseViewAccessEntrySummary.
        The name of the table.


        :param table_name: The table_name of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._table_name = table_name

    @property
    def view_schema(self):
        """
        Gets the view_schema of this DatabaseViewAccessEntrySummary.
        The name of the schema.


        :return: The view_schema of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._view_schema

    @view_schema.setter
    def view_schema(self, view_schema):
        """
        Sets the view_schema of this DatabaseViewAccessEntrySummary.
        The name of the schema.


        :param view_schema: The view_schema of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._view_schema = view_schema

    @property
    def view_name(self):
        """
        Gets the view_name of this DatabaseViewAccessEntrySummary.
        The name of the view.


        :return: The view_name of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """
        Sets the view_name of this DatabaseViewAccessEntrySummary.
        The name of the view.


        :param view_name: The view_name of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._view_name = view_name

    @property
    def view_text(self):
        """
        Gets the view_text of this DatabaseViewAccessEntrySummary.
        The definition of the view.


        :return: The view_text of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._view_text

    @view_text.setter
    def view_text(self, view_text):
        """
        Sets the view_text of this DatabaseViewAccessEntrySummary.
        The definition of the view.


        :param view_text: The view_text of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._view_text = view_text

    @property
    def column_name(self):
        """
        Gets the column_name of this DatabaseViewAccessEntrySummary.
        The name of column when there are column level privileges on a table or view.


        :return: The column_name of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this DatabaseViewAccessEntrySummary.
        The name of column when there are column level privileges on a table or view.


        :param column_name: The column_name of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._column_name = column_name

    @property
    def grantor(self):
        """
        Gets the grantor of this DatabaseViewAccessEntrySummary.
        The user who granted the privilege.


        :return: The grantor of this DatabaseViewAccessEntrySummary.
        :rtype: str
        """
        return self._grantor

    @grantor.setter
    def grantor(self, grantor):
        """
        Sets the grantor of this DatabaseViewAccessEntrySummary.
        The user who granted the privilege.


        :param grantor: The grantor of this DatabaseViewAccessEntrySummary.
        :type: str
        """
        self._grantor = grantor

    @property
    def is_access_constrained_by_database_vault(self):
        """
        Gets the is_access_constrained_by_database_vault of this DatabaseViewAccessEntrySummary.
        Indicates whether the table access is constrained via Oracle Database Vault.


        :return: The is_access_constrained_by_database_vault of this DatabaseViewAccessEntrySummary.
        :rtype: bool
        """
        return self._is_access_constrained_by_database_vault

    @is_access_constrained_by_database_vault.setter
    def is_access_constrained_by_database_vault(self, is_access_constrained_by_database_vault):
        """
        Sets the is_access_constrained_by_database_vault of this DatabaseViewAccessEntrySummary.
        Indicates whether the table access is constrained via Oracle Database Vault.


        :param is_access_constrained_by_database_vault: The is_access_constrained_by_database_vault of this DatabaseViewAccessEntrySummary.
        :type: bool
        """
        self._is_access_constrained_by_database_vault = is_access_constrained_by_database_vault

    @property
    def is_access_constrained_by_virtual_private_database(self):
        """
        Gets the is_access_constrained_by_virtual_private_database of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Virtual Private Database.


        :return: The is_access_constrained_by_virtual_private_database of this DatabaseViewAccessEntrySummary.
        :rtype: bool
        """
        return self._is_access_constrained_by_virtual_private_database

    @is_access_constrained_by_virtual_private_database.setter
    def is_access_constrained_by_virtual_private_database(self, is_access_constrained_by_virtual_private_database):
        """
        Sets the is_access_constrained_by_virtual_private_database of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Virtual Private Database.


        :param is_access_constrained_by_virtual_private_database: The is_access_constrained_by_virtual_private_database of this DatabaseViewAccessEntrySummary.
        :type: bool
        """
        self._is_access_constrained_by_virtual_private_database = is_access_constrained_by_virtual_private_database

    @property
    def is_access_constrained_by_redaction(self):
        """
        Gets the is_access_constrained_by_redaction of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Oracle Data Redaction.


        :return: The is_access_constrained_by_redaction of this DatabaseViewAccessEntrySummary.
        :rtype: bool
        """
        return self._is_access_constrained_by_redaction

    @is_access_constrained_by_redaction.setter
    def is_access_constrained_by_redaction(self, is_access_constrained_by_redaction):
        """
        Sets the is_access_constrained_by_redaction of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Oracle Data Redaction.


        :param is_access_constrained_by_redaction: The is_access_constrained_by_redaction of this DatabaseViewAccessEntrySummary.
        :type: bool
        """
        self._is_access_constrained_by_redaction = is_access_constrained_by_redaction

    @property
    def is_access_constrained_by_real_application_security(self):
        """
        Gets the is_access_constrained_by_real_application_security of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Real Application Security.


        :return: The is_access_constrained_by_real_application_security of this DatabaseViewAccessEntrySummary.
        :rtype: bool
        """
        return self._is_access_constrained_by_real_application_security

    @is_access_constrained_by_real_application_security.setter
    def is_access_constrained_by_real_application_security(self, is_access_constrained_by_real_application_security):
        """
        Sets the is_access_constrained_by_real_application_security of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Real Application Security.


        :param is_access_constrained_by_real_application_security: The is_access_constrained_by_real_application_security of this DatabaseViewAccessEntrySummary.
        :type: bool
        """
        self._is_access_constrained_by_real_application_security = is_access_constrained_by_real_application_security

    @property
    def is_access_constrained_by_sql_firewall(self):
        """
        Gets the is_access_constrained_by_sql_firewall of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Oracle Database SQL Firewall.


        :return: The is_access_constrained_by_sql_firewall of this DatabaseViewAccessEntrySummary.
        :rtype: bool
        """
        return self._is_access_constrained_by_sql_firewall

    @is_access_constrained_by_sql_firewall.setter
    def is_access_constrained_by_sql_firewall(self, is_access_constrained_by_sql_firewall):
        """
        Sets the is_access_constrained_by_sql_firewall of this DatabaseViewAccessEntrySummary.
        Indicates whether the view access is constrained via Oracle Database SQL Firewall.


        :param is_access_constrained_by_sql_firewall: The is_access_constrained_by_sql_firewall of this DatabaseViewAccessEntrySummary.
        :type: bool
        """
        self._is_access_constrained_by_sql_firewall = is_access_constrained_by_sql_firewall

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
