# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoverExternalExadataInfrastructureDetails(object):
    """
    The connection details and the discovery options for the Exadata discovery.
    """

    #: A constant which can be used with the discovery_type property of a DiscoverExternalExadataInfrastructureDetails.
    #: This constant has a value of "NEW"
    DISCOVERY_TYPE_NEW = "NEW"

    #: A constant which can be used with the discovery_type property of a DiscoverExternalExadataInfrastructureDetails.
    #: This constant has a value of "OVERRIDE"
    DISCOVERY_TYPE_OVERRIDE = "OVERRIDE"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoverExternalExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DiscoverExternalExadataInfrastructureDetails.
        :type compartment_id: str

        :param discovery_type:
            The value to assign to the discovery_type property of this DiscoverExternalExadataInfrastructureDetails.
            Allowed values for this property are: "NEW", "OVERRIDE"
        :type discovery_type: str

        :param db_system_ids:
            The value to assign to the db_system_ids property of this DiscoverExternalExadataInfrastructureDetails.
        :type db_system_ids: list[str]

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this DiscoverExternalExadataInfrastructureDetails.
        :type exadata_infrastructure_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'discovery_type': 'str',
            'db_system_ids': 'list[str]',
            'exadata_infrastructure_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'discovery_type': 'discoveryType',
            'db_system_ids': 'dbSystemIds',
            'exadata_infrastructure_id': 'exadataInfrastructureId'
        }

        self._compartment_id = None
        self._discovery_type = None
        self._db_system_ids = None
        self._exadata_infrastructure_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DiscoverExternalExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DiscoverExternalExadataInfrastructureDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DiscoverExternalExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DiscoverExternalExadataInfrastructureDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def discovery_type(self):
        """
        **[Required]** Gets the discovery_type of this DiscoverExternalExadataInfrastructureDetails.
        The type of discovery.

        Allowed values for this property are: "NEW", "OVERRIDE"


        :return: The discovery_type of this DiscoverExternalExadataInfrastructureDetails.
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """
        Sets the discovery_type of this DiscoverExternalExadataInfrastructureDetails.
        The type of discovery.


        :param discovery_type: The discovery_type of this DiscoverExternalExadataInfrastructureDetails.
        :type: str
        """
        allowed_values = ["NEW", "OVERRIDE"]
        if not value_allowed_none_or_none_sentinel(discovery_type, allowed_values):
            raise ValueError(
                "Invalid value for `discovery_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._discovery_type = discovery_type

    @property
    def db_system_ids(self):
        """
        **[Required]** Gets the db_system_ids of this DiscoverExternalExadataInfrastructureDetails.
        The list of the DB system identifiers.


        :return: The db_system_ids of this DiscoverExternalExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._db_system_ids

    @db_system_ids.setter
    def db_system_ids(self, db_system_ids):
        """
        Sets the db_system_ids of this DiscoverExternalExadataInfrastructureDetails.
        The list of the DB system identifiers.


        :param db_system_ids: The db_system_ids of this DiscoverExternalExadataInfrastructureDetails.
        :type: list[str]
        """
        self._db_system_ids = db_system_ids

    @property
    def exadata_infrastructure_id(self):
        """
        Gets the exadata_infrastructure_id of this DiscoverExternalExadataInfrastructureDetails.
        The `OCID`__ of the Exadata infrastructure. This is applicable for rediscovery only.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this DiscoverExternalExadataInfrastructureDetails.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this DiscoverExternalExadataInfrastructureDetails.
        The `OCID`__ of the Exadata infrastructure. This is applicable for rediscovery only.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this DiscoverExternalExadataInfrastructureDetails.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
