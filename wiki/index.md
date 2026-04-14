# Knowledge Base Index
Last updated: 2026-04-14
Total articles: 55

## Categories

### LLM Fundamentals
- [KV Cache Quantization](arxiv-2504-19874/kv-cache-quantization.md) - Compressing key-value caches in LLM inference for long-context models
- [TurboQuant](arxiv-2504-19874/turboquant.md) - Online vector quantization algorithm with near-optimal MSE and inner product distortion

### Vector Quantization and Compression
- [Vector Quantization Theory](arxiv-2504-19874/vector-quantization-theory.md) - Shannon's source coding, distortion-rate functions, and information-theoretic lower bounds
- [Random Rotation Quantization](arxiv-2504-19874/random-rotation-quantization.md) - Rotating vectors to enable independent per-coordinate scalar quantization
- [Quantized Johnson-Lindenstrauss Transform](arxiv-2504-19874/quantized-johnson-lindenstrauss-transform.md) - 1-bit sketching for unbiased inner product estimation
- [Product Quantization for Nearest Neighbor Search](arxiv-2504-19874/product-quantization-for-nearest-neighbor-search.md) - Codebook-based vector compression for vector databases and RAG

### Prompt Engineering
<!-- Techniques, frameworks, and best practices for prompting -->

### Retrieval-Augmented Generation (RAG)
<!-- RAG architectures, chunking, embedding, vector stores -->

### AI Agents
- [Agent Name Service (ANS)](ietf-draft-narajala-ans/agent-name-service.md) - IETF draft for a DNS-like universal directory for secure AI agent discovery
- [Agent Communication Protocols](ietf-draft-narajala-ans/agent-communication-protocols.md) - A2A (Google), MCP (Anthropic), ACP (IBM) protocol comparison
- [Agent Discovery](ietf-draft-narajala-ans/agent-discovery.md) - The problem of how agents find, verify, and communicate with each other
- [Agent Identity and Trust](ietf-draft-narajala-ans/agent-identity-and-trust.md) - PKI, certificates, ZKPs, and trust mechanisms for agents
- [MAESTRO Threat Framework](ietf-draft-narajala-ans/maestro-threat-framework.md) - OWASP seven-layer threat modeling framework for multi-agent systems
- [Agent Scaffolds](arxiv-2510-11977/agent-scaffolds.md) - Task-specific vs. generalist scaffolds and their cost-accuracy tradeoffs
- [Agent Shortcuts and Gaming](arxiv-2510-11977/agent-shortcuts-and-gaming.md) - Benchmark exploitation behaviors uncovered through log analysis
- [Agent Evaluation Infrastructure](arxiv-2510-11977/agent-evaluation-infrastructure.md) - Engineering challenges of standardized agent evaluation at scale

### Agent-First Data Systems
- [Agentic Speculation](agent-first-data-systems/agentic-speculation.md) - High-throughput exploratory querying by LLM agents to compensate for lack of data grounding
- [Agent-First Data Systems Architecture](agent-first-data-systems/agent-first-data-systems-architecture.md) - Proposed database redesign with probes, probe optimizer, and agentic memory
- [Probes and Briefs](agent-first-data-systems/probes-and-briefs.md) - Beyond-SQL query interface with natural language intent and phase-aware approximation
- [Probe Optimization](agent-first-data-systems/probe-optimization.md) - Satisficing, multi-query optimization, and cross-turn strategies for agent workloads
- [Agentic Memory Store](agent-first-data-systems/agentic-memory-store.md) - Persistent semantic cache for agent grounding and metadata
- [Branched Updates](agent-first-data-systems/branched-updates.md) - Multi-world transactions with copy-on-write for speculative agent writes
- [Sleeper Agents (Proactive Data Systems)](agent-first-data-systems/sleeper-agents.md) - In-database agents providing grounding feedback and cost steering

### Fine-Tuning and Training
<!-- LoRA, RLHF, GRPO, dataset preparation -->

### Guardrails and Responsible AI
<!-- Safety, content filtering, bias mitigation -->

### Benchmarking and Evaluation
- [Holistic Agent Leaderboard (HAL)](arxiv-2510-11977/holistic-agent-leaderboard.md) - Unified evaluation framework for reproducible, cost-controlled agent benchmarking
- [Agent Evaluation Benchmarks](arxiv-2510-11977/agent-evaluation-benchmarks.md) - 9 benchmarks across 4 domains: coding, web, science, customer service
- [Pareto Frontier in Agent Evaluation](arxiv-2510-11977/pareto-frontier-in-agent-evaluation.md) - Cost-accuracy tradeoff analysis showing steep, sparse frontiers
- [Reasoning Effort Tradeoffs](arxiv-2510-11977/reasoning-effort-tradeoffs.md) - Why more reasoning doesn't always improve agent accuracy
- [Automated Agent Log Analysis](arxiv-2510-11977/automated-agent-log-analysis.md) - Docent-based systematic behavioral analysis of agent execution traces

### LLM-Based Code Evolution
- [SATLUTION Framework](arxiv-2509-07367/satlution-framework.md) - First repository-scale self-evolving coding framework for SAT solving
- [LLM Code Evolution](arxiv-2509-07367/llm-code-evolution.md) - Paradigm of using LLMs in iterative loops to autonomously refine code
- [Repository-Scale Code Evolution](arxiv-2509-07367/repository-scale-code-evolution.md) - Extending code evolution from single files to full repositories
- [Evolutionary Coding Agents](arxiv-2509-07367/evolutionary-coding-agents.md) - Planning + Coding dual-agent architecture for iterative code improvement
- [Self-Evolving Rule Systems](arxiv-2509-07367/self-evolving-rule-systems.md) - Static + dynamic rule architectures that co-evolve with code
- [Verification Pipelines for Code Evolution](arxiv-2509-07367/verification-pipelines-for-code-evolution.md) - Two-stage correctness checking with formal proof validation

### Combinatorial Optimization
- [Boolean Satisfiability (SAT)](arxiv-2509-07367/boolean-satisfiability.md) - The canonical NP-complete problem, CDCL solvers, and SAT Competition
- [Multi-Armed Bandit Heuristic Tuning](arxiv-2509-07367/multi-armed-bandit-heuristic-tuning.md) - Bandit-based dynamic selection of solver heuristics at runtime

### Economics of Organization
- [Transaction Costs](coase-nature-of-the-firm/transaction-costs.md) - Costs of using the price mechanism that explain why firms exist
- [Theory of the Firm](coase-nature-of-the-firm/theory-of-the-firm.md) - Coase's 1937 definition of the firm as the supersession of the price mechanism
- [Price Mechanism vs. Entrepreneurial Coordination](coase-nature-of-the-firm/price-mechanism-vs-entrepreneurial-coordination.md) - Two alternative methods of organizing production
- [Firm Size Determinants](coase-nature-of-the-firm/firm-size-determinants.md) - Forces limiting firm growth and creating equilibrium boundaries
- [Vertical Integration and Combination](coase-nature-of-the-firm/vertical-integration-and-combination.md) - How firms expand by internalizing market transactions
- [Knight's Uncertainty Theory of the Firm](coase-nature-of-the-firm/knights-uncertainty-theory.md) - Frank Knight's competing theory and Coase's critique

### GenAI Applications
- [Claude Code Skills and Plugins](frontend-slides/claude-code-skills-and-plugins.md) - Modular, installable extensions that add specialized capabilities to Claude Code CLI
- [Zero-Dependency Web Presentations](frontend-slides/zero-dependency-web-presentations.md) - Self-contained HTML files with inline CSS/JS, no frameworks needed
- [Anti-AI-Slop Design](frontend-slides/anti-ai-slop-design.md) - Curated design presets that avoid generic AI-generated aesthetics

### AI Tool Design
- [Progressive Disclosure in AI Tools](frontend-slides/progressive-disclosure-in-ai-tools.md) - Loading AI tool instructions on-demand to conserve context window
- [Vibe Coding](frontend-slides/vibe-coding.md) - Philosophy of building software by describing intent, not writing code
- [Claude Code Memory System](claude-code-memory-management/claude-code-memory-system.md) - Auto memory feature with global and project scopes, 200-line MEMORY.md constraint
- [Structured Memory Architecture](claude-code-memory-management/structured-memory-architecture.md) - Directory-based memory organization with tools/, domain/, and general.md tiers
- [Claude Code Hooks](claude-code-memory-management/claude-code-hooks.md) - PreToolUse hooks for automatic memory injection with PPID-based session tracking
- [Domain Knowledge Lifecycle](claude-code-memory-management/domain-knowledge-lifecycle.md) - Three-stage progression from staging to skill promotion to pointer
- [Context Window Budget Management](claude-code-memory-management/context-window-budget-management.md) - Strategic allocation of the 200-line MEMORY.md budget

### Cloud AI Services
<!-- Amazon Bedrock, model hosting, inference APIs -->

### LLM Knowledge Bases
<!-- Meta-topic: using LLMs to build and maintain knowledge -->

### Software Engineering Philosophy
- [Programming as Theory Building](naur-programming-as-theory-building/programming-as-theory-building.md) - Naur's 1985 thesis that programming is building a mental theory, not producing code
- [Tacit Knowledge in Software](naur-programming-as-theory-building/tacit-knowledge-in-software.md) - Ryle's notion of theory applied to programmer knowledge that transcends documentation
- [Program Lifecycle](naur-programming-as-theory-building/program-lifecycle.md) - Life, death, and revival of programs based on whether theory-holders remain
- [Software Modification Challenges](naur-programming-as-theory-building/software-modification-challenges.md) - Why modifying programs without the underlying theory leads to structural decay
- [Metaphor-Driven Design](naur-programming-as-theory-building/metaphor-driven-design.md) - Using shared metaphors to communicate and align design theories across teams

## Source Summaries
- [Naur: Programming as Theory Building](naur-programming-as-theory-building/summary-naur-programming-as-theory-building.md)
- [IETF: Agent Name Service (ANS) Draft](ietf-draft-narajala-ans/summary-ietf-draft-narajala-ans.md)
- [Agent-First Data Systems (UC Berkeley)](agent-first-data-systems/summary-agent-first-data-systems.md)
- [HAL: Holistic Agent Leaderboard](arxiv-2510-11977/summary-arxiv-2510-11977.md)
- [SATLUTION: Autonomous Code Evolution Meets NP-Completeness](arxiv-2509-07367/summary-arxiv-2509-07367.md)
- [Coase: The Nature of the Firm (1937)](coase-nature-of-the-firm/summary-coase-nature-of-the-firm.md)
- [Frontend Slides: Claude Code Skill for Web Presentations](frontend-slides/summary-frontend-slides.md)
- [Claude Code Memory Management](claude-code-memory-management/summary-claude-code-memory-management.md)
- [TurboQuant: Online Vector Quantization](arxiv-2504-19874/summary-arxiv-2504-19874.md)
