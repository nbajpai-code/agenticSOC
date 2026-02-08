import feedparser
import os
import datetime
import pytz

def fetch_industry_updates():
    """
    Fetches latest blog posts from Gravitee.io, Wiz, and Palo Alto Networks (Unit 42)
    and appends relevant AI Agent Security news to industry.md.
    """
    feeds = {
        "Gravitee.io Blog": "https://www.gravitee.io/blog/rss.xml",
        "Wiz Blog": "https://www.wiz.io/blog/rss",
        "Palo Alto Networks Unit 42": "https://unit42.paloaltonetworks.com/feed/"
    }

    # Keywords to filter for "AI Agent Security" relevant content
    keywords = [
        "agent", "agentic", "autonomous", "ai security", "llm security", 
        "generative ai", "genai", "artificial intelligence", "copilot"
    ]

    new_updates = []
    
    print("Fetching industry updates...")
    
    # Time window: Last 30 days (since we run this monthly)
    now = datetime.datetime.now(pytz.utc)
    thirty_days_ago = now - datetime.timedelta(days=30)
    
    for source_name, feed_url in feeds.items():
        try:
            print(f"Parsing {source_name}...")
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries:
                # Parse date
                published = None
                if hasattr(entry, 'published_parsed'):
                     published = datetime.datetime(*entry.published_parsed[:6], tzinfo=pytz.utc)
                elif hasattr(entry, 'updated_parsed'):
                     published = datetime.datetime(*entry.updated_parsed[:6], tzinfo=pytz.utc)
                
                # If date parsing failed or entry is too old, skip
                if not published or published < thirty_days_ago:
                    continue
                    
                title = entry.title.lower()
                summary = entry.summary.lower() if hasattr(entry, 'summary') else ""
                
                # Check for Keywords
                is_relevant = any(k in title for k in keywords) or any(k in summary for k in keywords)
                
                if is_relevant:
                    new_updates.append({
                        'title': entry.title,
                        'link': entry.link,
                        'published': published.strftime('%Y-%m-%d'),
                        'source': source_name
                    })
        except Exception as e:
            print(f"Error parsing feed {source_name}: {e}")

    # Remove duplicates based on link
    unique_updates = {v['link']: v for v in new_updates}.values()
    
    if not unique_updates:
        print("No new relevant updates found.")
        return

    # Update the Industry File
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'industry.md')
    
    # Check if "## Latest Industry Updates" exists, if not add it
    try:
        with open(report_path, 'r') as f:
            content = f.read()
            
        header = "\n## Latest Industry Updates\n"
        if header not in content:
            with open(report_path, 'a') as f:
                f.write(header)
                
        # Append new items
        new_content = ""
        for item in unique_updates:
            # Check if link already exists in file to avoid duplicates on re-runs
            if item['link'] not in content:
                 new_content += f"- **{item['published']}** [{item['title']}]({item['link']}) - *{item['source']}*\n"
        
        if new_content:
            with open(report_path, 'a') as f:
                f.write(new_content)
            print(f"Successfully appended {len(new_content.strip().split(chr(10)))} updates to {report_path}")
        else:
            print("Updates found but they are already in the file.")
            
    except FileNotFoundError:
        print(f"Error: {report_path} not found.")

if __name__ == "__main__":
    fetch_industry_updates()
