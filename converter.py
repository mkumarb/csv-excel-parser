from werkzeug.utils import secure_filename
import os 
import pyexcel

class ExcelConverter():
    def create_data_viewer(self,uploadedfile,fileName):
        print(uploadedfile)
        # os.remove('templates/parser.handsontable.html')
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
        book.save_as('templates/'+fileName+'.parser.handsontable.html',
            readOnly=False,
            js_url='static/utils/handsontable-6.2.2.full.min.js',
            css_url='static/utils/handsontable-6.2.2.full.min.css'
        )
        f = open("templates/"+fileName+".parser.handsontable.html", "r")
        os.remove(uploadfile_name)
        
        return f.read()