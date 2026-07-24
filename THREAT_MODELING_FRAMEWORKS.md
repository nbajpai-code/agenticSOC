# Threat Modeling Frameworks: STRIDE, DREAD, PASTA

This guide serves as a comprehensive reference for three foundational threat modeling frameworks: **STRIDE**, **DREAD**, and **PASTA**. It includes definitions, scoring methodologies, and best practices for the 2024-2025 security landscape.

## 1. STRIDE
**Origin**: Microsoft  
**Focus**: Identifying threats by categorizing them. Best used during the **design/architecture** phase.

### Categories (The Mnemonics)
| Category | Definition | Violation of Security Property | Example |
| :--- | :--- | :--- | :--- |
| **S**poofing | Pretending to be someone/something else. | **Authenticity** | Using a stolen API key or falsifying an IP address. |
| **T**ampering | Modifying data or code. | **Integrity** | Changing a database record or injecting malicious code into a binary. |
| **R**epudiation | Claiming to not have performed an action. | **Non-repudiation** | A user deleting data without an audit log trace. |
| **I**nformation Disclosure | Exposing information to unauthorized parties. | **Confidentiality** | Leaking PII in error logs or an open S3 bucket. |
| **D**enial of Service | Denying service to valid users. | **Availability** | Flooding a server with requests or consuming all disk space. |
| **E**levation of Privilege | Gaining capabilities without authorization. | **Authorization** | A standard user exploiting a bug to become admin. |

### Best Practices (2025)
*   **Per-Element Analysis**: Apply STRIDE to every element (process, data store, data flow) in your Data Flow Diagram (DFD).
*   **STRIDE-per-Interaction**: Focus on trust boundaries where data crosses between entities.
*   **Automation**: Use tools like Microsoft Threat Modeling Tool or OTM (Open Threat Model).

---

## 2. DREAD
**Status**: *Legacy/Deprecated* by Microsoft, but still widely used for **Quantitative Risk Scoring**.  
**Focus**: Ranking/Prioritizing threats based on risk calculations.

### Scoring Components (Rated 1-10)
**Formula**: `Risk = (D + R + E + A + D) / 5`

1.  **D**amage Potential: How bad is the attack? (0 = Nothing, 10 = Complete System Takeover).
2.  **R**eproducibility: How easy is it to reproduce? (0 = Impossible, 10 = Just a script/URL).
3.  **E**xploitability: How much work is it to launch the attack? (0 = Advanced PhD required, 10 = Automated tool).
4.  **A**ffected Users: How many people will be impacted? (0 = None, 10 = All users).
5.  **D**iscoverability: How easy is it to find the vulnerability? (0 = Hidden, 10 = Visible in source code/UI).

> **Note**: "Discoverability" is often criticized because relying on security through obscurity (low discoverability) is bad practice. Many modern adaptations remove the 'D' and use **DREAD-D** or map it to CVSS.

---

## 3. PASTA
**Origin**: Veracode / Tony UcedaVélez  
**Full Name**: **P**rocess for **A**ttack **S**imulation and **T**hreat **A**nalysis.  
**Focus**: **Risk-Centric** & **Business-Centric**. Aligns technical threats with business objectives.

### The 7 Stages of PASTA
1.  **Define Objectives**: Identify business objectives and security compliance requirements (e.g., GDPR, PCI).
2.  **Define Technical Scope**: Map out the application boundaries and infrastructure.
3.  **Application Decomposition**: Break down the application into components (similar to DFDs in STRIDE).
4.  **Threat Analysis**: Identify likely threat agents (Cyber criminals, Insiders, Script Kiddies).
5.  **Vulnerability & Weakness Analysis**: Map known vulnerabilities (CVEs) to the components.
6.  **Attack Modeling**: Simulate attacks to verify if threats are viable (Attack Trees).
7.  **Risk & Impact Analysis**: Calculate risk based on the probability of attack and business impact.

### Best Practices (2025)
*   **Attack Simulation**: Use PASTA to drive Red Teaming exercises.
*   **Business Alignment**: Use PASTA when you need to justify security spend to non-technical leadership.

---

## 🔄 Weekly Updates (Research & News)
*Last Updated: 2026-07-24 10:22:11 UTC*

### 📄 Latest Research (Arxiv)
*   [The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI](http://arxiv.org/abs/2607.19433v1) (2026-07-20)
*   [ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems](http://arxiv.org/abs/2607.19432v1) (2026-07-20)
*   [Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing](http://arxiv.org/abs/2607.18485v1) (2026-07-20)
*   [Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents](http://arxiv.org/abs/2607.15657v1) (2026-07-17)
*   [Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems](http://arxiv.org/abs/2607.14611v1) (2026-07-16)

### 📰 Latest News
*   [Is Patching Dead? Vulnerability Management in the Post-Mythos Era](https://www.securityweek.com/is-patching-dead-vulnerability-management-in-the-post-mythos-era/) (Thu, 23 Jul 2026 15:00:00 +0000)
