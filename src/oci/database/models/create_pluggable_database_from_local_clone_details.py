# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .create_pluggable_database_creation_type_details import CreatePluggableDatabaseCreationTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePluggableDatabaseFromLocalCloneDetails(CreatePluggableDatabaseCreationTypeDetails):
    """
    Specifies the creation type Local Clone.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePluggableDatabaseFromLocalCloneDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreatePluggableDatabaseFromLocalCloneDetails.creation_type` attribute
        of this class is ``LOCAL_CLONE_PDB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param creation_type:
            The value to assign to the creation_type property of this CreatePluggableDatabaseFromLocalCloneDetails.
            Allowed values for this property are: "LOCAL_CLONE_PDB", "REMOTE_CLONE_PDB", "RELOCATE_PDB"
        :type creation_type: str

        :param source_pluggable_database_id:
            The value to assign to the source_pluggable_database_id property of this CreatePluggableDatabaseFromLocalCloneDetails.
        :type source_pluggable_database_id: str

        """
        self.swagger_types = {
            'creation_type': 'str',
            'source_pluggable_database_id': 'str'
        }

        self.attribute_map = {
            'creation_type': 'creationType',
            'source_pluggable_database_id': 'sourcePluggableDatabaseId'
        }

        self._creation_type = None
        self._source_pluggable_database_id = None
        self._creation_type = 'LOCAL_CLONE_PDB'

    @property
    def source_pluggable_database_id(self):
        """
        **[Required]** Gets the source_pluggable_database_id of this CreatePluggableDatabaseFromLocalCloneDetails.
        The OCID of the Source Pluggable Database.


        :return: The source_pluggable_database_id of this CreatePluggableDatabaseFromLocalCloneDetails.
        :rtype: str
        """
        return self._source_pluggable_database_id

    @source_pluggable_database_id.setter
    def source_pluggable_database_id(self, source_pluggable_database_id):
        """
        Sets the source_pluggable_database_id of this CreatePluggableDatabaseFromLocalCloneDetails.
        The OCID of the Source Pluggable Database.


        :param source_pluggable_database_id: The source_pluggable_database_id of this CreatePluggableDatabaseFromLocalCloneDetails.
        :type: str
        """
        self._source_pluggable_database_id = source_pluggable_database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other