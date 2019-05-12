import os
import tempfile

import pytesseract
from pdf2image import convert_from_path
from PIL import Image


class pdfTojpgToText:
    """
    This class ....
    """

    def __init__(self, filename, lang):
        """
        Initialize the class with:
        - filename: name of the PDF file downloaded from company house
        - lang: language used in the PDF, english is eng
        - images_from_path: all pages converted as a jpg
        - dict: dictionary return at the end of processing
        """

        self.filename = filename
        self.lang = lang
        self.images_from_path = None
        self.dict = {}

    def processpdf(self):
        """
        - Converts PDF to a serie of images
        - For each images check financial statement type and add to dictionary
        """

        self.pdfTojpg()
        self.jpgTodict()

    def pdfTojpg(self):
        """
        Converts a PDF file into a list of jpg temp files. This step os required because OCR do not
        work on PDF but rather on images.
        """

        with tempfile.TemporaryDirectory() as path:
            self.images_from_path = convert_from_path(self.filename, output_folder=path)

    def jpgTodict(self):
        """
        For each image of the page in the original PDF; it is checked for a specific financial
        statements:
        - STATEMENT OF COMPREHENSIVE INCOME

        The results are then stored in a dictionary.
        """

        # Create a counter to catch the page number
        i = 1

        for image in self.images_from_path:
            # Conver the image in its raw form
            text = pytesseract.image_to_string(image, lang=self.lang)

            # Check if the page contains the P&L
            if "STATEMENT OF COMPREHENSIVE INCOME" in text:
                raw = pytesseract.image_to_string(image, config="--psm 6 --oem 3", lang=self.lang)
                raw = (
                    raw.replace("/", "")
                    .replace(",", "")
                    .replace("(", "")
                    .replace(")", "")
                    .replace(".", "")
                    .replace(":", "")
                )
                j = 1
                for line in raw.splitlines():
                    line_ref = "line" + str(j)
                    self.dict.update({line_ref: line})
                    j = j + 1
            # Increments the counter
            i = i + 1
