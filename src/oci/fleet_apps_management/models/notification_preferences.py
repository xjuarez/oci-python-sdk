# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotificationPreferences(object):
    """
    Notification information to get notified when the fleet status changes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NotificationPreferences object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param topic_id:
            The value to assign to the topic_id property of this NotificationPreferences.
        :type topic_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NotificationPreferences.
        :type compartment_id: str

        :param preferences:
            The value to assign to the preferences property of this NotificationPreferences.
        :type preferences: oci.fleet_apps_management.models.Preferences

        """
        self.swagger_types = {
            'topic_id': 'str',
            'compartment_id': 'str',
            'preferences': 'Preferences'
        }

        self.attribute_map = {
            'topic_id': 'topicId',
            'compartment_id': 'compartmentId',
            'preferences': 'preferences'
        }

        self._topic_id = None
        self._compartment_id = None
        self._preferences = None

    @property
    def topic_id(self):
        """
        **[Required]** Gets the topic_id of this NotificationPreferences.
        Topic Id where the notifications will be directed.
        A topic is a communication channel for sending messages on chosen events to subscriptions.


        :return: The topic_id of this NotificationPreferences.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """
        Sets the topic_id of this NotificationPreferences.
        Topic Id where the notifications will be directed.
        A topic is a communication channel for sending messages on chosen events to subscriptions.


        :param topic_id: The topic_id of this NotificationPreferences.
        :type: str
        """
        self._topic_id = topic_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this NotificationPreferences.
        Compartment ID the topic belongs to.


        :return: The compartment_id of this NotificationPreferences.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NotificationPreferences.
        Compartment ID the topic belongs to.


        :param compartment_id: The compartment_id of this NotificationPreferences.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def preferences(self):
        """
        Gets the preferences of this NotificationPreferences.

        :return: The preferences of this NotificationPreferences.
        :rtype: oci.fleet_apps_management.models.Preferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """
        Sets the preferences of this NotificationPreferences.

        :param preferences: The preferences of this NotificationPreferences.
        :type: oci.fleet_apps_management.models.Preferences
        """
        self._preferences = preferences

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
