# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateHttpRedirectDetails(object):
    """
    The details of a HTTP Redirect configured to redirect traffic from one hostname to another.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateHttpRedirectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateHttpRedirectDetails.
        :type display_name: str

        :param target:
            The value to assign to the target property of this UpdateHttpRedirectDetails.
        :type target: HttpRedirectTarget

        :param response_code:
            The value to assign to the response_code property of this UpdateHttpRedirectDetails.
        :type response_code: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateHttpRedirectDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateHttpRedirectDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'target': 'HttpRedirectTarget',
            'response_code': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'target': 'target',
            'response_code': 'responseCode',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._target = None
        self._response_code = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateHttpRedirectDetails.
        The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.


        :return: The display_name of this UpdateHttpRedirectDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateHttpRedirectDetails.
        The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.


        :param display_name: The display_name of this UpdateHttpRedirectDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def target(self):
        """
        Gets the target of this UpdateHttpRedirectDetails.
        The redirect target object including all the redirect data.


        :return: The target of this UpdateHttpRedirectDetails.
        :rtype: HttpRedirectTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this UpdateHttpRedirectDetails.
        The redirect target object including all the redirect data.


        :param target: The target of this UpdateHttpRedirectDetails.
        :type: HttpRedirectTarget
        """
        self._target = target

    @property
    def response_code(self):
        """
        Gets the response_code of this UpdateHttpRedirectDetails.
        The response code returned for the redirect to the client. reference - https://tools.ietf.org/html/rfc7231#section-6.4


        :return: The response_code of this UpdateHttpRedirectDetails.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this UpdateHttpRedirectDetails.
        The response code returned for the redirect to the client. reference - https://tools.ietf.org/html/rfc7231#section-6.4


        :param response_code: The response_code of this UpdateHttpRedirectDetails.
        :type: int
        """
        self._response_code = response_code

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateHttpRedirectDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateHttpRedirectDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateHttpRedirectDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateHttpRedirectDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateHttpRedirectDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateHttpRedirectDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateHttpRedirectDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateHttpRedirectDetails.
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
