import base64
import json
import os
import copy
from io import BytesIO

import requests
from flask import render_template, redirect, request, url_for, flash, send_file, send_from_directory
from werkzeug.utils import secure_filename

from app import app, db
from app.models import UploadModel


@app.route("/")
def index():
    response = requests.get("http://127.0.0.1:5000/mock/api/")
    if response.status_code == 200:
        return render_template("index.html", data=response.json())
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file_load']
        image_file = request.files['image_load']

        filename = secure_filename(image_file.filename)
        print(filename)

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(image_path)
        image_file.save(image_path)

        with open(image_path, 'rb') as f:
            image_data = f.read()

        upload = UploadModel(filename=file.filename,
                             data_file=file.read(),

                             imgname=filename,
                             data_img=image_data
                             )

        db.session.add(upload)
        db.session.commit()
        flash(f'Uploaded: {file.filename} Image: {filename}')

    files = db.session.execute(db.select(UploadModel)).scalars()
    return render_template('upload_file.html',
                           pref=app.config["BASE_DIR"],
                           files=list(files)
                           )


@app.route('/download/<int:upload_id>/')
def download(upload_id):
    file = db.get_or_404(UploadModel, upload_id)
    return send_file(BytesIO(file.data_file),
                     download_name=file.filename,
                     as_attachment=True
                     )


@app.route("/mock/api/")
def mock_api():
    data = {"key": True,
            "group": "GoIteens 36",
            "age": 14}
    return data
