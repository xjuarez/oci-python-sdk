# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SaasAdminUserConfiguration(object):
    """
    SaaS administrative user configuration.
    """

    #: A constant which can be used with the access_type property of a SaasAdminUserConfiguration.
    #: This constant has a value of "READ_ONLY"
    ACCESS_TYPE_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the access_type property of a SaasAdminUserConfiguration.
    #: This constant has a value of "READ_WRITE"
    ACCESS_TYPE_READ_WRITE = "READ_WRITE"

    #: A constant which can be used with the access_type property of a SaasAdminUserConfiguration.
    #: This constant has a value of "ADMIN"
    ACCESS_TYPE_ADMIN = "ADMIN"

    def __init__(self, **kwargs):
        """
        Initializes a new SaasAdminUserConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this SaasAdminUserConfiguration.
        :type password: str

        :param secret_id:
            The value to assign to the secret_id property of this SaasAdminUserConfiguration.
        :type secret_id: str

        :param secret_version_number:
            The value to assign to the secret_version_number property of this SaasAdminUserConfiguration.
        :type secret_version_number: int

        :param duration:
            The value to assign to the duration property of this SaasAdminUserConfiguration.
        :type duration: int

        :param is_enabled:
            The value to assign to the is_enabled property of this SaasAdminUserConfiguration.
        :type is_enabled: bool

        :param access_type:
            The value to assign to the access_type property of this SaasAdminUserConfiguration.
            Allowed values for this property are: "READ_ONLY", "READ_WRITE", "ADMIN"
        :type access_type: str

        :param time_saas_admin_user_enabled:
            The value to assign to the time_saas_admin_user_enabled property of this SaasAdminUserConfiguration.
        :type time_saas_admin_user_enabled: datetime

        """
        self.swagger_types = {
            'password': 'str',
            'secret_id': 'str',
            'secret_version_number': 'int',
            'duration': 'int',
            'is_enabled': 'bool',
            'access_type': 'str',
            'time_saas_admin_user_enabled': 'datetime'
        }

        self.attribute_map = {
            'password': 'password',
            'secret_id': 'secretId',
            'secret_version_number': 'secretVersionNumber',
            'duration': 'duration',
            'is_enabled': 'isEnabled',
            'access_type': 'accessType',
            'time_saas_admin_user_enabled': 'timeSaasAdminUserEnabled'
        }

        self._password = None
        self._secret_id = None
        self._secret_version_number = None
        self._duration = None
        self._is_enabled = None
        self._access_type = None
        self._time_saas_admin_user_enabled = None

    @property
    def password(self):
        """
        Gets the password of this SaasAdminUserConfiguration.
        A strong password for SaaS administrative user. The password must be a minimum of nine (9) characters and contain a minimum of two (2) uppercase, two (2) lowercase, two (2) numbers, and two (2) special characters from _ (underscore), \\# (hashtag), or - (dash).


        :return: The password of this SaasAdminUserConfiguration.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this SaasAdminUserConfiguration.
        A strong password for SaaS administrative user. The password must be a minimum of nine (9) characters and contain a minimum of two (2) uppercase, two (2) lowercase, two (2) numbers, and two (2) special characters from _ (underscore), \\# (hashtag), or - (dash).


        :param password: The password of this SaasAdminUserConfiguration.
        :type: str
        """
        self._password = password

    @property
    def secret_id(self):
        """
        Gets the secret_id of this SaasAdminUserConfiguration.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The secret_id of this SaasAdminUserConfiguration.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this SaasAdminUserConfiguration.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param secret_id: The secret_id of this SaasAdminUserConfiguration.
        :type: str
        """
        self._secret_id = secret_id

    @property
    def secret_version_number(self):
        """
        Gets the secret_version_number of this SaasAdminUserConfiguration.
        The version of the vault secret. If no version is specified, the latest version will be used.


        :return: The secret_version_number of this SaasAdminUserConfiguration.
        :rtype: int
        """
        return self._secret_version_number

    @secret_version_number.setter
    def secret_version_number(self, secret_version_number):
        """
        Sets the secret_version_number of this SaasAdminUserConfiguration.
        The version of the vault secret. If no version is specified, the latest version will be used.


        :param secret_version_number: The secret_version_number of this SaasAdminUserConfiguration.
        :type: int
        """
        self._secret_version_number = secret_version_number

    @property
    def duration(self):
        """
        Gets the duration of this SaasAdminUserConfiguration.
        How long, in hours, the SaaS administrative user will stay enabled. If no duration is specified, the default value 1 will be used.


        :return: The duration of this SaasAdminUserConfiguration.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this SaasAdminUserConfiguration.
        How long, in hours, the SaaS administrative user will stay enabled. If no duration is specified, the default value 1 will be used.


        :param duration: The duration of this SaasAdminUserConfiguration.
        :type: int
        """
        self._duration = duration

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this SaasAdminUserConfiguration.
        Indicates if the SaaS administrative user is enabled for the Autonomous Database.


        :return: The is_enabled of this SaasAdminUserConfiguration.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this SaasAdminUserConfiguration.
        Indicates if the SaaS administrative user is enabled for the Autonomous Database.


        :param is_enabled: The is_enabled of this SaasAdminUserConfiguration.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def access_type(self):
        """
        Gets the access_type of this SaasAdminUserConfiguration.
        The access type for the SaaS administrative user. If no access type is specified, the READ_ONLY access type is used.

        Allowed values for this property are: "READ_ONLY", "READ_WRITE", "ADMIN"


        :return: The access_type of this SaasAdminUserConfiguration.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this SaasAdminUserConfiguration.
        The access type for the SaaS administrative user. If no access type is specified, the READ_ONLY access type is used.


        :param access_type: The access_type of this SaasAdminUserConfiguration.
        :type: str
        """
        allowed_values = ["READ_ONLY", "READ_WRITE", "ADMIN"]
        if not value_allowed_none_or_none_sentinel(access_type, allowed_values):
            raise ValueError(
                f"Invalid value for `access_type`, must be None or one of {allowed_values}"
            )
        self._access_type = access_type

    @property
    def time_saas_admin_user_enabled(self):
        """
        Gets the time_saas_admin_user_enabled of this SaasAdminUserConfiguration.
        The date and time the SaaS administrative user was enabled at, for the Autonomous Database.


        :return: The time_saas_admin_user_enabled of this SaasAdminUserConfiguration.
        :rtype: datetime
        """
        return self._time_saas_admin_user_enabled

    @time_saas_admin_user_enabled.setter
    def time_saas_admin_user_enabled(self, time_saas_admin_user_enabled):
        """
        Sets the time_saas_admin_user_enabled of this SaasAdminUserConfiguration.
        The date and time the SaaS administrative user was enabled at, for the Autonomous Database.


        :param time_saas_admin_user_enabled: The time_saas_admin_user_enabled of this SaasAdminUserConfiguration.
        :type: datetime
        """
        self._time_saas_admin_user_enabled = time_saas_admin_user_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
