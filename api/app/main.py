"""
Module: main.py
Purpose: Provide the Phase 0 FastAPI entry point for the LatticeHarden API.
Threat mitigated: Keeping the public API surface intentionally narrow reduces
the attack surface available to anonymous clients while the platform foundation
is being established.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.health import HealthResponse

API_VERSION = "0.1.0"

app = FastAPI(title="LatticeHarden API")

app.add_middleware(
    CORSMiddleware,
    # Security rationale: permissive CORS is a common misconfiguration that can
    # expose browser clients to unintended cross-origin access; origins must be
    # explicitly allowlisted when a trusted frontend boundary exists.
    allow_origins=[],
    allow_credentials=False,
    allow_methods=[],
    allow_headers=[],
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Return a minimal health signal without exposing internal details."""
    return HealthResponse(status="ok", version=API_VERSION)
