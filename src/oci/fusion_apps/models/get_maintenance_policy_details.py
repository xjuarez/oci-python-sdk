# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GetMaintenancePolicyDetails(object):
    """
    The policy that specifies the maintenance and upgrade preferences for an environment. For more information about the options, see `Understanding Environment Maintenance`__.

    __ https://docs.cloud.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm#about-env-maintenance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GetMaintenancePolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param quarterly_upgrade_begin_times:
            The value to assign to the quarterly_upgrade_begin_times property of this GetMaintenancePolicyDetails.
        :type quarterly_upgrade_begin_times: oci.fusion_apps.models.QuarterlyUpgradeBeginTimes

        :param monthly_patching_override:
            The value to assign to the monthly_patching_override property of this GetMaintenancePolicyDetails.
        :type monthly_patching_override: str

        :param environment_maintenance_override:
            The value to assign to the environment_maintenance_override property of this GetMaintenancePolicyDetails.
        :type environment_maintenance_override: str

        """
        self.swagger_types = {
            'quarterly_upgrade_begin_times': 'QuarterlyUpgradeBeginTimes',
            'monthly_patching_override': 'str',
            'environment_maintenance_override': 'str'
        }

        self.attribute_map = {
            'quarterly_upgrade_begin_times': 'quarterlyUpgradeBeginTimes',
            'monthly_patching_override': 'monthlyPatchingOverride',
            'environment_maintenance_override': 'environmentMaintenanceOverride'
        }

        self._quarterly_upgrade_begin_times = None
        self._monthly_patching_override = None
        self._environment_maintenance_override = None

    @property
    def quarterly_upgrade_begin_times(self):
        """
        Gets the quarterly_upgrade_begin_times of this GetMaintenancePolicyDetails.

        :return: The quarterly_upgrade_begin_times of this GetMaintenancePolicyDetails.
        :rtype: oci.fusion_apps.models.QuarterlyUpgradeBeginTimes
        """
        return self._quarterly_upgrade_begin_times

    @quarterly_upgrade_begin_times.setter
    def quarterly_upgrade_begin_times(self, quarterly_upgrade_begin_times):
        """
        Sets the quarterly_upgrade_begin_times of this GetMaintenancePolicyDetails.

        :param quarterly_upgrade_begin_times: The quarterly_upgrade_begin_times of this GetMaintenancePolicyDetails.
        :type: oci.fusion_apps.models.QuarterlyUpgradeBeginTimes
        """
        self._quarterly_upgrade_begin_times = quarterly_upgrade_begin_times

    @property
    def monthly_patching_override(self):
        """
        Gets the monthly_patching_override of this GetMaintenancePolicyDetails.
        Whether the Fusion environment will be updated monthly or updated on the quarterly cycle. This setting overrides the monthly patching setting of its Fusion environment family.


        :return: The monthly_patching_override of this GetMaintenancePolicyDetails.
        :rtype: str
        """
        return self._monthly_patching_override

    @monthly_patching_override.setter
    def monthly_patching_override(self, monthly_patching_override):
        """
        Sets the monthly_patching_override of this GetMaintenancePolicyDetails.
        Whether the Fusion environment will be updated monthly or updated on the quarterly cycle. This setting overrides the monthly patching setting of its Fusion environment family.


        :param monthly_patching_override: The monthly_patching_override of this GetMaintenancePolicyDetails.
        :type: str
        """
        self._monthly_patching_override = monthly_patching_override

    @property
    def environment_maintenance_override(self):
        """
        Gets the environment_maintenance_override of this GetMaintenancePolicyDetails.
        User choice to upgrade both production and non-production environments at the same time. Overrides the Fusion environment family setting.


        :return: The environment_maintenance_override of this GetMaintenancePolicyDetails.
        :rtype: str
        """
        return self._environment_maintenance_override

    @environment_maintenance_override.setter
    def environment_maintenance_override(self, environment_maintenance_override):
        """
        Sets the environment_maintenance_override of this GetMaintenancePolicyDetails.
        User choice to upgrade both production and non-production environments at the same time. Overrides the Fusion environment family setting.


        :param environment_maintenance_override: The environment_maintenance_override of this GetMaintenancePolicyDetails.
        :type: str
        """
        self._environment_maintenance_override = environment_maintenance_override

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
