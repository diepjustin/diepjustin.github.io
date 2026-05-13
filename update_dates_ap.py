import re

with open('index.html', 'r') as f:
    html = f.read()

replacements = {
    'Jun 21, 2025': 'June 21, 2025',
    'Oct 31, 2025': 'Oct. 31, 2025',
    'Aug 11, 2025': 'Aug. 11, 2025',
    'Dec 16, 2025': 'Dec. 16, 2025',
    'Apr 18, 2026': 'April 18, 2026',
    'Feb 11, 2026': 'Feb. 11, 2026',
    'May 08, 2025': 'May 8, 2025',
    'Sep 07, 2024': 'Sept. 7, 2024',
    'Nov 30, 2024': 'Nov. 30, 2024',
    'Jan 07, 2025': 'Jan. 7, 2025'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print("Successfully replaced with AP style.")
