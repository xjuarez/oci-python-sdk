# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Dimensions(object):
    """
    The scope of analytics data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Dimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_id:
            The value to assign to the target_id property of this Dimensions.
        :type target_id: str

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this Dimensions.
        :type sensitive_data_model_id: str

        """
        self.swagger_types = {
            'target_id': 'str',
            'sensitive_data_model_id': 'str'
        }

        self.attribute_map = {
            'target_id': 'targetId',
            'sensitive_data_model_id': 'sensitiveDataModelId'
        }

        self._target_id = None
        self._sensitive_data_model_id = None

    @property
    def target_id(self):
        """
        Gets the target_id of this Dimensions.
        The OCID of the target database.


        :return: The target_id of this Dimensions.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this Dimensions.
        The OCID of the target database.


        :param target_id: The target_id of this Dimensions.
        :type: str
        """
        self._target_id = target_id

    @property
    def sensitive_data_model_id(self):
        """
        Gets the sensitive_data_model_id of this Dimensions.
        The OCID of the sensitive data model.


        :return: The sensitive_data_model_id of this Dimensions.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this Dimensions.
        The OCID of the sensitive data model.


        :param sensitive_data_model_id: The sensitive_data_model_id of this Dimensions.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
