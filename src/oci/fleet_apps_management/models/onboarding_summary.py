# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OnboardingSummary(object):
    """
    Summary of the FleetAppManagementService Onboarding.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OnboardingSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OnboardingSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OnboardingSummary.
        :type compartment_id: str

        :param resource_region:
            The value to assign to the resource_region property of this OnboardingSummary.
        :type resource_region: str

        :param time_created:
            The value to assign to the time_created property of this OnboardingSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OnboardingSummary.
        :type time_updated: datetime

        :param is_fams_tag_enabled:
            The value to assign to the is_fams_tag_enabled property of this OnboardingSummary.
        :type is_fams_tag_enabled: bool

        :param version:
            The value to assign to the version property of this OnboardingSummary.
        :type version: str

        :param is_cost_tracking_tag_enabled:
            The value to assign to the is_cost_tracking_tag_enabled property of this OnboardingSummary.
        :type is_cost_tracking_tag_enabled: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OnboardingSummary.
        :type lifecycle_state: str

        :param system_tags:
            The value to assign to the system_tags property of this OnboardingSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'resource_region': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'is_fams_tag_enabled': 'bool',
            'version': 'str',
            'is_cost_tracking_tag_enabled': 'bool',
            'lifecycle_state': 'str',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'resource_region': 'resourceRegion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'is_fams_tag_enabled': 'isFamsTagEnabled',
            'version': 'version',
            'is_cost_tracking_tag_enabled': 'isCostTrackingTagEnabled',
            'lifecycle_state': 'lifecycleState',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._resource_region = None
        self._time_created = None
        self._time_updated = None
        self._is_fams_tag_enabled = None
        self._version = None
        self._is_cost_tracking_tag_enabled = None
        self._lifecycle_state = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OnboardingSummary.
        The unique id of the resource.


        :return: The id of this OnboardingSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OnboardingSummary.
        The unique id of the resource.


        :param id: The id of this OnboardingSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OnboardingSummary.
        Tenancy OCID


        :return: The compartment_id of this OnboardingSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OnboardingSummary.
        Tenancy OCID


        :param compartment_id: The compartment_id of this OnboardingSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_region(self):
        """
        Gets the resource_region of this OnboardingSummary.
        Associated region


        :return: The resource_region of this OnboardingSummary.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this OnboardingSummary.
        Associated region


        :param resource_region: The resource_region of this OnboardingSummary.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def time_created(self):
        """
        Gets the time_created of this OnboardingSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this OnboardingSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OnboardingSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this OnboardingSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OnboardingSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this OnboardingSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OnboardingSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this OnboardingSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def is_fams_tag_enabled(self):
        """
        Gets the is_fams_tag_enabled of this OnboardingSummary.
        A value determining FAMS tag is enabled or not


        :return: The is_fams_tag_enabled of this OnboardingSummary.
        :rtype: bool
        """
        return self._is_fams_tag_enabled

    @is_fams_tag_enabled.setter
    def is_fams_tag_enabled(self, is_fams_tag_enabled):
        """
        Sets the is_fams_tag_enabled of this OnboardingSummary.
        A value determining FAMS tag is enabled or not


        :param is_fams_tag_enabled: The is_fams_tag_enabled of this OnboardingSummary.
        :type: bool
        """
        self._is_fams_tag_enabled = is_fams_tag_enabled

    @property
    def version(self):
        """
        Gets the version of this OnboardingSummary.
        Version of FAMS the tenant is onboarded to.


        :return: The version of this OnboardingSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this OnboardingSummary.
        Version of FAMS the tenant is onboarded to.


        :param version: The version of this OnboardingSummary.
        :type: str
        """
        self._version = version

    @property
    def is_cost_tracking_tag_enabled(self):
        """
        Gets the is_cost_tracking_tag_enabled of this OnboardingSummary.
        A value determining if cost tracking tag is enabled or not


        :return: The is_cost_tracking_tag_enabled of this OnboardingSummary.
        :rtype: bool
        """
        return self._is_cost_tracking_tag_enabled

    @is_cost_tracking_tag_enabled.setter
    def is_cost_tracking_tag_enabled(self, is_cost_tracking_tag_enabled):
        """
        Sets the is_cost_tracking_tag_enabled of this OnboardingSummary.
        A value determining if cost tracking tag is enabled or not


        :param is_cost_tracking_tag_enabled: The is_cost_tracking_tag_enabled of this OnboardingSummary.
        :type: bool
        """
        self._is_cost_tracking_tag_enabled = is_cost_tracking_tag_enabled

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OnboardingSummary.
        The current state of the Onboarding.


        :return: The lifecycle_state of this OnboardingSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OnboardingSummary.
        The current state of the Onboarding.


        :param lifecycle_state: The lifecycle_state of this OnboardingSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OnboardingSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OnboardingSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OnboardingSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OnboardingSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other