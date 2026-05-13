import urllib.request
import re
from datetime import datetime

urls = [
    "https://omaha.com/news/local/crime-courts/article_48d546aa-e476-4fa0-a305-ea19a038f674.html",
    "https://www.dailynebraskan.com/news/unl-used-bad-data-to-make-27-5-million-cuts-faculty-say/article_8ad30fe6-4f53-4b7a-9071-5e222854fe6e.html",
    "https://omaha.com/news/local/article_10f919e4-8d35-4b71-8b67-d9ed748ab0b8.html",
    "https://www.nebraskanewsservice.net/news/south-omaha-to-mccook-a-freshman-senators-fight-for-nebraska-s-immigrant-community/article_6c1eb962-03b7-4493-9fc5-1aac3ec96437.html",
    "https://omaha.com/news/state-regional/article_635efd64-6da7-494e-afa9-e354371f81da.html",
    "https://www.dailynebraskan.com/news/jeffrey-epstein-calls-university-of-nebraska-creighton-not-good-places/article_961382a0-105f-40bd-b7fe-9100d4f66f42.html",
    "https://journalstar.com/life-entertainment/local/faith-values/article_150c4da3-aa45-43af-81c2-d069619046a9.html",
    "https://journalstar.com/sports/huskers/football/article_4e6f519e-6d53-11ef-a496-97e20091e293.html",
    "https://journalstar.com/news/local/article_13ff1f98-af58-11ef-86fd-3bb64b0de42d.html",
    "https://journalstar.com/news/local/article_5860d84e-caaf-11ef-9a33-1be0894ecc5b.html"
]

dates = []
for i, url in enumerate(urls):
    req = urllib.request.Request(
        url, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
        }
    )
    try:
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read().decode('utf-8', errors='ignore')
        
        # Try a few different date meta tags
        match = re.search(r'<meta[^>]*property="article:published_time"[^>]*content="([^"]+)"', html)
        if not match:
            match = re.search(r'<time[^>]*datetime="([^"]+)"', html)
        if not match:
            match = re.search(r'"datePublished"\s*:\s*"([^"]+)"', html)
            
        if match:
            date_str = match.group(1).split('T')[0]
            # Parse and format
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            formatted = dt.strftime("%b %d, %Y")
            dates.append(formatted)
        else:
            dates.append("Unknown Date")
    except Exception as e:
        dates.append("Error")

print(dates)
