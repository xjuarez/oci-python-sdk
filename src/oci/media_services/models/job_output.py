# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobOutput(object):
    """
    The output result of an executed MediaWorkflowJob.
    """

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "AUDIO"
    ASSET_TYPE_AUDIO = "AUDIO"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "VIDEO"
    ASSET_TYPE_VIDEO = "VIDEO"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "PLAYLIST"
    ASSET_TYPE_PLAYLIST = "PLAYLIST"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "IMAGE"
    ASSET_TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "CAPTION_FILE"
    ASSET_TYPE_CAPTION_FILE = "CAPTION_FILE"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "TRANSCRIPTION_JOB"
    ASSET_TYPE_TRANSCRIPTION_JOB = "TRANSCRIPTION_JOB"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "VISION_JOB"
    ASSET_TYPE_VISION_JOB = "VISION_JOB"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "TEXT_ANALYSIS"
    ASSET_TYPE_TEXT_ANALYSIS = "TEXT_ANALYSIS"

    #: A constant which can be used with the asset_type property of a JobOutput.
    #: This constant has a value of "OTHER"
    ASSET_TYPE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new JobOutput object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param asset_type:
            The value to assign to the asset_type property of this JobOutput.
            Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "TRANSCRIPTION_JOB", "VISION_JOB", "TEXT_ANALYSIS", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type asset_type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this JobOutput.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this JobOutput.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this JobOutput.
        :type object_name: str

        :param id:
            The value to assign to the id property of this JobOutput.
        :type id: str

        """
        self.swagger_types = {
            'asset_type': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'asset_type': 'assetType',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName',
            'id': 'id'
        }

        self._asset_type = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None
        self._id = None

    @property
    def asset_type(self):
        """
        Gets the asset_type of this JobOutput.
        Type of job output.

        Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "TRANSCRIPTION_JOB", "VISION_JOB", "TEXT_ANALYSIS", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The asset_type of this JobOutput.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """
        Sets the asset_type of this JobOutput.
        Type of job output.


        :param asset_type: The asset_type of this JobOutput.
        :type: str
        """
        allowed_values = ["AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "TRANSCRIPTION_JOB", "VISION_JOB", "TEXT_ANALYSIS", "OTHER"]
        if not value_allowed_none_or_none_sentinel(asset_type, allowed_values):
            asset_type = 'UNKNOWN_ENUM_VALUE'
        self._asset_type = asset_type

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this JobOutput.
        The namespace name of the job output.


        :return: The namespace_name of this JobOutput.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this JobOutput.
        The namespace name of the job output.


        :param namespace_name: The namespace_name of this JobOutput.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this JobOutput.
        The bucket name of the job output.


        :return: The bucket_name of this JobOutput.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this JobOutput.
        The bucket name of the job output.


        :param bucket_name: The bucket_name of this JobOutput.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        Gets the object_name of this JobOutput.
        The object name of the job output.


        :return: The object_name of this JobOutput.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this JobOutput.
        The object name of the job output.


        :param object_name: The object_name of this JobOutput.
        :type: str
        """
        self._object_name = object_name

    @property
    def id(self):
        """
        Gets the id of this JobOutput.
        The ID associated with the job output.


        :return: The id of this JobOutput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobOutput.
        The ID associated with the job output.


        :param id: The id of this JobOutput.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
