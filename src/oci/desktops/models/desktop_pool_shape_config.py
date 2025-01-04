# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopPoolShapeConfig(object):
    """
    The shape configuration used for each desktop compute instance in the desktop pool.
    """

    #: A constant which can be used with the baseline_ocpu_utilization property of a DesktopPoolShapeConfig.
    #: This constant has a value of "BASELINE_1_8"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_8 = "BASELINE_1_8"

    #: A constant which can be used with the baseline_ocpu_utilization property of a DesktopPoolShapeConfig.
    #: This constant has a value of "BASELINE_1_2"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_2 = "BASELINE_1_2"

    #: A constant which can be used with the baseline_ocpu_utilization property of a DesktopPoolShapeConfig.
    #: This constant has a value of "BASELINE_1_1"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_1 = "BASELINE_1_1"

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopPoolShapeConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this DesktopPoolShapeConfig.
        :type ocpus: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this DesktopPoolShapeConfig.
        :type memory_in_gbs: int

        :param baseline_ocpu_utilization:
            The value to assign to the baseline_ocpu_utilization property of this DesktopPoolShapeConfig.
            Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type baseline_ocpu_utilization: str

        """
        self.swagger_types = {
            'ocpus': 'int',
            'memory_in_gbs': 'int',
            'baseline_ocpu_utilization': 'str'
        }

        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'baseline_ocpu_utilization': 'baselineOcpuUtilization'
        }

        self._ocpus = None
        self._memory_in_gbs = None
        self._baseline_ocpu_utilization = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this DesktopPoolShapeConfig.
        The total number of OCPUs available for each desktop compute instance in the desktop pool.


        :return: The ocpus of this DesktopPoolShapeConfig.
        :rtype: int
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this DesktopPoolShapeConfig.
        The total number of OCPUs available for each desktop compute instance in the desktop pool.


        :param ocpus: The ocpus of this DesktopPoolShapeConfig.
        :type: int
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this DesktopPoolShapeConfig.
        The total amount of memory available in gigabytes for each desktop compute instance in the desktop pool.


        :return: The memory_in_gbs of this DesktopPoolShapeConfig.
        :rtype: int
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this DesktopPoolShapeConfig.
        The total amount of memory available in gigabytes for each desktop compute instance in the desktop pool.


        :param memory_in_gbs: The memory_in_gbs of this DesktopPoolShapeConfig.
        :type: int
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def baseline_ocpu_utilization(self):
        """
        Gets the baseline_ocpu_utilization of this DesktopPoolShapeConfig.
        The baseline OCPU utilization for a subcore burstable VM instance used for each desktop compute instance in
        the desktop pool.
        Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with
        `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance.

        Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The baseline_ocpu_utilization of this DesktopPoolShapeConfig.
        :rtype: str
        """
        return self._baseline_ocpu_utilization

    @baseline_ocpu_utilization.setter
    def baseline_ocpu_utilization(self, baseline_ocpu_utilization):
        """
        Sets the baseline_ocpu_utilization of this DesktopPoolShapeConfig.
        The baseline OCPU utilization for a subcore burstable VM instance used for each desktop compute instance in
        the desktop pool.
        Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with
        `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance.


        :param baseline_ocpu_utilization: The baseline_ocpu_utilization of this DesktopPoolShapeConfig.
        :type: str
        """
        allowed_values = ["BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"]
        if not value_allowed_none_or_none_sentinel(baseline_ocpu_utilization, allowed_values):
            baseline_ocpu_utilization = 'UNKNOWN_ENUM_VALUE'
        self._baseline_ocpu_utilization = baseline_ocpu_utilization

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
