# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteProtectedBranchDetails(object):
    """
    Information to delete a protected branch
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteProtectedBranchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param branch_name:
            The value to assign to the branch_name property of this DeleteProtectedBranchDetails.
        :type branch_name: str

        """
        self.swagger_types = {
            'branch_name': 'str'
        }

        self.attribute_map = {
            'branch_name': 'branchName'
        }

        self._branch_name = None

    @property
    def branch_name(self):
        """
        **[Required]** Gets the branch_name of this DeleteProtectedBranchDetails.
        Name of a protected branch.


        :return: The branch_name of this DeleteProtectedBranchDetails.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """
        Sets the branch_name of this DeleteProtectedBranchDetails.
        Name of a protected branch.


        :param branch_name: The branch_name of this DeleteProtectedBranchDetails.
        :type: str
        """
        self._branch_name = branch_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
