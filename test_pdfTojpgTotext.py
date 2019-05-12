import unittest

from pdfTojpgTotext import pdfTojpgToText


class TestPDFConversion(unittest.TestCase):
    def test_processpdf(self):
        """
        Test that the function processpdf is able to convert the pdf test to a jpg format and then
        retrieve a dictionary with the results.
        """

        t = pdfTojpgToText(filename="application-pdf.pdf", lang="eng")
        t.processpdf()
        self.assertEqual(t.dict["line1"], "DUEDIL LIMITED")
