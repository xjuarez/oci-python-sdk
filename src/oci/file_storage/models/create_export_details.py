# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExportDetails(object):
    """
    Details for creating the export.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_options:
            The value to assign to the export_options property of this CreateExportDetails.
        :type export_options: list[oci.file_storage.models.ClientOptions]

        :param export_set_id:
            The value to assign to the export_set_id property of this CreateExportDetails.
        :type export_set_id: str

        :param file_system_id:
            The value to assign to the file_system_id property of this CreateExportDetails.
        :type file_system_id: str

        :param path:
            The value to assign to the path property of this CreateExportDetails.
        :type path: str

        :param locks:
            The value to assign to the locks property of this CreateExportDetails.
        :type locks: list[oci.file_storage.models.ResourceLock]

        :param is_idmap_groups_for_sys_auth:
            The value to assign to the is_idmap_groups_for_sys_auth property of this CreateExportDetails.
        :type is_idmap_groups_for_sys_auth: bool

        """
        self.swagger_types = {
            'export_options': 'list[ClientOptions]',
            'export_set_id': 'str',
            'file_system_id': 'str',
            'path': 'str',
            'locks': 'list[ResourceLock]',
            'is_idmap_groups_for_sys_auth': 'bool'
        }

        self.attribute_map = {
            'export_options': 'exportOptions',
            'export_set_id': 'exportSetId',
            'file_system_id': 'fileSystemId',
            'path': 'path',
            'locks': 'locks',
            'is_idmap_groups_for_sys_auth': 'isIdmapGroupsForSysAuth'
        }

        self._export_options = None
        self._export_set_id = None
        self._file_system_id = None
        self._path = None
        self._locks = None
        self._is_idmap_groups_for_sys_auth = None

    @property
    def export_options(self):
        """
        Gets the export_options of this CreateExportDetails.
        Export options for the new export. For exports of mount targets with
        IPv4 address, if client options are left unspecified, client options
        would default to:

               [
                 {
                    \"source\" : \"0.0.0.0/0\",
                    \"requirePrivilegedSourcePort\" : false,
                    \"access\": \"READ_WRITE\",
                    \"identitySquash\": \"NONE\",
                    \"anonymousUid\": 65534,
                    \"anonymousGid\": 65534,
                    \"isAnonymousAccessAllowed\": false,
                    \"allowedAuth\": [\"SYS\"]
                  }
               ]

          For exports of mount targets with IPv6 address, if client options are
          left unspecified, client options would be an empty array, i.e. export
          would not be visible to any clients.

          **Note:** Mount targets do not have Internet-routable IP
          addresses.  Therefore they will not be reachable from the
          Internet, even if an associated `ClientOptions` item has
          a source of `0.0.0.0/0`.

          **If set to the empty array then the export will not be
          visible to any clients.**

          The export's `exportOptions` can be changed after creation
          using the `UpdateExport` operation.


        :return: The export_options of this CreateExportDetails.
        :rtype: list[oci.file_storage.models.ClientOptions]
        """
        return self._export_options

    @export_options.setter
    def export_options(self, export_options):
        """
        Sets the export_options of this CreateExportDetails.
        Export options for the new export. For exports of mount targets with
        IPv4 address, if client options are left unspecified, client options
        would default to:

               [
                 {
                    \"source\" : \"0.0.0.0/0\",
                    \"requirePrivilegedSourcePort\" : false,
                    \"access\": \"READ_WRITE\",
                    \"identitySquash\": \"NONE\",
                    \"anonymousUid\": 65534,
                    \"anonymousGid\": 65534,
                    \"isAnonymousAccessAllowed\": false,
                    \"allowedAuth\": [\"SYS\"]
                  }
               ]

          For exports of mount targets with IPv6 address, if client options are
          left unspecified, client options would be an empty array, i.e. export
          would not be visible to any clients.

          **Note:** Mount targets do not have Internet-routable IP
          addresses.  Therefore they will not be reachable from the
          Internet, even if an associated `ClientOptions` item has
          a source of `0.0.0.0/0`.

          **If set to the empty array then the export will not be
          visible to any clients.**

          The export's `exportOptions` can be changed after creation
          using the `UpdateExport` operation.


        :param export_options: The export_options of this CreateExportDetails.
        :type: list[oci.file_storage.models.ClientOptions]
        """
        self._export_options = export_options

    @property
    def export_set_id(self):
        """
        **[Required]** Gets the export_set_id of this CreateExportDetails.
        The `OCID`__ of this export's export set.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The export_set_id of this CreateExportDetails.
        :rtype: str
        """
        return self._export_set_id

    @export_set_id.setter
    def export_set_id(self, export_set_id):
        """
        Sets the export_set_id of this CreateExportDetails.
        The `OCID`__ of this export's export set.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param export_set_id: The export_set_id of this CreateExportDetails.
        :type: str
        """
        self._export_set_id = export_set_id

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this CreateExportDetails.
        The `OCID`__ of this export's file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The file_system_id of this CreateExportDetails.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this CreateExportDetails.
        The `OCID`__ of this export's file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param file_system_id: The file_system_id of this CreateExportDetails.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def path(self):
        """
        **[Required]** Gets the path of this CreateExportDetails.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/mediafiles`


        :return: The path of this CreateExportDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this CreateExportDetails.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/mediafiles`


        :param path: The path of this CreateExportDetails.
        :type: str
        """
        self._path = path

    @property
    def locks(self):
        """
        Gets the locks of this CreateExportDetails.
        Locks associated with this resource.


        :return: The locks of this CreateExportDetails.
        :rtype: list[oci.file_storage.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this CreateExportDetails.
        Locks associated with this resource.


        :param locks: The locks of this CreateExportDetails.
        :type: list[oci.file_storage.models.ResourceLock]
        """
        self._locks = locks

    @property
    def is_idmap_groups_for_sys_auth(self):
        """
        Gets the is_idmap_groups_for_sys_auth of this CreateExportDetails.
        Whether or not the export should use ID mapping for Unix groups rather than the group list provided within an NFS request's RPC header. When this flag is true the Unix UID from the RPC header is used to retrieve the list of secondary groups from a the ID mapping subsystem. The primary GID is always taken from the RPC header. If ID mapping is not configured, incorrectly configured, unavailable, or cannot be used to determine a list of secondary groups then an empty secondary group list is used for authorization. If the number of groups exceeds the limit of 256 groups, the list retrieved from LDAP is truncated to the first 256 groups read.


        :return: The is_idmap_groups_for_sys_auth of this CreateExportDetails.
        :rtype: bool
        """
        return self._is_idmap_groups_for_sys_auth

    @is_idmap_groups_for_sys_auth.setter
    def is_idmap_groups_for_sys_auth(self, is_idmap_groups_for_sys_auth):
        """
        Sets the is_idmap_groups_for_sys_auth of this CreateExportDetails.
        Whether or not the export should use ID mapping for Unix groups rather than the group list provided within an NFS request's RPC header. When this flag is true the Unix UID from the RPC header is used to retrieve the list of secondary groups from a the ID mapping subsystem. The primary GID is always taken from the RPC header. If ID mapping is not configured, incorrectly configured, unavailable, or cannot be used to determine a list of secondary groups then an empty secondary group list is used for authorization. If the number of groups exceeds the limit of 256 groups, the list retrieved from LDAP is truncated to the first 256 groups read.


        :param is_idmap_groups_for_sys_auth: The is_idmap_groups_for_sys_auth of this CreateExportDetails.
        :type: bool
        """
        self._is_idmap_groups_for_sys_auth = is_idmap_groups_for_sys_auth

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
