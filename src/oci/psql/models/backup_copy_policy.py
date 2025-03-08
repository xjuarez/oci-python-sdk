# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupCopyPolicy(object):
    """
    Backup copy details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupCopyPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this BackupCopyPolicy.
        :type compartment_id: str

        :param retention_period:
            The value to assign to the retention_period property of this BackupCopyPolicy.
        :type retention_period: int

        :param regions:
            The value to assign to the regions property of this BackupCopyPolicy.
        :type regions: list[str]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'retention_period': 'int',
            'regions': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'retention_period': 'retentionPeriod',
            'regions': 'regions'
        }

        self._compartment_id = None
        self._retention_period = None
        self._regions = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BackupCopyPolicy.
        target compartment to place a new backup


        :return: The compartment_id of this BackupCopyPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BackupCopyPolicy.
        target compartment to place a new backup


        :param compartment_id: The compartment_id of this BackupCopyPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def retention_period(self):
        """
        Gets the retention_period of this BackupCopyPolicy.
        Retention period in days of the backup copy.


        :return: The retention_period of this BackupCopyPolicy.
        :rtype: int
        """
        return self._retention_period

    @retention_period.setter
    def retention_period(self, retention_period):
        """
        Sets the retention_period of this BackupCopyPolicy.
        Retention period in days of the backup copy.


        :param retention_period: The retention_period of this BackupCopyPolicy.
        :type: int
        """
        self._retention_period = retention_period

    @property
    def regions(self):
        """
        Gets the regions of this BackupCopyPolicy.
        List of region names of the remote region


        :return: The regions of this BackupCopyPolicy.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this BackupCopyPolicy.
        List of region names of the remote region


        :param regions: The regions of this BackupCopyPolicy.
        :type: list[str]
        """
        self._regions = regions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
