# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotebookSessionShapeConfigDetails(object):
    """
    Details for the notebook session shape configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NotebookSessionShapeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this NotebookSessionShapeConfigDetails.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this NotebookSessionShapeConfigDetails.
        :type memory_in_gbs: float

        """
        self.swagger_types = {
            'ocpus': 'float',
            'memory_in_gbs': 'float'
        }

        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs'
        }

        self._ocpus = None
        self._memory_in_gbs = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this NotebookSessionShapeConfigDetails.
        The total number of OCPUs available to the notebook session instance.


        :return: The ocpus of this NotebookSessionShapeConfigDetails.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this NotebookSessionShapeConfigDetails.
        The total number of OCPUs available to the notebook session instance.


        :param ocpus: The ocpus of this NotebookSessionShapeConfigDetails.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this NotebookSessionShapeConfigDetails.
        The total amount of memory available to the notebook session instance, in gigabytes.


        :return: The memory_in_gbs of this NotebookSessionShapeConfigDetails.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this NotebookSessionShapeConfigDetails.
        The total amount of memory available to the notebook session instance, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this NotebookSessionShapeConfigDetails.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
