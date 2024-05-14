# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompositeState(object):
    """
    The composite state object provides information on the state of a task or schedule.
    """

    #: A constant which can be used with the composite_state_aggregator property of a CompositeState.
    #: This constant has a value of "TASK_SCHEDULE"
    COMPOSITE_STATE_AGGREGATOR_TASK_SCHEDULE = "TASK_SCHEDULE"

    #: A constant which can be used with the composite_state_aggregator property of a CompositeState.
    #: This constant has a value of "TASK"
    COMPOSITE_STATE_AGGREGATOR_TASK = "TASK"

    #: A constant which can be used with the composite_state_aggregator property of a CompositeState.
    #: This constant has a value of "TASK_OPERATOR"
    COMPOSITE_STATE_AGGREGATOR_TASK_OPERATOR = "TASK_OPERATOR"

    def __init__(self, **kwargs):
        """
        Initializes a new CompositeState object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param composite_state_aggregator:
            The value to assign to the composite_state_aggregator property of this CompositeState.
            Allowed values for this property are: "TASK_SCHEDULE", "TASK", "TASK_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type composite_state_aggregator: str

        :param key:
            The value to assign to the key property of this CompositeState.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this CompositeState.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this CompositeState.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CompositeState.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CompositeState.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this CompositeState.
        :type identifier: str

        :param description:
            The value to assign to the description property of this CompositeState.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this CompositeState.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this CompositeState.
        :type object_status: int

        :param all_states_map:
            The value to assign to the all_states_map property of this CompositeState.
        :type all_states_map: dict(str, State)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CompositeState.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param metadata:
            The value to assign to the metadata property of this CompositeState.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'composite_state_aggregator': 'str',
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'identifier': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'all_states_map': 'dict(str, State)',
            'registry_metadata': 'RegistryMetadata',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'composite_state_aggregator': 'compositeStateAggregator',
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'identifier': 'identifier',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'all_states_map': 'allStatesMap',
            'registry_metadata': 'registryMetadata',
            'metadata': 'metadata'
        }

        self._composite_state_aggregator = None
        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._identifier = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._all_states_map = None
        self._registry_metadata = None
        self._metadata = None

    @property
    def composite_state_aggregator(self):
        """
        Gets the composite_state_aggregator of this CompositeState.
        The type of the Composite State Aggregator.

        Allowed values for this property are: "TASK_SCHEDULE", "TASK", "TASK_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The composite_state_aggregator of this CompositeState.
        :rtype: str
        """
        return self._composite_state_aggregator

    @composite_state_aggregator.setter
    def composite_state_aggregator(self, composite_state_aggregator):
        """
        Sets the composite_state_aggregator of this CompositeState.
        The type of the Composite State Aggregator.


        :param composite_state_aggregator: The composite_state_aggregator of this CompositeState.
        :type: str
        """
        allowed_values = ["TASK_SCHEDULE", "TASK", "TASK_OPERATOR"]
        if not value_allowed_none_or_none_sentinel(composite_state_aggregator, allowed_values):
            composite_state_aggregator = 'UNKNOWN_ENUM_VALUE'
        self._composite_state_aggregator = composite_state_aggregator

    @property
    def key(self):
        """
        Gets the key of this CompositeState.
        Generated key that can be used in API calls to identify Composite State.


        :return: The key of this CompositeState.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CompositeState.
        Generated key that can be used in API calls to identify Composite State.


        :param key: The key of this CompositeState.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this CompositeState.
        The type of the object.


        :return: The model_type of this CompositeState.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CompositeState.
        The type of the object.


        :param model_type: The model_type of this CompositeState.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this CompositeState.
        The model version of an object.


        :return: The model_version of this CompositeState.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CompositeState.
        The model version of an object.


        :param model_version: The model_version of this CompositeState.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CompositeState.

        :return: The parent_ref of this CompositeState.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CompositeState.

        :param parent_ref: The parent_ref of this CompositeState.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this CompositeState.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CompositeState.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CompositeState.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CompositeState.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this CompositeState.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CompositeState.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CompositeState.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CompositeState.
        :type: str
        """
        self._identifier = identifier

    @property
    def description(self):
        """
        Gets the description of this CompositeState.
        Detailed description for the object.


        :return: The description of this CompositeState.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CompositeState.
        Detailed description for the object.


        :param description: The description of this CompositeState.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this CompositeState.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this CompositeState.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CompositeState.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this CompositeState.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this CompositeState.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CompositeState.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CompositeState.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CompositeState.
        :type: int
        """
        self._object_status = object_status

    @property
    def all_states_map(self):
        """
        Gets the all_states_map of this CompositeState.
        Map that stores all the States for a given Task or Schedule


        :return: The all_states_map of this CompositeState.
        :rtype: dict(str, State)
        """
        return self._all_states_map

    @all_states_map.setter
    def all_states_map(self, all_states_map):
        """
        Sets the all_states_map of this CompositeState.
        Map that stores all the States for a given Task or Schedule


        :param all_states_map: The all_states_map of this CompositeState.
        :type: dict(str, State)
        """
        self._all_states_map = all_states_map

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CompositeState.

        :return: The registry_metadata of this CompositeState.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CompositeState.

        :param registry_metadata: The registry_metadata of this CompositeState.
        :type: oci.data_integration.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    @property
    def metadata(self):
        """
        Gets the metadata of this CompositeState.

        :return: The metadata of this CompositeState.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CompositeState.

        :param metadata: The metadata of this CompositeState.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
