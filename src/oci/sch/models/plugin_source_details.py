# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200909

from .source_details import SourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PluginSourceDetails(SourceDetails):
    """
    Details about a connector plugin used to fetch data from a source.
    For configuration instructions, see
    `Creating a Connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/connector-hub/create-service-connector.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PluginSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.PluginSourceDetails.kind` attribute
        of this class is ``plugin`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this PluginSourceDetails.
            Allowed values for this property are: "logging", "monitoring", "streaming", "plugin"
        :type kind: str

        :param plugin_name:
            The value to assign to the plugin_name property of this PluginSourceDetails.
        :type plugin_name: str

        :param config_map:
            The value to assign to the config_map property of this PluginSourceDetails.
        :type config_map: object

        """
        self.swagger_types = {
            'kind': 'str',
            'plugin_name': 'str',
            'config_map': 'object'
        }

        self.attribute_map = {
            'kind': 'kind',
            'plugin_name': 'pluginName',
            'config_map': 'configMap'
        }

        self._kind = None
        self._plugin_name = None
        self._config_map = None
        self._kind = 'plugin'

    @property
    def plugin_name(self):
        """
        **[Required]** Gets the plugin_name of this PluginSourceDetails.
        The name of the connector plugin. This name indicates the service to be called by the connector plugin. For example, `QueueSource` indicates the Queue service.
        To find names of connector plugins, list the plugin using (ListConnectorPlugin)[#/en/serviceconnectors/latest/ConnectorPluginSummary/ListConnectorPlugins].


        :return: The plugin_name of this PluginSourceDetails.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """
        Sets the plugin_name of this PluginSourceDetails.
        The name of the connector plugin. This name indicates the service to be called by the connector plugin. For example, `QueueSource` indicates the Queue service.
        To find names of connector plugins, list the plugin using (ListConnectorPlugin)[#/en/serviceconnectors/latest/ConnectorPluginSummary/ListConnectorPlugins].


        :param plugin_name: The plugin_name of this PluginSourceDetails.
        :type: str
        """
        self._plugin_name = plugin_name

    @property
    def config_map(self):
        """
        **[Required]** Gets the config_map of this PluginSourceDetails.
        The configuration map for the connector plugin. This map includes parameters specific to the connector plugin type.
        For example, for `QueueSource`, the map lists the OCID of the selected queue.
        To find the parameters for a connector plugin, get the plugin using (GetConnectorPlugin)[#/en/serviceconnectors/latest/ConnectorPlugin/GetConnectorPlugin] and review its schema value.


        :return: The config_map of this PluginSourceDetails.
        :rtype: object
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """
        Sets the config_map of this PluginSourceDetails.
        The configuration map for the connector plugin. This map includes parameters specific to the connector plugin type.
        For example, for `QueueSource`, the map lists the OCID of the selected queue.
        To find the parameters for a connector plugin, get the plugin using (GetConnectorPlugin)[#/en/serviceconnectors/latest/ConnectorPlugin/GetConnectorPlugin] and review its schema value.


        :param config_map: The config_map of this PluginSourceDetails.
        :type: object
        """
        self._config_map = config_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other