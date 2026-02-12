# OWASP AI Vulnerability Scoring System (AIVSS)

## Overview
The **OWASP AI Vulnerability Scoring System (AIVSS)** is a standardized framework designed to evaluate and quantify security risks in Artificial Intelligence systems. Unlike traditional scoring systems (like CVSS) which may not capture the nuances of stochastic and probabilistic AI behaviors, AIVSS focuses on the unique vectors associated with Generative AI, Large Language Models (LLMs), and Agentic AI.

## Key Goals
*   **Standardization**: Provide a consistent metric for AI security risks.
*   **AI-Specific Context**: Address non-deterministic outputs, prompt injection, and model hallucinations.
*   **Agentic Focus**: Specifically cater to "Agentic AI" architectures where AI systems have autonomy and tool-use capabilities.

## AIVSS Framework Components

### 1. Scoring Factors
The system typically evaluates vulnerabilities based on:
*   **Model Robustness (MR)**: Resistance to adversarial attacks (e.g., poisoning, evasion).
*   **Data Sensitivity (DS)**: Impact of potential data leakage (training data or context).
*   **Ethical Implications (EI)**: Bias, toxicity, and potential for harm.
*   **System Agency**: The level of autonomy the AI agent possesses (e.g., read-only vs. execute actions).

### 2. Vulnerability Categories
AIVSS aligns closely with the **OWASP Top 10 for LLMs**:
*   **Prompt Injection**: Unauthorized control over model output.
*   **Insecure Output Handling**: Downstream execution of malicious model output.
*   **Supply Chain Vulnerabilities**: Compromised implementation of third-party models/libraries.
*   **Excessive Agency**: Agents performing unauthorized actions.

## References

### Official Repositories
*   **OWASP AIVSS Project**: [OWASP/www-project-artificial-intelligence-vulnerability-scoring-system](https://github.com/OWASP/www-project-artificial-intelligence-vulnerability-scoring-system)
    *   *The central repository for the AIVSS framework, rubrics, and methodologies.*
    
*   **Agentic AI Vulnerability Scoring System (Page)**: [Detailed Scoring Calculator & Framework](https://github.io/agentic-ai-vulnerability-scoring) *(Check specific repo links for latest version)*

### Related OWASP Standards
*   **OWASP Top 10 for LLM Applications**: [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
*   **OWASP AI Exchange**: [AI Security Exchange](https://owasp.org/www-project-ai-security-and-privacy-guide/)

## Usage in Agentic SOC
For an **Agentic SOC** (Security Operations Center), AIVSS provides the necessary rubric to:
1.  Score the risk of automated SOC analysts.
2.  Evaluate the "trustworthiness" of autonomous remediation actions.
3.  Define "Circuit Breakers" based on vulnerability scores (e.g., "Do not execute remediation if AIVSS score > 7.0").
