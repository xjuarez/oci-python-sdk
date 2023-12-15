# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisableCertificateDetails(object):
    """
    The request body info about disable certificate service list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DisableCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this DisableCertificateDetails.
        :type cluster_admin_password: str

        :param services:
            The value to assign to the services property of this DisableCertificateDetails.
        :type services: list[oci.bds.models.Service]

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'services': 'list[Service]'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'services': 'services'
        }

        self._cluster_admin_password = None
        self._services = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this DisableCertificateDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this DisableCertificateDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this DisableCertificateDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this DisableCertificateDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def services(self):
        """
        **[Required]** Gets the services of this DisableCertificateDetails.
        List of services for which certificate needs to be disabled.


        :return: The services of this DisableCertificateDetails.
        :rtype: list[oci.bds.models.Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this DisableCertificateDetails.
        List of services for which certificate needs to be disabled.


        :param services: The services of this DisableCertificateDetails.
        :type: list[oci.bds.models.Service]
        """
        self._services = services

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
