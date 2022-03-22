# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage_summary import DeployStageSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupDeployStageSummary(DeployStageSummary):
    """
    Specifies the instance group rolling deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupDeployStageSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupDeployStageSummary.deploy_stage_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ComputeInstanceGroupDeployStageSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this ComputeInstanceGroupDeployStageSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this ComputeInstanceGroupDeployStageSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this ComputeInstanceGroupDeployStageSummary.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this ComputeInstanceGroupDeployStageSummary.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeInstanceGroupDeployStageSummary.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this ComputeInstanceGroupDeployStageSummary.
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this ComputeInstanceGroupDeployStageSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputeInstanceGroupDeployStageSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeInstanceGroupDeployStageSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ComputeInstanceGroupDeployStageSummary.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this ComputeInstanceGroupDeployStageSummary.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeInstanceGroupDeployStageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeInstanceGroupDeployStageSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ComputeInstanceGroupDeployStageSummary.
        :type system_tags: dict(str, dict(str, object))

        :param compute_instance_group_deploy_environment_id:
            The value to assign to the compute_instance_group_deploy_environment_id property of this ComputeInstanceGroupDeployStageSummary.
        :type compute_instance_group_deploy_environment_id: str

        :param deployment_spec_deploy_artifact_id:
            The value to assign to the deployment_spec_deploy_artifact_id property of this ComputeInstanceGroupDeployStageSummary.
        :type deployment_spec_deploy_artifact_id: str

        :param deploy_artifact_ids:
            The value to assign to the deploy_artifact_ids property of this ComputeInstanceGroupDeployStageSummary.
        :type deploy_artifact_ids: list[str]

        :param rollout_policy:
            The value to assign to the rollout_policy property of this ComputeInstanceGroupDeployStageSummary.
        :type rollout_policy: oci.devops.models.ComputeInstanceGroupRolloutPolicy

        :param rollback_policy:
            The value to assign to the rollback_policy property of this ComputeInstanceGroupDeployStageSummary.
        :type rollback_policy: oci.devops.models.DeployStageRollbackPolicy

        :param failure_policy:
            The value to assign to the failure_policy property of this ComputeInstanceGroupDeployStageSummary.
        :type failure_policy: oci.devops.models.ComputeInstanceGroupFailurePolicy

        :param load_balancer_config:
            The value to assign to the load_balancer_config property of this ComputeInstanceGroupDeployStageSummary.
        :type load_balancer_config: oci.devops.models.LoadBalancerConfig

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'compute_instance_group_deploy_environment_id': 'str',
            'deployment_spec_deploy_artifact_id': 'str',
            'deploy_artifact_ids': 'list[str]',
            'rollout_policy': 'ComputeInstanceGroupRolloutPolicy',
            'rollback_policy': 'DeployStageRollbackPolicy',
            'failure_policy': 'ComputeInstanceGroupFailurePolicy',
            'load_balancer_config': 'LoadBalancerConfig'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'compute_instance_group_deploy_environment_id': 'computeInstanceGroupDeployEnvironmentId',
            'deployment_spec_deploy_artifact_id': 'deploymentSpecDeployArtifactId',
            'deploy_artifact_ids': 'deployArtifactIds',
            'rollout_policy': 'rolloutPolicy',
            'rollback_policy': 'rollbackPolicy',
            'failure_policy': 'failurePolicy',
            'load_balancer_config': 'loadBalancerConfig'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._compute_instance_group_deploy_environment_id = None
        self._deployment_spec_deploy_artifact_id = None
        self._deploy_artifact_ids = None
        self._rollout_policy = None
        self._rollback_policy = None
        self._failure_policy = None
        self._load_balancer_config = None
        self._deploy_stage_type = 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'

    @property
    def compute_instance_group_deploy_environment_id(self):
        """
        **[Required]** Gets the compute_instance_group_deploy_environment_id of this ComputeInstanceGroupDeployStageSummary.
        A compute instance group environment OCID for rolling deployment.


        :return: The compute_instance_group_deploy_environment_id of this ComputeInstanceGroupDeployStageSummary.
        :rtype: str
        """
        return self._compute_instance_group_deploy_environment_id

    @compute_instance_group_deploy_environment_id.setter
    def compute_instance_group_deploy_environment_id(self, compute_instance_group_deploy_environment_id):
        """
        Sets the compute_instance_group_deploy_environment_id of this ComputeInstanceGroupDeployStageSummary.
        A compute instance group environment OCID for rolling deployment.


        :param compute_instance_group_deploy_environment_id: The compute_instance_group_deploy_environment_id of this ComputeInstanceGroupDeployStageSummary.
        :type: str
        """
        self._compute_instance_group_deploy_environment_id = compute_instance_group_deploy_environment_id

    @property
    def deployment_spec_deploy_artifact_id(self):
        """
        **[Required]** Gets the deployment_spec_deploy_artifact_id of this ComputeInstanceGroupDeployStageSummary.
        The OCID of the artifact that contains the deployment specification.


        :return: The deployment_spec_deploy_artifact_id of this ComputeInstanceGroupDeployStageSummary.
        :rtype: str
        """
        return self._deployment_spec_deploy_artifact_id

    @deployment_spec_deploy_artifact_id.setter
    def deployment_spec_deploy_artifact_id(self, deployment_spec_deploy_artifact_id):
        """
        Sets the deployment_spec_deploy_artifact_id of this ComputeInstanceGroupDeployStageSummary.
        The OCID of the artifact that contains the deployment specification.


        :param deployment_spec_deploy_artifact_id: The deployment_spec_deploy_artifact_id of this ComputeInstanceGroupDeployStageSummary.
        :type: str
        """
        self._deployment_spec_deploy_artifact_id = deployment_spec_deploy_artifact_id

    @property
    def deploy_artifact_ids(self):
        """
        Gets the deploy_artifact_ids of this ComputeInstanceGroupDeployStageSummary.
        Additional file artifact OCIDs.


        :return: The deploy_artifact_ids of this ComputeInstanceGroupDeployStageSummary.
        :rtype: list[str]
        """
        return self._deploy_artifact_ids

    @deploy_artifact_ids.setter
    def deploy_artifact_ids(self, deploy_artifact_ids):
        """
        Sets the deploy_artifact_ids of this ComputeInstanceGroupDeployStageSummary.
        Additional file artifact OCIDs.


        :param deploy_artifact_ids: The deploy_artifact_ids of this ComputeInstanceGroupDeployStageSummary.
        :type: list[str]
        """
        self._deploy_artifact_ids = deploy_artifact_ids

    @property
    def rollout_policy(self):
        """
        **[Required]** Gets the rollout_policy of this ComputeInstanceGroupDeployStageSummary.

        :return: The rollout_policy of this ComputeInstanceGroupDeployStageSummary.
        :rtype: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        return self._rollout_policy

    @rollout_policy.setter
    def rollout_policy(self, rollout_policy):
        """
        Sets the rollout_policy of this ComputeInstanceGroupDeployStageSummary.

        :param rollout_policy: The rollout_policy of this ComputeInstanceGroupDeployStageSummary.
        :type: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        self._rollout_policy = rollout_policy

    @property
    def rollback_policy(self):
        """
        Gets the rollback_policy of this ComputeInstanceGroupDeployStageSummary.

        :return: The rollback_policy of this ComputeInstanceGroupDeployStageSummary.
        :rtype: oci.devops.models.DeployStageRollbackPolicy
        """
        return self._rollback_policy

    @rollback_policy.setter
    def rollback_policy(self, rollback_policy):
        """
        Sets the rollback_policy of this ComputeInstanceGroupDeployStageSummary.

        :param rollback_policy: The rollback_policy of this ComputeInstanceGroupDeployStageSummary.
        :type: oci.devops.models.DeployStageRollbackPolicy
        """
        self._rollback_policy = rollback_policy

    @property
    def failure_policy(self):
        """
        Gets the failure_policy of this ComputeInstanceGroupDeployStageSummary.

        :return: The failure_policy of this ComputeInstanceGroupDeployStageSummary.
        :rtype: oci.devops.models.ComputeInstanceGroupFailurePolicy
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """
        Sets the failure_policy of this ComputeInstanceGroupDeployStageSummary.

        :param failure_policy: The failure_policy of this ComputeInstanceGroupDeployStageSummary.
        :type: oci.devops.models.ComputeInstanceGroupFailurePolicy
        """
        self._failure_policy = failure_policy

    @property
    def load_balancer_config(self):
        """
        Gets the load_balancer_config of this ComputeInstanceGroupDeployStageSummary.

        :return: The load_balancer_config of this ComputeInstanceGroupDeployStageSummary.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._load_balancer_config

    @load_balancer_config.setter
    def load_balancer_config(self, load_balancer_config):
        """
        Sets the load_balancer_config of this ComputeInstanceGroupDeployStageSummary.

        :param load_balancer_config: The load_balancer_config of this ComputeInstanceGroupDeployStageSummary.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._load_balancer_config = load_balancer_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other