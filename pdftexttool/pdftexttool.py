from flask import Flask, request, send_file
import PyPDF2

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <h1>Here to make your life easier.</h1>
    <form method="POST" enctype="multipart/form-data" action="convert">
    <input type="file" name="myfile">
    <input type="submit" value='convert my file'>
    </form>
    

    <form method="POST" enctype="multipart/form-data" action="read">
    <input type="file" name="myfile">
    <input type="submit" value='read in browser'>
    </form>
    
    '''

@app.route('/convert', methods=['POST'])
def convert():
    myfile = request.files['myfile']
    myPDFFile = PyPDF2.PdfFileReader(myfile)

    with open('pdfContent.txt', 'w') as pdf_output:
        for page in range(myPDFFile.getNumPages()):
            data = myPDFFile.getPage(page).extractText()
            pdf_output.write(data)
    f = open('pdfContent.txt', 'rb')

    return send_file(f, attachment_filename='convertedfile.txt', as_attachment=True)
    print("succeeded")




@app.route('/read', methods=['POST'])
def read():
    myfile = request.files['myfile']
    myPDFFile = PyPDF2.PdfFileReader(myfile)

    with open('pdfContent.txt', 'w') as pdf_output:
        for page in range(myPDFFile.getNumPages()):
            data = myPDFFile.getPage(page).extractText()
            pdf_output.write(data)
    f = open('pdfContent.txt', 'rb')

    return send_file(f, attachment_filename='convertedfile.txt')
    print("succeeded")




if __name__ == '__main__':
    app.run(debug=True)