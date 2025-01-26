# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .listing_revision_package import ListingRevisionPackage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerPackage(ListingRevisionPackage):
    """
    A package for container image listings.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerPackage object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace_publisher.models.ContainerPackage.package_type` attribute
        of this class is ``CONTAINER_IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ContainerPackage.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ContainerPackage.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ContainerPackage.
        :type description: str

        :param listing_revision_id:
            The value to assign to the listing_revision_id property of this ContainerPackage.
        :type listing_revision_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerPackage.
        :type compartment_id: str

        :param artifact_id:
            The value to assign to the artifact_id property of this ContainerPackage.
        :type artifact_id: str

        :param term_id:
            The value to assign to the term_id property of this ContainerPackage.
        :type term_id: str

        :param package_version:
            The value to assign to the package_version property of this ContainerPackage.
        :type package_version: str

        :param package_type:
            The value to assign to the package_type property of this ContainerPackage.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART"
        :type package_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerPackage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param status:
            The value to assign to the status property of this ContainerPackage.
            Allowed values for this property are: "NEW", "PUBLISH_IN_PROGRESS", "UNPUBLISH_IN_PROGRESS", "PUBLISH_FAILED", "PUBLISHED", "PUBLISHED_AS_PRIVATE", "UNPUBLISHED"
        :type status: str

        :param are_security_upgrades_provided:
            The value to assign to the are_security_upgrades_provided property of this ContainerPackage.
        :type are_security_upgrades_provided: bool

        :param is_default:
            The value to assign to the is_default property of this ContainerPackage.
        :type is_default: bool

        :param time_created:
            The value to assign to the time_created property of this ContainerPackage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ContainerPackage.
        :type time_updated: datetime

        :param extended_metadata:
            The value to assign to the extended_metadata property of this ContainerPackage.
        :type extended_metadata: dict(str, str)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ContainerPackage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ContainerPackage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ContainerPackage.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'listing_revision_id': 'str',
            'compartment_id': 'str',
            'artifact_id': 'str',
            'term_id': 'str',
            'package_version': 'str',
            'package_type': 'str',
            'lifecycle_state': 'str',
            'status': 'str',
            'are_security_upgrades_provided': 'bool',
            'is_default': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'extended_metadata': 'dict(str, str)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'listing_revision_id': 'listingRevisionId',
            'compartment_id': 'compartmentId',
            'artifact_id': 'artifactId',
            'term_id': 'termId',
            'package_version': 'packageVersion',
            'package_type': 'packageType',
            'lifecycle_state': 'lifecycleState',
            'status': 'status',
            'are_security_upgrades_provided': 'areSecurityUpgradesProvided',
            'is_default': 'isDefault',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'extended_metadata': 'extendedMetadata',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._listing_revision_id = None
        self._compartment_id = None
        self._artifact_id = None
        self._term_id = None
        self._package_version = None
        self._package_type = None
        self._lifecycle_state = None
        self._status = None
        self._are_security_upgrades_provided = None
        self._is_default = None
        self._time_created = None
        self._time_updated = None
        self._extended_metadata = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._package_type = 'CONTAINER_IMAGE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
