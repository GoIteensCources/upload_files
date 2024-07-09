import json
from io import BytesIO

import requests
from flask import render_template, redirect, request, url_for, flash, send_file
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
        file = request.files['file']
        upload = UploadModel(filename=file.filename, data_file=file.read())
        db.session.add(upload)
        db.session.commit()
        flash(f'Uploaded: {file.filename}')

    files = db.session.execute(db.select(UploadModel)).scalars()
    return render_template('upload_file.html', files=files)


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
