import os
import re

root = r"d:\my-research\Cyberpradeep"
readme_path = os.path.join(root, "README.md")

with open(readme_path, "r", encoding="utf-8") as f:
    readme_text = f.read()

# Find all files referenced in README.md (any link or src)
matches = re.findall(r'assets/([a-zA-Z0-9_\-\.]+)', readme_text)
referenced_files = set(matches)

print(f"Referenced in README.md ({len(referenced_files)}):")
for rf in sorted(referenced_files):
    print("  ", rf)

assets_dir = os.path.join(root, "assets")
all_assets = set(os.listdir(assets_dir))

unused_assets = all_assets - referenced_files
print(f"\nUnused files in assets/ ({len(unused_assets)}):")
for u in sorted(unused_assets):
    print("  ", u)

root_files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
print(f"\nFiles in root ({len(root_files)}):")
for rf in sorted(root_files):
    print("  ", rf)

subdirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and d not in ('.git', 'assets')]
print(f"\nOther subdirectories in root: {subdirs}")

