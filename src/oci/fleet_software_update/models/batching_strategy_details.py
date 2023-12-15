# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BatchingStrategyDetails(object):
    """
    Batching strategy details to use during PRECHECK and APPLY Cycle Actions.
    """

    #: A constant which can be used with the type property of a BatchingStrategyDetails.
    #: This constant has a value of "SEQUENTIAL"
    TYPE_SEQUENTIAL = "SEQUENTIAL"

    #: A constant which can be used with the type property of a BatchingStrategyDetails.
    #: This constant has a value of "FIFTY_FIFTY"
    TYPE_FIFTY_FIFTY = "FIFTY_FIFTY"

    #: A constant which can be used with the type property of a BatchingStrategyDetails.
    #: This constant has a value of "SERVICE_AVAILABILITY_FACTOR"
    TYPE_SERVICE_AVAILABILITY_FACTOR = "SERVICE_AVAILABILITY_FACTOR"

    #: A constant which can be used with the type property of a BatchingStrategyDetails.
    #: This constant has a value of "NON_ROLLING"
    TYPE_NON_ROLLING = "NON_ROLLING"

    def __init__(self, **kwargs):
        """
        Initializes a new BatchingStrategyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.NonRollingBatchingStrategyDetails`
        * :class:`~oci.fleet_software_update.models.ServiceAvailabilityFactorBatchingStrategyDetails`
        * :class:`~oci.fleet_software_update.models.SequentialBatchingStrategyDetails`
        * :class:`~oci.fleet_software_update.models.FiftyFiftyBatchingStrategyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BatchingStrategyDetails.
            Allowed values for this property are: "SEQUENTIAL", "FIFTY_FIFTY", "SERVICE_AVAILABILITY_FACTOR", "NON_ROLLING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'NON_ROLLING':
            return 'NonRollingBatchingStrategyDetails'

        if type == 'SERVICE_AVAILABILITY_FACTOR':
            return 'ServiceAvailabilityFactorBatchingStrategyDetails'

        if type == 'SEQUENTIAL':
            return 'SequentialBatchingStrategyDetails'

        if type == 'FIFTY_FIFTY':
            return 'FiftyFiftyBatchingStrategyDetails'
        else:
            return 'BatchingStrategyDetails'

    @property
    def type(self):
        """
        Gets the type of this BatchingStrategyDetails.
        Supported batching strategies.

        Allowed values for this property are: "SEQUENTIAL", "FIFTY_FIFTY", "SERVICE_AVAILABILITY_FACTOR", "NON_ROLLING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this BatchingStrategyDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BatchingStrategyDetails.
        Supported batching strategies.


        :param type: The type of this BatchingStrategyDetails.
        :type: str
        """
        allowed_values = ["SEQUENTIAL", "FIFTY_FIFTY", "SERVICE_AVAILABILITY_FACTOR", "NON_ROLLING"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
