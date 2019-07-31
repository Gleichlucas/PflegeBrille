import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import detect
from flask import jsonify

UPLOAD_FOLDER = "C:\\yolo\\pytorch-yolo-v3\\uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'secret key'
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print("checkpoint 0")
    if request.method == 'POST':
        print("checkpoint 0.1")
        # check if the post request has the file part
        if 'file' not in request.files:
            print("checkpoint 0.1.1")
            flash('No file part')
            return redirect(request.url)
        print("checkpoint 0.2")
        file = request.files['file']
        print("checkpoint 0.3")
        # if user does not select file, browser also
        # submit an empty part without filename
        print("checkpoint 0.4")
        if file.filename == '':
            flash('No selected file')
            print("checkpoint 0.41")
            return redirect(request.url)
        print("checkpoint 0.5")
        if file: #and allowed_file(file.filename):
            print("checkpoint 0.6")
            filename = secure_filename(file.filename)
            print("checkpoint 1")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("checkpoint 2")
            return detect.classify_images()
    return

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=4555, debug=True)
