# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedDatabaseDetails(object):
    """
    Databases associated with a backup destination
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssociatedDatabaseDetails.
        :type id: str

        :param db_name:
            The value to assign to the db_name property of this AssociatedDatabaseDetails.
        :type db_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'db_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'db_name': 'dbName'
        }

        self._id = None
        self._db_name = None

    @property
    def id(self):
        """
        Gets the id of this AssociatedDatabaseDetails.
        The database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AssociatedDatabaseDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssociatedDatabaseDetails.
        The database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AssociatedDatabaseDetails.
        :type: str
        """
        self._id = id

    @property
    def db_name(self):
        """
        Gets the db_name of this AssociatedDatabaseDetails.
        The display name of the database that is associated with the backup destination.


        :return: The db_name of this AssociatedDatabaseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this AssociatedDatabaseDetails.
        The display name of the database that is associated with the backup destination.


        :param db_name: The db_name of this AssociatedDatabaseDetails.
        :type: str
        """
        self._db_name = db_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
