# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .create_deploy_stage_details import CreateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails(CreateDeployStageDetails):
    """
    Specifies the instance group canary deployment load balancer traffic shift stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.deploy_stage_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type deploy_pipeline_id: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param compute_instance_group_canary_deploy_stage_id:
            The value to assign to the compute_instance_group_canary_deploy_stage_id property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type compute_instance_group_canary_deploy_stage_id: str

        :param rollout_policy:
            The value to assign to the rollout_policy property of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type rollout_policy: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_pipeline_id': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'compute_instance_group_canary_deploy_stage_id': 'str',
            'rollout_policy': 'LoadBalancerTrafficShiftRolloutPolicy'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_pipeline_id': 'deployPipelineId',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'compute_instance_group_canary_deploy_stage_id': 'computeInstanceGroupCanaryDeployStageId',
            'rollout_policy': 'rolloutPolicy'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_pipeline_id = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._compute_instance_group_canary_deploy_stage_id = None
        self._rollout_policy = None
        self._deploy_stage_type = 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT'

    @property
    def compute_instance_group_canary_deploy_stage_id(self):
        """
        **[Required]** Gets the compute_instance_group_canary_deploy_stage_id of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        A compute instance group canary stage OCID for load balancer.


        :return: The compute_instance_group_canary_deploy_stage_id of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :rtype: str
        """
        return self._compute_instance_group_canary_deploy_stage_id

    @compute_instance_group_canary_deploy_stage_id.setter
    def compute_instance_group_canary_deploy_stage_id(self, compute_instance_group_canary_deploy_stage_id):
        """
        Sets the compute_instance_group_canary_deploy_stage_id of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        A compute instance group canary stage OCID for load balancer.


        :param compute_instance_group_canary_deploy_stage_id: The compute_instance_group_canary_deploy_stage_id of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type: str
        """
        self._compute_instance_group_canary_deploy_stage_id = compute_instance_group_canary_deploy_stage_id

    @property
    def rollout_policy(self):
        """
        **[Required]** Gets the rollout_policy of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.

        :return: The rollout_policy of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :rtype: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy
        """
        return self._rollout_policy

    @rollout_policy.setter
    def rollout_policy(self, rollout_policy):
        """
        Sets the rollout_policy of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.

        :param rollout_policy: The rollout_policy of this CreateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails.
        :type: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy
        """
        self._rollout_policy = rollout_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
