# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FsuGoalVersionDetails(object):
    """
    Goal version or image details for the Exadata Fleet Update Cycle.
    """

    #: A constant which can be used with the type property of a FsuGoalVersionDetails.
    #: This constant has a value of "VERSION"
    TYPE_VERSION = "VERSION"

    #: A constant which can be used with the type property of a FsuGoalVersionDetails.
    #: This constant has a value of "IMAGE_ID"
    TYPE_IMAGE_ID = "IMAGE_ID"

    #: A constant which can be used with the home_policy property of a FsuGoalVersionDetails.
    #: This constant has a value of "CREATE_NEW"
    HOME_POLICY_CREATE_NEW = "CREATE_NEW"

    #: A constant which can be used with the home_policy property of a FsuGoalVersionDetails.
    #: This constant has a value of "USE_EXISTING"
    HOME_POLICY_USE_EXISTING = "USE_EXISTING"

    def __init__(self, **kwargs):
        """
        Initializes a new FsuGoalVersionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.VersionFsuTargetDetails`
        * :class:`~oci.fleet_software_update.models.ImageIdFsuTargetDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FsuGoalVersionDetails.
            Allowed values for this property are: "VERSION", "IMAGE_ID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param home_policy:
            The value to assign to the home_policy property of this FsuGoalVersionDetails.
            Allowed values for this property are: "CREATE_NEW", "USE_EXISTING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type home_policy: str

        :param new_home_prefix:
            The value to assign to the new_home_prefix property of this FsuGoalVersionDetails.
        :type new_home_prefix: str

        """
        self.swagger_types = {
            'type': 'str',
            'home_policy': 'str',
            'new_home_prefix': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'home_policy': 'homePolicy',
            'new_home_prefix': 'newHomePrefix'
        }

        self._type = None
        self._home_policy = None
        self._new_home_prefix = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VERSION':
            return 'VersionFsuTargetDetails'

        if type == 'IMAGE_ID':
            return 'ImageIdFsuTargetDetails'
        else:
            return 'FsuGoalVersionDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this FsuGoalVersionDetails.
        Type of goal target version specified

        Allowed values for this property are: "VERSION", "IMAGE_ID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this FsuGoalVersionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FsuGoalVersionDetails.
        Type of goal target version specified


        :param type: The type of this FsuGoalVersionDetails.
        :type: str
        """
        allowed_values = ["VERSION", "IMAGE_ID"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def home_policy(self):
        """
        Gets the home_policy of this FsuGoalVersionDetails.
        Goal home policy to use when Staging the Goal Version during patching.
        CREATE_NEW: Create a new DBHome (for Database Collections) for the specified image or version.
        USE_EXISTING: All database targets in the same VMCluster or CloudVmCluster will be moved to a shared database home.
          If an existing home for the selected image or version is not found in the VM Cluster for a target database, then a new home will be created.
          If more than one existing home for the selected image is found, then the home with the least number of databases will be used.
          If multiple homes have the least number of databases, then a home will be selected at random.

        Allowed values for this property are: "CREATE_NEW", "USE_EXISTING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The home_policy of this FsuGoalVersionDetails.
        :rtype: str
        """
        return self._home_policy

    @home_policy.setter
    def home_policy(self, home_policy):
        """
        Sets the home_policy of this FsuGoalVersionDetails.
        Goal home policy to use when Staging the Goal Version during patching.
        CREATE_NEW: Create a new DBHome (for Database Collections) for the specified image or version.
        USE_EXISTING: All database targets in the same VMCluster or CloudVmCluster will be moved to a shared database home.
          If an existing home for the selected image or version is not found in the VM Cluster for a target database, then a new home will be created.
          If more than one existing home for the selected image is found, then the home with the least number of databases will be used.
          If multiple homes have the least number of databases, then a home will be selected at random.


        :param home_policy: The home_policy of this FsuGoalVersionDetails.
        :type: str
        """
        allowed_values = ["CREATE_NEW", "USE_EXISTING"]
        if not value_allowed_none_or_none_sentinel(home_policy, allowed_values):
            home_policy = 'UNKNOWN_ENUM_VALUE'
        self._home_policy = home_policy

    @property
    def new_home_prefix(self):
        """
        Gets the new_home_prefix of this FsuGoalVersionDetails.
        Prefix name used for new DB home resources created as part of the Stage Action.
        Format: <specified_prefix>_<timestamp>
        If not specified, a default OCI DB home resource will be generated for the new DB home resources created.


        :return: The new_home_prefix of this FsuGoalVersionDetails.
        :rtype: str
        """
        return self._new_home_prefix

    @new_home_prefix.setter
    def new_home_prefix(self, new_home_prefix):
        """
        Sets the new_home_prefix of this FsuGoalVersionDetails.
        Prefix name used for new DB home resources created as part of the Stage Action.
        Format: <specified_prefix>_<timestamp>
        If not specified, a default OCI DB home resource will be generated for the new DB home resources created.


        :param new_home_prefix: The new_home_prefix of this FsuGoalVersionDetails.
        :type: str
        """
        self._new_home_prefix = new_home_prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
