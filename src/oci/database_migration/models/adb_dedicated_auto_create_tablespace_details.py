# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_type_tablespace_details import TargetTypeTablespaceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ADBDedicatedAutoCreateTablespaceDetails(TargetTypeTablespaceDetails):
    """
    Migration tablespace settings valid for ADB-D target type using auto create feature
    """

    #: A constant which can be used with the block_size_in_kbs property of a ADBDedicatedAutoCreateTablespaceDetails.
    #: This constant has a value of "SIZE_8K"
    BLOCK_SIZE_IN_KBS_SIZE_8_K = "SIZE_8K"

    #: A constant which can be used with the block_size_in_kbs property of a ADBDedicatedAutoCreateTablespaceDetails.
    #: This constant has a value of "SIZE_16K"
    BLOCK_SIZE_IN_KBS_SIZE_16_K = "SIZE_16K"

    def __init__(self, **kwargs):
        """
        Initializes a new ADBDedicatedAutoCreateTablespaceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.ADBDedicatedAutoCreateTablespaceDetails.target_type` attribute
        of this class is ``ADB_D_AUTOCREATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this ADBDedicatedAutoCreateTablespaceDetails.
            Allowed values for this property are: "ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_type: str

        :param is_auto_create:
            The value to assign to the is_auto_create property of this ADBDedicatedAutoCreateTablespaceDetails.
        :type is_auto_create: bool

        :param is_big_file:
            The value to assign to the is_big_file property of this ADBDedicatedAutoCreateTablespaceDetails.
        :type is_big_file: bool

        :param extend_size_in_mbs:
            The value to assign to the extend_size_in_mbs property of this ADBDedicatedAutoCreateTablespaceDetails.
        :type extend_size_in_mbs: int

        :param block_size_in_kbs:
            The value to assign to the block_size_in_kbs property of this ADBDedicatedAutoCreateTablespaceDetails.
            Allowed values for this property are: "SIZE_8K", "SIZE_16K", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type block_size_in_kbs: str

        """
        self.swagger_types = {
            'target_type': 'str',
            'is_auto_create': 'bool',
            'is_big_file': 'bool',
            'extend_size_in_mbs': 'int',
            'block_size_in_kbs': 'str'
        }

        self.attribute_map = {
            'target_type': 'targetType',
            'is_auto_create': 'isAutoCreate',
            'is_big_file': 'isBigFile',
            'extend_size_in_mbs': 'extendSizeInMBs',
            'block_size_in_kbs': 'blockSizeInKBs'
        }

        self._target_type = None
        self._is_auto_create = None
        self._is_big_file = None
        self._extend_size_in_mbs = None
        self._block_size_in_kbs = None
        self._target_type = 'ADB_D_AUTOCREATE'

    @property
    def is_auto_create(self):
        """
        Gets the is_auto_create of this ADBDedicatedAutoCreateTablespaceDetails.
        True to auto-create tablespace in the target Database.


        :return: The is_auto_create of this ADBDedicatedAutoCreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_auto_create

    @is_auto_create.setter
    def is_auto_create(self, is_auto_create):
        """
        Sets the is_auto_create of this ADBDedicatedAutoCreateTablespaceDetails.
        True to auto-create tablespace in the target Database.


        :param is_auto_create: The is_auto_create of this ADBDedicatedAutoCreateTablespaceDetails.
        :type: bool
        """
        self._is_auto_create = is_auto_create

    @property
    def is_big_file(self):
        """
        Gets the is_big_file of this ADBDedicatedAutoCreateTablespaceDetails.
        True set tablespace to big file.


        :return: The is_big_file of this ADBDedicatedAutoCreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_big_file

    @is_big_file.setter
    def is_big_file(self, is_big_file):
        """
        Sets the is_big_file of this ADBDedicatedAutoCreateTablespaceDetails.
        True set tablespace to big file.


        :param is_big_file: The is_big_file of this ADBDedicatedAutoCreateTablespaceDetails.
        :type: bool
        """
        self._is_big_file = is_big_file

    @property
    def extend_size_in_mbs(self):
        """
        Gets the extend_size_in_mbs of this ADBDedicatedAutoCreateTablespaceDetails.
        Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.


        :return: The extend_size_in_mbs of this ADBDedicatedAutoCreateTablespaceDetails.
        :rtype: int
        """
        return self._extend_size_in_mbs

    @extend_size_in_mbs.setter
    def extend_size_in_mbs(self, extend_size_in_mbs):
        """
        Sets the extend_size_in_mbs of this ADBDedicatedAutoCreateTablespaceDetails.
        Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.


        :param extend_size_in_mbs: The extend_size_in_mbs of this ADBDedicatedAutoCreateTablespaceDetails.
        :type: int
        """
        self._extend_size_in_mbs = extend_size_in_mbs

    @property
    def block_size_in_kbs(self):
        """
        Gets the block_size_in_kbs of this ADBDedicatedAutoCreateTablespaceDetails.
        Size of Oracle database blocks in KB.

        Allowed values for this property are: "SIZE_8K", "SIZE_16K", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The block_size_in_kbs of this ADBDedicatedAutoCreateTablespaceDetails.
        :rtype: str
        """
        return self._block_size_in_kbs

    @block_size_in_kbs.setter
    def block_size_in_kbs(self, block_size_in_kbs):
        """
        Sets the block_size_in_kbs of this ADBDedicatedAutoCreateTablespaceDetails.
        Size of Oracle database blocks in KB.


        :param block_size_in_kbs: The block_size_in_kbs of this ADBDedicatedAutoCreateTablespaceDetails.
        :type: str
        """
        allowed_values = ["SIZE_8K", "SIZE_16K"]
        if not value_allowed_none_or_none_sentinel(block_size_in_kbs, allowed_values):
            block_size_in_kbs = 'UNKNOWN_ENUM_VALUE'
        self._block_size_in_kbs = block_size_in_kbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
