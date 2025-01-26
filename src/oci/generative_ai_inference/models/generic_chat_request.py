# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .base_chat_request import BaseChatRequest
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericChatRequest(BaseChatRequest):
    """
    Details for the chat request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericChatRequest object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.GenericChatRequest.api_format` attribute
        of this class is ``GENERIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param api_format:
            The value to assign to the api_format property of this GenericChatRequest.
            Allowed values for this property are: "COHERE", "GENERIC"
        :type api_format: str

        :param messages:
            The value to assign to the messages property of this GenericChatRequest.
        :type messages: list[oci.generative_ai_inference.models.Message]

        :param is_stream:
            The value to assign to the is_stream property of this GenericChatRequest.
        :type is_stream: bool

        :param num_generations:
            The value to assign to the num_generations property of this GenericChatRequest.
        :type num_generations: int

        :param is_echo:
            The value to assign to the is_echo property of this GenericChatRequest.
        :type is_echo: bool

        :param top_k:
            The value to assign to the top_k property of this GenericChatRequest.
        :type top_k: int

        :param top_p:
            The value to assign to the top_p property of this GenericChatRequest.
        :type top_p: float

        :param temperature:
            The value to assign to the temperature property of this GenericChatRequest.
        :type temperature: float

        :param frequency_penalty:
            The value to assign to the frequency_penalty property of this GenericChatRequest.
        :type frequency_penalty: float

        :param presence_penalty:
            The value to assign to the presence_penalty property of this GenericChatRequest.
        :type presence_penalty: float

        :param stop:
            The value to assign to the stop property of this GenericChatRequest.
        :type stop: list[str]

        :param log_probs:
            The value to assign to the log_probs property of this GenericChatRequest.
        :type log_probs: int

        :param max_tokens:
            The value to assign to the max_tokens property of this GenericChatRequest.
        :type max_tokens: int

        :param logit_bias:
            The value to assign to the logit_bias property of this GenericChatRequest.
        :type logit_bias: object

        """
        self.swagger_types = {
            'api_format': 'str',
            'messages': 'list[Message]',
            'is_stream': 'bool',
            'num_generations': 'int',
            'is_echo': 'bool',
            'top_k': 'int',
            'top_p': 'float',
            'temperature': 'float',
            'frequency_penalty': 'float',
            'presence_penalty': 'float',
            'stop': 'list[str]',
            'log_probs': 'int',
            'max_tokens': 'int',
            'logit_bias': 'object'
        }

        self.attribute_map = {
            'api_format': 'apiFormat',
            'messages': 'messages',
            'is_stream': 'isStream',
            'num_generations': 'numGenerations',
            'is_echo': 'isEcho',
            'top_k': 'topK',
            'top_p': 'topP',
            'temperature': 'temperature',
            'frequency_penalty': 'frequencyPenalty',
            'presence_penalty': 'presencePenalty',
            'stop': 'stop',
            'log_probs': 'logProbs',
            'max_tokens': 'maxTokens',
            'logit_bias': 'logitBias'
        }

        self._api_format = None
        self._messages = None
        self._is_stream = None
        self._num_generations = None
        self._is_echo = None
        self._top_k = None
        self._top_p = None
        self._temperature = None
        self._frequency_penalty = None
        self._presence_penalty = None
        self._stop = None
        self._log_probs = None
        self._max_tokens = None
        self._logit_bias = None
        self._api_format = 'GENERIC'

    @property
    def messages(self):
        """
        Gets the messages of this GenericChatRequest.
        The series of messages in a chat request. Includes the previous messages in a conversation. Each message includes a role (`USER` or the `CHATBOT`) and content.


        :return: The messages of this GenericChatRequest.
        :rtype: list[oci.generative_ai_inference.models.Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this GenericChatRequest.
        The series of messages in a chat request. Includes the previous messages in a conversation. Each message includes a role (`USER` or the `CHATBOT`) and content.


        :param messages: The messages of this GenericChatRequest.
        :type: list[oci.generative_ai_inference.models.Message]
        """
        self._messages = messages

    @property
    def is_stream(self):
        """
        Gets the is_stream of this GenericChatRequest.
        Whether to stream back partial progress. If set to true, as tokens become available, they are sent as data-only server-sent events.


        :return: The is_stream of this GenericChatRequest.
        :rtype: bool
        """
        return self._is_stream

    @is_stream.setter
    def is_stream(self, is_stream):
        """
        Sets the is_stream of this GenericChatRequest.
        Whether to stream back partial progress. If set to true, as tokens become available, they are sent as data-only server-sent events.


        :param is_stream: The is_stream of this GenericChatRequest.
        :type: bool
        """
        self._is_stream = is_stream

    @property
    def num_generations(self):
        """
        Gets the num_generations of this GenericChatRequest.
        The number of of generated texts that will be returned.


        :return: The num_generations of this GenericChatRequest.
        :rtype: int
        """
        return self._num_generations

    @num_generations.setter
    def num_generations(self, num_generations):
        """
        Sets the num_generations of this GenericChatRequest.
        The number of of generated texts that will be returned.


        :param num_generations: The num_generations of this GenericChatRequest.
        :type: int
        """
        self._num_generations = num_generations

    @property
    def is_echo(self):
        """
        Gets the is_echo of this GenericChatRequest.
        Whether to include the user prompt in the response. Applies only to non-stream results.


        :return: The is_echo of this GenericChatRequest.
        :rtype: bool
        """
        return self._is_echo

    @is_echo.setter
    def is_echo(self, is_echo):
        """
        Sets the is_echo of this GenericChatRequest.
        Whether to include the user prompt in the response. Applies only to non-stream results.


        :param is_echo: The is_echo of this GenericChatRequest.
        :type: bool
        """
        self._is_echo = is_echo

    @property
    def top_k(self):
        """
        Gets the top_k of this GenericChatRequest.
        An integer that sets up the model to use only the top k most likely tokens in the generated output. A higher k introduces more randomness into the output making the output text sound more natural. Default value is -1 which means to consider all tokens. Setting to 0 disables this method and considers all tokens.

        If also using top p, then the model considers only the top tokens whose probabilities add up to p percent and ignores the rest of the k tokens. For example, if k is 20, but the probabilities of the top 10 add up to .75, then only the top 10 tokens are chosen.


        :return: The top_k of this GenericChatRequest.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        """
        Sets the top_k of this GenericChatRequest.
        An integer that sets up the model to use only the top k most likely tokens in the generated output. A higher k introduces more randomness into the output making the output text sound more natural. Default value is -1 which means to consider all tokens. Setting to 0 disables this method and considers all tokens.

        If also using top p, then the model considers only the top tokens whose probabilities add up to p percent and ignores the rest of the k tokens. For example, if k is 20, but the probabilities of the top 10 add up to .75, then only the top 10 tokens are chosen.


        :param top_k: The top_k of this GenericChatRequest.
        :type: int
        """
        self._top_k = top_k

    @property
    def top_p(self):
        """
        Gets the top_p of this GenericChatRequest.
        If set to a probability 0.0 < p < 1.0, it ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step.

        To eliminate tokens with low likelihood, assign p a minimum percentage for the next token's likelihood. For example, when p is set to 0.75, the model eliminates the bottom 25 percent for the next token. Set to 1 to consider all tokens and set to 0 to disable. If both k and p are enabled, p acts after k.


        :return: The top_p of this GenericChatRequest.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        """
        Sets the top_p of this GenericChatRequest.
        If set to a probability 0.0 < p < 1.0, it ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step.

        To eliminate tokens with low likelihood, assign p a minimum percentage for the next token's likelihood. For example, when p is set to 0.75, the model eliminates the bottom 25 percent for the next token. Set to 1 to consider all tokens and set to 0 to disable. If both k and p are enabled, p acts after k.


        :param top_p: The top_p of this GenericChatRequest.
        :type: float
        """
        self._top_p = top_p

    @property
    def temperature(self):
        """
        Gets the temperature of this GenericChatRequest.
        A number that sets the randomness of the generated output. A lower temperature means a less random generations.

        Use lower numbers for tasks with a correct answer such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0 and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.


        :return: The temperature of this GenericChatRequest.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """
        Sets the temperature of this GenericChatRequest.
        A number that sets the randomness of the generated output. A lower temperature means a less random generations.

        Use lower numbers for tasks with a correct answer such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0 and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.


        :param temperature: The temperature of this GenericChatRequest.
        :type: float
        """
        self._temperature = temperature

    @property
    def frequency_penalty(self):
        """
        Gets the frequency_penalty of this GenericChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on their frequency in the generated text so far. Values > 0 encourage the model to use new tokens and values < 0 encourage the model to repeat tokens. Set to 0 to disable.


        :return: The frequency_penalty of this GenericChatRequest.
        :rtype: float
        """
        return self._frequency_penalty

    @frequency_penalty.setter
    def frequency_penalty(self, frequency_penalty):
        """
        Sets the frequency_penalty of this GenericChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on their frequency in the generated text so far. Values > 0 encourage the model to use new tokens and values < 0 encourage the model to repeat tokens. Set to 0 to disable.


        :param frequency_penalty: The frequency_penalty of this GenericChatRequest.
        :type: float
        """
        self._frequency_penalty = frequency_penalty

    @property
    def presence_penalty(self):
        """
        Gets the presence_penalty of this GenericChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on whether they've appeared in the generated text so far. Values > 0 encourage the model to use new tokens and values < 0 encourage the model to repeat tokens.

        Similar to frequency penalty, a penalty is applied to previously present tokens, except that this penalty is applied equally to all tokens that have already appeared, regardless of how many times they've appeared. Set to 0 to disable.


        :return: The presence_penalty of this GenericChatRequest.
        :rtype: float
        """
        return self._presence_penalty

    @presence_penalty.setter
    def presence_penalty(self, presence_penalty):
        """
        Sets the presence_penalty of this GenericChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on whether they've appeared in the generated text so far. Values > 0 encourage the model to use new tokens and values < 0 encourage the model to repeat tokens.

        Similar to frequency penalty, a penalty is applied to previously present tokens, except that this penalty is applied equally to all tokens that have already appeared, regardless of how many times they've appeared. Set to 0 to disable.


        :param presence_penalty: The presence_penalty of this GenericChatRequest.
        :type: float
        """
        self._presence_penalty = presence_penalty

    @property
    def stop(self):
        """
        Gets the stop of this GenericChatRequest.
        List of strings that stop the generation if they are generated for the response text. The returned output will not contain the stop strings.


        :return: The stop of this GenericChatRequest.
        :rtype: list[str]
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """
        Sets the stop of this GenericChatRequest.
        List of strings that stop the generation if they are generated for the response text. The returned output will not contain the stop strings.


        :param stop: The stop of this GenericChatRequest.
        :type: list[str]
        """
        self._stop = stop

    @property
    def log_probs(self):
        """
        Gets the log_probs of this GenericChatRequest.
        Includes the logarithmic probabilities for the most likely output tokens and the chosen tokens.

        For example, if the log probability is 5, the API returns a list of the 5 most likely tokens. The API returns the log probability of the sampled token, so there might be up to logprobs+1 elements in the response.


        :return: The log_probs of this GenericChatRequest.
        :rtype: int
        """
        return self._log_probs

    @log_probs.setter
    def log_probs(self, log_probs):
        """
        Sets the log_probs of this GenericChatRequest.
        Includes the logarithmic probabilities for the most likely output tokens and the chosen tokens.

        For example, if the log probability is 5, the API returns a list of the 5 most likely tokens. The API returns the log probability of the sampled token, so there might be up to logprobs+1 elements in the response.


        :param log_probs: The log_probs of this GenericChatRequest.
        :type: int
        """
        self._log_probs = log_probs

    @property
    def max_tokens(self):
        """
        Gets the max_tokens of this GenericChatRequest.
        The maximum number of tokens that can be generated per output sequence. The token count of your prompt plus `maxTokens` must not exceed the model's context length.
        Not setting a value for maxTokens results in the possible use of model's full context length.


        :return: The max_tokens of this GenericChatRequest.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        """
        Sets the max_tokens of this GenericChatRequest.
        The maximum number of tokens that can be generated per output sequence. The token count of your prompt plus `maxTokens` must not exceed the model's context length.
        Not setting a value for maxTokens results in the possible use of model's full context length.


        :param max_tokens: The max_tokens of this GenericChatRequest.
        :type: int
        """
        self._max_tokens = max_tokens

    @property
    def logit_bias(self):
        """
        Gets the logit_bias of this GenericChatRequest.
        Modifies the likelihood of specified tokens that appear in the completion.

        Example: '{\"6395\": 2, \"8134\": 1, \"21943\": 0.5, \"5923\": -100}'


        :return: The logit_bias of this GenericChatRequest.
        :rtype: object
        """
        return self._logit_bias

    @logit_bias.setter
    def logit_bias(self, logit_bias):
        """
        Sets the logit_bias of this GenericChatRequest.
        Modifies the likelihood of specified tokens that appear in the completion.

        Example: '{\"6395\": 2, \"8134\": 1, \"21943\": 0.5, \"5923\": -100}'


        :param logit_bias: The logit_bias of this GenericChatRequest.
        :type: object
        """
        self._logit_bias = logit_bias

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
