# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeCapacityTopology(object):
    """
    A compute capacity topology that allows you to query your bare metal hosts and their RDMA network topology.
    """

    #: A constant which can be used with the lifecycle_state property of a ComputeCapacityTopology.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ComputeCapacityTopology.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ComputeCapacityTopology.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ComputeCapacityTopology.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ComputeCapacityTopology.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeCapacityTopology object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this ComputeCapacityTopology.
        :type availability_domain: str

        :param capacity_source:
            The value to assign to the capacity_source property of this ComputeCapacityTopology.
        :type capacity_source: oci.core.models.CapacitySource

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeCapacityTopology.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeCapacityTopology.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ComputeCapacityTopology.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeCapacityTopology.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this ComputeCapacityTopology.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeCapacityTopology.
            Allowed values for this property are: "ACTIVE", "CREATING", "UPDATING", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ComputeCapacityTopology.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputeCapacityTopology.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'capacity_source': 'CapacitySource',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'capacity_source': 'capacitySource',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._availability_domain = None
        self._capacity_source = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ComputeCapacityTopology.
        The availability domain of the compute capacity topology.

        Example: `Uocm:US-CHICAGO-1-AD-2`


        :return: The availability_domain of this ComputeCapacityTopology.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ComputeCapacityTopology.
        The availability domain of the compute capacity topology.

        Example: `Uocm:US-CHICAGO-1-AD-2`


        :param availability_domain: The availability_domain of this ComputeCapacityTopology.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def capacity_source(self):
        """
        **[Required]** Gets the capacity_source of this ComputeCapacityTopology.

        :return: The capacity_source of this ComputeCapacityTopology.
        :rtype: oci.core.models.CapacitySource
        """
        return self._capacity_source

    @capacity_source.setter
    def capacity_source(self, capacity_source):
        """
        Sets the capacity_source of this ComputeCapacityTopology.

        :param capacity_source: The capacity_source of this ComputeCapacityTopology.
        :type: oci.core.models.CapacitySource
        """
        self._capacity_source = capacity_source

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ComputeCapacityTopology.
        The `OCID`__ of the compartment that contains the compute capacity topology.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ComputeCapacityTopology.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ComputeCapacityTopology.
        The `OCID`__ of the compartment that contains the compute capacity topology.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ComputeCapacityTopology.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ComputeCapacityTopology.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ComputeCapacityTopology.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ComputeCapacityTopology.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ComputeCapacityTopology.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this ComputeCapacityTopology.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ComputeCapacityTopology.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ComputeCapacityTopology.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ComputeCapacityTopology.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ComputeCapacityTopology.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ComputeCapacityTopology.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ComputeCapacityTopology.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ComputeCapacityTopology.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ComputeCapacityTopology.
        The `OCID`__ of the compute capacity topology.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ComputeCapacityTopology.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComputeCapacityTopology.
        The `OCID`__ of the compute capacity topology.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ComputeCapacityTopology.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ComputeCapacityTopology.
        The current state of the compute capacity topology.

        Allowed values for this property are: "ACTIVE", "CREATING", "UPDATING", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ComputeCapacityTopology.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ComputeCapacityTopology.
        The current state of the compute capacity topology.


        :param lifecycle_state: The lifecycle_state of this ComputeCapacityTopology.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "UPDATING", "DELETED", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ComputeCapacityTopology.
        The date and time that the compute capacity topology was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ComputeCapacityTopology.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputeCapacityTopology.
        The date and time that the compute capacity topology was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ComputeCapacityTopology.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ComputeCapacityTopology.
        The date and time that the compute capacity topology was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ComputeCapacityTopology.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ComputeCapacityTopology.
        The date and time that the compute capacity topology was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ComputeCapacityTopology.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
