import pypdf

pd_path = "/Users/hbakesson/Coding/sofia/Accelerate.pd"
md_path = "/Users/hbakesson/Coding/sofia/accelrate_raw.md"

reader = pypdf.PdfReader(pd_path)
print("Number of pages:", len(reader.pages))

text_by_page = []
for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        text_by_page.append(f"## Page {idx+1}\n\n{text}\n")
    else:
        text_by_page.append(f"## Page {idx+1}\n\n[Empty Page]\n")

full_content = "\n".join(text_by_page)

with open(md_path, "w", encoding="utf-8") as f:
    f.write(full_content)

print("Saved raw markdown to:", md_path)
