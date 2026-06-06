import re

raw_path = "/Users/hbakesson/Coding/sofia/accelrate_raw.md"

with open(raw_path, "r", encoding="utf-8") as f:
    text = f.read().replace("\t", " ")

pages = re.split(r"## Page \d+", text)
for idx, page in enumerate(pages):
    lines = [l.strip() for l in page.split("\n") if l.strip()]
    for i, line in enumerate(lines):
        if line == "CHAPTER" or re.match(r"^CHAPTER\s+\d+$", line) or line == "FOREWORD" or line == "PREFACE" or line.startswith("PART "):
            # Print surrounding lines
            start = max(0, i - 2)
            end = min(len(lines), i + 4)
            print(f"--- Page {idx+1} ---")
            for j in range(start, end):
                marker = "->" if j == i else "  "
                print(f"{marker} {lines[j]}")
