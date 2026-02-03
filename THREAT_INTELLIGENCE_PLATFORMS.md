# Threat Intelligence Platform Documentation Hubs

A curated list of comprehensive references and documentation hubs for major Threat Intelligence Platforms (TIPs), Security Operations Center (SOC) tools, and Threat Hunting resources.

## Major Commercial Platforms

### [Google Threat Intelligence](https://gtidocs.virustotal.com/)
Key documentation hub for Google's threat intelligence offerings, primarily centering on VirusTotal and related integrations.
- **Why it's useful**: Extensive API documentation, hunting patterns, and graph theory concepts for threat analysis.
- **Key Sections**:
    - [VirusTotal API v3](https://developers.virustotal.com/reference/overview)
    - [YARA Documentation](https://yara.readthedocs.io/en/stable/)
    - [Graph Visualization](https://gtidocs.virustotal.com/docs/graph-overview)

### [CrowdStrike Falcon](https://www.crowdstrike.com/resources/)
The public face of CrowdStrike's vast documentation ecosystem. While some deep technical docs require a login, their public resources and developer hub are extensive.
- **Why it's useful**: detailed guides on Endpoint Detection & Response (EDR) and Threat Intelligence module integration.
- **Key Sections**:
    - [Falcon Developer Portal (APIs)](https://falcon.crowdstrike.com/login/?next=%2Fsupport%2Fdocumentation) (Login required for full API docs)
    - [CrowdStrike Tech Center](https://www.crowdstrike.com/resources/tech-center/) (How-to guides & Demos)
    - [Adversary Universe](https://adversary.crowdstrike.com/en-US/) (Threat Actor profiles)

### [Microsoft Defender Threat Intelligence](https://learn.microsoft.com/en-us/defender/threat-intelligence/)
Microsoft's centralized documentation for their Threat Intelligence product, formerly RiskIQ.
- **Why it's useful**: Deep integration with the Microsoft 365 security stack and detailed threat actor profiles.
- **Key Sections**:
    - [Defender TI API](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0) (Microsoft Graph Security API)
    - [Threat Actor Naming](https://learn.microsoft.com/en-us/defender/threat-intelligence/threat-analytics-threat-naming)
    - [Indicator Management](https://learn.microsoft.com/en-us/defender/threat-intelligence/manage-indicators)

### [Palo Alto Networks Unit 42 / Cortex XSOAR](https://docs-cortex.paloaltonetworks.com/)
Documentation for Palo Alto's automation and threat intelligence platform.
- **Why it's useful**: Excellent resource for SOAR playbooks and "ATOMs" (Actionable Threat Objects and Mitigations).
- **Key Sections**:
    - [Unit 42 Playbooks](https://unit42.paloaltonetworks.com/playbook-viewer/)
    - [Cortex XSOAR Marketplace Integrations](https://cortex.marketplace.pan.dev/)
    - [XSOAR Developer Database](https://xsoar.pan.dev/)

### [Recorded Future](https://support.recordedfuture.com/hc/en-us)
Knowledge base for one of the world's largest intelligence providers. (Note: Full access often requires customer login, but API docs are often public).
- **Why it's useful**: Comprehensive ontology for threat data and detailed API references.
- **Key Sections**:
    - [Recorded Future API](https://api.recordedfuture.com/v1/)
    - [Insikt Group Research](https://www.recordedfuture.com/insikt-group)

### [BehavioSec / LexisNexis ThreatMetrix](https://risk.lexisnexis.com/products/threatmetrix)
(Included for behavioral biometrics and fraud intelligence references).

### [Mandiant Advantage](https://docs.mandiant.com/)
Now part of Google Cloud, Mandiant provides top-tier frontline intelligence.
- **Why it's useful**: "Frontline" intelligence derived from actual incident responses.
- **Key Sections**:
    - [Mandiant Advantage API](https://api.mandiant.com/)
    - [APT Groups](https://www.mandiant.com/resources/insights/apt-groups)

### [ThreatConnect](https://training.threatconnect.com/)
A learning portal and knowledge base combining TIP and SOAR documentation.
- **Why it's useful**: Good examples of data modeling for threats and CAL (Collective Analytics Layer).
- **Key Sections**:
    - [ThreatConnect API](https://docs.threatconnect.com/en/latest/rest_api/rest_api.html)
    - [Playbooks](https://docs.threatconnect.com/en/latest/playbooks/playbooks.html)

### [IBM X-Force Exchange](https://exchange.xforce.ibmcloud.com/faq)
IBM's collaborative threat intelligence platform.
- **Why it's useful**: Open access to a lot of threat data and vulnerability information without a paid subscription (for basic queries).
- **Key Sections**:
    - [X-Force API User Guide](https://api.xforce.ibmcloud.com/doc/)
    - [X-Force Collections](https://exchange.xforce.ibmcloud.com/activity/list)

### [Anomali ThreatStream](https://www.anomali.com/resources/documentation)
Documentation for Anomali's threat intelligence management platform.
- **Key Sections**:
    - [Anomali SDK](https://github.com/anomali)

---

## Open Source & Community Platforms

### [MISP (Malware Information Sharing Platform)](https://www.misp-project.org/documentation/)
The standard for open-source threat intelligence sharing.
- **Why it's useful**: The "MISP Book" is a gold standard for understanding how to structure and share IOCs.
- **Key Sections**:
    - [MISP User Guide](https://www.circleid.com/pdf/MISP-Book.pdf)
    - [PyMISP (Python Library)](https://github.com/MISP/PyMISP)
    - [MISP Objects Template](https://www.misp-project.org/objects.html)

### [OpenCTI](https://docs.opencti.io/latest/)
A modern open-source platform for unifying cyber threat intelligence.
- **Why it's useful**: Based on STIX2 standards, excellent for understanding threat relationships and graph databases in TI.
- **Key Sections**:
    - [OpenCTI Administration](https://docs.opencti.io/latest/administration/)
    - [The STIX Standard](https://oasis-open.github.io/cti-documentation/stix/intro)

### [MITRE ATT&CK](https://attack.mitre.org/)
While not a "platform" in the traditional sense, it is the foundational knowledge base for all modern threat modeling.
- **Key Sections**:
    - [Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
    - [Groups (Threat Actors)](https://attack.mitre.org/groups/)
