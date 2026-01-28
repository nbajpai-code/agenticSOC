from langchain_core.tools import tool
import random

@tool
def search_sim_logs(query: str) -> str:
    """
    Simulates searching a SIEM (like Splunk or Sentinel) for logs related to a query.
    Useful for finding login attempts, traffic patterns, or error messages.
    """
    print(f"\n[Tool] Searching SIEM logs for: {query}")
    # Mock logic based on common queries
    if "admin" in query.lower() or "failed" in query.lower():
        return "Found 15 failed login attempts for user 'admin' from IP 192.168.1.50 in the last 1 hour."
    elif "192.168.1.50" in query:
        return "IP 192.168.1.50 has been scanned by the firewall for port scanning behavior."
    else:
        return "No significant anomalies found in logs."

@tool
def virustotal_lookup(indicator: str) -> str:
    """
    Simulates checking a file hash, IP, or domain against VirusTotal threat intelligence.
    Returns the reputation score and category.
    """
    print(f"\n[Tool] Checking VirusTotal for: {indicator}")
    if "192.168.1.50" in indicator:
        return "Reputation: Malicious. Score: 85/100. Category: Known Scanner/Botnet."
    elif "bad_hash" in indicator:
        return "Reputation: Malicious. Score: 98/100. Ransomware signature detected."
    else:
        return "Reputation: Clean. Score: 0/100."

@tool
def firewall_block_ip(ip: str) -> str:
    """
    Simulates a firewall action to block a specific IP address.
    """
    print(f"\n[Tool] Blocking IP on Firewall: {ip}")
    return f"Successfully executed block rule for IP {ip}."

mock_tools_list = [search_sim_logs, virustotal_lookup, firewall_block_ip]
