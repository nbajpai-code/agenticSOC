import arxiv
import os
from datetime import datetime
import pytz

def fetch_papers():
    # Construct the query
    # "agenticSOC" OR "agentic ai cybersecurity"
    # arXiv API search query syntax: cat:cs.CR AND (all:"agenticSOC" OR all:"agentic ai cybersecurity")
    # however, simple keyword search is often broader and better for this specific request if volume is low.
    # Let's try likely keywords.
    
    query = 'all:"agenticSOC" OR all:"agentic ai cybersecurity" OR all:"agentic cybersecurity"'
    
    # We want recent papers, but "all" is requested. Let's get max 100 results for now.
    search = arxiv.Search(
        query=query,
        max_results=100,
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
                'pdf_url': result.pdf_url,
                'published': result.published,
                'summary': result.summary.replace('\n', ' '),
                'authors': [a.name for a in result.authors]
            })
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return

    # Generate Markdown
    md_content = "# Agentic AI & SOC Research Papers\n\n"
    md_content += f"Last Updated: {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
    md_content += "This list is automatically updated weekly.\n\n"
    
    if not papers:
        md_content += "No papers found matching the criteria yet.\n"
    else:
        md_content += "| Date | Title | Authors | PDF |\n"
        md_content += "|------|-------|---------|-----|\n"
        for p in papers:
            date_str = p['published'].strftime('%Y-%m-%d')
            authors_str = ", ".join(p['authors'])
            if len(authors_str) > 50:
                authors_str = authors_str[:47] + "..."
            title = p['title'].replace('|', '-')
            md_content += f"| {date_str} | [{title}]({p['url']}) | {authors_str} | [PDF]({p['pdf_url']}) |\n"
            
    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'RESEARCH_PAPERS.md')
    with open(output_file, 'w') as f:
        f.write(md_content)
    
    print(f"Successfully updated {output_file} with {len(papers)} papers.")

if __name__ == "__main__":
    fetch_papers()
