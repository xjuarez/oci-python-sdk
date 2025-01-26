# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLifecycleEnvironmentDetails(object):
    """
    Provides the information used to create a lifecycle environment. A lifecycle environment is a user-defined pipeline to deliver curated, versioned content in a prescribed, methodical manner.
    """

    #: A constant which can be used with the arch_type property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "ORACLE_LINUX_6"
    OS_FAMILY_ORACLE_LINUX_6 = "ORACLE_LINUX_6"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "WINDOWS_SERVER_2016"
    OS_FAMILY_WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "WINDOWS_SERVER_2019"
    OS_FAMILY_WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "WINDOWS_SERVER_2022"
    OS_FAMILY_WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"

    #: A constant which can be used with the os_family property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    #: A constant which can be used with the vendor_name property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    #: A constant which can be used with the vendor_name property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "MICROSOFT"
    VENDOR_NAME_MICROSOFT = "MICROSOFT"

    #: A constant which can be used with the location property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "ON_PREMISE"
    LOCATION_ON_PREMISE = "ON_PREMISE"

    #: A constant which can be used with the location property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "OCI_COMPUTE"
    LOCATION_OCI_COMPUTE = "OCI_COMPUTE"

    #: A constant which can be used with the location property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "AZURE"
    LOCATION_AZURE = "AZURE"

    #: A constant which can be used with the location property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "EC2"
    LOCATION_EC2 = "EC2"

    #: A constant which can be used with the location property of a CreateLifecycleEnvironmentDetails.
    #: This constant has a value of "GCP"
    LOCATION_GCP = "GCP"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLifecycleEnvironmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateLifecycleEnvironmentDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateLifecycleEnvironmentDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateLifecycleEnvironmentDetails.
        :type description: str

        :param stages:
            The value to assign to the stages property of this CreateLifecycleEnvironmentDetails.
        :type stages: list[oci.os_management_hub.models.CreateLifecycleStageDetails]

        :param arch_type:
            The value to assign to the arch_type property of this CreateLifecycleEnvironmentDetails.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"
        :type arch_type: str

        :param os_family:
            The value to assign to the os_family property of this CreateLifecycleEnvironmentDetails.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"
        :type os_family: str

        :param vendor_name:
            The value to assign to the vendor_name property of this CreateLifecycleEnvironmentDetails.
            Allowed values for this property are: "ORACLE", "MICROSOFT"
        :type vendor_name: str

        :param location:
            The value to assign to the location property of this CreateLifecycleEnvironmentDetails.
            Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"
        :type location: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateLifecycleEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateLifecycleEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'stages': 'list[CreateLifecycleStageDetails]',
            'arch_type': 'str',
            'os_family': 'str',
            'vendor_name': 'str',
            'location': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'stages': 'stages',
            'arch_type': 'archType',
            'os_family': 'osFamily',
            'vendor_name': 'vendorName',
            'location': 'location',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._stages = None
        self._arch_type = None
        self._os_family = None
        self._vendor_name = None
        self._location = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateLifecycleEnvironmentDetails.
        The `OCID`__ of the compartment that contains the lifecycle environment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateLifecycleEnvironmentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateLifecycleEnvironmentDetails.
        The `OCID`__ of the compartment that contains the lifecycle environment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateLifecycleEnvironmentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateLifecycleEnvironmentDetails.
        A user-friendly name for the lifecycle environment. Does not have to be unique and you can change the name later. Avoid entering confidential information.


        :return: The display_name of this CreateLifecycleEnvironmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateLifecycleEnvironmentDetails.
        A user-friendly name for the lifecycle environment. Does not have to be unique and you can change the name later. Avoid entering confidential information.


        :param display_name: The display_name of this CreateLifecycleEnvironmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateLifecycleEnvironmentDetails.
        User-specified information about the lifecycle environment. Avoid entering confidential information.


        :return: The description of this CreateLifecycleEnvironmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateLifecycleEnvironmentDetails.
        User-specified information about the lifecycle environment. Avoid entering confidential information.


        :param description: The description of this CreateLifecycleEnvironmentDetails.
        :type: str
        """
        self._description = description

    @property
    def stages(self):
        """
        **[Required]** Gets the stages of this CreateLifecycleEnvironmentDetails.
        User-specified list of ranked lifecycle stages used within the lifecycle environment.


        :return: The stages of this CreateLifecycleEnvironmentDetails.
        :rtype: list[oci.os_management_hub.models.CreateLifecycleStageDetails]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this CreateLifecycleEnvironmentDetails.
        User-specified list of ranked lifecycle stages used within the lifecycle environment.


        :param stages: The stages of this CreateLifecycleEnvironmentDetails.
        :type: list[oci.os_management_hub.models.CreateLifecycleStageDetails]
        """
        self._stages = stages

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this CreateLifecycleEnvironmentDetails.
        The CPU architecture of the managed instances in the lifecycle environment.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"


        :return: The arch_type of this CreateLifecycleEnvironmentDetails.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this CreateLifecycleEnvironmentDetails.
        The CPU architecture of the managed instances in the lifecycle environment.


        :param arch_type: The arch_type of this CreateLifecycleEnvironmentDetails.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            raise ValueError(
                f"Invalid value for `arch_type`, must be None or one of {allowed_values}"
            )
        self._arch_type = arch_type

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this CreateLifecycleEnvironmentDetails.
        The operating system of the managed instances in the lifecycle environment.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"


        :return: The os_family of this CreateLifecycleEnvironmentDetails.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this CreateLifecycleEnvironmentDetails.
        The operating system of the managed instances in the lifecycle environment.


        :param os_family: The os_family of this CreateLifecycleEnvironmentDetails.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            raise ValueError(
                f"Invalid value for `os_family`, must be None or one of {allowed_values}"
            )
        self._os_family = os_family

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this CreateLifecycleEnvironmentDetails.
        The vendor of the operating system used by the managed instances in the lifecycle environment.

        Allowed values for this property are: "ORACLE", "MICROSOFT"


        :return: The vendor_name of this CreateLifecycleEnvironmentDetails.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this CreateLifecycleEnvironmentDetails.
        The vendor of the operating system used by the managed instances in the lifecycle environment.


        :param vendor_name: The vendor_name of this CreateLifecycleEnvironmentDetails.
        :type: str
        """
        allowed_values = ["ORACLE", "MICROSOFT"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            raise ValueError(
                f"Invalid value for `vendor_name`, must be None or one of {allowed_values}"
            )
        self._vendor_name = vendor_name

    @property
    def location(self):
        """
        Gets the location of this CreateLifecycleEnvironmentDetails.
        The location of managed instances attached to the lifecycle environment. If no location is provided, the default is 'ON_PREMISE.'

        Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"


        :return: The location of this CreateLifecycleEnvironmentDetails.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this CreateLifecycleEnvironmentDetails.
        The location of managed instances attached to the lifecycle environment. If no location is provided, the default is 'ON_PREMISE.'


        :param location: The location of this CreateLifecycleEnvironmentDetails.
        :type: str
        """
        allowed_values = ["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]
        if not value_allowed_none_or_none_sentinel(location, allowed_values):
            raise ValueError(
                f"Invalid value for `location`, must be None or one of {allowed_values}"
            )
        self._location = location

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateLifecycleEnvironmentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateLifecycleEnvironmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateLifecycleEnvironmentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateLifecycleEnvironmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateLifecycleEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateLifecycleEnvironmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateLifecycleEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateLifecycleEnvironmentDetails.
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
