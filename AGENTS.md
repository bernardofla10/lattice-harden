# AGENTS.md

## Mission

LatticeHarden is an open-source security engineering portfolio platform built to demonstrate secure end-to-end deployment of LLM-based systems.

This repository is intentionally over-engineered for its use case. Do not optimize for the smallest possible implementation if that reduces the clarity, depth, or auditability of the security posture.

When making trade-offs, prioritize in this order:
1. Security
2. Correctness
3. Maintainability
4. Auditability
5. Simplicity
6. Speed of implementation

---

## How to Use This File

Use this document as the operational guide for working in the repository.

- Follow these rules before making architectural or code changes.
- If a topic requires deeper explanation, consult `docs/PROJECT_CONTEXT.md` and the documents listed in **Source of Truth**.
- If an existing ADR conflicts with an ad hoc implementation idea, the ADR wins unless the task explicitly requires revisiting that decision.

---

## Source of Truth

Before making changes, consult documents in this order:

1. `AGENTS.md`
2. `docs/adr/`
3. `docs/architecture.md`
4. `docs/threat-model.md`
5. `docs/PROJECT_CONTEXT.md`
6. module-local README files and existing tests

Precedence rules:
- If implementation differs from documentation, do not assume the code is correct. Investigate.
- If multiple documents conflict, follow the highest-precedence source above.
- If you introduce a significant architectural change, update or create an ADR.

---

## Non-Negotiable Rules

### Security-first
- Always prefer the more secure design when alternatives are otherwise comparable.
- Assume all external input is hostile.
- Prefer explicit controls over implicit assumptions.
- Treat missing validation as a defect.

### No secrets in code
- Never hardcode API keys, passwords, tokens, certificates, or private keys.
- Never commit real credentials, even in sample files.
- Use placeholders such as `YOUR_SECRET_HERE`.
- Do not bypass the project’s secret-management abstractions.

### Least privilege everywhere
- No wildcard permissions unless strictly unavoidable.
- Scope IAM, RBAC, and network rules to the minimum needed.
- If an exception is unavoidable, document the security rationale inline.

### Defense in depth
- Do not rely on a single control.
- A failure in one layer should not fully compromise the system.

### Security controls must be testable
- Any meaningful security control must have a corresponding test.
- Do not add auth, rate limiting, filtering, validation, or hardening logic without verifying expected behavior.

### Security rationale must be documented
- Every non-obvious security decision should explain:
  - what threat it mitigates
  - why this approach was chosen
  - what trade-off it introduces

---

## Execution Rules

When working on a task:

1. Identify the relevant module and current project phase.
2. Read applicable ADRs and local patterns before editing.
3. Prefer the smallest correct change that fits the existing architecture.
4. Preserve the security model unless the task explicitly changes it.
5. Add or update tests.
6. Update documentation if architecture, controls, or usage changed.

Before finalizing a change, ask:
- What threat does this mitigate?
- Is there a simpler implementation with the same security guarantees?
- What happens if this control fails?
- Is blast radius constrained?
- Is this consistent with roadmap and ADRs?

---

## Coding Standards

### Python
- Use Python 3.11+ conventions.
- Type hints are mandatory on all function signatures.
- Use Pydantic models for external inputs.
- Do not pass raw, unvalidated user input through the system.
- Security-relevant functions and modules must include docstrings.

Use this module header pattern for security-relevant modules:

```python
"""
Module: prompt_injection.py
Purpose: Detect prompt injection attempts in LLM inputs before forwarding to the model.
Threat mitigated: An attacker embedding instructions in user input that override
system-level instructions or attempt data exfiltration.
Reference: OWASP LLM Top 10 — LLM01: Prompt Injection
"""
```

Additional requirements:
- No SQL built by string concatenation.
- No shell command construction from user input.
- Prefer explicit validation and narrow failure modes.
- `bandit` and `semgrep` should pass before merge.

### FastAPI
- Validate all request inputs with Pydantic v2 models.
- Keep routes thin.
- Put reusable security logic in services or middleware.
- Do not leak internal implementation details in error messages.

### Terraform
- No hardcoded AMI IDs.
- Use encrypted remote state with locking for real environments.
- Tag resources consistently:
  - `Environment`
  - `Project = "latticeharden"`
  - `ManagedBy = "terraform"`
- Comment security-relevant resources with the threat they mitigate.

### Kubernetes
Required defaults unless explicitly justified:
- `runAsNonRoot: true`
- `readOnlyRootFilesystem: true`
- `allowPrivilegeEscalation: false`
- define `resources.requests`
- define `resources.limits`

Also:
- Prefer deny-by-default network policy posture.
- Keep RBAC minimal.
- Document any privileged exception inline.

### Docker
- Do not use `latest` tags.
- Pin versions explicitly.
- Prefer multi-stage builds.
- Minimize runtime attack surface.
- Prefer hardened or distroless images where appropriate.

### Git commits
Use Conventional Commits, such as:
- `feat(ai-security): add prompt injection classifier using regex and semantic checks`
- `fix(api): enforce rate limiting on login endpoints`
- `security(k8s): restrict egress from proxy namespace`
- `docs(adr): record Vault decision for runtime secrets`

---

## CI/CD Expectations

Security checks are part of the product.

Expected controls include:
- Semgrep
- Trivy
- TruffleHog
- container scanning
- manifest validation before deploy
- DAST when phase-appropriate

Do not bypass validation steps for convenience.

Do not use `kubectl apply -f` in CI/CD without prior manifest validation such as `kubeconform` or equivalent.

---

## ADR Policy

Create or update an ADR for:
- major architectural choices
- auth strategy changes
- secrets management changes
- infrastructure trust boundary changes
- meaningful AI security design decisions
- PQC integration decisions with security or complexity trade-offs

Use this template:

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

## Explicit Anti-Patterns

Do not do the following:
- Do not use n8n, Zapier, or other low-code automation tools in this repository.
- Do not use `latest` image tags.
- Do not commit credentials, including in example files.
- Do not implement cryptographic primitives from scratch.
- Do not add security controls without tests.
- Do not skip validation in deployment workflows.
- Do not broaden permissions just to make something work.
- Do not introduce architectural drift without documenting it.

---

## Preferred Behavior for Code Changes

When modifying or generating code for this repository:
- be precise
- be explicit
- explain security rationale for non-obvious choices
- avoid unnecessary abstraction
- prefer secure defaults
- keep implementations aligned with the documented structure
- do not invent new architectural layers without justification

When uncertain, prefer the option that is:
1. more secure
2. easier to audit
3. easier to test
4. more consistent with existing decisions

---

## Maintainer Intent

This repository exists to demonstrate serious security engineering capability in a single coherent platform.

Complexity is acceptable when it is deliberate, documented, testable, and security-motivated.

When in doubt, optimize for:
- demonstrable security depth
- architectural clarity
- technical credibility
- consistency with the long-term platform vision
