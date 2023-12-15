# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Replica(object):
    """
    Information about a MR table replica
    """

    #: A constant which can be used with the capacity_mode property of a Replica.
    #: This constant has a value of "PROVISIONED"
    CAPACITY_MODE_PROVISIONED = "PROVISIONED"

    #: A constant which can be used with the capacity_mode property of a Replica.
    #: This constant has a value of "ON_DEMAND"
    CAPACITY_MODE_ON_DEMAND = "ON_DEMAND"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    def __init__(self, **kwargs):
        """
        Initializes a new Replica object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this Replica.
        :type region: str

        :param table_id:
            The value to assign to the table_id property of this Replica.
        :type table_id: str

        :param max_write_units:
            The value to assign to the max_write_units property of this Replica.
        :type max_write_units: int

        :param capacity_mode:
            The value to assign to the capacity_mode property of this Replica.
            Allowed values for this property are: "PROVISIONED", "ON_DEMAND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type capacity_mode: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Replica.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Replica.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'region': 'str',
            'table_id': 'str',
            'max_write_units': 'int',
            'capacity_mode': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'region': 'region',
            'table_id': 'tableId',
            'max_write_units': 'maxWriteUnits',
            'capacity_mode': 'capacityMode',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._region = None
        self._table_id = None
        self._max_write_units = None
        self._capacity_mode = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def region(self):
        """
        Gets the region of this Replica.
        A customer-facing region identifier


        :return: The region of this Replica.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Replica.
        A customer-facing region identifier


        :param region: The region of this Replica.
        :type: str
        """
        self._region = region

    @property
    def table_id(self):
        """
        Gets the table_id of this Replica.
        The OCID of the replica table


        :return: The table_id of this Replica.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """
        Sets the table_id of this Replica.
        The OCID of the replica table


        :param table_id: The table_id of this Replica.
        :type: str
        """
        self._table_id = table_id

    @property
    def max_write_units(self):
        """
        Gets the max_write_units of this Replica.
        Maximum sustained write throughput limit of the replica table.


        :return: The max_write_units of this Replica.
        :rtype: int
        """
        return self._max_write_units

    @max_write_units.setter
    def max_write_units(self, max_write_units):
        """
        Sets the max_write_units of this Replica.
        Maximum sustained write throughput limit of the replica table.


        :param max_write_units: The max_write_units of this Replica.
        :type: int
        """
        self._max_write_units = max_write_units

    @property
    def capacity_mode(self):
        """
        Gets the capacity_mode of this Replica.
        The capacity mode of the replica.

        Allowed values for this property are: "PROVISIONED", "ON_DEMAND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The capacity_mode of this Replica.
        :rtype: str
        """
        return self._capacity_mode

    @capacity_mode.setter
    def capacity_mode(self, capacity_mode):
        """
        Sets the capacity_mode of this Replica.
        The capacity mode of the replica.


        :param capacity_mode: The capacity_mode of this Replica.
        :type: str
        """
        allowed_values = ["PROVISIONED", "ON_DEMAND"]
        if not value_allowed_none_or_none_sentinel(capacity_mode, allowed_values):
            capacity_mode = 'UNKNOWN_ENUM_VALUE'
        self._capacity_mode = capacity_mode

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Replica.
        The state of the replica.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Replica.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Replica.
        The state of the replica.


        :param lifecycle_state: The lifecycle_state of this Replica.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Replica.
        A message describing the current state in more detail.


        :return: The lifecycle_details of this Replica.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Replica.
        A message describing the current state in more detail.


        :param lifecycle_details: The lifecycle_details of this Replica.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
