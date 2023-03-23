# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateHdfsConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a Hadoop Distributed File System Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateHdfsConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateHdfsConnectionDetails.connection_type` attribute
        of this class is ``HDFS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateHdfsConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateHdfsConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateHdfsConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateHdfsConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateHdfsConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateHdfsConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateHdfsConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateHdfsConnectionDetails.
        :type nsg_ids: list[str]

        :param core_site_xml:
            The value to assign to the core_site_xml property of this UpdateHdfsConnectionDetails.
        :type core_site_xml: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'core_site_xml': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'core_site_xml': 'coreSiteXml'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._core_site_xml = None
        self._connection_type = 'HDFS'

    @property
    def core_site_xml(self):
        """
        Gets the core_site_xml of this UpdateHdfsConnectionDetails.
        The base64 encoded content of the Hadoop Distributed File System configuration file (core-site.xml).


        :return: The core_site_xml of this UpdateHdfsConnectionDetails.
        :rtype: str
        """
        return self._core_site_xml

    @core_site_xml.setter
    def core_site_xml(self, core_site_xml):
        """
        Sets the core_site_xml of this UpdateHdfsConnectionDetails.
        The base64 encoded content of the Hadoop Distributed File System configuration file (core-site.xml).


        :param core_site_xml: The core_site_xml of this UpdateHdfsConnectionDetails.
        :type: str
        """
        self._core_site_xml = core_site_xml

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
