# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CursorCacheStatementSummary(object):
    """
    The summary of a SQL statement in the cursor cache.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CursorCacheStatementSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_id:
            The value to assign to the sql_id property of this CursorCacheStatementSummary.
        :type sql_id: str

        :param schema:
            The value to assign to the schema property of this CursorCacheStatementSummary.
        :type schema: str

        :param sql_text:
            The value to assign to the sql_text property of this CursorCacheStatementSummary.
        :type sql_text: str

        """
        self.swagger_types = {
            'sql_id': 'str',
            'schema': 'str',
            'sql_text': 'str'
        }

        self.attribute_map = {
            'sql_id': 'sqlId',
            'schema': 'schema',
            'sql_text': 'sqlText'
        }

        self._sql_id = None
        self._schema = None
        self._sql_text = None

    @property
    def sql_id(self):
        """
        **[Required]** Gets the sql_id of this CursorCacheStatementSummary.
        The SQL statement identifier. Identifies a SQL statement in the cursor cache.


        :return: The sql_id of this CursorCacheStatementSummary.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        """
        Sets the sql_id of this CursorCacheStatementSummary.
        The SQL statement identifier. Identifies a SQL statement in the cursor cache.


        :param sql_id: The sql_id of this CursorCacheStatementSummary.
        :type: str
        """
        self._sql_id = sql_id

    @property
    def schema(self):
        """
        **[Required]** Gets the schema of this CursorCacheStatementSummary.
        The name of the parsing schema.


        :return: The schema of this CursorCacheStatementSummary.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this CursorCacheStatementSummary.
        The name of the parsing schema.


        :param schema: The schema of this CursorCacheStatementSummary.
        :type: str
        """
        self._schema = schema

    @property
    def sql_text(self):
        """
        **[Required]** Gets the sql_text of this CursorCacheStatementSummary.
        The first thousand characters of the SQL text.


        :return: The sql_text of this CursorCacheStatementSummary.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """
        Sets the sql_text of this CursorCacheStatementSummary.
        The first thousand characters of the SQL text.


        :param sql_text: The sql_text of this CursorCacheStatementSummary.
        :type: str
        """
        self._sql_text = sql_text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
