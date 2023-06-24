# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConsoleConnectionSummary(object):
    """
    The `InstanceConsoleConnection` API provides you with console access to dbnode
    enabling you to troubleshoot malfunctioning dbnode.
    """

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ConsoleConnectionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConsoleConnectionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConsoleConnectionSummary.
        :type compartment_id: str

        :param db_node_id:
            The value to assign to the db_node_id property of this ConsoleConnectionSummary.
        :type db_node_id: str

        :param connection_string:
            The value to assign to the connection_string property of this ConsoleConnectionSummary.
        :type connection_string: str

        :param fingerprint:
            The value to assign to the fingerprint property of this ConsoleConnectionSummary.
        :type fingerprint: str

        :param service_host_key_fingerprint:
            The value to assign to the service_host_key_fingerprint property of this ConsoleConnectionSummary.
        :type service_host_key_fingerprint: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConsoleConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ConsoleConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ConsoleConnectionSummary.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConsoleConnectionSummary.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_node_id': 'str',
            'connection_string': 'str',
            'fingerprint': 'str',
            'service_host_key_fingerprint': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_node_id': 'dbNodeId',
            'connection_string': 'connectionString',
            'fingerprint': 'fingerprint',
            'service_host_key_fingerprint': 'serviceHostKeyFingerprint',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._db_node_id = None
        self._connection_string = None
        self._fingerprint = None
        self._service_host_key_fingerprint = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_details = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConsoleConnectionSummary.
        The OCID of the console connection.


        :return: The id of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConsoleConnectionSummary.
        The OCID of the console connection.


        :param id: The id of this ConsoleConnectionSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConsoleConnectionSummary.
        The OCID of the compartment to contain the console connection.


        :return: The compartment_id of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConsoleConnectionSummary.
        The OCID of the compartment to contain the console connection.


        :param compartment_id: The compartment_id of this ConsoleConnectionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_node_id(self):
        """
        **[Required]** Gets the db_node_id of this ConsoleConnectionSummary.
        The OCID of the database node.


        :return: The db_node_id of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._db_node_id

    @db_node_id.setter
    def db_node_id(self, db_node_id):
        """
        Sets the db_node_id of this ConsoleConnectionSummary.
        The OCID of the database node.


        :param db_node_id: The db_node_id of this ConsoleConnectionSummary.
        :type: str
        """
        self._db_node_id = db_node_id

    @property
    def connection_string(self):
        """
        **[Required]** Gets the connection_string of this ConsoleConnectionSummary.
        The SSH connection string for the console connection.


        :return: The connection_string of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this ConsoleConnectionSummary.
        The SSH connection string for the console connection.


        :param connection_string: The connection_string of this ConsoleConnectionSummary.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def fingerprint(self):
        """
        **[Required]** Gets the fingerprint of this ConsoleConnectionSummary.
        The SSH public key fingerprint for the console connection.


        :return: The fingerprint of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this ConsoleConnectionSummary.
        The SSH public key fingerprint for the console connection.


        :param fingerprint: The fingerprint of this ConsoleConnectionSummary.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def service_host_key_fingerprint(self):
        """
        Gets the service_host_key_fingerprint of this ConsoleConnectionSummary.
        The SSH public key's fingerprint for the console connection service host.


        :return: The service_host_key_fingerprint of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._service_host_key_fingerprint

    @service_host_key_fingerprint.setter
    def service_host_key_fingerprint(self, service_host_key_fingerprint):
        """
        Sets the service_host_key_fingerprint of this ConsoleConnectionSummary.
        The SSH public key's fingerprint for the console connection service host.


        :param service_host_key_fingerprint: The service_host_key_fingerprint of this ConsoleConnectionSummary.
        :type: str
        """
        self._service_host_key_fingerprint = service_host_key_fingerprint

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConsoleConnectionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ConsoleConnectionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConsoleConnectionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ConsoleConnectionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConsoleConnectionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ConsoleConnectionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConsoleConnectionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ConsoleConnectionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ConsoleConnectionSummary.
        Information about the current lifecycle state.


        :return: The lifecycle_details of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ConsoleConnectionSummary.
        Information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ConsoleConnectionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConsoleConnectionSummary.
        The current state of the console connection.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConsoleConnectionSummary.
        The current state of the console connection.


        :param lifecycle_state: The lifecycle_state of this ConsoleConnectionSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
