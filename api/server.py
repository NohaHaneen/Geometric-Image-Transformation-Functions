from flask import Flask, flash, request, redirect, url_for, session
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename
import base64
from Transformation import transformation

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'Transformation/Input_Images'

@app.route("/members")
def members():
    return {"members":["Member1","Member2","Member3"]}

@app.route('/upload', methods=['POST'])
def fileUpload():
    # First grab the file
    file = request.files['file']  
    # Then save the file
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
    file.save(file_path) 
    # Read the saved file and convert it to base64 and return base64 as response
    with open(file_path, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string

@app.route('/submit', methods=['POST'])
def executeTransformation():
    param_data = request.json
    return transformation.startTransformation(param_data)
    # perspectiveTransformation.main()
    # print(param_data)
    # return 'yes'

if __name__ == "__main__":
    app.run(debug=True)

CORS(app, expose_headers='Authorization')
