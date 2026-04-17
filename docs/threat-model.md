# Threat Model

## Status

This document defines the initial threat model for LatticeHarden's foundation phase. It is intentionally high level and should be refined as concrete modules are implemented.

## Scope

LatticeHarden is an open-source platform intended to demonstrate secure deployment patterns for LLM-based systems. The threat model covers:

- repository and CI/CD trust assumptions
- infrastructure and deployment risks
- API-facing application risks
- AI-specific attack classes
- misuse risks introduced by future PQC experimentation

The model does not assume production traffic today. It exists to guide secure design before implementation expands.

## Security Objectives

The system should preserve:

1. Confidentiality of secrets, tokens, and sensitive user data
2. Integrity of source code, build artifacts, and deployment manifests
3. Availability of core services under reasonable abuse conditions
4. Integrity of LLM control flow and output handling
5. Auditability of security-relevant decisions and changes

## Assets

Primary assets include:

- source code and infrastructure definitions
- CI/CD workflow definitions and generated artifacts
- cloud credentials and secret references
- application authentication material
- LLM prompts, completions, and filtering logic
- security rules, findings, and benchmark data

## Threat Actors

Relevant threat actors include:

- anonymous internet attackers probing public endpoints
- malicious or careless contributors introducing unsafe changes
- automated scanners and credential harvesters targeting public repositories
- attackers attempting prompt injection, jailbreaks, or data extraction via LLM workflows
- attackers seeking privilege escalation through CI/CD, containers, or Kubernetes misconfiguration

## Trust Boundaries

The initial design recognizes these boundaries:

1. Developer workstation to repository
2. Repository to CI/CD execution
3. CI/CD to cloud or cluster deployment targets
4. External client to API ingress
5. API services to internal components
6. Application logic to LLM provider or local model runtime
7. Runtime workloads to secret stores and control-plane services

Every boundary crossing must be authenticated, validated, or otherwise constrained.

## Assumptions

The threat model assumes:

- all external input is hostile until validated
- public repositories will be continuously scanned by automated tooling
- cloud identities and CI/CD credentials are high-value targets
- LLM outputs are not inherently trustworthy
- security controls can fail and must be layered

## Primary Threats

### Supply Chain and Repository Threats

Threats:

- accidental credential exposure
- malicious dependency introduction
- unsafe workflow changes
- poisoned container bases or unpinned toolchains

Mitigations:

- no secrets in code or examples
- pinned versions where practical
- mandatory security scanning in CI/CD
- code review and ADR-backed architectural changes

### CI/CD and Artifact Integrity Threats

Threats:

- unauthorized workflow modification
- unvalidated manifests reaching deployment targets
- artifact tampering between build and deploy stages

Mitigations:

- validation gates before deploy
- explicit manifest validation
- container scanning and policy checks
- minimal permissions for automation identities

### Infrastructure Misconfiguration Threats

Threats:

- over-broad IAM permissions
- publicly exposed internal services
- unencrypted state or storage
- weak network segmentation

Mitigations:

- least-privilege IAM
- deny-by-default network posture where feasible
- encrypted state and managed secret stores
- documented security rationale for exceptions

### Application Security Threats

Threats:

- injection through unvalidated inputs
- broken authentication or authorization boundaries
- sensitive error leakage
- abuse through missing rate limits or insufficient request controls

Mitigations:

- strict Pydantic validation
- thin routes and reusable middleware or services
- narrow error handling
- test coverage for security-relevant controls

### AI Security Threats

Threats:

- prompt injection
- jailbreak attempts
- data extraction through model manipulation
- sensitive data disclosure in prompts or outputs
- unsafe tool invocation triggered by model-influenced content

Mitigations:

- prompt filtering before model execution
- output filtering and redaction
- benchmarked attack/defense testing
- explicit separation between validated inputs, model calls, and post-processing

### Kubernetes and Runtime Threats

Threats:

- container escape amplification through weak runtime settings
- lateral movement across namespaces or services
- privilege escalation inside workloads

Mitigations:

- `runAsNonRoot: true`
- `readOnlyRootFilesystem: true`
- `allowPrivilegeEscalation: false`
- declared resource requests and limits
- minimal RBAC and restrictive network policies

### PQC Experimentation Risks

Threats:

- misleading security claims from immature integrations
- incorrect use of experimental cryptographic tooling
- operational instability from hybrid experiments

Mitigations:

- use trusted libraries only
- treat PQC work as explicit experimentation until validated
- document trade-offs and benchmark impacts

## Abuse Cases

Representative abuse cases the project should eventually test:

1. A user submits input designed to override system instructions in an LLM workflow.
2. A contributor introduces a workflow change that weakens scanning or validation.
3. A container or manifest is configured with unnecessary privilege.
4. A route accepts raw user input and passes it to a dangerous sink without validation.
5. A secret is accidentally added to code, examples, or commit history.

## Control Failure Analysis

If a single control fails:

- validation failures should still be constrained by downstream business logic and runtime permissions
- CI/CD bypass should still face repository review, scanning in adjacent stages, and deployment policy checks
- prompt filtering failure should still be constrained by output filtering and narrow tool permissions
- runtime compromise should still face namespace, RBAC, and network boundaries

This reflects the repository requirement for defense in depth rather than reliance on one guardrail.

## Validation Strategy

Security controls are only meaningful if tested. As implementation progresses, the project should maintain:

- unit tests for validation and filtering logic
- integration tests for auth, API boundaries, and middleware behavior
- CI/CD checks for static analysis, secrets detection, and artifact scanning
- manifest validation before deployment
- AI red-team and benchmark scenarios for defense effectiveness

## Open Questions

These questions should be resolved through ADRs and implementation:

- what authentication model is used for public and internal APIs
- what secret-management path is used in each environment
- what deployment promotion model is trusted in CI/CD
- what model provider trust assumptions apply to AI workloads
- what PQC experiments remain isolated from production-like paths
