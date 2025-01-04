# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Trace(object):
    """
    The trace that displays the internal progression, such as reasoning and actions during an execution.
    """

    #: A constant which can be used with the trace_type property of a Trace.
    #: This constant has a value of "ERROR_TRACE"
    TRACE_TYPE_ERROR_TRACE = "ERROR_TRACE"

    #: A constant which can be used with the trace_type property of a Trace.
    #: This constant has a value of "RETRIEVAL_TRACE"
    TRACE_TYPE_RETRIEVAL_TRACE = "RETRIEVAL_TRACE"

    #: A constant which can be used with the trace_type property of a Trace.
    #: This constant has a value of "GENERATION_TRACE"
    TRACE_TYPE_GENERATION_TRACE = "GENERATION_TRACE"

    def __init__(self, **kwargs):
        """
        Initializes a new Trace object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_agent_runtime.models.ErrorTrace`
        * :class:`~oci.generative_ai_agent_runtime.models.RetrievalTrace`
        * :class:`~oci.generative_ai_agent_runtime.models.GenerationTrace`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_created:
            The value to assign to the time_created property of this Trace.
        :type time_created: datetime

        :param trace_type:
            The value to assign to the trace_type property of this Trace.
            Allowed values for this property are: "ERROR_TRACE", "RETRIEVAL_TRACE", "GENERATION_TRACE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type trace_type: str

        """
        self.swagger_types = {
            'time_created': 'datetime',
            'trace_type': 'str'
        }

        self.attribute_map = {
            'time_created': 'timeCreated',
            'trace_type': 'traceType'
        }

        self._time_created = None
        self._trace_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['traceType']

        if type == 'ERROR_TRACE':
            return 'ErrorTrace'

        if type == 'RETRIEVAL_TRACE':
            return 'RetrievalTrace'

        if type == 'GENERATION_TRACE':
            return 'GenerationTrace'
        else:
            return 'Trace'

    @property
    def time_created(self):
        """
        Gets the time_created of this Trace.
        The date and time that the trace was created in the format of an RFC3339 datetime string.


        :return: The time_created of this Trace.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Trace.
        The date and time that the trace was created in the format of an RFC3339 datetime string.


        :param time_created: The time_created of this Trace.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def trace_type(self):
        """
        **[Required]** Gets the trace_type of this Trace.
        The type of the trace.

        Allowed values for this property are: "ERROR_TRACE", "RETRIEVAL_TRACE", "GENERATION_TRACE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The trace_type of this Trace.
        :rtype: str
        """
        return self._trace_type

    @trace_type.setter
    def trace_type(self, trace_type):
        """
        Sets the trace_type of this Trace.
        The type of the trace.


        :param trace_type: The trace_type of this Trace.
        :type: str
        """
        allowed_values = ["ERROR_TRACE", "RETRIEVAL_TRACE", "GENERATION_TRACE"]
        if not value_allowed_none_or_none_sentinel(trace_type, allowed_values):
            trace_type = 'UNKNOWN_ENUM_VALUE'
        self._trace_type = trace_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
