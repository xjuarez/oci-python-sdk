# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectConfiguration(object):
    """
    A configuration to define the constraints when detecting vulnerable dependencies.
    """

    #: A constant which can be used with the upgrade_policy property of a DetectConfiguration.
    #: This constant has a value of "NEAREST"
    UPGRADE_POLICY_NEAREST = "NEAREST"

    def __init__(self, **kwargs):
        """
        Initializes a new DetectConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exclusions:
            The value to assign to the exclusions property of this DetectConfiguration.
        :type exclusions: list[str]

        :param upgrade_policy:
            The value to assign to the upgrade_policy property of this DetectConfiguration.
            Allowed values for this property are: "NEAREST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type upgrade_policy: str

        :param max_permissible_cvss_v2_score:
            The value to assign to the max_permissible_cvss_v2_score property of this DetectConfiguration.
        :type max_permissible_cvss_v2_score: float

        :param max_permissible_cvss_v3_score:
            The value to assign to the max_permissible_cvss_v3_score property of this DetectConfiguration.
        :type max_permissible_cvss_v3_score: float

        """
        self.swagger_types = {
            'exclusions': 'list[str]',
            'upgrade_policy': 'str',
            'max_permissible_cvss_v2_score': 'float',
            'max_permissible_cvss_v3_score': 'float'
        }

        self.attribute_map = {
            'exclusions': 'exclusions',
            'upgrade_policy': 'upgradePolicy',
            'max_permissible_cvss_v2_score': 'maxPermissibleCvssV2Score',
            'max_permissible_cvss_v3_score': 'maxPermissibleCvssV3Score'
        }

        self._exclusions = None
        self._upgrade_policy = None
        self._max_permissible_cvss_v2_score = None
        self._max_permissible_cvss_v3_score = None

    @property
    def exclusions(self):
        """
        Gets the exclusions of this DetectConfiguration.
        The list of dependencies to be ignored by the recommendation algorithm. The dependency pattern is matched against the 'group:artifact:version' or the purl of a dependency.
        An asterisk (*) at the end in the dependency pattern acts as a wildcard and matches zero or more characters.


        :return: The exclusions of this DetectConfiguration.
        :rtype: list[str]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """
        Sets the exclusions of this DetectConfiguration.
        The list of dependencies to be ignored by the recommendation algorithm. The dependency pattern is matched against the 'group:artifact:version' or the purl of a dependency.
        An asterisk (*) at the end in the dependency pattern acts as a wildcard and matches zero or more characters.


        :param exclusions: The exclusions of this DetectConfiguration.
        :type: list[str]
        """
        self._exclusions = exclusions

    @property
    def upgrade_policy(self):
        """
        Gets the upgrade_policy of this DetectConfiguration.
        The upgrade policy for recommendations.
        The `Nearest` upgrade policy upgrades a dependency to the oldest version that meets both of the following criteria: it is newer than the current version and it is not affected by a vulnerability.

        Allowed values for this property are: "NEAREST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The upgrade_policy of this DetectConfiguration.
        :rtype: str
        """
        return self._upgrade_policy

    @upgrade_policy.setter
    def upgrade_policy(self, upgrade_policy):
        """
        Sets the upgrade_policy of this DetectConfiguration.
        The upgrade policy for recommendations.
        The `Nearest` upgrade policy upgrades a dependency to the oldest version that meets both of the following criteria: it is newer than the current version and it is not affected by a vulnerability.


        :param upgrade_policy: The upgrade_policy of this DetectConfiguration.
        :type: str
        """
        allowed_values = ["NEAREST"]
        if not value_allowed_none_or_none_sentinel(upgrade_policy, allowed_values):
            upgrade_policy = 'UNKNOWN_ENUM_VALUE'
        self._upgrade_policy = upgrade_policy

    @property
    def max_permissible_cvss_v2_score(self):
        """
        Gets the max_permissible_cvss_v2_score of this DetectConfiguration.
        The maximum Common Vulnerability Scoring System Version 2 (CVSS V2) score. An artifact with a CVSS V2 score below this value is not considered for patching.


        :return: The max_permissible_cvss_v2_score of this DetectConfiguration.
        :rtype: float
        """
        return self._max_permissible_cvss_v2_score

    @max_permissible_cvss_v2_score.setter
    def max_permissible_cvss_v2_score(self, max_permissible_cvss_v2_score):
        """
        Sets the max_permissible_cvss_v2_score of this DetectConfiguration.
        The maximum Common Vulnerability Scoring System Version 2 (CVSS V2) score. An artifact with a CVSS V2 score below this value is not considered for patching.


        :param max_permissible_cvss_v2_score: The max_permissible_cvss_v2_score of this DetectConfiguration.
        :type: float
        """
        self._max_permissible_cvss_v2_score = max_permissible_cvss_v2_score

    @property
    def max_permissible_cvss_v3_score(self):
        """
        Gets the max_permissible_cvss_v3_score of this DetectConfiguration.
        The maximum Common Vulnerability Scoring System Version 3 (CVSS V3) score. An artifact with a CVSS V3 score below this value is not considered for patching.


        :return: The max_permissible_cvss_v3_score of this DetectConfiguration.
        :rtype: float
        """
        return self._max_permissible_cvss_v3_score

    @max_permissible_cvss_v3_score.setter
    def max_permissible_cvss_v3_score(self, max_permissible_cvss_v3_score):
        """
        Sets the max_permissible_cvss_v3_score of this DetectConfiguration.
        The maximum Common Vulnerability Scoring System Version 3 (CVSS V3) score. An artifact with a CVSS V3 score below this value is not considered for patching.


        :param max_permissible_cvss_v3_score: The max_permissible_cvss_v3_score of this DetectConfiguration.
        :type: float
        """
        self._max_permissible_cvss_v3_score = max_permissible_cvss_v3_score

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
