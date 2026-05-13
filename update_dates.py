import re

with open('index.html', 'r') as f:
    html = f.read()

dates = [
    'Jun 21, 2025', 'Oct 31, 2025', 'Aug 11, 2025', 'Dec 16, 2025', 
    'Apr 18, 2026', 'Feb 11, 2026', 'May 08, 2025', 'Sep 07, 2024', 
    'Nov 30, 2024', 'Jan 07, 2025'
]

# Find all occurrences of ⏱️ X min read
matches = list(re.finditer(r'⏱️ \d+ min read', html))

if len(matches) == len(dates):
    # Replace in reverse order so indices don't shift
    for match, date in zip(reversed(matches), reversed(dates)):
        start, end = match.span()
        html = html[:start] + date + html[end:]
        
    with open('index.html', 'w') as f:
        f.write(html)
    print("Successfully replaced all dates.")
else:
    print(f"Error: Found {len(matches)} matches but have {len(dates)} dates.")
