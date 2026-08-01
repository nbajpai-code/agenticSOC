# State of AI Agent Security (2025-2026)

## Executive Summary
The rapid proliferation of **Autonomous AI Agents** has introduced a critical new attack surface for enterprises. No longer just "chatbots," these agents possess the agency to plan, execute, and modify systems without human intervention. The industry consensus for 2025-2026 is clear: while adoption is skyrocketing, security controls are lagging dangerously behind, creating a "Shadow AI" ecosystem where agents operate with excessive permissions and zero visibility.

This document analyzes key industry reports, with a special focus on **Gravitee.io**, **Wiz**, and **Palo Alto Networks**, to provide a comprehensive view of the current threat landscape.

---

## Gravitee.io: The State of AI Agent Security 2026
*Source: [Gravitee.io State of AI Agent Security Report](https://www.gravitee.io/state-of-ai-agent-security)*

Gravitee.io's landmark report, based on a survey of 750 global IT leaders, exposes a "confidence paradox" where executive optimism masks severe security gaps.

### Key Findings
1.  **The "Ungoverned" Crisis**:
    - **88%** of organizations reported a confirmed or suspected security incident involving AI agents in the last 12 months.
    - **53%** of AI agents are "unmonitored" and "unsecured," effectively operating as "Ghost Agents" within corporate networks.
    - Only **22%** of organizations currently treat AI Agents as distinct "Identities" (Machine Identity) requiring their own IAM policies.

2.  **The Rise of "Agent Sprawl"**:
    - Enterprises are deploying agents faster than they can secure them. A typical enterprise now manages hundreds of distinct agents across different platforms (Microsoft Copilot, custom internal agents, third-party SaaS agents).
    - **Lack of Visibility**: Most organizations cannot produce a comprehensive inventory of all active AI agents in their environment.

3.  **Strategic Recommendations**:
    - **AI Gateway as the New Firewall**: Implement a centralized AI Gateway to govern all agent traffic, enforcing policies on prompts, models, and data access.
    - **Identity-First Security**: Treat every agent as a privileged user. Move from API keys to dynamic, short-lived tokens and strictly enforce Least Privilege.

---

## Wiz: State of AI in the Cloud 2025
*Source: [Wiz State of AI in the Cloud](https://www.wiz.io/blog/state-of-ai-in-the-cloud-2025)*

Wiz focuses on the infrastructure and cloud layer, highlighting how AI adoption is outpacing cloud security hygiene.

### Key Findings
- **Shadow AI is the New Shadow IT**: **62%** of cloud environments have "Shadow AI" instances—unapproved AI models or databases (like vector DBs) spun up by developers without security review.
- **Vulnerable Supply Chain**: Over **40%** of managed AI services (e.g., OpenAI on Azure, Bedrock on AWS) are configured with overly permissive access to S3 buckets or other storage services, enabling potential data exfiltration.
- **Hardcoded Secrets**: A surge in AI-related repositories containing hardcoded API keys (OpenAI, Hugging Face tokens), making "Credential Theft" the #1 attack vector for AI systems.

---

## Palo Alto Networks: Unit 42 AI Threat Report
*Source: [Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/)*

Palo Alto Networks provides a tactical view of how attackers are actually exploiting these systems in the wild.

### Top Threat Vectors (2025)
1.  **Prompt Injection & Jailbreaking**: Attackers are industrializing "jailbreak-as-a-service" to bypass safety guardrails of enterprise agents.
2.  **Model Poisoning**: Subtle manipulation of training data (Data Poisoning) or RAG knowledge bases to permanently alter agent behavior.
3.  **Resource Hijacking**: "Model Denial of Service" attacks where malicious agents spawn infinite loops or expensive queries to exhaust API quotas and drive up cloud costs (Denial of Wallet).

---

## Obsidian Security: The Identity Crisis
*Source: [Obsidian Security State of SaaS Security](https://www.obsidiansecurity.com/)*

Obsidian argues that AI Security is fundamentally an **Identity** problem.

- **Non-Human Identities (NHIs)**: AI Agents are the fastest-growing class of NHIs. They often share service accounts with "God Mode" privileges to read SharePoint, Jira, and Slack.
- **The Risk**: If an attacker compromises an agent (via prompt injection), they inherit the agent's permissions. Since agents engage in high-volume, automated activity, malicious actions are harder to distinguish from normal behavior.

---

## Recommended Action Plan for 2026

1.  **Discover**: Run an "Agent Inventory" scan. You cannot secure what you cannot see.
2.  **Govern**: Deploy an **AI Gateway** (e.g., Gravitee, Kong, or cloud-native equivalents) to intercept and inspect all agent traffic.
3.  **Identity**: Enforce **Service Accounts** for agents. Never allow an agent to run as a human user. Rotate keys daily.
4.  **Monitor**: Shift from "Log Analytics" to "Behavioral Analytics." Alert on agents accessing unusual data volumes or new data types.

## Helpful Links & Resources
- **[Gravitee.io State of AI Agent Security](https://www.gravitee.io/state-of-ai-agent-security)** – *The definitive report on agent governance.*
- **[OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)** – *The standard for AI application security.*
- **[NIST AI Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework)** – *US Government standard for AI safety.*
- **[Wiz AI Security Research](https://www.wiz.io/research)** – *Cloud-centric AI security findings.*
- **[Microsoft AI Red Team Guidelines](https://learn.microsoft.com/en-us/security/ai-red-teaming)** – *Best practices for testing agent robustness.*

## Latest Industry Updates
- **2026-02-04** [State of AI Agent Security 2026 Report: When Adoption Outpaces Control](https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control) - *Gravitee.io Blog*
- **2026-01-22** [Gravitee 4.10: One Control Point to Secure & Govern AI Agents, MCP, and LLMs](https://www.gravitee.io/blog/gravitee-4.10-one-control-point-to-secure-govern-ai-agents-mcp-and-llms) - *Gravitee.io Blog*
- **2026-01-22** [MCP Proxy: Unified Governance for Agents Tools](https://www.gravitee.io/blog/mcp-proxy-unified-governance-for-agents-tools) - *Gravitee.io Blog*
- **2026-01-22** [LLM Proxy: One Front Door to Multiple LLM Providers](https://www.gravitee.io/blog/llm-proxy-one-front-door-to-multiple-llm-providers) - *Gravitee.io Blog*
- **2026-01-20** [Distributed sync process for more resilient gateways](https://www.gravitee.io/blog/distributed-sync-process-for-more-resilient-gateways) - *Gravitee.io Blog*
- **2026-02-23** [MCP Authorization: How to Manage Permissions for AI Agents & Services](https://www.gravitee.io/blog/mcp-authorization-how-to-manage-permissions-for-ai-agents-services) - *Gravitee.io Blog*
- **2026-02-23** [MCP Authentication: The Complete Guide to Modern Credential Flow in AI Systems](https://www.gravitee.io/blog/mcp-authentication-the-complete-guide-to-modern-credential-flow-in-ai-systems) - *Gravitee.io Blog*
- **2026-02-13** [How AI Changes Authentication & Authorization Models](https://www.gravitee.io/blog/how-ai-changes-authentication-authorization-models) - *Gravitee.io Blog*
- **2026-02-24** [Security Insights Where Work Happens: Notion Custom Agents + Wiz MCP](https://www.wiz.io/blog/wiz-notion-mcp-agents-integration) - *Wiz Blog*
- **2026-02-20** [Building an Agentic Cloud Security Ecosystem: A Reference Architecture with Wiz MCP and Infosys Cyber Next](https://www.wiz.io/blog/infosys-mcp) - *Wiz Blog*
- **2026-02-12** [Introducing AI Cyber Model Arena: A Real-World Benchmark for AI Agents in Cybersecurity](https://www.wiz.io/blog/introducing-ai-cyber-model-arena-a-real-world-benchmark-for-ai-agents-in-cybersec) - *Wiz Blog*
- **2026-02-02** [Building AI Security Together: New Ways to Partner with Wiz for AI Security in 2026](https://www.wiz.io/blog/win-ai-partnerships) - *Wiz Blog*
- **2026-02-02** [Hacking Moltbook: The AI Social Network Any Human Can Control](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys) - *Wiz Blog*
- **2026-03-27** [88% of Companies Have Already Seen AI Agent Security Failures](https://www.gravitee.io/blog/88-of-companies-have-already-seen-ai-agent-security-failures) - *Gravitee.io Blog*
- **2026-03-30** [The Wiz Blue Agent, now Generally Available](https://www.wiz.io/blog/wiz-blue-agent-generally-available) - *Wiz Blog*
- **2026-03-26** [Introducing the Green Agent: AI-Powered Remediation for the Cloud](https://www.wiz.io/blog/introducing-wiz-green-agent) - *Wiz Blog*
- **2026-03-25** [Introducing Wiz Workflows: Your path to building a self healing cloud](https://www.wiz.io/blog/introducing-wiz-workflows) - *Wiz Blog*
- **2026-03-23** [Introducing the Wiz Red Agent- AI-Powered Attacker](https://www.wiz.io/blog/introducing-the-wiz-red-agent) - *Wiz Blog*
- **2026-03-23** [Introducing Wiz AI Application Protection Platform (AI-APP)](https://www.wiz.io/blog/introducing-wiz-ai-app) - *Wiz Blog*
- **2026-03-23** [Introducing Wiz Agents & Workflows: Security at the Speed of AI](https://www.wiz.io/blog/introducing-wiz-agents) - *Wiz Blog*
- **2026-03-11** [It’s Official: Wiz Joins Google](https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz) - *Wiz Blog*
- **2026-03-03** [Seeing AI Clearly: Building Visibility Across Modern AI Applications](https://www.wiz.io/blog/complete-ai-application-visibility-wiz) - *Wiz Blog*
- **2026-03-31** [Double Agents: Exposing Security Blind Spots in GCP Vertex AI](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/) - *Palo Alto Networks Unit 42*
- **2026-03-20** [Who’s Really Shopping? Retail Fraud in the Age of Agentic AI](https://unit42.paloaltonetworks.com/retail-fraud-agentic-ai/) - *Palo Alto Networks Unit 42*
- **2026-03-18** [Navigating Security Tradeoffs of AI Agents](https://unit42.paloaltonetworks.com/navigating-security-tradeoffs-ai-agents/) - *Palo Alto Networks Unit 42*
- **2026-03-17** [Open, Closed and Broken: Prompt Fuzzing Finds LLMs Still Fragile Across Open and Closed Models](https://unit42.paloaltonetworks.com/genai-llm-prompt-fuzzing/) - *Palo Alto Networks Unit 42*
- **2026-04-14** [Gravitee 4.11: Protect, Optimise, and Govern Your AI Stack](https://www.gravitee.io/blog/gravitee-4.11-protect-optimise-and-govern-your-ai-stack) - *Gravitee.io Blog*
- **2026-04-13** [Trusted On-Behalf-Of: Agent Delegation in Gravitee 4.11](https://www.gravitee.io/blog/trusted-on-behalf-of-agent-delegation-in-gravitee-4.11) - *Gravitee.io Blog*
- **2026-04-10** [AI Observability for Enterprise Teams: Monitor MCP Tools, LLM Costs, and Agent Traffic in One Place](https://www.gravitee.io/blog/ai-observability-for-enterprise-teams-monitor-mcp-tools-llm-costs-and-agent-traffic-in-one-place) - *Gravitee.io Blog*
- **2026-04-30** [Red Agent and Claude Opus: Securing Production Targets at Scale](https://www.wiz.io/blog/red-agent-claude-opus) - *Wiz Blog*
- **2026-04-29** [Wiz Code Week Recap: Securing AI Native Development](https://www.wiz.io/blog/wiz-code-week-recap) - *Wiz Blog*
- **2026-04-22** [Wiz at Google Next: Machine-Speed Defense for Any Cloud, Any Platform, Any AI](https://www.wiz.io/blog/wiz-at-google-cloud-next) - *Wiz Blog*
- **2026-04-21** [Closing the Security Gap in the Age of Agentic Coding](https://www.wiz.io/blog/securing-software-age-of-agentic-coding) - *Wiz Blog*
- **2026-04-16** [Securing AI Applications From Inception to Deployment](https://www.wiz.io/blog/securing-ai-application-from-inception-to-deployment) - *Wiz Blog*
- **2026-04-10** [Claude Mythos: Preparing for a World Where AI Finds and Exploits Vulnerabilities Faster Than Ever](https://www.wiz.io/blog/claude-mythos) - *Wiz Blog*
- **2026-04-23** [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/) - *Palo Alto Networks Unit 42*
- **2026-04-20** [Fracturing Software Security With Frontier AI Models](https://unit42.paloaltonetworks.com/ai-software-security-risks/) - *Palo Alto Networks Unit 42*
- **2026-04-08** [Cracks in the Bedrock: Agent God Mode](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/) - *Palo Alto Networks Unit 42*
- **2026-04-07** [Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/) - *Palo Alto Networks Unit 42*
- **2026-04-03** [When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/) - *Palo Alto Networks Unit 42*
- **2026-05-28** [AI Management Without The Patchwork](https://www.gravitee.io/blog/ai-management-without-the-patchwork) - *Gravitee.io Blog*
- **2026-05-28** [Context as a Service: The New Price of Staying Relevant](https://www.gravitee.io/blog/context-as-a-service-the-new-price-of-staying-relevant) - *Gravitee.io Blog*
- **2026-05-14** [MCP AI Explained: How Model Context Protocol Works](https://www.gravitee.io/blog/mcp-ai-explained-how-model-context-protocol-works) - *Gravitee.io Blog*
- **2026-05-14** [Event Stream Processor: How It Works & Where Governance Fits](https://www.gravitee.io/blog/event-stream-processor-how-it-works-where-governance-fits) - *Gravitee.io Blog*
- **2026-05-07** [The OWASP MCP Top 10 and AI IAM: Why Agents Need Identity-First Security](https://www.gravitee.io/blog/the-owasp-mcp-top-10-and-ai-iam-why-agents-need-identity-first-security) - *Gravitee.io Blog*
- **2026-05-08** [A Framework for AI Threat Readiness](https://www.wiz.io/blog/ai-threat-readiness-framework) - *Wiz Blog*
- **2026-05-05** [Introducing Penetration Test Findings: Unified Offensive Security in Wiz](https://www.wiz.io/blog/pen-test-findings) - *Wiz Blog*
- **2026-06-19** [What Every MCP Builder Needs to Know Before July](https://www.gravitee.io/blog/what-every-mcp-builder-needs-to-know-before-july) - *Gravitee.io Blog*
- **2026-06-19** [What Does API Stand For? Application Programming Interface Explained](https://www.gravitee.io/blog/what-does-api-stand-for-application-programming-interface-explained) - *Gravitee.io Blog*
- **2026-06-18** [Who Let the Agent In? Securing MCP Servers in Production](https://www.gravitee.io/blog/who-let-the-agent-in-securing-mcp-servers-in-production) - *Gravitee.io Blog*
- **2026-06-18** [MCP Server Mediation: Securing Third-Party MCP Connections](https://www.gravitee.io/blog/mcp-server-mediation-securing-third-party-mcp-connections) - *Gravitee.io Blog*
- **2026-06-29** [The Red Agent POV: Exploiting Broken Object-Level Authorization in an Airline GraphQL API](https://www.wiz.io/blog/red-agent-pov-bola) - *Wiz Blog*
- **2026-06-17** [The Red Agent POV: How it Reasoned its Way to SSRF](https://www.wiz.io/blog/red-agent-pov-ssrf) - *Wiz Blog*
- **2026-06-17** [Introducing the Red Agent POV Series](https://www.wiz.io/blog/red-agent-pov-series) - *Wiz Blog*
- **2026-06-23** [OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/) - *Palo Alto Networks Unit 42*
- **2026-06-11** [Trust No Skill: Integrity Verification for AI Agent Supply Chains](https://unit42.paloaltonetworks.com/ai-agent-supply-chain-risks/) - *Palo Alto Networks Unit 42*
- **2026-07-31** [MCP Credential Brokering: Keep API Keys From AI Agents](https://www.gravitee.io/blog/mcp-credential-brokering-keep-api-keys-from-ai-agents) - *Gravitee.io Blog*
- **2026-07-28** [Op Ed: To Regulate or Not to Regulate - That is The Question](https://www.gravitee.io/blog/op-ed-to-regulate-or-not-to-regulate-that-is-the-question) - *Gravitee.io Blog*
- **2026-07-23** [The Scariest Part of the OpenAI-Hugging Face Breach Isn't the Hack. It's How Far the Agent Got!](https://www.gravitee.io/blog/the-scariest-part-of-the-openai-hugging-face-breach-isnt-the-hack.-its-how-far-the-agent-got) - *Gravitee.io Blog*
- **2026-07-13** [Gravitee 4.12: See Everything, Enable Everyone](https://www.gravitee.io/blog/gravitee-4.12-see-everything-enable-everyone) - *Gravitee.io Blog*
- **2026-07-09** [First-Class Agent Identities + Self-Service Onboarding For The MCP Era](https://www.gravitee.io/blog/first-class-agent-identities-self-service-onboarding-for-the-mcp-era) - *Gravitee.io Blog*
- **2026-07-08** [Redefining Authorization Management for the Modern Agent-First Enterprise](https://www.gravitee.io/blog/redefining-authorization-management-for-the-modern-agent-first-enterprise) - *Gravitee.io Blog*
- **2026-07-30** [Rethinking Scanning for the AI Era: Wiz’s Agentic Code Security System](https://www.wiz.io/blog/agentic-code-security) - *Wiz Blog*
- **2026-07-29** [The Wiz Red Agent is Now Generally Available](https://www.wiz.io/blog/wiz-red-agent-is-ga) - *Wiz Blog*
- **2026-07-27** [Atlas: Wiz's autonomous AI Agent for vulnerability research, ranked #1 on CyberGym](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher) - *Wiz Blog*
- **2026-07-22** [Opening the Black Box: Agentless Threat Detection for Virtual Appliances](https://www.wiz.io/blog/agentless-threat-hunting-fortigate) - *Wiz Blog*
- **2026-07-21** [Agentless Threat Detection: Illuminating Cloud Blind Spots](https://www.wiz.io/blog/agentless-visibility-uncovering-cloud-blind-spots) - *Wiz Blog*
- **2026-07-15** [The Red Agent POV: The One Boolean That Broke a B2B Platform’s Credit System](https://www.wiz.io/blog/red-agent-pov-business-logic) - *Wiz Blog*
- **2026-07-08** [Wiz ASM for any environment, any risk, everywhere](https://www.wiz.io/blog/wiz-asm-auto-recon) - *Wiz Blog*
- **2026-07-02** [Build AI Security Agents with Wiz MCP](https://www.wiz.io/blog/introducing-wiz-mcp) - *Wiz Blog*
- **2026-07-30** [Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) - *Palo Alto Networks Unit 42*
