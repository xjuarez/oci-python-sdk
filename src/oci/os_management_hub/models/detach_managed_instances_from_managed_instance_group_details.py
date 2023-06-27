# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachManagedInstancesFromManagedInstanceGroupDetails(object):
    """
    The managed instance OCIDs to detach from the managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachManagedInstancesFromManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param managed_instances:
            The value to assign to the managed_instances property of this DetachManagedInstancesFromManagedInstanceGroupDetails.
        :type managed_instances: list[str]

        """
        self.swagger_types = {
            'managed_instances': 'list[str]'
        }

        self.attribute_map = {
            'managed_instances': 'managedInstances'
        }

        self._managed_instances = None

    @property
    def managed_instances(self):
        """
        Gets the managed_instances of this DetachManagedInstancesFromManagedInstanceGroupDetails.
        The list of managed instance OCIDs to be detached.


        :return: The managed_instances of this DetachManagedInstancesFromManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._managed_instances

    @managed_instances.setter
    def managed_instances(self, managed_instances):
        """
        Sets the managed_instances of this DetachManagedInstancesFromManagedInstanceGroupDetails.
        The list of managed instance OCIDs to be detached.


        :param managed_instances: The managed_instances of this DetachManagedInstancesFromManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._managed_instances = managed_instances

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
