# http://flask.pocoo.org/docs/1.0/patterns/fileuploads/

from flask import Flask, render_template, request, current_app, url_for
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = r'C:\Users\532975\Documents\Automation\Learn\Python\FlaskTest\Flask_FileUpload\uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		filename = secure_filename(file.filename)
		uploadFolder = current_app.config['UPLOAD_FOLDER']
		file.save(os.path.join(uploadFolder,filename))
		return f'file <b>{filename} </b>uploaded successfully to <b>{uploadFolder}</b>'
		
if __name__ == '__main__':
   app.run(debug = True)