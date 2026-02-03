
import feedparser
import os
import datetime
import pytz

def fetch_market_updates():
    feeds = [
        "https://techcrunch.com/category/security/feed/",
        "https://www.securityweek.com/feed/",
        "https://feeds.feedburner.com/TheHackersNews"
    ]
    
    # Keywords to identify relevant market news (Acquisitions, Funding, Startups in AI/SOC)
    market_keywords = [
        "acquisition", "acquired", "funding", "raised", "series a", "series b", "series c", 
        "startup", "investment", "merger", "buyout", "valuation"
    ]
    
    topic_keywords = [
        "agentic", "autonomous soc", "ai security", "automated security", 
        "security operations", "generative ai", "llm security", "ciso", "secops"
    ]
    
    relevant_updates = []
    
    print("Fetching market updates...")
    
    # Time window: Last 7 days
    now = datetime.datetime.now(pytz.utc)
    seven_days_ago = now - datetime.timedelta(days=7)
    
    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            print(f"Parsing {feed_url}: {len(feed.entries)} entries found.")
            
            for entry in feed.entries:
                # Parse date
                published = None
                if hasattr(entry, 'published_parsed'):
                     published = datetime.datetime(*entry.published_parsed[:6], tzinfo=pytz.utc)
                
                # If date parsing failed or entry is too old, skip
                if not published or published < seven_days_ago:
                    continue
                    
                title = entry.title.lower()
                summary = entry.summary.lower() if hasattr(entry, 'summary') else ""
                
                # Check for Market Keyword AND Topic Keyword
                is_market = any(k in title for k in market_keywords) or any(k in summary for k in market_keywords)
                is_topic = any(k in title for k in topic_keywords) or any(k in summary for k in topic_keywords)
                
                if is_market and is_topic:
                    relevant_updates.append({
                        'title': entry.title,
                        'link': entry.link,
                        'published': published.strftime('%Y-%m-%d'),
                        'source': feed.feed.title if hasattr(feed.feed, 'title') else "Unknown Source"
                    })
        except Exception as e:
            print(f"Error parsing feed {feed_url}: {e}")

    # Remove duplicates based on link
    unique_updates = {v['link']: v for v in relevant_updates}.values()
    
    if not unique_updates:
        print("No new relevant updates found.")
        return

    # Update the Report File
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'AGENTIC_SOC_MARKET_REPORT.md')
    
    new_content = f"\n\n## Weekly Updates ({datetime.datetime.now().strftime('%Y-%m-%d')})\n"
    for item in unique_updates:
        new_content += f"- **{item['published']}** [{item['title']}]({item['link']}) - *{item['source']}*\n"
        
    try:
        with open(report_path, 'a') as f:
            f.write(new_content)
        print(f"Successfully appended {len(unique_updates)} updates to {report_path}")
    except FileNotFoundError:
        print(f"Error: {report_path} not found.")

if __name__ == "__main__":
    fetch_market_updates()
