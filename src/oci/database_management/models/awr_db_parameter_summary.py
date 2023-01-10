# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbParameterSummary(object):
    """
    The summary of the AWR change history data for a single database parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbParameterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDbParameterSummary.
        :type name: str

        :param instance_number:
            The value to assign to the instance_number property of this AwrDbParameterSummary.
        :type instance_number: int

        :param begin_value:
            The value to assign to the begin_value property of this AwrDbParameterSummary.
        :type begin_value: str

        :param end_value:
            The value to assign to the end_value property of this AwrDbParameterSummary.
        :type end_value: str

        :param is_changed:
            The value to assign to the is_changed property of this AwrDbParameterSummary.
        :type is_changed: bool

        :param value_modified:
            The value to assign to the value_modified property of this AwrDbParameterSummary.
        :type value_modified: str

        :param is_default:
            The value to assign to the is_default property of this AwrDbParameterSummary.
        :type is_default: bool

        """
        self.swagger_types = {
            'name': 'str',
            'instance_number': 'int',
            'begin_value': 'str',
            'end_value': 'str',
            'is_changed': 'bool',
            'value_modified': 'str',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'instance_number': 'instanceNumber',
            'begin_value': 'beginValue',
            'end_value': 'endValue',
            'is_changed': 'isChanged',
            'value_modified': 'valueModified',
            'is_default': 'isDefault'
        }

        self._name = None
        self._instance_number = None
        self._begin_value = None
        self._end_value = None
        self._is_changed = None
        self._value_modified = None
        self._is_default = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrDbParameterSummary.
        The name of the parameter.


        :return: The name of this AwrDbParameterSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrDbParameterSummary.
        The name of the parameter.


        :param name: The name of this AwrDbParameterSummary.
        :type: str
        """
        self._name = name

    @property
    def instance_number(self):
        """
        Gets the instance_number of this AwrDbParameterSummary.
        The database instance number.


        :return: The instance_number of this AwrDbParameterSummary.
        :rtype: int
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """
        Sets the instance_number of this AwrDbParameterSummary.
        The database instance number.


        :param instance_number: The instance_number of this AwrDbParameterSummary.
        :type: int
        """
        self._instance_number = instance_number

    @property
    def begin_value(self):
        """
        Gets the begin_value of this AwrDbParameterSummary.
        The parameter value when the period began.


        :return: The begin_value of this AwrDbParameterSummary.
        :rtype: str
        """
        return self._begin_value

    @begin_value.setter
    def begin_value(self, begin_value):
        """
        Sets the begin_value of this AwrDbParameterSummary.
        The parameter value when the period began.


        :param begin_value: The begin_value of this AwrDbParameterSummary.
        :type: str
        """
        self._begin_value = begin_value

    @property
    def end_value(self):
        """
        Gets the end_value of this AwrDbParameterSummary.
        The parameter value when the period ended.


        :return: The end_value of this AwrDbParameterSummary.
        :rtype: str
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value):
        """
        Sets the end_value of this AwrDbParameterSummary.
        The parameter value when the period ended.


        :param end_value: The end_value of this AwrDbParameterSummary.
        :type: str
        """
        self._end_value = end_value

    @property
    def is_changed(self):
        """
        Gets the is_changed of this AwrDbParameterSummary.
        Indicates whether the parameter value changed within the period.


        :return: The is_changed of this AwrDbParameterSummary.
        :rtype: bool
        """
        return self._is_changed

    @is_changed.setter
    def is_changed(self, is_changed):
        """
        Sets the is_changed of this AwrDbParameterSummary.
        Indicates whether the parameter value changed within the period.


        :param is_changed: The is_changed of this AwrDbParameterSummary.
        :type: bool
        """
        self._is_changed = is_changed

    @property
    def value_modified(self):
        """
        Gets the value_modified of this AwrDbParameterSummary.
        Indicates whether the parameter has been modified after instance startup:
         - MODIFIED - Parameter has been modified with ALTER SESSION
         - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions\u2019 values to be modified)
         - FALSE - Parameter has not been modified after instance startup


        :return: The value_modified of this AwrDbParameterSummary.
        :rtype: str
        """
        return self._value_modified

    @value_modified.setter
    def value_modified(self, value_modified):
        """
        Sets the value_modified of this AwrDbParameterSummary.
        Indicates whether the parameter has been modified after instance startup:
         - MODIFIED - Parameter has been modified with ALTER SESSION
         - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions\u2019 values to be modified)
         - FALSE - Parameter has not been modified after instance startup


        :param value_modified: The value_modified of this AwrDbParameterSummary.
        :type: str
        """
        self._value_modified = value_modified

    @property
    def is_default(self):
        """
        Gets the is_default of this AwrDbParameterSummary.
        Indicates whether the parameter value in the end snapshot is the default.


        :return: The is_default of this AwrDbParameterSummary.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this AwrDbParameterSummary.
        Indicates whether the parameter value in the end snapshot is the default.


        :param is_default: The is_default of this AwrDbParameterSummary.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
