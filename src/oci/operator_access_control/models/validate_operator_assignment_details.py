# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateOperatorAssignmentDetails(object):
    """
    Details of the ValidateOperatorAssignment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateOperatorAssignmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_name:
            The value to assign to the action_name property of this ValidateOperatorAssignmentDetails.
        :type action_name: str

        """
        self.swagger_types = {
            'action_name': 'str'
        }

        self.attribute_map = {
            'action_name': 'actionName'
        }

        self._action_name = None

    @property
    def action_name(self):
        """
        Gets the action_name of this ValidateOperatorAssignmentDetails.
        Specifies the name of the operator action name for creating accessRequest.


        :return: The action_name of this ValidateOperatorAssignmentDetails.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """
        Sets the action_name of this ValidateOperatorAssignmentDetails.
        Specifies the name of the operator action name for creating accessRequest.


        :param action_name: The action_name of this ValidateOperatorAssignmentDetails.
        :type: str
        """
        self._action_name = action_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
