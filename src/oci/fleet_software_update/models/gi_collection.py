# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .fsu_collection import FsuCollection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiCollection(FsuCollection):
    """
    Details to create a 'GI' type Exadata Fleet Update Collection.
    """

    #: A constant which can be used with the source_major_version property of a GiCollection.
    #: This constant has a value of "GI_18"
    SOURCE_MAJOR_VERSION_GI_18 = "GI_18"

    #: A constant which can be used with the source_major_version property of a GiCollection.
    #: This constant has a value of "GI_19"
    SOURCE_MAJOR_VERSION_GI_19 = "GI_19"

    def __init__(self, **kwargs):
        """
        Initializes a new GiCollection object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.GiCollection.type` attribute
        of this class is ``GI`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GiCollection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this GiCollection.
        :type display_name: str

        :param type:
            The value to assign to the type property of this GiCollection.
            Allowed values for this property are: "DB", "GI", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param service_type:
            The value to assign to the service_type property of this GiCollection.
            Allowed values for this property are: "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GiCollection.
        :type compartment_id: str

        :param active_fsu_cycle:
            The value to assign to the active_fsu_cycle property of this GiCollection.
        :type active_fsu_cycle: oci.fleet_software_update.models.ActiveCycleDetails

        :param target_count:
            The value to assign to the target_count property of this GiCollection.
        :type target_count: int

        :param time_created:
            The value to assign to the time_created property of this GiCollection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this GiCollection.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GiCollection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this GiCollection.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GiCollection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GiCollection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this GiCollection.
        :type system_tags: dict(str, dict(str, object))

        :param source_major_version:
            The value to assign to the source_major_version property of this GiCollection.
            Allowed values for this property are: "GI_18", "GI_19", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_major_version: str

        :param fleet_discovery:
            The value to assign to the fleet_discovery property of this GiCollection.
        :type fleet_discovery: oci.fleet_software_update.models.GiFleetDiscoveryDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'type': 'str',
            'service_type': 'str',
            'compartment_id': 'str',
            'active_fsu_cycle': 'ActiveCycleDetails',
            'target_count': 'int',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'source_major_version': 'str',
            'fleet_discovery': 'GiFleetDiscoveryDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'type': 'type',
            'service_type': 'serviceType',
            'compartment_id': 'compartmentId',
            'active_fsu_cycle': 'activeFsuCycle',
            'target_count': 'targetCount',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'source_major_version': 'sourceMajorVersion',
            'fleet_discovery': 'fleetDiscovery'
        }

        self._id = None
        self._display_name = None
        self._type = None
        self._service_type = None
        self._compartment_id = None
        self._active_fsu_cycle = None
        self._target_count = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._source_major_version = None
        self._fleet_discovery = None
        self._type = 'GI'

    @property
    def source_major_version(self):
        """
        **[Required]** Gets the source_major_version of this GiCollection.
        Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Collection.
        Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.

        Allowed values for this property are: "GI_18", "GI_19", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_major_version of this GiCollection.
        :rtype: str
        """
        return self._source_major_version

    @source_major_version.setter
    def source_major_version(self, source_major_version):
        """
        Sets the source_major_version of this GiCollection.
        Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Collection.
        Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.


        :param source_major_version: The source_major_version of this GiCollection.
        :type: str
        """
        allowed_values = ["GI_18", "GI_19"]
        if not value_allowed_none_or_none_sentinel(source_major_version, allowed_values):
            source_major_version = 'UNKNOWN_ENUM_VALUE'
        self._source_major_version = source_major_version

    @property
    def fleet_discovery(self):
        """
        **[Required]** Gets the fleet_discovery of this GiCollection.

        :return: The fleet_discovery of this GiCollection.
        :rtype: oci.fleet_software_update.models.GiFleetDiscoveryDetails
        """
        return self._fleet_discovery

    @fleet_discovery.setter
    def fleet_discovery(self, fleet_discovery):
        """
        Sets the fleet_discovery of this GiCollection.

        :param fleet_discovery: The fleet_discovery of this GiCollection.
        :type: oci.fleet_software_update.models.GiFleetDiscoveryDetails
        """
        self._fleet_discovery = fleet_discovery

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
