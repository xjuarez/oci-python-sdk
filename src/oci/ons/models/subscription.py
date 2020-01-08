# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Subscription(object):
    """
    The subscription's configuration. For general information about subscriptions, see
    `Notifications Overview`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "PENDING"
    LIFECYCLE_STATE_PENDING = "PENDING"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Subscription object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Subscription.
        :type id: str

        :param topic_id:
            The value to assign to the topic_id property of this Subscription.
        :type topic_id: str

        :param protocol:
            The value to assign to the protocol property of this Subscription.
        :type protocol: str

        :param endpoint:
            The value to assign to the endpoint property of this Subscription.
        :type endpoint: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Subscription.
            Allowed values for this property are: "PENDING", "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Subscription.
        :type compartment_id: str

        :param created_time:
            The value to assign to the created_time property of this Subscription.
        :type created_time: int

        :param deliver_policy:
            The value to assign to the deliver_policy property of this Subscription.
        :type deliver_policy: str

        :param etag:
            The value to assign to the etag property of this Subscription.
        :type etag: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Subscription.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Subscription.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'topic_id': 'str',
            'protocol': 'str',
            'endpoint': 'str',
            'lifecycle_state': 'str',
            'compartment_id': 'str',
            'created_time': 'int',
            'deliver_policy': 'str',
            'etag': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'topic_id': 'topicId',
            'protocol': 'protocol',
            'endpoint': 'endpoint',
            'lifecycle_state': 'lifecycleState',
            'compartment_id': 'compartmentId',
            'created_time': 'createdTime',
            'deliver_policy': 'deliverPolicy',
            'etag': 'etag',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._topic_id = None
        self._protocol = None
        self._endpoint = None
        self._lifecycle_state = None
        self._compartment_id = None
        self._created_time = None
        self._deliver_policy = None
        self._etag = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Subscription.
        The `OCID`__ of the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Subscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subscription.
        The `OCID`__ of the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Subscription.
        :type: str
        """
        self._id = id

    @property
    def topic_id(self):
        """
        **[Required]** Gets the topic_id of this Subscription.
        The `OCID`__ of the associated topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The topic_id of this Subscription.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """
        Sets the topic_id of this Subscription.
        The `OCID`__ of the associated topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param topic_id: The topic_id of this Subscription.
        :type: str
        """
        self._topic_id = topic_id

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this Subscription.
        The protocol used for the subscription.
        For information about subscription protocols, see
        `To create a subscription`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#createSub


        :return: The protocol of this Subscription.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this Subscription.
        The protocol used for the subscription.
        For information about subscription protocols, see
        `To create a subscription`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#createSub


        :param protocol: The protocol of this Subscription.
        :type: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        """
        **[Required]** Gets the endpoint of this Subscription.
        A locator that corresponds to the subscription protocol.
        For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.


        :return: The endpoint of this Subscription.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this Subscription.
        A locator that corresponds to the subscription protocol.
        For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.


        :param endpoint: The endpoint of this Subscription.
        :type: str
        """
        self._endpoint = endpoint

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Subscription.
        The lifecycle state of the subscription. The status of a new subscription is PENDING; when confirmed, the subscription status changes to ACTIVE.

        Allowed values for this property are: "PENDING", "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Subscription.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Subscription.
        The lifecycle state of the subscription. The status of a new subscription is PENDING; when confirmed, the subscription status changes to ACTIVE.


        :param lifecycle_state: The lifecycle_state of this Subscription.
        :type: str
        """
        allowed_values = ["PENDING", "ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Subscription.
        The `OCID`__ of the compartment for the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Subscription.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Subscription.
        The `OCID`__ of the compartment for the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Subscription.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_time(self):
        """
        Gets the created_time of this Subscription.
        The time when this suscription was created.


        :return: The created_time of this Subscription.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """
        Sets the created_time of this Subscription.
        The time when this suscription was created.


        :param created_time: The created_time of this Subscription.
        :type: int
        """
        self._created_time = created_time

    @property
    def deliver_policy(self):
        """
        Gets the deliver_policy of this Subscription.
        The delivery policy of the subscription. Stored as a JSON string.


        :return: The deliver_policy of this Subscription.
        :rtype: str
        """
        return self._deliver_policy

    @deliver_policy.setter
    def deliver_policy(self, deliver_policy):
        """
        Sets the deliver_policy of this Subscription.
        The delivery policy of the subscription. Stored as a JSON string.


        :param deliver_policy: The deliver_policy of this Subscription.
        :type: str
        """
        self._deliver_policy = deliver_policy

    @property
    def etag(self):
        """
        Gets the etag of this Subscription.
        For optimistic concurrency control. See `if-match`.


        :return: The etag of this Subscription.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this Subscription.
        For optimistic concurrency control. See `if-match`.


        :param etag: The etag of this Subscription.
        :type: str
        """
        self._etag = etag

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Subscription.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Subscription.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Subscription.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Subscription.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Subscription.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Subscription.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Subscription.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Subscription.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
