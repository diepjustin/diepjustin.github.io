import re
import urllib.parse

with open('index.html', 'r') as f:
    content = f.read()

def replace_photo_src(match):
    original_path = match.group(1)
    
    # Check if the path already contains JPEG, if so, just fix extension
    if "JPEG/" in original_path:
        filename = original_path.split("JPEG/")[-1]
    else:
        filename = original_path
        
    # Remove old extension (which could be .webp, .jpeg, .JPG, .jpg)
    filename_no_ext = re.sub(r'\.(webp|jpeg|jpg|JPG)$', '', filename, flags=re.IGNORECASE)
    
    # New path
    new_path = f"photos/JPEG/{filename_no_ext}.jpg"
    return f'src="{new_path}"'

# Find all src="photos/..." 
content = re.sub(r'src="photos/([^"]+)"', replace_photo_src, content)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated image paths.")
