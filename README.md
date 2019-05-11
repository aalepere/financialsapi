# financialsapi

## Purpose of the project
The purpose of this project is to be able to offer financials information via an API.

## Background
Most of the companies in the UK have to publish their financials statements on yearly basis on the company house website. However, those financial statement are available as scanned PDF document.

## Process
As mention above, the finanicals statements are available in scanned PDF fornat; therefore the first step of this project is to OCR those documents to be able to extract both the balance sheet and the P&L. Once this information correctly parse, it will be stored in the database and made externally available through a REST API.

## Stack
In order to complete that project; Tesseract, Django & Rest framework will be used:
- Tesseract: https://github.com/tesseract-ocr/tesseract
- Django: https://www.djangoproject.com/
- Rest framework: https://www.django-rest-framework.org/
