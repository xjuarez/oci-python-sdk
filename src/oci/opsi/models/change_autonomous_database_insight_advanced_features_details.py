# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails(object):
    """
    Advanced feature details of autonomous database insight.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_details:
            The value to assign to the connection_details property of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :type connection_details: oci.opsi.models.ConnectionDetails

        :param credential_details:
            The value to assign to the credential_details property of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :type credential_details: oci.opsi.models.CredentialDetails

        :param opsi_private_endpoint_id:
            The value to assign to the opsi_private_endpoint_id property of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :type opsi_private_endpoint_id: str

        """
        self.swagger_types = {
            'connection_details': 'ConnectionDetails',
            'credential_details': 'CredentialDetails',
            'opsi_private_endpoint_id': 'str'
        }

        self.attribute_map = {
            'connection_details': 'connectionDetails',
            'credential_details': 'credentialDetails',
            'opsi_private_endpoint_id': 'opsiPrivateEndpointId'
        }

        self._connection_details = None
        self._credential_details = None
        self._opsi_private_endpoint_id = None

    @property
    def connection_details(self):
        """
        **[Required]** Gets the connection_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.

        :return: The connection_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :rtype: oci.opsi.models.ConnectionDetails
        """
        return self._connection_details

    @connection_details.setter
    def connection_details(self, connection_details):
        """
        Sets the connection_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.

        :param connection_details: The connection_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :type: oci.opsi.models.ConnectionDetails
        """
        self._connection_details = connection_details

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.

        :return: The credential_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :rtype: oci.opsi.models.CredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.

        :param credential_details: The credential_details of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :type: oci.opsi.models.CredentialDetails
        """
        self._credential_details = credential_details

    @property
    def opsi_private_endpoint_id(self):
        """
        Gets the opsi_private_endpoint_id of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The opsi_private_endpoint_id of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :rtype: str
        """
        return self._opsi_private_endpoint_id

    @opsi_private_endpoint_id.setter
    def opsi_private_endpoint_id(self, opsi_private_endpoint_id):
        """
        Sets the opsi_private_endpoint_id of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param opsi_private_endpoint_id: The opsi_private_endpoint_id of this ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails.
        :type: str
        """
        self._opsi_private_endpoint_id = opsi_private_endpoint_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
