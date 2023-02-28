# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCustomTableDetails(object):
    """
    Details for updating the custom table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCustomTableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param saved_custom_table:
            The value to assign to the saved_custom_table property of this UpdateCustomTableDetails.
        :type saved_custom_table: oci.usage_api.models.SavedCustomTable

        """
        self.swagger_types = {
            'saved_custom_table': 'SavedCustomTable'
        }

        self.attribute_map = {
            'saved_custom_table': 'savedCustomTable'
        }

        self._saved_custom_table = None

    @property
    def saved_custom_table(self):
        """
        **[Required]** Gets the saved_custom_table of this UpdateCustomTableDetails.

        :return: The saved_custom_table of this UpdateCustomTableDetails.
        :rtype: oci.usage_api.models.SavedCustomTable
        """
        return self._saved_custom_table

    @saved_custom_table.setter
    def saved_custom_table(self, saved_custom_table):
        """
        Sets the saved_custom_table of this UpdateCustomTableDetails.

        :param saved_custom_table: The saved_custom_table of this UpdateCustomTableDetails.
        :type: oci.usage_api.models.SavedCustomTable
        """
        self._saved_custom_table = saved_custom_table

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
