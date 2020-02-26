import PyPDF2 as p2 

PDFfile = open("License.pdf","rb")
pdfread = p2.PdfFileReader(PDFfile)

x = pdfread.getPage(0)

print(x.extractText())

i = 0

while i < pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i + 1
