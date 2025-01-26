# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 0.0.1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseService(object):
    """
    Object representing a single service.
    """

    #: A constant which can be used with the platform_type property of a BaseService.
    #: This constant has a value of "IAAS"
    PLATFORM_TYPE_IAAS = "IAAS"

    #: A constant which can be used with the platform_type property of a BaseService.
    #: This constant has a value of "SAAS"
    PLATFORM_TYPE_SAAS = "SAAS"

    #: A constant which can be used with the platform_type property of a BaseService.
    #: This constant has a value of "PAAS"
    PLATFORM_TYPE_PAAS = "PAAS"

    #: A constant which can be used with the comms_manager_name property of a BaseService.
    #: This constant has a value of "CN"
    COMMS_MANAGER_NAME_CN = "CN"

    #: A constant which can be used with the comms_manager_name property of a BaseService.
    #: This constant has a value of "FUSION"
    COMMS_MANAGER_NAME_FUSION = "FUSION"

    #: A constant which can be used with the comms_manager_name property of a BaseService.
    #: This constant has a value of "AS"
    COMMS_MANAGER_NAME_AS = "AS"

    #: A constant which can be used with the comms_manager_name property of a BaseService.
    #: This constant has a value of "ERF"
    COMMS_MANAGER_NAME_ERF = "ERF"

    #: A constant which can be used with the lifecycle_state property of a BaseService.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BaseService.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new BaseService object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.announcements_service.models.Service`
        * :class:`~oci.announcements_service.models.ServiceSummary`
        * :class:`~oci.announcements_service.models.NotificationsSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BaseService.
        :type type: str

        :param id:
            The value to assign to the id property of this BaseService.
        :type id: str

        :param service_name:
            The value to assign to the service_name property of this BaseService.
        :type service_name: str

        :param short_name:
            The value to assign to the short_name property of this BaseService.
        :type short_name: str

        :param team_name:
            The value to assign to the team_name property of this BaseService.
        :type team_name: str

        :param platform_type:
            The value to assign to the platform_type property of this BaseService.
            Allowed values for this property are: "IAAS", "SAAS", "PAAS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param comms_manager_name:
            The value to assign to the comms_manager_name property of this BaseService.
            Allowed values for this property are: "CN", "FUSION", "AS", "ERF", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type comms_manager_name: str

        :param excluded_realms:
            The value to assign to the excluded_realms property of this BaseService.
        :type excluded_realms: list[str]

        :param previous_service_names:
            The value to assign to the previous_service_names property of this BaseService.
        :type previous_service_names: list[str]

        :param time_created:
            The value to assign to the time_created property of this BaseService.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BaseService.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BaseService.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'service_name': 'str',
            'short_name': 'str',
            'team_name': 'str',
            'platform_type': 'str',
            'comms_manager_name': 'str',
            'excluded_realms': 'list[str]',
            'previous_service_names': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'service_name': 'serviceName',
            'short_name': 'shortName',
            'team_name': 'teamName',
            'platform_type': 'platformType',
            'comms_manager_name': 'commsManagerName',
            'excluded_realms': 'excludedRealms',
            'previous_service_names': 'previousServiceNames',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState'
        }

        self._type = None
        self._id = None
        self._service_name = None
        self._short_name = None
        self._team_name = None
        self._platform_type = None
        self._comms_manager_name = None
        self._excluded_realms = None
        self._previous_service_names = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'Service':
            return 'Service'

        if type == 'ServiceSummary':
            return 'ServiceSummary'

        if type == 'NotificationsSummary':
            return 'NotificationsSummary'
        else:
            return 'BaseService'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this BaseService.
        The discriminator property.


        :return: The type of this BaseService.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BaseService.
        The discriminator property.


        :param type: The type of this BaseService.
        :type: str
        """
        self._type = type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BaseService.
        ID of the service object.


        :return: The id of this BaseService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BaseService.
        ID of the service object.


        :param id: The id of this BaseService.
        :type: str
        """
        self._id = id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this BaseService.
        Name of the service represented by this object.


        :return: The service_name of this BaseService.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this BaseService.
        Name of the service represented by this object.


        :param service_name: The service_name of this BaseService.
        :type: str
        """
        self._service_name = service_name

    @property
    def short_name(self):
        """
        **[Required]** Gets the short_name of this BaseService.
        Short name of the team to whom this service object is related.


        :return: The short_name of this BaseService.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this BaseService.
        Short name of the team to whom this service object is related.


        :param short_name: The short_name of this BaseService.
        :type: str
        """
        self._short_name = short_name

    @property
    def team_name(self):
        """
        **[Required]** Gets the team_name of this BaseService.
        Team name to which this service object is related.


        :return: The team_name of this BaseService.
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """
        Sets the team_name of this BaseService.
        Team name to which this service object is related.


        :param team_name: The team_name of this BaseService.
        :type: str
        """
        self._team_name = team_name

    @property
    def platform_type(self):
        """
        **[Required]** Gets the platform_type of this BaseService.
        The platform type this service object is related to.

        Allowed values for this property are: "IAAS", "SAAS", "PAAS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this BaseService.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this BaseService.
        The platform type this service object is related to.


        :param platform_type: The platform_type of this BaseService.
        :type: str
        """
        allowed_values = ["IAAS", "SAAS", "PAAS"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def comms_manager_name(self):
        """
        **[Required]** Gets the comms_manager_name of this BaseService.
        Name of the comms manager team that manages Notifications to this service.

        Allowed values for this property are: "CN", "FUSION", "AS", "ERF", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The comms_manager_name of this BaseService.
        :rtype: str
        """
        return self._comms_manager_name

    @comms_manager_name.setter
    def comms_manager_name(self, comms_manager_name):
        """
        Sets the comms_manager_name of this BaseService.
        Name of the comms manager team that manages Notifications to this service.


        :param comms_manager_name: The comms_manager_name of this BaseService.
        :type: str
        """
        allowed_values = ["CN", "FUSION", "AS", "ERF"]
        if not value_allowed_none_or_none_sentinel(comms_manager_name, allowed_values):
            comms_manager_name = 'UNKNOWN_ENUM_VALUE'
        self._comms_manager_name = comms_manager_name

    @property
    def excluded_realms(self):
        """
        **[Required]** Gets the excluded_realms of this BaseService.
        The list of realms where this service is not available to be used.


        :return: The excluded_realms of this BaseService.
        :rtype: list[str]
        """
        return self._excluded_realms

    @excluded_realms.setter
    def excluded_realms(self, excluded_realms):
        """
        Sets the excluded_realms of this BaseService.
        The list of realms where this service is not available to be used.


        :param excluded_realms: The excluded_realms of this BaseService.
        :type: list[str]
        """
        self._excluded_realms = excluded_realms

    @property
    def previous_service_names(self):
        """
        **[Required]** Gets the previous_service_names of this BaseService.
        The list of previously used names for this service object.


        :return: The previous_service_names of this BaseService.
        :rtype: list[str]
        """
        return self._previous_service_names

    @previous_service_names.setter
    def previous_service_names(self, previous_service_names):
        """
        Sets the previous_service_names of this BaseService.
        The list of previously used names for this service object.


        :param previous_service_names: The previous_service_names of this BaseService.
        :type: list[str]
        """
        self._previous_service_names = previous_service_names

    @property
    def time_created(self):
        """
        Gets the time_created of this BaseService.
        The date and time when the service object was created.


        :return: The time_created of this BaseService.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BaseService.
        The date and time when the service object was created.


        :param time_created: The time_created of this BaseService.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BaseService.
        The date and time when the service object was updated.


        :return: The time_updated of this BaseService.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BaseService.
        The date and time when the service object was updated.


        :param time_updated: The time_updated of this BaseService.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BaseService.
        Current state of the service object.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BaseService.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BaseService.
        Current state of the service object.


        :param lifecycle_state: The lifecycle_state of this BaseService.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
