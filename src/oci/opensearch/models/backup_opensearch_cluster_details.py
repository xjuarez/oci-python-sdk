# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupOpensearchClusterDetails(object):
    """
    Information about an OpenSearch cluster backup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupOpensearchClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this BackupOpensearchClusterDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this BackupOpensearchClusterDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName'
        }

        self._compartment_id = None
        self._display_name = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BackupOpensearchClusterDetails.
        The OCID of the compartment where the cluster backup is located.


        :return: The compartment_id of this BackupOpensearchClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BackupOpensearchClusterDetails.
        The OCID of the compartment where the cluster backup is located.


        :param compartment_id: The compartment_id of this BackupOpensearchClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BackupOpensearchClusterDetails.
        The name of the cluster backup. Avoid entering confidential information.


        :return: The display_name of this BackupOpensearchClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BackupOpensearchClusterDetails.
        The name of the cluster backup. Avoid entering confidential information.


        :param display_name: The display_name of this BackupOpensearchClusterDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
