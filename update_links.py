import os
import urllib.parse

def add_links(directory):
    if not os.path.exists(directory):
        return
    files = [f for f in os.listdir(directory) if f.startswith("Chapter") and f.endswith(".md")]
    files.sort()
    
    for i in range(len(files) - 1):
        current = os.path.join(directory, files[i])
        next_file = files[i+1]
        next_name = next_file[:-3] # remove .md
        next_url = urllib.parse.quote(next_file)
        
        with open(current, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "# Next Chapter" not in content and "➡ **[Chapter" not in content:
            with open(current, 'a', encoding='utf-8') as f:
                f.write(f"\n\n---\n\n# Next Chapter\n\n➡ **[{next_name}](./{next_url})**\n")
            print(f"Added link to {current}")

add_links(r"c:\Users\Haris Laptops\Documents\personal repository\Blue-Team-Handbook\Windows\Fundamentals")
add_links(r"c:\Users\Haris Laptops\Documents\personal repository\Blue-Team-Handbook\Linux\Fundamentals")
print("Done")
