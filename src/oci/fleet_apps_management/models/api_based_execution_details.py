# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .execution_details import ExecutionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiBasedExecutionDetails(ExecutionDetails):
    """
    Details for API based execution
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiBasedExecutionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.ApiBasedExecutionDetails.execution_type` attribute
        of this class is ``API`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param execution_type:
            The value to assign to the execution_type property of this ApiBasedExecutionDetails.
            Allowed values for this property are: "SCRIPT", "API"
        :type execution_type: str

        :param endpoint:
            The value to assign to the endpoint property of this ApiBasedExecutionDetails.
        :type endpoint: str

        """
        self.swagger_types = {
            'execution_type': 'str',
            'endpoint': 'str'
        }

        self.attribute_map = {
            'execution_type': 'executionType',
            'endpoint': 'endpoint'
        }

        self._execution_type = None
        self._endpoint = None
        self._execution_type = 'API'

    @property
    def endpoint(self):
        """
        **[Required]** Gets the endpoint of this ApiBasedExecutionDetails.
        Endpoint to be invoked.


        :return: The endpoint of this ApiBasedExecutionDetails.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this ApiBasedExecutionDetails.
        Endpoint to be invoked.


        :param endpoint: The endpoint of this ApiBasedExecutionDetails.
        :type: str
        """
        self._endpoint = endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
