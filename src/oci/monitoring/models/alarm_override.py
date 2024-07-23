# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmOverride(object):
    """
    Values to use for an independent evaluation of the alarm.
    You can specify values for query, severity, body, and pending duration.
    When an alarm contains overrides, the Monitoring service evaluates each override in order,
    beginning with the first override in the array (index position `0`),
    and then evaluates the alarm's base values (`ruleName` value of `BASE`)
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmOverride object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pending_duration:
            The value to assign to the pending_duration property of this AlarmOverride.
        :type pending_duration: str

        :param severity:
            The value to assign to the severity property of this AlarmOverride.
        :type severity: str

        :param body:
            The value to assign to the body property of this AlarmOverride.
        :type body: str

        :param rule_name:
            The value to assign to the rule_name property of this AlarmOverride.
        :type rule_name: str

        :param query:
            The value to assign to the query property of this AlarmOverride.
        :type query: str

        """
        self.swagger_types = {
            'pending_duration': 'str',
            'severity': 'str',
            'body': 'str',
            'rule_name': 'str',
            'query': 'str'
        }

        self.attribute_map = {
            'pending_duration': 'pendingDuration',
            'severity': 'severity',
            'body': 'body',
            'rule_name': 'ruleName',
            'query': 'query'
        }

        self._pending_duration = None
        self._severity = None
        self._body = None
        self._rule_name = None
        self._query = None

    @property
    def pending_duration(self):
        """
        Gets the pending_duration of this AlarmOverride.
        The period of time that the condition defined in the alarm must persist before the alarm state
        changes from \"OK\" to \"FIRING\". For example, a value of 5 minutes means that the
        alarm must persist in breaching the condition for five minutes before the alarm updates its
        state to \"FIRING\".

        The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
        for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M.

        Under the default value of PT1M, the first evaluation that breaches the alarm updates the
        state to \"FIRING\".

        The alarm updates its status to \"OK\" when the breaching condition has been clear for
        the most recent minute.

        Example: `PT5M`


        :return: The pending_duration of this AlarmOverride.
        :rtype: str
        """
        return self._pending_duration

    @pending_duration.setter
    def pending_duration(self, pending_duration):
        """
        Sets the pending_duration of this AlarmOverride.
        The period of time that the condition defined in the alarm must persist before the alarm state
        changes from \"OK\" to \"FIRING\". For example, a value of 5 minutes means that the
        alarm must persist in breaching the condition for five minutes before the alarm updates its
        state to \"FIRING\".

        The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
        for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M.

        Under the default value of PT1M, the first evaluation that breaches the alarm updates the
        state to \"FIRING\".

        The alarm updates its status to \"OK\" when the breaching condition has been clear for
        the most recent minute.

        Example: `PT5M`


        :param pending_duration: The pending_duration of this AlarmOverride.
        :type: str
        """
        self._pending_duration = pending_duration

    @property
    def severity(self):
        """
        Gets the severity of this AlarmOverride.
        The perceived severity of the alarm with regard to the affected system.

        Example: `CRITICAL`


        :return: The severity of this AlarmOverride.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this AlarmOverride.
        The perceived severity of the alarm with regard to the affected system.

        Example: `CRITICAL`


        :param severity: The severity of this AlarmOverride.
        :type: str
        """
        self._severity = severity

    @property
    def body(self):
        """
        Gets the body of this AlarmOverride.
        The human-readable content of the delivered alarm notification.
        Optionally include `dynamic variables`__.
        Oracle recommends providing guidance
        to operators for resolving the alarm condition. Consider adding links to standard runbook
        practices. Avoid entering confidential information.

        Example: `High CPU usage alert. Follow runbook instructions for resolution.`

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm


        :return: The body of this AlarmOverride.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this AlarmOverride.
        The human-readable content of the delivered alarm notification.
        Optionally include `dynamic variables`__.
        Oracle recommends providing guidance
        to operators for resolving the alarm condition. Consider adding links to standard runbook
        practices. Avoid entering confidential information.

        Example: `High CPU usage alert. Follow runbook instructions for resolution.`

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm


        :param body: The body of this AlarmOverride.
        :type: str
        """
        self._body = body

    @property
    def rule_name(self):
        """
        Gets the rule_name of this AlarmOverride.
        A user-friendly description for this alarm override. Must be unique across all `ruleName` values for the alarm.


        :return: The rule_name of this AlarmOverride.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """
        Sets the rule_name of this AlarmOverride.
        A user-friendly description for this alarm override. Must be unique across all `ruleName` values for the alarm.


        :param rule_name: The rule_name of this AlarmOverride.
        :type: str
        """
        self._rule_name = rule_name

    @property
    def query(self):
        """
        Gets the query of this AlarmOverride.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval depend on the specified time range. More
        interval values are supported for smaller time ranges. You can optionally
        specify dimensions and grouping functions.
        Also, you can customize the
        `absence detection period`__.
        Supported grouping functions: `grouping()`, `groupBy()`.
        For information about writing MQL expressions, see
        `Editing the MQL Expression for a Query`__.
        For details about MQL, see
        `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service. See
        `Supported Services`__.

        Example of threshold alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

          -----

        Example of absence alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

          -----
        Example of absence alarm with custom absence detection period of 20 hours:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent(20h)

          -----

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :return: The query of this AlarmOverride.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this AlarmOverride.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval depend on the specified time range. More
        interval values are supported for smaller time ranges. You can optionally
        specify dimensions and grouping functions.
        Also, you can customize the
        `absence detection period`__.
        Supported grouping functions: `grouping()`, `groupBy()`.
        For information about writing MQL expressions, see
        `Editing the MQL Expression for a Query`__.
        For details about MQL, see
        `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service. See
        `Supported Services`__.

        Example of threshold alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

          -----

        Example of absence alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

          -----
        Example of absence alarm with custom absence detection period of 20 hours:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent(20h)

          -----

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :param query: The query of this AlarmOverride.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
