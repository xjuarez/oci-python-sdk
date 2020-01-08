# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateHttpMonitorDetails(object):
    """
    The request body used to create an HTTP monitor.
    """

    #: A constant which can be used with the protocol property of a CreateHttpMonitorDetails.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a CreateHttpMonitorDetails.
    #: This constant has a value of "HTTPS"
    PROTOCOL_HTTPS = "HTTPS"

    #: A constant which can be used with the method property of a CreateHttpMonitorDetails.
    #: This constant has a value of "GET"
    METHOD_GET = "GET"

    #: A constant which can be used with the method property of a CreateHttpMonitorDetails.
    #: This constant has a value of "HEAD"
    METHOD_HEAD = "HEAD"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateHttpMonitorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateHttpMonitorDetails.
        :type compartment_id: str

        :param targets:
            The value to assign to the targets property of this CreateHttpMonitorDetails.
        :type targets: list[str]

        :param vantage_point_names:
            The value to assign to the vantage_point_names property of this CreateHttpMonitorDetails.
        :type vantage_point_names: list[str]

        :param port:
            The value to assign to the port property of this CreateHttpMonitorDetails.
        :type port: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this CreateHttpMonitorDetails.
        :type timeout_in_seconds: int

        :param protocol:
            The value to assign to the protocol property of this CreateHttpMonitorDetails.
            Allowed values for this property are: "HTTP", "HTTPS"
        :type protocol: str

        :param method:
            The value to assign to the method property of this CreateHttpMonitorDetails.
            Allowed values for this property are: "GET", "HEAD"
        :type method: str

        :param path:
            The value to assign to the path property of this CreateHttpMonitorDetails.
        :type path: str

        :param headers:
            The value to assign to the headers property of this CreateHttpMonitorDetails.
        :type headers: dict(str, str)

        :param display_name:
            The value to assign to the display_name property of this CreateHttpMonitorDetails.
        :type display_name: str

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this CreateHttpMonitorDetails.
        :type interval_in_seconds: int

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateHttpMonitorDetails.
        :type is_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateHttpMonitorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateHttpMonitorDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'targets': 'list[str]',
            'vantage_point_names': 'list[str]',
            'port': 'int',
            'timeout_in_seconds': 'int',
            'protocol': 'str',
            'method': 'str',
            'path': 'str',
            'headers': 'dict(str, str)',
            'display_name': 'str',
            'interval_in_seconds': 'int',
            'is_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'targets': 'targets',
            'vantage_point_names': 'vantagePointNames',
            'port': 'port',
            'timeout_in_seconds': 'timeoutInSeconds',
            'protocol': 'protocol',
            'method': 'method',
            'path': 'path',
            'headers': 'headers',
            'display_name': 'displayName',
            'interval_in_seconds': 'intervalInSeconds',
            'is_enabled': 'isEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._targets = None
        self._vantage_point_names = None
        self._port = None
        self._timeout_in_seconds = None
        self._protocol = None
        self._method = None
        self._path = None
        self._headers = None
        self._display_name = None
        self._interval_in_seconds = None
        self._is_enabled = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateHttpMonitorDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateHttpMonitorDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateHttpMonitorDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateHttpMonitorDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def targets(self):
        """
        **[Required]** Gets the targets of this CreateHttpMonitorDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :return: The targets of this CreateHttpMonitorDetails.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this CreateHttpMonitorDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :param targets: The targets of this CreateHttpMonitorDetails.
        :type: list[str]
        """
        self._targets = targets

    @property
    def vantage_point_names(self):
        """
        Gets the vantage_point_names of this CreateHttpMonitorDetails.
        A list of names of vantage points from which to execute the probe.


        :return: The vantage_point_names of this CreateHttpMonitorDetails.
        :rtype: list[str]
        """
        return self._vantage_point_names

    @vantage_point_names.setter
    def vantage_point_names(self, vantage_point_names):
        """
        Sets the vantage_point_names of this CreateHttpMonitorDetails.
        A list of names of vantage points from which to execute the probe.


        :param vantage_point_names: The vantage_point_names of this CreateHttpMonitorDetails.
        :type: list[str]
        """
        self._vantage_point_names = vantage_point_names

    @property
    def port(self):
        """
        Gets the port of this CreateHttpMonitorDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :return: The port of this CreateHttpMonitorDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateHttpMonitorDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :param port: The port of this CreateHttpMonitorDetails.
        :type: int
        """
        self._port = port

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this CreateHttpMonitorDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :return: The timeout_in_seconds of this CreateHttpMonitorDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this CreateHttpMonitorDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :param timeout_in_seconds: The timeout_in_seconds of this CreateHttpMonitorDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreateHttpMonitorDetails.
        Allowed values for this property are: "HTTP", "HTTPS"


        :return: The protocol of this CreateHttpMonitorDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreateHttpMonitorDetails.

        :param protocol: The protocol of this CreateHttpMonitorDetails.
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def method(self):
        """
        Gets the method of this CreateHttpMonitorDetails.
        Allowed values for this property are: "GET", "HEAD"


        :return: The method of this CreateHttpMonitorDetails.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this CreateHttpMonitorDetails.

        :param method: The method of this CreateHttpMonitorDetails.
        :type: str
        """
        allowed_values = ["GET", "HEAD"]
        if not value_allowed_none_or_none_sentinel(method, allowed_values):
            raise ValueError(
                "Invalid value for `method`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._method = method

    @property
    def path(self):
        """
        Gets the path of this CreateHttpMonitorDetails.
        The optional URL path to probe, including query parameters.


        :return: The path of this CreateHttpMonitorDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this CreateHttpMonitorDetails.
        The optional URL path to probe, including query parameters.


        :param path: The path of this CreateHttpMonitorDetails.
        :type: str
        """
        self._path = path

    @property
    def headers(self):
        """
        Gets the headers of this CreateHttpMonitorDetails.
        A dictionary of HTTP request headers.

        *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.


        :return: The headers of this CreateHttpMonitorDetails.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this CreateHttpMonitorDetails.
        A dictionary of HTTP request headers.

        *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.


        :param headers: The headers of this CreateHttpMonitorDetails.
        :type: dict(str, str)
        """
        self._headers = headers

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateHttpMonitorDetails.
        A user-friendly and mutable name suitable for display in a user interface.


        :return: The display_name of this CreateHttpMonitorDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateHttpMonitorDetails.
        A user-friendly and mutable name suitable for display in a user interface.


        :param display_name: The display_name of this CreateHttpMonitorDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def interval_in_seconds(self):
        """
        **[Required]** Gets the interval_in_seconds of this CreateHttpMonitorDetails.
        The monitor interval in seconds. Valid values: 10, 30, and 60.


        :return: The interval_in_seconds of this CreateHttpMonitorDetails.
        :rtype: int
        """
        return self._interval_in_seconds

    @interval_in_seconds.setter
    def interval_in_seconds(self, interval_in_seconds):
        """
        Sets the interval_in_seconds of this CreateHttpMonitorDetails.
        The monitor interval in seconds. Valid values: 10, 30, and 60.


        :param interval_in_seconds: The interval_in_seconds of this CreateHttpMonitorDetails.
        :type: int
        """
        self._interval_in_seconds = interval_in_seconds

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CreateHttpMonitorDetails.
        Enables or disables the monitor. Set to 'true' to launch monitoring.


        :return: The is_enabled of this CreateHttpMonitorDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateHttpMonitorDetails.
        Enables or disables the monitor. Set to 'true' to launch monitoring.


        :param is_enabled: The is_enabled of this CreateHttpMonitorDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateHttpMonitorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace.  For more information,
        see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateHttpMonitorDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateHttpMonitorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace.  For more information,
        see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateHttpMonitorDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateHttpMonitorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateHttpMonitorDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateHttpMonitorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateHttpMonitorDetails.
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
