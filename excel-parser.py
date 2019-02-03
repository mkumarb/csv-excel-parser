from flask import Flask, request, render_template
from converter import ExcelConverter
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        cvt = ExcelConverter()
        upload_file = request.files['uploadedfile']
        
        fileName = os.path.splitext(upload_file.filename)[0]
        print(f'Files: {request.files}')
        request.files = None
        HtmlResponse = cvt.create_data_viewer(upload_file,fileName)
        print("can Delete")
        os.remove("templates/"+fileName+".parser.handsontable.html")
        return HtmlResponse
    return render_template("upload-file.html")


if __name__ == "__main__":
    app.run()