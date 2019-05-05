# financialsapi
Retrieves financials of UK companies through API


A simple guide to extract images (jpeg, png) from PDF.

Objectives:
Extract Images from PDF
Required Tools:
Poppler for windows— Poppler is a PDF rendering library . Include the pdftoppm utility
Poppler for Mac — If HomeBrew already installed, can use brew install Poppler
Pdf2image— Python module. Wraps the pdftoppm utility to convert PDF to a PIL Image object.
Steps:
Install Poppler. For windows, Add “xxx/bin/” to env path
pip install pdf2image


https://pypi.org/project/pytesseract/

Prerequisites:

Python-tesseract requires python 2.6+ or python 3.x
You will need the Python Imaging Library (PIL) (or the Pillow fork). Under Debian/Ubuntu, this is the package python-imaging or python3-imaging.
Install Google Tesseract OCR (additional info how to install the engine on Linux, Mac OSX and Windows). You must be able to invoke the tesseract command as tesseract. If this isn’t the case, for example because tesseract isn’t in your PATH, you will have to change the “tesseract_cmd” variable pytesseract.pytesseract.tesseract_cmd. Under Debian/Ubuntu you can use the package tesseract-ocr. For Mac OS users. please install homebrew package tesseract.
Installing via pip:

```
shell
(env)> pip install pytesseract
```
