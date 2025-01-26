# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .generate_library_url_details import GenerateLibraryUrlDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateLogReaderComponentLibraryUrlDetails(GenerateLibraryUrlDetails):
    """
    Definition of the additional attributes for default library URL generation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateLogReaderComponentLibraryUrlDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.GenerateLogReaderComponentLibraryUrlDetails.library_type` attribute
        of this class is ``LOG_READER_COMPONENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param library_type:
            The value to assign to the library_type property of this GenerateLogReaderComponentLibraryUrlDetails.
            Allowed values for this property are: "LOG_READER_COMPONENT"
        :type library_type: str

        """
        self.swagger_types = {
            'library_type': 'str'
        }

        self.attribute_map = {
            'library_type': 'libraryType'
        }

        self._library_type = None
        self._library_type = 'LOG_READER_COMPONENT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
