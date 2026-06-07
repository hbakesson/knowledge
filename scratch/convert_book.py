import pypdf
import os
import re

print("Initializing PDF reader...")
reader = pypdf.PdfReader("Engineering at Google.pdf")
total_pages = len(reader.pages)
print(f"Loaded PDF with {total_pages} pages.")

outline = reader.outline

# Flatten outline to map page numbers to titles and levels
flat_outline = {}
def flatten_outline(outline_list, level=0):
    for item in outline_list:
        if isinstance(item, list):
            flatten_outline(item, level + 1)
        else:
            title = item.get('/Title', 'Untitled').strip()
            try:
                page_num = reader.get_destination_page_number(item)
                if page_num not in flat_outline:
                    flat_outline[page_num] = []
                flat_outline[page_num].append((level, title))
            except Exception:
                pass

flatten_outline(outline)

print(f"Mapped outlines for {len(flat_outline)} pages.")

# Generate Table of Contents in Markdown
toc_lines = ["# Software Engineering at Google", "", "## Table of Contents", ""]
temp_list = []
def build_toc(outline_list, indent=0):
    for item in outline_list:
        if isinstance(item, list):
            build_toc(item, indent + 2)
        else:
            title = item.get('/Title', 'Untitled').strip()
            try:
                page_num = reader.get_destination_page_number(item)
                # Create a markdown link anchor
                anchor = title.lower().replace(" ", "-").replace("?", "").replace(":", "").replace(",", "").replace(".", "").replace("’", "").replace("“", "").replace("”", "")
                toc_lines.append(f"{'  ' * indent}- [{title}](#{anchor}) (Page {page_num})")
            except Exception:
                toc_lines.append(f"{'  ' * indent}- {title}")

build_toc(outline)
toc_lines.append("")
toc_lines.append("---")
toc_lines.append("")

# Write TOC and content page-by-page
output_path = "engineering_at_google.md"
print(f"Writing output to {output_path}...")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(toc_lines))
    
    for i in range(total_pages):
        page = reader.pages[i]
        text = page.extract_text()
        if not text or not text.strip():
            continue
            
        # Check if page matches outline elements
        if i in flat_outline:
            for level, title in flat_outline[i]:
                # Chapters are usually level 0 or 1 depending on outline structure
                # We map level to markdown headings
                heading_marker = "#" * (level + 2)
                f.write(f"\n\n{heading_marker} {title}\n\n")
        
        # Clean text: remove page number footers (e.g. single numbers at the end of the text)
        lines = text.split("\n")
        cleaned_lines = []
        for line in lines:
            line_str = line.strip()
            # Skip page runner numbers and running headers
            if re.match(r"^\d+$", line_str):
                continue
            if line_str.startswith("Chapter ") and len(line_str) < 50:
                continue
            if line_str.startswith("Part ") and len(line_str) < 30:
                continue
            cleaned_lines.append(line)
            
        f.write("\n".join(cleaned_lines) + "\n")
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{total_pages} pages...")

print("Conversion complete!")
