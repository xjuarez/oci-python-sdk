# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryDetails(object):
    """
    Request object containing the query to be run against the trace data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_text:
            The value to assign to the query_text property of this QueryDetails.
        :type query_text: str

        """
        self.swagger_types = {
            'query_text': 'str'
        }

        self.attribute_map = {
            'query_text': 'queryText'
        }

        self._query_text = None

    @property
    def query_text(self):
        """
        Gets the query_text of this QueryDetails.
        Application Performance Monitoring defined query string that filters and retrieves trace data results.


        :return: The query_text of this QueryDetails.
        :rtype: str
        """
        return self._query_text

    @query_text.setter
    def query_text(self, query_text):
        """
        Sets the query_text of this QueryDetails.
        Application Performance Monitoring defined query string that filters and retrieves trace data results.


        :param query_text: The query_text of this QueryDetails.
        :type: str
        """
        self._query_text = query_text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
