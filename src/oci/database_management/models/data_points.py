# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataPoints(object):
    """
    The aggregated datapoints of the metric.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataPoints object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this DataPoints.
        :type timestamp: datetime

        :param value:
            The value to assign to the value property of this DataPoints.
        :type value: float

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'value': 'float'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'value': 'value'
        }

        self._timestamp = None
        self._value = None

    @property
    def timestamp(self):
        """
        Gets the timestamp of this DataPoints.
        The data point date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :return: The timestamp of this DataPoints.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this DataPoints.
        The data point date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :param timestamp: The timestamp of this DataPoints.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def value(self):
        """
        Gets the value of this DataPoints.
        The value of the metric.


        :return: The value of this DataPoints.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DataPoints.
        The value of the metric.


        :param value: The value of this DataPoints.
        :type: float
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
