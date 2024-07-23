# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveLockDetails(object):
    """
    Request payload to remove lock to the resource.
    """

    #: A constant which can be used with the type property of a RemoveLockDetails.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a RemoveLockDetails.
    #: This constant has a value of "DELETE"
    TYPE_DELETE = "DELETE"

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveLockDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RemoveLockDetails.
            Allowed values for this property are: "FULL", "DELETE"
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RemoveLockDetails.
        :type compartment_id: str

        :param related_resource_id:
            The value to assign to the related_resource_id property of this RemoveLockDetails.
        :type related_resource_id: str

        :param message:
            The value to assign to the message property of this RemoveLockDetails.
        :type message: str

        :param time_created:
            The value to assign to the time_created property of this RemoveLockDetails.
        :type time_created: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'compartment_id': 'str',
            'related_resource_id': 'str',
            'message': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'compartment_id': 'compartmentId',
            'related_resource_id': 'relatedResourceId',
            'message': 'message',
            'time_created': 'timeCreated'
        }

        self._type = None
        self._compartment_id = None
        self._related_resource_id = None
        self._message = None
        self._time_created = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this RemoveLockDetails.
        Type of the lock.

        Allowed values for this property are: "FULL", "DELETE"


        :return: The type of this RemoveLockDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RemoveLockDetails.
        Type of the lock.


        :param type: The type of this RemoveLockDetails.
        :type: str
        """
        allowed_values = ["FULL", "DELETE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RemoveLockDetails.
        The compartment ID of the lock.


        :return: The compartment_id of this RemoveLockDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RemoveLockDetails.
        The compartment ID of the lock.


        :param compartment_id: The compartment_id of this RemoveLockDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def related_resource_id(self):
        """
        Gets the related_resource_id of this RemoveLockDetails.
        The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.


        :return: The related_resource_id of this RemoveLockDetails.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        """
        Sets the related_resource_id of this RemoveLockDetails.
        The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.


        :param related_resource_id: The related_resource_id of this RemoveLockDetails.
        :type: str
        """
        self._related_resource_id = related_resource_id

    @property
    def message(self):
        """
        Gets the message of this RemoveLockDetails.
        A message added by the creator of the lock. This is typically used to give an
        indication of why the resource is locked.


        :return: The message of this RemoveLockDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this RemoveLockDetails.
        A message added by the creator of the lock. This is typically used to give an
        indication of why the resource is locked.


        :param message: The message of this RemoveLockDetails.
        :type: str
        """
        self._message = message

    @property
    def time_created(self):
        """
        Gets the time_created of this RemoveLockDetails.
        When the lock was created.


        :return: The time_created of this RemoveLockDetails.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RemoveLockDetails.
        When the lock was created.


        :param time_created: The time_created of this RemoveLockDetails.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other