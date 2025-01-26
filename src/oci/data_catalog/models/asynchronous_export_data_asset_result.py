# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AsynchronousExportDataAssetResult(object):
    """
    Details about the job which performs an export.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AsynchronousExportDataAssetResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_definition_name:
            The value to assign to the job_definition_name property of this AsynchronousExportDataAssetResult.
        :type job_definition_name: str

        :param job_definition_key:
            The value to assign to the job_definition_key property of this AsynchronousExportDataAssetResult.
        :type job_definition_key: str

        :param job_key:
            The value to assign to the job_key property of this AsynchronousExportDataAssetResult.
        :type job_key: str

        :param job_execution_key:
            The value to assign to the job_execution_key property of this AsynchronousExportDataAssetResult.
        :type job_execution_key: str

        :param source_key:
            The value to assign to the source_key property of this AsynchronousExportDataAssetResult.
        :type source_key: str

        """
        self.swagger_types = {
            'job_definition_name': 'str',
            'job_definition_key': 'str',
            'job_key': 'str',
            'job_execution_key': 'str',
            'source_key': 'str'
        }

        self.attribute_map = {
            'job_definition_name': 'jobDefinitionName',
            'job_definition_key': 'jobDefinitionKey',
            'job_key': 'jobKey',
            'job_execution_key': 'jobExecutionKey',
            'source_key': 'sourceKey'
        }

        self._job_definition_name = None
        self._job_definition_key = None
        self._job_key = None
        self._job_execution_key = None
        self._source_key = None

    @property
    def job_definition_name(self):
        """
        Gets the job_definition_name of this AsynchronousExportDataAssetResult.
        Display name of the export job.


        :return: The job_definition_name of this AsynchronousExportDataAssetResult.
        :rtype: str
        """
        return self._job_definition_name

    @job_definition_name.setter
    def job_definition_name(self, job_definition_name):
        """
        Sets the job_definition_name of this AsynchronousExportDataAssetResult.
        Display name of the export job.


        :param job_definition_name: The job_definition_name of this AsynchronousExportDataAssetResult.
        :type: str
        """
        self._job_definition_name = job_definition_name

    @property
    def job_definition_key(self):
        """
        Gets the job_definition_key of this AsynchronousExportDataAssetResult.
        Unique key of the export job definition.


        :return: The job_definition_key of this AsynchronousExportDataAssetResult.
        :rtype: str
        """
        return self._job_definition_key

    @job_definition_key.setter
    def job_definition_key(self, job_definition_key):
        """
        Sets the job_definition_key of this AsynchronousExportDataAssetResult.
        Unique key of the export job definition.


        :param job_definition_key: The job_definition_key of this AsynchronousExportDataAssetResult.
        :type: str
        """
        self._job_definition_key = job_definition_key

    @property
    def job_key(self):
        """
        Gets the job_key of this AsynchronousExportDataAssetResult.
        Unique key of the export job.


        :return: The job_key of this AsynchronousExportDataAssetResult.
        :rtype: str
        """
        return self._job_key

    @job_key.setter
    def job_key(self, job_key):
        """
        Sets the job_key of this AsynchronousExportDataAssetResult.
        Unique key of the export job.


        :param job_key: The job_key of this AsynchronousExportDataAssetResult.
        :type: str
        """
        self._job_key = job_key

    @property
    def job_execution_key(self):
        """
        Gets the job_execution_key of this AsynchronousExportDataAssetResult.
        Unique key of the job execution.


        :return: The job_execution_key of this AsynchronousExportDataAssetResult.
        :rtype: str
        """
        return self._job_execution_key

    @job_execution_key.setter
    def job_execution_key(self, job_execution_key):
        """
        Sets the job_execution_key of this AsynchronousExportDataAssetResult.
        Unique key of the job execution.


        :param job_execution_key: The job_execution_key of this AsynchronousExportDataAssetResult.
        :type: str
        """
        self._job_execution_key = job_execution_key

    @property
    def source_key(self):
        """
        Gets the source_key of this AsynchronousExportDataAssetResult.
        Unique key of the object being exported.


        :return: The source_key of this AsynchronousExportDataAssetResult.
        :rtype: str
        """
        return self._source_key

    @source_key.setter
    def source_key(self, source_key):
        """
        Sets the source_key of this AsynchronousExportDataAssetResult.
        Unique key of the object being exported.


        :param source_key: The source_key of this AsynchronousExportDataAssetResult.
        :type: str
        """
        self._source_key = source_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
