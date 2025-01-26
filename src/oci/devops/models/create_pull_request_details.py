# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePullRequestDetails(object):
    """
    The information about new Pull Request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePullRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreatePullRequestDetails.
        :type display_name: str

        :param source_branch:
            The value to assign to the source_branch property of this CreatePullRequestDetails.
        :type source_branch: str

        :param destination_branch:
            The value to assign to the destination_branch property of this CreatePullRequestDetails.
        :type destination_branch: str

        :param repository_id:
            The value to assign to the repository_id property of this CreatePullRequestDetails.
        :type repository_id: str

        :param source_repository_id:
            The value to assign to the source_repository_id property of this CreatePullRequestDetails.
        :type source_repository_id: str

        :param description:
            The value to assign to the description property of this CreatePullRequestDetails.
        :type description: str

        :param reviewers:
            The value to assign to the reviewers property of this CreatePullRequestDetails.
        :type reviewers: list[oci.devops.models.CreateReviewerDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePullRequestDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePullRequestDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'source_branch': 'str',
            'destination_branch': 'str',
            'repository_id': 'str',
            'source_repository_id': 'str',
            'description': 'str',
            'reviewers': 'list[CreateReviewerDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'source_branch': 'sourceBranch',
            'destination_branch': 'destinationBranch',
            'repository_id': 'repositoryId',
            'source_repository_id': 'sourceRepositoryId',
            'description': 'description',
            'reviewers': 'reviewers',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._source_branch = None
        self._destination_branch = None
        self._repository_id = None
        self._source_repository_id = None
        self._description = None
        self._reviewers = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreatePullRequestDetails.
        Pull Request title


        :return: The display_name of this CreatePullRequestDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePullRequestDetails.
        Pull Request title


        :param display_name: The display_name of this CreatePullRequestDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def source_branch(self):
        """
        **[Required]** Gets the source_branch of this CreatePullRequestDetails.
        The source branch of the pull request.


        :return: The source_branch of this CreatePullRequestDetails.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        """
        Sets the source_branch of this CreatePullRequestDetails.
        The source branch of the pull request.


        :param source_branch: The source_branch of this CreatePullRequestDetails.
        :type: str
        """
        self._source_branch = source_branch

    @property
    def destination_branch(self):
        """
        Gets the destination_branch of this CreatePullRequestDetails.
        The destination branch of the pull request. If not provided, default branch will be used as the destination branch.


        :return: The destination_branch of this CreatePullRequestDetails.
        :rtype: str
        """
        return self._destination_branch

    @destination_branch.setter
    def destination_branch(self, destination_branch):
        """
        Sets the destination_branch of this CreatePullRequestDetails.
        The destination branch of the pull request. If not provided, default branch will be used as the destination branch.


        :param destination_branch: The destination_branch of this CreatePullRequestDetails.
        :type: str
        """
        self._destination_branch = destination_branch

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this CreatePullRequestDetails.
        The OCID of the repository.


        :return: The repository_id of this CreatePullRequestDetails.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this CreatePullRequestDetails.
        The OCID of the repository.


        :param repository_id: The repository_id of this CreatePullRequestDetails.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def source_repository_id(self):
        """
        Gets the source_repository_id of this CreatePullRequestDetails.
        The OCID of the forked repository that will act as the source of the changes to be included in the pull request against the parent repository.


        :return: The source_repository_id of this CreatePullRequestDetails.
        :rtype: str
        """
        return self._source_repository_id

    @source_repository_id.setter
    def source_repository_id(self, source_repository_id):
        """
        Sets the source_repository_id of this CreatePullRequestDetails.
        The OCID of the forked repository that will act as the source of the changes to be included in the pull request against the parent repository.


        :param source_repository_id: The source_repository_id of this CreatePullRequestDetails.
        :type: str
        """
        self._source_repository_id = source_repository_id

    @property
    def description(self):
        """
        Gets the description of this CreatePullRequestDetails.
        Details of the pull request. Avoid entering confidential information.


        :return: The description of this CreatePullRequestDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePullRequestDetails.
        Details of the pull request. Avoid entering confidential information.


        :param description: The description of this CreatePullRequestDetails.
        :type: str
        """
        self._description = description

    @property
    def reviewers(self):
        """
        Gets the reviewers of this CreatePullRequestDetails.
        Reviewers for this pull request.


        :return: The reviewers of this CreatePullRequestDetails.
        :rtype: list[oci.devops.models.CreateReviewerDetails]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        """
        Sets the reviewers of this CreatePullRequestDetails.
        Reviewers for this pull request.


        :param reviewers: The reviewers of this CreatePullRequestDetails.
        :type: list[oci.devops.models.CreateReviewerDetails]
        """
        self._reviewers = reviewers

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePullRequestDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreatePullRequestDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePullRequestDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreatePullRequestDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePullRequestDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreatePullRequestDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePullRequestDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreatePullRequestDetails.
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
