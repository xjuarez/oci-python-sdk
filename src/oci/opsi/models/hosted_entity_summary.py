# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostedEntitySummary(object):
    """
    Information about a hosted entity which includes identifier, name, and type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostedEntitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_identifier:
            The value to assign to the entity_identifier property of this HostedEntitySummary.
        :type entity_identifier: str

        :param entity_name:
            The value to assign to the entity_name property of this HostedEntitySummary.
        :type entity_name: str

        :param entity_type:
            The value to assign to the entity_type property of this HostedEntitySummary.
        :type entity_type: str

        """
        self.swagger_types = {
            'entity_identifier': 'str',
            'entity_name': 'str',
            'entity_type': 'str'
        }

        self.attribute_map = {
            'entity_identifier': 'entityIdentifier',
            'entity_name': 'entityName',
            'entity_type': 'entityType'
        }

        self._entity_identifier = None
        self._entity_name = None
        self._entity_type = None

    @property
    def entity_identifier(self):
        """
        **[Required]** Gets the entity_identifier of this HostedEntitySummary.
        The identifier of the entity.


        :return: The entity_identifier of this HostedEntitySummary.
        :rtype: str
        """
        return self._entity_identifier

    @entity_identifier.setter
    def entity_identifier(self, entity_identifier):
        """
        Sets the entity_identifier of this HostedEntitySummary.
        The identifier of the entity.


        :param entity_identifier: The entity_identifier of this HostedEntitySummary.
        :type: str
        """
        self._entity_identifier = entity_identifier

    @property
    def entity_name(self):
        """
        **[Required]** Gets the entity_name of this HostedEntitySummary.
        The entity name.


        :return: The entity_name of this HostedEntitySummary.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this HostedEntitySummary.
        The entity name.


        :param entity_name: The entity_name of this HostedEntitySummary.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this HostedEntitySummary.
        The entity type.


        :return: The entity_type of this HostedEntitySummary.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HostedEntitySummary.
        The entity type.


        :param entity_type: The entity_type of this HostedEntitySummary.
        :type: str
        """
        self._entity_type = entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
