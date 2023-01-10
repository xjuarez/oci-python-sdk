# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OcpuAllocationNumberParam(object):
    """
    OCPU allocation parameter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OcpuAllocationNumberParam object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpu_allocation_number:
            The value to assign to the ocpu_allocation_number property of this OcpuAllocationNumberParam.
        :type ocpu_allocation_number: float

        """
        self.swagger_types = {
            'ocpu_allocation_number': 'float'
        }

        self.attribute_map = {
            'ocpu_allocation_number': 'ocpuAllocationNumber'
        }

        self._ocpu_allocation_number = None

    @property
    def ocpu_allocation_number(self):
        """
        **[Required]** Gets the ocpu_allocation_number of this OcpuAllocationNumberParam.
        Number of OCPU allocation


        :return: The ocpu_allocation_number of this OcpuAllocationNumberParam.
        :rtype: float
        """
        return self._ocpu_allocation_number

    @ocpu_allocation_number.setter
    def ocpu_allocation_number(self, ocpu_allocation_number):
        """
        Sets the ocpu_allocation_number of this OcpuAllocationNumberParam.
        Number of OCPU allocation


        :param ocpu_allocation_number: The ocpu_allocation_number of this OcpuAllocationNumberParam.
        :type: float
        """
        self._ocpu_allocation_number = ocpu_allocation_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
