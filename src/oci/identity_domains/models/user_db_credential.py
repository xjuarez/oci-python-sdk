# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserDbCredential(object):
    """
    User's Database Credential
    """

    #: A constant which can be used with the idcs_prevented_operations property of a UserDbCredential.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a UserDbCredential.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a UserDbCredential.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    #: A constant which can be used with the status property of a UserDbCredential.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a UserDbCredential.
    #: This constant has a value of "INACTIVE"
    STATUS_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new UserDbCredential object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UserDbCredential.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this UserDbCredential.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this UserDbCredential.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this UserDbCredential.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this UserDbCredential.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this UserDbCredential.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this UserDbCredential.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this UserDbCredential.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this UserDbCredential.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this UserDbCredential.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this UserDbCredential.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this UserDbCredential.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this UserDbCredential.
        :type tenancy_ocid: str

        :param name:
            The value to assign to the name property of this UserDbCredential.
        :type name: str

        :param db_password:
            The value to assign to the db_password property of this UserDbCredential.
        :type db_password: str

        :param description:
            The value to assign to the description property of this UserDbCredential.
        :type description: str

        :param mixed_db_password:
            The value to assign to the mixed_db_password property of this UserDbCredential.
        :type mixed_db_password: str

        :param salt:
            The value to assign to the salt property of this UserDbCredential.
        :type salt: str

        :param mixed_salt:
            The value to assign to the mixed_salt property of this UserDbCredential.
        :type mixed_salt: str

        :param last_set_date:
            The value to assign to the last_set_date property of this UserDbCredential.
        :type last_set_date: str

        :param expired:
            The value to assign to the expired property of this UserDbCredential.
        :type expired: bool

        :param status:
            The value to assign to the status property of this UserDbCredential.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param expires_on:
            The value to assign to the expires_on property of this UserDbCredential.
        :type expires_on: str

        :param user:
            The value to assign to the user property of this UserDbCredential.
        :type user: oci.identity_domains.models.UserDbCredentialsUser

        :param urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user:
            The value to assign to the urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user property of this UserDbCredential.
        :type urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user: oci.identity_domains.models.ExtensionSelfChangeUser

        """
        self.swagger_types = {
            'id': 'str',
            'ocid': 'str',
            'schemas': 'list[str]',
            'meta': 'Meta',
            'idcs_created_by': 'IdcsCreatedBy',
            'idcs_last_modified_by': 'IdcsLastModifiedBy',
            'idcs_prevented_operations': 'list[str]',
            'tags': 'list[Tags]',
            'delete_in_progress': 'bool',
            'idcs_last_upgraded_in_release': 'str',
            'domain_ocid': 'str',
            'compartment_ocid': 'str',
            'tenancy_ocid': 'str',
            'name': 'str',
            'db_password': 'str',
            'description': 'str',
            'mixed_db_password': 'str',
            'salt': 'str',
            'mixed_salt': 'str',
            'last_set_date': 'str',
            'expired': 'bool',
            'status': 'str',
            'expires_on': 'str',
            'user': 'UserDbCredentialsUser',
            'urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user': 'ExtensionSelfChangeUser'
        }

        self.attribute_map = {
            'id': 'id',
            'ocid': 'ocid',
            'schemas': 'schemas',
            'meta': 'meta',
            'idcs_created_by': 'idcsCreatedBy',
            'idcs_last_modified_by': 'idcsLastModifiedBy',
            'idcs_prevented_operations': 'idcsPreventedOperations',
            'tags': 'tags',
            'delete_in_progress': 'deleteInProgress',
            'idcs_last_upgraded_in_release': 'idcsLastUpgradedInRelease',
            'domain_ocid': 'domainOcid',
            'compartment_ocid': 'compartmentOcid',
            'tenancy_ocid': 'tenancyOcid',
            'name': 'name',
            'db_password': 'dbPassword',
            'description': 'description',
            'mixed_db_password': 'mixedDbPassword',
            'salt': 'salt',
            'mixed_salt': 'mixedSalt',
            'last_set_date': 'lastSetDate',
            'expired': 'expired',
            'status': 'status',
            'expires_on': 'expiresOn',
            'user': 'user',
            'urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user': 'urn:ietf:params:scim:schemas:oracle:idcs:extension:selfChange:User'
        }

        self._id = None
        self._ocid = None
        self._schemas = None
        self._meta = None
        self._idcs_created_by = None
        self._idcs_last_modified_by = None
        self._idcs_prevented_operations = None
        self._tags = None
        self._delete_in_progress = None
        self._idcs_last_upgraded_in_release = None
        self._domain_ocid = None
        self._compartment_ocid = None
        self._tenancy_ocid = None
        self._name = None
        self._db_password = None
        self._description = None
        self._mixed_db_password = None
        self._salt = None
        self._mixed_salt = None
        self._last_set_date = None
        self._expired = None
        self._status = None
        self._expires_on = None
        self._user = None
        self._urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user = None

    @property
    def id(self):
        """
        Gets the id of this UserDbCredential.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :return: The id of this UserDbCredential.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserDbCredential.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :param id: The id of this UserDbCredential.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this UserDbCredential.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :return: The ocid of this UserDbCredential.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this UserDbCredential.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :param ocid: The ocid of this UserDbCredential.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this UserDbCredential.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schemas of this UserDbCredential.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this UserDbCredential.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schemas: The schemas of this UserDbCredential.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this UserDbCredential.

        :return: The meta of this UserDbCredential.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this UserDbCredential.

        :param meta: The meta of this UserDbCredential.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this UserDbCredential.

        :return: The idcs_created_by of this UserDbCredential.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this UserDbCredential.

        :param idcs_created_by: The idcs_created_by of this UserDbCredential.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this UserDbCredential.

        :return: The idcs_last_modified_by of this UserDbCredential.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this UserDbCredential.

        :param idcs_last_modified_by: The idcs_last_modified_by of this UserDbCredential.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this UserDbCredential.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The idcs_prevented_operations of this UserDbCredential.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this UserDbCredential.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this UserDbCredential.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this UserDbCredential.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The tags of this UserDbCredential.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UserDbCredential.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param tags: The tags of this UserDbCredential.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this UserDbCredential.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The delete_in_progress of this UserDbCredential.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this UserDbCredential.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param delete_in_progress: The delete_in_progress of this UserDbCredential.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this UserDbCredential.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The idcs_last_upgraded_in_release of this UserDbCredential.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this UserDbCredential.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this UserDbCredential.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this UserDbCredential.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_ocid of this UserDbCredential.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this UserDbCredential.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_ocid: The domain_ocid of this UserDbCredential.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this UserDbCredential.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The compartment_ocid of this UserDbCredential.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this UserDbCredential.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param compartment_ocid: The compartment_ocid of this UserDbCredential.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this UserDbCredential.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The tenancy_ocid of this UserDbCredential.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this UserDbCredential.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param tenancy_ocid: The tenancy_ocid of this UserDbCredential.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def name(self):
        """
        Gets the name of this UserDbCredential.
        Name

        **Added In:** 2109090424

        **SCIM++ Properties:**
         - caseExact: false
         - type: string
         - mutability: readOnly
         - required: false
         - returned: default


        :return: The name of this UserDbCredential.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserDbCredential.
        Name

        **Added In:** 2109090424

        **SCIM++ Properties:**
         - caseExact: false
         - type: string
         - mutability: readOnly
         - required: false
         - returned: default


        :param name: The name of this UserDbCredential.
        :type: str
        """
        self._name = name

    @property
    def db_password(self):
        """
        **[Required]** Gets the db_password of this UserDbCredential.
        The user's database password.

        **SCIM++ Properties:**
         - type: string
         - mutability: immutable
         - returned: default
         - required: true


        :return: The db_password of this UserDbCredential.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """
        Sets the db_password of this UserDbCredential.
        The user's database password.

        **SCIM++ Properties:**
         - type: string
         - mutability: immutable
         - returned: default
         - required: true


        :param db_password: The db_password of this UserDbCredential.
        :type: str
        """
        self._db_password = db_password

    @property
    def description(self):
        """
        Gets the description of this UserDbCredential.
        Description

        **Added In:** 2109020413

        **SCIM++ Properties:**
         - caseExact: false
         - type: string
         - mutability: readWrite
         - required: false
         - returned: default


        :return: The description of this UserDbCredential.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserDbCredential.
        Description

        **Added In:** 2109020413

        **SCIM++ Properties:**
         - caseExact: false
         - type: string
         - mutability: readWrite
         - required: false
         - returned: default


        :param description: The description of this UserDbCredential.
        :type: str
        """
        self._description = description

    @property
    def mixed_db_password(self):
        """
        Gets the mixed_db_password of this UserDbCredential.
        The user's database password with mixed salt.

        **SCIM++ Properties:**
         - type: string
         - mutability: readOnly
         - returned: default
         - required: false


        :return: The mixed_db_password of this UserDbCredential.
        :rtype: str
        """
        return self._mixed_db_password

    @mixed_db_password.setter
    def mixed_db_password(self, mixed_db_password):
        """
        Sets the mixed_db_password of this UserDbCredential.
        The user's database password with mixed salt.

        **SCIM++ Properties:**
         - type: string
         - mutability: readOnly
         - returned: default
         - required: false


        :param mixed_db_password: The mixed_db_password of this UserDbCredential.
        :type: str
        """
        self._mixed_db_password = mixed_db_password

    @property
    def salt(self):
        """
        Gets the salt of this UserDbCredential.
        The salt of the password.

        **SCIM++ Properties:**
         - type: string
         - mutability: readOnly
         - returned: default
         - required: false


        :return: The salt of this UserDbCredential.
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """
        Sets the salt of this UserDbCredential.
        The salt of the password.

        **SCIM++ Properties:**
         - type: string
         - mutability: readOnly
         - returned: default
         - required: false


        :param salt: The salt of this UserDbCredential.
        :type: str
        """
        self._salt = salt

    @property
    def mixed_salt(self):
        """
        Gets the mixed_salt of this UserDbCredential.
        The mixed salt of the password.

        **SCIM++ Properties:**
         - type: string
         - mutability: readOnly
         - returned: default
         - required: false


        :return: The mixed_salt of this UserDbCredential.
        :rtype: str
        """
        return self._mixed_salt

    @mixed_salt.setter
    def mixed_salt(self, mixed_salt):
        """
        Sets the mixed_salt of this UserDbCredential.
        The mixed salt of the password.

        **SCIM++ Properties:**
         - type: string
         - mutability: readOnly
         - returned: default
         - required: false


        :param mixed_salt: The mixed_salt of this UserDbCredential.
        :type: str
        """
        self._mixed_salt = mixed_salt

    @property
    def last_set_date(self):
        """
        Gets the last_set_date of this UserDbCredential.
        A DateTime that specifies the date and time when the current database password was set.

        **SCIM++ Properties:**
         - type: dateTime
         - mutability: readOnly
         - returned: default


        :return: The last_set_date of this UserDbCredential.
        :rtype: str
        """
        return self._last_set_date

    @last_set_date.setter
    def last_set_date(self, last_set_date):
        """
        Sets the last_set_date of this UserDbCredential.
        A DateTime that specifies the date and time when the current database password was set.

        **SCIM++ Properties:**
         - type: dateTime
         - mutability: readOnly
         - returned: default


        :param last_set_date: The last_set_date of this UserDbCredential.
        :type: str
        """
        self._last_set_date = last_set_date

    @property
    def expired(self):
        """
        Gets the expired of this UserDbCredential.
        Indicates that the database password has expired.

        **SCIM++ Properties:**
         - type: boolean
         - mutability: readOnly
         - returned: default


        :return: The expired of this UserDbCredential.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """
        Sets the expired of this UserDbCredential.
        Indicates that the database password has expired.

        **SCIM++ Properties:**
         - type: boolean
         - mutability: readOnly
         - returned: default


        :param expired: The expired of this UserDbCredential.
        :type: bool
        """
        self._expired = expired

    @property
    def status(self):
        """
        Gets the status of this UserDbCredential.
        User credential status

        **Added In:** 2109090424

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: never
         - type: string
         - uniqueness: none

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this UserDbCredential.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserDbCredential.
        User credential status

        **Added In:** 2109090424

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: never
         - type: string
         - uniqueness: none


        :param status: The status of this UserDbCredential.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def expires_on(self):
        """
        Gets the expires_on of this UserDbCredential.
        When the user credential expires.

        **Added In:** 2109090424

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The expires_on of this UserDbCredential.
        :rtype: str
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """
        Sets the expires_on of this UserDbCredential.
        When the user credential expires.

        **Added In:** 2109090424

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param expires_on: The expires_on of this UserDbCredential.
        :type: str
        """
        self._expires_on = expires_on

    @property
    def user(self):
        """
        Gets the user of this UserDbCredential.

        :return: The user of this UserDbCredential.
        :rtype: oci.identity_domains.models.UserDbCredentialsUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this UserDbCredential.

        :param user: The user of this UserDbCredential.
        :type: oci.identity_domains.models.UserDbCredentialsUser
        """
        self._user = user

    @property
    def urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user(self):
        """
        Gets the urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user of this UserDbCredential.

        :return: The urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user of this UserDbCredential.
        :rtype: oci.identity_domains.models.ExtensionSelfChangeUser
        """
        return self._urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user

    @urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user.setter
    def urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user(self, urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user):
        """
        Sets the urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user of this UserDbCredential.

        :param urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user: The urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user of this UserDbCredential.
        :type: oci.identity_domains.models.ExtensionSelfChangeUser
        """
        self._urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user = urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
