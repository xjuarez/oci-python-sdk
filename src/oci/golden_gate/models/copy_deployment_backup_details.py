# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CopyDeploymentBackupDetails(object):
    """
    The information about the copy for a Deployment Backup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CopyDeploymentBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace_name:
            The value to assign to the namespace_name property of this CopyDeploymentBackupDetails.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this CopyDeploymentBackupDetails.
        :type bucket_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CopyDeploymentBackupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CopyDeploymentBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'namespace_name': 'str',
            'bucket_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._namespace_name = None
        self._bucket_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this CopyDeploymentBackupDetails.
        Name of namespace that serves as a container for all of your buckets


        :return: The namespace_name of this CopyDeploymentBackupDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CopyDeploymentBackupDetails.
        Name of namespace that serves as a container for all of your buckets


        :param namespace_name: The namespace_name of this CopyDeploymentBackupDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CopyDeploymentBackupDetails.
        Name of the bucket where the object is to be uploaded in the object storage


        :return: The bucket_name of this CopyDeploymentBackupDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CopyDeploymentBackupDetails.
        Name of the bucket where the object is to be uploaded in the object storage


        :param bucket_name: The bucket_name of this CopyDeploymentBackupDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CopyDeploymentBackupDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CopyDeploymentBackupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CopyDeploymentBackupDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CopyDeploymentBackupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CopyDeploymentBackupDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CopyDeploymentBackupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CopyDeploymentBackupDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CopyDeploymentBackupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
