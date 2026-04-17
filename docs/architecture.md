# Architecture

## Status

This document describes the target architecture for LatticeHarden's initial foundation. It is intended to guide implementation and documentation as the repository grows from the current baseline.

## Overview

LatticeHarden is an open-source security engineering portfolio platform built to demonstrate secure end-to-end deployment of LLM-based systems. The repository is intentionally designed as a reference implementation, not a minimal product, so that security rationale, controls, and trade-offs remain visible and auditable.

The architecture is organized around four layers:

1. DevSecOps platform security
2. Application security
3. AI security
4. Post-quantum cryptography experimentation

Each layer must remain aligned with the repository-wide priorities defined in [AGENTS.md](/mnt/c/Users/berna/lattice-harden/AGENTS.md:1):

1. Security
2. Correctness
3. Maintainability
4. Auditability
5. Simplicity
6. Speed of implementation

## Architectural Goals

The platform should:

- demonstrate secure-by-default engineering patterns across infrastructure, application, and AI boundaries
- make non-obvious security decisions easy to inspect through code, tests, and ADRs
- constrain blast radius when a single control fails
- separate concerns so that controls can be verified independently
- prefer well-known, trusted tooling over ad hoc security mechanisms

## Target Repository Layout

The repository is expected to evolve toward the following structure:

```text
lattice-harden/
├── infra/                    # Terraform for cloud infrastructure
├── api/                      # FastAPI application and tests
├── k8s/                      # Kubernetes manifests and policies
├── security/                 # Security tooling, rules, and DAST assets
├── ai-security/              # LLM filtering, red team, and benchmarks
├── pqc/                      # Post-quantum cryptography experiments
├── docs/
│   ├── adr/
│   ├── architecture.md
│   ├── PROJECT_CONTEXT.md
│   └── threat-model.md
└── .github/workflows/        # CI/CD and security automation
```

This is a target layout, not a claim that all modules are already implemented.

## Layered Design

### Layer 1: DevSecOps Platform Security

This layer establishes the trusted execution foundation for the rest of the system.

Primary responsibilities:

- define infrastructure as code using Terraform
- provision cloud resources with least-privilege IAM
- enforce encryption, network segmentation, and secret-management integrations
- validate infrastructure and manifests in CI/CD before deployment
- harden container build and runtime defaults

Representative controls:

- encrypted state and locking for real Terraform environments
- narrow IAM policies and explicit trust relationships
- hardened Kubernetes defaults such as non-root execution and read-only filesystems
- manifest validation before deploy
- image and dependency scanning in CI/CD

### Layer 2: Application Security

This layer defines the API and service boundaries that process external input.

Primary responsibilities:

- expose a narrow, validated FastAPI surface
- enforce strict input models using Pydantic v2
- keep routes thin and move reusable security logic into services or middleware
- avoid leakage of internal implementation details in errors
- enforce authentication, authorization, and abuse controls as the platform matures

Representative controls:

- strict request validation
- narrow failure modes
- rate limiting and sanitization patterns
- explicit separation between transport, validation, and business logic

### Layer 3: AI Security

This layer protects LLM-assisted workflows against attack classes that do not exist in traditional applications alone.

Primary responsibilities:

- inspect user-controlled prompts before model execution
- redact or block sensitive inputs and outputs
- measure defense effectiveness against representative attack scenarios
- document AI-specific trade-offs through repeatable tests and benchmarks

Representative controls:

- prompt injection detection
- PII redaction
- output filtering
- red-team scenarios for jailbreak, prompt injection, and data extraction

### Layer 4: Post-Quantum Cryptography

This layer demonstrates controlled adoption of post-quantum tools without inventing cryptographic primitives.

Primary responsibilities:

- evaluate trusted PQC libraries and integration patterns
- compare hybrid and classical approaches
- document operational and performance trade-offs

Representative controls:

- use trusted libraries rather than custom implementations
- isolate experiments from core application security assumptions
- benchmark latency, throughput, and interoperability impacts

## Trust Boundaries

The system should be designed around explicit trust boundaries:

1. External users and clients are untrusted.
2. Public API ingress is untrusted until validated.
3. Internal services are not automatically trusted; access should be authenticated and narrowly scoped.
4. LLM inputs and outputs are untrusted data flows and must be filtered accordingly.
5. CI/CD is a privileged path and must enforce validation before artifacts reach runtime environments.
6. Cloud control plane and secret stores are trusted only through tightly scoped identities and audited access paths.

## Security Design Principles

The following principles govern architecture choices:

- validate early and explicitly
- assume hostile input at every external boundary
- favor defense in depth over single-point controls
- minimize privileges for identities, workloads, and network paths
- prefer managed, auditable controls over bespoke mechanisms
- ensure every meaningful control is testable
- record non-obvious decisions in ADRs

## Deployment View

At maturity, the expected deployment flow is:

1. Code changes are pushed through pull requests.
2. CI/CD runs security checks such as Semgrep, Trivy, secret scanning, and manifest validation.
3. Container images are built from pinned, hardened bases.
4. Infrastructure and Kubernetes resources are validated before deployment.
5. Runtime workloads execute with restricted privileges and explicit network policies.
6. LLM-facing paths apply security filtering before and after model invocation.

## Non-Goals

The architecture intentionally does not optimize for:

- minimal implementation size at the expense of security clarity
- rapid feature delivery that bypasses validation or review
- undocumented shortcuts that broaden privilege or reduce auditability
- custom cryptographic primitives

## Documentation Requirements

When the architecture changes materially:

- update this document
- update the threat model if trust boundaries or attack surfaces change
- create or revise an ADR for significant architectural decisions
- add or update tests for relevant controls
