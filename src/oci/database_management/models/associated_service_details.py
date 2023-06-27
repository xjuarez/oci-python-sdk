# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedServiceDetails(object):
    """
    The details of the associated service that will be enabled or disabled for an external DB System.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedServiceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this AssociatedServiceDetails.
        :type is_enabled: bool

        :param metadata:
            The value to assign to the metadata property of this AssociatedServiceDetails.
        :type metadata: str

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'metadata': 'str'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'metadata': 'metadata'
        }

        self._is_enabled = None
        self._metadata = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this AssociatedServiceDetails.
        The status of the associated service.


        :return: The is_enabled of this AssociatedServiceDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AssociatedServiceDetails.
        The status of the associated service.


        :param is_enabled: The is_enabled of this AssociatedServiceDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def metadata(self):
        """
        Gets the metadata of this AssociatedServiceDetails.
        The associated service-specific inputs in JSON string format, which Database Management can identify.


        :return: The metadata of this AssociatedServiceDetails.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this AssociatedServiceDetails.
        The associated service-specific inputs in JSON string format, which Database Management can identify.


        :param metadata: The metadata of this AssociatedServiceDetails.
        :type: str
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
