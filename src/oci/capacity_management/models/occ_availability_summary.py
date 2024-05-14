# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccAvailabilitySummary(object):
    """
    The details about the available capacity and constraints for different resource types present in the availability catalog.
    """

    #: A constant which can be used with the namespace property of a OccAvailabilitySummary.
    #: This constant has a value of "COMPUTE"
    NAMESPACE_COMPUTE = "COMPUTE"

    #: A constant which can be used with the resource_type property of a OccAvailabilitySummary.
    #: This constant has a value of "SERVER_HW"
    RESOURCE_TYPE_SERVER_HW = "SERVER_HW"

    #: A constant which can be used with the resource_type property of a OccAvailabilitySummary.
    #: This constant has a value of "CAPACITY_CONSTRAINT"
    RESOURCE_TYPE_CAPACITY_CONSTRAINT = "CAPACITY_CONSTRAINT"

    #: A constant which can be used with the workload_type property of a OccAvailabilitySummary.
    #: This constant has a value of "GENERIC"
    WORKLOAD_TYPE_GENERIC = "GENERIC"

    #: A constant which can be used with the workload_type property of a OccAvailabilitySummary.
    #: This constant has a value of "ROW"
    WORKLOAD_TYPE_ROW = "ROW"

    #: A constant which can be used with the workload_type property of a OccAvailabilitySummary.
    #: This constant has a value of "US_PROD"
    WORKLOAD_TYPE_US_PROD = "US_PROD"

    def __init__(self, **kwargs):
        """
        Initializes a new OccAvailabilitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param catalog_id:
            The value to assign to the catalog_id property of this OccAvailabilitySummary.
        :type catalog_id: str

        :param namespace:
            The value to assign to the namespace property of this OccAvailabilitySummary.
            Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type namespace: str

        :param date_final_customer_order:
            The value to assign to the date_final_customer_order property of this OccAvailabilitySummary.
        :type date_final_customer_order: datetime

        :param date_expected_capacity_handover:
            The value to assign to the date_expected_capacity_handover property of this OccAvailabilitySummary.
        :type date_expected_capacity_handover: datetime

        :param resource_type:
            The value to assign to the resource_type property of this OccAvailabilitySummary.
            Allowed values for this property are: "SERVER_HW", "CAPACITY_CONSTRAINT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param workload_type:
            The value to assign to the workload_type property of this OccAvailabilitySummary.
            Allowed values for this property are: "GENERIC", "ROW", "US_PROD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type workload_type: str

        :param resource_name:
            The value to assign to the resource_name property of this OccAvailabilitySummary.
        :type resource_name: str

        :param available_quantity:
            The value to assign to the available_quantity property of this OccAvailabilitySummary.
        :type available_quantity: int

        :param unit:
            The value to assign to the unit property of this OccAvailabilitySummary.
        :type unit: str

        """
        self.swagger_types = {
            'catalog_id': 'str',
            'namespace': 'str',
            'date_final_customer_order': 'datetime',
            'date_expected_capacity_handover': 'datetime',
            'resource_type': 'str',
            'workload_type': 'str',
            'resource_name': 'str',
            'available_quantity': 'int',
            'unit': 'str'
        }

        self.attribute_map = {
            'catalog_id': 'catalogId',
            'namespace': 'namespace',
            'date_final_customer_order': 'dateFinalCustomerOrder',
            'date_expected_capacity_handover': 'dateExpectedCapacityHandover',
            'resource_type': 'resourceType',
            'workload_type': 'workloadType',
            'resource_name': 'resourceName',
            'available_quantity': 'availableQuantity',
            'unit': 'unit'
        }

        self._catalog_id = None
        self._namespace = None
        self._date_final_customer_order = None
        self._date_expected_capacity_handover = None
        self._resource_type = None
        self._workload_type = None
        self._resource_name = None
        self._available_quantity = None
        self._unit = None

    @property
    def catalog_id(self):
        """
        **[Required]** Gets the catalog_id of this OccAvailabilitySummary.
        The OCID of the availability catalog.


        :return: The catalog_id of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this OccAvailabilitySummary.
        The OCID of the availability catalog.


        :param catalog_id: The catalog_id of this OccAvailabilitySummary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this OccAvailabilitySummary.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.

        Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The namespace of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OccAvailabilitySummary.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.


        :param namespace: The namespace of this OccAvailabilitySummary.
        :type: str
        """
        allowed_values = ["COMPUTE"]
        if not value_allowed_none_or_none_sentinel(namespace, allowed_values):
            namespace = 'UNKNOWN_ENUM_VALUE'
        self._namespace = namespace

    @property
    def date_final_customer_order(self):
        """
        **[Required]** Gets the date_final_customer_order of this OccAvailabilitySummary.
        The date by which the customer must place the order to have their capacity requirements met by the customer handover date.


        :return: The date_final_customer_order of this OccAvailabilitySummary.
        :rtype: datetime
        """
        return self._date_final_customer_order

    @date_final_customer_order.setter
    def date_final_customer_order(self, date_final_customer_order):
        """
        Sets the date_final_customer_order of this OccAvailabilitySummary.
        The date by which the customer must place the order to have their capacity requirements met by the customer handover date.


        :param date_final_customer_order: The date_final_customer_order of this OccAvailabilitySummary.
        :type: datetime
        """
        self._date_final_customer_order = date_final_customer_order

    @property
    def date_expected_capacity_handover(self):
        """
        **[Required]** Gets the date_expected_capacity_handover of this OccAvailabilitySummary.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :return: The date_expected_capacity_handover of this OccAvailabilitySummary.
        :rtype: datetime
        """
        return self._date_expected_capacity_handover

    @date_expected_capacity_handover.setter
    def date_expected_capacity_handover(self, date_expected_capacity_handover):
        """
        Sets the date_expected_capacity_handover of this OccAvailabilitySummary.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :param date_expected_capacity_handover: The date_expected_capacity_handover of this OccAvailabilitySummary.
        :type: datetime
        """
        self._date_expected_capacity_handover = date_expected_capacity_handover

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this OccAvailabilitySummary.
        The different types of resources against which customers can place capacity requests.

        Allowed values for this property are: "SERVER_HW", "CAPACITY_CONSTRAINT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this OccAvailabilitySummary.
        The different types of resources against which customers can place capacity requests.


        :param resource_type: The resource_type of this OccAvailabilitySummary.
        :type: str
        """
        allowed_values = ["SERVER_HW", "CAPACITY_CONSTRAINT"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def workload_type(self):
        """
        **[Required]** Gets the workload_type of this OccAvailabilitySummary.
        The type of workload (Generic/ROW).

        Allowed values for this property are: "GENERIC", "ROW", "US_PROD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The workload_type of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """
        Sets the workload_type of this OccAvailabilitySummary.
        The type of workload (Generic/ROW).


        :param workload_type: The workload_type of this OccAvailabilitySummary.
        :type: str
        """
        allowed_values = ["GENERIC", "ROW", "US_PROD"]
        if not value_allowed_none_or_none_sentinel(workload_type, allowed_values):
            workload_type = 'UNKNOWN_ENUM_VALUE'
        self._workload_type = workload_type

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this OccAvailabilitySummary.
        The name of the resource that the customer can request.


        :return: The resource_name of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this OccAvailabilitySummary.
        The name of the resource that the customer can request.


        :param resource_name: The resource_name of this OccAvailabilitySummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def available_quantity(self):
        """
        **[Required]** Gets the available_quantity of this OccAvailabilitySummary.
        The quantity of available resource that the customer can request.


        :return: The available_quantity of this OccAvailabilitySummary.
        :rtype: int
        """
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, available_quantity):
        """
        Sets the available_quantity of this OccAvailabilitySummary.
        The quantity of available resource that the customer can request.


        :param available_quantity: The available_quantity of this OccAvailabilitySummary.
        :type: int
        """
        self._available_quantity = available_quantity

    @property
    def unit(self):
        """
        **[Required]** Gets the unit of this OccAvailabilitySummary.
        The unit in which the resource available is measured.


        :return: The unit of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this OccAvailabilitySummary.
        The unit in which the resource available is measured.


        :param unit: The unit of this OccAvailabilitySummary.
        :type: str
        """
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
