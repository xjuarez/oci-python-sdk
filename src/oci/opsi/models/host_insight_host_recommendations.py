# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostInsightHostRecommendations(object):
    """
    Contains recommendations depending of resource metric received.
    """

    #: A constant which can be used with the metric_recommendation_name property of a HostInsightHostRecommendations.
    #: This constant has a value of "HOST_CPU_RECOMMENDATIONS"
    METRIC_RECOMMENDATION_NAME_HOST_CPU_RECOMMENDATIONS = "HOST_CPU_RECOMMENDATIONS"

    #: A constant which can be used with the metric_recommendation_name property of a HostInsightHostRecommendations.
    #: This constant has a value of "HOST_MEMORY_RECOMMENDATIONS"
    METRIC_RECOMMENDATION_NAME_HOST_MEMORY_RECOMMENDATIONS = "HOST_MEMORY_RECOMMENDATIONS"

    #: A constant which can be used with the metric_recommendation_name property of a HostInsightHostRecommendations.
    #: This constant has a value of "HOST_NETWORK_RECOMMENDATIONS"
    METRIC_RECOMMENDATION_NAME_HOST_NETWORK_RECOMMENDATIONS = "HOST_NETWORK_RECOMMENDATIONS"

    #: A constant which can be used with the metric_recommendation_name property of a HostInsightHostRecommendations.
    #: This constant has a value of "HOST_STORAGE_RECOMMENDATIONS"
    METRIC_RECOMMENDATION_NAME_HOST_STORAGE_RECOMMENDATIONS = "HOST_STORAGE_RECOMMENDATIONS"

    def __init__(self, **kwargs):
        """
        Initializes a new HostInsightHostRecommendations object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.HostCpuRecommendations`
        * :class:`~oci.opsi.models.HostNetworkRecommendations`
        * :class:`~oci.opsi.models.HostMemoryRecommendations`
        * :class:`~oci.opsi.models.HostStorageRecommendations`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_recommendation_name:
            The value to assign to the metric_recommendation_name property of this HostInsightHostRecommendations.
            Allowed values for this property are: "HOST_CPU_RECOMMENDATIONS", "HOST_MEMORY_RECOMMENDATIONS", "HOST_NETWORK_RECOMMENDATIONS", "HOST_STORAGE_RECOMMENDATIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_recommendation_name: str

        """
        self.swagger_types = {
            'metric_recommendation_name': 'str'
        }

        self.attribute_map = {
            'metric_recommendation_name': 'metricRecommendationName'
        }

        self._metric_recommendation_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['metricRecommendationName']

        if type == 'HOST_CPU_RECOMMENDATIONS':
            return 'HostCpuRecommendations'

        if type == 'HOST_NETWORK_RECOMMENDATIONS':
            return 'HostNetworkRecommendations'

        if type == 'HOST_MEMORY_RECOMMENDATIONS':
            return 'HostMemoryRecommendations'

        if type == 'HOST_STORAGE_RECOMMENDATIONS':
            return 'HostStorageRecommendations'
        else:
            return 'HostInsightHostRecommendations'

    @property
    def metric_recommendation_name(self):
        """
        **[Required]** Gets the metric_recommendation_name of this HostInsightHostRecommendations.
        Name of recommendations depending of resource metric received.

        Allowed values for this property are: "HOST_CPU_RECOMMENDATIONS", "HOST_MEMORY_RECOMMENDATIONS", "HOST_NETWORK_RECOMMENDATIONS", "HOST_STORAGE_RECOMMENDATIONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_recommendation_name of this HostInsightHostRecommendations.
        :rtype: str
        """
        return self._metric_recommendation_name

    @metric_recommendation_name.setter
    def metric_recommendation_name(self, metric_recommendation_name):
        """
        Sets the metric_recommendation_name of this HostInsightHostRecommendations.
        Name of recommendations depending of resource metric received.


        :param metric_recommendation_name: The metric_recommendation_name of this HostInsightHostRecommendations.
        :type: str
        """
        allowed_values = ["HOST_CPU_RECOMMENDATIONS", "HOST_MEMORY_RECOMMENDATIONS", "HOST_NETWORK_RECOMMENDATIONS", "HOST_STORAGE_RECOMMENDATIONS"]
        if not value_allowed_none_or_none_sentinel(metric_recommendation_name, allowed_values):
            metric_recommendation_name = 'UNKNOWN_ENUM_VALUE'
        self._metric_recommendation_name = metric_recommendation_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other