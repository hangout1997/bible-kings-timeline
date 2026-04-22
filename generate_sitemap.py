import os
from datetime import datetime
import urllib.parse

# ─── Configuration ───
BASE_URL = "https://visiodivina.uk/"
EXCLUDE_FILES = ["404.html", "google", "test"] # Files to skip
PRIORITY_MAP = {
    "index.html": "1.0",
}
DEFAULT_PRIORITY = "0.8"
CHANGEFREQ = "monthly"

def generate_sitemap():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    files.sort()
    
    # Put index.html first if exists
    if "index.html" in files:
        files.remove("index.html")
        files.insert(0, "index.html")

    now = datetime.now().strftime("%Y-%m-%d")
    
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for file in files:
        # Skip excluded files
        if any(ex in file for ex in EXCLUDE_FILES):
            continue
            
        # URL Construction
        if file == "index.html":
            url = BASE_URL
        else:
            # URL encode for Chinese characters
            encoded_file = urllib.parse.quote(file)
            url = f"{BASE_URL}{encoded_file}"
            
        priority = PRIORITY_MAP.get(file, DEFAULT_PRIORITY)
        
        xml_content.append('  <url>')
        xml_content.append(f'    <loc>{url}</loc>')
        xml_content.append(f'    <lastmod>{now}</lastmod>')
        xml_content.append(f'    <changefreq>{CHANGEFREQ}</changefreq>')
        xml_content.append(f'    <priority>{priority}</priority>')
        xml_content.append('  </url>')

    xml_content.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_content))
    
    print(f"Successfully generated sitemap.xml with {len(files)} links.")

if __name__ == "__main__":
    generate_sitemap()
