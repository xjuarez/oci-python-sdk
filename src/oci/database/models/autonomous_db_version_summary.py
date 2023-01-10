# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDbVersionSummary(object):
    """
    The supported Autonomous Database version.
    """

    #: A constant which can be used with the db_workload property of a AutonomousDbVersionSummary.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a AutonomousDbVersionSummary.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the db_workload property of a AutonomousDbVersionSummary.
    #: This constant has a value of "AJD"
    DB_WORKLOAD_AJD = "AJD"

    #: A constant which can be used with the db_workload property of a AutonomousDbVersionSummary.
    #: This constant has a value of "APEX"
    DB_WORKLOAD_APEX = "APEX"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDbVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this AutonomousDbVersionSummary.
        :type version: str

        :param db_workload:
            The value to assign to the db_workload property of this AutonomousDbVersionSummary.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_workload: str

        :param is_dedicated:
            The value to assign to the is_dedicated property of this AutonomousDbVersionSummary.
        :type is_dedicated: bool

        :param details:
            The value to assign to the details property of this AutonomousDbVersionSummary.
        :type details: str

        :param is_free_tier_enabled:
            The value to assign to the is_free_tier_enabled property of this AutonomousDbVersionSummary.
        :type is_free_tier_enabled: bool

        :param is_paid_enabled:
            The value to assign to the is_paid_enabled property of this AutonomousDbVersionSummary.
        :type is_paid_enabled: bool

        :param is_default_for_free:
            The value to assign to the is_default_for_free property of this AutonomousDbVersionSummary.
        :type is_default_for_free: bool

        :param is_default_for_paid:
            The value to assign to the is_default_for_paid property of this AutonomousDbVersionSummary.
        :type is_default_for_paid: bool

        """
        self.swagger_types = {
            'version': 'str',
            'db_workload': 'str',
            'is_dedicated': 'bool',
            'details': 'str',
            'is_free_tier_enabled': 'bool',
            'is_paid_enabled': 'bool',
            'is_default_for_free': 'bool',
            'is_default_for_paid': 'bool'
        }

        self.attribute_map = {
            'version': 'version',
            'db_workload': 'dbWorkload',
            'is_dedicated': 'isDedicated',
            'details': 'details',
            'is_free_tier_enabled': 'isFreeTierEnabled',
            'is_paid_enabled': 'isPaidEnabled',
            'is_default_for_free': 'isDefaultForFree',
            'is_default_for_paid': 'isDefaultForPaid'
        }

        self._version = None
        self._db_workload = None
        self._is_dedicated = None
        self._details = None
        self._is_free_tier_enabled = None
        self._is_paid_enabled = None
        self._is_default_for_free = None
        self._is_default_for_paid = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this AutonomousDbVersionSummary.
        A valid Oracle Database version for Autonomous Database.


        :return: The version of this AutonomousDbVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AutonomousDbVersionSummary.
        A valid Oracle Database version for Autonomous Database.


        :param version: The version of this AutonomousDbVersionSummary.
        :type: str
        """
        self._version = version

    @property
    def db_workload(self):
        """
        Gets the db_workload of this AutonomousDbVersionSummary.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.

        Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_workload of this AutonomousDbVersionSummary.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this AutonomousDbVersionSummary.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.


        :param db_workload: The db_workload of this AutonomousDbVersionSummary.
        :type: str
        """
        allowed_values = ["OLTP", "DW", "AJD", "APEX"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            db_workload = 'UNKNOWN_ENUM_VALUE'
        self._db_workload = db_workload

    @property
    def is_dedicated(self):
        """
        Gets the is_dedicated of this AutonomousDbVersionSummary.
        True if the database uses `dedicated Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The is_dedicated of this AutonomousDbVersionSummary.
        :rtype: bool
        """
        return self._is_dedicated

    @is_dedicated.setter
    def is_dedicated(self, is_dedicated):
        """
        Sets the is_dedicated of this AutonomousDbVersionSummary.
        True if the database uses `dedicated Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param is_dedicated: The is_dedicated of this AutonomousDbVersionSummary.
        :type: bool
        """
        self._is_dedicated = is_dedicated

    @property
    def details(self):
        """
        Gets the details of this AutonomousDbVersionSummary.
        A URL that points to a detailed description of the Autonomous Database version.


        :return: The details of this AutonomousDbVersionSummary.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this AutonomousDbVersionSummary.
        A URL that points to a detailed description of the Autonomous Database version.


        :param details: The details of this AutonomousDbVersionSummary.
        :type: str
        """
        self._details = details

    @property
    def is_free_tier_enabled(self):
        """
        Gets the is_free_tier_enabled of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software can be used for Always-Free Autonomous Databases.


        :return: The is_free_tier_enabled of this AutonomousDbVersionSummary.
        :rtype: bool
        """
        return self._is_free_tier_enabled

    @is_free_tier_enabled.setter
    def is_free_tier_enabled(self, is_free_tier_enabled):
        """
        Sets the is_free_tier_enabled of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software can be used for Always-Free Autonomous Databases.


        :param is_free_tier_enabled: The is_free_tier_enabled of this AutonomousDbVersionSummary.
        :type: bool
        """
        self._is_free_tier_enabled = is_free_tier_enabled

    @property
    def is_paid_enabled(self):
        """
        Gets the is_paid_enabled of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software has payments enabled.


        :return: The is_paid_enabled of this AutonomousDbVersionSummary.
        :rtype: bool
        """
        return self._is_paid_enabled

    @is_paid_enabled.setter
    def is_paid_enabled(self, is_paid_enabled):
        """
        Sets the is_paid_enabled of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software has payments enabled.


        :param is_paid_enabled: The is_paid_enabled of this AutonomousDbVersionSummary.
        :type: bool
        """
        self._is_paid_enabled = is_paid_enabled

    @property
    def is_default_for_free(self):
        """
        Gets the is_default_for_free of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software's default is free.


        :return: The is_default_for_free of this AutonomousDbVersionSummary.
        :rtype: bool
        """
        return self._is_default_for_free

    @is_default_for_free.setter
    def is_default_for_free(self, is_default_for_free):
        """
        Sets the is_default_for_free of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software's default is free.


        :param is_default_for_free: The is_default_for_free of this AutonomousDbVersionSummary.
        :type: bool
        """
        self._is_default_for_free = is_default_for_free

    @property
    def is_default_for_paid(self):
        """
        Gets the is_default_for_paid of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software's default is paid.


        :return: The is_default_for_paid of this AutonomousDbVersionSummary.
        :rtype: bool
        """
        return self._is_default_for_paid

    @is_default_for_paid.setter
    def is_default_for_paid(self, is_default_for_paid):
        """
        Sets the is_default_for_paid of this AutonomousDbVersionSummary.
        True if this version of the Oracle Database software's default is paid.


        :param is_default_for_paid: The is_default_for_paid of this AutonomousDbVersionSummary.
        :type: bool
        """
        self._is_default_for_paid = is_default_for_paid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
