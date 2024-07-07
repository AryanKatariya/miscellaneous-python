import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in pdfFiles:
 pdfFileObj = open(filename, 'rb')
 pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
