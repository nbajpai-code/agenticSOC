import arxiv
import feedparser
import os
from datetime import datetime
import pytz

def fetch_threat_modeling_updates():
    # 1. Fetch from Arxiv (Research)
    # Query: Threat Modeling, STRIDE, PASTA, Attack Trees
    arxiv_query = '(all:"threat modeling" OR all:"STRIDE framework" OR all:"attack simulation" OR all:"security risk analysis")'
    
    search = arxiv.Search(
        query=arxiv_query,
        max_results=5,
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
                'published': result.published.strftime('%Y-%m-%d')
            })
    except Exception as e:
        print(f"Error fetching Arxiv: {e}")

    # 2. Fetch from News (Security Week)
    feed_url = "https://www.securityweek.com/feed/"
    feed = feedparser.parse(feed_url)
    
    news_items = []
    keywords = ["threat model", "stride", "vulnerability management", "risk analysis", "architecture"]
    
    for entry in feed.entries:
        title = entry.title.lower()
        if any(k in title for k in keywords):
            news_items.append({
                'title': entry.title,
                'url': entry.link,
                'published': entry.published
            })
            if len(news_items) >= 5: break

    # 3. Read and Update File
    target_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'THREAT_MODELING_FRAMEWORKS.md')
    
    try:
        with open(target_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("Target file not found for update.")
        return

    # Split at the dynamic section marker
    marker = "## 🔄 Weekly Updates (Research & News)"
    if marker in content:
        static_content = content.split(marker)[0]
    else:
        static_content = content + "\n"

    # Build new dynamic content
    new_content = static_content + marker + "\n"
    new_content += f"*Last Updated: {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}*\n\n"
    
    new_content += "### 📄 Latest Research (Arxiv)\n"
    if not papers:
        new_content += "No new threat modeling papers found this week.\n"
    else:
        for p in papers:
            new_content += f"*   [{p['title']}]({p['url']}) ({p['published']})\n"
    
    new_content += "\n### 📰 Latest News\n"
    if not news_items:
        new_content += "No related news found this week.\n"
    else:
        for n in news_items:
            new_content += f"*   [{n['title']}]({n['url']}) ({n['published']})\n"

    with open(target_file, 'w') as f:
        f.write(new_content)
    
    print(f"Successfully updated {target_file}")

if __name__ == "__main__":
    fetch_threat_modeling_updates()
