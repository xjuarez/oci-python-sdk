# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_profile_details import CreateProfileDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGroupProfileDetails(CreateProfileDetails):
    """
    Description of a group registration profile to be created.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGroupProfileDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CreateGroupProfileDetails.profile_type` attribute
        of this class is ``GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateGroupProfileDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateGroupProfileDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateGroupProfileDetails.
        :type description: str

        :param management_station_id:
            The value to assign to the management_station_id property of this CreateGroupProfileDetails.
        :type management_station_id: str

        :param profile_type:
            The value to assign to the profile_type property of this CreateGroupProfileDetails.
            Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"
        :type profile_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateGroupProfileDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateGroupProfileDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param managed_instance_group_id:
            The value to assign to the managed_instance_group_id property of this CreateGroupProfileDetails.
        :type managed_instance_group_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'management_station_id': 'str',
            'profile_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'managed_instance_group_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'management_station_id': 'managementStationId',
            'profile_type': 'profileType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'managed_instance_group_id': 'managedInstanceGroupId'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._management_station_id = None
        self._profile_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._managed_instance_group_id = None
        self._profile_type = 'GROUP'

    @property
    def managed_instance_group_id(self):
        """
        **[Required]** Gets the managed_instance_group_id of this CreateGroupProfileDetails.
        The OCID of the managed instance group from which the registration profile will inherit its software sources.


        :return: The managed_instance_group_id of this CreateGroupProfileDetails.
        :rtype: str
        """
        return self._managed_instance_group_id

    @managed_instance_group_id.setter
    def managed_instance_group_id(self, managed_instance_group_id):
        """
        Sets the managed_instance_group_id of this CreateGroupProfileDetails.
        The OCID of the managed instance group from which the registration profile will inherit its software sources.


        :param managed_instance_group_id: The managed_instance_group_id of this CreateGroupProfileDetails.
        :type: str
        """
        self._managed_instance_group_id = managed_instance_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
