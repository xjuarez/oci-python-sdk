# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSubscriberDetails(object):
    """
    Information about a new subscriber.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSubscriberDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateSubscriberDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSubscriberDetails.
        :type compartment_id: str

        :param clients:
            The value to assign to the clients property of this CreateSubscriberDetails.
        :type clients: list[oci.apigateway.models.Client]

        :param usage_plans:
            The value to assign to the usage_plans property of this CreateSubscriberDetails.
        :type usage_plans: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSubscriberDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSubscriberDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'clients': 'list[Client]',
            'usage_plans': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'clients': 'clients',
            'usage_plans': 'usagePlans',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._clients = None
        self._usage_plans = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSubscriberDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateSubscriberDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSubscriberDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateSubscriberDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSubscriberDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateSubscriberDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSubscriberDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateSubscriberDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def clients(self):
        """
        **[Required]** Gets the clients of this CreateSubscriberDetails.
        The clients belonging to this subscriber.


        :return: The clients of this CreateSubscriberDetails.
        :rtype: list[oci.apigateway.models.Client]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """
        Sets the clients of this CreateSubscriberDetails.
        The clients belonging to this subscriber.


        :param clients: The clients of this CreateSubscriberDetails.
        :type: list[oci.apigateway.models.Client]
        """
        self._clients = clients

    @property
    def usage_plans(self):
        """
        **[Required]** Gets the usage_plans of this CreateSubscriberDetails.
        An array of `OCID`__s of usage
        plan resources.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The usage_plans of this CreateSubscriberDetails.
        :rtype: list[str]
        """
        return self._usage_plans

    @usage_plans.setter
    def usage_plans(self, usage_plans):
        """
        Sets the usage_plans of this CreateSubscriberDetails.
        An array of `OCID`__s of usage
        plan resources.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param usage_plans: The usage_plans of this CreateSubscriberDetails.
        :type: list[str]
        """
        self._usage_plans = usage_plans

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSubscriberDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSubscriberDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSubscriberDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSubscriberDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSubscriberDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSubscriberDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSubscriberDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSubscriberDetails.
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
