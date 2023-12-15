# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .task import Task
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskFromOCIDataflowTaskDetails(Task):
    """
    The information about the OCI Dataflow task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaskFromOCIDataflowTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.TaskFromOCIDataflowTaskDetails.model_type` attribute
        of this class is ``OCI_DATAFLOW_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TaskFromOCIDataflowTaskDetails.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this TaskFromOCIDataflowTaskDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TaskFromOCIDataflowTaskDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskFromOCIDataflowTaskDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TaskFromOCIDataflowTaskDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskFromOCIDataflowTaskDetails.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskFromOCIDataflowTaskDetails.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this TaskFromOCIDataflowTaskDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this TaskFromOCIDataflowTaskDetails.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this TaskFromOCIDataflowTaskDetails.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this TaskFromOCIDataflowTaskDetails.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this TaskFromOCIDataflowTaskDetails.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this TaskFromOCIDataflowTaskDetails.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this TaskFromOCIDataflowTaskDetails.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param is_concurrent_allowed:
            The value to assign to the is_concurrent_allowed property of this TaskFromOCIDataflowTaskDetails.
        :type is_concurrent_allowed: bool

        :param metadata:
            The value to assign to the metadata property of this TaskFromOCIDataflowTaskDetails.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this TaskFromOCIDataflowTaskDetails.
        :type key_map: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this TaskFromOCIDataflowTaskDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param dataflow_application:
            The value to assign to the dataflow_application property of this TaskFromOCIDataflowTaskDetails.
        :type dataflow_application: oci.data_integration.models.DataflowApplication

        :param driver_shape_details:
            The value to assign to the driver_shape_details property of this TaskFromOCIDataflowTaskDetails.
        :type driver_shape_details: oci.data_integration.models.ShapeDetails

        :param executor_shape_details:
            The value to assign to the executor_shape_details property of this TaskFromOCIDataflowTaskDetails.
        :type executor_shape_details: oci.data_integration.models.ShapeDetails

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'config_provider_delegate': 'ConfigProvider',
            'is_concurrent_allowed': 'bool',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)',
            'registry_metadata': 'RegistryMetadata',
            'dataflow_application': 'DataflowApplication',
            'driver_shape_details': 'ShapeDetails',
            'executor_shape_details': 'ShapeDetails'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'config_provider_delegate': 'configProviderDelegate',
            'is_concurrent_allowed': 'isConcurrentAllowed',
            'metadata': 'metadata',
            'key_map': 'keyMap',
            'registry_metadata': 'registryMetadata',
            'dataflow_application': 'dataflowApplication',
            'driver_shape_details': 'driverShapeDetails',
            'executor_shape_details': 'executorShapeDetails'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._input_ports = None
        self._output_ports = None
        self._parameters = None
        self._op_config_values = None
        self._config_provider_delegate = None
        self._is_concurrent_allowed = None
        self._metadata = None
        self._key_map = None
        self._registry_metadata = None
        self._dataflow_application = None
        self._driver_shape_details = None
        self._executor_shape_details = None
        self._model_type = 'OCI_DATAFLOW_TASK'

    @property
    def dataflow_application(self):
        """
        Gets the dataflow_application of this TaskFromOCIDataflowTaskDetails.

        :return: The dataflow_application of this TaskFromOCIDataflowTaskDetails.
        :rtype: oci.data_integration.models.DataflowApplication
        """
        return self._dataflow_application

    @dataflow_application.setter
    def dataflow_application(self, dataflow_application):
        """
        Sets the dataflow_application of this TaskFromOCIDataflowTaskDetails.

        :param dataflow_application: The dataflow_application of this TaskFromOCIDataflowTaskDetails.
        :type: oci.data_integration.models.DataflowApplication
        """
        self._dataflow_application = dataflow_application

    @property
    def driver_shape_details(self):
        """
        Gets the driver_shape_details of this TaskFromOCIDataflowTaskDetails.

        :return: The driver_shape_details of this TaskFromOCIDataflowTaskDetails.
        :rtype: oci.data_integration.models.ShapeDetails
        """
        return self._driver_shape_details

    @driver_shape_details.setter
    def driver_shape_details(self, driver_shape_details):
        """
        Sets the driver_shape_details of this TaskFromOCIDataflowTaskDetails.

        :param driver_shape_details: The driver_shape_details of this TaskFromOCIDataflowTaskDetails.
        :type: oci.data_integration.models.ShapeDetails
        """
        self._driver_shape_details = driver_shape_details

    @property
    def executor_shape_details(self):
        """
        Gets the executor_shape_details of this TaskFromOCIDataflowTaskDetails.

        :return: The executor_shape_details of this TaskFromOCIDataflowTaskDetails.
        :rtype: oci.data_integration.models.ShapeDetails
        """
        return self._executor_shape_details

    @executor_shape_details.setter
    def executor_shape_details(self, executor_shape_details):
        """
        Sets the executor_shape_details of this TaskFromOCIDataflowTaskDetails.

        :param executor_shape_details: The executor_shape_details of this TaskFromOCIDataflowTaskDetails.
        :type: oci.data_integration.models.ShapeDetails
        """
        self._executor_shape_details = executor_shape_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
