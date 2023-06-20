# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatastoreSummary(object):
    """
    Datastore summary for a getting an Sddc.
    """

    #: A constant which can be used with the datastore_type property of a DatastoreSummary.
    #: This constant has a value of "MANAGEMENT"
    DATASTORE_TYPE_MANAGEMENT = "MANAGEMENT"

    #: A constant which can be used with the datastore_type property of a DatastoreSummary.
    #: This constant has a value of "WORKLOAD"
    DATASTORE_TYPE_WORKLOAD = "WORKLOAD"

    def __init__(self, **kwargs):
        """
        Initializes a new DatastoreSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param block_volume_ids:
            The value to assign to the block_volume_ids property of this DatastoreSummary.
        :type block_volume_ids: list[str]

        :param datastore_type:
            The value to assign to the datastore_type property of this DatastoreSummary.
            Allowed values for this property are: "MANAGEMENT", "WORKLOAD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type datastore_type: str

        :param capacity:
            The value to assign to the capacity property of this DatastoreSummary.
        :type capacity: float

        """
        self.swagger_types = {
            'block_volume_ids': 'list[str]',
            'datastore_type': 'str',
            'capacity': 'float'
        }

        self.attribute_map = {
            'block_volume_ids': 'blockVolumeIds',
            'datastore_type': 'datastoreType',
            'capacity': 'capacity'
        }

        self._block_volume_ids = None
        self._datastore_type = None
        self._capacity = None

    @property
    def block_volume_ids(self):
        """
        **[Required]** Gets the block_volume_ids of this DatastoreSummary.
        A list of `OCID`__s of Block Storage Volumes.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The block_volume_ids of this DatastoreSummary.
        :rtype: list[str]
        """
        return self._block_volume_ids

    @block_volume_ids.setter
    def block_volume_ids(self, block_volume_ids):
        """
        Sets the block_volume_ids of this DatastoreSummary.
        A list of `OCID`__s of Block Storage Volumes.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param block_volume_ids: The block_volume_ids of this DatastoreSummary.
        :type: list[str]
        """
        self._block_volume_ids = block_volume_ids

    @property
    def datastore_type(self):
        """
        **[Required]** Gets the datastore_type of this DatastoreSummary.
        Type of the datastore.

        Allowed values for this property are: "MANAGEMENT", "WORKLOAD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The datastore_type of this DatastoreSummary.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """
        Sets the datastore_type of this DatastoreSummary.
        Type of the datastore.


        :param datastore_type: The datastore_type of this DatastoreSummary.
        :type: str
        """
        allowed_values = ["MANAGEMENT", "WORKLOAD"]
        if not value_allowed_none_or_none_sentinel(datastore_type, allowed_values):
            datastore_type = 'UNKNOWN_ENUM_VALUE'
        self._datastore_type = datastore_type

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this DatastoreSummary.
        Size of the Block Storage Volume in GB.


        :return: The capacity of this DatastoreSummary.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this DatastoreSummary.
        Size of the Block Storage Volume in GB.


        :param capacity: The capacity of this DatastoreSummary.
        :type: float
        """
        self._capacity = capacity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
