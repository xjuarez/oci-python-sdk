# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .credential_entity_specific_details import CredentialEntitySpecificDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetCredentialEntitySpecificDetails(CredentialEntitySpecificDetails):
    """
    Fleet credential details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FleetCredentialEntitySpecificDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.FleetCredentialEntitySpecificDetails.credential_level` attribute
        of this class is ``FLEET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_level:
            The value to assign to the credential_level property of this FleetCredentialEntitySpecificDetails.
            Allowed values for this property are: "FLEET", "RESOURCE", "TARGET"
        :type credential_level: str

        :param variables:
            The value to assign to the variables property of this FleetCredentialEntitySpecificDetails.
        :type variables: list[oci.fleet_apps_management.models.Variable]

        """
        self.swagger_types = {
            'credential_level': 'str',
            'variables': 'list[Variable]'
        }

        self.attribute_map = {
            'credential_level': 'credentialLevel',
            'variables': 'variables'
        }

        self._credential_level = None
        self._variables = None
        self._credential_level = 'FLEET'

    @property
    def variables(self):
        """
        Gets the variables of this FleetCredentialEntitySpecificDetails.
        List of fleet credential variables.


        :return: The variables of this FleetCredentialEntitySpecificDetails.
        :rtype: list[oci.fleet_apps_management.models.Variable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this FleetCredentialEntitySpecificDetails.
        List of fleet credential variables.


        :param variables: The variables of this FleetCredentialEntitySpecificDetails.
        :type: list[oci.fleet_apps_management.models.Variable]
        """
        self._variables = variables

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
