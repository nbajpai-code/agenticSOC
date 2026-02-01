# Mastering ChatGPT for Threat Intelligence: A Comprehensive Prompt Library

This library contains categorized prompts designed to leverage ChatGPT for Threat Intelligence (CTI) and Security Operations Center (SOC) tasks.

## 🔍 1. Threat Actor & TTP Analysis
Use these prompts to profile adversaries and understand their tactics, techniques, and procedures (TTPs).

*   **TTP Mapping**: "Analyze the following threat report summary and map the observed behaviors to the MITRE ATT&CK framework techniques and tactics: [Insert Report/Text]."
*   **Adversary Profiling**: "Based on the following indicators and behaviors, which known Threat Actor (APT group) does this most closely resemble? Explain your reasoning referring to common TTPs of that group: [Insert Indicators]."
*   **Campaign Evolution**: "Summarize the evolution of the [Insert APT Name] threat group over the last 3 years, specifically focusing on changes in their malware toolset and targeting scope."
*   **Hypothesis Generation**: "Generate 5 hypotheses for a potential cyber attack against a [Insert Industry, e.g., Financial] organization involving [Insert Specific Tech, e.g., Kubernetes] infrastructure."
*   **Cybercrime Forum Analysis**: "Analyze the following unstructured text from a cybercrime forum. Extract variables related to targeted organizations, technologies being exploited, and the actor's intent: [Insert Text]."

## 🧬 2. IOC Analysis & Deobfuscation
Help with analyzing Indicators of Compromise and understanding malicious scripts.

*   **Log Log Analysis**: "Analyze the following log snippet for signs of malicious activity. Highlight suspicious IP addresses, user agents, or command patterns: [Insert Log Snippet]."
*   **Script Explanation**: "Explain what the following PowerShell/Bash script does line-by-line. Identify any malicious intent or data exfiltration techniques: [Insert Code]."
*   **Base64 Decoding**: "Decode the following Base64 string and explain if the output looks like a command, a URL, or binary data: [Insert String]."
*   **Regex Generation**: "Write a Regular Expression (Regex) to detect the following pattern in a server log file: [Describe Pattern, e.g., credit card numbers, specific error codes]."

## 🛡️ 3. Vulnerability & Risk Assessment
Prompts to contextualize vulnerabilities and prioritize patches.

*   **CVE Context**: "Explain CVE-[Insert ID] in simple terms. How is it exploited, what is the impact, and is there a known Proof of Concept (PoC) available?"
*   **Risk Prioritization**: "I have the following 5 vulnerabilities detected in my environment. Based on exploitability and impact, rank them in order of priority for patching: [Insert List of CVEs]."
*   **Mitigation Strategies**: "Suggest temporary mitigation strategies for [Insert Vulnerability Name] if we cannot immediately apply the vendor patch."

## 🚨 4. Incident Response & Playbooks
Assistance during active incidents or for preparation.

*   **Playbook Creation**: "Draft a step-by-step Incident Response Playbook for a [Insert Scenario, e.g., Ransomware Infection] scenario, covering Detection, Containment, Eradication, and Recovery."
*   **Communication Templates**: "Write a notification email to employees alerting them of a phishing campaign targeting the organization. Keep the tone urgent but calm, and provide 3 tips to identify the email."
*   **SOC Query Generation**: "Write a Splunk SPL / KQL query to search for successful logins from outside our geo-location followed by large data transfers: [Insert specific index/source details if known]."

## 📝 5. Reporting & Summarization
Turning raw data into actionable intelligence.

*   **Executive Summary**: "Summarize the technical details of the following incident report into a 1-paragraph Executive Summary suitable for a C-Level audience: [Insert Technical Details]."
*   **Threat Briefing**: "Create a weekly threat intelligence briefing outline covering the top 3 emerging threats in the [Insert Industry] sector."
*   **Technical to Non-Technical**: "Rewrite the following technical finding to be understood by a Legal or HR representative: [Insert Technical Paragraph]."

## 🎓 6. Training & Simulation
Using ChatGPT for skill building.

*   **Scenario Generation**: "Create a Tabletop Exercise (TTX) scenario for a SOC team involving a supply chain attack via a software update. Include 3 distinct 'injects' or complications that occur during the exercise."
*   **Quiz Creation**: "Generate 5 multiple-choice questions to test a junior analyst's understanding of DNS tunneling detection."
*   **RAG Simulation**: "Act as a Retrieval-Augmented Generation (RAG) system. I will provide a snippet of a knowledge base below. Answer questions ONLY based on that snippet. Snippet: [Insert Data]. Question: [Insert Question]."

## 📚 7. Key References & Research
Enrich your understanding with these foundational papers and guidelines.

### NIST Guidelines (National Institute of Standards and Technology)
*   **NIST AI Risk Management Framework: Generative AI Profile (NIST AI 600-1)**:
    *   *Focus*: Managing risks specific to Generative AI, including hallucinations, bias, and data security.
    *   *Link*: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
*   **Secure Software Development Practices for Generative AI (SP 800-218A)**:
    *   *Focus*: Protecting training data and model integrity to prevent poisoning and supply chain attacks.

### Arxiv Research Papers
*   **"Automation of Threat Intelligence Workflows"**: Research validating the use of LLMs for IOC extraction and creating relationship graphs.
*   **"Threat Intelligence Copilots"**: Concepts around using AI as an assistant for attribution and prioritization.
*   **"Benchmarking LLM Performance"**: Look for **CyberSOCEval** and **CTIBench** to understand how different models perform on specific cybersecurity tasks.

## 🛠️ 8. Community Tools & Repositories
Explore these GitHub repositories for more prompts and tools.

*   **[Prompt-Hacking-Resources](https://github.com/PromptLabs/Prompt-Hacking-Resources)**: Excellent for dealing with adversarial prompts and understanding injection attacks.
*   **[Cyber-Security-chatGPT-prompt](https://github.com/DummyKitty/Cyber-Security-chatGPT-prompt)**: A collection of community-sourced prompts for various security roles.
*   **[cybersecurity-threat-intelligence](https://github.com/paulveillard/cybersecurity-threat-intelligence)**: Tools and indicators that can be paired with LLM analysis.

## 💡 Best Practices for Prompting
*   **Context is King**: Always provide specific context (logs, error messages, industry) for better results.
*   **Chain functionality**: Ask follow-up questions. "Critique your own analysis above - what did you miss?"
*   **Sanitize Data**: **NEVER** paste real PII, credentials, or sensitive internal IP addresses into a public LLM.
