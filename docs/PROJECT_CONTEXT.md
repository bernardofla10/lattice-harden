# PROJECT_CONTEXT.md

## Status

This document describes the target architecture and phased implementation plan for LatticeHarden. It is a planning and alignment artifact, not a claim that every module below already exists in the repository today.

## Overview

LatticeHarden is an open-source security engineering portfolio project that demonstrates secure end-to-end deployment of LLM-based applications.

It is not intended to be a lightweight product. It is a reference platform designed to showcase deep technical competency across multiple security domains inside one coherent repository.

The project is intentionally over-engineered for its use case so it can demonstrate a wide range of practical security engineering patterns.

---

## Strategic Objective

The project exists to demonstrate competency across four connected areas:

1. DevSecOps platform security
2. Application security
3. AI security
4. Post-quantum cryptography integration

The value of the project is not only the final system, but the visibility of the reasoning behind each security decision.

This means the repository should communicate:
- threat awareness
- secure defaults
- layered controls
- sound trade-off analysis
- engineering maturity

---

## Architectural Layers

### Layer 1 — DevSecOps Platform
Purpose:
- secure infrastructure as code
- hardened CI/CD with security gates
- container and runtime hardening
- secure Kubernetes deployment patterns

Representative capabilities:
- Terraform-based AWS provisioning
- least-privilege IAM
- KMS-backed encryption strategy
- secret-management integration
- EKS hardening
- security validation in delivery pipelines

### Layer 2 — Application Security
Purpose:
- secure API design
- strong validation and auth boundaries
- threat-informed service implementation
- secure middleware and API defenses

Representative capabilities:
- FastAPI with strict input validation
- JWT and OAuth2-based auth patterns
- rate limiting
- request sanitization
- SAST/DAST integration
- OWASP Top 10-driven design decisions

### Layer 3 — AI Security
Purpose:
- protect LLM workflows against common attack classes
- evaluate attack/defense effectiveness
- demonstrate practical AI red-teaming patterns

Representative capabilities:
- prompt injection detection
- PII redaction
- output filtering
- jailbreak and data-extraction attack scenarios
- adversarial ML experiments using ART
- benchmark-driven evaluation before and after defenses

### Layer 4 — Post-Quantum Cryptography
Purpose:
- demonstrate secure adoption of post-quantum tooling
- benchmark performance and trade-offs
- connect classical and PQC techniques in a hybrid model

Representative capabilities:
- Kyber-based key encapsulation via trusted libraries
- Dilithium-based signatures via trusted libraries
- hybrid TLS experiments
- performance comparison across classical and PQC approaches

---

## Target Repository Structure

```text
lattice-harden/
├── infra/                    # Terraform — AWS infrastructure as code
│   ├── modules/
│   │   ├── vpc/
│   │   ├── eks/
│   │   ├── iam/
│   │   └── secrets/
│   ├── environments/
│   │   ├── dev/
│   │   └── prod/
│   └── README.md
│
├── api/                      # FastAPI application
│   ├── app/
│   │   ├── main.py
│   │   ├── auth/
│   │   ├── middleware/
│   │   ├── routes/
│   │   └── models/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/                      # Kubernetes manifests
│   ├── base/
│   ├── overlays/
│   ├── rbac/
│   ├── network-policies/
│   └── pod-security/
│
├── security/                 # Security tooling and documentation
│   ├── threat-model/
│   ├── semgrep-rules/
│   ├── trivy-config/
│   └── dast/
│
├── ai-security/              # AI Security layer
│   ├── proxy/
│   │   ├── filters/
│   │   │   ├── prompt_injection.py
│   │   │   ├── pii_redactor.py
│   │   │   └── output_filter.py
│   │   └── main.py
│   ├── red_team/
│   │   ├── attacks/
│   │   │   ├── prompt_injection/
│   │   │   ├── jailbreak/
│   │   │   └── data_extraction/
│   │   └── adversarial/
│   └── benchmarks/
│
├── pqc/                      # Post-Quantum Cryptography module
│   ├── kyber/
│   ├── dilithium/
│   ├── hybrid_tls/
│   └── benchmarks/
│
├── docs/
│   ├── adr/
│   ├── PROJECT_CONTEXT.md
│   ├── threat-model.md
│   └── architecture.md
│
└── .github/
    └── workflows/
        ├── security.yml
        ├── container.yml
        └── deploy.yml
```

This is the intended repository layout as the project matures.

---

## Technology Stack

### Infrastructure
- Terraform >= 1.6
- AWS EKS
- AWS VPC
- AWS IAM
- AWS KMS
- AWS Secrets Manager
- Helm >= 3.12

### Application
- Python >= 3.11
- FastAPI >= 0.104
- Pydantic v2 >= 2.4
- Docker

### Security Tooling
- Semgrep
- Trivy
- TruffleHog
- OWASP ZAP
- Falco
- HashiCorp Vault

### AI Security
- OpenAI API or Ollama
- Adversarial Robustness Toolbox (ART)
- LangChain
- spaCy

### Post-Quantum Cryptography
- liboqs-python
- OpenSSL 3.x with OQS provider

---

## Core Security Principles

These principles should shape implementation decisions across the codebase.

### Secrets management
- Secrets must never be hardcoded.
- The project should rely on managed secret stores and controlled injection mechanisms.
- Terraform state must be protected with encryption and locking.

### Least privilege
- Every identity, service account, and policy should have only the permissions it actually needs.
- Wildcards should be treated as exceptions, not defaults.
- Network access should follow zero-trust assumptions.

### Input validation
- External inputs must be validated strictly.
- Dangerous operations should not be constructed directly from user input.
- Validation should occur as early as possible.

### Defense in depth
- Security controls should exist at multiple layers.
- A control bypass should not collapse the entire system.

### Decision traceability
- Security-relevant choices should be explained.
- Non-obvious trade-offs should be recorded in ADRs.

---

## Development Roadmap

### Phase 0 — Foundation (April to June 2026)
Goal:
- establish repository presence
- create CI/CD security pipeline
- produce professional baseline documentation

Deliverables:
- full repository skeleton
- English README
- `security.yml` with Semgrep, Trivy, and TruffleHog on every PR
- `docs/architecture.md`
- `docs/threat-model.md`
- basic FastAPI service for pipeline scanning

Parallel study track:
- ISC2 CC

### Phase 1 — DevSecOps + AppSec Foundation (July to September 2026)
Goal:
- build secure working infrastructure and API foundation

Deliverables:
- Terraform modules for VPC, EKS, IAM, and secrets
- FastAPI auth, rate limiting, and strict validation
- hardened Docker build strategy
- `container.yml` with image build and Trivy scan
- initial K8s deployment with RBAC and NetworkPolicies
- OWASP Top 10 coverage documented in threat-model artifacts

Parallel study track:
- AWS Solutions Architect Associate (SAA-C03)

### Phase 2 — Advanced Security + AI Security (October 2026 to March 2027)
Goal:
- build production-grade security posture and AI security differentiators

Deliverables:
- Falco, Vault integration, pod security admission, OPA/Gatekeeper
- DAST integration in staging
- `ai-security/proxy/` with prompt injection detection, PII redaction, and output filtering
- `ai-security/red_team/` attack tooling
- `ai-security/benchmarks/` reproducible evaluation of defenses

Parallel study track:
- CKA
- CKS

### Phase 3 — PQC Integration + Capstone (January to December 2027)
Goal:
- complete the platform and integrate PQC as a capstone differentiator

Deliverables:
- `pqc/` modules for Kyber and Dilithium through trusted libraries
- `pqc/hybrid_tls/` hybrid TLS experiments
- `pqc/benchmarks/` for latency, throughput, and key-size comparisons
- complete integrated demonstration across all layers
- full README refresh with architecture, controls, and attack scenarios

Parallel study track:
- AWS Security Specialty
- eWPTv2 or BSCP

---

## Coding and Documentation Conventions

### Python
- Type hints are mandatory.
- Pydantic models should represent external inputs.
- Security-relevant modules should explain purpose and threat mitigated.
- Static and security analysis should pass before merge.

Recommended module header pattern:

```python
"""
Module: prompt_injection.py
Purpose: Detect prompt injection attempts in LLM inputs before forwarding to the model.
Threat mitigated: An attacker embedding instructions in user input that override
                  system-level instructions or exfiltrate data.
Reference: OWASP LLM Top 10 — LLM01: Prompt Injection
"""
```

### Terraform
- Security-relevant resources should document what they protect.
- Use data sources instead of hardcoded machine identifiers.
- Use remote state with encryption and locking.

### Kubernetes
- Non-root execution should be the default.
- Read-only filesystem should be the default.
- Privilege escalation should be disabled by default.
- Resource requests and limits should always be declared.

### Git history
Use Conventional Commits to keep changes legible and categorized.

---

## Explicit Anti-Patterns

The following are intentionally out of scope or prohibited:

- low-code automation platforms such as n8n or Zapier inside this repository
- `latest` Docker tags
- storing credentials in the repository
- implementing cryptography from scratch
- shipping untested security controls
- deploying unvalidated manifests in CI/CD

These are not stylistic preferences. They are project constraints.

---

## ADR Guidance

All significant architectural decisions should be documented in `docs/adr/`.

Recommended format:

```md
# ADR-001: Title

## Status
Proposed | Accepted | Deprecated

## Context
What problem are we solving? What are the constraints?

## Decision
What did we decide?

## Security rationale
Why is this decision the more secure choice? What threat does it mitigate?

## Trade-offs
What are we giving up? What complexity does this add?

## Alternatives considered
What else did we evaluate and why did we reject it?
```

---

## Maintainer Intent

This project should feel like a coherent security engineering platform, not a random collection of demos.

Every addition should reinforce at least one of these qualities:
- security depth
- architectural discipline
- clear threat rationale
- practical credibility
- long-term capstone coherence

The project is allowed to be ambitious and layered. It is not allowed to be sloppy, arbitrary, or security-theater.
