# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DownloadMaskingReportDetails(object):
    """
    Details to download a masking report.
    """

    #: A constant which can be used with the report_format property of a DownloadMaskingReportDetails.
    #: This constant has a value of "PDF"
    REPORT_FORMAT_PDF = "PDF"

    #: A constant which can be used with the report_format property of a DownloadMaskingReportDetails.
    #: This constant has a value of "XLS"
    REPORT_FORMAT_XLS = "XLS"

    def __init__(self, **kwargs):
        """
        Initializes a new DownloadMaskingReportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param report_id:
            The value to assign to the report_id property of this DownloadMaskingReportDetails.
        :type report_id: str

        :param report_format:
            The value to assign to the report_format property of this DownloadMaskingReportDetails.
            Allowed values for this property are: "PDF", "XLS"
        :type report_format: str

        """
        self.swagger_types = {
            'report_id': 'str',
            'report_format': 'str'
        }

        self.attribute_map = {
            'report_id': 'reportId',
            'report_format': 'reportFormat'
        }

        self._report_id = None
        self._report_format = None

    @property
    def report_id(self):
        """
        **[Required]** Gets the report_id of this DownloadMaskingReportDetails.
        The OCID of the masking report to be downloaded.


        :return: The report_id of this DownloadMaskingReportDetails.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """
        Sets the report_id of this DownloadMaskingReportDetails.
        The OCID of the masking report to be downloaded.


        :param report_id: The report_id of this DownloadMaskingReportDetails.
        :type: str
        """
        self._report_id = report_id

    @property
    def report_format(self):
        """
        **[Required]** Gets the report_format of this DownloadMaskingReportDetails.
        Format of the report.

        Allowed values for this property are: "PDF", "XLS"


        :return: The report_format of this DownloadMaskingReportDetails.
        :rtype: str
        """
        return self._report_format

    @report_format.setter
    def report_format(self, report_format):
        """
        Sets the report_format of this DownloadMaskingReportDetails.
        Format of the report.


        :param report_format: The report_format of this DownloadMaskingReportDetails.
        :type: str
        """
        allowed_values = ["PDF", "XLS"]
        if not value_allowed_none_or_none_sentinel(report_format, allowed_values):
            raise ValueError(
                f"Invalid value for `report_format`, must be None or one of {allowed_values}"
            )
        self._report_format = report_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
