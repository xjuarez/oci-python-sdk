# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210929

from .update_host_dump_transfer_details import UpdateHostDumpTransferDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOciCliDumpTransferDetails(UpdateHostDumpTransferDetails):
    """
    Optional dump transfer details for OCI-CLI-based dump transfer in source or target host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOciCliDumpTransferDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateOciCliDumpTransferDetails.kind` attribute
        of this class is ``OCI_CLI`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wallet_location:
            The value to assign to the wallet_location property of this UpdateOciCliDumpTransferDetails.
        :type wallet_location: str

        :param kind:
            The value to assign to the kind property of this UpdateOciCliDumpTransferDetails.
            Allowed values for this property are: "CURL", "OCI_CLI"
        :type kind: str

        :param oci_home:
            The value to assign to the oci_home property of this UpdateOciCliDumpTransferDetails.
        :type oci_home: str

        """
        self.swagger_types = {
            'wallet_location': 'str',
            'kind': 'str',
            'oci_home': 'str'
        }

        self.attribute_map = {
            'wallet_location': 'walletLocation',
            'kind': 'kind',
            'oci_home': 'ociHome'
        }

        self._wallet_location = None
        self._kind = None
        self._oci_home = None
        self._kind = 'OCI_CLI'

    @property
    def oci_home(self):
        """
        **[Required]** Gets the oci_home of this UpdateOciCliDumpTransferDetails.
        Path to the OCI CLI installation in the node.


        :return: The oci_home of this UpdateOciCliDumpTransferDetails.
        :rtype: str
        """
        return self._oci_home

    @oci_home.setter
    def oci_home(self, oci_home):
        """
        Sets the oci_home of this UpdateOciCliDumpTransferDetails.
        Path to the OCI CLI installation in the node.


        :param oci_home: The oci_home of this UpdateOciCliDumpTransferDetails.
        :type: str
        """
        self._oci_home = oci_home

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
