# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateJavaDownloadTokenDetails(object):
    """
    The attributes of the JavaDownloadToken to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateJavaDownloadTokenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateJavaDownloadTokenDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateJavaDownloadTokenDetails.
        :type description: str

        :param is_default:
            The value to assign to the is_default property of this UpdateJavaDownloadTokenDetails.
        :type is_default: bool

        :param time_expires:
            The value to assign to the time_expires property of this UpdateJavaDownloadTokenDetails.
        :type time_expires: datetime

        :param license_type:
            The value to assign to the license_type property of this UpdateJavaDownloadTokenDetails.
        :type license_type: list[oci.jms_java_downloads.models.LicenseType]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateJavaDownloadTokenDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateJavaDownloadTokenDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'is_default': 'bool',
            'time_expires': 'datetime',
            'license_type': 'list[LicenseType]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'is_default': 'isDefault',
            'time_expires': 'timeExpires',
            'license_type': 'licenseType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._is_default = None
        self._time_expires = None
        self._license_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateJavaDownloadTokenDetails.
        User provided display name of the JavaDownloadToken.


        :return: The display_name of this UpdateJavaDownloadTokenDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateJavaDownloadTokenDetails.
        User provided display name of the JavaDownloadToken.


        :param display_name: The display_name of this UpdateJavaDownloadTokenDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateJavaDownloadTokenDetails.
        User provided description of the JavaDownloadToken.


        :return: The description of this UpdateJavaDownloadTokenDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateJavaDownloadTokenDetails.
        User provided description of the JavaDownloadToken.


        :param description: The description of this UpdateJavaDownloadTokenDetails.
        :type: str
        """
        self._description = description

    @property
    def is_default(self):
        """
        Gets the is_default of this UpdateJavaDownloadTokenDetails.
        Update the token default status.


        :return: The is_default of this UpdateJavaDownloadTokenDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this UpdateJavaDownloadTokenDetails.
        Update the token default status.


        :param is_default: The is_default of this UpdateJavaDownloadTokenDetails.
        :type: bool
        """
        self._is_default = is_default

    @property
    def time_expires(self):
        """
        Gets the time_expires of this UpdateJavaDownloadTokenDetails.
        Expiry time of the token.


        :return: The time_expires of this UpdateJavaDownloadTokenDetails.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this UpdateJavaDownloadTokenDetails.
        Expiry time of the token.


        :param time_expires: The time_expires of this UpdateJavaDownloadTokenDetails.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def license_type(self):
        """
        Gets the license_type of this UpdateJavaDownloadTokenDetails.
        The license type(s) associated with the JavaDownloadToken.


        :return: The license_type of this UpdateJavaDownloadTokenDetails.
        :rtype: list[oci.jms_java_downloads.models.LicenseType]
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this UpdateJavaDownloadTokenDetails.
        The license type(s) associated with the JavaDownloadToken.


        :param license_type: The license_type of this UpdateJavaDownloadTokenDetails.
        :type: list[oci.jms_java_downloads.models.LicenseType]
        """
        self._license_type = license_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateJavaDownloadTokenDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this UpdateJavaDownloadTokenDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateJavaDownloadTokenDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this UpdateJavaDownloadTokenDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateJavaDownloadTokenDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this UpdateJavaDownloadTokenDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateJavaDownloadTokenDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this UpdateJavaDownloadTokenDetails.
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
