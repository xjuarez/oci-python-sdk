# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkDeActivationMetadata(object):
    """
    Metadata about the bulk deactivation operation.  The bulk deactivation operation is atomic and binary.  If the processing of any of the attributes
    in the bulk deactivation request results in a processing or validation error, then none of the attributes in the request are deactivated.
    The bulk deactivation request succeeds only when all the attributes in the bulk deactivation request are processed and they get a successful
    attributeStatus back.
    """

    #: A constant which can be used with the operation_status property of a BulkDeActivationMetadata.
    #: This constant has a value of "SUCCESS"
    OPERATION_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the operation_status property of a BulkDeActivationMetadata.
    #: This constant has a value of "EMPTY_ATTRIBUTE_LIST"
    OPERATION_STATUS_EMPTY_ATTRIBUTE_LIST = "EMPTY_ATTRIBUTE_LIST"

    #: A constant which can be used with the operation_status property of a BulkDeActivationMetadata.
    #: This constant has a value of "NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED"
    OPERATION_STATUS_NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED = "NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED"

    #: A constant which can be used with the operation_status property of a BulkDeActivationMetadata.
    #: This constant has a value of "STRING_ATTRIBUTE_LIMIT_EXCEEDED"
    OPERATION_STATUS_STRING_ATTRIBUTE_LIMIT_EXCEEDED = "STRING_ATTRIBUTE_LIMIT_EXCEEDED"

    #: A constant which can be used with the operation_status property of a BulkDeActivationMetadata.
    #: This constant has a value of "INVALID_BULK_REQUEST"
    OPERATION_STATUS_INVALID_BULK_REQUEST = "INVALID_BULK_REQUEST"

    #: A constant which can be used with the operation_type property of a BulkDeActivationMetadata.
    #: This constant has a value of "DEACTIVATE"
    OPERATION_TYPE_DEACTIVATE = "DEACTIVATE"

    def __init__(self, **kwargs):
        """
        Initializes a new BulkDeActivationMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_status:
            The value to assign to the operation_status property of this BulkDeActivationMetadata.
            Allowed values for this property are: "SUCCESS", "EMPTY_ATTRIBUTE_LIST", "NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED", "STRING_ATTRIBUTE_LIMIT_EXCEEDED", "INVALID_BULK_REQUEST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_status: str

        :param operation_type:
            The value to assign to the operation_type property of this BulkDeActivationMetadata.
            Allowed values for this property are: "DEACTIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param attributes_de_activated:
            The value to assign to the attributes_de_activated property of this BulkDeActivationMetadata.
        :type attributes_de_activated: int

        :param synthetic_attributes_de_activated:
            The value to assign to the synthetic_attributes_de_activated property of this BulkDeActivationMetadata.
        :type synthetic_attributes_de_activated: int

        :param available_string_attributes:
            The value to assign to the available_string_attributes property of this BulkDeActivationMetadata.
        :type available_string_attributes: int

        :param available_numeric_attributes:
            The value to assign to the available_numeric_attributes property of this BulkDeActivationMetadata.
        :type available_numeric_attributes: int

        :param available_synthetic_string_attributes:
            The value to assign to the available_synthetic_string_attributes property of this BulkDeActivationMetadata.
        :type available_synthetic_string_attributes: int

        :param available_synthetic_numeric_attributes:
            The value to assign to the available_synthetic_numeric_attributes property of this BulkDeActivationMetadata.
        :type available_synthetic_numeric_attributes: int

        """
        self.swagger_types = {
            'operation_status': 'str',
            'operation_type': 'str',
            'attributes_de_activated': 'int',
            'synthetic_attributes_de_activated': 'int',
            'available_string_attributes': 'int',
            'available_numeric_attributes': 'int',
            'available_synthetic_string_attributes': 'int',
            'available_synthetic_numeric_attributes': 'int'
        }

        self.attribute_map = {
            'operation_status': 'operationStatus',
            'operation_type': 'operationType',
            'attributes_de_activated': 'attributesDeActivated',
            'synthetic_attributes_de_activated': 'syntheticAttributesDeActivated',
            'available_string_attributes': 'availableStringAttributes',
            'available_numeric_attributes': 'availableNumericAttributes',
            'available_synthetic_string_attributes': 'availableSyntheticStringAttributes',
            'available_synthetic_numeric_attributes': 'availableSyntheticNumericAttributes'
        }

        self._operation_status = None
        self._operation_type = None
        self._attributes_de_activated = None
        self._synthetic_attributes_de_activated = None
        self._available_string_attributes = None
        self._available_numeric_attributes = None
        self._available_synthetic_string_attributes = None
        self._available_synthetic_numeric_attributes = None

    @property
    def operation_status(self):
        """
        **[Required]** Gets the operation_status of this BulkDeActivationMetadata.
        Operation status of the bulk deactivation operation.  The bulk deactivation operation could have either a success or an error status as defined below.  Note that
        if a bulk operation has not succeeded, we do not deactivate any tags in the request set.
        SUCCESS - The bulk deactivation operation has succeeded and all the attributes in the bulk deactivation request have been deactivated by this operation or deactivated earlier.
        The following are error statuses for the bulk deactivation operation.  Note that none of the attributes (string or numeric) in the bulk request have been deactivated by this bulk
        deactivation operation if any of the below statuses are returned.
        EMPTY_ATTRIBUTE_LIST - The bulk deactivation request object was empty and did not contain any attributes to be deactivated.
        NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED - The number of numeric attributes in the bulk request exceeded the maximum limit (100) of numeric attributes that could be present in the APM Domain.
        STRING_ATTRIBUTE_LIMIT_EXCEEDED - The number of string attributes in the bulk request exceeded the maximum limit (700) of string attributes that could be present in the APM Domain.
        INVALID_BULK_REQUEST - The bulk request contains invalid attribute(s), or attribute(s) that resulted in a validation error, or an attribute that resulted
        in a processing error.

        Allowed values for this property are: "SUCCESS", "EMPTY_ATTRIBUTE_LIST", "NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED", "STRING_ATTRIBUTE_LIMIT_EXCEEDED", "INVALID_BULK_REQUEST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_status of this BulkDeActivationMetadata.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """
        Sets the operation_status of this BulkDeActivationMetadata.
        Operation status of the bulk deactivation operation.  The bulk deactivation operation could have either a success or an error status as defined below.  Note that
        if a bulk operation has not succeeded, we do not deactivate any tags in the request set.
        SUCCESS - The bulk deactivation operation has succeeded and all the attributes in the bulk deactivation request have been deactivated by this operation or deactivated earlier.
        The following are error statuses for the bulk deactivation operation.  Note that none of the attributes (string or numeric) in the bulk request have been deactivated by this bulk
        deactivation operation if any of the below statuses are returned.
        EMPTY_ATTRIBUTE_LIST - The bulk deactivation request object was empty and did not contain any attributes to be deactivated.
        NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED - The number of numeric attributes in the bulk request exceeded the maximum limit (100) of numeric attributes that could be present in the APM Domain.
        STRING_ATTRIBUTE_LIMIT_EXCEEDED - The number of string attributes in the bulk request exceeded the maximum limit (700) of string attributes that could be present in the APM Domain.
        INVALID_BULK_REQUEST - The bulk request contains invalid attribute(s), or attribute(s) that resulted in a validation error, or an attribute that resulted
        in a processing error.


        :param operation_status: The operation_status of this BulkDeActivationMetadata.
        :type: str
        """
        allowed_values = ["SUCCESS", "EMPTY_ATTRIBUTE_LIST", "NUMERIC_ATTRIBUTE_LIMIT_EXCEEDED", "STRING_ATTRIBUTE_LIMIT_EXCEEDED", "INVALID_BULK_REQUEST"]
        if not value_allowed_none_or_none_sentinel(operation_status, allowed_values):
            operation_status = 'UNKNOWN_ENUM_VALUE'
        self._operation_status = operation_status

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this BulkDeActivationMetadata.
        Type of operation.

        Allowed values for this property are: "DEACTIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this BulkDeActivationMetadata.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this BulkDeActivationMetadata.
        Type of operation.


        :param operation_type: The operation_type of this BulkDeActivationMetadata.
        :type: str
        """
        allowed_values = ["DEACTIVATE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def attributes_de_activated(self):
        """
        Gets the attributes_de_activated of this BulkDeActivationMetadata.
        Total number attributes (both string and numeric) in TRACES namespace that were deactivated.


        :return: The attributes_de_activated of this BulkDeActivationMetadata.
        :rtype: int
        """
        return self._attributes_de_activated

    @attributes_de_activated.setter
    def attributes_de_activated(self, attributes_de_activated):
        """
        Sets the attributes_de_activated of this BulkDeActivationMetadata.
        Total number attributes (both string and numeric) in TRACES namespace that were deactivated.


        :param attributes_de_activated: The attributes_de_activated of this BulkDeActivationMetadata.
        :type: int
        """
        self._attributes_de_activated = attributes_de_activated

    @property
    def synthetic_attributes_de_activated(self):
        """
        Gets the synthetic_attributes_de_activated of this BulkDeActivationMetadata.
        Total number attributes (both string and numeric) in SYNTHETIC namespace that were deactivated.


        :return: The synthetic_attributes_de_activated of this BulkDeActivationMetadata.
        :rtype: int
        """
        return self._synthetic_attributes_de_activated

    @synthetic_attributes_de_activated.setter
    def synthetic_attributes_de_activated(self, synthetic_attributes_de_activated):
        """
        Sets the synthetic_attributes_de_activated of this BulkDeActivationMetadata.
        Total number attributes (both string and numeric) in SYNTHETIC namespace that were deactivated.


        :param synthetic_attributes_de_activated: The synthetic_attributes_de_activated of this BulkDeActivationMetadata.
        :type: int
        """
        self._synthetic_attributes_de_activated = synthetic_attributes_de_activated

    @property
    def available_string_attributes(self):
        """
        Gets the available_string_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional string attributes in TRACES namespace in the APM Domain.


        :return: The available_string_attributes of this BulkDeActivationMetadata.
        :rtype: int
        """
        return self._available_string_attributes

    @available_string_attributes.setter
    def available_string_attributes(self, available_string_attributes):
        """
        Sets the available_string_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional string attributes in TRACES namespace in the APM Domain.


        :param available_string_attributes: The available_string_attributes of this BulkDeActivationMetadata.
        :type: int
        """
        self._available_string_attributes = available_string_attributes

    @property
    def available_numeric_attributes(self):
        """
        Gets the available_numeric_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional numeric attributes in TRACES namespace in the APM Domain.


        :return: The available_numeric_attributes of this BulkDeActivationMetadata.
        :rtype: int
        """
        return self._available_numeric_attributes

    @available_numeric_attributes.setter
    def available_numeric_attributes(self, available_numeric_attributes):
        """
        Sets the available_numeric_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional numeric attributes in TRACES namespace in the APM Domain.


        :param available_numeric_attributes: The available_numeric_attributes of this BulkDeActivationMetadata.
        :type: int
        """
        self._available_numeric_attributes = available_numeric_attributes

    @property
    def available_synthetic_string_attributes(self):
        """
        Gets the available_synthetic_string_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional string attributes in SYNTHETIC namespace in the APM Domain.


        :return: The available_synthetic_string_attributes of this BulkDeActivationMetadata.
        :rtype: int
        """
        return self._available_synthetic_string_attributes

    @available_synthetic_string_attributes.setter
    def available_synthetic_string_attributes(self, available_synthetic_string_attributes):
        """
        Sets the available_synthetic_string_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional string attributes in SYNTHETIC namespace in the APM Domain.


        :param available_synthetic_string_attributes: The available_synthetic_string_attributes of this BulkDeActivationMetadata.
        :type: int
        """
        self._available_synthetic_string_attributes = available_synthetic_string_attributes

    @property
    def available_synthetic_numeric_attributes(self):
        """
        Gets the available_synthetic_numeric_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional numeric attributes in SYNTHETIC namespace in the APM Domain.


        :return: The available_synthetic_numeric_attributes of this BulkDeActivationMetadata.
        :rtype: int
        """
        return self._available_synthetic_numeric_attributes

    @available_synthetic_numeric_attributes.setter
    def available_synthetic_numeric_attributes(self, available_synthetic_numeric_attributes):
        """
        Sets the available_synthetic_numeric_attributes of this BulkDeActivationMetadata.
        Total number of free slots available for activation of additional numeric attributes in SYNTHETIC namespace in the APM Domain.


        :param available_synthetic_numeric_attributes: The available_synthetic_numeric_attributes of this BulkDeActivationMetadata.
        :type: int
        """
        self._available_synthetic_numeric_attributes = available_synthetic_numeric_attributes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
