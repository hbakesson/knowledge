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

chapter_titles = {
    "1": "Accelerate",
    "2": "Measuring Performance",
    "3": "Measuring and Changing Culture",
    "4": "Technical Practices",
    "5": "Architecture",
    "6": "Integrating Infosec into the Delivery Lifecycle",
    "7": "Management Practices for Software",
    "8": "Product Development",
    "9": "Making Work Sustainable",
    "10": "Employee Satisfaction, Identity, and Engagement",
    "11": "Leaders and Managers",
    "12": "The Science Behind This Book",
    "13": "Introduction to Psychometrics",
    "14": "Why Use a Survey",
    "15": "The Data for the Project",
    "16": "High-Performance Leadership and Management"
}

part_titles = {
    "I": "What We Found",
    "II": "The Research",
    "III": "Transformation"
}

# We'll collect processed lines here
processed_lines = []

for page_idx, page in enumerate(pages):
    lines = page.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_line = re.sub(r" +", " ", line).strip()
        cleaned_lines.append(cleaned_line)
        
    non_empty_indices = [i for i, line in enumerate(cleaned_lines) if line]
    if not non_empty_indices:
        continue
        
    # Remove first line if it's a page number or ACCELERATE header
    first_idx = non_empty_indices[0]
    first_line = cleaned_lines[first_idx]
    if re.match(r"^\d+$", first_line) or first_line == "ACCELERATE":
        cleaned_lines[first_idx] = ""
        
    # Remove last line if it's a page number or ACCELERATE header
    last_idx = non_empty_indices[-1]
    last_line = cleaned_lines[last_idx]
    if re.match(r"^\d+$", last_line) or last_line == "ACCELERATE":
        cleaned_lines[last_idx] = ""
        
    # Rebuild page text
    page_text = "\n".join(cleaned_lines)
    
    # Page index < 13 is the front matter, TOC, figures, tables list (Pages 1 to 13)
    if page_idx < 13:
        processed_lines.append(page_text)
    else:
        # Process lines of this page for headers/chapters/parts
        page_lines = page_text.split("\n")
        n = len(page_lines)
        i = 0
        page_processed = []
        
        def find_drop_cap(page_proc_list):
            drop_cap = ""
            k = len(page_proc_list) - 1
            found_idx = -1
            while k >= 0:
                if page_proc_list[k].strip():
                    prev_text = page_proc_list[k].strip()
                    if len(prev_text) <= 3 and (prev_text.isalpha() or '“' in prev_text or '"' in prev_text):
                        drop_cap = prev_text
                        found_idx = k
                    break
                k -= 1
            if found_idx != -1:
                page_proc_list[found_idx] = ""
            return drop_cap
            
        def join_drop_cap(drop_cap, body_text):
            if not drop_cap:
                return body_text
            if drop_cap == "A" and body_text.startswith("few"):
                return "A " + body_text
            return drop_cap + body_text
            
        while i < n:
            line = page_lines[i].strip()
            if not line:
                page_processed.append("")
                i += 1
                continue
                
            # Match Part X: e.g. "PART I" (exactly)
            part_match = re.match(r"^PART\s+([IVXLCDM]+)$", line, re.IGNORECASE)
            if part_match:
                part_num = part_match.group(1).upper()
                if part_num in part_titles:
                    title = part_titles[part_num]
                    j = i + 1
                    while j < n and (not page_lines[j].strip() or page_lines[j].strip().upper() == title.upper()):
                        j += 1
                    page_processed.append(f"\n# Part {part_num}: {title}\n")
                    i = j
                    continue
                    
            # Match CHAPTER X: e.g. "CHAPTER 1" (exactly)
            chap_match = re.match(r"^CHAPTER\s+(\d+)$", line, re.IGNORECASE)
            if chap_match:
                chap_num = chap_match.group(1)
                if chap_num in chapter_titles:
                    title = chapter_titles[chap_num]
                    
                    drop_cap = find_drop_cap(page_processed)
                        
                    j = i + 1
                    while j < n and (not page_lines[j].strip() or page_lines[j].strip().upper() == title.upper()):
                        j += 1
                        
                    page_processed.append(f"\n## Chapter {chap_num}: {title}\n")
                    i = j
                    
                    # Find first body line to attach drop cap
                    body_idx = i
                    while body_idx < n and not page_lines[body_idx].strip():
                        body_idx += 1
                    if body_idx < n and drop_cap:
                        page_lines[body_idx] = join_drop_cap(drop_cap, page_lines[body_idx])
                        i = body_idx
                    continue

            # Match Foreword
            if line.upper() == "FOREWORD":
                drop_cap = find_drop_cap(page_processed)
                j = i + 1
                while j < n and not page_lines[j].strip():
                    j += 1
                if j < n and page_lines[j].strip().upper().startswith("BY "):
                    author = page_lines[j].strip()[3:].title()
                    page_processed.append(f"\n## Foreword By {author}\n")
                    i = j + 1
                else:
                    page_processed.append(f"\n## Foreword\n")
                    i = j
                
                # Find first body line to attach drop cap
                body_idx = i
                while body_idx < n and not page_lines[body_idx].strip():
                    body_idx += 1
                if body_idx < n and drop_cap:
                    page_lines[body_idx] = join_drop_cap(drop_cap, page_lines[body_idx])
                    i = body_idx
                continue

            # Match Preface
            if line.upper() == "PREFACE":
                drop_cap = find_drop_cap(page_processed)
                page_processed.append(f"\n## Preface\n")
                i += 1
                
                body_idx = i
                while body_idx < n and not page_lines[body_idx].strip():
                    body_idx += 1
                if body_idx < n and drop_cap:
                    page_lines[body_idx] = join_drop_cap(drop_cap, page_lines[body_idx])
                    i = body_idx
                continue

            # Match Conclusion
            if line.upper() == "CONCLUSION":
                drop_cap = find_drop_cap(page_processed)
                page_processed.append(f"\n## Conclusion\n")
                i += 1
                
                body_idx = i
                while body_idx < n and not page_lines[body_idx].strip():
                    body_idx += 1
                if body_idx < n and drop_cap:
                    page_lines[body_idx] = join_drop_cap(drop_cap, page_lines[body_idx])
                    i = body_idx
                continue

            # Match Quick Reference: Capabilities To Drive Improvement
            if line.upper().startswith("QUICK REFERENCE"):
                drop_cap = find_drop_cap(page_processed)
                page_processed.append(f"\n## Quick Reference: Capabilities to Drive Improvement\n")
                # Skip title lines
                j = i + 1
                while j < n and (not page_lines[j].strip() or page_lines[j].strip().upper().startswith("CAPABILITIES") or page_lines[j].strip().upper().startswith("IMPROVEMENT")):
                    j += 1
                i = j
                
                body_idx = i
                while body_idx < n and not page_lines[body_idx].strip():
                    body_idx += 1
                if body_idx < n and drop_cap:
                    page_lines[body_idx] = join_drop_cap(drop_cap, page_lines[body_idx])
                    i = body_idx
                continue

            # Match Appendix A, B, C
            if line.upper() == "APPENDIX A":
                page_processed.append(f"\n## Appendix A: Capabilities to Drive Improvement\n")
                i += 1
                j = i
                while j < n and (not page_lines[j].strip() or page_lines[j].strip().upper().startswith("CAPABILITIES")):
                    j += 1
                i = j
                continue
            if line.upper() == "APPENDIX B":
                page_processed.append(f"\n## Appendix B: The Stats\n")
                i += 1
                j = i
                while j < n and (not page_lines[j].strip() or page_lines[j].strip().upper().startswith("THE STATS")):
                    j += 1
                i = j
                continue
            if line.upper() == "APPENDIX C":
                page_processed.append(f"\n## Appendix C: Statistical Methods Used in Our Research\n")
                i += 1
                j = i
                while j < n and (not page_lines[j].strip() or page_lines[j].strip().upper().startswith("STATISTICAL METHODS")):
                    j += 1
                i = j
                continue

            # Match other special sections
            if line.upper() in ["ACKNOWLEDGMENTS", "BIBLIOGRAPHY", "INDEX", "ABOUT THE AUTHORS", "FIGURES", "TABLES"]:
                page_processed.append(f"\n## {line.title()}\n")
                i += 1
                continue

            # Check for general sub-headings: ALL CAPS, short (<= 80 chars), not ending in sentence punctuation
            if (line.isupper() and len(line) <= 80 
                    and not line.endswith(('.', ':', '?', '!')) 
                    and len(line) > 3):
                if not any(line.upper().startswith(x) for x in ["CHAPTER", "PART", "APPENDIX"]):
                    page_processed.append(f"\n### {line.title()}\n")
                    i += 1
                    continue
                    
            page_processed.append(page_lines[i])
            i += 1
            
        processed_lines.append("\n".join(page_processed))

# Join all processed pages
full_text = "\n\n".join(processed_lines)

# Phase 4: Join lines into paragraphs
restructured_paragraphs = []
chunks = full_text.split("\n\n")

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
                or "|" in l_s or l_s.startswith("[") or (looks_like_col := (":" in l_s and len(l_s) < 35))):
            is_list_or_table = True
            break
            
    if is_list_or_table:
        restructured_paragraphs.append("\n".join([l.strip() for l in lines_in_chunk if l.strip()]))
    else:
        # Re-flow normal paragraph
        joined_text = ""
        for l in lines_in_chunk:
            l_s = l.strip()
            if not l_s:
                continue
            if joined_text:
                if joined_text.endswith("-"):
                    joined_text = joined_text[:-1] + l_s
                else:
                    joined_text += " " + l_s
            else:
                joined_text = l_s
                
        joined_text = re.sub(r" +", " ", joined_text)
        restructured_paragraphs.append(joined_text)

# Write output
final_output = "\n\n".join(restructured_paragraphs)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_output)

print("Restructured v7 complete.")
