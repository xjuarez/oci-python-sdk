# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateBasicFilterDetails(object):
    """
    Validate the basic filter criteria provided by the user.
    It takes either credentialDetails or databaseCredential. It's recommended to provide databaseCredential
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateBasicFilterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this ValidateBasicFilterDetails.
        :type credential_details: oci.database_management.models.SqlTuningSetAdminCredentialDetails

        :param database_credential:
            The value to assign to the database_credential property of this ValidateBasicFilterDetails.
        :type database_credential: oci.database_management.models.DatabaseCredentialDetails

        :param owner:
            The value to assign to the owner property of this ValidateBasicFilterDetails.
        :type owner: str

        :param name:
            The value to assign to the name property of this ValidateBasicFilterDetails.
        :type name: str

        :param basic_filter:
            The value to assign to the basic_filter property of this ValidateBasicFilterDetails.
        :type basic_filter: str

        """
        self.swagger_types = {
            'credential_details': 'SqlTuningSetAdminCredentialDetails',
            'database_credential': 'DatabaseCredentialDetails',
            'owner': 'str',
            'name': 'str',
            'basic_filter': 'str'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'database_credential': 'databaseCredential',
            'owner': 'owner',
            'name': 'name',
            'basic_filter': 'basicFilter'
        }

        self._credential_details = None
        self._database_credential = None
        self._owner = None
        self._name = None
        self._basic_filter = None

    @property
    def credential_details(self):
        """
        Gets the credential_details of this ValidateBasicFilterDetails.

        :return: The credential_details of this ValidateBasicFilterDetails.
        :rtype: oci.database_management.models.SqlTuningSetAdminCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this ValidateBasicFilterDetails.

        :param credential_details: The credential_details of this ValidateBasicFilterDetails.
        :type: oci.database_management.models.SqlTuningSetAdminCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def database_credential(self):
        """
        Gets the database_credential of this ValidateBasicFilterDetails.

        :return: The database_credential of this ValidateBasicFilterDetails.
        :rtype: oci.database_management.models.DatabaseCredentialDetails
        """
        return self._database_credential

    @database_credential.setter
    def database_credential(self, database_credential):
        """
        Sets the database_credential of this ValidateBasicFilterDetails.

        :param database_credential: The database_credential of this ValidateBasicFilterDetails.
        :type: oci.database_management.models.DatabaseCredentialDetails
        """
        self._database_credential = database_credential

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this ValidateBasicFilterDetails.
        The owner of the Sql tuning set.


        :return: The owner of this ValidateBasicFilterDetails.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this ValidateBasicFilterDetails.
        The owner of the Sql tuning set.


        :param owner: The owner of this ValidateBasicFilterDetails.
        :type: str
        """
        self._owner = owner

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ValidateBasicFilterDetails.
        The name of the Sql tuning set.


        :return: The name of this ValidateBasicFilterDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ValidateBasicFilterDetails.
        The name of the Sql tuning set.


        :param name: The name of this ValidateBasicFilterDetails.
        :type: str
        """
        self._name = name

    @property
    def basic_filter(self):
        """
        **[Required]** Gets the basic_filter of this ValidateBasicFilterDetails.
        Specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW.
        User could use any combination of the following columns with appropriate values as Sql predicate
        Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/18/arpls/DBMS_SQLTUNE.html#GUID-1F4AFB03-7B29-46FC-B3F2-CB01EC36326C


        :return: The basic_filter of this ValidateBasicFilterDetails.
        :rtype: str
        """
        return self._basic_filter

    @basic_filter.setter
    def basic_filter(self, basic_filter):
        """
        Sets the basic_filter of this ValidateBasicFilterDetails.
        Specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW.
        User could use any combination of the following columns with appropriate values as Sql predicate
        Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/18/arpls/DBMS_SQLTUNE.html#GUID-1F4AFB03-7B29-46FC-B3F2-CB01EC36326C


        :param basic_filter: The basic_filter of this ValidateBasicFilterDetails.
        :type: str
        """
        self._basic_filter = basic_filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
