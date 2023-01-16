import os
import subprocess
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from dlclive import benchmark

app = Flask(__name__)

UPLOAD_FOLDER = 'src/static/uploads'
MODEL_FOLDER = 'src/static/models'
RESULT_FOLDER = 'src/static/results'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024

def getModelName():
    result : list[str]= []
    for dir in os.listdir(MODEL_FOLDER):
        path = os.path.join(MODEL_FOLDER, dir)
        if os.path.isdir(path):
            result.append(dir)
    return result

@app.route("/")
def hello_world():
    return render_template('analyse_image.html', models_proposed=getModelName())

@app.route('/', methods=['POST'])
def upload_video():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	else:
		model_path = os.path.join(MODEL_FOLDER, request.form["model"])
		filename = secure_filename(file.filename)
		filename_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(filename_path)  
		benchmark(model_path, filename_path, save_video=True, output=RESULT_FOLDER, pixels=45000)
        #print('upload_video filename: ' + filename)

		result_name = os.path.basename(filename).split(".")[0] + "_DLCLIVE_LABELED"
		subprocess.call(['ffmpeg', '-i', os.path.join(RESULT_FOLDER, result_name + ".avi"), os.path.join(RESULT_FOLDER, result_name + ".mp4")])  

		flash('Video successfully uploaded and displayed below')
		return render_template('analyse_image.html', filename=filename, resultFilename=(result_name + ".mp4"), models_proposed=getModelName())

@app.route('/display_upload/<filename>')
def display_upload_video(filename):
	#print('display_video filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/display_result/<filename>')
def display_result_video(filename):
	#print('display_video filename: ' + filename)
	return redirect(url_for('static', filename='results/' + filename), code=301)