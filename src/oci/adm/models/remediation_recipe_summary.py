# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemediationRecipeSummary(object):
    """
    The summary of a Remediation Recipe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemediationRecipeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RemediationRecipeSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this RemediationRecipeSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this RemediationRecipeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RemediationRecipeSummary.
        :type time_updated: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this RemediationRecipeSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RemediationRecipeSummary.
        :type lifecycle_state: str

        :param knowledge_base_id:
            The value to assign to the knowledge_base_id property of this RemediationRecipeSummary.
        :type knowledge_base_id: str

        :param is_run_triggered_on_kb_change:
            The value to assign to the is_run_triggered_on_kb_change property of this RemediationRecipeSummary.
        :type is_run_triggered_on_kb_change: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RemediationRecipeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RemediationRecipeSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RemediationRecipeSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'knowledge_base_id': 'str',
            'is_run_triggered_on_kb_change': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'knowledge_base_id': 'knowledgeBaseId',
            'is_run_triggered_on_kb_change': 'isRunTriggeredOnKbChange',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._knowledge_base_id = None
        self._is_run_triggered_on_kb_change = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RemediationRecipeSummary.
        The Oracle Cloud Identifier (`OCID`__) of the remediation recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this RemediationRecipeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RemediationRecipeSummary.
        The Oracle Cloud Identifier (`OCID`__) of the remediation recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this RemediationRecipeSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RemediationRecipeSummary.
        The name of the Remediation Recipe.


        :return: The display_name of this RemediationRecipeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RemediationRecipeSummary.
        The name of the Remediation Recipe.


        :param display_name: The display_name of this RemediationRecipeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this RemediationRecipeSummary.
        The creation date and time of the Remediation Recipe (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this RemediationRecipeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RemediationRecipeSummary.
        The creation date and time of the Remediation Recipe (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this RemediationRecipeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this RemediationRecipeSummary.
        The date and time the Remediation Recipe was last updated (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this RemediationRecipeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RemediationRecipeSummary.
        The date and time the Remediation Recipe was last updated (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this RemediationRecipeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RemediationRecipeSummary.
        The compartment Oracle Cloud Identifier (`OCID`__) of the remediation recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this RemediationRecipeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RemediationRecipeSummary.
        The compartment Oracle Cloud Identifier (`OCID`__) of the remediation recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this RemediationRecipeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RemediationRecipeSummary.
        The current lifecycle state of the Remediation Recipe.


        :return: The lifecycle_state of this RemediationRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RemediationRecipeSummary.
        The current lifecycle state of the Remediation Recipe.


        :param lifecycle_state: The lifecycle_state of this RemediationRecipeSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def knowledge_base_id(self):
        """
        **[Required]** Gets the knowledge_base_id of this RemediationRecipeSummary.
        The Oracle Cloud Identifier (`OCID`__) of the knowledge base.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The knowledge_base_id of this RemediationRecipeSummary.
        :rtype: str
        """
        return self._knowledge_base_id

    @knowledge_base_id.setter
    def knowledge_base_id(self, knowledge_base_id):
        """
        Sets the knowledge_base_id of this RemediationRecipeSummary.
        The Oracle Cloud Identifier (`OCID`__) of the knowledge base.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param knowledge_base_id: The knowledge_base_id of this RemediationRecipeSummary.
        :type: str
        """
        self._knowledge_base_id = knowledge_base_id

    @property
    def is_run_triggered_on_kb_change(self):
        """
        **[Required]** Gets the is_run_triggered_on_kb_change of this RemediationRecipeSummary.
        Boolean indicating if a run should be automatically triggered once the Knowledge Base is updated.


        :return: The is_run_triggered_on_kb_change of this RemediationRecipeSummary.
        :rtype: bool
        """
        return self._is_run_triggered_on_kb_change

    @is_run_triggered_on_kb_change.setter
    def is_run_triggered_on_kb_change(self, is_run_triggered_on_kb_change):
        """
        Sets the is_run_triggered_on_kb_change of this RemediationRecipeSummary.
        Boolean indicating if a run should be automatically triggered once the Knowledge Base is updated.


        :param is_run_triggered_on_kb_change: The is_run_triggered_on_kb_change of this RemediationRecipeSummary.
        :type: bool
        """
        self._is_run_triggered_on_kb_change = is_run_triggered_on_kb_change

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this RemediationRecipeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this RemediationRecipeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RemediationRecipeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this RemediationRecipeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this RemediationRecipeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this RemediationRecipeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RemediationRecipeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this RemediationRecipeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RemediationRecipeSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this RemediationRecipeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RemediationRecipeSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this RemediationRecipeSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
