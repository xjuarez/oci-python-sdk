# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .host_insight_host_recommendations import HostInsightHostRecommendations
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostCpuRecommendations(HostInsightHostRecommendations):
    """
    Contains CPU recommendation.
    """

    #: A constant which can be used with the burstable property of a HostCpuRecommendations.
    #: This constant has a value of "BASELINE_1_8"
    BURSTABLE_BASELINE_1_8 = "BASELINE_1_8"

    #: A constant which can be used with the burstable property of a HostCpuRecommendations.
    #: This constant has a value of "BASELINE_1_2"
    BURSTABLE_BASELINE_1_2 = "BASELINE_1_2"

    #: A constant which can be used with the burstable property of a HostCpuRecommendations.
    #: This constant has a value of "NO_RECOMMENDATION"
    BURSTABLE_NO_RECOMMENDATION = "NO_RECOMMENDATION"

    #: A constant which can be used with the burstable property of a HostCpuRecommendations.
    #: This constant has a value of "DISABLE_BURSTABLE"
    BURSTABLE_DISABLE_BURSTABLE = "DISABLE_BURSTABLE"

    #: A constant which can be used with the unused_instance property of a HostCpuRecommendations.
    #: This constant has a value of "IN_USE"
    UNUSED_INSTANCE_IN_USE = "IN_USE"

    #: A constant which can be used with the unused_instance property of a HostCpuRecommendations.
    #: This constant has a value of "NOT_IN_USE"
    UNUSED_INSTANCE_NOT_IN_USE = "NOT_IN_USE"

    #: A constant which can be used with the unused_instance property of a HostCpuRecommendations.
    #: This constant has a value of "IS_NOT_DETERMINED"
    UNUSED_INSTANCE_IS_NOT_DETERMINED = "IS_NOT_DETERMINED"

    def __init__(self, **kwargs):
        """
        Initializes a new HostCpuRecommendations object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostCpuRecommendations.metric_recommendation_name` attribute
        of this class is ``HOST_CPU_RECOMMENDATIONS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_recommendation_name:
            The value to assign to the metric_recommendation_name property of this HostCpuRecommendations.
            Allowed values for this property are: "HOST_CPU_RECOMMENDATIONS", "HOST_MEMORY_RECOMMENDATIONS", "HOST_NETWORK_RECOMMENDATIONS", "HOST_STORAGE_RECOMMENDATIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_recommendation_name: str

        :param burstable:
            The value to assign to the burstable property of this HostCpuRecommendations.
            Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "NO_RECOMMENDATION", "DISABLE_BURSTABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type burstable: str

        :param shape:
            The value to assign to the shape property of this HostCpuRecommendations.
        :type shape: str

        :param unused_instance:
            The value to assign to the unused_instance property of this HostCpuRecommendations.
            Allowed values for this property are: "IN_USE", "NOT_IN_USE", "IS_NOT_DETERMINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unused_instance: str

        :param is_abandoned_instance:
            The value to assign to the is_abandoned_instance property of this HostCpuRecommendations.
        :type is_abandoned_instance: bool

        """
        self.swagger_types = {
            'metric_recommendation_name': 'str',
            'burstable': 'str',
            'shape': 'str',
            'unused_instance': 'str',
            'is_abandoned_instance': 'bool'
        }

        self.attribute_map = {
            'metric_recommendation_name': 'metricRecommendationName',
            'burstable': 'burstable',
            'shape': 'shape',
            'unused_instance': 'unusedInstance',
            'is_abandoned_instance': 'isAbandonedInstance'
        }

        self._metric_recommendation_name = None
        self._burstable = None
        self._shape = None
        self._unused_instance = None
        self._is_abandoned_instance = None
        self._metric_recommendation_name = 'HOST_CPU_RECOMMENDATIONS'

    @property
    def burstable(self):
        """
        Gets the burstable of this HostCpuRecommendations.
        Show if OPSI recommends to convert an instance to a burstable instance and show recommended cpu baseline if positive recommendation.

        Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "NO_RECOMMENDATION", "DISABLE_BURSTABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The burstable of this HostCpuRecommendations.
        :rtype: str
        """
        return self._burstable

    @burstable.setter
    def burstable(self, burstable):
        """
        Sets the burstable of this HostCpuRecommendations.
        Show if OPSI recommends to convert an instance to a burstable instance and show recommended cpu baseline if positive recommendation.


        :param burstable: The burstable of this HostCpuRecommendations.
        :type: str
        """
        allowed_values = ["BASELINE_1_8", "BASELINE_1_2", "NO_RECOMMENDATION", "DISABLE_BURSTABLE"]
        if not value_allowed_none_or_none_sentinel(burstable, allowed_values):
            burstable = 'UNKNOWN_ENUM_VALUE'
        self._burstable = burstable

    @property
    def shape(self):
        """
        Gets the shape of this HostCpuRecommendations.
        Show if OPSI recommends to change the shape of an instance and show recommended shape based on CPU utilization.


        :return: The shape of this HostCpuRecommendations.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this HostCpuRecommendations.
        Show if OPSI recommends to change the shape of an instance and show recommended shape based on CPU utilization.


        :param shape: The shape of this HostCpuRecommendations.
        :type: str
        """
        self._shape = shape

    @property
    def unused_instance(self):
        """
        Gets the unused_instance of this HostCpuRecommendations.
        Identify unused instances based on cpu, memory and network metrics.

        Allowed values for this property are: "IN_USE", "NOT_IN_USE", "IS_NOT_DETERMINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unused_instance of this HostCpuRecommendations.
        :rtype: str
        """
        return self._unused_instance

    @unused_instance.setter
    def unused_instance(self, unused_instance):
        """
        Sets the unused_instance of this HostCpuRecommendations.
        Identify unused instances based on cpu, memory and network metrics.


        :param unused_instance: The unused_instance of this HostCpuRecommendations.
        :type: str
        """
        allowed_values = ["IN_USE", "NOT_IN_USE", "IS_NOT_DETERMINED"]
        if not value_allowed_none_or_none_sentinel(unused_instance, allowed_values):
            unused_instance = 'UNKNOWN_ENUM_VALUE'
        self._unused_instance = unused_instance

    @property
    def is_abandoned_instance(self):
        """
        Gets the is_abandoned_instance of this HostCpuRecommendations.
        Identify if an instance is abandoned.


        :return: The is_abandoned_instance of this HostCpuRecommendations.
        :rtype: bool
        """
        return self._is_abandoned_instance

    @is_abandoned_instance.setter
    def is_abandoned_instance(self, is_abandoned_instance):
        """
        Sets the is_abandoned_instance of this HostCpuRecommendations.
        Identify if an instance is abandoned.


        :param is_abandoned_instance: The is_abandoned_instance of this HostCpuRecommendations.
        :type: bool
        """
        self._is_abandoned_instance = is_abandoned_instance

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other