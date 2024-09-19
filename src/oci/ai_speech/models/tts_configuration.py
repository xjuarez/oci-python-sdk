# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TtsConfiguration(object):
    """
    Speech configuration for TTS API.
    """

    #: A constant which can be used with the model_family property of a TtsConfiguration.
    #: This constant has a value of "ORACLE"
    MODEL_FAMILY_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new TtsConfiguration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_speech.models.TtsOracleConfiguration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_family:
            The value to assign to the model_family property of this TtsConfiguration.
            Allowed values for this property are: "ORACLE"
        :type model_family: str

        """
        self.swagger_types = {
            'model_family': 'str'
        }

        self.attribute_map = {
            'model_family': 'modelFamily'
        }

        self._model_family = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelFamily']

        if type == 'ORACLE':
            return 'TtsOracleConfiguration'
        else:
            return 'TtsConfiguration'

    @property
    def model_family(self):
        """
        **[Required]** Gets the model_family of this TtsConfiguration.
        The class of models to use for speech generation. The available model families are:
        - ORACLE

        Allowed values for this property are: "ORACLE"


        :return: The model_family of this TtsConfiguration.
        :rtype: str
        """
        return self._model_family

    @model_family.setter
    def model_family(self, model_family):
        """
        Sets the model_family of this TtsConfiguration.
        The class of models to use for speech generation. The available model families are:
        - ORACLE


        :param model_family: The model_family of this TtsConfiguration.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(model_family, allowed_values):
            raise ValueError(
                f"Invalid value for `model_family`, must be None or one of {allowed_values}"
            )
        self._model_family = model_family

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other