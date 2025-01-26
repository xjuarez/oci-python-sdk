# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateScheduleDetails(object):
    """
    Scheduling related details for the Exadata Fleet Update Action during create operations.
    The specified time should not conflict with existing Exadata Infrastructure maintenance windows.
    Null scheduleDetails for Stage and Apply Actions in Exadata Fleet Update Cycle creation would not create Actions.
    Null scheduleDetails for CreateAction would execute the Exadata Fleet Update Action as soon as possible.
    """

    #: A constant which can be used with the type property of a CreateScheduleDetails.
    #: This constant has a value of "START_TIME"
    TYPE_START_TIME = "START_TIME"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateScheduleDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.CreateStartTimeScheduleDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateScheduleDetails.
            Allowed values for this property are: "START_TIME"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'START_TIME':
            return 'CreateStartTimeScheduleDetails'
        else:
            return 'CreateScheduleDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateScheduleDetails.
        Type of scheduling strategy to use for Fleet Patching Update Action execution.

        Allowed values for this property are: "START_TIME"


        :return: The type of this CreateScheduleDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateScheduleDetails.
        Type of scheduling strategy to use for Fleet Patching Update Action execution.


        :param type: The type of this CreateScheduleDetails.
        :type: str
        """
        allowed_values = ["START_TIME"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
