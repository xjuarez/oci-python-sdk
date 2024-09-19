# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MoveExecutionActionMemberDetails(object):
    """
    Request to move an execution action member to an execution action resource from another.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MoveExecutionActionMemberDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_execution_action_id:
            The value to assign to the source_execution_action_id property of this MoveExecutionActionMemberDetails.
        :type source_execution_action_id: str

        :param execution_action_member_id:
            The value to assign to the execution_action_member_id property of this MoveExecutionActionMemberDetails.
        :type execution_action_member_id: str

        :param execution_action_member_count:
            The value to assign to the execution_action_member_count property of this MoveExecutionActionMemberDetails.
        :type execution_action_member_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MoveExecutionActionMemberDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MoveExecutionActionMemberDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'source_execution_action_id': 'str',
            'execution_action_member_id': 'str',
            'execution_action_member_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'source_execution_action_id': 'sourceExecutionActionId',
            'execution_action_member_id': 'executionActionMemberId',
            'execution_action_member_count': 'executionActionMemberCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._source_execution_action_id = None
        self._execution_action_member_id = None
        self._execution_action_member_count = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def source_execution_action_id(self):
        """
        Gets the source_execution_action_id of this MoveExecutionActionMemberDetails.
        The `OCID`__ of the source execution action resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_execution_action_id of this MoveExecutionActionMemberDetails.
        :rtype: str
        """
        return self._source_execution_action_id

    @source_execution_action_id.setter
    def source_execution_action_id(self, source_execution_action_id):
        """
        Sets the source_execution_action_id of this MoveExecutionActionMemberDetails.
        The `OCID`__ of the source execution action resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_execution_action_id: The source_execution_action_id of this MoveExecutionActionMemberDetails.
        :type: str
        """
        self._source_execution_action_id = source_execution_action_id

    @property
    def execution_action_member_id(self):
        """
        Gets the execution_action_member_id of this MoveExecutionActionMemberDetails.
        The `OCID`__ of the execution action member to be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The execution_action_member_id of this MoveExecutionActionMemberDetails.
        :rtype: str
        """
        return self._execution_action_member_id

    @execution_action_member_id.setter
    def execution_action_member_id(self, execution_action_member_id):
        """
        Sets the execution_action_member_id of this MoveExecutionActionMemberDetails.
        The `OCID`__ of the execution action member to be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param execution_action_member_id: The execution_action_member_id of this MoveExecutionActionMemberDetails.
        :type: str
        """
        self._execution_action_member_id = execution_action_member_id

    @property
    def execution_action_member_count(self):
        """
        Gets the execution_action_member_count of this MoveExecutionActionMemberDetails.
        The number of execution action member without ocids to be moved.


        :return: The execution_action_member_count of this MoveExecutionActionMemberDetails.
        :rtype: int
        """
        return self._execution_action_member_count

    @execution_action_member_count.setter
    def execution_action_member_count(self, execution_action_member_count):
        """
        Sets the execution_action_member_count of this MoveExecutionActionMemberDetails.
        The number of execution action member without ocids to be moved.


        :param execution_action_member_count: The execution_action_member_count of this MoveExecutionActionMemberDetails.
        :type: int
        """
        self._execution_action_member_count = execution_action_member_count

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MoveExecutionActionMemberDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this MoveExecutionActionMemberDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MoveExecutionActionMemberDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this MoveExecutionActionMemberDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MoveExecutionActionMemberDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this MoveExecutionActionMemberDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MoveExecutionActionMemberDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this MoveExecutionActionMemberDetails.
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