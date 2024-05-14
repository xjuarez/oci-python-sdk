# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccountRecoverySetting(object):
    """
    Account Recovery Settings
    """

    #: A constant which can be used with the idcs_prevented_operations property of a AccountRecoverySetting.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a AccountRecoverySetting.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a AccountRecoverySetting.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    #: A constant which can be used with the factors property of a AccountRecoverySetting.
    #: This constant has a value of "email"
    FACTORS_EMAIL = "email"

    #: A constant which can be used with the factors property of a AccountRecoverySetting.
    #: This constant has a value of "sms"
    FACTORS_SMS = "sms"

    #: A constant which can be used with the factors property of a AccountRecoverySetting.
    #: This constant has a value of "secquestions"
    FACTORS_SECQUESTIONS = "secquestions"

    #: A constant which can be used with the factors property of a AccountRecoverySetting.
    #: This constant has a value of "push"
    FACTORS_PUSH = "push"

    #: A constant which can be used with the factors property of a AccountRecoverySetting.
    #: This constant has a value of "totp"
    FACTORS_TOTP = "totp"

    def __init__(self, **kwargs):
        """
        Initializes a new AccountRecoverySetting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AccountRecoverySetting.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this AccountRecoverySetting.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this AccountRecoverySetting.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this AccountRecoverySetting.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this AccountRecoverySetting.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this AccountRecoverySetting.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this AccountRecoverySetting.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this AccountRecoverySetting.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this AccountRecoverySetting.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this AccountRecoverySetting.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this AccountRecoverySetting.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this AccountRecoverySetting.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this AccountRecoverySetting.
        :type tenancy_ocid: str

        :param external_id:
            The value to assign to the external_id property of this AccountRecoverySetting.
        :type external_id: str

        :param factors:
            The value to assign to the factors property of this AccountRecoverySetting.
            Allowed values for items in this list are: "email", "sms", "secquestions", "push", "totp", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type factors: list[str]

        :param max_incorrect_attempts:
            The value to assign to the max_incorrect_attempts property of this AccountRecoverySetting.
        :type max_incorrect_attempts: int

        :param lockout_duration:
            The value to assign to the lockout_duration property of this AccountRecoverySetting.
        :type lockout_duration: int

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
            'external_id': 'str',
            'factors': 'list[str]',
            'max_incorrect_attempts': 'int',
            'lockout_duration': 'int'
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
            'external_id': 'externalId',
            'factors': 'factors',
            'max_incorrect_attempts': 'maxIncorrectAttempts',
            'lockout_duration': 'lockoutDuration'
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
        self._external_id = None
        self._factors = None
        self._max_incorrect_attempts = None
        self._lockout_duration = None

    @property
    def id(self):
        """
        Gets the id of this AccountRecoverySetting.
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


        :return: The id of this AccountRecoverySetting.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccountRecoverySetting.
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


        :param id: The id of this AccountRecoverySetting.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this AccountRecoverySetting.
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


        :return: The ocid of this AccountRecoverySetting.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this AccountRecoverySetting.
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


        :param ocid: The ocid of this AccountRecoverySetting.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this AccountRecoverySetting.
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


        :return: The schemas of this AccountRecoverySetting.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this AccountRecoverySetting.
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


        :param schemas: The schemas of this AccountRecoverySetting.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this AccountRecoverySetting.

        :return: The meta of this AccountRecoverySetting.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this AccountRecoverySetting.

        :param meta: The meta of this AccountRecoverySetting.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this AccountRecoverySetting.

        :return: The idcs_created_by of this AccountRecoverySetting.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this AccountRecoverySetting.

        :param idcs_created_by: The idcs_created_by of this AccountRecoverySetting.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this AccountRecoverySetting.

        :return: The idcs_last_modified_by of this AccountRecoverySetting.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this AccountRecoverySetting.

        :param idcs_last_modified_by: The idcs_last_modified_by of this AccountRecoverySetting.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this AccountRecoverySetting.
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


        :return: The idcs_prevented_operations of this AccountRecoverySetting.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this AccountRecoverySetting.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this AccountRecoverySetting.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this AccountRecoverySetting.
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


        :return: The tags of this AccountRecoverySetting.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AccountRecoverySetting.
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


        :param tags: The tags of this AccountRecoverySetting.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this AccountRecoverySetting.
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


        :return: The delete_in_progress of this AccountRecoverySetting.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this AccountRecoverySetting.
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


        :param delete_in_progress: The delete_in_progress of this AccountRecoverySetting.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this AccountRecoverySetting.
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


        :return: The idcs_last_upgraded_in_release of this AccountRecoverySetting.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this AccountRecoverySetting.
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


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this AccountRecoverySetting.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this AccountRecoverySetting.
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


        :return: The domain_ocid of this AccountRecoverySetting.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this AccountRecoverySetting.
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


        :param domain_ocid: The domain_ocid of this AccountRecoverySetting.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this AccountRecoverySetting.
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


        :return: The compartment_ocid of this AccountRecoverySetting.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this AccountRecoverySetting.
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


        :param compartment_ocid: The compartment_ocid of this AccountRecoverySetting.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this AccountRecoverySetting.
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


        :return: The tenancy_ocid of this AccountRecoverySetting.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this AccountRecoverySetting.
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


        :param tenancy_ocid: The tenancy_ocid of this AccountRecoverySetting.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def external_id(self):
        """
        Gets the external_id of this AccountRecoverySetting.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The external_id of this AccountRecoverySetting.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this AccountRecoverySetting.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param external_id: The external_id of this AccountRecoverySetting.
        :type: str
        """
        self._external_id = external_id

    @property
    def factors(self):
        """
        **[Required]** Gets the factors of this AccountRecoverySetting.
        The account recovery factor used (for example, email, mobile number (SMS), security questions, mobile application push or TOTP) to verify the identity of the user and reset the user's password.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "email", "sms", "secquestions", "push", "totp", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The factors of this AccountRecoverySetting.
        :rtype: list[str]
        """
        return self._factors

    @factors.setter
    def factors(self, factors):
        """
        Sets the factors of this AccountRecoverySetting.
        The account recovery factor used (for example, email, mobile number (SMS), security questions, mobile application push or TOTP) to verify the identity of the user and reset the user's password.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param factors: The factors of this AccountRecoverySetting.
        :type: list[str]
        """
        allowed_values = ["email", "sms", "secquestions", "push", "totp"]
        if factors:
            factors[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in factors]
        self._factors = factors

    @property
    def max_incorrect_attempts(self):
        """
        **[Required]** Gets the max_incorrect_attempts of this AccountRecoverySetting.
        Indicates the maximum number of failed account recovery attempts allowed for the user.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none
         - idcsMinValue: 1
         - idcsMaxValue: 99


        :return: The max_incorrect_attempts of this AccountRecoverySetting.
        :rtype: int
        """
        return self._max_incorrect_attempts

    @max_incorrect_attempts.setter
    def max_incorrect_attempts(self, max_incorrect_attempts):
        """
        Sets the max_incorrect_attempts of this AccountRecoverySetting.
        Indicates the maximum number of failed account recovery attempts allowed for the user.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none
         - idcsMinValue: 1
         - idcsMaxValue: 99


        :param max_incorrect_attempts: The max_incorrect_attempts of this AccountRecoverySetting.
        :type: int
        """
        self._max_incorrect_attempts = max_incorrect_attempts

    @property
    def lockout_duration(self):
        """
        **[Required]** Gets the lockout_duration of this AccountRecoverySetting.
        Indicates how many minutes to disable account recovery for the user. The default value is 30 metric minutes.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none
         - idcsMinValue: 5
         - idcsMaxValue: 9999


        :return: The lockout_duration of this AccountRecoverySetting.
        :rtype: int
        """
        return self._lockout_duration

    @lockout_duration.setter
    def lockout_duration(self, lockout_duration):
        """
        Sets the lockout_duration of this AccountRecoverySetting.
        Indicates how many minutes to disable account recovery for the user. The default value is 30 metric minutes.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none
         - idcsMinValue: 5
         - idcsMaxValue: 9999


        :param lockout_duration: The lockout_duration of this AccountRecoverySetting.
        :type: int
        """
        self._lockout_duration = lockout_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
