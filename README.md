# LatticeHarden

[![CI Status](https://img.shields.io/badge/CI-in%20progress-lightgrey)](#project-status)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](#license)

LatticeHarden is a security engineering reference platform for secure end-to-end deployment of LLM-based systems.

## Project Status

LatticeHarden is currently in **Phase 0 — Foundation (April to June 2026)**. The repository skeleton, baseline documentation, and security-first architecture artifacts are in place. Infrastructure modules, application services, AI security controls, and PQC experiments remain **in progress** and should be read as planned work unless explicitly implemented in the repository.

## Architecture Overview

| Layer | Domain | Purpose | Current Status |
| --- | --- | --- | --- |
| Layer 1 | DevSecOps Platform | Secure infrastructure as code, hardened CI/CD, container and Kubernetes security baselines | Foundation and structure in progress |
| Layer 2 | Application Security | Secure API boundaries, validation, authentication patterns, and service hardening | Planned for Phase 1 |
| Layer 3 | AI Security | LLM-specific filtering, red teaming, and benchmark-driven evaluation | Planned for Phase 2 |
| Layer 4 | Post-Quantum Cryptography | Controlled PQC experimentation through trusted libraries and hybrid integration patterns | Planned for Phase 3 |

## Tech Stack

### Layer 1 — DevSecOps Platform

- Terraform >= 1.6
- AWS EKS
- AWS VPC
- AWS IAM
- AWS KMS
- AWS Secrets Manager
- Helm >= 3.12
- Docker
- Kubernetes

### Layer 2 — Application Security

- Python >= 3.11
- FastAPI >= 0.104
- Pydantic v2 >= 2.4

### Layer 3 — AI Security

- OpenAI API or Ollama
- Adversarial Robustness Toolbox (ART)
- LangChain
- spaCy
- Semgrep
- Trivy
- TruffleHog
- OWASP ZAP
- Falco
- HashiCorp Vault

### Layer 4 — Post-Quantum Cryptography

- liboqs-python
- OpenSSL 3.x with OQS provider

## Roadmap

### Phase 0 — Foundation (April to June 2026)

- Establish repository presence
- Create CI/CD security pipeline
- Produce professional baseline documentation
- Deliver repository skeleton, English README, architecture and threat model artifacts

### Phase 1 — DevSecOps + AppSec Foundation (July to September 2026)

- Build secure infrastructure and API foundation
- Add Terraform modules for VPC, EKS, IAM, and secrets
- Add FastAPI auth, rate limiting, and strict validation
- Add hardened container pipeline and initial Kubernetes security controls

### Phase 2 — Advanced Security + AI Security (October 2026 to March 2027)

- Build production-grade security posture and AI security differentiators
- Add Falco, Vault integration, pod security admission, and policy controls
- Add DAST integration, AI proxy filtering, red-team tooling, and defense benchmarks

### Phase 3 — PQC Integration + Capstone (January to December 2027)

- Integrate post-quantum cryptography experiments as a capstone layer
- Add Kyber and Dilithium modules through trusted libraries
- Add hybrid TLS experiments and PQC benchmark suites
- Deliver integrated demonstration across infrastructure, application, AI, and PQC layers

## Repository Structure

```text
lattice-harden/
├── infra/               # Terraform modules and environment definitions
├── api/                 # FastAPI service, tests, and container assets
├── k8s/                 # Kubernetes manifests, RBAC, and network policy assets
├── security/            # Security tooling configuration and threat artifacts
├── ai-security/         # LLM filtering, red-team scenarios, and benchmarks
├── pqc/                 # Post-quantum cryptography experiments
├── docs/                # ADRs, architecture, threat model, and project context
└── .github/workflows/   # CI/CD and security automation
```

See [docs/PROJECT_CONTEXT.md](/mnt/c/users/berna/lattice-harden/docs/PROJECT_CONTEXT.md:1) for the full target layout and phased implementation plan.

## Local Development

Local run instructions are intentionally minimal at this stage because the repository is still in foundation work. As modules are implemented, this section will be expanded with environment prerequisites, secure local setup, and service-specific runbooks.

Expected future local workflows include:

- Python virtual environment setup for `api/` and `ai-security/`
- Terraform validation and planning for `infra/`
- Manifest validation for `k8s/`
- Security scanning and test execution through repository automation

## Security Design Philosophy

LatticeHarden is built around a security-first model in which trust boundaries, validation points, and control layering are made explicit early rather than retrofitted later. The repository prioritizes least privilege, hostile-input assumptions, and defense in depth across infrastructure, application, and AI-facing components. Security-relevant decisions are expected to remain auditable through documentation, ADRs, and tests rather than hidden behind informal convention. The project favors trusted tooling and explicit controls over convenience-driven shortcuts, especially where deployment, secrets, and cryptographic handling are involved.

## License

This repository is released under the **MIT License**.
