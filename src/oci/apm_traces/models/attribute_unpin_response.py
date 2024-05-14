# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttributeUnpinResponse(object):
    """
    Response of an individual attribute item in the bulk unpin operation.
    """

    #: A constant which can be used with the operation_type property of a AttributeUnpinResponse.
    #: This constant has a value of "UNPIN"
    OPERATION_TYPE_UNPIN = "UNPIN"

    #: A constant which can be used with the attribute_name_space property of a AttributeUnpinResponse.
    #: This constant has a value of "TRACES"
    ATTRIBUTE_NAME_SPACE_TRACES = "TRACES"

    #: A constant which can be used with the attribute_name_space property of a AttributeUnpinResponse.
    #: This constant has a value of "SYNTHETIC"
    ATTRIBUTE_NAME_SPACE_SYNTHETIC = "SYNTHETIC"

    #: A constant which can be used with the attribute_status property of a AttributeUnpinResponse.
    #: This constant has a value of "ATTRIBUTE_UNPINNED"
    ATTRIBUTE_STATUS_ATTRIBUTE_UNPINNED = "ATTRIBUTE_UNPINNED"

    #: A constant which can be used with the attribute_status property of a AttributeUnpinResponse.
    #: This constant has a value of "DUPLICATE_ATTRIBUTE"
    ATTRIBUTE_STATUS_DUPLICATE_ATTRIBUTE = "DUPLICATE_ATTRIBUTE"

    #: A constant which can be used with the attribute_status property of a AttributeUnpinResponse.
    #: This constant has a value of "INVALID_ATTRIBUTE"
    ATTRIBUTE_STATUS_INVALID_ATTRIBUTE = "INVALID_ATTRIBUTE"

    #: A constant which can be used with the attribute_status property of a AttributeUnpinResponse.
    #: This constant has a value of "ATTRIBUTE_NOT_FOUND"
    ATTRIBUTE_STATUS_ATTRIBUTE_NOT_FOUND = "ATTRIBUTE_NOT_FOUND"

    #: A constant which can be used with the attribute_status property of a AttributeUnpinResponse.
    #: This constant has a value of "ATTRIBUTE_NOT_PROCESSED"
    ATTRIBUTE_STATUS_ATTRIBUTE_NOT_PROCESSED = "ATTRIBUTE_NOT_PROCESSED"

    def __init__(self, **kwargs):
        """
        Initializes a new AttributeUnpinResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this AttributeUnpinResponse.
        :type attribute_name: str

        :param operation_type:
            The value to assign to the operation_type property of this AttributeUnpinResponse.
            Allowed values for this property are: "UNPIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param attribute_name_space:
            The value to assign to the attribute_name_space property of this AttributeUnpinResponse.
            Allowed values for this property are: "TRACES", "SYNTHETIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attribute_name_space: str

        :param attribute_status:
            The value to assign to the attribute_status property of this AttributeUnpinResponse.
            Allowed values for this property are: "ATTRIBUTE_UNPINNED", "DUPLICATE_ATTRIBUTE", "INVALID_ATTRIBUTE", "ATTRIBUTE_NOT_FOUND", "ATTRIBUTE_NOT_PROCESSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attribute_status: str

        :param time_updated:
            The value to assign to the time_updated property of this AttributeUnpinResponse.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'operation_type': 'str',
            'attribute_name_space': 'str',
            'attribute_status': 'str',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName',
            'operation_type': 'operationType',
            'attribute_name_space': 'attributeNameSpace',
            'attribute_status': 'attributeStatus',
            'time_updated': 'timeUpdated'
        }

        self._attribute_name = None
        self._operation_type = None
        self._attribute_name_space = None
        self._attribute_status = None
        self._time_updated = None

    @property
    def attribute_name(self):
        """
        **[Required]** Gets the attribute_name of this AttributeUnpinResponse.
        Attribute that was unpinned by this bulk operation.


        :return: The attribute_name of this AttributeUnpinResponse.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """
        Sets the attribute_name of this AttributeUnpinResponse.
        Attribute that was unpinned by this bulk operation.


        :param attribute_name: The attribute_name of this AttributeUnpinResponse.
        :type: str
        """
        self._attribute_name = attribute_name

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this AttributeUnpinResponse.
        Type of operation - unpin.

        Allowed values for this property are: "UNPIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this AttributeUnpinResponse.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this AttributeUnpinResponse.
        Type of operation - unpin.


        :param operation_type: The operation_type of this AttributeUnpinResponse.
        :type: str
        """
        allowed_values = ["UNPIN"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def attribute_name_space(self):
        """
        **[Required]** Gets the attribute_name_space of this AttributeUnpinResponse.
        Namespace of the attribute whose properties were updated.  The attributeNameSpace will default to TRACES if it is
        not passed in.

        Allowed values for this property are: "TRACES", "SYNTHETIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attribute_name_space of this AttributeUnpinResponse.
        :rtype: str
        """
        return self._attribute_name_space

    @attribute_name_space.setter
    def attribute_name_space(self, attribute_name_space):
        """
        Sets the attribute_name_space of this AttributeUnpinResponse.
        Namespace of the attribute whose properties were updated.  The attributeNameSpace will default to TRACES if it is
        not passed in.


        :param attribute_name_space: The attribute_name_space of this AttributeUnpinResponse.
        :type: str
        """
        allowed_values = ["TRACES", "SYNTHETIC"]
        if not value_allowed_none_or_none_sentinel(attribute_name_space, allowed_values):
            attribute_name_space = 'UNKNOWN_ENUM_VALUE'
        self._attribute_name_space = attribute_name_space

    @property
    def attribute_status(self):
        """
        **[Required]** Gets the attribute_status of this AttributeUnpinResponse.
        Status of the attribute after this operation.  The attribute can have one of the following statuses after the unpin operation.  The attribute
        can have either a success status or an error status.  The status of the attribute must be correlated with the operation status property in the bulk operation metadata
        object.  The bulk operation will be successful only when all attributes in the bulk request are processed successfully and they get a success status back.
        The following are successful status values of individual attribute items in a bulk attribute unpin operation.
        ATTRIBUTE_UNPINNED - The attribute is marked unpinned and associated notes have been cleared.
        DUPLICATE_ATTRIBUTE - The attribute is a duplicate of an attribute that was present in this bulk request.  Note that we deduplicate the attribute collection, process only unique attributes,
        and call out duplicates.  A duplicate attribute in a bulk request will not prevent the processing of further attributes in the bulk operation.
        The following values are error statuses and the bulk processing is stopped when the first error is encountered.
        INVALID_ATTRIBUTE - The attribute is invalid.  The size of the attribute is more than a 1000 chars.
        ATTRIBUTE_NOT_FOUND - The attribute was not found in the set of pinned attributes.
        ATTRIBUTE_NOT_PROCESSED - The attribute was not processed, as there was another attribute in this bulk request collection that resulted in a processing error.

        Allowed values for this property are: "ATTRIBUTE_UNPINNED", "DUPLICATE_ATTRIBUTE", "INVALID_ATTRIBUTE", "ATTRIBUTE_NOT_FOUND", "ATTRIBUTE_NOT_PROCESSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attribute_status of this AttributeUnpinResponse.
        :rtype: str
        """
        return self._attribute_status

    @attribute_status.setter
    def attribute_status(self, attribute_status):
        """
        Sets the attribute_status of this AttributeUnpinResponse.
        Status of the attribute after this operation.  The attribute can have one of the following statuses after the unpin operation.  The attribute
        can have either a success status or an error status.  The status of the attribute must be correlated with the operation status property in the bulk operation metadata
        object.  The bulk operation will be successful only when all attributes in the bulk request are processed successfully and they get a success status back.
        The following are successful status values of individual attribute items in a bulk attribute unpin operation.
        ATTRIBUTE_UNPINNED - The attribute is marked unpinned and associated notes have been cleared.
        DUPLICATE_ATTRIBUTE - The attribute is a duplicate of an attribute that was present in this bulk request.  Note that we deduplicate the attribute collection, process only unique attributes,
        and call out duplicates.  A duplicate attribute in a bulk request will not prevent the processing of further attributes in the bulk operation.
        The following values are error statuses and the bulk processing is stopped when the first error is encountered.
        INVALID_ATTRIBUTE - The attribute is invalid.  The size of the attribute is more than a 1000 chars.
        ATTRIBUTE_NOT_FOUND - The attribute was not found in the set of pinned attributes.
        ATTRIBUTE_NOT_PROCESSED - The attribute was not processed, as there was another attribute in this bulk request collection that resulted in a processing error.


        :param attribute_status: The attribute_status of this AttributeUnpinResponse.
        :type: str
        """
        allowed_values = ["ATTRIBUTE_UNPINNED", "DUPLICATE_ATTRIBUTE", "INVALID_ATTRIBUTE", "ATTRIBUTE_NOT_FOUND", "ATTRIBUTE_NOT_PROCESSED"]
        if not value_allowed_none_or_none_sentinel(attribute_status, allowed_values):
            attribute_status = 'UNKNOWN_ENUM_VALUE'
        self._attribute_status = attribute_status

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AttributeUnpinResponse.
        Time when the attribute was activated or deactivated.  Note that ingest might not have picked up the changes even if this time has elapsed.


        :return: The time_updated of this AttributeUnpinResponse.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AttributeUnpinResponse.
        Time when the attribute was activated or deactivated.  Note that ingest might not have picked up the changes even if this time has elapsed.


        :param time_updated: The time_updated of this AttributeUnpinResponse.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
