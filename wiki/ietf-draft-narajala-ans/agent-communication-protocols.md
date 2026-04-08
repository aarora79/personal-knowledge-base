---
title: Agent Communication Protocols
created: 2026-04-07
updated: 2026-04-07
sources: [raw/20260407-ietf-draft-narajala-ans.md]
related: [agent-name-service](agent-name-service.md), [agent-discovery](agent-discovery.md), [agent-identity-and-trust](agent-identity-and-trust.md), [Agent Scaffolds](../arxiv-2510-11977/agent-scaffolds.md)
tags: [a2a, mcp, acp, agent-protocols, interoperability, ai-agents, multi-agent-systems]
---

# Agent Communication Protocols

As AI agents become more prevalent, several protocols have emerged to standardize how they communicate and interact with each other and with external tools. The three most prominent protocols as of 2025 are A2A, MCP, and ACP, each addressing different aspects of the agent communication problem.

**Agent2Agent Protocol (A2A)** was developed by Google to provide a standardized protocol for inter-agent communication. A2A focuses on bridging different agent frameworks, enabling agents built on different platforms to discover and interact with each other. It uses the concept of an "Agent Card" as a metadata document describing an agent's capabilities, endpoints, and identity.

**Model Context Protocol (MCP)** was developed by Anthropic to simplify the integration of AI models with external tools and data sources. MCP focuses on dynamic discovery and integration, providing a standard way for agents to discover available tools, understand their input/output schemas, and invoke them. It emphasizes the tool-use pattern where an LLM can call external functions through a standardized interface.

**Agent Communication Protocol (ACP)** was designed by IBM Research to standardize broader agent-to-agent communication needs. ACP targets automation, collaboration, UI integration, and developer tooling, evolving from initial MCP concepts into a more comprehensive protocol for agent orchestration and delegation.

These protocols are complementary rather than competing. A2A handles agent-to-agent discovery and communication, MCP handles agent-to-tool integration, and ACP addresses orchestration and delegation patterns. The Agent Name Service (ANS) IETF draft proposes a protocol-agnostic registry layer that sits above all three, providing unified discovery regardless of which protocol an agent uses. ANS achieves this through a Protocol Adapter Layer that translates between its internal representation and protocol-specific formats, and through structured ANSNames that encode the protocol type as part of the agent identifier.

Earlier work in multi-agent systems, such as the Foundation for Intelligent Physical Agents (FIPA) Agent Communication Language specifications from 2002, explored similar territory but lacked standardized security mechanisms and universally adopted transport protocols suitable for the modern internet.

## Key Points
- A2A (Google): inter-agent communication, bridging different agent frameworks
- MCP (Anthropic): agent-to-tool integration, dynamic tool discovery
- ACP (IBM): agent orchestration, delegation, automation
- Protocols are complementary, not competing
- ANS provides a protocol-agnostic discovery layer above all three
- FIPA ACL was a precursor but lacked security and modern transport
- Protocol Adapter Layer in ANS translates between protocol-specific formats

## Related Concepts
- [Agent Name Service](agent-name-service.md) - protocol-agnostic registry that unifies discovery across A2A, MCP, ACP
- [Agent Discovery](agent-discovery.md) - the problem these protocols help solve
- [Agent Identity and Trust](agent-identity-and-trust.md) - security mechanisms integrated with these protocols

## Sources
- raw/20260407-ietf-draft-narajala-ans.md - IETF draft describing how ANS complements A2A, MCP, and ACP
