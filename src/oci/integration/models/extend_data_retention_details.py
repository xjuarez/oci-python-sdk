# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtendDataRetentionDetails(object):
    """
    Details for extending data retention for given integration instance
    """

    #: A constant which can be used with the data_retention_period property of a ExtendDataRetentionDetails.
    #: This constant has a value of "MONTHS_1"
    DATA_RETENTION_PERIOD_MONTHS_1 = "MONTHS_1"

    #: A constant which can be used with the data_retention_period property of a ExtendDataRetentionDetails.
    #: This constant has a value of "MONTHS_3"
    DATA_RETENTION_PERIOD_MONTHS_3 = "MONTHS_3"

    #: A constant which can be used with the data_retention_period property of a ExtendDataRetentionDetails.
    #: This constant has a value of "MONTHS_6"
    DATA_RETENTION_PERIOD_MONTHS_6 = "MONTHS_6"

    def __init__(self, **kwargs):
        """
        Initializes a new ExtendDataRetentionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_retention_period:
            The value to assign to the data_retention_period property of this ExtendDataRetentionDetails.
            Allowed values for this property are: "MONTHS_1", "MONTHS_3", "MONTHS_6"
        :type data_retention_period: str

        """
        self.swagger_types = {
            'data_retention_period': 'str'
        }

        self.attribute_map = {
            'data_retention_period': 'dataRetentionPeriod'
        }

        self._data_retention_period = None

    @property
    def data_retention_period(self):
        """
        **[Required]** Gets the data_retention_period of this ExtendDataRetentionDetails.
        Data retention period set for given integration instance

        Allowed values for this property are: "MONTHS_1", "MONTHS_3", "MONTHS_6"


        :return: The data_retention_period of this ExtendDataRetentionDetails.
        :rtype: str
        """
        return self._data_retention_period

    @data_retention_period.setter
    def data_retention_period(self, data_retention_period):
        """
        Sets the data_retention_period of this ExtendDataRetentionDetails.
        Data retention period set for given integration instance


        :param data_retention_period: The data_retention_period of this ExtendDataRetentionDetails.
        :type: str
        """
        allowed_values = ["MONTHS_1", "MONTHS_3", "MONTHS_6"]
        if not value_allowed_none_or_none_sentinel(data_retention_period, allowed_values):
            raise ValueError(
                f"Invalid value for `data_retention_period`, must be None or one of {allowed_values}"
            )
        self._data_retention_period = data_retention_period

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
