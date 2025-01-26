# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GroupToRolesMappingDetails(object):
    """
    Defines the IDP Groups to GoldenGate roles mapping. This field is used only for IAM deployment and does not have any impact on non-IAM deployments.
    For IAM deployment, when user does not specify this mapping, then it has null value and default mapping is used.
    User belonging to each group can only perform the actions according to the role the respective group is mapped to.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GroupToRolesMappingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param security_group_id:
            The value to assign to the security_group_id property of this GroupToRolesMappingDetails.
        :type security_group_id: str

        :param administrator_group_id:
            The value to assign to the administrator_group_id property of this GroupToRolesMappingDetails.
        :type administrator_group_id: str

        :param operator_group_id:
            The value to assign to the operator_group_id property of this GroupToRolesMappingDetails.
        :type operator_group_id: str

        :param user_group_id:
            The value to assign to the user_group_id property of this GroupToRolesMappingDetails.
        :type user_group_id: str

        """
        self.swagger_types = {
            'security_group_id': 'str',
            'administrator_group_id': 'str',
            'operator_group_id': 'str',
            'user_group_id': 'str'
        }

        self.attribute_map = {
            'security_group_id': 'securityGroupId',
            'administrator_group_id': 'administratorGroupId',
            'operator_group_id': 'operatorGroupId',
            'user_group_id': 'userGroupId'
        }

        self._security_group_id = None
        self._administrator_group_id = None
        self._operator_group_id = None
        self._user_group_id = None

    @property
    def security_group_id(self):
        """
        **[Required]** Gets the security_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role securityGroup.
        It grants administration of security related objects and invoke security related service requests. This role has full privileges.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The security_group_id of this GroupToRolesMappingDetails.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """
        Sets the security_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role securityGroup.
        It grants administration of security related objects and invoke security related service requests. This role has full privileges.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param security_group_id: The security_group_id of this GroupToRolesMappingDetails.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def administrator_group_id(self):
        """
        Gets the administrator_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role administratorGroup.
        It grants full access to the user, including the ability to alter general, non-security related operational parameters
        and profiles of the server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The administrator_group_id of this GroupToRolesMappingDetails.
        :rtype: str
        """
        return self._administrator_group_id

    @administrator_group_id.setter
    def administrator_group_id(self, administrator_group_id):
        """
        Sets the administrator_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role administratorGroup.
        It grants full access to the user, including the ability to alter general, non-security related operational parameters
        and profiles of the server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param administrator_group_id: The administrator_group_id of this GroupToRolesMappingDetails.
        :type: str
        """
        self._administrator_group_id = administrator_group_id

    @property
    def operator_group_id(self):
        """
        Gets the operator_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role operatorGroup.
        It allows users to perform only operational actions, like starting and stopping resources.
        Operators cannot alter the operational parameters or profiles of the MA server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The operator_group_id of this GroupToRolesMappingDetails.
        :rtype: str
        """
        return self._operator_group_id

    @operator_group_id.setter
    def operator_group_id(self, operator_group_id):
        """
        Sets the operator_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role operatorGroup.
        It allows users to perform only operational actions, like starting and stopping resources.
        Operators cannot alter the operational parameters or profiles of the MA server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param operator_group_id: The operator_group_id of this GroupToRolesMappingDetails.
        :type: str
        """
        self._operator_group_id = operator_group_id

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role userGroup.
        It allows information-only service requests, which do not alter or affect the operation of either the MA.
        Examples of query and read-only information include performance metric information and resource status and monitoring information

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The user_group_id of this GroupToRolesMappingDetails.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this GroupToRolesMappingDetails.
        The `OCID`__ of the IDP group which will be mapped to goldengate role userGroup.
        It allows information-only service requests, which do not alter or affect the operation of either the MA.
        Examples of query and read-only information include performance metric information and resource status and monitoring information

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param user_group_id: The user_group_id of this GroupToRolesMappingDetails.
        :type: str
        """
        self._user_group_id = user_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
