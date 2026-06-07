import pypdf

reader = pypdf.PdfReader("Engineering at Google.pdf")
outline = reader.outline

def print_outline(outline_list, indent=0):
    for item in outline_list:
        if isinstance(item, list):
            print_outline(item, indent + 2)
        else:
            title = item.get('/Title', 'Untitled')
            # Resolve page number
            page_num = "Unknown"
            try:
                page_num = reader.get_destination_page_number(item)
            except Exception:
                pass
            print(f"{' ' * indent}- {title} (Page {page_num})")

if outline:
    print("=== DOCUMENT OUTLINE ===")
    print_outline(outline)
else:
    print("No outline found in PDF.")
