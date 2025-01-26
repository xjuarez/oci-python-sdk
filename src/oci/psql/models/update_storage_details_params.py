# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStorageDetailsParams(object):
    """
    Storage details of the database system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStorageDetailsParams object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param iops:
            The value to assign to the iops property of this UpdateStorageDetailsParams.
        :type iops: int

        """
        self.swagger_types = {
            'iops': 'int'
        }

        self.attribute_map = {
            'iops': 'iops'
        }

        self._iops = None

    @property
    def iops(self):
        """
        Gets the iops of this UpdateStorageDetailsParams.
        Guaranteed input/output storage requests per second (IOPS) available to the database system.
        Only valid for `OCI_OPTIMIZED_STORAGE` database system type.


        :return: The iops of this UpdateStorageDetailsParams.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """
        Sets the iops of this UpdateStorageDetailsParams.
        Guaranteed input/output storage requests per second (IOPS) available to the database system.
        Only valid for `OCI_OPTIMIZED_STORAGE` database system type.


        :param iops: The iops of this UpdateStorageDetailsParams.
        :type: int
        """
        self._iops = iops

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
