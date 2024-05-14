# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .auto_scaling_policy_details import AutoScalingPolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThresholdBasedAutoScalingPolicyDetails(AutoScalingPolicyDetails):
    """
    Details for a threshold-based autoscaling policy to enable on the model deployment.
    In a threshold-based autoscaling policy, an autoscaling action is triggered when a performance metric meets
    or exceeds a threshold.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ThresholdBasedAutoScalingPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.ThresholdBasedAutoScalingPolicyDetails.auto_scaling_policy_type` attribute
        of this class is ``THRESHOLD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param auto_scaling_policy_type:
            The value to assign to the auto_scaling_policy_type property of this ThresholdBasedAutoScalingPolicyDetails.
            Allowed values for this property are: "THRESHOLD"
        :type auto_scaling_policy_type: str

        :param rules:
            The value to assign to the rules property of this ThresholdBasedAutoScalingPolicyDetails.
        :type rules: list[oci.data_science.models.MetricExpressionRule]

        :param maximum_instance_count:
            The value to assign to the maximum_instance_count property of this ThresholdBasedAutoScalingPolicyDetails.
        :type maximum_instance_count: int

        :param minimum_instance_count:
            The value to assign to the minimum_instance_count property of this ThresholdBasedAutoScalingPolicyDetails.
        :type minimum_instance_count: int

        :param initial_instance_count:
            The value to assign to the initial_instance_count property of this ThresholdBasedAutoScalingPolicyDetails.
        :type initial_instance_count: int

        """
        self.swagger_types = {
            'auto_scaling_policy_type': 'str',
            'rules': 'list[MetricExpressionRule]',
            'maximum_instance_count': 'int',
            'minimum_instance_count': 'int',
            'initial_instance_count': 'int'
        }

        self.attribute_map = {
            'auto_scaling_policy_type': 'autoScalingPolicyType',
            'rules': 'rules',
            'maximum_instance_count': 'maximumInstanceCount',
            'minimum_instance_count': 'minimumInstanceCount',
            'initial_instance_count': 'initialInstanceCount'
        }

        self._auto_scaling_policy_type = None
        self._rules = None
        self._maximum_instance_count = None
        self._minimum_instance_count = None
        self._initial_instance_count = None
        self._auto_scaling_policy_type = 'THRESHOLD'

    @property
    def rules(self):
        """
        **[Required]** Gets the rules of this ThresholdBasedAutoScalingPolicyDetails.
        The list of autoscaling policy rules.


        :return: The rules of this ThresholdBasedAutoScalingPolicyDetails.
        :rtype: list[oci.data_science.models.MetricExpressionRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this ThresholdBasedAutoScalingPolicyDetails.
        The list of autoscaling policy rules.


        :param rules: The rules of this ThresholdBasedAutoScalingPolicyDetails.
        :type: list[oci.data_science.models.MetricExpressionRule]
        """
        self._rules = rules

    @property
    def maximum_instance_count(self):
        """
        **[Required]** Gets the maximum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        For a threshold-based autoscaling policy, this value is the maximum number of instances the model deployment is allowed
        to increase to (scale out).


        :return: The maximum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        :rtype: int
        """
        return self._maximum_instance_count

    @maximum_instance_count.setter
    def maximum_instance_count(self, maximum_instance_count):
        """
        Sets the maximum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        For a threshold-based autoscaling policy, this value is the maximum number of instances the model deployment is allowed
        to increase to (scale out).


        :param maximum_instance_count: The maximum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        :type: int
        """
        self._maximum_instance_count = maximum_instance_count

    @property
    def minimum_instance_count(self):
        """
        **[Required]** Gets the minimum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        For a threshold-based autoscaling policy, this value is the minimum number of instances the model deployment is allowed
        to decrease to (scale in).


        :return: The minimum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        :rtype: int
        """
        return self._minimum_instance_count

    @minimum_instance_count.setter
    def minimum_instance_count(self, minimum_instance_count):
        """
        Sets the minimum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        For a threshold-based autoscaling policy, this value is the minimum number of instances the model deployment is allowed
        to decrease to (scale in).


        :param minimum_instance_count: The minimum_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        :type: int
        """
        self._minimum_instance_count = minimum_instance_count

    @property
    def initial_instance_count(self):
        """
        **[Required]** Gets the initial_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the model deployment
        immediately after autoscaling is enabled. Note that anytime this value is updated, the number of instances will be reset
        to this value. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from
        this initial number to a number that is based on the limits that you set.


        :return: The initial_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        :rtype: int
        """
        return self._initial_instance_count

    @initial_instance_count.setter
    def initial_instance_count(self, initial_instance_count):
        """
        Sets the initial_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the model deployment
        immediately after autoscaling is enabled. Note that anytime this value is updated, the number of instances will be reset
        to this value. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from
        this initial number to a number that is based on the limits that you set.


        :param initial_instance_count: The initial_instance_count of this ThresholdBasedAutoScalingPolicyDetails.
        :type: int
        """
        self._initial_instance_count = initial_instance_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
