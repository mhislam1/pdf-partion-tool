import pymupdf
from pathlib import Path


pdf_path = Path(
    "data/input/pymuPDF-test.pdf"
)

doc = pymupdf.open(pdf_path) # open a documentimport pymupdf

