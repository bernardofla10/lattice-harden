"""
Module: health.py
Purpose: Define the validated response contract for the health endpoint.
Threat mitigated: Explicit response models reduce accidental disclosure of
internal runtime details through loosely structured API responses.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    """Schema returned by the public health endpoint."""

    model_config = ConfigDict(extra="forbid")

    status: Literal["ok"]
    version: str
