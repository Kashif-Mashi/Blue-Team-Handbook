import os
import urllib.parse
import re

def add_solution_links(base_dir, solution_dir_name):
    labs_dir = base_dir
    solution_dir = os.path.join(base_dir, solution_dir_name)
    
    if not os.path.exists(labs_dir) or not os.path.exists(solution_dir):
        print(f"Directory missing: {labs_dir} or {solution_dir}")
        return
        
    solution_files = [f for f in os.listdir(solution_dir) if f.endswith(".md")]
    
    for item in os.listdir(labs_dir):
        lab_path = os.path.join(labs_dir, item)
        if os.path.isdir(lab_path) and item.startswith("Lab "):
            match = re.search(r"Lab (\d+)", item)
            if match:
                lab_num = match.group(1)
                readme_path = os.path.join(lab_path, "README.md")
                
                if os.path.exists(readme_path):
                    # Find corresponding solution
                    sol_file = next((f for f in solution_files if f.startswith(f"Lab {lab_num}")), None)
                    if sol_file:
                        url_encoded_sol = urllib.parse.quote(sol_file)
                        rel_path = f"../{solution_dir_name}/{url_encoded_sol}"
                        
                        with open(readme_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            
                        if "# Solution" not in content and "➡ **[View Solution" not in content:
                            with open(readme_path, 'a', encoding='utf-8') as f:
                                f.write(f"\n\n---\n\n# Solution\n\n➡ **[View Solution]({rel_path})**\n")
                            print(f"Added solution link to {readme_path}")
                    else:
                        print(f"No solution file found for Lab {lab_num} in {solution_dir}")

print("Processing Windows Labs...")
add_solution_links(r"c:\Users\Haris Laptops\Documents\personal repository\Blue-Team-Handbook\Windows\Labs", "Solution")

print("\nProcessing Linux Labs...")
add_solution_links(r"c:\Users\Haris Laptops\Documents\personal repository\Blue-Team-Handbook\Linux\Labs", "Solutions")

print("\nDone")
