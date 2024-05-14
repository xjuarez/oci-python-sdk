# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Worker(object):
    """
    The information about an On-premise VP worker.
    """

    #: A constant which can be used with the worker_type property of a Worker.
    #: This constant has a value of "DOCKER"
    WORKER_TYPE_DOCKER = "DOCKER"

    #: A constant which can be used with the status property of a Worker.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a Worker.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new Worker object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Worker.
        :type id: str

        :param runtime_id:
            The value to assign to the runtime_id property of this Worker.
        :type runtime_id: str

        :param display_name:
            The value to assign to the display_name property of this Worker.
        :type display_name: str

        :param name:
            The value to assign to the name property of this Worker.
        :type name: str

        :param opvp_id:
            The value to assign to the opvp_id property of this Worker.
        :type opvp_id: str

        :param opvp_name:
            The value to assign to the opvp_name property of this Worker.
        :type opvp_name: str

        :param version_details:
            The value to assign to the version_details property of this Worker.
        :type version_details: oci.apm_synthetics.models.OnPremiseVpWorkerVersionDetails

        :param configuration_details:
            The value to assign to the configuration_details property of this Worker.
        :type configuration_details: object

        :param worker_type:
            The value to assign to the worker_type property of this Worker.
            Allowed values for this property are: "DOCKER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type worker_type: str

        :param status:
            The value to assign to the status property of this Worker.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param priority:
            The value to assign to the priority property of this Worker.
        :type priority: int

        :param geo_info:
            The value to assign to the geo_info property of this Worker.
        :type geo_info: str

        :param monitor_list:
            The value to assign to the monitor_list property of this Worker.
        :type monitor_list: list[oci.apm_synthetics.models.WorkerMonitorList]

        :param identity_info:
            The value to assign to the identity_info property of this Worker.
        :type identity_info: oci.apm_synthetics.models.IdentityInfoDetails

        :param time_last_sync_up:
            The value to assign to the time_last_sync_up property of this Worker.
        :type time_last_sync_up: datetime

        :param time_created:
            The value to assign to the time_created property of this Worker.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Worker.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Worker.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Worker.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'runtime_id': 'str',
            'display_name': 'str',
            'name': 'str',
            'opvp_id': 'str',
            'opvp_name': 'str',
            'version_details': 'OnPremiseVpWorkerVersionDetails',
            'configuration_details': 'object',
            'worker_type': 'str',
            'status': 'str',
            'priority': 'int',
            'geo_info': 'str',
            'monitor_list': 'list[WorkerMonitorList]',
            'identity_info': 'IdentityInfoDetails',
            'time_last_sync_up': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'runtime_id': 'runtimeId',
            'display_name': 'displayName',
            'name': 'name',
            'opvp_id': 'opvpId',
            'opvp_name': 'opvpName',
            'version_details': 'versionDetails',
            'configuration_details': 'configurationDetails',
            'worker_type': 'workerType',
            'status': 'status',
            'priority': 'priority',
            'geo_info': 'geoInfo',
            'monitor_list': 'monitorList',
            'identity_info': 'identityInfo',
            'time_last_sync_up': 'timeLastSyncUp',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._runtime_id = None
        self._display_name = None
        self._name = None
        self._opvp_id = None
        self._opvp_name = None
        self._version_details = None
        self._configuration_details = None
        self._worker_type = None
        self._status = None
        self._priority = None
        self._geo_info = None
        self._monitor_list = None
        self._identity_info = None
        self._time_last_sync_up = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Worker.
        The `OCID`__ of the On-premise VP worker.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Worker.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Worker.
        The `OCID`__ of the On-premise VP worker.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Worker.
        :type: str
        """
        self._id = id

    @property
    def runtime_id(self):
        """
        **[Required]** Gets the runtime_id of this Worker.
        The runtime assigned id of the On-premise VP worker.


        :return: The runtime_id of this Worker.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        """
        Sets the runtime_id of this Worker.
        The runtime assigned id of the On-premise VP worker.


        :param runtime_id: The runtime_id of this Worker.
        :type: str
        """
        self._runtime_id = runtime_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Worker.
        Unique On-premise VP worker name that cannot be edited. The name should not contain any confidential information.


        :return: The display_name of this Worker.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Worker.
        Unique On-premise VP worker name that cannot be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this Worker.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Worker.
        Unique permanent name of the On-premise VP worker. This is the same as the displayName.


        :return: The name of this Worker.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Worker.
        Unique permanent name of the On-premise VP worker. This is the same as the displayName.


        :param name: The name of this Worker.
        :type: str
        """
        self._name = name

    @property
    def opvp_id(self):
        """
        **[Required]** Gets the opvp_id of this Worker.
        The `OCID`__ of the On-premise vantage point.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The opvp_id of this Worker.
        :rtype: str
        """
        return self._opvp_id

    @opvp_id.setter
    def opvp_id(self, opvp_id):
        """
        Sets the opvp_id of this Worker.
        The `OCID`__ of the On-premise vantage point.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param opvp_id: The opvp_id of this Worker.
        :type: str
        """
        self._opvp_id = opvp_id

    @property
    def opvp_name(self):
        """
        **[Required]** Gets the opvp_name of this Worker.
        On-premise vantage point name.


        :return: The opvp_name of this Worker.
        :rtype: str
        """
        return self._opvp_name

    @opvp_name.setter
    def opvp_name(self, opvp_name):
        """
        Sets the opvp_name of this Worker.
        On-premise vantage point name.


        :param opvp_name: The opvp_name of this Worker.
        :type: str
        """
        self._opvp_name = opvp_name

    @property
    def version_details(self):
        """
        **[Required]** Gets the version_details of this Worker.

        :return: The version_details of this Worker.
        :rtype: oci.apm_synthetics.models.OnPremiseVpWorkerVersionDetails
        """
        return self._version_details

    @version_details.setter
    def version_details(self, version_details):
        """
        Sets the version_details of this Worker.

        :param version_details: The version_details of this Worker.
        :type: oci.apm_synthetics.models.OnPremiseVpWorkerVersionDetails
        """
        self._version_details = version_details

    @property
    def configuration_details(self):
        """
        Gets the configuration_details of this Worker.
        Configuration details of the On-premise VP worker.


        :return: The configuration_details of this Worker.
        :rtype: object
        """
        return self._configuration_details

    @configuration_details.setter
    def configuration_details(self, configuration_details):
        """
        Sets the configuration_details of this Worker.
        Configuration details of the On-premise VP worker.


        :param configuration_details: The configuration_details of this Worker.
        :type: object
        """
        self._configuration_details = configuration_details

    @property
    def worker_type(self):
        """
        **[Required]** Gets the worker_type of this Worker.
        Type of the On-premise VP worker.

        Allowed values for this property are: "DOCKER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The worker_type of this Worker.
        :rtype: str
        """
        return self._worker_type

    @worker_type.setter
    def worker_type(self, worker_type):
        """
        Sets the worker_type of this Worker.
        Type of the On-premise VP worker.


        :param worker_type: The worker_type of this Worker.
        :type: str
        """
        allowed_values = ["DOCKER"]
        if not value_allowed_none_or_none_sentinel(worker_type, allowed_values):
            worker_type = 'UNKNOWN_ENUM_VALUE'
        self._worker_type = worker_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this Worker.
        Enables or disables the On-premise VP worker.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this Worker.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Worker.
        Enables or disables the On-premise VP worker.


        :param status: The status of this Worker.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def priority(self):
        """
        **[Required]** Gets the priority of this Worker.
        Priority of the On-premise VP worker to schedule monitors.


        :return: The priority of this Worker.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this Worker.
        Priority of the On-premise VP worker to schedule monitors.


        :param priority: The priority of this Worker.
        :type: int
        """
        self._priority = priority

    @property
    def geo_info(self):
        """
        Gets the geo_info of this Worker.
        Geographical information of the On-premise VP worker.


        :return: The geo_info of this Worker.
        :rtype: str
        """
        return self._geo_info

    @geo_info.setter
    def geo_info(self, geo_info):
        """
        Sets the geo_info of this Worker.
        Geographical information of the On-premise VP worker.


        :param geo_info: The geo_info of this Worker.
        :type: str
        """
        self._geo_info = geo_info

    @property
    def monitor_list(self):
        """
        Gets the monitor_list of this Worker.
        Monitors list assigned to the On-premise VP worker.


        :return: The monitor_list of this Worker.
        :rtype: list[oci.apm_synthetics.models.WorkerMonitorList]
        """
        return self._monitor_list

    @monitor_list.setter
    def monitor_list(self, monitor_list):
        """
        Sets the monitor_list of this Worker.
        Monitors list assigned to the On-premise VP worker.


        :param monitor_list: The monitor_list of this Worker.
        :type: list[oci.apm_synthetics.models.WorkerMonitorList]
        """
        self._monitor_list = monitor_list

    @property
    def identity_info(self):
        """
        Gets the identity_info of this Worker.

        :return: The identity_info of this Worker.
        :rtype: oci.apm_synthetics.models.IdentityInfoDetails
        """
        return self._identity_info

    @identity_info.setter
    def identity_info(self, identity_info):
        """
        Sets the identity_info of this Worker.

        :param identity_info: The identity_info of this Worker.
        :type: oci.apm_synthetics.models.IdentityInfoDetails
        """
        self._identity_info = identity_info

    @property
    def time_last_sync_up(self):
        """
        Gets the time_last_sync_up of this Worker.
        The time the resource was last synced, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_sync_up of this Worker.
        :rtype: datetime
        """
        return self._time_last_sync_up

    @time_last_sync_up.setter
    def time_last_sync_up(self, time_last_sync_up):
        """
        Sets the time_last_sync_up of this Worker.
        The time the resource was last synced, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_sync_up: The time_last_sync_up of this Worker.
        :type: datetime
        """
        self._time_last_sync_up = time_last_sync_up

    @property
    def time_created(self):
        """
        Gets the time_created of this Worker.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Worker.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Worker.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Worker.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Worker.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Worker.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Worker.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Worker.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Worker.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Worker.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Worker.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Worker.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Worker.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Worker.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Worker.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Worker.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
