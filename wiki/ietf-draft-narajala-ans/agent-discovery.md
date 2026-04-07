---
title: Agent Discovery
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-ietf-draft-narajala-ans.md]
related: [agent-name-service](agent-name-service.md), [agent-communication-protocols](agent-communication-protocols.md), [agent-identity-and-trust](agent-identity-and-trust.md)
tags: [agent-discovery, service-discovery, dns, capability-matching, ai-agents, multi-agent-systems]
---

# Agent Discovery

Agent discovery is the problem of how AI agents find, verify, and establish communication with other agents in a multi-agent ecosystem. As agent-to-agent communication is expected to become a significant component of internet traffic, robust discovery mechanisms become essential infrastructure.

Traditional service discovery mechanisms are insufficient for agentic AI. The Domain Name System (DNS) maps human-readable names to network addresses but has no concept of agent capabilities, identity verification, or lifecycle management. DNS-Based Service Discovery (DNS-SD) adds local service discovery but does not address verifiable identity or complex capability matching on a global scale.

Agent discovery in the agentic AI era requires several capabilities that go beyond traditional service discovery. First, it needs capability-aware resolution: agents must find other agents based on what they can do, not just their name or address. An agent looking for sentiment analysis should be able to query a registry for agents with that specific capability. Second, it requires identity verification: before interacting with a discovered agent, the requesting agent needs cryptographic assurance of the other agent's identity. Third, it needs lifecycle management: agents are registered, renewed, and eventually decommissioned, and the discovery system must track this lifecycle. Fourth, it must be protocol-agnostic: agents using different communication protocols (A2A, MCP, ACP) must be discoverable through a common mechanism.

The Agent Name Service (ANS) IETF draft proposes a comprehensive solution using structured naming (ANSName format), PKI-based identity, a Protocol Adapter Layer for cross-protocol discovery, and formal resolution algorithms. The resolution process involves querying the ANS service, looking up agent records in the registry, verifying cryptographic signatures and certificate chains, and returning verified endpoint information to the requesting agent. ANS also supports version negotiation, allowing agents to discover compatible versions of a service.

## Key Points
- DNS and DNS-SD are insufficient for agent-to-agent discovery
- Agent discovery requires capability matching, not just name resolution
- Identity verification must be cryptographic and PKI-based
- Agents have lifecycles (registration, renewal, revocation) that discovery must track
- Discovery must work across multiple communication protocols
- ANS proposes capability-aware resolution with formal algorithms
- Version negotiation allows discovery of compatible agent versions

## Related Concepts
- [Agent Name Service](agent-name-service.md) - the proposed protocol for solving agent discovery
- [Agent Communication Protocols](agent-communication-protocols.md) - the protocols that agents use after discovery
- [Agent Identity and Trust](agent-identity-and-trust.md) - the trust layer that makes discovery secure

## Sources
- raw/20260407-ietf-draft-narajala-ans.md - IETF draft analyzing discovery gaps and proposing ANS
