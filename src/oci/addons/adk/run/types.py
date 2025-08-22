# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
ADK Run action models
"""
import json
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from pydantic_core import ValidationError

from oci.addons.adk.agent_error import AgentError
from oci.addons.adk.run.traces import Trace, TraceType
from oci.addons.adk.logger import default_logger as logger


class FunctionCall(BaseModel):
    """Represents a function call that is required from the client."""

    name: str = Field(..., alias="name")
    arguments: str | dict = Field(..., alias="arguments")


class PerformedAction(BaseModel):
    """Represents an action that was performed by the agent."""

    action_id: str = Field(..., alias="action_id")
    performed_action_type: str = Field(..., alias="performed_action_type")
    function_call_output: str = Field(..., alias="function_call_output")


class RequiredAction(BaseModel):
    """Represents an action that is required from the client."""

    action_id: str = Field(..., alias="action_id")
    required_action_type: str = Field(..., alias="required_action_type")
    function_call: FunctionCall = Field(..., alias="function_call")


class ContentModeration(BaseModel):
    """Represents content moderation from server."""

    violence: float = Field(..., ge=0.0, le=1.0, description="Level of violence content")


class PromptInjection(BaseModel):
    """Represents prompt injection violation from server."""

    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score for prompt injection detection")


class PersonallyIdentifiableInformation(BaseModel):
    """Represents personally identifiable information from server."""

    length: int = Field(..., ge=0, description="Length of the detected entity")
    offset: int = Field(..., ge=0, description="Character offset in the original text")
    text: str = Field(..., description="The actual detected text")
    label: str = Field(..., description="The type of PII (e.g., TELEPHONE_NUMBER, EMAIL)")
    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score of detection")


class GuardrailFinding(BaseModel):
    """Represents guardrail input or output content from server."""

    content_moderation: Optional[ContentModeration] = Field(None, alias="contentModeration")
    personally_identifiable_information: Optional[List[PersonallyIdentifiableInformation]] | None = Field(None, alias="personallyIdentifiableInformation")
    prompt_injection: Optional[PromptInjection] = Field(None, alias="promptInjection")


class GuardrailResult(BaseModel):
    """Represents guardrail result from server."""

    input: Optional[GuardrailFinding] = Field(None, description="Input guardrail result of agent response.")
    output: Optional[GuardrailFinding] = Field(None, description="Output guardrail result of agent response.")


class RawResponse(BaseModel):
    """Represents an action that is required from the client."""
    raw_data: Dict[str, Any] = Field(..., alias="raw_data")

    def get_traces(self) -> List[Trace]:
        """Safely extract traces from agent response."""
        traces: List[Trace] = []
        if self.raw_data.get("traces") is None or not self.raw_data.get("traces"):
            return traces

        for trace_data in self.raw_data.get("traces", []):
            try:
                trace_type_str = trace_data.get("trace_type")
                trace_type = TraceType(trace_type_str)
                trace_cls = trace_type.get_class()

                if not trace_cls:
                    continue

                trace = trace_cls.model_validate(trace_data)
                traces.append(trace)
            except (ValidationError, ValueError) as e:
                logger.debug(f"Failed to parse trace data with error: {str(e)} | Data: {trace_data}")
                continue

        return traces

    def get_guardrail_result(self) -> GuardrailResult | None:
        """Safely extract guardrail result (a JSON encoded string) from agent response."""
        try:
            return GuardrailResult.model_validate(json.loads(self.raw_data["guardrail_result"])) if self.raw_data["guardrail_result"] else None
        except (KeyError, TypeError, ValidationError):
            return None

    def get_required_action(self) -> List[RequiredAction] | None:
        """Safely extract required action result from agent response."""
        try:
            required_actions: List[RequiredAction] = [RequiredAction.model_validate(item) for item in
                                                      self.raw_data["required_actions"]]
            return required_actions
        except (KeyError, TypeError, ValidationError):
            return None

    def get_nested_text(self) -> str | None:
        """Safely extract text from nested data structure."""
        try:
            if self.raw_data is None:
                raise AgentError("RunResponse raw_data cannot be none")
            return self.raw_data["message"]["content"]["text"]
        except (KeyError, TypeError, AgentError):
            return None


class InputLocationType(str, Enum):
    """Represents teh type of input location."""

    INLINE = "INLINE"
    OBJECT_STORAGE_PREFIX = "OBJECT_STORAGE_PREFIX"

    def get_class(self):
        return {
            InputLocationType.INLINE: InlineInputLocation,
            InputLocationType.OBJECT_STORAGE_PREFIX: ObjectStorageInputLocation
        }.get(self)


class InputLocation(BaseModel):
    """Represents Input Location."""

    input_location_type: InputLocationType

    def to_dict(self):
        data = self.model_dump()
        data["input_location_type"] = self.input_location_type.value
        return data


class InlineInputLocation(InputLocation):
    """Represents an input location where data is provided directly as inline content."""

    input_location_type: InputLocationType = Field(default=InputLocationType.INLINE)
    content: str


class ObjectStorageInputLocation(InputLocation):
    """Represents an input location where data is stored in an object storage service."""

    input_location_type: InputLocationType = Field(default=InputLocationType.OBJECT_STORAGE_PREFIX)
    namespace_name: str
    bucket_name: str
    prefix: str
