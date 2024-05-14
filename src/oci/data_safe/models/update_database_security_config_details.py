# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDatabaseSecurityConfigDetails(object):
    """
    The details to update the database security config.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDatabaseSecurityConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDatabaseSecurityConfigDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDatabaseSecurityConfigDetails.
        :type description: str

        :param sql_firewall_config:
            The value to assign to the sql_firewall_config property of this UpdateDatabaseSecurityConfigDetails.
        :type sql_firewall_config: oci.data_safe.models.UpdateSqlFirewallConfigDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDatabaseSecurityConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDatabaseSecurityConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'sql_firewall_config': 'UpdateSqlFirewallConfigDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'sql_firewall_config': 'sqlFirewallConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._sql_firewall_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDatabaseSecurityConfigDetails.
        The display name of the database security config. The name does not have to be unique, and it is changeable.


        :return: The display_name of this UpdateDatabaseSecurityConfigDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDatabaseSecurityConfigDetails.
        The display name of the database security config. The name does not have to be unique, and it is changeable.


        :param display_name: The display_name of this UpdateDatabaseSecurityConfigDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateDatabaseSecurityConfigDetails.
        The description of the security policy.


        :return: The description of this UpdateDatabaseSecurityConfigDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDatabaseSecurityConfigDetails.
        The description of the security policy.


        :param description: The description of this UpdateDatabaseSecurityConfigDetails.
        :type: str
        """
        self._description = description

    @property
    def sql_firewall_config(self):
        """
        Gets the sql_firewall_config of this UpdateDatabaseSecurityConfigDetails.

        :return: The sql_firewall_config of this UpdateDatabaseSecurityConfigDetails.
        :rtype: oci.data_safe.models.UpdateSqlFirewallConfigDetails
        """
        return self._sql_firewall_config

    @sql_firewall_config.setter
    def sql_firewall_config(self, sql_firewall_config):
        """
        Sets the sql_firewall_config of this UpdateDatabaseSecurityConfigDetails.

        :param sql_firewall_config: The sql_firewall_config of this UpdateDatabaseSecurityConfigDetails.
        :type: oci.data_safe.models.UpdateSqlFirewallConfigDetails
        """
        self._sql_firewall_config = sql_firewall_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDatabaseSecurityConfigDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDatabaseSecurityConfigDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDatabaseSecurityConfigDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDatabaseSecurityConfigDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDatabaseSecurityConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDatabaseSecurityConfigDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDatabaseSecurityConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDatabaseSecurityConfigDetails.
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
