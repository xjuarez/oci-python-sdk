# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchSummary(object):
    """
    Summary of the Patch.
    """

    #: A constant which can be used with the severity property of a PatchSummary.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a PatchSummary.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a PatchSummary.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a PatchSummary.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PatchSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this PatchSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this PatchSummary.
        :type description: str

        :param type:
            The value to assign to the type property of this PatchSummary.
        :type type: str

        :param patch_type:
            The value to assign to the patch_type property of this PatchSummary.
        :type patch_type: oci.fleet_apps_management.models.PatchType

        :param severity:
            The value to assign to the severity property of this PatchSummary.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param time_released:
            The value to assign to the time_released property of this PatchSummary.
        :type time_released: datetime

        :param artifact_details:
            The value to assign to the artifact_details property of this PatchSummary.
        :type artifact_details: oci.fleet_apps_management.models.ArtifactDetails

        :param product:
            The value to assign to the product property of this PatchSummary.
        :type product: oci.fleet_apps_management.models.PatchProduct

        :param compartment_id:
            The value to assign to the compartment_id property of this PatchSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PatchSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PatchSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this PatchSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PatchSummary.
        :type time_updated: datetime

        :param resource_region:
            The value to assign to the resource_region property of this PatchSummary.
        :type resource_region: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PatchSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PatchSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PatchSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'patch_type': 'PatchType',
            'severity': 'str',
            'time_released': 'datetime',
            'artifact_details': 'ArtifactDetails',
            'product': 'PatchProduct',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'resource_region': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'patch_type': 'patchType',
            'severity': 'severity',
            'time_released': 'timeReleased',
            'artifact_details': 'artifactDetails',
            'product': 'product',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'resource_region': 'resourceRegion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._patch_type = None
        self._severity = None
        self._time_released = None
        self._artifact_details = None
        self._product = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._resource_region = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PatchSummary.
        The OCID of the resource.


        :return: The id of this PatchSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PatchSummary.
        The OCID of the resource.


        :param id: The id of this PatchSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PatchSummary.
        A user-friendly name. Should be unique within the tenancy, and cannot be changed after creation.
        Avoid entering confidential information.


        :return: The name of this PatchSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PatchSummary.
        A user-friendly name. Should be unique within the tenancy, and cannot be changed after creation.
        Avoid entering confidential information.


        :param name: The name of this PatchSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PatchSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this PatchSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PatchSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this PatchSummary.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        Gets the type of this PatchSummary.
        Provide information on who defined the patch.
        Example: For Custom Patches the value will be USER_DEFINED
        For Oracle Defined Patches the value will be ORACLE_DEFINED


        :return: The type of this PatchSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PatchSummary.
        Provide information on who defined the patch.
        Example: For Custom Patches the value will be USER_DEFINED
        For Oracle Defined Patches the value will be ORACLE_DEFINED


        :param type: The type of this PatchSummary.
        :type: str
        """
        self._type = type

    @property
    def patch_type(self):
        """
        **[Required]** Gets the patch_type of this PatchSummary.

        :return: The patch_type of this PatchSummary.
        :rtype: oci.fleet_apps_management.models.PatchType
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """
        Sets the patch_type of this PatchSummary.

        :param patch_type: The patch_type of this PatchSummary.
        :type: oci.fleet_apps_management.models.PatchType
        """
        self._patch_type = patch_type

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this PatchSummary.
        Patch Severity.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this PatchSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this PatchSummary.
        Patch Severity.


        :param severity: The severity of this PatchSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def time_released(self):
        """
        **[Required]** Gets the time_released of this PatchSummary.
        Date when the patch was released.


        :return: The time_released of this PatchSummary.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this PatchSummary.
        Date when the patch was released.


        :param time_released: The time_released of this PatchSummary.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def artifact_details(self):
        """
        Gets the artifact_details of this PatchSummary.

        :return: The artifact_details of this PatchSummary.
        :rtype: oci.fleet_apps_management.models.ArtifactDetails
        """
        return self._artifact_details

    @artifact_details.setter
    def artifact_details(self, artifact_details):
        """
        Sets the artifact_details of this PatchSummary.

        :param artifact_details: The artifact_details of this PatchSummary.
        :type: oci.fleet_apps_management.models.ArtifactDetails
        """
        self._artifact_details = artifact_details

    @property
    def product(self):
        """
        **[Required]** Gets the product of this PatchSummary.

        :return: The product of this PatchSummary.
        :rtype: oci.fleet_apps_management.models.PatchProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this PatchSummary.

        :param product: The product of this PatchSummary.
        :type: oci.fleet_apps_management.models.PatchProduct
        """
        self._product = product

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PatchSummary.
        OCID of the compartment to which the resource belongs to.


        :return: The compartment_id of this PatchSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PatchSummary.
        OCID of the compartment to which the resource belongs to.


        :param compartment_id: The compartment_id of this PatchSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PatchSummary.
        The current state of the Patch.


        :return: The lifecycle_state of this PatchSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PatchSummary.
        The current state of the Patch.


        :param lifecycle_state: The lifecycle_state of this PatchSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PatchSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this PatchSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PatchSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this PatchSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PatchSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this PatchSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PatchSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this PatchSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PatchSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this PatchSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PatchSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this PatchSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def resource_region(self):
        """
        Gets the resource_region of this PatchSummary.
        Associated region


        :return: The resource_region of this PatchSummary.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this PatchSummary.
        Associated region


        :param resource_region: The resource_region of this PatchSummary.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PatchSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PatchSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PatchSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PatchSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PatchSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PatchSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PatchSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PatchSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this PatchSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this PatchSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this PatchSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this PatchSummary.
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
