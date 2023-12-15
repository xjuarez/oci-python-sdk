# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HelmChartImageDetails(object):
    """
    Helmchart image details.
    """

    #: A constant which can be used with the validation_status property of a HelmChartImageDetails.
    #: This constant has a value of "VALIDATION_IN_PROGRESS"
    VALIDATION_STATUS_VALIDATION_IN_PROGRESS = "VALIDATION_IN_PROGRESS"

    #: A constant which can be used with the validation_status property of a HelmChartImageDetails.
    #: This constant has a value of "VALIDATION_FAILED"
    VALIDATION_STATUS_VALIDATION_FAILED = "VALIDATION_FAILED"

    #: A constant which can be used with the validation_status property of a HelmChartImageDetails.
    #: This constant has a value of "VALIDATION_COMPLETED"
    VALIDATION_STATUS_VALIDATION_COMPLETED = "VALIDATION_COMPLETED"

    #: A constant which can be used with the publication_status property of a HelmChartImageDetails.
    #: This constant has a value of "PUBLICATION_IN_PROGRESS"
    PUBLICATION_STATUS_PUBLICATION_IN_PROGRESS = "PUBLICATION_IN_PROGRESS"

    #: A constant which can be used with the publication_status property of a HelmChartImageDetails.
    #: This constant has a value of "PUBLICATION_COMPLETED"
    PUBLICATION_STATUS_PUBLICATION_COMPLETED = "PUBLICATION_COMPLETED"

    #: A constant which can be used with the publication_status property of a HelmChartImageDetails.
    #: This constant has a value of "PUBLICATION_FAILED"
    PUBLICATION_STATUS_PUBLICATION_FAILED = "PUBLICATION_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new HelmChartImageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_registry_id:
            The value to assign to the source_registry_id property of this HelmChartImageDetails.
        :type source_registry_id: str

        :param source_registry_url:
            The value to assign to the source_registry_url property of this HelmChartImageDetails.
        :type source_registry_url: str

        :param supported_kubernetes_versions:
            The value to assign to the supported_kubernetes_versions property of this HelmChartImageDetails.
        :type supported_kubernetes_versions: list[str]

        :param validation_status:
            The value to assign to the validation_status property of this HelmChartImageDetails.
            Allowed values for this property are: "VALIDATION_IN_PROGRESS", "VALIDATION_FAILED", "VALIDATION_COMPLETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type validation_status: str

        :param validation_error:
            The value to assign to the validation_error property of this HelmChartImageDetails.
        :type validation_error: str

        :param publication_status:
            The value to assign to the publication_status property of this HelmChartImageDetails.
            Allowed values for this property are: "PUBLICATION_IN_PROGRESS", "PUBLICATION_COMPLETED", "PUBLICATION_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type publication_status: str

        :param publication_error:
            The value to assign to the publication_error property of this HelmChartImageDetails.
        :type publication_error: str

        """
        self.swagger_types = {
            'source_registry_id': 'str',
            'source_registry_url': 'str',
            'supported_kubernetes_versions': 'list[str]',
            'validation_status': 'str',
            'validation_error': 'str',
            'publication_status': 'str',
            'publication_error': 'str'
        }

        self.attribute_map = {
            'source_registry_id': 'sourceRegistryId',
            'source_registry_url': 'sourceRegistryUrl',
            'supported_kubernetes_versions': 'supportedKubernetesVersions',
            'validation_status': 'validationStatus',
            'validation_error': 'validationError',
            'publication_status': 'publicationStatus',
            'publication_error': 'publicationError'
        }

        self._source_registry_id = None
        self._source_registry_url = None
        self._supported_kubernetes_versions = None
        self._validation_status = None
        self._validation_error = None
        self._publication_status = None
        self._publication_error = None

    @property
    def source_registry_id(self):
        """
        Gets the source_registry_id of this HelmChartImageDetails.
        The source registry OCID of the helmchart image.


        :return: The source_registry_id of this HelmChartImageDetails.
        :rtype: str
        """
        return self._source_registry_id

    @source_registry_id.setter
    def source_registry_id(self, source_registry_id):
        """
        Sets the source_registry_id of this HelmChartImageDetails.
        The source registry OCID of the helmchart image.


        :param source_registry_id: The source_registry_id of this HelmChartImageDetails.
        :type: str
        """
        self._source_registry_id = source_registry_id

    @property
    def source_registry_url(self):
        """
        **[Required]** Gets the source_registry_url of this HelmChartImageDetails.
        source registry url of the helmchart image.


        :return: The source_registry_url of this HelmChartImageDetails.
        :rtype: str
        """
        return self._source_registry_url

    @source_registry_url.setter
    def source_registry_url(self, source_registry_url):
        """
        Sets the source_registry_url of this HelmChartImageDetails.
        source registry url of the helmchart image.


        :param source_registry_url: The source_registry_url of this HelmChartImageDetails.
        :type: str
        """
        self._source_registry_url = source_registry_url

    @property
    def supported_kubernetes_versions(self):
        """
        Gets the supported_kubernetes_versions of this HelmChartImageDetails.
        The supported versions of Kubernetes


        :return: The supported_kubernetes_versions of this HelmChartImageDetails.
        :rtype: list[str]
        """
        return self._supported_kubernetes_versions

    @supported_kubernetes_versions.setter
    def supported_kubernetes_versions(self, supported_kubernetes_versions):
        """
        Sets the supported_kubernetes_versions of this HelmChartImageDetails.
        The supported versions of Kubernetes


        :param supported_kubernetes_versions: The supported_kubernetes_versions of this HelmChartImageDetails.
        :type: list[str]
        """
        self._supported_kubernetes_versions = supported_kubernetes_versions

    @property
    def validation_status(self):
        """
        **[Required]** Gets the validation_status of this HelmChartImageDetails.
        image validation status.

        Allowed values for this property are: "VALIDATION_IN_PROGRESS", "VALIDATION_FAILED", "VALIDATION_COMPLETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The validation_status of this HelmChartImageDetails.
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """
        Sets the validation_status of this HelmChartImageDetails.
        image validation status.


        :param validation_status: The validation_status of this HelmChartImageDetails.
        :type: str
        """
        allowed_values = ["VALIDATION_IN_PROGRESS", "VALIDATION_FAILED", "VALIDATION_COMPLETED"]
        if not value_allowed_none_or_none_sentinel(validation_status, allowed_values):
            validation_status = 'UNKNOWN_ENUM_VALUE'
        self._validation_status = validation_status

    @property
    def validation_error(self):
        """
        Gets the validation_error of this HelmChartImageDetails.
        image validation failure errors


        :return: The validation_error of this HelmChartImageDetails.
        :rtype: str
        """
        return self._validation_error

    @validation_error.setter
    def validation_error(self, validation_error):
        """
        Sets the validation_error of this HelmChartImageDetails.
        image validation failure errors


        :param validation_error: The validation_error of this HelmChartImageDetails.
        :type: str
        """
        self._validation_error = validation_error

    @property
    def publication_status(self):
        """
        **[Required]** Gets the publication_status of this HelmChartImageDetails.
        image publication status

        Allowed values for this property are: "PUBLICATION_IN_PROGRESS", "PUBLICATION_COMPLETED", "PUBLICATION_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The publication_status of this HelmChartImageDetails.
        :rtype: str
        """
        return self._publication_status

    @publication_status.setter
    def publication_status(self, publication_status):
        """
        Sets the publication_status of this HelmChartImageDetails.
        image publication status


        :param publication_status: The publication_status of this HelmChartImageDetails.
        :type: str
        """
        allowed_values = ["PUBLICATION_IN_PROGRESS", "PUBLICATION_COMPLETED", "PUBLICATION_FAILED"]
        if not value_allowed_none_or_none_sentinel(publication_status, allowed_values):
            publication_status = 'UNKNOWN_ENUM_VALUE'
        self._publication_status = publication_status

    @property
    def publication_error(self):
        """
        Gets the publication_error of this HelmChartImageDetails.
        image validation failure errors


        :return: The publication_error of this HelmChartImageDetails.
        :rtype: str
        """
        return self._publication_error

    @publication_error.setter
    def publication_error(self, publication_error):
        """
        Sets the publication_error of this HelmChartImageDetails.
        image validation failure errors


        :param publication_error: The publication_error of this HelmChartImageDetails.
        :type: str
        """
        self._publication_error = publication_error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
