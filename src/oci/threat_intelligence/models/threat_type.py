# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThreatType(object):
    """
    A threat type along with attribution data that associates it to a threat indicator.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ThreatType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ThreatType.
        :type id: str

        :param name:
            The value to assign to the name property of this ThreatType.
        :type name: str

        :param attribution:
            The value to assign to the attribution property of this ThreatType.
        :type attribution: list[oci.threat_intelligence.models.DataAttribution]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'attribution': 'list[DataAttribution]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'attribution': 'attribution'
        }

        self._id = None
        self._name = None
        self._attribution = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ThreatType.
        The OCID of the threat type.


        :return: The id of this ThreatType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ThreatType.
        The OCID of the threat type.


        :param id: The id of this ThreatType.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ThreatType.
        The name of the threat type.


        :return: The name of this ThreatType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ThreatType.
        The name of the threat type.


        :param name: The name of this ThreatType.
        :type: str
        """
        self._name = name

    @property
    def attribution(self):
        """
        **[Required]** Gets the attribution of this ThreatType.
        The list of supporting attribution information.


        :return: The attribution of this ThreatType.
        :rtype: list[oci.threat_intelligence.models.DataAttribution]
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """
        Sets the attribution of this ThreatType.
        The list of supporting attribution information.


        :param attribution: The attribution of this ThreatType.
        :type: list[oci.threat_intelligence.models.DataAttribution]
        """
        self._attribution = attribution

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
