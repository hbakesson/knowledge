import pypdf

reader = pypdf.PdfReader("Engineering at Google.pdf")

for i in range(1, 16):
    txt = reader.pages[i].extract_text()
    if txt and txt.strip():
        print(f"=== PAGE {i} ===")
        print(txt)
        print("-" * 50)
