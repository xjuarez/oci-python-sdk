# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .update_schedule_details import UpdateScheduleDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStartTimeScheduleDetails(UpdateScheduleDetails):
    """
    Start time details for the Exadata Fleet Update Action.
    The specified time should not conflict with existing Exadata Infrastructure maintenance windows.
    If Stage and Apply Actions are created with a timeToStart specified during Exadata Fleet Update Cycle
    creation, Apply should be scheduled at least 24 hours after the start time of the Stage Action.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStartTimeScheduleDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.UpdateStartTimeScheduleDetails.type` attribute
        of this class is ``START_TIME`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateStartTimeScheduleDetails.
            Allowed values for this property are: "START_TIME", "NONE"
        :type type: str

        :param time_to_start:
            The value to assign to the time_to_start property of this UpdateStartTimeScheduleDetails.
        :type time_to_start: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'time_to_start': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'time_to_start': 'timeToStart'
        }

        self._type = None
        self._time_to_start = None
        self._type = 'START_TIME'

    @property
    def time_to_start(self):
        """
        **[Required]** Gets the time_to_start of this UpdateStartTimeScheduleDetails.
        The date and time the Exadata Fleet Update Action is expected to start.
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_to_start of this UpdateStartTimeScheduleDetails.
        :rtype: datetime
        """
        return self._time_to_start

    @time_to_start.setter
    def time_to_start(self, time_to_start):
        """
        Sets the time_to_start of this UpdateStartTimeScheduleDetails.
        The date and time the Exadata Fleet Update Action is expected to start.
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_to_start: The time_to_start of this UpdateStartTimeScheduleDetails.
        :type: datetime
        """
        self._time_to_start = time_to_start

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
