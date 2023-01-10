# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SnapshotDetails(object):
    """
    The details of the newly generated AWR snapshot.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SnapshotDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param snapshot_id:
            The value to assign to the snapshot_id property of this SnapshotDetails.
        :type snapshot_id: int

        """
        self.swagger_types = {
            'snapshot_id': 'int'
        }

        self.attribute_map = {
            'snapshot_id': 'snapshotId'
        }

        self._snapshot_id = None

    @property
    def snapshot_id(self):
        """
        **[Required]** Gets the snapshot_id of this SnapshotDetails.
        The ID of the beginning AWR snapshot.


        :return: The snapshot_id of this SnapshotDetails.
        :rtype: int
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """
        Sets the snapshot_id of this SnapshotDetails.
        The ID of the beginning AWR snapshot.


        :param snapshot_id: The snapshot_id of this SnapshotDetails.
        :type: int
        """
        self._snapshot_id = snapshot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
