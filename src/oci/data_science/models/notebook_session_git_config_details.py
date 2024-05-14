# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotebookSessionGitConfigDetails(object):
    """
    Git configuration Details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NotebookSessionGitConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param notebook_session_git_repo_config_collection:
            The value to assign to the notebook_session_git_repo_config_collection property of this NotebookSessionGitConfigDetails.
        :type notebook_session_git_repo_config_collection: list[oci.data_science.models.NotebookSessionGitRepoConfigDetails]

        """
        self.swagger_types = {
            'notebook_session_git_repo_config_collection': 'list[NotebookSessionGitRepoConfigDetails]'
        }

        self.attribute_map = {
            'notebook_session_git_repo_config_collection': 'notebookSessionGitRepoConfigCollection'
        }

        self._notebook_session_git_repo_config_collection = None

    @property
    def notebook_session_git_repo_config_collection(self):
        """
        Gets the notebook_session_git_repo_config_collection of this NotebookSessionGitConfigDetails.
        A collection of Git repository configurations.


        :return: The notebook_session_git_repo_config_collection of this NotebookSessionGitConfigDetails.
        :rtype: list[oci.data_science.models.NotebookSessionGitRepoConfigDetails]
        """
        return self._notebook_session_git_repo_config_collection

    @notebook_session_git_repo_config_collection.setter
    def notebook_session_git_repo_config_collection(self, notebook_session_git_repo_config_collection):
        """
        Sets the notebook_session_git_repo_config_collection of this NotebookSessionGitConfigDetails.
        A collection of Git repository configurations.


        :param notebook_session_git_repo_config_collection: The notebook_session_git_repo_config_collection of this NotebookSessionGitConfigDetails.
        :type: list[oci.data_science.models.NotebookSessionGitRepoConfigDetails]
        """
        self._notebook_session_git_repo_config_collection = notebook_session_git_repo_config_collection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
