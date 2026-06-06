import re

md_path = "/Users/hbakesson/Coding/sofia/accelrate.md"

with open(md_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    # Replace tabs with spaces
    line_clean = line.replace('\t', ' ')
    # Replace multiple spaces with a single space
    line_clean = re.sub(r' +', ' ', line_clean)
    # Strip leading/trailing spaces but keep newline character
    line_clean = line_clean.strip()
    cleaned_lines.append(line_clean)

# Combine and clean up multiple empty lines
text = "\n".join(cleaned_lines)
text = re.sub(r'\n{3,}', '\n\n', text)

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaned markdown file successfully.")
