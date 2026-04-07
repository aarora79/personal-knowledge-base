---
title: Agent Name Service (ANS)
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-ietf-draft-narajala-ans.md]
related: [agent-communication-protocols](agent-communication-protocols.md), [agent-discovery](agent-discovery.md), [agent-identity-and-trust](agent-identity-and-trust.md)
tags: [agent-name-service, dns, pki, capability-discovery, ietf, ai-agents, multi-agent-systems]
---

# Agent Name Service (ANS)

The Agent Name Service (ANS) is a proposed IETF protocol (draft-narajala-ans-00, May 2025) that defines a universal directory service for secure AI agent discovery and interoperability. ANS is designed as a DNS-like system for the agentic AI era, addressing the fact that traditional DNS maps human-readable names to network addresses but lacks the semantic richness, identity verification, and capability matching that autonomous AI agents require.

ANS is protocol-agnostic. Rather than replacing emerging agent communication protocols like A2A, MCP, or ACP, it provides a complementary infrastructure layer that sits above them. Agents register with ANS regardless of which protocol they use, and other agents discover them through ANS resolution. The system integrates Public Key Infrastructure (PKI) certificates for verifiable agent identity and trust, ensuring that agents can be authenticated before interaction.

The architecture consists of several core components: the Agent Registry (a distributed database storing agent metadata, capabilities, certificates, and protocol-specific extensions), a Registration Authority (RA) that validates agent registrations and enforces policies, a Certificate Authority (CA) that issues X.509 certificates, and a Protocol Adapter Layer that translates between the registry's internal representation and protocol-specific formats.

ANS introduces a structured naming convention called ANSName with the format: `Protocol://AgentID.Capability.Provider.Version[.Extension]`. For example, `a2a://textProcessor.DocumentTranslation.AcmeCorp.v2.1.hipaa`. This naming structure encodes identity, capability, and contextual metadata in a format that is both human-readable and machine-resolvable. Resolution goes beyond simple name lookup to enable capability-aware discovery, where agents can find other agents based on what they can do, not just who they are.

The specification includes a formal resolution algorithm, secure resolution with cryptographic verification of responses, agent lifecycle management (registration, renewal, revocation), and a comprehensive threat analysis using the MAESTRO framework covering impersonation, registry poisoning, man-in-the-middle attacks, and denial of service.

## Key Points
- DNS-like directory service designed specifically for AI agents
- Protocol-agnostic: works across A2A, MCP, ACP, and future protocols
- PKI-based identity verification using X.509 certificates
- Structured naming: `Protocol://AgentID.Capability.Provider.Version`
- Capability-aware resolution beyond simple name-to-address mapping
- Agent lifecycle management: registration, renewal, revocation
- Zero-knowledge proofs for capability attestation without revealing internals
- Challenge-response mechanisms for ongoing capability validation
- MAESTRO-based threat analysis covering impersonation, poisoning, MitM, DoS

## Related Concepts
- [Agent Communication Protocols](agent-communication-protocols.md) - the protocols (A2A, MCP, ACP) that ANS complements
- [Agent Discovery](agent-discovery.md) - the broader problem that ANS addresses
- [Agent Identity and Trust](agent-identity-and-trust.md) - PKI, certificates, and trust mechanisms in ANS

## Sources
- raw/20260407-ietf-draft-narajala-ans.md - Full IETF Internet-Draft (draft-narajala-ans-00) by Huang, Narajala, Habler, and Sheriff
