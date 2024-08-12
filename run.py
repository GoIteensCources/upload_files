import os

from app import app

from app.models import *


if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    print(app.url_map)
    app.run()
