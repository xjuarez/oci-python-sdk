# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseSecurityConfigSummary(object):
    """
    Database Security Configurations resource represents the target database configurations.
    Included in the Database Security Configurations are the SQL Firewall configurations such as
    the status of the firewall, the time that the firewall status was last updated, violation log auto purge settings, etc.
    """

    #: A constant which can be used with the lifecycle_state property of a DatabaseSecurityConfigSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseSecurityConfigSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseSecurityConfigSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseSecurityConfigSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseSecurityConfigSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a DatabaseSecurityConfigSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseSecurityConfigSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseSecurityConfigSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatabaseSecurityConfigSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseSecurityConfigSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DatabaseSecurityConfigSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DatabaseSecurityConfigSummary.
        :type description: str

        :param target_id:
            The value to assign to the target_id property of this DatabaseSecurityConfigSummary.
        :type target_id: str

        :param time_created:
            The value to assign to the time_created property of this DatabaseSecurityConfigSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseSecurityConfigSummary.
        :type time_updated: datetime

        :param time_last_refreshed:
            The value to assign to the time_last_refreshed property of this DatabaseSecurityConfigSummary.
        :type time_last_refreshed: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseSecurityConfigSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "FAILED", "NEEDS_ATTENTION", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseSecurityConfigSummary.
        :type lifecycle_details: str

        :param sql_firewall_config:
            The value to assign to the sql_firewall_config property of this DatabaseSecurityConfigSummary.
        :type sql_firewall_config: oci.data_safe.models.SqlFirewallConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseSecurityConfigSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseSecurityConfigSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'target_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_refreshed': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'sql_firewall_config': 'SqlFirewallConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'target_id': 'targetId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_refreshed': 'timeLastRefreshed',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'sql_firewall_config': 'sqlFirewallConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._target_id = None
        self._time_created = None
        self._time_updated = None
        self._time_last_refreshed = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._sql_firewall_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatabaseSecurityConfigSummary.
        The OCID of the database security config.


        :return: The id of this DatabaseSecurityConfigSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseSecurityConfigSummary.
        The OCID of the database security config.


        :param id: The id of this DatabaseSecurityConfigSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DatabaseSecurityConfigSummary.
        The OCID of the compartment containing the database security config.


        :return: The compartment_id of this DatabaseSecurityConfigSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseSecurityConfigSummary.
        The OCID of the compartment containing the database security config.


        :param compartment_id: The compartment_id of this DatabaseSecurityConfigSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DatabaseSecurityConfigSummary.
        The display name of the database security config.


        :return: The display_name of this DatabaseSecurityConfigSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DatabaseSecurityConfigSummary.
        The display name of the database security config.


        :param display_name: The display_name of this DatabaseSecurityConfigSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DatabaseSecurityConfigSummary.
        The description of the database security config.


        :return: The description of this DatabaseSecurityConfigSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatabaseSecurityConfigSummary.
        The description of the database security config.


        :param description: The description of this DatabaseSecurityConfigSummary.
        :type: str
        """
        self._description = description

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this DatabaseSecurityConfigSummary.
        The target OCID corresponding to the database security config.


        :return: The target_id of this DatabaseSecurityConfigSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this DatabaseSecurityConfigSummary.
        The target OCID corresponding to the database security config.


        :param target_id: The target_id of this DatabaseSecurityConfigSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DatabaseSecurityConfigSummary.
        The time that the database security config was created, in the format defined by RFC3339.


        :return: The time_created of this DatabaseSecurityConfigSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatabaseSecurityConfigSummary.
        The time that the database security config was created, in the format defined by RFC3339.


        :param time_created: The time_created of this DatabaseSecurityConfigSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DatabaseSecurityConfigSummary.
        The date and time the database security configuration was last updated, in the format defined by RFC3339.


        :return: The time_updated of this DatabaseSecurityConfigSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DatabaseSecurityConfigSummary.
        The date and time the database security configuration was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this DatabaseSecurityConfigSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_refreshed(self):
        """
        Gets the time_last_refreshed of this DatabaseSecurityConfigSummary.
        The last date and time the database security config was refreshed, in the format defined by RFC3339.


        :return: The time_last_refreshed of this DatabaseSecurityConfigSummary.
        :rtype: datetime
        """
        return self._time_last_refreshed

    @time_last_refreshed.setter
    def time_last_refreshed(self, time_last_refreshed):
        """
        Sets the time_last_refreshed of this DatabaseSecurityConfigSummary.
        The last date and time the database security config was refreshed, in the format defined by RFC3339.


        :param time_last_refreshed: The time_last_refreshed of this DatabaseSecurityConfigSummary.
        :type: datetime
        """
        self._time_last_refreshed = time_last_refreshed

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DatabaseSecurityConfigSummary.
        The current state of the database security config.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "FAILED", "NEEDS_ATTENTION", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseSecurityConfigSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseSecurityConfigSummary.
        The current state of the database security config.


        :param lifecycle_state: The lifecycle_state of this DatabaseSecurityConfigSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "FAILED", "NEEDS_ATTENTION", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseSecurityConfigSummary.
        Details about the current state of the database security config in Data Safe.


        :return: The lifecycle_details of this DatabaseSecurityConfigSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseSecurityConfigSummary.
        Details about the current state of the database security config in Data Safe.


        :param lifecycle_details: The lifecycle_details of this DatabaseSecurityConfigSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def sql_firewall_config(self):
        """
        Gets the sql_firewall_config of this DatabaseSecurityConfigSummary.

        :return: The sql_firewall_config of this DatabaseSecurityConfigSummary.
        :rtype: oci.data_safe.models.SqlFirewallConfig
        """
        return self._sql_firewall_config

    @sql_firewall_config.setter
    def sql_firewall_config(self, sql_firewall_config):
        """
        Sets the sql_firewall_config of this DatabaseSecurityConfigSummary.

        :param sql_firewall_config: The sql_firewall_config of this DatabaseSecurityConfigSummary.
        :type: oci.data_safe.models.SqlFirewallConfig
        """
        self._sql_firewall_config = sql_firewall_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DatabaseSecurityConfigSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DatabaseSecurityConfigSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseSecurityConfigSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DatabaseSecurityConfigSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DatabaseSecurityConfigSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DatabaseSecurityConfigSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseSecurityConfigSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DatabaseSecurityConfigSummary.
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
