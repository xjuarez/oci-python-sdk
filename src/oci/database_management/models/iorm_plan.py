# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IormPlan(object):
    """
    The IORM plan from an Exadata storage server.
    """

    #: A constant which can be used with the plan_status property of a IormPlan.
    #: This constant has a value of "ACTIVE"
    PLAN_STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the plan_status property of a IormPlan.
    #: This constant has a value of "INACTIVE"
    PLAN_STATUS_INACTIVE = "INACTIVE"

    #: A constant which can be used with the plan_status property of a IormPlan.
    #: This constant has a value of "OTHER"
    PLAN_STATUS_OTHER = "OTHER"

    #: A constant which can be used with the plan_objective property of a IormPlan.
    #: This constant has a value of "AUTO"
    PLAN_OBJECTIVE_AUTO = "AUTO"

    #: A constant which can be used with the plan_objective property of a IormPlan.
    #: This constant has a value of "HIGH_THROUGHPUT"
    PLAN_OBJECTIVE_HIGH_THROUGHPUT = "HIGH_THROUGHPUT"

    #: A constant which can be used with the plan_objective property of a IormPlan.
    #: This constant has a value of "LOW_LATENCY"
    PLAN_OBJECTIVE_LOW_LATENCY = "LOW_LATENCY"

    #: A constant which can be used with the plan_objective property of a IormPlan.
    #: This constant has a value of "BALANCED"
    PLAN_OBJECTIVE_BALANCED = "BALANCED"

    #: A constant which can be used with the plan_objective property of a IormPlan.
    #: This constant has a value of "BASIC"
    PLAN_OBJECTIVE_BASIC = "BASIC"

    #: A constant which can be used with the plan_objective property of a IormPlan.
    #: This constant has a value of "OTHER"
    PLAN_OBJECTIVE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new IormPlan object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_status:
            The value to assign to the plan_status property of this IormPlan.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type plan_status: str

        :param plan_objective:
            The value to assign to the plan_objective property of this IormPlan.
            Allowed values for this property are: "AUTO", "HIGH_THROUGHPUT", "LOW_LATENCY", "BALANCED", "BASIC", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type plan_objective: str

        :param db_plan:
            The value to assign to the db_plan property of this IormPlan.
        :type db_plan: oci.database_management.models.DatabasePlan

        """
        self.swagger_types = {
            'plan_status': 'str',
            'plan_objective': 'str',
            'db_plan': 'DatabasePlan'
        }

        self.attribute_map = {
            'plan_status': 'planStatus',
            'plan_objective': 'planObjective',
            'db_plan': 'dbPlan'
        }

        self._plan_status = None
        self._plan_objective = None
        self._db_plan = None

    @property
    def plan_status(self):
        """
        **[Required]** Gets the plan_status of this IormPlan.
        The status of the IORM plan.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The plan_status of this IormPlan.
        :rtype: str
        """
        return self._plan_status

    @plan_status.setter
    def plan_status(self, plan_status):
        """
        Sets the plan_status of this IormPlan.
        The status of the IORM plan.


        :param plan_status: The plan_status of this IormPlan.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "OTHER"]
        if not value_allowed_none_or_none_sentinel(plan_status, allowed_values):
            plan_status = 'UNKNOWN_ENUM_VALUE'
        self._plan_status = plan_status

    @property
    def plan_objective(self):
        """
        **[Required]** Gets the plan_objective of this IormPlan.
        The objective of the IORM plan.

        Allowed values for this property are: "AUTO", "HIGH_THROUGHPUT", "LOW_LATENCY", "BALANCED", "BASIC", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The plan_objective of this IormPlan.
        :rtype: str
        """
        return self._plan_objective

    @plan_objective.setter
    def plan_objective(self, plan_objective):
        """
        Sets the plan_objective of this IormPlan.
        The objective of the IORM plan.


        :param plan_objective: The plan_objective of this IormPlan.
        :type: str
        """
        allowed_values = ["AUTO", "HIGH_THROUGHPUT", "LOW_LATENCY", "BALANCED", "BASIC", "OTHER"]
        if not value_allowed_none_or_none_sentinel(plan_objective, allowed_values):
            plan_objective = 'UNKNOWN_ENUM_VALUE'
        self._plan_objective = plan_objective

    @property
    def db_plan(self):
        """
        Gets the db_plan of this IormPlan.

        :return: The db_plan of this IormPlan.
        :rtype: oci.database_management.models.DatabasePlan
        """
        return self._db_plan

    @db_plan.setter
    def db_plan(self, db_plan):
        """
        Sets the db_plan of this IormPlan.

        :param db_plan: The db_plan of this IormPlan.
        :type: oci.database_management.models.DatabasePlan
        """
        self._db_plan = db_plan

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
