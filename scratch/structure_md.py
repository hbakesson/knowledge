import re

input_path = "/Users/hbakesson/Coding/sofia/accelrate.md"
output_path = "/Users/hbakesson/Coding/sofia/accelrate.md"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# Split into lines
lines = text.split("\n")

# Phase 1: Identify page indicators, headers/footers, and clean them
cleaned_lines = []
i = 0
n = len(lines)

while i < n:
    line = lines[i].strip()
    
    # Skip empty lines
    if not line:
        cleaned_lines.append("")
        i += 1
        continue
        
    # Check for page markers
    if re.match(r"^## Page \d+$", line):
        # Page marker, skip it
        i += 1
        continue
        
    # Check for isolated page numbers (e.g. just a number)
    if re.match(r"^\d+$", line):
        # Skip isolated numbers
        i += 1
        continue
        
    # Check for running header "ACCELERATE" in caps near page boundary
    # Or just general repetitive headers
    if line == "ACCELERATE":
        i += 1
        continue
        
    cleaned_lines.append(lines[i])
    i += 1

# Phase 2: Detect parts, chapters, and drop-caps
processed_lines = []
i = 0
n = len(cleaned_lines)

# A list to store restructured lines
output_lines = []

while i < n:
    line = cleaned_lines[i]
    line_stripped = line.strip()
    
    if not line_stripped:
        output_lines.append("")
        i += 1
        continue
        
    # Match Chapter headings: e.g. "CHAPTER 1"
    chapter_match = re.match(r"^CHAPTER\s+(\d+)$", line_stripped, re.IGNORECASE)
    part_match = re.match(r"^PART\s+([IVXLCDM]+):?\s*(.*)$", line_stripped, re.IGNORECASE)
    
    if part_match:
        part_num = part_match.group(1)
        part_title = part_match.group(2).strip()
        # Look ahead for title if not on the same line
        if not part_title and i + 1 < n:
            i += 1
            part_title = cleaned_lines[i].strip()
        output_lines.append(f"\n# Part {part_num}: {part_title}\n")
        i += 1
        continue
        
    if chapter_match:
        chap_num = chapter_match.group(1)
        
        # Check if previous line was a drop cap (1-2 chars, e.g. "B" or "“B" or "T")
        drop_cap = ""
        if len(output_lines) > 0:
            # find last non-empty line in output_lines
            last_idx = len(output_lines) - 1
            while last_idx >= 0 and not output_lines[last_idx].strip():
                last_idx -= 1
            if last_idx >= 0:
                prev_val = output_lines[last_idx].strip()
                if len(prev_val) <= 3 and prev_val.isalpha() or (len(prev_val) <= 4 and ('“' in prev_val or '"' in prev_val)):
                    drop_cap = prev_val
                    # remove it from output_lines
                    output_lines[last_idx] = ""
                    
        # Look ahead for chapter title (usually the next non-empty line)
        chap_title = ""
        j = i + 1
        while j < n and not cleaned_lines[j].strip():
            j += 1
        if j < n:
            chap_title = cleaned_lines[j].strip()
            i = j
            
        output_lines.append(f"\n## Chapter {chap_num}: {chap_title}\n")
        
        # Now find the first line of body text and apply the drop cap
        j = i + 1
        while j < n and not cleaned_lines[j].strip():
            j += 1
        if j < n and drop_cap:
            next_line = cleaned_lines[j]
            # Prepended drop cap
            cleaned_lines[j] = drop_cap + next_line
            
        i += 1
        continue
        
    output_lines.append(line)
    i += 1

# Phase 3: Format section headings (ALL CAPS lines) and merge paragraph lines
# We want to treat lines that are ALL CAPS, relatively short, and don't end in punctuation as section headings.
final_lines = []
i = 0
n = len(output_lines)

while i < n:
    line = output_lines[i]
    line_stripped = line.strip()
    
    if not line_stripped:
        final_lines.append("")
        i += 1
        continue
        
    # Check for other specific sections like Forewords, Preface, Conclusion, Appendix, etc.
    special_headers = [
        "FOREWORD", "PREFACE", "CONCLUSION", "APPENDIX A", "APPENDIX B", "APPENDIX C", 
        "ACKNOWLEDGMENTS", "BIBLIOGRAPHY", "INDEX", "ABOUT THE AUTHORS", "FIGURES", "TABLES",
        "QUICK REFERENCE:"
    ]
    is_special = False
    for sh in special_headers:
        if line_stripped.upper().startswith(sh):
            is_special = True
            break
            
    if is_special:
        # Check if the title is split or complete
        title = line_stripped
        if i + 1 < n and output_lines[i+1].strip() and not output_lines[i+1].strip().endswith('.') and len(output_lines[i+1].strip()) < 50:
            # Maybe it is "Foreword\nBy Martin Fowler"
            title += " " + output_lines[i+1].strip()
            i += 1
        final_lines.append(f"\n## {title}\n")
        i += 1
        continue
        
    # Check for general sub-headings: ALL CAPS, short (<= 80 chars), not ending in punctuation
    if (line_stripped.isupper() and len(line_stripped) <= 80 
            and not line_stripped.endswith(('.', ':', '?', '!')) 
            and len(line_stripped) > 3):
        # Could be a section header
        final_lines.append(f"\n### {line_stripped}\n")
        i += 1
        continue
        
    final_lines.append(line)
    i += 1

# Phase 4: Join broken lines to reform paragraphs.
# We will join lines that look like they flow into the next line.
text_processed = "\n".join(final_lines)
paragraphs = text_processed.split("\n\n")
restructured_paragraphs = []

for para in paragraphs:
    para_stripped = para.strip()
    if not para_stripped:
        continue
        
    # If it is a header, keep it as is
    if para_stripped.startswith("#") or para_stripped.startswith("##") or para_stripped.startswith("###"):
        restructured_paragraphs.append(para_stripped)
        continue
        
    # If it looks like a list or table, keep lines separate but strip them
    lines_in_para = para_stripped.split("\n")
    is_list_or_table = False
    for l in lines_in_para:
        l_s = l.strip()
        if (l_s.startswith(("-", "*", "+", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")) 
                or "|" in l_s or l_s.startswith("[") or ":" in l_s and len(l_s) < 30):
            is_list_or_table = True
            break
            
    if is_list_or_table:
        restructured_paragraphs.append(para_stripped)
    else:
        # Join lines into a single paragraph text block
        joined_text = " ".join([l.strip() for l in lines_in_para if l.strip()])
        # Normalize spaces
        joined_text = re.sub(r' +', ' ', joined_text)
        restructured_paragraphs.append(joined_text)

# Write to file
final_text = "\n\n".join(restructured_paragraphs)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_text)

print("Markdown file restructured and formatted successfully!")
