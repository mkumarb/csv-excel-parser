from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import pyexcel
import os 

app = Flask(__name__)

def create_data_viewer(uploadedfile):
    os.remove('templates/parser.handsontable.html')
    csv_extension = 'csv'
    uploadfile_name = ''
    uploadfile_name=secure_filename(uploadedfile.filename)
    uploadedfile.save(uploadfile_name)
    if csv_extension in uploadfile_name.lower():
        print(f'File extension is csv. Hence no sheets to be considered')
        book = pyexcel.get_book(file_name=uploadfile_name)
    else:
        print(f'File extension is not csv. Hence sheets to be considered')
        book = pyexcel.get_book(file_name=uploadfile_name,skip_hidden_sheets=False)
    print(f'File name: {uploadfile_name}')
    book.save_as('templates/parser.handsontable.html',
        readOnly=False,
        js_url='static/utils/handsontable-6.2.2.full.min.js',
        css_url='static/utils/handsontable-6.2.2.full.min.css'
    )
    os.remove(uploadfile_name)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        upload_file = request.files['uploadedfile']
        print(f'Files: {request.files}')
        request.files = None
        create_data_viewer(upload_file)
        return render_template("parser.handsontable.html")
    return render_template("upload-file.html")


if __name__ == "__main__":
    app.run()