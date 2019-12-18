#https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
# https://pythonhosted.org/PyPDF2/index.html
# https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
# https://automatetheboringstuff.com/chapter13/

import os,sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

# filename = 'Test.pdf'
# filename = r"C:\Users\532975\Downloads\AgencyCIRA-09242019_113727.pdf"

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# //// extract text from PDF doc write to a new file ////
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# infile = PdfFileReader(filename, 'rb')
# output = PdfFileWriter()
# print (infile.getNumPages())
# for i in range(infile.getNumPages()):
#     p = infile.getPage(i)
#     if p.getContents(): # getContents is None if  page is blank
#         output.addPage(p)
# with open('newfile.pdf', 'wb') as f:
#    output.write(f)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# //// extract text from PDF doc print all page contents ////
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# pdf = PdfFileReader(filename, 'rb')
# number_of_pages = pdf.getNumPages()
# search_text = 'From Date:'
# for index in range(0, number_of_pages):
# 	page = pdf.getPage(index)
# 	page_content = page.extractText()
# 	print(page_content)
# 	if search_text in page_content:
# 		print("Found text")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# alt version to loop thru pages using page numbers provided
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# def get_pdf_content(pdf_path, page_nums=[0]):
# 	content = ''
# 	pdf = PdfFileReader(filename, 'rb')
# 	for page_num in page_nums:
# 		content += pdf.getPage(page_num).extractText()
# 	return content
# print(get_pdf_content(filename))


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# //// extract text from PDF doc one page at a time ////
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# read_pdf = PdfFileReader(filename, 'rb')
# number_of_pages = read_pdf.getNumPages()
# page = read_pdf.getPage(35)
# page_content = page.extractText()
# print(page_content)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# //// extract text from PDF doc all pages using loop ////
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# read_pdf = PdfFileReader(filename, 'rb')
# number_of_pages = read_pdf.getNumPages()
# print (number_of_pages)
# print(read_pdf.documentInfo)
# print(read_pdf.getDocumentInfo())
# print(read_pdf.getPageLayout())
# for x in range(0,number_of_pages):
# 	page = read_pdf.getPage(x)
# 	page_content = page.extractText()
# 	print(page_content)
# # 	text = page_content
# # print(text)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# //// Merge PDF docs //// FINAL 4/28/17
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# path = r"C:\Users\532975\Documents\Automation\GitHub\Learn\Python\PDFs"
# filenames = next(os.walk(path))[2]
# # print(filenames)
# merger = PdfFileMerger()
# for filename in filenames:
# 	print(filename)
# 	merger.append(PdfFileReader(filename))
# merger.write(r"MERGED_PDFs.pdf")


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# //// Merge PDF docs //// FINAL 12/5/19
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# from PyPDF2 import PdfFileMerger
# pdfs = ['Moduel 1 certificate.pdf', 'Moduel 2 certificate.pdf','Module3_certificate.pdf', 'Module4 certificate.pdf']
# merger = PdfFileMerger()
# for pdf in pdfs:
#     merger.append(pdf)
# merger.write("result.pdf")
# merger.close()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# //// Merge PDF docs - traverse directory //// FINAL 12/17/19
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
path = r"<your path>"
merger = PdfFileMerger()
files_to_process = ['.pdf']
for root, dirnames, filenames in os.walk(path):
     for file in filenames:
        fileName, ext = os.path.splitext(file)
        if ext.lower() in files_to_process:
            print(f"Processing {file}...")
            merger.append(os.path.join(root,file))
merger.write(os.path.join(root,r"MERGED_PDFs.pdf"))
merger.close()