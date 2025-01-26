# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_pipeline_details import UpdatePipelineDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateZeroEtlPipelineDetails(UpdatePipelineDetails):
    """
    Information to update for an existing ZeroETL pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateZeroEtlPipelineDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateZeroEtlPipelineDetails.recipe_type` attribute
        of this class is ``ZERO_ETL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recipe_type:
            The value to assign to the recipe_type property of this UpdateZeroEtlPipelineDetails.
            Allowed values for this property are: "ZERO_ETL"
        :type recipe_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateZeroEtlPipelineDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateZeroEtlPipelineDetails.
        :type description: str

        :param license_model:
            The value to assign to the license_model property of this UpdateZeroEtlPipelineDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateZeroEtlPipelineDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateZeroEtlPipelineDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param process_options:
            The value to assign to the process_options property of this UpdateZeroEtlPipelineDetails.
        :type process_options: oci.golden_gate.models.ProcessOptions

        :param mapping_rules:
            The value to assign to the mapping_rules property of this UpdateZeroEtlPipelineDetails.
        :type mapping_rules: list[oci.golden_gate.models.MappingRule]

        """
        self.swagger_types = {
            'recipe_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'license_model': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'process_options': 'ProcessOptions',
            'mapping_rules': 'list[MappingRule]'
        }

        self.attribute_map = {
            'recipe_type': 'recipeType',
            'display_name': 'displayName',
            'description': 'description',
            'license_model': 'licenseModel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'process_options': 'processOptions',
            'mapping_rules': 'mappingRules'
        }

        self._recipe_type = None
        self._display_name = None
        self._description = None
        self._license_model = None
        self._freeform_tags = None
        self._defined_tags = None
        self._process_options = None
        self._mapping_rules = None
        self._recipe_type = 'ZERO_ETL'

    @property
    def process_options(self):
        """
        Gets the process_options of this UpdateZeroEtlPipelineDetails.

        :return: The process_options of this UpdateZeroEtlPipelineDetails.
        :rtype: oci.golden_gate.models.ProcessOptions
        """
        return self._process_options

    @process_options.setter
    def process_options(self, process_options):
        """
        Sets the process_options of this UpdateZeroEtlPipelineDetails.

        :param process_options: The process_options of this UpdateZeroEtlPipelineDetails.
        :type: oci.golden_gate.models.ProcessOptions
        """
        self._process_options = process_options

    @property
    def mapping_rules(self):
        """
        Gets the mapping_rules of this UpdateZeroEtlPipelineDetails.
        Mapping for source/target schema/tables for the pipeline data replication.


        :return: The mapping_rules of this UpdateZeroEtlPipelineDetails.
        :rtype: list[oci.golden_gate.models.MappingRule]
        """
        return self._mapping_rules

    @mapping_rules.setter
    def mapping_rules(self, mapping_rules):
        """
        Sets the mapping_rules of this UpdateZeroEtlPipelineDetails.
        Mapping for source/target schema/tables for the pipeline data replication.


        :param mapping_rules: The mapping_rules of this UpdateZeroEtlPipelineDetails.
        :type: list[oci.golden_gate.models.MappingRule]
        """
        self._mapping_rules = mapping_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
