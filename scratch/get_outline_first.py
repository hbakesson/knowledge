import pypdf

reader = pypdf.PdfReader("Engineering at Google.pdf")
outline = reader.outline

flat_outline = []

def flatten_outline(outline_list, level=0):
    for item in outline_list:
        if isinstance(item, list):
            flatten_outline(item, level + 1)
        else:
            title = item.get('/Title', 'Untitled')
            page_num = "Unknown"
            try:
                page_num = reader.get_destination_page_number(item)
            except Exception:
                pass
            flat_outline.append((level, title, page_num))

flatten_outline(outline)

print("=== TOTAL OUTLINE ITEMS:", len(flat_outline))
print("=== FIRST 100 ITEMS ===")
for i in range(min(100, len(flat_outline))):
    level, title, page_num = flat_outline[i]
    print(f"{'  ' * level}- {title} (Page {page_num})")
