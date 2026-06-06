import os
import sys

pd_path = "/Users/hbakesson/Coding/sofia/Accelerate.pd"

with open(pd_path, "rb") as f:
    header = f.read(10)
    print("Header:", header)

# Check what pdf libraries are available
for lib in ["pypdf", "pypdf2", "pymupdf", "fitz", "pdfplumber", "pdfminer"]:
    try:
        __import__(lib)
        print(f"Library {lib} is available")
    except ImportError:
        pass
