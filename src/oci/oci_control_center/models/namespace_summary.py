# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamespaceSummary(object):
    """
    A summary of the source service or application emitting the metric.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NamespaceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace_name:
            The value to assign to the namespace_name property of this NamespaceSummary.
        :type namespace_name: str

        """
        self.swagger_types = {
            'namespace_name': 'str'
        }

        self.attribute_map = {
            'namespace_name': 'namespaceName'
        }

        self._namespace_name = None

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this NamespaceSummary.
        The name of the source service emitting the metric.


        :return: The namespace_name of this NamespaceSummary.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this NamespaceSummary.
        The name of the source service emitting the metric.


        :param namespace_name: The namespace_name of this NamespaceSummary.
        :type: str
        """
        self._namespace_name = namespace_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
