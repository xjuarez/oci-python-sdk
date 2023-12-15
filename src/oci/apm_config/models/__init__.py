# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210201

from __future__ import absolute_import

from .apdex import Apdex
from .apdex_rules import ApdexRules
from .apdex_rules_summary import ApdexRulesSummary
from .config import Config
from .config_collection import ConfigCollection
from .config_summary import ConfigSummary
from .create_apdex_rules_details import CreateApdexRulesDetails
from .create_config_details import CreateConfigDetails
from .create_metric_group_details import CreateMetricGroupDetails
from .create_options_details import CreateOptionsDetails
from .create_span_filter_details import CreateSpanFilterDetails
from .dimension import Dimension
from .metric import Metric
from .metric_group import MetricGroup
from .metric_group_summary import MetricGroupSummary
from .namespace import Namespace
from .namespace_collection import NamespaceCollection
from .namespace_metric import NamespaceMetric
from .namespace_metric_collection import NamespaceMetricCollection
from .options import Options
from .options_summary import OptionsSummary
from .retrieve_namespace_metrics_details import RetrieveNamespaceMetricsDetails
from .span_filter import SpanFilter
from .span_filter_reference import SpanFilterReference
from .span_filter_summary import SpanFilterSummary
from .update_apdex_rules_details import UpdateApdexRulesDetails
from .update_config_details import UpdateConfigDetails
from .update_metric_group_details import UpdateMetricGroupDetails
from .update_options_details import UpdateOptionsDetails
from .update_span_filter_details import UpdateSpanFilterDetails
from .validate_span_filter_pattern_details import ValidateSpanFilterPatternDetails

# Maps type names to classes for apm_config services.
apm_config_type_mapping = {
    "Apdex": Apdex,
    "ApdexRules": ApdexRules,
    "ApdexRulesSummary": ApdexRulesSummary,
    "Config": Config,
    "ConfigCollection": ConfigCollection,
    "ConfigSummary": ConfigSummary,
    "CreateApdexRulesDetails": CreateApdexRulesDetails,
    "CreateConfigDetails": CreateConfigDetails,
    "CreateMetricGroupDetails": CreateMetricGroupDetails,
    "CreateOptionsDetails": CreateOptionsDetails,
    "CreateSpanFilterDetails": CreateSpanFilterDetails,
    "Dimension": Dimension,
    "Metric": Metric,
    "MetricGroup": MetricGroup,
    "MetricGroupSummary": MetricGroupSummary,
    "Namespace": Namespace,
    "NamespaceCollection": NamespaceCollection,
    "NamespaceMetric": NamespaceMetric,
    "NamespaceMetricCollection": NamespaceMetricCollection,
    "Options": Options,
    "OptionsSummary": OptionsSummary,
    "RetrieveNamespaceMetricsDetails": RetrieveNamespaceMetricsDetails,
    "SpanFilter": SpanFilter,
    "SpanFilterReference": SpanFilterReference,
    "SpanFilterSummary": SpanFilterSummary,
    "UpdateApdexRulesDetails": UpdateApdexRulesDetails,
    "UpdateConfigDetails": UpdateConfigDetails,
    "UpdateMetricGroupDetails": UpdateMetricGroupDetails,
    "UpdateOptionsDetails": UpdateOptionsDetails,
    "UpdateSpanFilterDetails": UpdateSpanFilterDetails,
    "ValidateSpanFilterPatternDetails": ValidateSpanFilterPatternDetails
}
