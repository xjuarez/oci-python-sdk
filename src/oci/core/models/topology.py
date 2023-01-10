# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Topology(object):
    """
    Defines the representation of a virtual network topology.
    """

    #: A constant which can be used with the type property of a Topology.
    #: This constant has a value of "NETWORKING"
    TYPE_NETWORKING = "NETWORKING"

    #: A constant which can be used with the type property of a Topology.
    #: This constant has a value of "VCN"
    TYPE_VCN = "VCN"

    #: A constant which can be used with the type property of a Topology.
    #: This constant has a value of "SUBNET"
    TYPE_SUBNET = "SUBNET"

    #: A constant which can be used with the type property of a Topology.
    #: This constant has a value of "PATH"
    TYPE_PATH = "PATH"

    def __init__(self, **kwargs):
        """
        Initializes a new Topology object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.VcnTopology`
        * :class:`~oci.core.models.NetworkingTopology`
        * :class:`~oci.core.models.SubnetTopology`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Topology.
            Allowed values for this property are: "NETWORKING", "VCN", "SUBNET", "PATH"
        :type type: str

        :param entities:
            The value to assign to the entities property of this Topology.
        :type entities: list[object]

        :param relationships:
            The value to assign to the relationships property of this Topology.
        :type relationships: list[oci.core.models.TopologyEntityRelationship]

        :param time_created:
            The value to assign to the time_created property of this Topology.
        :type time_created: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'entities': 'list[object]',
            'relationships': 'list[TopologyEntityRelationship]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'entities': 'entities',
            'relationships': 'relationships',
            'time_created': 'timeCreated'
        }

        self._type = None
        self._entities = None
        self._relationships = None
        self._time_created = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VCN':
            return 'VcnTopology'

        if type == 'NETWORKING':
            return 'NetworkingTopology'

        if type == 'SUBNET':
            return 'SubnetTopology'
        else:
            return 'Topology'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Topology.
        Type of the topology object.

        Allowed values for this property are: "NETWORKING", "VCN", "SUBNET", "PATH"


        :return: The type of this Topology.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Topology.
        Type of the topology object.


        :param type: The type of this Topology.
        :type: str
        """
        allowed_values = ["NETWORKING", "VCN", "SUBNET", "PATH"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def entities(self):
        """
        **[Required]** Gets the entities of this Topology.
        Lists entities comprising the virtual network topology.


        :return: The entities of this Topology.
        :rtype: list[object]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this Topology.
        Lists entities comprising the virtual network topology.


        :param entities: The entities of this Topology.
        :type: list[object]
        """
        self._entities = entities

    @property
    def relationships(self):
        """
        **[Required]** Gets the relationships of this Topology.
        Lists relationships between entities in the virtual network topology.


        :return: The relationships of this Topology.
        :rtype: list[oci.core.models.TopologyEntityRelationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this Topology.
        Lists relationships between entities in the virtual network topology.


        :param relationships: The relationships of this Topology.
        :type: list[oci.core.models.TopologyEntityRelationship]
        """
        self._relationships = relationships

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Topology.
        Records when the virtual network topology was created, in `RFC3339`__ format for date and time.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Topology.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Topology.
        Records when the virtual network topology was created, in `RFC3339`__ format for date and time.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Topology.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
