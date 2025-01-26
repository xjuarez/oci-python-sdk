# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .config_category_details import ConfigCategoryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProductConfigCategoryDetails(ConfigCategoryDetails):
    """
    Product Config Category Details.
    Defines individual products which contribute to the applications hosting on the resources that are to be managed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProductConfigCategoryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.ProductConfigCategoryDetails.config_category` attribute
        of this class is ``PRODUCT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_category:
            The value to assign to the config_category property of this ProductConfigCategoryDetails.
            Allowed values for this property are: "PRODUCT", "PRODUCT_STACK", "ENVIRONMENT", "PATCH_TYPE", "CREDENTIAL"
        :type config_category: str

        :param versions:
            The value to assign to the versions property of this ProductConfigCategoryDetails.
        :type versions: list[str]

        :param credentials:
            The value to assign to the credentials property of this ProductConfigCategoryDetails.
        :type credentials: list[oci.fleet_apps_management.models.ConfigAssociationDetails]

        :param components:
            The value to assign to the components property of this ProductConfigCategoryDetails.
        :type components: list[str]

        :param compatible_products:
            The value to assign to the compatible_products property of this ProductConfigCategoryDetails.
        :type compatible_products: list[oci.fleet_apps_management.models.ConfigAssociationDetails]

        :param patch_types:
            The value to assign to the patch_types property of this ProductConfigCategoryDetails.
        :type patch_types: list[oci.fleet_apps_management.models.ConfigAssociationDetails]

        """
        self.swagger_types = {
            'config_category': 'str',
            'versions': 'list[str]',
            'credentials': 'list[ConfigAssociationDetails]',
            'components': 'list[str]',
            'compatible_products': 'list[ConfigAssociationDetails]',
            'patch_types': 'list[ConfigAssociationDetails]'
        }

        self.attribute_map = {
            'config_category': 'configCategory',
            'versions': 'versions',
            'credentials': 'credentials',
            'components': 'components',
            'compatible_products': 'compatibleProducts',
            'patch_types': 'patchTypes'
        }

        self._config_category = None
        self._versions = None
        self._credentials = None
        self._components = None
        self._compatible_products = None
        self._patch_types = None
        self._config_category = 'PRODUCT'

    @property
    def versions(self):
        """
        **[Required]** Gets the versions of this ProductConfigCategoryDetails.
        Versions associated with the PRODUCT .


        :return: The versions of this ProductConfigCategoryDetails.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this ProductConfigCategoryDetails.
        Versions associated with the PRODUCT .


        :param versions: The versions of this ProductConfigCategoryDetails.
        :type: list[str]
        """
        self._versions = versions

    @property
    def credentials(self):
        """
        Gets the credentials of this ProductConfigCategoryDetails.
        OCID for the Credential name to be associated with the Product.
        These are useful for target discovery or lifecycle management activities, for example, Oracle WebLogic admin credentials for Oracle WebLogic Application server.


        :return: The credentials of this ProductConfigCategoryDetails.
        :rtype: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ProductConfigCategoryDetails.
        OCID for the Credential name to be associated with the Product.
        These are useful for target discovery or lifecycle management activities, for example, Oracle WebLogic admin credentials for Oracle WebLogic Application server.


        :param credentials: The credentials of this ProductConfigCategoryDetails.
        :type: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        self._credentials = credentials

    @property
    def components(self):
        """
        Gets the components of this ProductConfigCategoryDetails.
        Various components of the Product.
        For example:The administration server or node manager can be the components of the Oracle WebLogic Application server.
        Forms server or concurrent manager can be the components of the Oracle E-Business Suite.


        :return: The components of this ProductConfigCategoryDetails.
        :rtype: list[str]
        """
        return self._components

    @components.setter
    def components(self, components):
        """
        Sets the components of this ProductConfigCategoryDetails.
        Various components of the Product.
        For example:The administration server or node manager can be the components of the Oracle WebLogic Application server.
        Forms server or concurrent manager can be the components of the Oracle E-Business Suite.


        :param components: The components of this ProductConfigCategoryDetails.
        :type: list[str]
        """
        self._components = components

    @property
    def compatible_products(self):
        """
        Gets the compatible_products of this ProductConfigCategoryDetails.
        Products compatible with this Product.
        Provide products from the list of other products you have created that are compatible with the present one


        :return: The compatible_products of this ProductConfigCategoryDetails.
        :rtype: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        return self._compatible_products

    @compatible_products.setter
    def compatible_products(self, compatible_products):
        """
        Sets the compatible_products of this ProductConfigCategoryDetails.
        Products compatible with this Product.
        Provide products from the list of other products you have created that are compatible with the present one


        :param compatible_products: The compatible_products of this ProductConfigCategoryDetails.
        :type: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        self._compatible_products = compatible_products

    @property
    def patch_types(self):
        """
        Gets the patch_types of this ProductConfigCategoryDetails.
        Patch Types associated with this Product.


        :return: The patch_types of this ProductConfigCategoryDetails.
        :rtype: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        return self._patch_types

    @patch_types.setter
    def patch_types(self, patch_types):
        """
        Sets the patch_types of this ProductConfigCategoryDetails.
        Patch Types associated with this Product.


        :param patch_types: The patch_types of this ProductConfigCategoryDetails.
        :type: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        self._patch_types = patch_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
