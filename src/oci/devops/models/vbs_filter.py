# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .filter import Filter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VbsFilter(Filter):
    """
    The filter for VBS events.
    """

    #: A constant which can be used with the events property of a VbsFilter.
    #: This constant has a value of "PUSH"
    EVENTS_PUSH = "PUSH"

    #: A constant which can be used with the events property of a VbsFilter.
    #: This constant has a value of "MERGE_REQUEST_CREATED"
    EVENTS_MERGE_REQUEST_CREATED = "MERGE_REQUEST_CREATED"

    #: A constant which can be used with the events property of a VbsFilter.
    #: This constant has a value of "MERGE_REQUEST_UPDATED"
    EVENTS_MERGE_REQUEST_UPDATED = "MERGE_REQUEST_UPDATED"

    #: A constant which can be used with the events property of a VbsFilter.
    #: This constant has a value of "MERGE_REQUEST_MERGED"
    EVENTS_MERGE_REQUEST_MERGED = "MERGE_REQUEST_MERGED"

    def __init__(self, **kwargs):
        """
        Initializes a new VbsFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.VbsFilter.trigger_source` attribute
        of this class is ``VBS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trigger_source:
            The value to assign to the trigger_source property of this VbsFilter.
        :type trigger_source: str

        :param events:
            The value to assign to the events property of this VbsFilter.
            Allowed values for items in this list are: "PUSH", "MERGE_REQUEST_CREATED", "MERGE_REQUEST_UPDATED", "MERGE_REQUEST_MERGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type events: list[str]

        :param include:
            The value to assign to the include property of this VbsFilter.
        :type include: oci.devops.models.VbsFilterAttributes

        :param exclude:
            The value to assign to the exclude property of this VbsFilter.
        :type exclude: oci.devops.models.VbsFilterExclusionAttributes

        """
        self.swagger_types = {
            'trigger_source': 'str',
            'events': 'list[str]',
            'include': 'VbsFilterAttributes',
            'exclude': 'VbsFilterExclusionAttributes'
        }

        self.attribute_map = {
            'trigger_source': 'triggerSource',
            'events': 'events',
            'include': 'include',
            'exclude': 'exclude'
        }

        self._trigger_source = None
        self._events = None
        self._include = None
        self._exclude = None
        self._trigger_source = 'VBS'

    @property
    def events(self):
        """
        Gets the events of this VbsFilter.
        The events, for example, PUSH, PULL_REQUEST_MERGE.

        Allowed values for items in this list are: "PUSH", "MERGE_REQUEST_CREATED", "MERGE_REQUEST_UPDATED", "MERGE_REQUEST_MERGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The events of this VbsFilter.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this VbsFilter.
        The events, for example, PUSH, PULL_REQUEST_MERGE.


        :param events: The events of this VbsFilter.
        :type: list[str]
        """
        allowed_values = ["PUSH", "MERGE_REQUEST_CREATED", "MERGE_REQUEST_UPDATED", "MERGE_REQUEST_MERGED"]
        if events:
            events[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in events]
        self._events = events

    @property
    def include(self):
        """
        Gets the include of this VbsFilter.

        :return: The include of this VbsFilter.
        :rtype: oci.devops.models.VbsFilterAttributes
        """
        return self._include

    @include.setter
    def include(self, include):
        """
        Sets the include of this VbsFilter.

        :param include: The include of this VbsFilter.
        :type: oci.devops.models.VbsFilterAttributes
        """
        self._include = include

    @property
    def exclude(self):
        """
        Gets the exclude of this VbsFilter.

        :return: The exclude of this VbsFilter.
        :rtype: oci.devops.models.VbsFilterExclusionAttributes
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """
        Sets the exclude of this VbsFilter.

        :param exclude: The exclude of this VbsFilter.
        :type: oci.devops.models.VbsFilterExclusionAttributes
        """
        self._exclude = exclude

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
