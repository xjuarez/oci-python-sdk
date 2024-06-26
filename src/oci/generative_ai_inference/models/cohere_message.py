# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereMessage(object):
    """
    An message that represents a single dialogue of chat
    """

    #: A constant which can be used with the role property of a CohereMessage.
    #: This constant has a value of "CHATBOT"
    ROLE_CHATBOT = "CHATBOT"

    #: A constant which can be used with the role property of a CohereMessage.
    #: This constant has a value of "USER"
    ROLE_USER = "USER"

    def __init__(self, **kwargs):
        """
        Initializes a new CohereMessage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this CohereMessage.
            Allowed values for this property are: "CHATBOT", "USER"
        :type role: str

        :param message:
            The value to assign to the message property of this CohereMessage.
        :type message: str

        """
        self.swagger_types = {
            'role': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'role': 'role',
            'message': 'message'
        }

        self._role = None
        self._message = None

    @property
    def role(self):
        """
        **[Required]** Gets the role of this CohereMessage.
        One of CHATBOT|USER to identify who the message is coming from.

        Allowed values for this property are: "CHATBOT", "USER"


        :return: The role of this CohereMessage.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this CohereMessage.
        One of CHATBOT|USER to identify who the message is coming from.


        :param role: The role of this CohereMessage.
        :type: str
        """
        allowed_values = ["CHATBOT", "USER"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                f"Invalid value for `role`, must be None or one of {allowed_values}"
            )
        self._role = role

    @property
    def message(self):
        """
        **[Required]** Gets the message of this CohereMessage.
        Contents of the chat message.


        :return: The message of this CohereMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CohereMessage.
        Contents of the chat message.


        :param message: The message of this CohereMessage.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
