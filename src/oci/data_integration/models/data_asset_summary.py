# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummary(object):
    """
    The summary object for data asset.
    """

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "ORACLE_DATA_ASSET"
    MODEL_TYPE_ORACLE_DATA_ASSET = "ORACLE_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE_DATA_ASSET"
    MODEL_TYPE_ORACLE_OBJECT_STORAGE_DATA_ASSET = "ORACLE_OBJECT_STORAGE_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "ORACLE_ATP_DATA_ASSET"
    MODEL_TYPE_ORACLE_ATP_DATA_ASSET = "ORACLE_ATP_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "ORACLE_ADWC_DATA_ASSET"
    MODEL_TYPE_ORACLE_ADWC_DATA_ASSET = "ORACLE_ADWC_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "MYSQL_DATA_ASSET"
    MODEL_TYPE_MYSQL_DATA_ASSET = "MYSQL_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "GENERIC_JDBC_DATA_ASSET"
    MODEL_TYPE_GENERIC_JDBC_DATA_ASSET = "GENERIC_JDBC_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "FUSION_APP_DATA_ASSET"
    MODEL_TYPE_FUSION_APP_DATA_ASSET = "FUSION_APP_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "AMAZON_S3_DATA_ASSET"
    MODEL_TYPE_AMAZON_S3_DATA_ASSET = "AMAZON_S3_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "LAKE_DATA_ASSET"
    MODEL_TYPE_LAKE_DATA_ASSET = "LAKE_DATA_ASSET"

    #: A constant which can be used with the model_type property of a DataAssetSummary.
    #: This constant has a value of "REST_DATA_ASSET"
    MODEL_TYPE_REST_DATA_ASSET = "REST_DATA_ASSET"

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.DataAssetSummaryFromMySQL`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromAtp`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromAdwc`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromJdbc`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromAmazonS3`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromObjectStorage`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromLake`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromRest`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromOracle`
        * :class:`~oci.data_integration.models.DataAssetSummaryFromFusionApp`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetSummary.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_DATA_ASSET", "REST_DATA_ASSET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetSummary.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetSummary.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetSummary.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetSummary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetSummary.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetSummary.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetSummary.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetSummary.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetSummary.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetSummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'native_type_system': 'TypeSystem',
            'object_version': 'int',
            'parent_ref': 'ParentReference',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'native_type_system': 'nativeTypeSystem',
            'object_version': 'objectVersion',
            'parent_ref': 'parentRef',
            'metadata': 'metadata'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._native_type_system = None
        self._object_version = None
        self._parent_ref = None
        self._metadata = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'MYSQL_DATA_ASSET':
            return 'DataAssetSummaryFromMySQL'

        if type == 'ORACLE_ATP_DATA_ASSET':
            return 'DataAssetSummaryFromAtp'

        if type == 'ORACLE_ADWC_DATA_ASSET':
            return 'DataAssetSummaryFromAdwc'

        if type == 'GENERIC_JDBC_DATA_ASSET':
            return 'DataAssetSummaryFromJdbc'

        if type == 'AMAZON_S3_DATA_ASSET':
            return 'DataAssetSummaryFromAmazonS3'

        if type == 'ORACLE_OBJECT_STORAGE_DATA_ASSET':
            return 'DataAssetSummaryFromObjectStorage'

        if type == 'LAKE_DATA_ASSET':
            return 'DataAssetSummaryFromLake'

        if type == 'REST_DATA_ASSET':
            return 'DataAssetSummaryFromRest'

        if type == 'ORACLE_DATA_ASSET':
            return 'DataAssetSummaryFromOracle'

        if type == 'FUSION_APP_DATA_ASSET':
            return 'DataAssetSummaryFromFusionApp'
        else:
            return 'DataAssetSummary'

    @property
    def model_type(self):
        """
        Gets the model_type of this DataAssetSummary.
        The type of the data asset.

        Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_DATA_ASSET", "REST_DATA_ASSET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this DataAssetSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DataAssetSummary.
        The type of the data asset.


        :param model_type: The model_type of this DataAssetSummary.
        :type: str
        """
        allowed_values = ["ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_DATA_ASSET", "REST_DATA_ASSET"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this DataAssetSummary.
        Generated key that can be used in API calls to identify data asset.


        :return: The key of this DataAssetSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataAssetSummary.
        Generated key that can be used in API calls to identify data asset.


        :param key: The key of this DataAssetSummary.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DataAssetSummary.
        The model version of an object.


        :return: The model_version of this DataAssetSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DataAssetSummary.
        The model version of an object.


        :param model_version: The model_version of this DataAssetSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this DataAssetSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this DataAssetSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataAssetSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this DataAssetSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DataAssetSummary.
        The user-defined description of the data asset.


        :return: The description of this DataAssetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataAssetSummary.
        The user-defined description of the data asset.


        :param description: The description of this DataAssetSummary.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this DataAssetSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DataAssetSummary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DataAssetSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DataAssetSummary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this DataAssetSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this DataAssetSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DataAssetSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DataAssetSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def external_key(self):
        """
        Gets the external_key of this DataAssetSummary.
        The external key for the object.


        :return: The external_key of this DataAssetSummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this DataAssetSummary.
        The external key for the object.


        :param external_key: The external_key of this DataAssetSummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def asset_properties(self):
        """
        Gets the asset_properties of this DataAssetSummary.
        Additional properties for the data asset.


        :return: The asset_properties of this DataAssetSummary.
        :rtype: dict(str, str)
        """
        return self._asset_properties

    @asset_properties.setter
    def asset_properties(self, asset_properties):
        """
        Sets the asset_properties of this DataAssetSummary.
        Additional properties for the data asset.


        :param asset_properties: The asset_properties of this DataAssetSummary.
        :type: dict(str, str)
        """
        self._asset_properties = asset_properties

    @property
    def native_type_system(self):
        """
        Gets the native_type_system of this DataAssetSummary.

        :return: The native_type_system of this DataAssetSummary.
        :rtype: oci.data_integration.models.TypeSystem
        """
        return self._native_type_system

    @native_type_system.setter
    def native_type_system(self, native_type_system):
        """
        Sets the native_type_system of this DataAssetSummary.

        :param native_type_system: The native_type_system of this DataAssetSummary.
        :type: oci.data_integration.models.TypeSystem
        """
        self._native_type_system = native_type_system

    @property
    def object_version(self):
        """
        Gets the object_version of this DataAssetSummary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DataAssetSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DataAssetSummary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DataAssetSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DataAssetSummary.

        :return: The parent_ref of this DataAssetSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DataAssetSummary.

        :param parent_ref: The parent_ref of this DataAssetSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def metadata(self):
        """
        Gets the metadata of this DataAssetSummary.

        :return: The metadata of this DataAssetSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DataAssetSummary.

        :param metadata: The metadata of this DataAssetSummary.
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
