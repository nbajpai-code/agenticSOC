import arxiv
import feedparser
import os
from datetime import datetime
import pytz

def fetch_frontiers_content():
    # 1. Fetch from Arxiv (Research Frontiers)
    # Query logic: (AI AND Security) OR (Quantum AND Cryptography) OR (Zero Trust)
    # But specifically "Agentic" is hot.
    
    arxiv_query = '(all:"agentic ai" OR all:"autonomous soc" OR all:"post-quantum cryptography" OR all:"adversarial machine learning" OR all:"moving target defense" OR all:"zero trust architecture")'
    
    search = arxiv.Search(
        query=arxiv_query,
        max_results=15,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    
    papers = []
    try:
        client = arxiv.Client()
        results = client.results(search)
        for result in results:
            papers.append({
                'title': result.title,
                'url': result.entry_id,
                'published': result.published.strftime('%Y-%m-%d'),
                'source': 'Arxiv'
            })
    except Exception as e:
        print(f"Error fetching Arxiv: {e}")

    # 2. Fetch from Security Week (News Frontiers)
    # Use the existing RSS feed but filter for "Frontier" keywords
    feed_url = "https://www.securityweek.com/feed/"
    feed = feedparser.parse(feed_url)
    
    news_items = []
    keywords = [
        "quantum", "ai ", "artificial intelligence", "deepfake", 
        "zero trust", "supply chain", "autonomous", "resilience"
    ]
    
    for entry in feed.entries:
        title = entry.title.lower()
        if any(k in title for k in keywords):
            news_items.append({
                'title': entry.title,
                'url': entry.link,
                'published': entry.published,
                'source': 'SecurityWeek'
            })
            if len(news_items) >= 10: break

    # Generate Content
    md_content = "# Frontiers in Cybersecurity Technology\n\n"
    md_content += f"**Last Updated:** {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
    
    md_content += "## 🚀 Key Frontiers (2025-2026)\n"
    md_content += "*   **Agentic AI & Autonomous SOC**: AI models that plan and execute multi-step security workflows involved in detection, triage, and response.\n"
    md_content += "*   **Post-Quantum Cryptography (PQC)**: Transitioning to cryptographic algorithms resistant to quantum computer attacks.\n"
    md_content += "*   **Identity Resilience & Deepfake Defense**: Combating synthetic media and sophisticated identity attacks.\n"
    md_content += "*   **IT/OT Convergence Security**: Integrated protection for industrial control systems merged with enterprise IT.\n"
    md_content += "*   **Automated Moving Target Defense (AMTD)**: Dynamic shifting of attack surfaces to confuse adversaries.\n\n"

    md_content += "## 📄 Latest Research (Arxiv)\n"
    if not papers:
        md_content += "No new research papers found recently.\n"
    else:
        for p in papers:
            md_content += f"*   [{p['title']}]({p['url']}) ({p['published']})\n"

    md_content += "\n## 📰 Latest Signal (News)\n"
    if not news_items:
        md_content += "No recent news matching frontier topics.\n"
    else:
        for n in news_items:
            md_content += f"*   [{n['title']}]({n['url']}) - *{n['source']}*\n"

    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CYBERSECURITY_FRONTIERS.md')
    with open(output_file, 'w') as f:
        f.write(md_content)
    
    print(f"Updated benchmarks with {len(papers)} papers and {len(news_items)} news items.")

if __name__ == "__main__":
    fetch_frontiers_content()
