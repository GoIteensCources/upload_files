import base64
from app import app


@app.template_filter('to_base64')
def render_image(binary_data):
    base64_data = base64.b64encode(binary_data).decode('utf-8')
    return f"data:image/png;base64,{base64_data}"
