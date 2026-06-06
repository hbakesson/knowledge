import re

raw_path = "/Users/hbakesson/Coding/sofia/accelrate_raw.md"
output_path = "/Users/hbakesson/Coding/sofia/accelrate.md"

with open(raw_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Replace tabs with spaces
raw_text = raw_text.replace("\t", " ")

# Split into pages
pages = re.split(r"## Page \d+", raw_text)

cleaned_pages = []
for idx, page in enumerate(pages):
    lines = page.split("\n")
    # Clean spaces
    cleaned_lines = []
    for line in lines:
        cleaned_line = re.sub(r" +", " ", line).strip()
        cleaned_lines.append(cleaned_line)
        
    # Remove empty lines from boundary check
    non_empty_indices = [i for i, line in enumerate(cleaned_lines) if line]
    if not non_empty_indices:
        continue
        
    # Check first line for page number or running header
    first_idx = non_empty_indices[0]
    first_line = cleaned_lines[first_idx]
    
    # If first line is a page number, delete it
    if re.match(r"^\d+$", first_line):
        cleaned_lines[first_idx] = ""
    # If first line is a common running header
    elif first_line in ["ACCELERATE", "PART I", "PART II", "PART III"]:
        cleaned_lines[first_idx] = ""
        
    # Check last line for page number or running header
    last_idx = non_empty_indices[-1]
    last_line = cleaned_lines[last_idx]
    if re.match(r"^\d+$", last_line):
        cleaned_lines[last_idx] = ""
    elif last_line in ["ACCELERATE", "PART I", "PART II", "PART III"]:
        cleaned_lines[last_idx] = ""
        
    # Reassemble page
    cleaned_pages.append("\n".join(cleaned_lines))

# Join all cleaned pages
full_text = "\n\n".join(cleaned_pages)

# Now process the lines of the entire document
lines = full_text.split("\n")
n = len(lines)
processed_lines = []
i = 0

special_sections = [
    "FOREWORD", "PREFACE", "CONCLUSION", "APPENDIX A", "APPENDIX B", "APPENDIX C", 
    "ACKNOWLEDGMENTS", "BIBLIOGRAPHY", "INDEX", "ABOUT THE AUTHORS", "FIGURES", "TABLES",
    "QUICK REFERENCE"
]

while i < n:
    line = lines[i].strip()
    if not line:
        processed_lines.append("")
        i += 1
        continue
        
    # Match PART X
    part_match = re.match(r"^PART\s+([IVXLCDM]+)$", line, re.IGNORECASE)
    if part_match:
        part_num = part_match.group(1).upper()
        # Next non-empty line is title
        j = i + 1
        while j < n and not lines[j].strip():
            j += 1
        if j < n:
            part_title = lines[j].strip().title()
            processed_lines.append(f"\n# Part {part_num}: {part_title}\n")
            i = j + 1
            continue
            
    # Match CHAPTER X
    chap_match = re.match(r"^CHAPTER\s+(\d+)$", line, re.IGNORECASE)
    if chap_match:
        chap_num = chap_match.group(1)
        
        # Look behind for drop cap letter
        drop_cap = ""
        # Look back up to 3 non-empty lines in processed_lines to see if there's an isolated letter/word
        k = len(processed_lines) - 1
        found_drop_cap_idx = -1
        while k >= 0:
            if processed_lines[k].strip():
                prev_text = processed_lines[k].strip()
                # A drop cap is usually a single letter, or letter with quote
                if len(prev_text) <= 3 and (prev_text.isalpha() or '“' in prev_text or '"' in prev_text):
                    drop_cap = prev_text
                    found_drop_cap_idx = k
                break
            k -= 1
            
        if found_drop_cap_idx != -1:
            # Remove the drop cap line from processed_lines
            processed_lines[found_drop_cap_idx] = ""
            
        # Next non-empty line is chapter title
        j = i + 1
        while j < n and not lines[j].strip():
            j += 1
        if j < n:
            chap_title = lines[j].strip().title()
            processed_lines.append(f"\n## Chapter {chap_num}: {chap_title}\n")
            i = j + 1
            
            # Find the next non-empty body line to re-attach the drop cap
            body_idx = i
            while body_idx < n and not lines[body_idx].strip():
                body_idx += 1
            if body_idx < n and drop_cap:
                # Prepend the drop cap to this body line
                lines[body_idx] = drop_cap + lines[body_idx]
                i = body_idx
            continue
            
    # Check for other special sections
    is_special = False
    for spec in special_sections:
        if line.upper().startswith(spec):
            # Check if there is "By ..." on the next line
            header_text = line.title()
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n and lines[j].strip().upper().startswith("BY "):
                header_text += " " + lines[j].strip().title()
                i = j
            processed_lines.append(f"\n## {header_text}\n")
            is_special = True
            break
            
    if is_special:
        i += 1
        continue
        
    # Check for general sub-headings: ALL CAPS, short (<= 80 chars), not ending in sentence punctuation
    if (line.isupper() and len(line) <= 80 
            and not line.endswith(('.', ':', '?', '!')) 
            and len(line) > 3):
        processed_lines.append(f"\n### {line.title()}\n")
        i += 1
        continue
        
    processed_lines.append(lines[i])
    i += 1

# Phase 4: Join lines into paragraphs
restructured_paragraphs = []
text_combined = "\n".join(processed_lines)
# Split by empty lines to find paragraph chunks
chunks = text_combined.split("\n\n")

for chunk in chunks:
    chunk_stripped = chunk.strip()
    if not chunk_stripped:
        continue
        
    if chunk_stripped.startswith("#") or chunk_stripped.startswith("##") or chunk_stripped.startswith("###"):
        restructured_paragraphs.append(chunk_stripped)
        continue
        
    # Check if this paragraph is a list or a table
    lines_in_chunk = chunk_stripped.split("\n")
    is_list_or_table = False
    for l in lines_in_chunk:
        l_s = l.strip()
        if (l_s.startswith(("-", "*", "+", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")) 
                or "|" in l_s or l_s.startswith("[") or (":" in l_s and len(l_s) < 35)):
            is_list_or_table = True
            break
            
    if is_list_or_table:
        restructured_paragraphs.append("\n".join([l.strip() for l in lines_in_chunk if l.strip()]))
    else:
        # Re-flow normal paragraph
        # First, handle end-of-line hyphenation: e.g. "per-\nformance" -> "performance"
        joined_text = ""
        for l in lines_in_chunk:
            l_s = l.strip()
            if not l_s:
                continue
            if joined_text:
                if joined_text.endswith("-"):
                    # Check if it was a word wrap hyphen
                    joined_text = joined_text[:-1] + l_s
                else:
                    joined_text += " " + l_s
            else:
                joined_text = l_s
                
        # Double check double spaces
        joined_text = re.sub(r" +", " ", joined_text)
        restructured_paragraphs.append(joined_text)

# Write output
final_output = "\n\n".join(restructured_paragraphs)

# Let's fix specific common parsing errors
# For example, "Foreword By Martin Fowler Foreword By Courtney Kissler" being joined
final_output = final_output.replace("Foreword By Martin Fowler Foreword By Courtney Kissler", "## Foreword By Martin Fowler\n\n## Foreword By Courtney Kissler")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_output)

print("Restructured v2 complete.")
