import feedparser
import os
from datetime import datetime
import pytz

def fetch_security_week_updates():
    feed_url = "https://www.securityweek.com/feed/"
    feed = feedparser.parse(feed_url)
    
    # Define keywords to filter actionable insights
    # "agentic SOC" is very specific, so we broaden to AI/LLM + SOC/Security, and general high-severity threats.
    keywords = [
        "agentic", "agent", "soc", "security operations", 
        "ai ", "artificial intelligence", "llm", "generative ai",
        "apt", "vulnerability", "malware", "ransomware", "zero-day",
        "threat intelligence", "supply chain"
    ]
    
    relevant_entries = []
    
    print(f"Fetching updates from {feed_url}...")
    
    for entry in feed.entries:
        title = entry.title.lower()
        summary = entry.summary.lower() if 'summary' in entry else ""
        content = entry.content[0].value.lower() if 'content' in entry else ""
        
        # Check if any keyword is in title or summary
        if any(k in title for k in keywords) or any(k in summary for k in keywords):
            relevant_entries.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary if 'summary' in entry else "No summary available."
            })
            
    # Sort by published date (if parsed mostly correct, feedparser usually handles this)
    # usually feeds are already sorted new to old.
    
    # Generate Markdown
    md_content = "# Security Week: Actionable Insights & Updates\n\n"
    md_content += f"**Last Updated:** {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
    md_content += "This tracker monitors [SecurityWeek](https://www.securityweek.com) for news related to **Agentic SOC**, **Advanced Threats**, and **AI in Cybersecurity**.\n\n"
    
    if not relevant_entries:
        md_content += "No relevant updates found in the latest feed.\n"
    else:
        for item in relevant_entries:
            md_content += f"## [{item['title']}]({item['link']})\n"
            md_content += f"**Date:** {item['published']}\n\n"
            md_content += f"{item['summary']}\n\n"
            md_content += "---\n"

    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'SECURITY_WEEK_SUMMARY.md')
    with open(output_file, 'w') as f:
        f.write(md_content)
    
    print(f"Successfully updated {output_file} with {len(relevant_entries)} items.")

if __name__ == "__main__":
    fetch_security_week_updates()
