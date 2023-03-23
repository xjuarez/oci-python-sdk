# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Operations(object):
    """
    Each patch operation object MUST have exactly one \"op\" member, whose value indicates the operation to perform and MAY be one of \"add\", \"remove\", or \"replace\". See `Section 3.5.2`__ for details.

    __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.5.2
    """

    #: A constant which can be used with the op property of a Operations.
    #: This constant has a value of "ADD"
    OP_ADD = "ADD"

    #: A constant which can be used with the op property of a Operations.
    #: This constant has a value of "REMOVE"
    OP_REMOVE = "REMOVE"

    #: A constant which can be used with the op property of a Operations.
    #: This constant has a value of "REPLACE"
    OP_REPLACE = "REPLACE"

    def __init__(self, **kwargs):
        """
        Initializes a new Operations object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param op:
            The value to assign to the op property of this Operations.
            Allowed values for this property are: "ADD", "REMOVE", "REPLACE"
        :type op: str

        :param path:
            The value to assign to the path property of this Operations.
        :type path: str

        :param value:
            The value to assign to the value property of this Operations.
        :type value: object

        """
        self.swagger_types = {
            'op': 'str',
            'path': 'str',
            'value': 'object'
        }

        self.attribute_map = {
            'op': 'op',
            'path': 'path',
            'value': 'value'
        }

        self._op = None
        self._path = None
        self._value = None

    @property
    def op(self):
        """
        **[Required]** Gets the op of this Operations.
        Defines the operation to be performed for this Patch. If op=remove, value is not required.

        Allowed values for this property are: "ADD", "REMOVE", "REPLACE"


        :return: The op of this Operations.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this Operations.
        Defines the operation to be performed for this Patch. If op=remove, value is not required.


        :param op: The op of this Operations.
        :type: str
        """
        allowed_values = ["ADD", "REMOVE", "REPLACE"]
        if not value_allowed_none_or_none_sentinel(op, allowed_values):
            raise ValueError(
                "Invalid value for `op`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._op = op

    @property
    def path(self):
        """
        **[Required]** Gets the path of this Operations.
        String containing an attribute path describing the target of the operation. The \"path\" attribute is OPTIONAL for \"add\" and \"replace\" and is REQUIRED for \"remove\" operations. See `Section 3.5.2`__ for details

        __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.5.2


        :return: The path of this Operations.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Operations.
        String containing an attribute path describing the target of the operation. The \"path\" attribute is OPTIONAL for \"add\" and \"replace\" and is REQUIRED for \"remove\" operations. See `Section 3.5.2`__ for details

        __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.5.2


        :param path: The path of this Operations.
        :type: str
        """
        self._path = path

    @property
    def value(self):
        """
        Gets the value of this Operations.
        The value could be either a simple value attribute e.g. string or number OR complex like map of the attributes to be added or replaced OR multivalues complex attributes.q1


        :return: The value of this Operations.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Operations.
        The value could be either a simple value attribute e.g. string or number OR complex like map of the attributes to be added or replaced OR multivalues complex attributes.q1


        :param value: The value of this Operations.
        :type: object
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
