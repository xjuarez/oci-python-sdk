# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePeerTargetDatabaseDetails(object):
    """
    The details used to register the peer database of a database already registered in Data Safe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePeerTargetDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreatePeerTargetDatabaseDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreatePeerTargetDatabaseDetails.
        :type description: str

        :param dataguard_association_id:
            The value to assign to the dataguard_association_id property of this CreatePeerTargetDatabaseDetails.
        :type dataguard_association_id: str

        :param database_details:
            The value to assign to the database_details property of this CreatePeerTargetDatabaseDetails.
        :type database_details: oci.data_safe.models.DatabaseDetails

        :param tls_config:
            The value to assign to the tls_config property of this CreatePeerTargetDatabaseDetails.
        :type tls_config: oci.data_safe.models.TlsConfig

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'dataguard_association_id': 'str',
            'database_details': 'DatabaseDetails',
            'tls_config': 'TlsConfig'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'dataguard_association_id': 'dataguardAssociationId',
            'database_details': 'databaseDetails',
            'tls_config': 'tlsConfig'
        }

        self._display_name = None
        self._description = None
        self._dataguard_association_id = None
        self._database_details = None
        self._tls_config = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreatePeerTargetDatabaseDetails.
        The display name of the peer target database in Data Safe. The name is modifiable and does not need to be unique.


        :return: The display_name of this CreatePeerTargetDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePeerTargetDatabaseDetails.
        The display name of the peer target database in Data Safe. The name is modifiable and does not need to be unique.


        :param display_name: The display_name of this CreatePeerTargetDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreatePeerTargetDatabaseDetails.
        The description of the peer target database in Data Safe.


        :return: The description of this CreatePeerTargetDatabaseDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePeerTargetDatabaseDetails.
        The description of the peer target database in Data Safe.


        :param description: The description of this CreatePeerTargetDatabaseDetails.
        :type: str
        """
        self._description = description

    @property
    def dataguard_association_id(self):
        """
        Gets the dataguard_association_id of this CreatePeerTargetDatabaseDetails.
        The OCID of the Data Guard Association resource in which the database being registered is considered as peer database to the primary database.


        :return: The dataguard_association_id of this CreatePeerTargetDatabaseDetails.
        :rtype: str
        """
        return self._dataguard_association_id

    @dataguard_association_id.setter
    def dataguard_association_id(self, dataguard_association_id):
        """
        Sets the dataguard_association_id of this CreatePeerTargetDatabaseDetails.
        The OCID of the Data Guard Association resource in which the database being registered is considered as peer database to the primary database.


        :param dataguard_association_id: The dataguard_association_id of this CreatePeerTargetDatabaseDetails.
        :type: str
        """
        self._dataguard_association_id = dataguard_association_id

    @property
    def database_details(self):
        """
        **[Required]** Gets the database_details of this CreatePeerTargetDatabaseDetails.

        :return: The database_details of this CreatePeerTargetDatabaseDetails.
        :rtype: oci.data_safe.models.DatabaseDetails
        """
        return self._database_details

    @database_details.setter
    def database_details(self, database_details):
        """
        Sets the database_details of this CreatePeerTargetDatabaseDetails.

        :param database_details: The database_details of this CreatePeerTargetDatabaseDetails.
        :type: oci.data_safe.models.DatabaseDetails
        """
        self._database_details = database_details

    @property
    def tls_config(self):
        """
        Gets the tls_config of this CreatePeerTargetDatabaseDetails.

        :return: The tls_config of this CreatePeerTargetDatabaseDetails.
        :rtype: oci.data_safe.models.TlsConfig
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        """
        Sets the tls_config of this CreatePeerTargetDatabaseDetails.

        :param tls_config: The tls_config of this CreatePeerTargetDatabaseDetails.
        :type: oci.data_safe.models.TlsConfig
        """
        self._tls_config = tls_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
