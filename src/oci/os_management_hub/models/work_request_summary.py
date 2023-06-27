# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    The summary of a work request.
    """

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "INSTALL_PACKAGES"
    OPERATION_TYPE_INSTALL_PACKAGES = "INSTALL_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "REMOVE_PACKAGES"
    OPERATION_TYPE_REMOVE_PACKAGES = "REMOVE_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_PACKAGES"
    OPERATION_TYPE_UPDATE_PACKAGES = "UPDATE_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ALL_PACKAGES"
    OPERATION_TYPE_UPDATE_ALL_PACKAGES = "UPDATE_ALL_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_SECURITY"
    OPERATION_TYPE_UPDATE_SECURITY = "UPDATE_SECURITY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_BUGFIX"
    OPERATION_TYPE_UPDATE_BUGFIX = "UPDATE_BUGFIX"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ENHANCEMENT"
    OPERATION_TYPE_UPDATE_ENHANCEMENT = "UPDATE_ENHANCEMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_OTHER"
    OPERATION_TYPE_UPDATE_OTHER = "UPDATE_OTHER"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_KSPLICE_KERNEL"
    OPERATION_TYPE_UPDATE_KSPLICE_KERNEL = "UPDATE_KSPLICE_KERNEL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_KSPLICE_USERSPACE"
    OPERATION_TYPE_UPDATE_KSPLICE_USERSPACE = "UPDATE_KSPLICE_USERSPACE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ENABLE_MODULE_STREAMS"
    OPERATION_TYPE_ENABLE_MODULE_STREAMS = "ENABLE_MODULE_STREAMS"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DISABLE_MODULE_STREAMS"
    OPERATION_TYPE_DISABLE_MODULE_STREAMS = "DISABLE_MODULE_STREAMS"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SWITCH_MODULE_STREAM"
    OPERATION_TYPE_SWITCH_MODULE_STREAM = "SWITCH_MODULE_STREAM"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "INSTALL_MODULE_PROFILES"
    OPERATION_TYPE_INSTALL_MODULE_PROFILES = "INSTALL_MODULE_PROFILES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "REMOVE_MODULE_PROFILES"
    OPERATION_TYPE_REMOVE_MODULE_PROFILES = "REMOVE_MODULE_PROFILES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SET_SOFTWARE_SOURCES"
    OPERATION_TYPE_SET_SOFTWARE_SOURCES = "SET_SOFTWARE_SOURCES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "LIST_PACKAGES"
    OPERATION_TYPE_LIST_PACKAGES = "LIST_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SET_MANAGEMENT_STATION_CONFIG"
    OPERATION_TYPE_SET_MANAGEMENT_STATION_CONFIG = "SET_MANAGEMENT_STATION_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SYNC_MANAGEMENT_STATION_MIRROR"
    OPERATION_TYPE_SYNC_MANAGEMENT_STATION_MIRROR = "SYNC_MANAGEMENT_STATION_MIRROR"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_MANAGEMENT_STATION_SOFTWARE"
    OPERATION_TYPE_UPDATE_MANAGEMENT_STATION_SOFTWARE = "UPDATE_MANAGEMENT_STATION_SOFTWARE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE"
    OPERATION_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MODULE_ACTIONS"
    OPERATION_TYPE_MODULE_ACTIONS = "MODULE_ACTIONS"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "LIFECYCLE_PROMOTION"
    OPERATION_TYPE_LIFECYCLE_PROMOTION = "LIFECYCLE_PROMOTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SOFTWARE_SOURCE"
    OPERATION_TYPE_CREATE_SOFTWARE_SOURCE = "CREATE_SOFTWARE_SOURCE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_SOFTWARE_SOURCE"
    OPERATION_TYPE_UPDATE_SOFTWARE_SOURCE = "UPDATE_SOFTWARE_SOURCE"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
            Allowed values for this property are: "INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_ALL_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_KERNEL", "UPDATE_KSPLICE_USERSPACE", "ENABLE_MODULE_STREAMS", "DISABLE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "INSTALL_MODULE_PROFILES", "REMOVE_MODULE_PROFILES", "SET_SOFTWARE_SOURCES", "LIST_PACKAGES", "SET_MANAGEMENT_STATION_CONFIG", "SYNC_MANAGEMENT_STATION_MIRROR", "UPDATE_MANAGEMENT_STATION_SOFTWARE", "UPDATE", "MODULE_ACTIONS", "LIFECYCLE_PROMOTION", "CREATE_SOFTWARE_SOURCE", "UPDATE_SOFTWARE_SOURCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this WorkRequestSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this WorkRequestSummary.
        :type display_name: str

        :param message:
            The value to assign to the message property of this WorkRequestSummary.
        :type message: str

        :param parent_id:
            The value to assign to the parent_id property of this WorkRequestSummary.
        :type parent_id: str

        :param children_id:
            The value to assign to the children_id property of this WorkRequestSummary.
        :type children_id: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        :param time_created:
            The value to assign to the time_created property of this WorkRequestSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'message': 'str',
            'parent_id': 'str',
            'children_id': 'list[str]',
            'compartment_id': 'str',
            'percent_complete': 'float',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'message': 'message',
            'parent_id': 'parentId',
            'children_id': 'childrenId',
            'compartment_id': 'compartmentId',
            'percent_complete': 'percentComplete',
            'time_created': 'timeCreated'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._description = None
        self._display_name = None
        self._message = None
        self._parent_id = None
        self._children_id = None
        self._compartment_id = None
        self._percent_complete = None
        self._time_created = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        Type of the work request.

        Allowed values for this property are: "INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_ALL_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_KERNEL", "UPDATE_KSPLICE_USERSPACE", "ENABLE_MODULE_STREAMS", "DISABLE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "INSTALL_MODULE_PROFILES", "REMOVE_MODULE_PROFILES", "SET_SOFTWARE_SOURCES", "LIST_PACKAGES", "SET_MANAGEMENT_STATION_CONFIG", "SYNC_MANAGEMENT_STATION_MIRROR", "UPDATE_MANAGEMENT_STATION_SOFTWARE", "UPDATE", "MODULE_ACTIONS", "LIFECYCLE_PROMOTION", "CREATE_SOFTWARE_SOURCE", "UPDATE_SOFTWARE_SOURCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        Type of the work request.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_ALL_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_KERNEL", "UPDATE_KSPLICE_USERSPACE", "ENABLE_MODULE_STREAMS", "DISABLE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "INSTALL_MODULE_PROFILES", "REMOVE_MODULE_PROFILES", "SET_SOFTWARE_SOURCES", "LIST_PACKAGES", "SET_MANAGEMENT_STATION_CONFIG", "SYNC_MANAGEMENT_STATION_MIRROR", "UPDATE_MANAGEMENT_STATION_SOFTWARE", "UPDATE", "MODULE_ACTIONS", "LIFECYCLE_PROMOTION", "CREATE_SOFTWARE_SOURCE", "UPDATE_SOFTWARE_SOURCE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        Status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        Status of the work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The OCID of the work request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The OCID of the work request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this WorkRequestSummary.
        A short description about the work request.


        :return: The description of this WorkRequestSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkRequestSummary.
        A short description about the work request.


        :param description: The description of this WorkRequestSummary.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this WorkRequestSummary.
        A short display name for the work request.


        :return: The display_name of this WorkRequestSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WorkRequestSummary.
        A short display name for the work request.


        :param display_name: The display_name of this WorkRequestSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def message(self):
        """
        Gets the message of this WorkRequestSummary.
        A progress or error message, if there is any.


        :return: The message of this WorkRequestSummary.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestSummary.
        A progress or error message, if there is any.


        :param message: The message of this WorkRequestSummary.
        :type: str
        """
        self._message = message

    @property
    def parent_id(self):
        """
        Gets the parent_id of this WorkRequestSummary.
        The OCID of the parent work request.


        :return: The parent_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this WorkRequestSummary.
        The OCID of the parent work request.


        :param parent_id: The parent_id of this WorkRequestSummary.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def children_id(self):
        """
        Gets the children_id of this WorkRequestSummary.
        The list of OCIDs for the child work requests.


        :return: The children_id of this WorkRequestSummary.
        :rtype: list[str]
        """
        return self._children_id

    @children_id.setter
    def children_id(self, children_id):
        """
        Sets the children_id of this WorkRequestSummary.
        The list of OCIDs for the child work requests.


        :param children_id: The children_id of this WorkRequestSummary.
        :type: list[str]
        """
        self._children_id = children_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this WorkRequestSummary.
        The percentage complete of the operation tracked by this work request.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        The percentage complete of the operation tracked by this work request.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this WorkRequestSummary.
        The date and time the request was created - as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WorkRequestSummary.
        The date and time the request was created - as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this WorkRequestSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
