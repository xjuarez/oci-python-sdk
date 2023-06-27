# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamProfileSummary(object):
    """
    Summary information pertaining to a module stream profile provided by a software source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamProfileSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamProfileSummary.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStreamProfileSummary.
        :type stream_name: str

        :param name:
            The value to assign to the name property of this ModuleStreamProfileSummary.
        :type name: str

        :param is_default:
            The value to assign to the is_default property of this ModuleStreamProfileSummary.
        :type is_default: bool

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str',
            'name': 'str',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName',
            'name': 'name',
            'is_default': 'isDefault'
        }

        self._module_name = None
        self._stream_name = None
        self._name = None
        self._is_default = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamProfileSummary.
        The name of the module that contains the stream profile.


        :return: The module_name of this ModuleStreamProfileSummary.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamProfileSummary.
        The name of the module that contains the stream profile.


        :param module_name: The module_name of this ModuleStreamProfileSummary.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this ModuleStreamProfileSummary.
        The name of the stream that contains the profile.


        :return: The stream_name of this ModuleStreamProfileSummary.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStreamProfileSummary.
        The name of the stream that contains the profile.


        :param stream_name: The stream_name of this ModuleStreamProfileSummary.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModuleStreamProfileSummary.
        The name of the profile.


        :return: The name of this ModuleStreamProfileSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModuleStreamProfileSummary.
        The name of the profile.


        :param name: The name of this ModuleStreamProfileSummary.
        :type: str
        """
        self._name = name

    @property
    def is_default(self):
        """
        Gets the is_default of this ModuleStreamProfileSummary.
        Indicates if this profile is the default for its module stream.


        :return: The is_default of this ModuleStreamProfileSummary.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this ModuleStreamProfileSummary.
        Indicates if this profile is the default for its module stream.


        :param is_default: The is_default of this ModuleStreamProfileSummary.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
