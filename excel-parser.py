from flask import Flask, request, render_template
from converter import ExcelConverter
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
<<<<<<< HEAD
        uploaded_file = request.files['uploadedfile']
        print(f'Files: {request.files}')
        request.files = None
        create_data_viewer(uploaded_file)
        return render_template("parser.handsontable.html")
=======
        cvt = ExcelConverter()
        upload_file = request.files['uploadedfile']
        
        fileName = os.path.splitext(upload_file.filename)[0]
        print(f'Files: {request.files}')
        request.files = None
        HtmlResponse = cvt.create_data_viewer(upload_file,fileName)
        print("can Delete")
        os.remove("templates/"+fileName+".parser.handsontable.html")
        return HtmlResponse
>>>>>>> b902610e9b6178c23993ad243426d7e0423b3337
    return render_template("upload-file.html")


if __name__ == "__main__":
    app.run()