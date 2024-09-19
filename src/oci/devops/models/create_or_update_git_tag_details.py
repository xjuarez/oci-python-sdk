# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .create_or_update_git_ref_details import CreateOrUpdateGitRefDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOrUpdateGitTagDetails(CreateOrUpdateGitRefDetails):
    """
    The information needed to create a lightweight tag.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOrUpdateGitTagDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateOrUpdateGitTagDetails.ref_type` attribute
        of this class is ``TAG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ref_name:
            The value to assign to the ref_name property of this CreateOrUpdateGitTagDetails.
        :type ref_name: str

        :param ref_type:
            The value to assign to the ref_type property of this CreateOrUpdateGitTagDetails.
            Allowed values for this property are: "BRANCH", "TAG"
        :type ref_type: str

        :param object_id:
            The value to assign to the object_id property of this CreateOrUpdateGitTagDetails.
        :type object_id: str

        """
        self.swagger_types = {
            'ref_name': 'str',
            'ref_type': 'str',
            'object_id': 'str'
        }

        self.attribute_map = {
            'ref_name': 'refName',
            'ref_type': 'refType',
            'object_id': 'objectId'
        }

        self._ref_name = None
        self._ref_type = None
        self._object_id = None
        self._ref_type = 'TAG'

    @property
    def object_id(self):
        """
        **[Required]** Gets the object_id of this CreateOrUpdateGitTagDetails.
        SHA-1 hash value of the object pointed to by the tag.


        :return: The object_id of this CreateOrUpdateGitTagDetails.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """
        Sets the object_id of this CreateOrUpdateGitTagDetails.
        SHA-1 hash value of the object pointed to by the tag.


        :param object_id: The object_id of this CreateOrUpdateGitTagDetails.
        :type: str
        """
        self._object_id = object_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other