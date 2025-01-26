# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SwitchOverDataGuardDetails(object):
    """
    The Data Guard switchover parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SwitchOverDataGuardDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_admin_password:
            The value to assign to the database_admin_password property of this SwitchOverDataGuardDetails.
        :type database_admin_password: str

        """
        self.swagger_types = {
            'database_admin_password': 'str'
        }

        self.attribute_map = {
            'database_admin_password': 'databaseAdminPassword'
        }

        self._database_admin_password = None

    @property
    def database_admin_password(self):
        """
        **[Required]** Gets the database_admin_password of this SwitchOverDataGuardDetails.
        The administrator password of the primary database in this Data Guard association.

        **The password MUST be the same as the primary admin password.**


        :return: The database_admin_password of this SwitchOverDataGuardDetails.
        :rtype: str
        """
        return self._database_admin_password

    @database_admin_password.setter
    def database_admin_password(self, database_admin_password):
        """
        Sets the database_admin_password of this SwitchOverDataGuardDetails.
        The administrator password of the primary database in this Data Guard association.

        **The password MUST be the same as the primary admin password.**


        :param database_admin_password: The database_admin_password of this SwitchOverDataGuardDetails.
        :type: str
        """
        self._database_admin_password = database_admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
