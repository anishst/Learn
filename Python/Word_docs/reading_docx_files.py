# https://python-docx.readthedocs.io/en/latest/
from docx import Document

doc = Document('anish.docx')

allText = []
for docpara in doc.paragraphs:
    allText.append(docpara.text)

print(allText)