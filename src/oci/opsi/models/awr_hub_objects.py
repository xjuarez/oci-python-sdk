# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrHubObjects(object):
    """
    Logical grouping used for Awr Hub Object operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrHubObjects object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param awr_snapshots:
            The value to assign to the awr_snapshots property of this AwrHubObjects.
        :type awr_snapshots: object

        """
        self.swagger_types = {
            'awr_snapshots': 'object'
        }

        self.attribute_map = {
            'awr_snapshots': 'awrSnapshots'
        }

        self._awr_snapshots = None

    @property
    def awr_snapshots(self):
        """
        Gets the awr_snapshots of this AwrHubObjects.
        Awr Hub Object.


        :return: The awr_snapshots of this AwrHubObjects.
        :rtype: object
        """
        return self._awr_snapshots

    @awr_snapshots.setter
    def awr_snapshots(self, awr_snapshots):
        """
        Sets the awr_snapshots of this AwrHubObjects.
        Awr Hub Object.


        :param awr_snapshots: The awr_snapshots of this AwrHubObjects.
        :type: object
        """
        self._awr_snapshots = awr_snapshots

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
