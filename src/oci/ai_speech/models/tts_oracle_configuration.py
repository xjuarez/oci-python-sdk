# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101

from .tts_configuration import TtsConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TtsOracleConfiguration(TtsConfiguration):
    """
    Use this configuration for selecting a model from Oracle model family.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TtsOracleConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_speech.models.TtsOracleConfiguration.model_family` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_family:
            The value to assign to the model_family property of this TtsOracleConfiguration.
            Allowed values for this property are: "ORACLE"
        :type model_family: str

        :param model_details:
            The value to assign to the model_details property of this TtsOracleConfiguration.
        :type model_details: oci.ai_speech.models.TtsOracleModelDetails

        :param speech_settings:
            The value to assign to the speech_settings property of this TtsOracleConfiguration.
        :type speech_settings: oci.ai_speech.models.TtsOracleSpeechSettings

        """
        self.swagger_types = {
            'model_family': 'str',
            'model_details': 'TtsOracleModelDetails',
            'speech_settings': 'TtsOracleSpeechSettings'
        }

        self.attribute_map = {
            'model_family': 'modelFamily',
            'model_details': 'modelDetails',
            'speech_settings': 'speechSettings'
        }

        self._model_family = None
        self._model_details = None
        self._speech_settings = None
        self._model_family = 'ORACLE'

    @property
    def model_details(self):
        """
        Gets the model_details of this TtsOracleConfiguration.

        :return: The model_details of this TtsOracleConfiguration.
        :rtype: oci.ai_speech.models.TtsOracleModelDetails
        """
        return self._model_details

    @model_details.setter
    def model_details(self, model_details):
        """
        Sets the model_details of this TtsOracleConfiguration.

        :param model_details: The model_details of this TtsOracleConfiguration.
        :type: oci.ai_speech.models.TtsOracleModelDetails
        """
        self._model_details = model_details

    @property
    def speech_settings(self):
        """
        Gets the speech_settings of this TtsOracleConfiguration.

        :return: The speech_settings of this TtsOracleConfiguration.
        :rtype: oci.ai_speech.models.TtsOracleSpeechSettings
        """
        return self._speech_settings

    @speech_settings.setter
    def speech_settings(self, speech_settings):
        """
        Sets the speech_settings of this TtsOracleConfiguration.

        :param speech_settings: The speech_settings of this TtsOracleConfiguration.
        :type: oci.ai_speech.models.TtsOracleSpeechSettings
        """
        self._speech_settings = speech_settings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
