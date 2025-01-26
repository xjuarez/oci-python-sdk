# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoFace(object):
    """
    Detected face in a video.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VideoFace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param segments:
            The value to assign to the segments property of this VideoFace.
        :type segments: list[oci.ai_vision.models.VideoFaceSegment]

        """
        self.swagger_types = {
            'segments': 'list[VideoFaceSegment]'
        }

        self.attribute_map = {
            'segments': 'segments'
        }

        self._segments = None

    @property
    def segments(self):
        """
        **[Required]** Gets the segments of this VideoFace.
        Face segments in a video.


        :return: The segments of this VideoFace.
        :rtype: list[oci.ai_vision.models.VideoFaceSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """
        Sets the segments of this VideoFace.
        Face segments in a video.


        :param segments: The segments of this VideoFace.
        :type: list[oci.ai_vision.models.VideoFaceSegment]
        """
        self._segments = segments

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
