# Security Policy

## Project Status

LatticeHarden is a security engineering portfolio and research project. It is intended to serve as a reference platform for secure LLM system deployment patterns, infrastructure hardening, and AI security experimentation. It is not a commercial product or managed service.

## Reporting a Vulnerability

If you believe you have identified a security vulnerability in this repository, please report it by email to `bernardofla10ps4@gmail.com`.

Please include:

- a clear description of the issue
- the affected file, module, or workflow
- reproduction steps or proof-of-concept details when available
- the potential security impact

Please do not disclose suspected vulnerabilities publicly before the issue has been reviewed.

## Scope for Responsible Disclosure

Responsible disclosure is in scope for:

- source code in this repository
- infrastructure-as-code under `infra/`
- Kubernetes manifests under `k8s/`
- CI/CD workflows under `.github/workflows/`
- security controls and reference implementations under `security/` and `ai-security/`
- documentation errors that could materially misrepresent the security posture or safe usage of the repository

Out of scope:

- third-party services, dependencies, or platforms not maintained in this repository
- local development environment issues unrelated to repository code or configuration
- theoretical concerns without a concrete security impact on the repository's documented architecture or controls

## Research-Only PQC Notice

The contents of `pqc/` are research and experimentation artifacts for post-quantum cryptography evaluation. They are not intended for production use and should not be treated as validated cryptographic guidance or production-ready controls.
