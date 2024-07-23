# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Logprobs(object):
    """
    Includes the logarithmic probabilities for the most likely output tokens and the chosen tokens.

    For example, if the log probability is 5, the API returns a list of the 5 most likely tokens. The API returns the log probability of the sampled token, so there might be up to logprobs+1 elements in the response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Logprobs object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text_offset:
            The value to assign to the text_offset property of this Logprobs.
        :type text_offset: list[int]

        :param token_logprobs:
            The value to assign to the token_logprobs property of this Logprobs.
        :type token_logprobs: list[float]

        :param tokens:
            The value to assign to the tokens property of this Logprobs.
        :type tokens: list[str]

        :param top_logprobs:
            The value to assign to the top_logprobs property of this Logprobs.
        :type top_logprobs: list[dict(str, str)]

        """
        self.swagger_types = {
            'text_offset': 'list[int]',
            'token_logprobs': 'list[float]',
            'tokens': 'list[str]',
            'top_logprobs': 'list[dict(str, str)]'
        }

        self.attribute_map = {
            'text_offset': 'textOffset',
            'token_logprobs': 'tokenLogprobs',
            'tokens': 'tokens',
            'top_logprobs': 'topLogprobs'
        }

        self._text_offset = None
        self._token_logprobs = None
        self._tokens = None
        self._top_logprobs = None

    @property
    def text_offset(self):
        """
        Gets the text_offset of this Logprobs.
        The text offset.


        :return: The text_offset of this Logprobs.
        :rtype: list[int]
        """
        return self._text_offset

    @text_offset.setter
    def text_offset(self, text_offset):
        """
        Sets the text_offset of this Logprobs.
        The text offset.


        :param text_offset: The text_offset of this Logprobs.
        :type: list[int]
        """
        self._text_offset = text_offset

    @property
    def token_logprobs(self):
        """
        Gets the token_logprobs of this Logprobs.
        The logarithmic probabilites of the output token.


        :return: The token_logprobs of this Logprobs.
        :rtype: list[float]
        """
        return self._token_logprobs

    @token_logprobs.setter
    def token_logprobs(self, token_logprobs):
        """
        Sets the token_logprobs of this Logprobs.
        The logarithmic probabilites of the output token.


        :param token_logprobs: The token_logprobs of this Logprobs.
        :type: list[float]
        """
        self._token_logprobs = token_logprobs

    @property
    def tokens(self):
        """
        Gets the tokens of this Logprobs.
        The list of output tokens.


        :return: The tokens of this Logprobs.
        :rtype: list[str]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """
        Sets the tokens of this Logprobs.
        The list of output tokens.


        :param tokens: The tokens of this Logprobs.
        :type: list[str]
        """
        self._tokens = tokens

    @property
    def top_logprobs(self):
        """
        Gets the top_logprobs of this Logprobs.
        The logarithmic probabilities of each of the top k tokens.


        :return: The top_logprobs of this Logprobs.
        :rtype: list[dict(str, str)]
        """
        return self._top_logprobs

    @top_logprobs.setter
    def top_logprobs(self, top_logprobs):
        """
        Sets the top_logprobs of this Logprobs.
        The logarithmic probabilities of each of the top k tokens.


        :param top_logprobs: The top_logprobs of this Logprobs.
        :type: list[dict(str, str)]
        """
        self._top_logprobs = top_logprobs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
