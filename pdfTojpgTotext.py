from pdf2image import convert_from_path
from PIL import Image 
import tempfile
import pytesseract
import os

filename = "application-pdf.pdf"

with tempfile.TemporaryDirectory() as path: 
    images_from_path = convert_from_path(filename, output_folder=path)


final = {}
i = 1

for image in images_from_path:
    text = pytesseract.image_to_string(image)
    if 'STATEMENT OF FINANCIAL POSITION' in text:
        final.update({"page":i, "content":os.linesep.join([s for s in text.splitlines() if s])})
    i = i + 1


print(final["content"])
