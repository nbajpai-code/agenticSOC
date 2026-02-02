import os
from datetime import datetime
import pytz
from youtubesearchpython import VideosSearch

def fetch_talks():
    # Keywords that suggest high-quality CISO content
    queries = [
        "CISO Enterprise Security",
        "CISO Panel Discussion Security 2024",
        "Chief Information Security Officer Strategy",
        "CISO future of cybersecurity"
    ]
    
    all_videos = []
    seen_urls = set()

    print("Fetching CISO talks from YouTube...")

    for query in queries:
        print(f"Searching for: {query}")
        try:
            videos_search = VideosSearch(query, limit=10)
            results = videos_search.result()
            
            if 'result' in results:
                for video in results['result']:
                    link = video['link']
                    if link not in seen_urls:
                        seen_urls.add(link)
                        all_videos.append({
                            'title': video['title'],
                            'link': link,
                            'channel': video['channel']['name'],
                            'published': video['publishedTime'], # Note: This is a string like "2 days ago", not a datetime
                            'duration': video['duration'],
                            'views': video['viewCount']['short']
                        })
        except Exception as e:
            print(f"Error searching for {query}: {e}")

    # Generate Markdown
    md_content = "# CISO Enterprise Security Talks\n\n"
    md_content += f"Last Updated: {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
    md_content += "A curated list of recent talks, panels, and discussions featuring CISOs on enterprise security. Automatically updated weekly.\n\n"
    
    if not all_videos:
        md_content += "No talks found.\n"
    else:
        # Simple deduplication based on URL was done above.
        # We might want to limit the total number? 
        # Let's keep top 20 for now to avoid the list getting huge if we append, 
        # but here we are overwriting (w+), so we just list what we found this run.
        # Actually, user asked to "update this list", implying it might grow or stay fresh.
        # The existing pattern replacs the file. Let's stick to that for now.
        
        md_content += "| Title | Channel | Duration | Views | Watch |\n"
        md_content += "|-------|---------|----------|-------|-------|\n"
        
        for v in all_videos:
            title = v['title'].replace('|', '-')
            channel = v['channel'].replace('|', '-')
            md_content += f"| {title} | {channel} | {v['duration']} | {v['views']} | [Link]({v['link']}) |\n"
            
    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CISO_TALKS.md')
    with open(output_file, 'w') as f:
        f.write(md_content)
    
    print(f"Successfully updated {output_file} with {len(all_videos)} talks.")

if __name__ == "__main__":
    fetch_talks()
