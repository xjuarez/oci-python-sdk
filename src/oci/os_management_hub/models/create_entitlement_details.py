# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEntitlementDetails(object):
    """
    Creates an entitlement for the specified compartment OCID and CSI.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEntitlementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEntitlementDetails.
        :type compartment_id: str

        :param csi:
            The value to assign to the csi property of this CreateEntitlementDetails.
        :type csi: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'csi': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'csi': 'csi'
        }

        self._compartment_id = None
        self._csi = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateEntitlementDetails.
        The OCID of the tenancy containing the entitlement.


        :return: The compartment_id of this CreateEntitlementDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateEntitlementDetails.
        The OCID of the tenancy containing the entitlement.


        :param compartment_id: The compartment_id of this CreateEntitlementDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def csi(self):
        """
        **[Required]** Gets the csi of this CreateEntitlementDetails.
        A Customer Support Identifier (CSI) is a unique key given to a customer to unlock software sources. It uniquely identifies the entitlement.


        :return: The csi of this CreateEntitlementDetails.
        :rtype: str
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """
        Sets the csi of this CreateEntitlementDetails.
        A Customer Support Identifier (CSI) is a unique key given to a customer to unlock software sources. It uniquely identifies the entitlement.


        :param csi: The csi of this CreateEntitlementDetails.
        :type: str
        """
        self._csi = csi

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
