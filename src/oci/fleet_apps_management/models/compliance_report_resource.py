# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComplianceReportResource(object):
    """
    Details of the Resource
    """

    #: A constant which can be used with the compliance_state property of a ComplianceReportResource.
    #: This constant has a value of "UNKNOWN"
    COMPLIANCE_STATE_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the compliance_state property of a ComplianceReportResource.
    #: This constant has a value of "COMPLIANT"
    COMPLIANCE_STATE_COMPLIANT = "COMPLIANT"

    #: A constant which can be used with the compliance_state property of a ComplianceReportResource.
    #: This constant has a value of "NON_COMPLIANT"
    COMPLIANCE_STATE_NON_COMPLIANT = "NON_COMPLIANT"

    #: A constant which can be used with the compliance_state property of a ComplianceReportResource.
    #: This constant has a value of "WARNING"
    COMPLIANCE_STATE_WARNING = "WARNING"

    def __init__(self, **kwargs):
        """
        Initializes a new ComplianceReportResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this ComplianceReportResource.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this ComplianceReportResource.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this ComplianceReportResource.
        :type resource_type: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this ComplianceReportResource.
        :type tenancy_id: str

        :param tenancy_name:
            The value to assign to the tenancy_name property of this ComplianceReportResource.
        :type tenancy_name: str

        :param compartment:
            The value to assign to the compartment property of this ComplianceReportResource.
        :type compartment: str

        :param resource_region:
            The value to assign to the resource_region property of this ComplianceReportResource.
        :type resource_region: str

        :param compliance_state:
            The value to assign to the compliance_state property of this ComplianceReportResource.
            Allowed values for this property are: "UNKNOWN", "COMPLIANT", "NON_COMPLIANT", "WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type compliance_state: str

        :param products:
            The value to assign to the products property of this ComplianceReportResource.
        :type products: list[oci.fleet_apps_management.models.ComplianceReportProduct]

        """
        self.swagger_types = {
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'tenancy_id': 'str',
            'tenancy_name': 'str',
            'compartment': 'str',
            'resource_region': 'str',
            'compliance_state': 'str',
            'products': 'list[ComplianceReportProduct]'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'tenancy_id': 'tenancyId',
            'tenancy_name': 'tenancyName',
            'compartment': 'compartment',
            'resource_region': 'resourceRegion',
            'compliance_state': 'complianceState',
            'products': 'products'
        }

        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._tenancy_id = None
        self._tenancy_name = None
        self._compartment = None
        self._resource_region = None
        self._compliance_state = None
        self._products = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this ComplianceReportResource.
        The OCID to identify the resource.


        :return: The resource_id of this ComplianceReportResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ComplianceReportResource.
        The OCID to identify the resource.


        :param resource_id: The resource_id of this ComplianceReportResource.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this ComplianceReportResource.
        Display name of the resource.


        :return: The resource_name of this ComplianceReportResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this ComplianceReportResource.
        Display name of the resource.


        :param resource_name: The resource_name of this ComplianceReportResource.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this ComplianceReportResource.
        Type of the resource.


        :return: The resource_type of this ComplianceReportResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ComplianceReportResource.
        Type of the resource.


        :param resource_type: The resource_type of this ComplianceReportResource.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this ComplianceReportResource.
        TenancyId of the resource.


        :return: The tenancy_id of this ComplianceReportResource.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this ComplianceReportResource.
        TenancyId of the resource.


        :param tenancy_id: The tenancy_id of this ComplianceReportResource.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def tenancy_name(self):
        """
        Gets the tenancy_name of this ComplianceReportResource.
        Tenancy the resource belongs to.


        :return: The tenancy_name of this ComplianceReportResource.
        :rtype: str
        """
        return self._tenancy_name

    @tenancy_name.setter
    def tenancy_name(self, tenancy_name):
        """
        Sets the tenancy_name of this ComplianceReportResource.
        Tenancy the resource belongs to.


        :param tenancy_name: The tenancy_name of this ComplianceReportResource.
        :type: str
        """
        self._tenancy_name = tenancy_name

    @property
    def compartment(self):
        """
        Gets the compartment of this ComplianceReportResource.
        Compartment the resource belongs to.


        :return: The compartment of this ComplianceReportResource.
        :rtype: str
        """
        return self._compartment

    @compartment.setter
    def compartment(self, compartment):
        """
        Sets the compartment of this ComplianceReportResource.
        Compartment the resource belongs to.


        :param compartment: The compartment of this ComplianceReportResource.
        :type: str
        """
        self._compartment = compartment

    @property
    def resource_region(self):
        """
        Gets the resource_region of this ComplianceReportResource.
        The region the resource belongs to.


        :return: The resource_region of this ComplianceReportResource.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this ComplianceReportResource.
        The region the resource belongs to.


        :param resource_region: The resource_region of this ComplianceReportResource.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def compliance_state(self):
        """
        **[Required]** Gets the compliance_state of this ComplianceReportResource.
        The last known compliance state of the fleet.

        Allowed values for this property are: "UNKNOWN", "COMPLIANT", "NON_COMPLIANT", "WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The compliance_state of this ComplianceReportResource.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """
        Sets the compliance_state of this ComplianceReportResource.
        The last known compliance state of the fleet.


        :param compliance_state: The compliance_state of this ComplianceReportResource.
        :type: str
        """
        allowed_values = ["UNKNOWN", "COMPLIANT", "NON_COMPLIANT", "WARNING"]
        if not value_allowed_none_or_none_sentinel(compliance_state, allowed_values):
            compliance_state = 'UNKNOWN_ENUM_VALUE'
        self._compliance_state = compliance_state

    @property
    def products(self):
        """
        Gets the products of this ComplianceReportResource.
        Products associated with the Fleet.
        Only the products belonging to managed targets will be shown.


        :return: The products of this ComplianceReportResource.
        :rtype: list[oci.fleet_apps_management.models.ComplianceReportProduct]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this ComplianceReportResource.
        Products associated with the Fleet.
        Only the products belonging to managed targets will be shown.


        :param products: The products of this ComplianceReportResource.
        :type: list[oci.fleet_apps_management.models.ComplianceReportProduct]
        """
        self._products = products

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
