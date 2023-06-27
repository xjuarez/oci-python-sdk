# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerImageSignature(object):
    """
    Container image signature metadata.
    """

    #: A constant which can be used with the signing_algorithm property of a ContainerImageSignature.
    #: This constant has a value of "SHA_224_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_224_RSA_PKCS_PSS = "SHA_224_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a ContainerImageSignature.
    #: This constant has a value of "SHA_256_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_256_RSA_PKCS_PSS = "SHA_256_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a ContainerImageSignature.
    #: This constant has a value of "SHA_384_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_384_RSA_PKCS_PSS = "SHA_384_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a ContainerImageSignature.
    #: This constant has a value of "SHA_512_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_512_RSA_PKCS_PSS = "SHA_512_RSA_PKCS_PSS"

    #: A constant which can be used with the lifecycle_state property of a ContainerImageSignature.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ContainerImageSignature.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ContainerImageSignature.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerImageSignature object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerImageSignature.
        :type compartment_id: str

        :param created_by:
            The value to assign to the created_by property of this ContainerImageSignature.
        :type created_by: str

        :param display_name:
            The value to assign to the display_name property of this ContainerImageSignature.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ContainerImageSignature.
        :type id: str

        :param image_id:
            The value to assign to the image_id property of this ContainerImageSignature.
        :type image_id: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this ContainerImageSignature.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this ContainerImageSignature.
        :type kms_key_version_id: str

        :param message:
            The value to assign to the message property of this ContainerImageSignature.
        :type message: str

        :param signature:
            The value to assign to the signature property of this ContainerImageSignature.
        :type signature: str

        :param signing_algorithm:
            The value to assign to the signing_algorithm property of this ContainerImageSignature.
            Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type signing_algorithm: str

        :param time_created:
            The value to assign to the time_created property of this ContainerImageSignature.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerImageSignature.
            Allowed values for this property are: "AVAILABLE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ContainerImageSignature.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ContainerImageSignature.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ContainerImageSignature.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'created_by': 'str',
            'display_name': 'str',
            'id': 'str',
            'image_id': 'str',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'message': 'str',
            'signature': 'str',
            'signing_algorithm': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'display_name': 'displayName',
            'id': 'id',
            'image_id': 'imageId',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'message': 'message',
            'signature': 'signature',
            'signing_algorithm': 'signingAlgorithm',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._compartment_id = None
        self._created_by = None
        self._display_name = None
        self._id = None
        self._image_id = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._message = None
        self._signature = None
        self._signing_algorithm = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ContainerImageSignature.
        The `OCID`__ of the compartment in which the container repository exists.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ContainerImageSignature.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerImageSignature.
        The `OCID`__ of the compartment in which the container repository exists.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ContainerImageSignature.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this ContainerImageSignature.
        The id of the user or principal that created the resource.


        :return: The created_by of this ContainerImageSignature.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ContainerImageSignature.
        The id of the user or principal that created the resource.


        :param created_by: The created_by of this ContainerImageSignature.
        :type: str
        """
        self._created_by = created_by

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ContainerImageSignature.
        The last 10 characters of the kmsKeyId, the last 10 characters of the kmsKeyVersionId, the signingAlgorithm, and the last 10 characters of the signatureId.

        Example: `wrmz22sixa::qdwyc2ptun::SHA_256_RSA_PKCS_PSS::2vwmobasva`


        :return: The display_name of this ContainerImageSignature.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ContainerImageSignature.
        The last 10 characters of the kmsKeyId, the last 10 characters of the kmsKeyVersionId, the signingAlgorithm, and the last 10 characters of the signatureId.

        Example: `wrmz22sixa::qdwyc2ptun::SHA_256_RSA_PKCS_PSS::2vwmobasva`


        :param display_name: The display_name of this ContainerImageSignature.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ContainerImageSignature.
        The `OCID`__ of the container image signature.

        Example: `ocid1.containerimagesignature.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ContainerImageSignature.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContainerImageSignature.
        The `OCID`__ of the container image signature.

        Example: `ocid1.containerimagesignature.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ContainerImageSignature.
        :type: str
        """
        self._id = id

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this ContainerImageSignature.
        The `OCID`__ of the container image.

        Example: `ocid1.containerimage.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The image_id of this ContainerImageSignature.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ContainerImageSignature.
        The `OCID`__ of the container image.

        Example: `ocid1.containerimage.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param image_id: The image_id of this ContainerImageSignature.
        :type: str
        """
        self._image_id = image_id

    @property
    def kms_key_id(self):
        """
        **[Required]** Gets the kms_key_id of this ContainerImageSignature.
        The `OCID`__ of the kmsKeyId used to sign the container image.

        Example: `ocid1.key.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_id of this ContainerImageSignature.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this ContainerImageSignature.
        The `OCID`__ of the kmsKeyId used to sign the container image.

        Example: `ocid1.key.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_id: The kms_key_id of this ContainerImageSignature.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def kms_key_version_id(self):
        """
        **[Required]** Gets the kms_key_version_id of this ContainerImageSignature.
        The `OCID`__ of the kmsKeyVersionId used to sign the container image.

        Example: `ocid1.keyversion.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_version_id of this ContainerImageSignature.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this ContainerImageSignature.
        The `OCID`__ of the kmsKeyVersionId used to sign the container image.

        Example: `ocid1.keyversion.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_version_id: The kms_key_version_id of this ContainerImageSignature.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    @property
    def message(self):
        """
        **[Required]** Gets the message of this ContainerImageSignature.
        The base64 encoded signature payload that was signed.


        :return: The message of this ContainerImageSignature.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ContainerImageSignature.
        The base64 encoded signature payload that was signed.


        :param message: The message of this ContainerImageSignature.
        :type: str
        """
        self._message = message

    @property
    def signature(self):
        """
        **[Required]** Gets the signature of this ContainerImageSignature.
        The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.


        :return: The signature of this ContainerImageSignature.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this ContainerImageSignature.
        The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.


        :param signature: The signature of this ContainerImageSignature.
        :type: str
        """
        self._signature = signature

    @property
    def signing_algorithm(self):
        """
        **[Required]** Gets the signing_algorithm of this ContainerImageSignature.
        The algorithm to be used for signing. These are the only supported signing algorithms for container images.

        Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The signing_algorithm of this ContainerImageSignature.
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """
        Sets the signing_algorithm of this ContainerImageSignature.
        The algorithm to be used for signing. These are the only supported signing algorithms for container images.


        :param signing_algorithm: The signing_algorithm of this ContainerImageSignature.
        :type: str
        """
        allowed_values = ["SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"]
        if not value_allowed_none_or_none_sentinel(signing_algorithm, allowed_values):
            signing_algorithm = 'UNKNOWN_ENUM_VALUE'
        self._signing_algorithm = signing_algorithm

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerImageSignature.
        An RFC 3339 timestamp indicating when the image was created.


        :return: The time_created of this ContainerImageSignature.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerImageSignature.
        An RFC 3339 timestamp indicating when the image was created.


        :param time_created: The time_created of this ContainerImageSignature.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ContainerImageSignature.
        The current state of the container image signature.

        Allowed values for this property are: "AVAILABLE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ContainerImageSignature.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ContainerImageSignature.
        The current state of the container image signature.


        :param lifecycle_state: The lifecycle_state of this ContainerImageSignature.
        :type: str
        """
        allowed_values = ["AVAILABLE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ContainerImageSignature.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ContainerImageSignature.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ContainerImageSignature.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ContainerImageSignature.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ContainerImageSignature.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ContainerImageSignature.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ContainerImageSignature.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ContainerImageSignature.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        **[Required]** Gets the system_tags of this ContainerImageSignature.
        The system tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ContainerImageSignature.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ContainerImageSignature.
        The system tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ContainerImageSignature.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
