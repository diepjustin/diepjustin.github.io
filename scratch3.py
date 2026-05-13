import re

with open('index.html', 'r') as f:
    lines = f.readlines()

urls = []
for i, line in enumerate(lines):
    if "⏱️" in line:
        # The URL is usually in the <h3> tag on the line below it, or the <a> tag two lines above it.
        # Let's find the nearest <a> tag before this line
        url = None
        for j in range(i, i+5):
            if "<h3><a href=" in lines[j]:
                match = re.search(r'href="([^"]+)"', lines[j])
                if match:
                    url = match.group(1)
                    title = re.search(r'>([^<]+)</a>', lines[j]).group(1)
                    print(f"Line {i}: {line.strip()}")
                    print(f"URL: {url}")
                    print(f"Title: {title}\n")
                    break

