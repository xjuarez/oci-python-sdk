# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricExtraction(object):
    """
    Specify metric extraction for SAVED_SEARCH scheduled task execution
    to post to OCI Monitoring.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricExtraction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this MetricExtraction.
        :type compartment_id: str

        :param namespace:
            The value to assign to the namespace property of this MetricExtraction.
        :type namespace: str

        :param metric_name:
            The value to assign to the metric_name property of this MetricExtraction.
        :type metric_name: str

        :param resource_group:
            The value to assign to the resource_group property of this MetricExtraction.
        :type resource_group: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'namespace': 'str',
            'metric_name': 'str',
            'resource_group': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'namespace': 'namespace',
            'metric_name': 'metricName',
            'resource_group': 'resourceGroup'
        }

        self._compartment_id = None
        self._namespace = None
        self._metric_name = None
        self._resource_group = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MetricExtraction.
        The compartment OCID (/iaas/Content/General/Concepts/identifiers.htm) of the extracted metric.


        :return: The compartment_id of this MetricExtraction.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MetricExtraction.
        The compartment OCID (/iaas/Content/General/Concepts/identifiers.htm) of the extracted metric.


        :param compartment_id: The compartment_id of this MetricExtraction.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this MetricExtraction.
        The namespace of the extracted metric.
        A valid value starts with an alphabetical character and includes only
        alphanumeric characters and underscores (_).


        :return: The namespace of this MetricExtraction.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this MetricExtraction.
        The namespace of the extracted metric.
        A valid value starts with an alphabetical character and includes only
        alphanumeric characters and underscores (_).


        :param namespace: The namespace of this MetricExtraction.
        :type: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this MetricExtraction.
        The metric name of the extracted metric.
        A valid value starts with an alphabetical character and includes only
        alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).


        :return: The metric_name of this MetricExtraction.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this MetricExtraction.
        The metric name of the extracted metric.
        A valid value starts with an alphabetical character and includes only
        alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).


        :param metric_name: The metric_name of this MetricExtraction.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def resource_group(self):
        """
        Gets the resource_group of this MetricExtraction.
        The resourceGroup of the extracted metric.
        A valid value starts with an alphabetical character and includes only
        alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).


        :return: The resource_group of this MetricExtraction.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this MetricExtraction.
        The resourceGroup of the extracted metric.
        A valid value starts with an alphabetical character and includes only
        alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).


        :param resource_group: The resource_group of this MetricExtraction.
        :type: str
        """
        self._resource_group = resource_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other