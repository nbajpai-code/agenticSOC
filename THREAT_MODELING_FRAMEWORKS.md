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
*Last Updated: 2026-07-31 10:42:20 UTC*

### 📄 Latest Research (Arxiv)
*   [Emerging Challenges in Threat Modeling for GenAI-Augmented Systems: A View from the Trenches](http://arxiv.org/abs/2607.28431v1) (2026-07-30)
*   [Strategy Phasing of Cyber Attacks on Digital Substations](http://arxiv.org/abs/2607.27661v1) (2026-07-30)
*   [Revisiting the Adversarial Robustness of Graph-Based Traffic Forecasting](http://arxiv.org/abs/2607.27604v1) (2026-07-30)
*   [ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping](http://arxiv.org/abs/2607.27528v1) (2026-07-29)
*   [Send and Pretend: Exploiting Transcript Consistency Issues in End-to-End Encrypted Group Chats](http://arxiv.org/abs/2607.27510v1) (2026-07-29)

### 📰 Latest News
No related news found this week.
