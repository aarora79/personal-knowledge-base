---
title: "Source Summary: Agent Name Service (ANS) IETF Draft"
created: 2026-04-07
source: raw/20260407-ietf-draft-narajala-ans.md
depth: 500
articles_created: [agent-name-service.md, agent-communication-protocols.md, agent-discovery.md, agent-identity-and-trust.md, maestro-threat-framework.md]
---

# Agent Name Service (ANS) IETF Draft - Expert Summary

This IETF Internet-Draft (draft-narajala-ans-00, May 2025) by Huang, Narajala, Habler, and Sheriff proposes the Agent Name Service (ANS), a protocol-agnostic directory service architecture for secure AI agent discovery and interoperability. The draft positions ANS as a foundational infrastructure layer analogous to DNS but designed for the semantic richness, identity verification, capability matching, and lifecycle management requirements of autonomous AI agents. It is submitted as an Independent Submission with Experimental intended status.

## Architectural Components

The ANS architecture comprises six principal components. The **Agent Registry** is a potentially distributed database storing Agent Credential and Entitlement Management (ACEM) records, Decentralized Identifiers (DIDs), capabilities, PKI certificates, protocol-specific metadata via `protocolExtensions`, and registration/renewal timestamps. The **Registration Authority (RA)** validates registration and renewal requests against registry policies, performs identity verification (domain validation, organizational checks), and coordinates certificate issuance. The **Certificate Authority (CA)** issues and manages X.509 digital certificates (per RFC 5280) that form the root of trust. The **Protocol Adapter Layer** translates between the registry's internal normalized representation and protocol-specific formats (A2A Agent Cards, MCP tool descriptions, ACP agent profiles). The **Request/Response Schema** is a protocol-agnostic JSON-based schema (RFC 8259) with `protocolExtensions` for protocol-specific data. The **ANS Service** itself provides the resolution interface.

## Naming and Resolution

ANS defines a structured naming convention, the ANSName, with the format:

```
Protocol://AgentID.Capability.Provider.Version[.Extension]
```

Where Protocol is drawn from {a2a, mcp, acp, ...}, Version must adhere to Semantic Versioning, and Extension is an optional deployment-specific metadata field (e.g., "hipaa", "testenv"). AgentID, Capability, and Provider should be registered with a governance authority analogous to ICANN to prevent collisions.

The formal resolution algorithm `Resolve(ANSName, RequestedVersionRange)` proceeds through: (1) parsing the ANSName into components, (2) querying the registry for matching records, (3) version negotiation across multiple matches using semantic versioning ranges, (4) retrieving the EndpointRecord (containing data, signature, and certificate), (5) verifying the registry's signature on the response using the registry's trusted CA, and (6) verifying the target agent's certificate chain against a separate trusted CA for agent certificates. The two-phase verification distinguishes between trust in the registry's response integrity and trust in the agent's identity -- a critical design decision that prevents a compromised registry from undetectably substituting agent endpoints.

## Protocol Landscape

The draft explicitly positions ANS as complementary to three emerging agent communication protocols:

- **A2A (Agent2Agent Protocol)** by Google: focuses on inter-agent communication, bridging heterogeneous agent frameworks. Uses Agent Cards as capability descriptors.
- **MCP (Model Context Protocol)** by Anthropic: focuses on AI model integration with external tools and data sources. Defines tool descriptions with input/output schemas and endpoints.
- **ACP (Agent Communication Protocol)** by IBM Research: targets broader agent-to-agent communication including delegation, orchestration, UI integration, and developer tooling.

The Protocol Adapter Layer normalizes these protocol-specific representations into the registry's internal schema while preserving protocol-specific data in `protocolExtensions`. For example, an MCP tool registered under ANSName `mcp://sentimentAnalyzer.textAnalysis.ExampleCorp.v1.0` stores its `input_schema`, `output_schema`, and `mcpEndpoint` in the MCP-specific extension fields, while the core identity, capability, and provider are normalized into ANS-standard columns.

## Identity and Trust Model

The Agent Identity module implements a multi-layered identity model: cryptographic identity (X.509 certificate), logical identity (ANSName), and protocol-specific identity (A2A Agent Card, MCP tool description, etc.). The draft specifies a dual-responsibility validation model where the RA performs foundational validation at registration/renewal time (signature verification, policy adherence, legitimacy checks), while each Requesting Agent performs continuous context-specific validation before every interaction (cryptographic verification, capability alignment).

Two advanced mechanisms address capability attestation. **Zero-knowledge proofs (ZKPs)**, specifically using the Groth16 proof system, allow agents to prove possession of capabilities without revealing internal state or data. The verification circuit encodes constraints like `agent.hasCapability(c) AND agent.isAuthorized(c)` alongside certificate validity checks. **Challenge-response mechanisms** provide ongoing runtime validation: the registry sends a known-answer test to an agent claiming a specific capability (e.g., sentiment analysis with claimed accuracy), compares the result, and may trigger revocation if performance degrades.

Authentication enforcement combines OAuth 2.0 for authorization tokens, mutual TLS (mTLS) for transport-level identity verification, and JWT validation. Resource access control uses RBAC+ABAC with an OPA (Open Policy Agent) policy decision point operating in distributed evaluation mode, with context attributes spanning agent role, resource classification, time window, and operation sensitivity.

## Security Analysis (MAESTRO Framework)

The draft performs a systematic threat analysis mapped to the MAESTRO (Multi-Agent Environment, Security, Threat, Risk, and Outcome) seven-layer framework from the OWASP GenAI Security Project. Four primary threats are analyzed:

1. **Agent Impersonation** (Layer 7 - Agent Ecosystem): Mitigated by mandatory PKI with certificate validation and private key proof of possession. All communications must be digitally signed with recipient-side verification.

2. **Registry Poisoning** (Layers 2/4/6/7): Mitigated by strict RA validation during registration/renewal, cryptographic signing of all registry responses (secure resolution), and database access controls at the infrastructure layer.

3. **Man-in-the-Middle** (Layers 4/6): Mitigated by digital signatures using agent PKI keys as the core mechanism, supplemented by secure transport (mTLS). The formal resolution algorithm enforces response integrity verification at the protocol level.

4. **Denial of Service** (Layers 4/7): Mitigated by distributed architecture design, standard operational defenses (rate limiting with TokenBucket algorithm at 100/s refill rate and 500 burst capacity, per-capability), and anycast routing. Resolution algorithms may include DoS limits.

Additional security controls include certificate revocation via CRL (RFC 5280) and OCSP (RFC 6960), mandatory secure key storage (HSMs, secure enclaves), DNSSEC-like signed resolution responses, Sybil attack resistance through costly registration processes, and protocol-specific security leverage (OAuth capability tokens, A2A/MCP/ACP built-in security features).

## ANS Architecture Diagram

```
  +---------------------------------------------------+
  |                   ANS Service                      |
  |  (Resolution interface for agent queries)          |
  +---------------------------------------------------+
         |                |                |
         v                v                v
  +-----------+   +--------------+   +----------+
  | Agent     |   | Registration |   | Cert     |
  | Registry  |   | Authority    |   | Authority|
  | (ACEM,    |   | (RA)         |   | (CA)     |
  | DIDs,     |   | - Validates  |   | - Issues |
  | certs,    |   |   identity   |   |   X.509  |
  | caps)     |   | - Enforces   |   |   certs  |
  +-----------+   |   policy     |   +----------+
                  +--------------+
         |                |                |
         v                v                v
  +---------------------------------------------------+
  |            Protocol Adapter Layer                  |
  |  Translates between internal schema and:           |
  |  +-------+  +---------+  +-------+  +--------+   |
  |  |  A2A  |  |   MCP   |  |  ACP  |  | Future |   |
  |  | Cards |  |  Tools  |  | Profs |  |  ...   |   |
  |  +-------+  +---------+  +-------+  +--------+   |
  +---------------------------------------------------+
```

## Agent Resolution Sequence

```
  Requesting          ANS            Agent
    Agent            Service         Registry    CA
      |                |                |         |
      | 1. Resolve     |                |         |
      |   ANSName      |                |         |
      |--------------->|                |         |
      |                | 2. Query       |         |
      |                |   registry     |         |
      |                |--------------->|         |
      |                |                |         |
      |                | 3. Return      |         |
      |                |   EndpointRec  |         |
      |                |<---------------|         |
      |                |                          |
      |                | 4. Verify registry       |
      |                |    signature via CA      |
      |                |------------------------->|
      |                |                          |
      |                | 5. Verify agent          |
      |                |    cert chain via CA     |
      |                |------------------------->|
      |                |                          |
      | 6. Return verified                        |
      |   endpoint info|                          |
      |<---------------|                          |
      |                                           |
```

## Implementation Considerations and Limitations

The draft acknowledges several open challenges: governance structure for name registration (analogous to ICANN), scalability of the resolution infrastructure, cross-protocol interoperability limits where protocol-specific semantics may not translate cleanly, the computational cost of ZKP generation and verification, and the bootstrapping problem of establishing initial trust in the CA infrastructure. The reference implementation pointers include JSON Schema repositories on GitHub for registration, renewal, and capability request/response schemas.

## What This Source Covers
- ANS architecture: registry, RA, CA, Protocol Adapter Layer, ANS Service
- ANSName formal naming structure with semantic versioning
- Formal resolution algorithm with two-phase cryptographic verification
- A2A, MCP, ACP protocol comparison and Protocol Adapter Layer normalization
- Multi-layered agent identity: cryptographic, logical, protocol-specific
- Dual-responsibility validation: RA baseline + continuous Requesting Agent validation
- Zero-knowledge proofs (Groth16) for capability attestation
- Challenge-response mechanisms for runtime capability validation
- OAuth 2.0 + mTLS + JWT authentication stack
- RBAC+ABAC resource access control with OPA policy engine
- MAESTRO seven-layer threat analysis: impersonation, poisoning, MitM, DoS
- PKI security controls: revocation, HSMs, RA validation rigor
- Governance, scalability, and cross-protocol interoperability challenges

## Wiki Articles From This Source
- [Agent Name Service](agent-name-service.md) - The core ANS protocol, a DNS-like directory for AI agents
- [Agent Communication Protocols](agent-communication-protocols.md) - A2A, MCP, and ACP protocol comparison
- [Agent Discovery](agent-discovery.md) - The problem of how agents find and verify each other
- [Agent Identity and Trust](agent-identity-and-trust.md) - PKI certificates, ZKPs, and trust mechanisms
- [MAESTRO Threat Framework](maestro-threat-framework.md) - OWASP seven-layer threat model for multi-agent systems
