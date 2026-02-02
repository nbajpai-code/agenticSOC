# Offensive Security & Red Teaming Tools

This document contains a comprehensive list of open-source tools used for Man-in-the-Middle (MITM) attacks, Remote Access (RAT/C2), Spoofing, and Post-Exploitation.

> [!WARNING]
> **Legal Disclaimer**: These tools are intended for **authorized security testing, red teaming, and educational purposes only**. Using these tools to attack targets without explicit permission is **illegal**. The maintainers of this repository assume no liability for misuse.

## Man-in-the-Middle (MITM)

Tools Intercepting, modifying, and replaying network traffic.

### 1. Bettercap
The "Swiss Army knife" for network attacks and monitoring. It supports ARP spoofing, DNS spoofing, packet sniffing, and more.
- **Language**: Go
- **Features**: Modular, Wi-Fi/BLE/HID support, web UI.
- **Repo**: [bettercap/bettercap](https://github.com/bettercap/bettercap)

### 2. mitmproxy
An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.
- **Language**: Python
- **Features**: SSL/TLS interception, modifying HTTP traffic on the fly, replay requests.
- **Repo**: [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

### 3. Evilginx3
A standalone man-in-the-middle attack framework used for advanced phishing credentials and session cookies, bypassing 2FA.
- **Language**: Go
- **Features**: Phishing with reverse proxy, session hijacking.
- **Repo**: [kgretzky/evilginx2](https://github.com/kgretzky/evilginx2) (Note: Evilginx3 is the latest iteration)

### 4. Ettercap
A comprehensive suite for man-in-the-middle attacks. It features sniffing of live connections, content filtering on the fly.
- **Language**: C
- **Features**: Network protocol analysis, active and passive dissection.
- **Repo**: [Ettercap/ettercap](https://github.com/Ettercap/ettercap)

## Remote Access & Command and Control (C2/RAT)

Tools for maintaining access and controlling compromised systems.

### 5. Sliver
A general-purpose cross-platform implant framework that supports C2 over Mutual-TLS, HTTP(S), and DNS.
- **Language**: Go
- **Features**: Dynamic compilation, multiple C2 protocols, evasion capabilities.
- **Repo**: [BishopFox/sliver](https://github.com/BishopFox/sliver)

### 6. Havoc
A modern and malleable post-exploitation command and control framework.
- **Language**: C / C++ / Go
- **Features**: Modern GUI, malleable profiles, payload generation.
- **Repo**: [HavocFramework/Havoc](https://github.com/HavocFramework/Havoc)

### 7. Quasar RAT
A fast and light-weight remote administration tool coded in C#.
- **Language**: C#
- **Features**: TCP network stream, high stability, easy-to-use GUI.
- **Repo**: [quasar/Quasar](https://github.com/quasar/Quasar)

### 8. AsyncRAT
An open-source remote administration tool designed to monitor and control computers through a secure encrypted connection.
- **Language**: C#
- **Features**: Encrypted connection, plugins, screen capture.
- **Repo**: [NYAN-x-CAT/AsyncRAT-C-Sharp](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp)

### 9. Empire
A post-exploitation framework that includes a pure-PowerShell2.0 Windows agent, and a pure Python 2.6/2.7 Linux/OS X agent.
- **Language**: Python / PowerShell
- **Features**: Cryptological communications, extensive module library.
- **Repo**: [BC-SECURITY/Empire](https://github.com/BC-SECURITY/Empire)

## Spoofing Tools (ARP, DNS, Email, IP)

Tools for masquerading as another device or user.

### 10. Responder
A LLMNR, NBT-NS and MDNS poisoner, with a built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server.
- **Language**: Python
- **Features**: Credential harvesting via spoofed responses in local networks.
- **Repo**: [lgandx/Responder](https://github.com/lgandx/Responder)

### 11. dnschef
A highly configurable DNS proxy for Penetration Testers and Malware Analysts.
- **Language**: Python
- **Features**: Analyze and intercept DNS traffic, fake responses.
- **Repo**: [iphelix/dnschef](https://github.com/iphelix/dnschef)

### 12. Gophish
An open-source phishing toolkit designed for businesses and penetration testers.
- **Language**: Go
- **Features**: Email campaign launching, tracking, template cloning.
- **Repo**: [gophish/gophish](https://github.com/gophish/gophish)

### 13. espoofer
An email spoofing testing tool to check if a target domain is vulnerable to email spoofing (SPF/DKIM/DMARC bypass).
- **Language**: Python
- **Repo**: [chenjj/espoofer](https://github.com/chenjj/espoofer)

## Post-Exploitation & Credential Dumping

Tools used after initial access to gather data or move laterally.

### 14. Mimikatz
A tool to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory.
- **Language**: C
- **Repo**: [gentilkiwi/mimikatz](https://github.com/gentilkiwi/mimikatz)

### 15. BloodHound
uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment.
- **Language**: JavaScript / C#
- **Features**: Visualizing attack paths in AD.
- **Repo**: [BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound)

### 16. Rubeus
A C# toolset for raw Kerberos interaction and abuses.
- **Language**: C#
- **Features**: Roasting, ticket requests, harvest.
- **Repo**: [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus)
