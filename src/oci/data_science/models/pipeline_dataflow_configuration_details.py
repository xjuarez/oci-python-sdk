# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineDataflowConfigurationDetails(object):
    """
    The configuration details of a Dataflow step.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineDataflowConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param configuration:
            The value to assign to the configuration property of this PipelineDataflowConfigurationDetails.
        :type configuration: object

        :param driver_shape:
            The value to assign to the driver_shape property of this PipelineDataflowConfigurationDetails.
        :type driver_shape: str

        :param driver_shape_config_details:
            The value to assign to the driver_shape_config_details property of this PipelineDataflowConfigurationDetails.
        :type driver_shape_config_details: oci.data_science.models.PipelineShapeConfigDetails

        :param executor_shape:
            The value to assign to the executor_shape property of this PipelineDataflowConfigurationDetails.
        :type executor_shape: str

        :param executor_shape_config_details:
            The value to assign to the executor_shape_config_details property of this PipelineDataflowConfigurationDetails.
        :type executor_shape_config_details: oci.data_science.models.PipelineShapeConfigDetails

        :param num_executors:
            The value to assign to the num_executors property of this PipelineDataflowConfigurationDetails.
        :type num_executors: int

        :param warehouse_bucket_uri:
            The value to assign to the warehouse_bucket_uri property of this PipelineDataflowConfigurationDetails.
        :type warehouse_bucket_uri: str

        :param logs_bucket_uri:
            The value to assign to the logs_bucket_uri property of this PipelineDataflowConfigurationDetails.
        :type logs_bucket_uri: str

        """
        self.swagger_types = {
            'configuration': 'object',
            'driver_shape': 'str',
            'driver_shape_config_details': 'PipelineShapeConfigDetails',
            'executor_shape': 'str',
            'executor_shape_config_details': 'PipelineShapeConfigDetails',
            'num_executors': 'int',
            'warehouse_bucket_uri': 'str',
            'logs_bucket_uri': 'str'
        }

        self.attribute_map = {
            'configuration': 'configuration',
            'driver_shape': 'driverShape',
            'driver_shape_config_details': 'driverShapeConfigDetails',
            'executor_shape': 'executorShape',
            'executor_shape_config_details': 'executorShapeConfigDetails',
            'num_executors': 'numExecutors',
            'warehouse_bucket_uri': 'warehouseBucketUri',
            'logs_bucket_uri': 'logsBucketUri'
        }

        self._configuration = None
        self._driver_shape = None
        self._driver_shape_config_details = None
        self._executor_shape = None
        self._executor_shape_config_details = None
        self._num_executors = None
        self._warehouse_bucket_uri = None
        self._logs_bucket_uri = None

    @property
    def configuration(self):
        """
        Gets the configuration of this PipelineDataflowConfigurationDetails.
        The Spark configuration passed to the running process.


        :return: The configuration of this PipelineDataflowConfigurationDetails.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this PipelineDataflowConfigurationDetails.
        The Spark configuration passed to the running process.


        :param configuration: The configuration of this PipelineDataflowConfigurationDetails.
        :type: object
        """
        self._configuration = configuration

    @property
    def driver_shape(self):
        """
        Gets the driver_shape of this PipelineDataflowConfigurationDetails.
        The VM shape for the driver.


        :return: The driver_shape of this PipelineDataflowConfigurationDetails.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this PipelineDataflowConfigurationDetails.
        The VM shape for the driver.


        :param driver_shape: The driver_shape of this PipelineDataflowConfigurationDetails.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def driver_shape_config_details(self):
        """
        Gets the driver_shape_config_details of this PipelineDataflowConfigurationDetails.

        :return: The driver_shape_config_details of this PipelineDataflowConfigurationDetails.
        :rtype: oci.data_science.models.PipelineShapeConfigDetails
        """
        return self._driver_shape_config_details

    @driver_shape_config_details.setter
    def driver_shape_config_details(self, driver_shape_config_details):
        """
        Sets the driver_shape_config_details of this PipelineDataflowConfigurationDetails.

        :param driver_shape_config_details: The driver_shape_config_details of this PipelineDataflowConfigurationDetails.
        :type: oci.data_science.models.PipelineShapeConfigDetails
        """
        self._driver_shape_config_details = driver_shape_config_details

    @property
    def executor_shape(self):
        """
        Gets the executor_shape of this PipelineDataflowConfigurationDetails.
        The VM shape for the executors.


        :return: The executor_shape of this PipelineDataflowConfigurationDetails.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this PipelineDataflowConfigurationDetails.
        The VM shape for the executors.


        :param executor_shape: The executor_shape of this PipelineDataflowConfigurationDetails.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def executor_shape_config_details(self):
        """
        Gets the executor_shape_config_details of this PipelineDataflowConfigurationDetails.

        :return: The executor_shape_config_details of this PipelineDataflowConfigurationDetails.
        :rtype: oci.data_science.models.PipelineShapeConfigDetails
        """
        return self._executor_shape_config_details

    @executor_shape_config_details.setter
    def executor_shape_config_details(self, executor_shape_config_details):
        """
        Sets the executor_shape_config_details of this PipelineDataflowConfigurationDetails.

        :param executor_shape_config_details: The executor_shape_config_details of this PipelineDataflowConfigurationDetails.
        :type: oci.data_science.models.PipelineShapeConfigDetails
        """
        self._executor_shape_config_details = executor_shape_config_details

    @property
    def num_executors(self):
        """
        Gets the num_executors of this PipelineDataflowConfigurationDetails.
        The number of executor VMs requested.


        :return: The num_executors of this PipelineDataflowConfigurationDetails.
        :rtype: int
        """
        return self._num_executors

    @num_executors.setter
    def num_executors(self, num_executors):
        """
        Sets the num_executors of this PipelineDataflowConfigurationDetails.
        The number of executor VMs requested.


        :param num_executors: The num_executors of this PipelineDataflowConfigurationDetails.
        :type: int
        """
        self._num_executors = num_executors

    @property
    def warehouse_bucket_uri(self):
        """
        Gets the warehouse_bucket_uri of this PipelineDataflowConfigurationDetails.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs.


        :return: The warehouse_bucket_uri of this PipelineDataflowConfigurationDetails.
        :rtype: str
        """
        return self._warehouse_bucket_uri

    @warehouse_bucket_uri.setter
    def warehouse_bucket_uri(self, warehouse_bucket_uri):
        """
        Sets the warehouse_bucket_uri of this PipelineDataflowConfigurationDetails.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs.


        :param warehouse_bucket_uri: The warehouse_bucket_uri of this PipelineDataflowConfigurationDetails.
        :type: str
        """
        self._warehouse_bucket_uri = warehouse_bucket_uri

    @property
    def logs_bucket_uri(self):
        """
        Gets the logs_bucket_uri of this PipelineDataflowConfigurationDetails.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.


        :return: The logs_bucket_uri of this PipelineDataflowConfigurationDetails.
        :rtype: str
        """
        return self._logs_bucket_uri

    @logs_bucket_uri.setter
    def logs_bucket_uri(self, logs_bucket_uri):
        """
        Sets the logs_bucket_uri of this PipelineDataflowConfigurationDetails.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.


        :param logs_bucket_uri: The logs_bucket_uri of this PipelineDataflowConfigurationDetails.
        :type: str
        """
        self._logs_bucket_uri = logs_bucket_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
