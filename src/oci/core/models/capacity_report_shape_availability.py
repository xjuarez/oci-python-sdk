# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CapacityReportShapeAvailability(object):
    """
    Information about the available capacity for a shape.
    """

    #: A constant which can be used with the availability_status property of a CapacityReportShapeAvailability.
    #: This constant has a value of "OUT_OF_HOST_CAPACITY"
    AVAILABILITY_STATUS_OUT_OF_HOST_CAPACITY = "OUT_OF_HOST_CAPACITY"

    #: A constant which can be used with the availability_status property of a CapacityReportShapeAvailability.
    #: This constant has a value of "HARDWARE_NOT_SUPPORTED"
    AVAILABILITY_STATUS_HARDWARE_NOT_SUPPORTED = "HARDWARE_NOT_SUPPORTED"

    #: A constant which can be used with the availability_status property of a CapacityReportShapeAvailability.
    #: This constant has a value of "AVAILABLE"
    AVAILABILITY_STATUS_AVAILABLE = "AVAILABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new CapacityReportShapeAvailability object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fault_domain:
            The value to assign to the fault_domain property of this CapacityReportShapeAvailability.
        :type fault_domain: str

        :param instance_shape:
            The value to assign to the instance_shape property of this CapacityReportShapeAvailability.
        :type instance_shape: str

        :param instance_shape_config:
            The value to assign to the instance_shape_config property of this CapacityReportShapeAvailability.
        :type instance_shape_config: oci.core.models.CapacityReportInstanceShapeConfig

        :param available_count:
            The value to assign to the available_count property of this CapacityReportShapeAvailability.
        :type available_count: int

        :param availability_status:
            The value to assign to the availability_status property of this CapacityReportShapeAvailability.
            Allowed values for this property are: "OUT_OF_HOST_CAPACITY", "HARDWARE_NOT_SUPPORTED", "AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability_status: str

        """
        self.swagger_types = {
            'fault_domain': 'str',
            'instance_shape': 'str',
            'instance_shape_config': 'CapacityReportInstanceShapeConfig',
            'available_count': 'int',
            'availability_status': 'str'
        }

        self.attribute_map = {
            'fault_domain': 'faultDomain',
            'instance_shape': 'instanceShape',
            'instance_shape_config': 'instanceShapeConfig',
            'available_count': 'availableCount',
            'availability_status': 'availabilityStatus'
        }

        self._fault_domain = None
        self._instance_shape = None
        self._instance_shape_config = None
        self._available_count = None
        self._availability_status = None

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this CapacityReportShapeAvailability.
        The fault domain for the capacity report.

        If you do not specify the fault domain, the capacity report includes information about all fault domains.


        :return: The fault_domain of this CapacityReportShapeAvailability.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this CapacityReportShapeAvailability.
        The fault domain for the capacity report.

        If you do not specify the fault domain, the capacity report includes information about all fault domains.


        :param fault_domain: The fault_domain of this CapacityReportShapeAvailability.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def instance_shape(self):
        """
        Gets the instance_shape of this CapacityReportShapeAvailability.
        The shape that the capacity report was requested for.


        :return: The instance_shape of this CapacityReportShapeAvailability.
        :rtype: str
        """
        return self._instance_shape

    @instance_shape.setter
    def instance_shape(self, instance_shape):
        """
        Sets the instance_shape of this CapacityReportShapeAvailability.
        The shape that the capacity report was requested for.


        :param instance_shape: The instance_shape of this CapacityReportShapeAvailability.
        :type: str
        """
        self._instance_shape = instance_shape

    @property
    def instance_shape_config(self):
        """
        Gets the instance_shape_config of this CapacityReportShapeAvailability.

        :return: The instance_shape_config of this CapacityReportShapeAvailability.
        :rtype: oci.core.models.CapacityReportInstanceShapeConfig
        """
        return self._instance_shape_config

    @instance_shape_config.setter
    def instance_shape_config(self, instance_shape_config):
        """
        Sets the instance_shape_config of this CapacityReportShapeAvailability.

        :param instance_shape_config: The instance_shape_config of this CapacityReportShapeAvailability.
        :type: oci.core.models.CapacityReportInstanceShapeConfig
        """
        self._instance_shape_config = instance_shape_config

    @property
    def available_count(self):
        """
        Gets the available_count of this CapacityReportShapeAvailability.
        The total number of new instances that can be created with the specified shape configuration.


        :return: The available_count of this CapacityReportShapeAvailability.
        :rtype: int
        """
        return self._available_count

    @available_count.setter
    def available_count(self, available_count):
        """
        Sets the available_count of this CapacityReportShapeAvailability.
        The total number of new instances that can be created with the specified shape configuration.


        :param available_count: The available_count of this CapacityReportShapeAvailability.
        :type: int
        """
        self._available_count = available_count

    @property
    def availability_status(self):
        """
        Gets the availability_status of this CapacityReportShapeAvailability.
        A flag denoting whether capacity is available.

        Allowed values for this property are: "OUT_OF_HOST_CAPACITY", "HARDWARE_NOT_SUPPORTED", "AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The availability_status of this CapacityReportShapeAvailability.
        :rtype: str
        """
        return self._availability_status

    @availability_status.setter
    def availability_status(self, availability_status):
        """
        Sets the availability_status of this CapacityReportShapeAvailability.
        A flag denoting whether capacity is available.


        :param availability_status: The availability_status of this CapacityReportShapeAvailability.
        :type: str
        """
        allowed_values = ["OUT_OF_HOST_CAPACITY", "HARDWARE_NOT_SUPPORTED", "AVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability_status, allowed_values):
            availability_status = 'UNKNOWN_ENUM_VALUE'
        self._availability_status = availability_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
