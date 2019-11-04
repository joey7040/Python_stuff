import pypdf as p2 

PDF = open("smallpdf.pdf","rb")
pdf = p2.PdfFileReader(PDFfile)

x = pdfread.getPage(0)

print(x.extractTect())

