# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_config_source_details import CreateConfigSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBitbucketServerConfigSourceDetails(CreateConfigSourceDetails):
    """
    Creation details for a Bitbucket Server configuration source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBitbucketServerConfigSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateBitbucketServerConfigSourceDetails.config_source_type` attribute
        of this class is ``BITBUCKET_SERVER_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this CreateBitbucketServerConfigSourceDetails.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this CreateBitbucketServerConfigSourceDetails.
        :type working_directory: str

        :param configuration_source_provider_id:
            The value to assign to the configuration_source_provider_id property of this CreateBitbucketServerConfigSourceDetails.
        :type configuration_source_provider_id: str

        :param repository_url:
            The value to assign to the repository_url property of this CreateBitbucketServerConfigSourceDetails.
        :type repository_url: str

        :param branch_name:
            The value to assign to the branch_name property of this CreateBitbucketServerConfigSourceDetails.
        :type branch_name: str

        :param project_id:
            The value to assign to the project_id property of this CreateBitbucketServerConfigSourceDetails.
        :type project_id: str

        :param repository_id:
            The value to assign to the repository_id property of this CreateBitbucketServerConfigSourceDetails.
        :type repository_id: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str',
            'configuration_source_provider_id': 'str',
            'repository_url': 'str',
            'branch_name': 'str',
            'project_id': 'str',
            'repository_id': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory',
            'configuration_source_provider_id': 'configurationSourceProviderId',
            'repository_url': 'repositoryUrl',
            'branch_name': 'branchName',
            'project_id': 'projectId',
            'repository_id': 'repositoryId'
        }

        self._config_source_type = None
        self._working_directory = None
        self._configuration_source_provider_id = None
        self._repository_url = None
        self._branch_name = None
        self._project_id = None
        self._repository_id = None
        self._config_source_type = 'BITBUCKET_SERVER_CONFIG_SOURCE'

    @property
    def configuration_source_provider_id(self):
        """
        **[Required]** Gets the configuration_source_provider_id of this CreateBitbucketServerConfigSourceDetails.
        Unique identifier (`OCID`__)
        for the Bitbucket Server configuration source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The configuration_source_provider_id of this CreateBitbucketServerConfigSourceDetails.
        :rtype: str
        """
        return self._configuration_source_provider_id

    @configuration_source_provider_id.setter
    def configuration_source_provider_id(self, configuration_source_provider_id):
        """
        Sets the configuration_source_provider_id of this CreateBitbucketServerConfigSourceDetails.
        Unique identifier (`OCID`__)
        for the Bitbucket Server configuration source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param configuration_source_provider_id: The configuration_source_provider_id of this CreateBitbucketServerConfigSourceDetails.
        :type: str
        """
        self._configuration_source_provider_id = configuration_source_provider_id

    @property
    def repository_url(self):
        """
        **[Required]** Gets the repository_url of this CreateBitbucketServerConfigSourceDetails.
        The URL of the Bitbucket Server repository.


        :return: The repository_url of this CreateBitbucketServerConfigSourceDetails.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this CreateBitbucketServerConfigSourceDetails.
        The URL of the Bitbucket Server repository.


        :param repository_url: The repository_url of this CreateBitbucketServerConfigSourceDetails.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def branch_name(self):
        """
        Gets the branch_name of this CreateBitbucketServerConfigSourceDetails.
        The name of the branch within the Bitbucket Server repository.


        :return: The branch_name of this CreateBitbucketServerConfigSourceDetails.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """
        Sets the branch_name of this CreateBitbucketServerConfigSourceDetails.
        The name of the branch within the Bitbucket Server repository.


        :param branch_name: The branch_name of this CreateBitbucketServerConfigSourceDetails.
        :type: str
        """
        self._branch_name = branch_name

    @property
    def project_id(self):
        """
        Gets the project_id of this CreateBitbucketServerConfigSourceDetails.
        Unique identifier for a Bitbucket Server project.


        :return: The project_id of this CreateBitbucketServerConfigSourceDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateBitbucketServerConfigSourceDetails.
        Unique identifier for a Bitbucket Server project.


        :param project_id: The project_id of this CreateBitbucketServerConfigSourceDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def repository_id(self):
        """
        Gets the repository_id of this CreateBitbucketServerConfigSourceDetails.
        Bitbucket Server repository identifier, usually identified as <repository>.git.


        :return: The repository_id of this CreateBitbucketServerConfigSourceDetails.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this CreateBitbucketServerConfigSourceDetails.
        Bitbucket Server repository identifier, usually identified as <repository>.git.


        :param repository_id: The repository_id of this CreateBitbucketServerConfigSourceDetails.
        :type: str
        """
        self._repository_id = repository_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
