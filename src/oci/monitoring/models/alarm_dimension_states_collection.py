# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmDimensionStatesCollection(object):
    """
    The list of current alarm state entries for each metric stream that matches the filters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmDimensionStatesCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alarm_id:
            The value to assign to the alarm_id property of this AlarmDimensionStatesCollection.
        :type alarm_id: str

        :param is_enabled:
            The value to assign to the is_enabled property of this AlarmDimensionStatesCollection.
        :type is_enabled: bool

        :param is_notifications_per_metric_dimension_enabled:
            The value to assign to the is_notifications_per_metric_dimension_enabled property of this AlarmDimensionStatesCollection.
        :type is_notifications_per_metric_dimension_enabled: bool

        :param items:
            The value to assign to the items property of this AlarmDimensionStatesCollection.
        :type items: list[oci.monitoring.models.AlarmDimensionStatesEntry]

        """
        self.swagger_types = {
            'alarm_id': 'str',
            'is_enabled': 'bool',
            'is_notifications_per_metric_dimension_enabled': 'bool',
            'items': 'list[AlarmDimensionStatesEntry]'
        }

        self.attribute_map = {
            'alarm_id': 'alarmId',
            'is_enabled': 'isEnabled',
            'is_notifications_per_metric_dimension_enabled': 'isNotificationsPerMetricDimensionEnabled',
            'items': 'items'
        }

        self._alarm_id = None
        self._is_enabled = None
        self._is_notifications_per_metric_dimension_enabled = None
        self._items = None

    @property
    def alarm_id(self):
        """
        **[Required]** Gets the alarm_id of this AlarmDimensionStatesCollection.
        The `OCID`__ of the alarm to retrieve alarm state entries for.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The alarm_id of this AlarmDimensionStatesCollection.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """
        Sets the alarm_id of this AlarmDimensionStatesCollection.
        The `OCID`__ of the alarm to retrieve alarm state entries for.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param alarm_id: The alarm_id of this AlarmDimensionStatesCollection.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this AlarmDimensionStatesCollection.
        Whether the alarm is enabled.

        Example: `true`


        :return: The is_enabled of this AlarmDimensionStatesCollection.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AlarmDimensionStatesCollection.
        Whether the alarm is enabled.

        Example: `true`


        :param is_enabled: The is_enabled of this AlarmDimensionStatesCollection.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_notifications_per_metric_dimension_enabled(self):
        """
        **[Required]** Gets the is_notifications_per_metric_dimension_enabled of this AlarmDimensionStatesCollection.
        When set to `true`, splits notifications per metric stream. When set to `false`, groups notifications across metric streams.
        Example: `true`


        :return: The is_notifications_per_metric_dimension_enabled of this AlarmDimensionStatesCollection.
        :rtype: bool
        """
        return self._is_notifications_per_metric_dimension_enabled

    @is_notifications_per_metric_dimension_enabled.setter
    def is_notifications_per_metric_dimension_enabled(self, is_notifications_per_metric_dimension_enabled):
        """
        Sets the is_notifications_per_metric_dimension_enabled of this AlarmDimensionStatesCollection.
        When set to `true`, splits notifications per metric stream. When set to `false`, groups notifications across metric streams.
        Example: `true`


        :param is_notifications_per_metric_dimension_enabled: The is_notifications_per_metric_dimension_enabled of this AlarmDimensionStatesCollection.
        :type: bool
        """
        self._is_notifications_per_metric_dimension_enabled = is_notifications_per_metric_dimension_enabled

    @property
    def items(self):
        """
        **[Required]** Gets the items of this AlarmDimensionStatesCollection.
        Array of alarm state entries.


        :return: The items of this AlarmDimensionStatesCollection.
        :rtype: list[oci.monitoring.models.AlarmDimensionStatesEntry]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AlarmDimensionStatesCollection.
        Array of alarm state entries.


        :param items: The items of this AlarmDimensionStatesCollection.
        :type: list[oci.monitoring.models.AlarmDimensionStatesEntry]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
