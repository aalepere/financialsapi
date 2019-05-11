# UK Financials API
## Purpose of the project
The purpose of this project is to be able to offer financials information via an API.

## Background
Most of the companies in the UK have to publish their financials statements on yearly basis on the company house website. However, those financial statement are available as scanned PDF document.

## Process
As mention above, the finanicals statements are available in scanned PDF fornat; therefore the first step of this project is to OCR those documents to be able to extract both the balance sheet and the P&L. Once this information correctly parse, it will be stored in the database and made externally available through a REST API.

## Stack
In order to complete that project; Company House API, Tesseract, Django & Rest framework will be used:
- Company House API: https://developer.companieshouse.gov.uk/api/docs/
- Tesseract: https://github.com/tesseract-ocr/tesseract
- Django: https://www.djangoproject.com/
- Rest framework: https://www.django-rest-framework.org/

## Use
`pdfTojpgToText.py` is a class that can be initialized with:
- the PDF file that contains the financial statement of a given company; and
- the language of the file.

### Example
```python
>>>from pdfTojpgToText import pdfTojpgToText
>>>companyA = pdfTojpgToText(filename="application-pdf.pdf", lang="eng")
>>>companyA.processpdf()
>>>companyA.dict
{'line1': 'DUEDIL LIMITED ',
 'line2': 'STATEMENT OF COMPREHENSIVE INCOME ',
 'line3': 'FOR THE YEAR ENDED 31 DECEMBER 2017',
 'line4': '2017 2016',
 'line5': ' £ £',
 'line6': 'Turnover 4101689 2247618',
 'line7': 'Cost of sales  806367 609512',
 'line8': 'Gross profit 3295322 1638106',
 'line9': ' Administrative expenses 8608930 8099728',
 'line10': 'Operating loss  5313608 6461622',
 'line11': 'Interest receivable and similar income   - 2',
 'line12': 'Interest payable and expenses 258398 194217 ¢',
 'line13': 'Loss before tax 5572006 6655837',
 'line14': 'Tax on loss 344676 488126',
 'line15': ' Loss for the financial year 5227330 6167711',
 'line16': 'There was no other comprehensive income for 2017 2016£NIL ',
 'line17': 'The notes on pages 8 to 12 form part of these financial statements',
 'line18': 'Page 6'}
 ```
