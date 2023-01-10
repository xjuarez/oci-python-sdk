# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaReleaseSummary(object):
    """
    A summary of the Java release properties.
    """

    #: A constant which can be used with the security_status property of a JavaReleaseSummary.
    #: This constant has a value of "UNKNOWN"
    SECURITY_STATUS_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the security_status property of a JavaReleaseSummary.
    #: This constant has a value of "UP_TO_DATE"
    SECURITY_STATUS_UP_TO_DATE = "UP_TO_DATE"

    #: A constant which can be used with the security_status property of a JavaReleaseSummary.
    #: This constant has a value of "UPDATE_REQUIRED"
    SECURITY_STATUS_UPDATE_REQUIRED = "UPDATE_REQUIRED"

    #: A constant which can be used with the security_status property of a JavaReleaseSummary.
    #: This constant has a value of "UPGRADE_REQUIRED"
    SECURITY_STATUS_UPGRADE_REQUIRED = "UPGRADE_REQUIRED"

    #: A constant which can be used with the release_type property of a JavaReleaseSummary.
    #: This constant has a value of "CPU"
    RELEASE_TYPE_CPU = "CPU"

    #: A constant which can be used with the release_type property of a JavaReleaseSummary.
    #: This constant has a value of "FEATURE"
    RELEASE_TYPE_FEATURE = "FEATURE"

    #: A constant which can be used with the release_type property of a JavaReleaseSummary.
    #: This constant has a value of "BPR"
    RELEASE_TYPE_BPR = "BPR"

    #: A constant which can be used with the release_type property of a JavaReleaseSummary.
    #: This constant has a value of "PATCH_RELEASE"
    RELEASE_TYPE_PATCH_RELEASE = "PATCH_RELEASE"

    #: A constant which can be used with the license_type property of a JavaReleaseSummary.
    #: This constant has a value of "OTN"
    LICENSE_TYPE_OTN = "OTN"

    #: A constant which can be used with the license_type property of a JavaReleaseSummary.
    #: This constant has a value of "NFTC"
    LICENSE_TYPE_NFTC = "NFTC"

    #: A constant which can be used with the license_type property of a JavaReleaseSummary.
    #: This constant has a value of "RESTRICTED"
    LICENSE_TYPE_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the artifact_content_types property of a JavaReleaseSummary.
    #: This constant has a value of "JDK"
    ARTIFACT_CONTENT_TYPES_JDK = "JDK"

    #: A constant which can be used with the artifact_content_types property of a JavaReleaseSummary.
    #: This constant has a value of "JRE"
    ARTIFACT_CONTENT_TYPES_JRE = "JRE"

    #: A constant which can be used with the artifact_content_types property of a JavaReleaseSummary.
    #: This constant has a value of "SERVER_JRE"
    ARTIFACT_CONTENT_TYPES_SERVER_JRE = "SERVER_JRE"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaReleaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param release_version:
            The value to assign to the release_version property of this JavaReleaseSummary.
        :type release_version: str

        :param family_version:
            The value to assign to the family_version property of this JavaReleaseSummary.
        :type family_version: str

        :param parent_release_version:
            The value to assign to the parent_release_version property of this JavaReleaseSummary.
        :type parent_release_version: str

        :param security_status:
            The value to assign to the security_status property of this JavaReleaseSummary.
            Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type security_status: str

        :param release_type:
            The value to assign to the release_type property of this JavaReleaseSummary.
            Allowed values for this property are: "CPU", "FEATURE", "BPR", "PATCH_RELEASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type release_type: str

        :param license_type:
            The value to assign to the license_type property of this JavaReleaseSummary.
            Allowed values for this property are: "OTN", "NFTC", "RESTRICTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_type: str

        :param family_details:
            The value to assign to the family_details property of this JavaReleaseSummary.
        :type family_details: oci.jms.models.JavaFamily

        :param license_details:
            The value to assign to the license_details property of this JavaReleaseSummary.
        :type license_details: oci.jms.models.JavaLicense

        :param release_date:
            The value to assign to the release_date property of this JavaReleaseSummary.
        :type release_date: datetime

        :param release_notes_url:
            The value to assign to the release_notes_url property of this JavaReleaseSummary.
        :type release_notes_url: str

        :param artifact_content_types:
            The value to assign to the artifact_content_types property of this JavaReleaseSummary.
            Allowed values for items in this list are: "JDK", "JRE", "SERVER_JRE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type artifact_content_types: list[str]

        """
        self.swagger_types = {
            'release_version': 'str',
            'family_version': 'str',
            'parent_release_version': 'str',
            'security_status': 'str',
            'release_type': 'str',
            'license_type': 'str',
            'family_details': 'JavaFamily',
            'license_details': 'JavaLicense',
            'release_date': 'datetime',
            'release_notes_url': 'str',
            'artifact_content_types': 'list[str]'
        }

        self.attribute_map = {
            'release_version': 'releaseVersion',
            'family_version': 'familyVersion',
            'parent_release_version': 'parentReleaseVersion',
            'security_status': 'securityStatus',
            'release_type': 'releaseType',
            'license_type': 'licenseType',
            'family_details': 'familyDetails',
            'license_details': 'licenseDetails',
            'release_date': 'releaseDate',
            'release_notes_url': 'releaseNotesUrl',
            'artifact_content_types': 'artifactContentTypes'
        }

        self._release_version = None
        self._family_version = None
        self._parent_release_version = None
        self._security_status = None
        self._release_type = None
        self._license_type = None
        self._family_details = None
        self._license_details = None
        self._release_date = None
        self._release_notes_url = None
        self._artifact_content_types = None

    @property
    def release_version(self):
        """
        **[Required]** Gets the release_version of this JavaReleaseSummary.
        Java release version identifier.


        :return: The release_version of this JavaReleaseSummary.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """
        Sets the release_version of this JavaReleaseSummary.
        Java release version identifier.


        :param release_version: The release_version of this JavaReleaseSummary.
        :type: str
        """
        self._release_version = release_version

    @property
    def family_version(self):
        """
        **[Required]** Gets the family_version of this JavaReleaseSummary.
        Java release family identifier.


        :return: The family_version of this JavaReleaseSummary.
        :rtype: str
        """
        return self._family_version

    @family_version.setter
    def family_version(self, family_version):
        """
        Sets the family_version of this JavaReleaseSummary.
        Java release family identifier.


        :param family_version: The family_version of this JavaReleaseSummary.
        :type: str
        """
        self._family_version = family_version

    @property
    def parent_release_version(self):
        """
        Gets the parent_release_version of this JavaReleaseSummary.
        Parent Java release version identifier. This is applicable for BPR releases.


        :return: The parent_release_version of this JavaReleaseSummary.
        :rtype: str
        """
        return self._parent_release_version

    @parent_release_version.setter
    def parent_release_version(self, parent_release_version):
        """
        Sets the parent_release_version of this JavaReleaseSummary.
        Parent Java release version identifier. This is applicable for BPR releases.


        :param parent_release_version: The parent_release_version of this JavaReleaseSummary.
        :type: str
        """
        self._parent_release_version = parent_release_version

    @property
    def security_status(self):
        """
        **[Required]** Gets the security_status of this JavaReleaseSummary.
        The security status of the Java version.

        Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The security_status of this JavaReleaseSummary.
        :rtype: str
        """
        return self._security_status

    @security_status.setter
    def security_status(self, security_status):
        """
        Sets the security_status of this JavaReleaseSummary.
        The security status of the Java version.


        :param security_status: The security_status of this JavaReleaseSummary.
        :type: str
        """
        allowed_values = ["UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"]
        if not value_allowed_none_or_none_sentinel(security_status, allowed_values):
            security_status = 'UNKNOWN_ENUM_VALUE'
        self._security_status = security_status

    @property
    def release_type(self):
        """
        **[Required]** Gets the release_type of this JavaReleaseSummary.
        Release category of the Java version.

        Allowed values for this property are: "CPU", "FEATURE", "BPR", "PATCH_RELEASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The release_type of this JavaReleaseSummary.
        :rtype: str
        """
        return self._release_type

    @release_type.setter
    def release_type(self, release_type):
        """
        Sets the release_type of this JavaReleaseSummary.
        Release category of the Java version.


        :param release_type: The release_type of this JavaReleaseSummary.
        :type: str
        """
        allowed_values = ["CPU", "FEATURE", "BPR", "PATCH_RELEASE"]
        if not value_allowed_none_or_none_sentinel(release_type, allowed_values):
            release_type = 'UNKNOWN_ENUM_VALUE'
        self._release_type = release_type

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this JavaReleaseSummary.
        License type for the Java version.

        Allowed values for this property are: "OTN", "NFTC", "RESTRICTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_type of this JavaReleaseSummary.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this JavaReleaseSummary.
        License type for the Java version.


        :param license_type: The license_type of this JavaReleaseSummary.
        :type: str
        """
        allowed_values = ["OTN", "NFTC", "RESTRICTED"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            license_type = 'UNKNOWN_ENUM_VALUE'
        self._license_type = license_type

    @property
    def family_details(self):
        """
        Gets the family_details of this JavaReleaseSummary.

        :return: The family_details of this JavaReleaseSummary.
        :rtype: oci.jms.models.JavaFamily
        """
        return self._family_details

    @family_details.setter
    def family_details(self, family_details):
        """
        Sets the family_details of this JavaReleaseSummary.

        :param family_details: The family_details of this JavaReleaseSummary.
        :type: oci.jms.models.JavaFamily
        """
        self._family_details = family_details

    @property
    def license_details(self):
        """
        Gets the license_details of this JavaReleaseSummary.

        :return: The license_details of this JavaReleaseSummary.
        :rtype: oci.jms.models.JavaLicense
        """
        return self._license_details

    @license_details.setter
    def license_details(self, license_details):
        """
        Sets the license_details of this JavaReleaseSummary.

        :param license_details: The license_details of this JavaReleaseSummary.
        :type: oci.jms.models.JavaLicense
        """
        self._license_details = license_details

    @property
    def release_date(self):
        """
        **[Required]** Gets the release_date of this JavaReleaseSummary.
        The release date of the Java version (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The release_date of this JavaReleaseSummary.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this JavaReleaseSummary.
        The release date of the Java version (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param release_date: The release_date of this JavaReleaseSummary.
        :type: datetime
        """
        self._release_date = release_date

    @property
    def release_notes_url(self):
        """
        **[Required]** Gets the release_notes_url of this JavaReleaseSummary.
        Release notes associated with the Java version.


        :return: The release_notes_url of this JavaReleaseSummary.
        :rtype: str
        """
        return self._release_notes_url

    @release_notes_url.setter
    def release_notes_url(self, release_notes_url):
        """
        Sets the release_notes_url of this JavaReleaseSummary.
        Release notes associated with the Java version.


        :param release_notes_url: The release_notes_url of this JavaReleaseSummary.
        :type: str
        """
        self._release_notes_url = release_notes_url

    @property
    def artifact_content_types(self):
        """
        **[Required]** Gets the artifact_content_types of this JavaReleaseSummary.
        Artifact content types for the Java version.

        Allowed values for items in this list are: "JDK", "JRE", "SERVER_JRE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The artifact_content_types of this JavaReleaseSummary.
        :rtype: list[str]
        """
        return self._artifact_content_types

    @artifact_content_types.setter
    def artifact_content_types(self, artifact_content_types):
        """
        Sets the artifact_content_types of this JavaReleaseSummary.
        Artifact content types for the Java version.


        :param artifact_content_types: The artifact_content_types of this JavaReleaseSummary.
        :type: list[str]
        """
        allowed_values = ["JDK", "JRE", "SERVER_JRE"]
        if artifact_content_types:
            artifact_content_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in artifact_content_types]
        self._artifact_content_types = artifact_content_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
