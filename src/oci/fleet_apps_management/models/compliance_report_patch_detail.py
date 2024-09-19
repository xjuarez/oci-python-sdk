# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComplianceReportPatchDetail(object):
    """
    Details of the Patch
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComplianceReportPatchDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param patch_name:
            The value to assign to the patch_name property of this ComplianceReportPatchDetail.
        :type patch_name: str

        :param patch_description:
            The value to assign to the patch_description property of this ComplianceReportPatchDetail.
        :type patch_description: str

        :param time_applied:
            The value to assign to the time_applied property of this ComplianceReportPatchDetail.
        :type time_applied: datetime

        :param time_released:
            The value to assign to the time_released property of this ComplianceReportPatchDetail.
        :type time_released: datetime

        :param patch_type:
            The value to assign to the patch_type property of this ComplianceReportPatchDetail.
        :type patch_type: str

        """
        self.swagger_types = {
            'patch_name': 'str',
            'patch_description': 'str',
            'time_applied': 'datetime',
            'time_released': 'datetime',
            'patch_type': 'str'
        }

        self.attribute_map = {
            'patch_name': 'patchName',
            'patch_description': 'patchDescription',
            'time_applied': 'timeApplied',
            'time_released': 'timeReleased',
            'patch_type': 'patchType'
        }

        self._patch_name = None
        self._patch_description = None
        self._time_applied = None
        self._time_released = None
        self._patch_type = None

    @property
    def patch_name(self):
        """
        **[Required]** Gets the patch_name of this ComplianceReportPatchDetail.
        The OCID to identify this analysis results.


        :return: The patch_name of this ComplianceReportPatchDetail.
        :rtype: str
        """
        return self._patch_name

    @patch_name.setter
    def patch_name(self, patch_name):
        """
        Sets the patch_name of this ComplianceReportPatchDetail.
        The OCID to identify this analysis results.


        :param patch_name: The patch_name of this ComplianceReportPatchDetail.
        :type: str
        """
        self._patch_name = patch_name

    @property
    def patch_description(self):
        """
        Gets the patch_description of this ComplianceReportPatchDetail.
        The OCID of the work request to start the analysis.


        :return: The patch_description of this ComplianceReportPatchDetail.
        :rtype: str
        """
        return self._patch_description

    @patch_description.setter
    def patch_description(self, patch_description):
        """
        Sets the patch_description of this ComplianceReportPatchDetail.
        The OCID of the work request to start the analysis.


        :param patch_description: The patch_description of this ComplianceReportPatchDetail.
        :type: str
        """
        self._patch_description = patch_description

    @property
    def time_applied(self):
        """
        Gets the time_applied of this ComplianceReportPatchDetail.
        Time the patch was applied


        :return: The time_applied of this ComplianceReportPatchDetail.
        :rtype: datetime
        """
        return self._time_applied

    @time_applied.setter
    def time_applied(self, time_applied):
        """
        Sets the time_applied of this ComplianceReportPatchDetail.
        Time the patch was applied


        :param time_applied: The time_applied of this ComplianceReportPatchDetail.
        :type: datetime
        """
        self._time_applied = time_applied

    @property
    def time_released(self):
        """
        Gets the time_released of this ComplianceReportPatchDetail.
        Date on which patch was released.


        :return: The time_released of this ComplianceReportPatchDetail.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this ComplianceReportPatchDetail.
        Date on which patch was released.


        :param time_released: The time_released of this ComplianceReportPatchDetail.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def patch_type(self):
        """
        **[Required]** Gets the patch_type of this ComplianceReportPatchDetail.
        Type of patch.


        :return: The patch_type of this ComplianceReportPatchDetail.
        :rtype: str
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """
        Sets the patch_type of this ComplianceReportPatchDetail.
        Type of patch.


        :param patch_type: The patch_type of this ComplianceReportPatchDetail.
        :type: str
        """
        self._patch_type = patch_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
